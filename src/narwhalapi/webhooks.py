"""Local webhook verification. Always verify the exact raw request bytes."""

import hashlib
import hmac
import re
import time
from collections.abc import Mapping
from decimal import InvalidOperation

from ._decode import read_json
from ._generated.models import WebhookEvent, decode_WebhookEvent
from .errors import WebhookVerificationError


def verify(
    raw_body: bytes,
    headers: Mapping[str, str],
    secrets: str | list[str],
    tolerance_seconds: int = 300,
    now: float | None = None,
) -> WebhookEvent:
    """Verify raw bytes; use the resulting event_id for idempotency."""
    keys = [secrets] if isinstance(secrets, str) else secrets
    if not keys or any(not key for key in keys):
        raise ValueError("webhook secrets must not be empty")
    lower = {key.lower(): value for key, value in headers.items()}
    timestamp = lower.get("x-narwhal-timestamp")
    signature = lower.get("x-narwhal-signature")
    if timestamp is None or signature is None:
        raise WebhookVerificationError("missing_header")
    if re.fullmatch(r"[0-9]+", timestamp) is None:
        raise WebhookVerificationError("bad_timestamp")
    current = int(time.time() if now is None else now)
    # Bound parsing as well as comparison, including arbitrarily long timestamps.
    ts = 0
    for start in range(0, len(timestamp), 9):
        chunk = timestamp[start : start + 9]
        ts = ts * 10 ** len(chunk) + int(chunk)
        if ts > current + tolerance_seconds:
            raise WebhookVerificationError("timestamp_out_of_range")
    if abs(current - ts) > tolerance_seconds:
        raise WebhookVerificationError("timestamp_out_of_range")
    message = timestamp.encode() + b"." + raw_body
    expected = [
        hmac.new(key.encode(), message, hashlib.sha256).hexdigest().encode()
        for key in keys
    ]
    matched = False
    for entry in signature.split(","):
        entry = entry.strip()
        if entry.startswith("sha256="):
            candidate = entry[7:].lower().encode()
            for digest in expected:
                matched |= hmac.compare_digest(candidate, digest)
    if not matched:
        raise WebhookVerificationError("no_matching_signature")
    try:
        return decode_WebhookEvent(_with_current_names(read_json(raw_body)))
    except (ValueError, KeyError, TypeError, UnicodeError, InvalidOperation):
        raise WebhookVerificationError("invalid_body") from None


def _with_current_names(body: object) -> object:
    """Queued retries and replays keep the body they were first sent with. A prediction body
    sent before the 22 October 2026 lean contracts names the market `event_id`."""
    if isinstance(body, dict):
        prediction = body.get("prediction")
        if (
            isinstance(prediction, dict)
            and "prediction_event_id" not in prediction
            and "event_id" in prediction
        ):
            body["prediction"] = {
                **prediction,
                "prediction_event_id": prediction["event_id"],
            }
    return body

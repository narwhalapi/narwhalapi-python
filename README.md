# Narwhal API for Python

Typed synchronous and asynchronous clients for economics (including the equity risk premium), foreign exchange, calendars,
stocks, funds, crypto, company calendars, company filings and financials, physical palm oil, physical commodity reference prices, spot gold and silver, prediction markets, FX and commodity bar history, and webhook delivery. Python 3.10 or newer. Install with `pip install narwhalapi`.

Set `NARWHAL_API_KEY` in the environment. Keep keys on the server. The default base URL is
`https://api.narwhalapi.com`; override it with `NARWHAL_BASE_URL` or `base_url=`.

## Quickstart

```pycon
>>> from decimal import Decimal
>>> from narwhalapi import Narwhal
>>> with Narwhal() as nw:
...     cpi = nw.economics.cpi("USA")
...     rates = nw.fx.rates("USD", currencies=["EUR", "JPY"])
...     days = list(nw.fx.rate_history_iter(
...         "USD", currencies=["EUR"], start_date="2026-08-20", end_date="2026-08-24"
...     ))
>>> isinstance(cpi.value, Decimal)
True
>>> isinstance(rates.rates[0].rate, Decimal)
True
>>> all(isinstance(rate.rate, Decimal) for day in days for rate in day.rates)
True

```

Decimals remain exact `Decimal` values. Use `format(value, "f")` to display fixed-point
wire text, including very small values. Decimal inputs accept `Decimal` or `str`;
other numeric types raise `TypeError`. Responses accept only decimal strings matching
`^-?\d+(\.\d+)?$` with ASCII digits. Dates and timestamps remain strings.

```python
from narwhalapi import AsyncNarwhal, errors

async def load_rates():
    async with AsyncNarwhal() as nw:
        try:
            return await nw.fx.rates("USD", currencies=["IDR", "SGD"])
        except errors.RateLimited as error:
            if error.is_quota_exhausted:
                return None
            raise
```

Share a synchronous client across threads. Use one async client per event loop.
Context managers close connections; explicit `close()` and `await aclose()` also work.

## Operations and types

Namespaces are `economics`, `fx`, `calendars`, `commodities`, `equities`, `funds`, `crypto`,
`company_calendars`, `filings`, `predictions`, `events`, `webhooks`, and
`calendar_subscriptions`. Operations not yet in the live API appear under `nw.unstable`;
there are none today.
Models and known string constants are available through `narwhalapi.models`,
for example `from narwhalapi.models import Cpi`.
Unknown enum strings are retained. Union variants are frozen dataclasses with a `kind`;
its `kind` is the variant model name (for example `PalmoilSchedulePrice`).
An unknown variant has `kind="unknown"` and keeps its JSON in `raw`.
New response fields are ignored.

Required path arguments may be positional. Query and body arguments are keyword-only:

```python
nw.fx.convert_currency(from_="USD", to="IDR", amount="100.00")
nw.fx.rate_history("USD", currencies=["IDR"], start_date="2026-01-01", end_date="2026-01-31")
spot = nw.commodities.spot_price("XAU", "USD")
nw.webhooks.update_destination(
    "destination-id", url="https://example.test/webhook",
    countries=["IDN"], families=["prices"], enabled=False,
)
feed_url = nw.calendar_subscriptions.feed_url("subscription-token")
```

Updates require `enabled` explicitly. Creation sends only supplied fields; omitted fields
and explicit `None` remain distinct in request bodies. `feed_url()` makes no request.
Lists use the documented repeated or comma-joined encoding. Scalar strings, empty list
items and items containing commas are rejected for list query parameters.

Every paginated operation has an `_iter` method, yielding items lazily (use `async for`
with an async client). Filters persist across pages; `limit` is the page size. Cursor expiry
raises `errors.CursorExpired`, including after earlier items were yielded.

Top-level `meta` contains optional `request_id`, `quota`, and `short` values from response
headers. Each rate limit has optional `limit`, `remaining`, and `reset` fields.

## Failures and retries

All client failures inherit `errors.NarwhalError`. `errors.ApiError` exposes `status`,
`code`, `title`, `detail`, `request_id`, `instance`, `retry_after`, and `raw_body` bytes.
Typed subclasses cover common statuses and cursor expiry. Known codes are exported as
uppercase constants in `narwhalapi.codes`; codes also accept future strings.
`TransportError.cause` preserves the underlying error. `DecodeError.raw_body` keeps an
invalid success response as the original bytes. Import exceptions directly, for example
`from narwhalapi.errors import RateLimited`. API errors display server fields as
`HTTP <status> <code>: <title> (request_id <id>)`. All SDK errors support pickling.
Client representations exclude credentials.

Defaults are a 30-second attempt timeout, a 10-second connect timeout, two retries, and a
30-second maximum retry wait. Only short-window 429s retry on any method. A 503 retries
on GET; a transport failure retries on GET only before any response. Monthly quota
exhaustion never retries. Redirects are not followed.
Use `max_retries=0` to disable retries. Both clients honor standard proxy and certificate
environment variables, including `HTTPS_PROXY` and `SSL_CERT_FILE`; supply `proxy=`
to select an explicit proxy. `extra_headers` cannot replace Authorization.
The `transport`, `clock`, `sleep`, and `random_fraction` constructor options support tests;
async `sleep` must be awaitable.

## Webhooks

`from narwhalapi.webhooks import verify` verifies **exact raw bytes** before decoding.
It accepts a nonempty secret string or a nonempty list of nonempty secrets during
rotation. Empty secrets raise `ValueError` before verification. Timestamp tolerance is
300 seconds by default. Use the returned `event_id` as the idempotency key and store it
before applying the event. Future schema versions still decode.

FastAPI:

```python
raw_body = await request.body()
event = verify(raw_body, request.headers, webhook_secret)
```

Flask:

```python
raw_body = request.get_data(cache=True)
event = verify(raw_body, request.headers, webhook_secret)
```

Do not parse and re-serialize the body before verification. A verification failure raises
`errors.WebhookVerificationError` with a `reason`. Neither framework is a package dependency.

## Links

- https://narwhalapi.com/
- https://narwhalapi.com/docs
- https://narwhalapi.com/pricing
- https://narwhalapi.com/compare/economic-data-apis
- https://narwhalapi.com/commodities/gold
- https://narwhalapi.com/economics/united-states

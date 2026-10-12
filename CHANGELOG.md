# Changelog

## 0.2.0 — 2026-10-12

- Breaking: economic calendar releases now carry Narwhal's English `name`, a permanent
  `series_id`, a `topic` and a `stage` beside the publisher's `title`, and each schedule
  carries its `local_date`. The API lists releases compactly by default; the SDK always asks
  for the full release (`view=full`), so every field stays typed. Research articles are no
  longer listed.
- `CALENDAR_NOT_PUBLISHED` for the 404 returned when a holiday calendar year is not published.
- FX bars publish their five fields again in the contract (no wire change).

## 0.1.0 — 2026-10-09

- Initial typed synchronous and asynchronous clients for the stable API: economics,
  FX, calendars, physical palm oil, spot prices (`commodities.spot_price`), events,
  webhook destinations and calendar subscriptions.
- `nw.unstable` holds operations not yet in the live API; it is empty in this release.
- Exact decimals, typed errors, bounded retries, page iterators, response metadata,
  and local webhook signature verification.
- `codes.PLAN_UPGRADE_REQUIRED` for the 403 returned when a request reaches before the
  plan's history window.
- The release also covers prediction market reads, FX and commodity bar history, and physical commodity reference price series.
- Spot `bid` and `ask` are optional because the API may omit them.

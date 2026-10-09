# Changelog

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

# Changelog

## 0.5.0 — 2026-10-29

Breaking: FX bar prices are `Decimal` values now.
New: stocks, funds, crypto, company calendars, central banks, the Filings API and custom series.

- FX bars: `FxBar.open`, `high`, `low` and `close` are `Decimal` instead of `str`, like every
  other price in the SDK.
  Migrate: `Decimal(bar.close)` still works; use `str(bar.close)` where text is needed.
- History reads: the economics `*_history` methods (`cpi_history`, `gdp_history`,
  `gdp_growth_history`, `inflation_history`, `labour_force_participation_history`,
  `unemployment_history`, `trade_history`) take optional `as_of` and `version`;
  `yield_curve_history` takes `as_of` only. Observation rows have an optional
  `first_reported_at`, and `ResourceHistory` has an optional `as_of`.
- Financials: `FinancialRow.items` skips null item values instead of failing the response.
- Docs: GDP growth `quarter_over_quarter` says it is not annualized. Paged responses say
  `next_cursor` is always sent and is `None` on the last page. Holiday years are 1900-2200.
  Calendar subscription methods list their 401, 404, 429 and 503 errors.
- Stocks: `client.equities` reads prices (`price`, `prices`), daily bars (`bars`), profiles,
  dividends, splits, earnings, valuation and its history, movers, search and cost of capital.
  US listings on NYSE, Nasdaq and NYSE American, and Korea. Ids look like `XNAS:AAPL`.
- Funds: `client.funds` reads ETF prices and mutual fund NAVs (`price`, `prices`), bars,
  profiles, distributions and search. `price` answers an ETF or a mutual fund NAV, told apart
  by `type`.
- Crypto: `client.crypto` reads pair prices (`price`, `prices`), bars and the pair list
  (`list_pairs`).
- Company calendars: `client.company_calendars` lists upcoming `dividends` and `splits`.
- Central banks: `economics` reads policy rates (`policy_rate`, `policy_rate_history`), central
  bank balance sheets (`central_bank_balance_sheet`) and reserves (`central_bank_reserves`). A
  policy rate is a point rate (`PointPolicyRate`) or a target range (`RangePolicyRate`).
- Equity risk premium: `economics` reads the premium investors need for a country's shares
  (Free plan): `list_equity_risk_premium` for every country, `get_equity_risk_premium` for one
  country (optional `date`) and `equity_risk_premium_history` (with `equity_risk_premium_history_iter`).
  `EquityRiskPremium` splits `total_erp` into `mature_erp` and `country_risk_premium`, all in
  percent as `Decimal`, with a `basis` for each part.
- Companies: `filings.company` returns `CompanyWithListings`, a company with the stock listing
  ids (`listings`) you can pass to `client.equities`.
- Filings API: `client.filings` (and `AsyncNarwhal`) reads company financials, filings,
  holders and as-reported statements: `search_companies`, `company`, `financials`,
  `list_company_filings`, `filing`, `list_latest_filings`, `list_holders` and `as_reported`.
  Every money, share, percent and ratio value is a `Decimal` with the exact wire text.
  A `FinancialRow` holds its period fields (`fy`, `fq`, `fh`, `end`, `currency`, `derived`) and
  all financial items in `row.items`, a `dict[str, Decimal]` such as `row.items["revenue"]`.
- Custom series: `economics` can search the series catalogue (`search_catalogue`), read one series
  (`read_catalogue_series`), its observations (`read_catalogue_observations`) and the latest value
  of several at once (`read_catalogue_latest_batch`). Series ids look like `fred:unrate`.
  `read_series_observations` also takes `as_of` and `version` (Pro plan).
- Registries: filings cover 31 registries (`usa`, `jpn`, `kor`, `twn`, `gbr` and 26 EU and EEA
  countries). The UK is covered for UK issuers on regulated markets (annual reports), and `gbr`
  company ids are LEIs, for example `gbr:549300MKFYEKVRWML317`. Taiwan includes TPEx issuers
  (listing MIC `ROCO`) besides `XTAI`.
- Taiwan: filings accept `period="semiannual"`. Taiwan reports semiannual year-to-date income
  statements and balance sheets.
- As-reported statements are available for US filings only; other registries answer
  `as_reported_unavailable` (404).
- Webhooks: the new `filings` family and the `companies` watch list on destinations;
  deliveries for it carry a `filing` record (`FilingWebhookEvent`).

## 0.4.0 — 2026-10-22

Breaking: 0.3.x fails on calls changed by the API contracts of 21-22 October 2026.
Upgrade to 0.4.0 for these calls. 0.4.0 fails against gateways using the old response
formats. Fields the API omits when empty are now optional (`None`). Lists are always present.

- Trade: the four separate export and import methods are removed (`economics.trade_exports`,
  `trade_exports_history`, `trade_imports`, `trade_imports_history`). Their routes no longer
  exist. `economics.trade` and `economics.trade_history` return exports and imports in one
  row. The models `TradeExports`, `TradeImports` and `TradeProductFilter` are removed, and
  `TradeSummary` has no `coverage`.
  Migrate: call the combined methods and read `exports` and `imports` from the row.
- Economics series: `Cpi` has an `index_base` string instead of `base_period` and
  `base_value`. `Inflation`, `Unemployment` and `LabourForceParticipation` have no `unit`.
  `SeriesSource` has no `released_on_basis`.
  Migrate: read `index_base`; drop reads of `unit`.
- GDP: `Gdp` drops `seasonal_adjustment`, `annualization` and `price_basis`. `GdpGrowth` drops
  `seasonal_adjustment`, `quarter_over_quarter_seasonal_adjustment`,
  `year_over_year_seasonal_adjustment`, `annualization`, `price_basis` and `unit`. The
  optional flags `annualized` and `not_seasonally_adjusted` (and, on growth,
  `quarter_over_quarter_not_seasonally_adjusted` and `year_over_year_not_seasonally_adjusted`)
  are present only when true.
  Migrate: treat a missing flag as false.
- Economics history: `HistoricalEconomicsResponse` and `HistoricalObservation` are removed.
  Each indicator has its own response type (`CpiHistory`, `GdpHistory`, `GdpGrowthHistory`,
  `InflationHistory`, `RateHistory`, `TradeHistory`) with matching `...Observation` rows.
  Rows contain only `period` and `value` (trade rows hold `exports` and `imports`).
  Migrate: use the new response and observation types.
- Economic calendar: `EconomicRelease` is replaced by `EconomicReleaseSummary` (lists) and
  `EconomicReleaseDetail` (`economics.get_release`). `indicators` is now `values`
  (`EconomicReleaseValue`). The `EconomicReleaseIndicator` and `EconomicReleaseSchedule`
  models are removed. The schedule now uses the flat fields `at`, `date`, `between` and `by`.
  `reference_period` is renamed to `period`. `title`, `variant` and `officially_published_at`
  are removed. `EconomicCalendar` has no `as_of`, `snapshot` or `status`. `between` is a list
  of two dates.
  Migrate: read the flat schedule fields and `values`.
- Holidays: `CalendarHolidays.year`, `CalendarHolidaysOnDate.date`,
  `CalendarNextHoliday.from_date`, `nationwide` (on coverage and holidays) and
  `TopicCalendar.variant` are removed.
  Migrate: use the values from your request.
- FX and commodities: `FxConversion` has no `amount`. `FxHistory` has no `has_more`; its
  `start_date` and `end_date` are optional. `FxBars` and `CommodityBars` have no `interval`,
  and `start` and `end` appear only when the range was clipped. `Quote.role` is removed.
  `PhysicalSeries` has `country` and no `market` or `publisher`; its list call has no `market`
  parameter. `attribution` is now required on `PhysicalSeries`, `PhysicalLatest` and
  `PhysicalObservations`.
  Migrate: use the amount you sent; filter series by country.
- Palm oil: `PalmoilScalarSeries.commodity`, `PalmoilScheduleSeries.commodity` and
  `PalmoilScheduleSeries.producer_type` are removed.
  Migrate: remove reads of these fields.
- Prediction event fields: events no longer have `body`, `quality` or `shape`. The models
  `BinaryBody`, `ScalarBody`, `ExtremeBody`, `TimingBody`, `PredictionQuality`,
  `PredictionResolution`, `ScalarSummary` and `ScalarSummaryBounds` are removed. Each event
  type carries its own fields: binary `probability`, `quotes`, `labels`; scalar `median`,
  `p10`, `p90`, `above`, `outcomes`; extreme `up`, `down`, `observation`, `window`; timing
  `steps`, `not_within_window`. All have `resolves_with` and `stale`. `resolution` is now a
  plain string instead of an object with `description` and `resolves_with`.
  Migrate: read event fields directly; use `resolves_with` for `resolution.resolves_with`.
- Prediction venues, lists and history: `PredictionVenue` has no `role`, `venue_event_id`,
  `depth_usd` or `fetched_at`. `settlement` is now an optional string instead of an object
  with `status`. The `VenueSettlement` model is removed. `match` is optional.
  `PredictionEventSummary` has no `as_of`. `PredictionTopicDetail.events` is a list of the new
  `PredictionTopicEvent` (no `topic_id` or `shape`). `next_event_id` is removed.
  `PredictionHistory` has no `event_id`, `shape`, `interval`, `start` or `captured_from`, and
  `end` is optional. `PredictionBar` has `timestamp` instead of `start` and `end`.
  `PolicyPath` and `PolicyPathHistory` have no `authority`, `method` or `unit`; the history
  has `meeting_dates` (`PolicyPathMeetingDate`), and `PolicyPathDay.meetings` is a list of the
  new `PolicyPathOdds` (no `resolves_at`). `PredictionWebhookEvent.event_id` is
  `prediction_event_id`.
  Migrate: use the new types and read the settlement string directly.
- Prediction results: events and event summaries now include `result` (`PredictionResult`)
  with `final`, `settled_at`, `amended_at` and the settled `markets` for each venue.
  `unavailable` is sent for each venue only when true.
  Migrate: read results from events or event summaries.
- Events and webhooks: `EventDetail` is now the event itself, with no `event` wrapper or
  `status`. `EventsPage` has no `status`. `DeliveryEvent` has no `event_type`,
  `schema_version`, `publication_id` or `holiday_country`. `WebhookEvent` has no `is_test`,
  `publication_id` or `holiday_country`. Test deliveries use the event type `webhook.test`.
  The webhook verifier accepts both new bodies with null fields omitted and old bodies. For
  old prediction bodies whose market is named `event_id`, it fills `prediction_event_id`.
  Migrate: read event fields directly; check `type` instead of `is_test`.
- Webhook records: `WebhookConfigurationHistory` renames `version` to `config_version` and
  removes `destination_id` and `activation_snapshot`. `WebhookDestinationList.limit` is renamed
  to `destination_limit`. `WebhookDeliveriesResponse` has no `limit`.
  `WebhookDelivery.next_attempt_at`, `retry_until` and `replays` are optional.
  `WebhookTestResponse` has no `destination_id`. `CalendarSubscriptionCreated` has no
  `refresh_note`.
  Migrate: rename the fields; handle missing values.
- No-content responses: `webhooks.delete_destination`, `webhooks.replay_delivery` and
  `calendar_subscriptions.revoke` respond with `204` and return an empty `NoContent` object.
  The models `WebhookDeleteResponse`, `WebhookReplayResponse` and
  `CalendarSubscriptionRevoked` are removed.
  Migrate: stop reading `deleted`, `replayed` and `revoked`; success means no error.
- Errors: `Problem` has no `instance` or `ok`.
  Migrate: remove reads of these fields.
- Calendar `view`: the SDK no longer offers or sends this parameter. The API ignores it. Lists
  always contain the full release.
  Migrate: no changes needed.
- Enums removed with their fields: `Annualization`, `CentralBank`,
  `GrowthSeasonalAdjustment`, `IndicatorValueStatus`, `PredictionInterval`, `QuoteFreshness`,
  `QuoteRole`, `SchedulePrecision`, `ScheduleTimeBasis`, `SeasonalAdjustment`, `ValueScale`,
  `ValueTransformation`. New: `EconomicReleaseValueValueStatus`, `PredictionVenueSettlement`,
  `ScalarEventAbove`.
  Migrate: remove references to the removed enums.
- README lists the product's key pages as full URLs.

## 0.3.0 — 2026-10-18

- Breaking: `webhooks.verify` now returns a `WebhookEvent`, read from the delivery bodies the
  API documents. 0.2.0 read deliveries as the REST `DeliveryEvent`, which needs an `event_type`
  field that webhook bodies never carry, so it rejected real deliveries with `invalid_body`.
  `WebhookEvent` reads economics, release calendar and holiday events, prediction events
  (`prediction`, with the event status and venue settlements) and test deliveries (`is_test`,
  no `cursor`). Unknown event types still decode, with the type kept as a string.
- `economics.read_series_observations(series_id, ...)` reads the observations of one economic
  series by its id, with a page iterator (`read_series_observations_iter`).
- Prediction history (`binary_history`, `scalar_history`, `extreme_history`, `timing_history`)
  now comes in pages of about 5,000 bars with a `next_cursor`. Pass `cursor`, or use the new
  `…_iter` iterators, to read a whole window; each page repeats the series keys with the next
  slice of bars. The API pages these responses for every version, so 0.2.0 sees only the first
  page of a wide window.
- Webhook destinations carry `disabled_reason`: `customer` (switched off by the account),
  `plan_limit` (paused because the plan no longer includes it) or none.
- New code constants for the documented errors: `SNAPSHOT_UNAVAILABLE`, `REQUEST_TOO_LARGE`,
  `RIGHTS_STATE_CHANGING`, `COMMAND_UNAVAILABLE`, `PHYSICAL_SERIES_NOT_FOUND`,
  `PHYSICAL_REFERENCE_UNAVAILABLE`, `EVENT_NOT_FOUND`, `PREDICTIONS_UNAVAILABLE` and
  `LIMIT_REACHED`.
- No change on the wire: the contract now names the palm oil price unions and the shared
  problem response, and documents `400` instead of `422` for webhook and calendar subscription
  validation errors, which is what the API always returned.

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

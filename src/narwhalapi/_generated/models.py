# Generated from spec/live/openapi.json sha256 ba06d620d3f1f03774f3f30363a59e00f14ab7cde053c552d2164ad83a9ea678. Do not edit.
# Generated from spec/next/openapi.json sha256 ba06d620d3f1f03774f3f30363a59e00f14ab7cde053c552d2164ad83a9ea678. Do not edit.
from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import ClassVar, Literal, TypeAlias

from .._decode import (
    read_bool,
    read_cursor,
    read_decimal,
    read_int,
    read_list,
    read_object,
    read_str,
)
from .._meta import ResponseMeta


@dataclass(frozen=True, slots=True)
class _PalmoilHistory:
    pass


@dataclass(frozen=True, slots=True)
class _PalmoilObservation:
    pass


@dataclass(frozen=True, slots=True)
class _PalmoilPrice:
    pass


@dataclass(frozen=True, slots=True)
class _PalmoilSeries:
    pass


class BarInterval:
    """Known values; response fields also accept future strings."""

    V15M: Literal["15m"] = "15m"
    V1D: Literal["1d"] = "1d"
    V1H: Literal["1h"] = "1h"
    V1M: Literal["1m"] = "1m"
    V4H: Literal["4h"] = "4h"
    V5M: Literal["5m"] = "5m"


class CommodityUnit:
    """Known values; response fields also accept future strings."""

    BARREL: Literal["barrel"] = "barrel"
    POUND: Literal["pound"] = "pound"
    TROY_OUNCE: Literal["troy_ounce"] = "troy_ounce"


class DeliveryFamily:
    """Known values; response fields also accept future strings."""

    ACTIVITY: Literal["activity"] = "activity"
    GDP: Literal["gdp"] = "gdp"
    HOLIDAYS: Literal["holidays"] = "holidays"
    HOUSING: Literal["housing"] = "housing"
    LABOUR: Literal["labour"] = "labour"
    MONEY: Literal["money"] = "money"
    POLICY_RATE: Literal["policy_rate"] = "policy_rate"
    PRICES: Literal["prices"] = "prices"
    PUBLIC_FINANCE: Literal["public_finance"] = "public_finance"
    SURVEY: Literal["survey"] = "survey"
    TRADE: Literal["trade"] = "trade"
    YIELD_CURVE: Literal["yield_curve"] = "yield_curve"


class EconomicFamily:
    """Known values; response fields also accept future strings."""

    ACTIVITY: Literal["activity"] = "activity"
    GDP: Literal["gdp"] = "gdp"
    HOUSING: Literal["housing"] = "housing"
    LABOUR: Literal["labour"] = "labour"
    MONEY: Literal["money"] = "money"
    POLICY_RATE: Literal["policy_rate"] = "policy_rate"
    PRICES: Literal["prices"] = "prices"
    PUBLIC_FINANCE: Literal["public_finance"] = "public_finance"
    SURVEY: Literal["survey"] = "survey"
    TRADE: Literal["trade"] = "trade"
    YIELD_CURVE: Literal["yield_curve"] = "yield_curve"


class EconomicReleaseValueValueStatus:
    """Known values; response fields also accept future strings."""

    PENDING_CAPTURE: Literal["pending_capture"] = "pending_capture"
    UNAVAILABLE: Literal["unavailable"] = "unavailable"


class ExtremeObservation:
    """Known values; response fields also accept future strings."""

    ANY_RELEASE: Literal["any_release"] = "any_release"
    ANY_TRADE: Literal["any_trade"] = "any_trade"
    CLOSE: Literal["close"] = "close"


class HolidayScope:
    """Known values; response fields also accept future strings."""

    BANK: Literal["bank"] = "bank"
    CENTRAL_GOVERNMENT: Literal["central_government"] = "central_government"
    COLLECTIVE_LEAVE: Literal["collective_leave"] = "collective_leave"
    FEDERAL_GOVERNMENT: Literal["federal_government"] = "federal_government"
    NATIONAL_PUBLIC: Literal["national_public"] = "national_public"
    PRIVATE_SECTOR: Literal["private_sector"] = "private_sector"
    PUBLIC_SECTOR: Literal["public_sector"] = "public_sector"
    REGIONAL_PUBLIC: Literal["regional_public"] = "regional_public"


class IndicatorUnit:
    """Known values; response fields also accept future strings."""

    BALANCE: Literal["balance"] = "balance"
    CURRENCY: Literal["currency"] = "currency"
    INDEX: Literal["index"] = "index"
    PERCENT: Literal["percent"] = "percent"
    RATIO: Literal["ratio"] = "ratio"
    THOUSANDS: Literal["thousands"] = "thousands"


class MarketSession:
    """Known values; response fields also accept future strings."""

    INTERBANK_CLOSED: Literal["interbank_closed"] = "interbank_closed"
    OPEN: Literal["open"] = "open"
    WEEKEND: Literal["weekend"] = "weekend"


class PalmoilFrequency:
    """Known values; response fields also accept future strings."""

    DAILY: Literal["daily"] = "daily"
    FORTNIGHTLY: Literal["fortnightly"] = "fortnightly"
    IRREGULAR: Literal["irregular"] = "irregular"
    MONTHLY: Literal["monthly"] = "monthly"
    WEEKLY: Literal["weekly"] = "weekly"


class PalmoilPeriodType:
    """Known values; response fields also accept future strings."""

    EFFECTIVE: Literal["effective"] = "effective"
    OBSERVATION: Literal["observation"] = "observation"


class PalmoilPriceType:
    """Known values; response fields also accept future strings."""

    GOVERNMENT_REFERENCE: Literal["government_reference"] = "government_reference"
    MARKET_AVERAGE: Literal["market_average"] = "market_average"
    OFFICIAL_PURCHASE_SCHEDULE: Literal["official_purchase_schedule"] = (
        "official_purchase_schedule"
    )


class PalmoilProduct:
    """Known values; response fields also accept future strings."""

    CPO: Literal["cpo"] = "cpo"
    FFB: Literal["ffb"] = "ffb"


class PalmoilScalarPriceType:
    """Known values; response fields also accept future strings."""

    GOVERNMENT_REFERENCE: Literal["government_reference"] = "government_reference"
    MARKET_AVERAGE: Literal["market_average"] = "market_average"


class PalmoilScalarUnit:
    """Known values; response fields also accept future strings."""

    METRIC_TON: Literal["metric_ton"] = "metric_ton"
    ONE_PERCENT_OER: Literal["one_percent_oer"] = "one_percent_oer"


class PhysicalCategory:
    """Known values; response fields also accept future strings."""

    EMISSIONS: Literal["emissions"] = "emissions"
    ENERGY: Literal["energy"] = "energy"
    FERTILIZERS: Literal["fertilizers"] = "fertilizers"
    FORESTRY: Literal["forestry"] = "forestry"
    GRAINS: Literal["grains"] = "grains"
    LIVESTOCK_DAIRY: Literal["livestock-dairy"] = "livestock-dairy"
    METALS: Literal["metals"] = "metals"
    OILS_OILSEEDS: Literal["oils-oilseeds"] = "oils-oilseeds"
    SOFTS: Literal["softs"] = "softs"


class PhysicalFrequency:
    """Known values; response fields also accept future strings."""

    ANNUAL: Literal["annual"] = "annual"
    DAILY: Literal["daily"] = "daily"
    INTRADAY: Literal["intraday"] = "intraday"
    IRREGULAR: Literal["irregular"] = "irregular"
    MONTHLY: Literal["monthly"] = "monthly"
    QUARTERLY: Literal["quarterly"] = "quarterly"
    SEMIANNUAL: Literal["semiannual"] = "semiannual"
    THREE_TIMES_MONTHLY: Literal["three_times_monthly"] = "three_times_monthly"
    TWICE_MONTHLY: Literal["twice_monthly"] = "twice_monthly"
    WEEKLY: Literal["weekly"] = "weekly"


class PhysicalPriceType:
    """Known values; response fields also accept future strings."""

    AUCTION_CLEARING: Literal["auction_clearing"] = "auction_clearing"
    EXPORT_UNIT_VALUE: Literal["export_unit_value"] = "export_unit_value"
    FARMGATE_AVERAGE: Literal["farmgate_average"] = "farmgate_average"
    GOVERNMENT_REFERENCE: Literal["government_reference"] = "government_reference"
    IMPORT_UNIT_VALUE: Literal["import_unit_value"] = "import_unit_value"
    INTERNATIONAL_BENCHMARK: Literal["international_benchmark"] = (
        "international_benchmark"
    )
    MARKET_AVERAGE: Literal["market_average"] = "market_average"
    OFFICIAL_BUY: Literal["official_buy"] = "official_buy"
    OFFICIAL_REFERENCE_RATE: Literal["official_reference_rate"] = (
        "official_reference_rate"
    )
    OFFICIAL_SELL: Literal["official_sell"] = "official_sell"
    REGULATED_AVERAGE: Literal["regulated_average"] = "regulated_average"
    RETAIL_AVERAGE: Literal["retail_average"] = "retail_average"
    RETAIL_BUY: Literal["retail_buy"] = "retail_buy"
    RETAIL_SELL: Literal["retail_sell"] = "retail_sell"
    WHOLESALE_AVERAGE: Literal["wholesale_average"] = "wholesale_average"


class PredictionEventStatus:
    """Known values; response fields also accept future strings."""

    CLOSED: Literal["closed"] = "closed"
    SETTLED: Literal["settled"] = "settled"
    TRADING: Literal["trading"] = "trading"
    UPCOMING: Literal["upcoming"] = "upcoming"
    VOID: Literal["void"] = "void"


class PredictionShape:
    """Known values; response fields also accept future strings."""

    BINARY: Literal["binary"] = "binary"
    CATEGORICAL: Literal["categorical"] = "categorical"
    EXTREME: Literal["extreme"] = "extreme"
    SCALAR: Literal["scalar"] = "scalar"
    SET: Literal["set"] = "set"
    TIMING: Literal["timing"] = "timing"


class PredictionVenueSettlement:
    """Known values; response fields also accept future strings."""

    SETTLED: Literal["settled"] = "settled"
    VOID: Literal["void"] = "void"


class PredictionWebhookStatus:
    """Known values; response fields also accept future strings."""

    CLOSED: Literal["closed"] = "closed"
    SETTLED: Literal["settled"] = "settled"
    VOID: Literal["void"] = "void"


class ProducerArrangement:
    """Known values; response fields also accept future strings."""

    PURCHASE_AGREEMENT: Literal["purchase_agreement"] = "purchase_agreement"
    SUPPORTED_SCHEME: Literal["supported_scheme"] = "supported_scheme"


class ReleaseStage:
    """Known values; response fields also accept future strings."""

    ADVANCE: Literal["advance"] = "advance"
    FINAL: Literal["final"] = "final"
    FIRST: Literal["first"] = "first"
    FLASH: Literal["flash"] = "flash"
    PRELIMINARY: Literal["preliminary"] = "preliminary"
    SECOND: Literal["second"] = "second"
    THIRD: Literal["third"] = "third"


class ReleaseStatus:
    """Known values; response fields also accept future strings."""

    CANCELLED: Literal["cancelled"] = "cancelled"
    PUBLISHED: Literal["published"] = "published"
    SCHEDULED: Literal["scheduled"] = "scheduled"


class ReleaseTopic:
    """Known values; response fields also accept future strings."""

    BALANCE_OF_PAYMENTS: Literal["balance_of_payments"] = "balance_of_payments"
    BUSINESS_CONFIDENCE: Literal["business_confidence"] = "business_confidence"
    CONSTRUCTION: Literal["construction"] = "construction"
    CONSUMER_CONFIDENCE: Literal["consumer_confidence"] = "consumer_confidence"
    CONSUMER_PRICES: Literal["consumer_prices"] = "consumer_prices"
    EMPLOYMENT: Literal["employment"] = "employment"
    ENERGY: Literal["energy"] = "energy"
    GDP: Literal["gdp"] = "gdp"
    HOME_SALES: Literal["home_sales"] = "home_sales"
    HOUSE_PRICES: Literal["house_prices"] = "house_prices"
    HOUSEHOLD_SPENDING: Literal["household_spending"] = "household_spending"
    HOUSING_CONSTRUCTION: Literal["housing_construction"] = "housing_construction"
    IMPORT_EXPORT_PRICES: Literal["import_export_prices"] = "import_export_prices"
    INDUSTRIAL_PRODUCTION: Literal["industrial_production"] = "industrial_production"
    INVESTMENT: Literal["investment"] = "investment"
    JOBLESS_CLAIMS: Literal["jobless_claims"] = "jobless_claims"
    LABOUR_FORCE: Literal["labour_force"] = "labour_force"
    MANUFACTURING: Literal["manufacturing"] = "manufacturing"
    MERCHANDISE_TRADE: Literal["merchandise_trade"] = "merchandise_trade"
    MONEY_CREDIT: Literal["money_credit"] = "money_credit"
    OTHER: Literal["other"] = "other"
    POLICY_COMMUNICATION: Literal["policy_communication"] = "policy_communication"
    POLICY_MINUTES: Literal["policy_minutes"] = "policy_minutes"
    POLICY_RATE: Literal["policy_rate"] = "policy_rate"
    PRODUCER_PRICES: Literal["producer_prices"] = "producer_prices"
    PUBLIC_FINANCE: Literal["public_finance"] = "public_finance"
    RETAIL_SALES: Literal["retail_sales"] = "retail_sales"
    SERVICES: Literal["services"] = "services"
    TOURISM: Literal["tourism"] = "tourism"
    WAGES: Literal["wages"] = "wages"
    WHOLESALE_TRADE: Literal["wholesale_trade"] = "wholesale_trade"


class ResolutionKind:
    """Known values; response fields also accept future strings."""

    OCCURRENCE: Literal["occurrence"] = "occurrence"
    PRICE_FIX: Literal["price_fix"] = "price_fix"
    PRICE_WINDOW: Literal["price_window"] = "price_window"
    RELEASE: Literal["release"] = "release"


class ResourceObservationStatus:
    """Known values; response fields also accept future strings."""

    BREAK_IN_SERIES: Literal["break_in_series"] = "break_in_series"
    BREAK_IN_SERIES_AND_DEFINITION_DIFFERS: Literal[
        "break_in_series_and_definition_differs"
    ] = "break_in_series_and_definition_differs"
    DEFINITION_DIFFERS: Literal["definition_differs"] = "definition_differs"
    ESTIMATED: Literal["estimated"] = "estimated"
    PROVISIONAL: Literal["provisional"] = "provisional"


class ResourceUnit:
    """Known values; response fields also accept future strings."""

    CURRENCY: Literal["currency"] = "currency"
    CURRENCY_PER_HOUR: Literal["currency_per_hour"] = "currency_per_hour"
    CURRENCY_PER_MONTH: Literal["currency_per_month"] = "currency_per_month"
    CURRENCY_PER_WEEK: Literal["currency_per_week"] = "currency_per_week"
    CURRENCY_PER_YEAR: Literal["currency_per_year"] = "currency_per_year"
    INDEX: Literal["index"] = "index"
    JOB: Literal["job"] = "job"
    PERCENT: Literal["percent"] = "percent"
    PERSON: Literal["person"] = "person"


class ScalarEventAbove:
    """Known values; response fields also accept future strings."""

    MEDIAN: Literal["median"] = "median"
    P10: Literal["p10"] = "p10"
    P90: Literal["p90"] = "p90"


class SettlementStatus:
    """Known values; response fields also accept future strings."""

    DISPUTED: Literal["disputed"] = "disputed"
    PENDING: Literal["pending"] = "pending"
    SETTLED: Literal["settled"] = "settled"
    VOID: Literal["void"] = "void"


class TimingStepKind:
    """Known values; response fields also accept future strings."""

    DATE: Literal["date"] = "date"
    MEETING: Literal["meeting"] = "meeting"


class TopicGroup:
    """Known values; response fields also accept future strings."""

    CENTRAL_BANKS: Literal["central_banks"] = "central_banks"
    ENERGY: Literal["energy"] = "energy"
    GLOBAL_ACTIVITY: Literal["global_activity"] = "global_activity"
    GLOBAL_PRICES: Literal["global_prices"] = "global_prices"
    METALS: Literal["metals"] = "metals"
    US_ACTIVITY: Literal["us_activity"] = "us_activity"
    US_JOBS: Literal["us_jobs"] = "us_jobs"
    US_PRICES: Literal["us_prices"] = "us_prices"


class Venue:
    """Known values; response fields also accept future strings."""

    KALSHI: Literal["kalshi"] = "kalshi"
    POLYMARKET: Literal["polymarket"] = "polymarket"


class VenueDifference:
    """Known values; response fields also accept future strings."""

    OUTCOME_SET: Literal["outcome_set"] = "outcome_set"
    RULES: Literal["rules"] = "rules"
    SOURCE: Literal["source"] = "source"
    TIMING: Literal["timing"] = "timing"


class VenueExclusionReason:
    """Known values; response fields also accept future strings."""

    OUTCOME_SET: Literal["outcome_set"] = "outcome_set"
    RULES: Literal["rules"] = "rules"
    SOURCE: Literal["source"] = "source"
    STALE: Literal["stale"] = "stale"
    THIN: Literal["thin"] = "thin"
    TIMING: Literal["timing"] = "timing"


class WebhookDeliveryState:
    """Known values; response fields also accept future strings."""

    CANCELLED: Literal["cancelled"] = "cancelled"
    FAILED: Literal["failed"] = "failed"
    LEASED: Literal["leased"] = "leased"
    PENDING: Literal["pending"] = "pending"
    SUCCEEDED: Literal["succeeded"] = "succeeded"


class WebhookDisabledReason:
    """Known values; response fields also accept future strings."""

    CUSTOMER: Literal["customer"] = "customer"
    PLAN_LIMIT: Literal["plan_limit"] = "plan_limit"


class WebhookEventType:
    """Known values; response fields also accept future strings."""

    DATASET_PUBLISHED: Literal["dataset.published"] = "dataset.published"
    DATASET_REVISED: Literal["dataset.revised"] = "dataset.revised"
    HOLIDAY_CALENDAR_REVISED: Literal["holiday.calendar.revised"] = (
        "holiday.calendar.revised"
    )
    PREDICTION_EVENT_CLOSED: Literal["prediction.event.closed"] = (
        "prediction.event.closed"
    )
    PREDICTION_EVENT_SETTLED: Literal["prediction.event.settled"] = (
        "prediction.event.settled"
    )
    RELEASE_CANCELLED: Literal["release.cancelled"] = "release.cancelled"
    RELEASE_RESCHEDULED: Literal["release.rescheduled"] = "release.rescheduled"
    RELEASE_SCHEDULED: Literal["release.scheduled"] = "release.scheduled"
    RELEASE_UPDATED: Literal["release.updated"] = "release.updated"
    WEBHOOK_TEST: Literal["webhook.test"] = "webhook.test"
    YIELD_CURVE_PUBLISHED: Literal["yield_curve.published"] = "yield_curve.published"
    YIELD_CURVE_REVISED: Literal["yield_curve.revised"] = "yield_curve.revised"


class WebhookFamily:
    """Known values; response fields also accept future strings."""

    ACTIVITY: Literal["activity"] = "activity"
    GDP: Literal["gdp"] = "gdp"
    HOLIDAYS: Literal["holidays"] = "holidays"
    HOUSING: Literal["housing"] = "housing"
    LABOUR: Literal["labour"] = "labour"
    MONEY: Literal["money"] = "money"
    POLICY_RATE: Literal["policy_rate"] = "policy_rate"
    PREDICTIONS: Literal["predictions"] = "predictions"
    PRICES: Literal["prices"] = "prices"
    PUBLIC_FINANCE: Literal["public_finance"] = "public_finance"
    SURVEY: Literal["survey"] = "survey"
    TRADE: Literal["trade"] = "trade"
    YIELD_CURVE: Literal["yield_curve"] = "yield_curve"


class WebhookTestStatus:
    """Known values; response fields also accept future strings."""

    DISABLED: Literal["disabled"] = "disabled"
    QUEUED: Literal["queued"] = "queued"
    RATE_LIMITED: Literal["rate_limited"] = "rate_limited"


class YieldCurveType:
    """Known values; response fields also accept future strings."""

    CONSTANT_MATURITY_YTM: Literal["constant_maturity_ytm"] = "constant_maturity_ytm"
    NOMINAL_PAR: Literal["nominal_par"] = "nominal_par"
    NOMINAL_ZERO_COUPON: Literal["nominal_zero_coupon"] = "nominal_zero_coupon"
    SPOT_SVENSSON: Literal["spot_svensson"] = "spot_svensson"
    ZERO_COUPON: Literal["zero_coupon"] = "zero_coupon"


@dataclass(frozen=True, slots=True, kw_only=True)
class BinaryEvent:
    as_of: str | None = None
    closes_at: str | None = None
    event_id: str
    labels: BinaryLabels | None = None
    probability: str | None = None
    question: str
    quotes: list[Quote]
    release_id: str | None = None
    resolution: str
    resolves_at: str | None = None
    resolves_with: str | None = None
    result: PredictionResult | None = None
    stale: bool | None = None
    status: str
    topic_id: str
    unit: str | None = None
    venues: list[PredictionVenue]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class BinaryLabels:
    no: str
    yes: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CalendarCoverage:
    scope: str
    subdivision_codes: list[str] | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class CalendarHoliday:
    date: str
    local_name: str | None = None
    name: str
    observed: bool | None = None
    scope: str
    subdivision_codes: list[str] | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class CalendarHolidays:
    country: str
    coverage: list[CalendarCoverage]
    holidays: list[CalendarHoliday]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CalendarHolidaysOnDate:
    country: str
    coverage: list[CalendarCoverage]
    holidays: list[CalendarHoliday]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CalendarNextHoliday:
    country: str
    coverage: list[CalendarCoverage]
    holiday: CalendarHoliday | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CalendarSubscriptionCreated:
    expires_at: str
    subscription_id: str
    url: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CalendarSubscriptionInput:
    countries: list[str]
    end_date: str
    families: list[str] | None = None
    include_holidays: bool | None = None
    include_releases: bool | None = None
    scope: str | None = None
    start_date: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CommodityBar:
    close: Decimal
    high: Decimal | None = None
    low: Decimal | None = None
    open: Decimal | None = None
    timestamp: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CommodityBars:
    bars: list[CommodityBar]
    currency: str
    end: str | None = None
    next_cursor: str | None = None
    start: str | None = None
    symbol: str
    unit: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CommodityOilPalmFfbAgePrice:
    price: Decimal
    tree_age_max_years: int
    tree_age_min_years: int


@dataclass(frozen=True, slots=True, kw_only=True)
class CommoditySpot:
    currency: str
    price: Decimal
    stale: bool
    symbol: str
    timestamp: str
    unit: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class Cpi:
    country: str
    index_base: str
    period: str
    released_on: str
    source: SeriesSource | None = None
    value: Decimal
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CpiHistory:
    as_of: str | None = None
    country: str
    index_base: str
    next_cursor: str | None = None
    observations: list[CpiHistoryObservation]
    source: SeriesSource | None = None
    start: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CpiHistoryObservation:
    period: str
    value: Decimal


@dataclass(frozen=True, slots=True, kw_only=True)
class DeliveryEvent:
    country: str
    cursor: str
    event_id: str
    family: str
    holiday_generation: int | None = None
    holiday_year: int | None = None
    recorded_at: str
    release_id: str | None = None
    resource_id: str | None = None
    resource_version: str | None = None
    type: str


@dataclass(frozen=True, slots=True, kw_only=True)
class EconomicCalendar:
    next_cursor: str | None = None
    releases: list[EconomicReleaseSummary]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EconomicReleaseDetail:
    at: str | None = None
    between: list[str] | None = None
    by: str | None = None
    country: str
    date: str | None = None
    family: str
    name: str
    notice: str | None = None
    observed_at: str | None = None
    period: str | None = None
    release_id: str
    revision: int
    series_id: str | None = None
    stage: str | None = None
    status: str
    timezone: str | None = None
    topic: str | None = None
    values: list[EconomicReleaseValue]
    version: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EconomicReleaseSummary:
    at: str | None = None
    between: list[str] | None = None
    by: str | None = None
    country: str
    date: str | None = None
    family: str
    name: str
    notice: str | None = None
    period: str | None = None
    release_id: str
    revision: int
    series_id: str | None = None
    stage: str | None = None
    status: str
    timezone: str | None = None
    topic: str | None = None
    values: list[EconomicReleaseValue]


@dataclass(frozen=True, slots=True, kw_only=True)
class EconomicReleaseValue:
    actual: Decimal | None = None
    annualized: bool | None = None
    currency: str | None = None
    index_base: str | None = None
    measure: str
    not_seasonally_adjusted: bool | None = None
    period: str | None = None
    previous: Decimal | None = None
    previous_revised_from: Decimal | None = None
    scale: str | None = None
    transformation: str | None = None
    unit: str
    value_status: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class EventDetail:
    country: str
    cursor: str
    event_id: str
    family: str
    holiday_generation: int | None = None
    holiday_year: int | None = None
    recorded_at: str
    release_id: str | None = None
    resource_id: str | None = None
    resource_version: str | None = None
    type: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EventsPage:
    cursor: str
    events: list[DeliveryEvent]
    next_cursor: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class ExtremeEvent:
    as_of: str | None = None
    closes_at: str | None = None
    down: list[ExtremeLevel]
    event_id: str
    observation: str
    question: str
    release_id: str | None = None
    resolution: str
    resolves_at: str | None = None
    resolves_with: str | None = None
    result: PredictionResult | None = None
    stale: bool | None = None
    status: str
    topic_id: str
    unit: str | None = None
    up: list[ExtremeLevel]
    venues: list[PredictionVenue]
    window: ExtremeWindow
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class ExtremeLevel:
    key: str
    level: Decimal
    probability: str | None = None
    quotes: list[Quote]


@dataclass(frozen=True, slots=True, kw_only=True)
class ExtremeWindow:
    end: str
    start: str


@dataclass(frozen=True, slots=True, kw_only=True)
class FxBar:
    close: str
    high: str
    low: str
    open: str
    timestamp: str


@dataclass(frozen=True, slots=True, kw_only=True)
class FxBars:
    bars: list[FxBar]
    base: str
    currency: str
    end: str | None = None
    next_cursor: str | None = None
    start: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class FxConversion:
    converted: Decimal
    from_: str
    market_session: str
    rate: Decimal
    stale: bool
    timestamp: str
    to: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class FxHistoricalObservation:
    date: str
    rates: list[FxHistoricalRate]


@dataclass(frozen=True, slots=True, kw_only=True)
class FxHistoricalRate:
    currency: str
    rate: Decimal


@dataclass(frozen=True, slots=True, kw_only=True)
class FxHistory:
    base: str
    end_date: str | None = None
    next_cursor: str | None = None
    observations: list[FxHistoricalObservation]
    start_date: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class FxRate:
    currency: str
    rate: Decimal
    stale: bool
    timestamp: str


@dataclass(frozen=True, slots=True, kw_only=True)
class FxRates:
    base: str
    market_session: str
    rates: list[FxRate]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class Gdp:
    annualized: bool | None = None
    country: str
    currency: str
    not_seasonally_adjusted: bool | None = None
    period: str
    released_on: str
    source: SeriesSource | None = None
    value: Decimal
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class GdpGrowth:
    annualized: bool | None = None
    country: str
    not_seasonally_adjusted: bool | None = None
    period: str
    quarter_over_quarter: Decimal
    quarter_over_quarter_not_seasonally_adjusted: bool | None = None
    released_on: str
    source: SeriesSource | None = None
    year_over_year: Decimal
    year_over_year_not_seasonally_adjusted: bool | None = None
    year_to_date: Decimal | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class GdpGrowthHistory:
    annualized: bool | None = None
    as_of: str | None = None
    country: str
    next_cursor: str | None = None
    not_seasonally_adjusted: bool | None = None
    observations: list[GdpGrowthHistoryObservation]
    quarter_over_quarter_not_seasonally_adjusted: bool | None = None
    source: SeriesSource | None = None
    start: str | None = None
    year_over_year_not_seasonally_adjusted: bool | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class GdpGrowthHistoryObservation:
    period: str
    quarter_over_quarter: Decimal | None = None
    year_over_year: Decimal | None = None
    year_to_date: Decimal | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class GdpHistory:
    annualized: bool | None = None
    as_of: str | None = None
    country: str
    currency: str
    next_cursor: str | None = None
    not_seasonally_adjusted: bool | None = None
    observations: list[GdpHistoryObservation]
    source: SeriesSource | None = None
    start: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class GdpHistoryObservation:
    period: str
    value: Decimal


@dataclass(frozen=True, slots=True, kw_only=True)
class Inflation:
    country: str
    month_over_month: Decimal
    period: str
    released_on: str
    source: SeriesSource | None = None
    year_over_year: Decimal
    year_to_date: Decimal | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class InflationHistory:
    as_of: str | None = None
    country: str
    next_cursor: str | None = None
    observations: list[InflationHistoryObservation]
    source: SeriesSource | None = None
    start: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class InflationHistoryObservation:
    month_over_month: Decimal | None = None
    period: str
    year_over_year: Decimal | None = None
    year_to_date: Decimal | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class LabourForceParticipation:
    country: str
    period: str
    rate: Decimal
    released_on: str
    source: SeriesSource | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class NoContent:
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilFfbMarketHistory(_PalmoilHistory):
    kind: ClassVar[Literal["PalmoilFfbMarketHistory"]] = "PalmoilFfbMarketHistory"
    currency: str
    next_cursor: str | None = None
    observations: list[PalmoilFfbObservation]
    series_id: str
    unit: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilFfbMarketPrice(_PalmoilPrice):
    kind: ClassVar[Literal["PalmoilFfbMarketPrice"]] = "PalmoilFfbMarketPrice"
    currency: str
    period_end: str
    period_start: str
    price: Decimal
    revision: int
    series_id: str
    unit: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilFfbObservation(_PalmoilObservation):
    kind: ClassVar[Literal["PalmoilFfbObservation"]] = "PalmoilFfbObservation"
    period_end: str
    period_start: str
    price: Decimal
    revision: int


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilMarketHistory(_PalmoilHistory):
    kind: ClassVar[Literal["PalmoilMarketHistory"]] = "PalmoilMarketHistory"
    currency: str
    next_cursor: str | None = None
    observations: list[PalmoilMarketObservation]
    series_id: str
    unit: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilMarketObservation(_PalmoilObservation):
    kind: ClassVar[Literal["PalmoilMarketObservation"]] = "PalmoilMarketObservation"
    period_end: str
    period_start: str
    price: Decimal
    price_month: str
    revision: int


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilMarketPrice(_PalmoilPrice):
    kind: ClassVar[Literal["PalmoilMarketPrice"]] = "PalmoilMarketPrice"
    currency: str
    period_end: str
    period_start: str
    price: Decimal
    price_month: str
    revision: int
    series_id: str
    unit: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilScalarHistory(_PalmoilHistory):
    kind: ClassVar[Literal["PalmoilScalarHistory"]] = "PalmoilScalarHistory"
    currency: str
    next_cursor: str | None = None
    observations: list[PalmoilScalarObservation]
    series_id: str
    unit: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilScalarObservation(_PalmoilObservation):
    kind: ClassVar[Literal["PalmoilScalarObservation"]] = "PalmoilScalarObservation"
    period_end: str
    period_start: str
    price: Decimal
    revision: int


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilScalarPrice(_PalmoilPrice):
    kind: ClassVar[Literal["PalmoilScalarPrice"]] = "PalmoilScalarPrice"
    currency: str
    period_end: str
    period_start: str
    price: Decimal
    revision: int
    series_id: str
    unit: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilScalarSeries(_PalmoilSeries):
    kind: ClassVar[Literal["PalmoilScalarSeries"]] = "PalmoilScalarSeries"
    area: str | None = None
    country: str
    coverage_end: str
    coverage_start: str
    currency: str
    frequency: str
    observation_type: str
    period_type: str
    price_type: str
    product: str
    series_id: str
    unit: str


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilScheduleHistory(_PalmoilHistory):
    kind: ClassVar[Literal["PalmoilScheduleHistory"]] = "PalmoilScheduleHistory"
    currency: str
    next_cursor: str | None = None
    observations: list[PalmoilScheduleObservation]
    series_id: str
    unit: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilScheduleObservation(_PalmoilObservation):
    kind: ClassVar[Literal["PalmoilScheduleObservation"]] = "PalmoilScheduleObservation"
    period_end: str
    period_start: str
    prices: list[CommodityOilPalmFfbAgePrice]
    revision: int


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilSchedulePrice(_PalmoilPrice):
    kind: ClassVar[Literal["PalmoilSchedulePrice"]] = "PalmoilSchedulePrice"
    currency: str
    period_end: str
    period_start: str
    prices: list[CommodityOilPalmFfbAgePrice]
    revision: int
    series_id: str
    unit: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilScheduleSeries(_PalmoilSeries):
    kind: ClassVar[Literal["PalmoilScheduleSeries"]] = "PalmoilScheduleSeries"
    area: str | None = None
    country: str
    coverage_end: str
    coverage_start: str
    currency: str
    frequency: str
    observation_type: str
    period_type: str
    price_type: str
    producer_arrangement: str | None = None
    product: str
    series_id: str
    unit: str


@dataclass(frozen=True, slots=True, kw_only=True)
class PalmoilSeriesDiscovery:
    next_cursor: str | None = None
    series: list[PalmoilSeries]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PhysicalLatest:
    attribution: str
    currency: str
    period_end: str
    period_start: str
    price: Decimal
    published_on: str | None = None
    revision: int
    series_id: str
    unit: str
    unit_quantity: Decimal
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PhysicalObservation:
    period_end: str
    period_start: str
    price: Decimal
    published_on: str | None = None
    revision: int


@dataclass(frozen=True, slots=True, kw_only=True)
class PhysicalObservations:
    attribution: str
    currency: str
    next_cursor: str | None = None
    observations: list[PhysicalObservation]
    series_id: str
    unit: str
    unit_quantity: Decimal
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PhysicalSeries:
    area: str | None = None
    attribution: str
    basis: str | None = None
    category: str
    commodity: str
    country: str
    coverage_end: str
    coverage_start: str
    currency: str
    description: str
    frequency: str
    price_type: str
    product: str
    series_id: str
    unit: str
    unit_quantity: Decimal
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PhysicalSeriesPage:
    next_cursor: str | None = None
    series: list[PhysicalSeries]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PolicyPath:
    as_of: str | None = None
    meetings: list[PolicyPathMeeting]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PolicyPathDay:
    date: str
    meetings: list[PolicyPathOdds]


@dataclass(frozen=True, slots=True, kw_only=True)
class PolicyPathHistory:
    days: list[PolicyPathDay]
    meeting_dates: list[PolicyPathMeetingDate]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PolicyPathMeeting:
    cumulative_change_bps: Decimal
    event_id: str
    expected_change_bps: Decimal
    p_cut: str
    p_hike: str
    p_hold: str
    resolves_at: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class PolicyPathMeetingDate:
    event_id: str
    resolves_at: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class PolicyPathOdds:
    cumulative_change_bps: Decimal
    event_id: str
    expected_change_bps: Decimal
    p_cut: str
    p_hike: str
    p_hold: str


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionBar:
    close: str
    high: str | None = None
    low: str | None = None
    open: str | None = None
    timestamp: str


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionEventSummary:
    closes_at: str | None = None
    event_id: str
    question: str
    release_id: str | None = None
    resolves_at: str | None = None
    result: PredictionResultSummary | None = None
    shape: str
    status: str
    topic_id: str


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionEventsPage:
    events: list[PredictionEventSummary]
    next_cursor: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionHistory:
    backfill_venue: str | None = None
    end: str | None = None
    next_cursor: str | None = None
    series: list[PredictionSeries]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionResult:
    amended_at: str | None = None
    final: bool
    settled_at: str | None = None
    venues: list[PredictionResultVenue]


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionResultMarket:
    market_id: str
    outcome: str
    value: Decimal | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionResultSummary:
    amended_at: str | None = None
    final: bool
    settled_at: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionResultVenue:
    amended_at: str | None = None
    final: bool | None = None
    markets: list[PredictionResultMarket]
    settled_at: str | None = None
    unavailable: bool | None = None
    venue: str


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionSeries:
    active_from: str
    active_to: str | None = None
    bars: list[PredictionBar]
    key: str


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionTopic:
    calendar: TopicCalendar | None = None
    group: str
    next_event_id: str | None = None
    resolution_kind: str
    shape: str
    title: str
    topic_id: str
    unit: str | None = None
    venues: list[str]


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionTopicDetail:
    calendar: TopicCalendar | None = None
    events: list[PredictionTopicEvent]
    group: str
    resolution_kind: str
    shape: str
    title: str
    topic_id: str
    unit: str | None = None
    venues: list[str]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionTopicEvent:
    closes_at: str | None = None
    event_id: str
    question: str
    release_id: str | None = None
    resolves_at: str | None = None
    result: PredictionResultSummary | None = None
    status: str


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionTopics:
    topics: list[PredictionTopic]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionVenue:
    excluded_reason: str | None = None
    match: VenueMatch | None = None
    open_interest_usd: Decimal | None = None
    rules_text: str | None = None
    rules_url: str | None = None
    settlement: str | None = None
    settlement_source: str | None = None
    url: str
    venue: str
    volume_24h_usd: Decimal | None = None
    weight: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionWebhookEvent:
    closes_at: str | None = None
    prediction_event_id: str
    release_id: str | None = None
    resolves_at: str | None = None
    settlements: list[PredictionWebhookSettlement]
    shape: str
    status: str
    topic_id: str


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionWebhookSettlement:
    status: str
    venue: str


@dataclass(frozen=True, slots=True, kw_only=True)
class Problem:
    code: str
    detail: str
    request_id: str
    status: int
    title: str
    type: str


@dataclass(frozen=True, slots=True, kw_only=True)
class Quote:
    market_ids: list[str]
    probability: str
    venue: str


@dataclass(frozen=True, slots=True, kw_only=True)
class RateHistory:
    as_of: str | None = None
    country: str
    next_cursor: str | None = None
    observations: list[RateHistoryObservation]
    source: SeriesSource | None = None
    start: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class RateHistoryObservation:
    period: str
    rate: Decimal


@dataclass(frozen=True, slots=True, kw_only=True)
class ResourceHistory:
    country: str
    currency: str | None = None
    next_cursor: str | None = None
    observations: list[ResourceObservation]
    series_id: str
    source: SeriesSource | None = None
    unit: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class ResourceObservation:
    period: str
    released_on: str | None = None
    status: str | None = None
    value: Decimal


@dataclass(frozen=True, slots=True, kw_only=True)
class ScalarEvent:
    above: list[str]
    as_of: str | None = None
    closes_at: str | None = None
    event_id: str
    median: Decimal | None = None
    outcomes: list[ScalarOutcome]
    p10: Decimal | None = None
    p90: Decimal | None = None
    question: str
    release_id: str | None = None
    resolution: str
    resolves_at: str | None = None
    resolves_with: str | None = None
    result: PredictionResult | None = None
    stale: bool | None = None
    status: str
    topic_id: str
    unit: str | None = None
    venues: list[PredictionVenue]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class ScalarOutcome:
    key: str
    label: str
    lower: Decimal | None = None
    probability: str | None = None
    quotes: list[Quote]
    upper: Decimal | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class SeriesSource:
    distributor: str
    publisher: str


@dataclass(frozen=True, slots=True, kw_only=True)
class TimingEvent:
    as_of: str | None = None
    closes_at: str | None = None
    event_id: str
    not_within_window: str | None = None
    question: str
    release_id: str | None = None
    resolution: str
    resolves_at: str | None = None
    resolves_with: str | None = None
    result: PredictionResult | None = None
    stale: bool | None = None
    status: str
    steps: list[TimingStep]
    topic_id: str
    unit: str | None = None
    venues: list[PredictionVenue]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class TimingStep:
    by: str
    key: str
    kind: str
    label: str
    probability: str | None = None
    quotes: list[Quote]


@dataclass(frozen=True, slots=True, kw_only=True)
class TopicCalendar:
    country: str
    family: str


@dataclass(frozen=True, slots=True, kw_only=True)
class TradeHistory:
    as_of: str | None = None
    country: str
    currency: str
    next_cursor: str | None = None
    observations: list[TradeHistoryObservation]
    source: SeriesSource | None = None
    start: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class TradeHistoryObservation:
    exports: Decimal | None = None
    imports: Decimal | None = None
    period: str


@dataclass(frozen=True, slots=True, kw_only=True)
class TradeSummary:
    balance: Decimal
    country: str
    currency: str
    exports: Decimal
    imports: Decimal
    period: str
    released_on: str
    source: SeriesSource | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class Unemployment:
    country: str
    period: str
    rate: Decimal
    released_on: str
    source: SeriesSource | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class VenueMatch:
    differences: list[str]
    note: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookConfigurationHistory:
    config_version: int
    countries: list[str]
    enabled: bool
    families: list[str]
    recorded_at: str
    url: str


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookDeliveriesResponse:
    deliveries: list[WebhookDelivery]
    next_cursor: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookDelivery:
    attempts: int
    config_version: int
    created_at: str
    delivery_id: str
    event_cursor: int | None = None
    is_test: bool | None = None
    last_error: str | None = None
    last_status: int | None = None
    next_attempt_at: str | None = None
    replays: int | None = None
    retry_until: str | None = None
    state: str
    updated_at: str


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookDestinationCreated:
    config_version: int
    countries: list[str]
    created_at: str
    destination_id: str
    disabled_reason: str | None = None
    enabled: bool
    families: list[str]
    secret: str
    secret_version: int
    updated_at: str
    url: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookDestinationInput:
    countries: list[str]
    enabled: bool | None = None
    families: list[str]
    url: str


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookDestinationList:
    destination_limit: int
    destinations: list[WebhookDestinationResponse]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookDestinationResponse:
    config_version: int
    countries: list[str]
    created_at: str
    destination_id: str
    disabled_reason: str | None = None
    enabled: bool
    families: list[str]
    secret_version: int
    updated_at: str
    url: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookEvent:
    country: str | None = None
    cursor: str | None = None
    event_id: str
    family: str | None = None
    holiday_generation: int | None = None
    holiday_year: int | None = None
    prediction: PredictionWebhookEvent | None = None
    recorded_at: str
    release_id: str | None = None
    resource_id: str | None = None
    resource_version: str | None = None
    schema_version: str
    type: str


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookHistoryResponse:
    history: list[WebhookConfigurationHistory]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookTestResponse:
    delivery_id: str | None = None
    retry_after_seconds: int | None = None
    status: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class YieldCurve:
    country: str
    curve_type: str
    date: str
    yields: list[YieldPoint]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class YieldCurveHistoryObservation:
    date: str
    yields: list[YieldPoint]


@dataclass(frozen=True, slots=True, kw_only=True)
class YieldCurveHistoryResponse:
    country: str
    curve_type: str
    next_cursor: str | None = None
    observations: list[YieldCurveHistoryObservation]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class YieldPoint:
    maturity: str
    yield_percent: Decimal


@dataclass(frozen=True, slots=True)
class PalmoilHistoryUnknown(_PalmoilHistory):
    kind: ClassVar[Literal["unknown"]] = "unknown"
    raw: dict[str, object]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)
    _raw_body: bytes = field(default=b"", repr=False, compare=False)


PalmoilHistory: TypeAlias = (
    PalmoilScheduleHistory
    | PalmoilMarketHistory
    | PalmoilScalarHistory
    | PalmoilFfbMarketHistory
    | PalmoilHistoryUnknown
)


@dataclass(frozen=True, slots=True)
class PalmoilObservationUnknown(_PalmoilObservation):
    kind: ClassVar[Literal["unknown"]] = "unknown"
    raw: dict[str, object]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)
    _raw_body: bytes = field(default=b"", repr=False, compare=False)


PalmoilObservation: TypeAlias = (
    PalmoilScheduleObservation
    | PalmoilMarketObservation
    | PalmoilScalarObservation
    | PalmoilFfbObservation
    | PalmoilObservationUnknown
)


@dataclass(frozen=True, slots=True)
class PalmoilPriceUnknown(_PalmoilPrice):
    kind: ClassVar[Literal["unknown"]] = "unknown"
    raw: dict[str, object]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)
    _raw_body: bytes = field(default=b"", repr=False, compare=False)


PalmoilPrice: TypeAlias = (
    PalmoilSchedulePrice
    | PalmoilMarketPrice
    | PalmoilScalarPrice
    | PalmoilFfbMarketPrice
    | PalmoilPriceUnknown
)


@dataclass(frozen=True, slots=True)
class PalmoilSeriesUnknown(_PalmoilSeries):
    kind: ClassVar[Literal["unknown"]] = "unknown"
    raw: dict[str, object]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)
    _raw_body: bytes = field(default=b"", repr=False, compare=False)


PalmoilSeries: TypeAlias = (
    PalmoilScheduleSeries | PalmoilScalarSeries | PalmoilSeriesUnknown
)


def decode_BinaryEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> BinaryEvent:
    data = read_object(value)
    return BinaryEvent(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        closes_at=read_str(data["closes_at"])
        if data.get("closes_at") is not None
        else None,
        event_id=read_str(data["event_id"]),
        labels=decode_BinaryLabels(data["labels"])
        if data.get("labels") is not None
        else None,
        probability=read_str(data["probability"])
        if data.get("probability") is not None
        else None,
        question=read_str(data["question"]),
        quotes=[decode_Quote(item0) for item0 in read_list(data["quotes"])],
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resolution=read_str(data["resolution"]),
        resolves_at=read_str(data["resolves_at"])
        if data.get("resolves_at") is not None
        else None,
        resolves_with=read_str(data["resolves_with"])
        if data.get("resolves_with") is not None
        else None,
        result=decode_PredictionResult(data["result"])
        if data.get("result") is not None
        else None,
        stale=read_bool(data["stale"]) if data.get("stale") is not None else None,
        status=read_str(data["status"]),
        topic_id=read_str(data["topic_id"]),
        unit=read_str(data["unit"]) if data.get("unit") is not None else None,
        venues=[decode_PredictionVenue(item0) for item0 in read_list(data["venues"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_BinaryLabels(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> BinaryLabels:
    data = read_object(value)
    return BinaryLabels(
        no=read_str(data["no"]),
        yes=read_str(data["yes"]),
    )


def decode_CalendarCoverage(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CalendarCoverage:
    data = read_object(value)
    return CalendarCoverage(
        scope=read_str(data["scope"]),
        subdivision_codes=[
            read_str(item0) for item0 in read_list(data["subdivision_codes"])
        ]
        if data.get("subdivision_codes") is not None
        else None,
    )


def decode_CalendarHoliday(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CalendarHoliday:
    data = read_object(value)
    return CalendarHoliday(
        date=read_str(data["date"]),
        local_name=read_str(data["local_name"])
        if data.get("local_name") is not None
        else None,
        name=read_str(data["name"]),
        observed=read_bool(data["observed"])
        if data.get("observed") is not None
        else None,
        scope=read_str(data["scope"]),
        subdivision_codes=[
            read_str(item0) for item0 in read_list(data["subdivision_codes"])
        ]
        if data.get("subdivision_codes") is not None
        else None,
    )


def decode_CalendarHolidays(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CalendarHolidays:
    data = read_object(value)
    return CalendarHolidays(
        country=read_str(data["country"]),
        coverage=[
            decode_CalendarCoverage(item0) for item0 in read_list(data["coverage"])
        ],
        holidays=[
            decode_CalendarHoliday(item0) for item0 in read_list(data["holidays"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CalendarHolidaysOnDate(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CalendarHolidaysOnDate:
    data = read_object(value)
    return CalendarHolidaysOnDate(
        country=read_str(data["country"]),
        coverage=[
            decode_CalendarCoverage(item0) for item0 in read_list(data["coverage"])
        ],
        holidays=[
            decode_CalendarHoliday(item0) for item0 in read_list(data["holidays"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CalendarNextHoliday(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CalendarNextHoliday:
    data = read_object(value)
    return CalendarNextHoliday(
        country=read_str(data["country"]),
        coverage=[
            decode_CalendarCoverage(item0) for item0 in read_list(data["coverage"])
        ],
        holiday=decode_CalendarHoliday(data["holiday"])
        if data.get("holiday") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CalendarSubscriptionCreated(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CalendarSubscriptionCreated:
    data = read_object(value)
    return CalendarSubscriptionCreated(
        expires_at=read_str(data["expires_at"]),
        subscription_id=read_str(data["subscription_id"]),
        url=read_str(data["url"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CalendarSubscriptionInput(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CalendarSubscriptionInput:
    data = read_object(value)
    return CalendarSubscriptionInput(
        countries=[read_str(item0) for item0 in read_list(data["countries"])],
        end_date=read_str(data["end_date"]),
        families=[read_str(item0) for item0 in read_list(data["families"])]
        if data.get("families") is not None
        else None,
        include_holidays=read_bool(data["include_holidays"])
        if data.get("include_holidays") is not None
        else None,
        include_releases=read_bool(data["include_releases"])
        if data.get("include_releases") is not None
        else None,
        scope=read_str(data["scope"]) if data.get("scope") is not None else None,
        start_date=read_str(data["start_date"]),
    )


def decode_CommodityBar(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CommodityBar:
    data = read_object(value)
    return CommodityBar(
        close=read_decimal(data["close"]),
        high=read_decimal(data["high"]) if data.get("high") is not None else None,
        low=read_decimal(data["low"]) if data.get("low") is not None else None,
        open=read_decimal(data["open"]) if data.get("open") is not None else None,
        timestamp=read_str(data["timestamp"]),
    )


def decode_CommodityBars(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CommodityBars:
    data = read_object(value)
    return CommodityBars(
        bars=[decode_CommodityBar(item0) for item0 in read_list(data["bars"])],
        currency=read_str(data["currency"]),
        end=read_str(data["end"]) if data.get("end") is not None else None,
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        start=read_str(data["start"]) if data.get("start") is not None else None,
        symbol=read_str(data["symbol"]),
        unit=read_str(data["unit"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CommodityOilPalmFfbAgePrice(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CommodityOilPalmFfbAgePrice:
    data = read_object(value)
    return CommodityOilPalmFfbAgePrice(
        price=read_decimal(data["price"]),
        tree_age_max_years=read_int(data["tree_age_max_years"]),
        tree_age_min_years=read_int(data["tree_age_min_years"]),
    )


def decode_CommoditySpot(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CommoditySpot:
    data = read_object(value)
    return CommoditySpot(
        currency=read_str(data["currency"]),
        price=read_decimal(data["price"]),
        stale=read_bool(data["stale"]),
        symbol=read_str(data["symbol"]),
        timestamp=read_str(data["timestamp"]),
        unit=read_str(data["unit"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_Cpi(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> Cpi:
    data = read_object(value)
    return Cpi(
        country=read_str(data["country"]),
        index_base=read_str(data["index_base"]),
        period=read_str(data["period"]),
        released_on=read_str(data["released_on"]),
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        value=read_decimal(data["value"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CpiHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CpiHistory:
    data = read_object(value)
    return CpiHistory(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        country=read_str(data["country"]),
        index_base=read_str(data["index_base"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_CpiHistoryObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        start=read_str(data["start"]) if data.get("start") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CpiHistoryObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CpiHistoryObservation:
    data = read_object(value)
    return CpiHistoryObservation(
        period=read_str(data["period"]),
        value=read_decimal(data["value"]),
    )


def decode_DeliveryEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> DeliveryEvent:
    data = read_object(value)
    return DeliveryEvent(
        country=read_str(data["country"]),
        cursor=read_str(data["cursor"]),
        event_id=read_str(data["event_id"]),
        family=read_str(data["family"]),
        holiday_generation=read_int(data["holiday_generation"])
        if data.get("holiday_generation") is not None
        else None,
        holiday_year=read_int(data["holiday_year"])
        if data.get("holiday_year") is not None
        else None,
        recorded_at=read_str(data["recorded_at"]),
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resource_id=read_str(data["resource_id"])
        if data.get("resource_id") is not None
        else None,
        resource_version=read_str(data["resource_version"])
        if data.get("resource_version") is not None
        else None,
        type=read_str(data["type"]),
    )


def decode_EconomicCalendar(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EconomicCalendar:
    data = read_object(value)
    return EconomicCalendar(
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        releases=[
            decode_EconomicReleaseSummary(item0)
            for item0 in read_list(data["releases"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EconomicReleaseDetail(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EconomicReleaseDetail:
    data = read_object(value)
    return EconomicReleaseDetail(
        at=read_str(data["at"]) if data.get("at") is not None else None,
        between=[read_str(item0) for item0 in read_list(data["between"])]
        if data.get("between") is not None
        else None,
        by=read_str(data["by"]) if data.get("by") is not None else None,
        country=read_str(data["country"]),
        date=read_str(data["date"]) if data.get("date") is not None else None,
        family=read_str(data["family"]),
        name=read_str(data["name"]),
        notice=read_str(data["notice"]) if data.get("notice") is not None else None,
        observed_at=read_str(data["observed_at"])
        if data.get("observed_at") is not None
        else None,
        period=read_str(data["period"]) if data.get("period") is not None else None,
        release_id=read_str(data["release_id"]),
        revision=read_int(data["revision"]),
        series_id=read_str(data["series_id"])
        if data.get("series_id") is not None
        else None,
        stage=read_str(data["stage"]) if data.get("stage") is not None else None,
        status=read_str(data["status"]),
        timezone=read_str(data["timezone"])
        if data.get("timezone") is not None
        else None,
        topic=read_str(data["topic"]) if data.get("topic") is not None else None,
        values=[
            decode_EconomicReleaseValue(item0) for item0 in read_list(data["values"])
        ],
        version=read_str(data["version"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EconomicReleaseSummary(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EconomicReleaseSummary:
    data = read_object(value)
    return EconomicReleaseSummary(
        at=read_str(data["at"]) if data.get("at") is not None else None,
        between=[read_str(item0) for item0 in read_list(data["between"])]
        if data.get("between") is not None
        else None,
        by=read_str(data["by"]) if data.get("by") is not None else None,
        country=read_str(data["country"]),
        date=read_str(data["date"]) if data.get("date") is not None else None,
        family=read_str(data["family"]),
        name=read_str(data["name"]),
        notice=read_str(data["notice"]) if data.get("notice") is not None else None,
        period=read_str(data["period"]) if data.get("period") is not None else None,
        release_id=read_str(data["release_id"]),
        revision=read_int(data["revision"]),
        series_id=read_str(data["series_id"])
        if data.get("series_id") is not None
        else None,
        stage=read_str(data["stage"]) if data.get("stage") is not None else None,
        status=read_str(data["status"]),
        timezone=read_str(data["timezone"])
        if data.get("timezone") is not None
        else None,
        topic=read_str(data["topic"]) if data.get("topic") is not None else None,
        values=[
            decode_EconomicReleaseValue(item0) for item0 in read_list(data["values"])
        ],
    )


def decode_EconomicReleaseValue(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EconomicReleaseValue:
    data = read_object(value)
    return EconomicReleaseValue(
        actual=read_decimal(data["actual"]) if data.get("actual") is not None else None,
        annualized=read_bool(data["annualized"])
        if data.get("annualized") is not None
        else None,
        currency=read_str(data["currency"])
        if data.get("currency") is not None
        else None,
        index_base=read_str(data["index_base"])
        if data.get("index_base") is not None
        else None,
        measure=read_str(data["measure"]),
        not_seasonally_adjusted=read_bool(data["not_seasonally_adjusted"])
        if data.get("not_seasonally_adjusted") is not None
        else None,
        period=read_str(data["period"]) if data.get("period") is not None else None,
        previous=read_decimal(data["previous"])
        if data.get("previous") is not None
        else None,
        previous_revised_from=read_decimal(data["previous_revised_from"])
        if data.get("previous_revised_from") is not None
        else None,
        scale=read_str(data["scale"]) if data.get("scale") is not None else None,
        transformation=read_str(data["transformation"])
        if data.get("transformation") is not None
        else None,
        unit=read_str(data["unit"]),
        value_status=read_str(data["value_status"])
        if data.get("value_status") is not None
        else None,
    )


def decode_EventDetail(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EventDetail:
    data = read_object(value)
    return EventDetail(
        country=read_str(data["country"]),
        cursor=read_str(data["cursor"]),
        event_id=read_str(data["event_id"]),
        family=read_str(data["family"]),
        holiday_generation=read_int(data["holiday_generation"])
        if data.get("holiday_generation") is not None
        else None,
        holiday_year=read_int(data["holiday_year"])
        if data.get("holiday_year") is not None
        else None,
        recorded_at=read_str(data["recorded_at"]),
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resource_id=read_str(data["resource_id"])
        if data.get("resource_id") is not None
        else None,
        resource_version=read_str(data["resource_version"])
        if data.get("resource_version") is not None
        else None,
        type=read_str(data["type"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EventsPage(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EventsPage:
    data = read_object(value)
    return EventsPage(
        cursor=read_str(data["cursor"]),
        events=[decode_DeliveryEvent(item0) for item0 in read_list(data["events"])],
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_ExtremeEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ExtremeEvent:
    data = read_object(value)
    return ExtremeEvent(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        closes_at=read_str(data["closes_at"])
        if data.get("closes_at") is not None
        else None,
        down=[decode_ExtremeLevel(item0) for item0 in read_list(data["down"])],
        event_id=read_str(data["event_id"]),
        observation=read_str(data["observation"]),
        question=read_str(data["question"]),
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resolution=read_str(data["resolution"]),
        resolves_at=read_str(data["resolves_at"])
        if data.get("resolves_at") is not None
        else None,
        resolves_with=read_str(data["resolves_with"])
        if data.get("resolves_with") is not None
        else None,
        result=decode_PredictionResult(data["result"])
        if data.get("result") is not None
        else None,
        stale=read_bool(data["stale"]) if data.get("stale") is not None else None,
        status=read_str(data["status"]),
        topic_id=read_str(data["topic_id"]),
        unit=read_str(data["unit"]) if data.get("unit") is not None else None,
        up=[decode_ExtremeLevel(item0) for item0 in read_list(data["up"])],
        venues=[decode_PredictionVenue(item0) for item0 in read_list(data["venues"])],
        window=decode_ExtremeWindow(data["window"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_ExtremeLevel(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ExtremeLevel:
    data = read_object(value)
    return ExtremeLevel(
        key=read_str(data["key"]),
        level=read_decimal(data["level"]),
        probability=read_str(data["probability"])
        if data.get("probability") is not None
        else None,
        quotes=[decode_Quote(item0) for item0 in read_list(data["quotes"])],
    )


def decode_ExtremeWindow(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ExtremeWindow:
    data = read_object(value)
    return ExtremeWindow(
        end=read_str(data["end"]),
        start=read_str(data["start"]),
    )


def decode_FxBar(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FxBar:
    data = read_object(value)
    return FxBar(
        close=read_str(data["close"]),
        high=read_str(data["high"]),
        low=read_str(data["low"]),
        open=read_str(data["open"]),
        timestamp=read_str(data["timestamp"]),
    )


def decode_FxBars(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FxBars:
    data = read_object(value)
    return FxBars(
        bars=[decode_FxBar(item0) for item0 in read_list(data["bars"])],
        base=read_str(data["base"]),
        currency=read_str(data["currency"]),
        end=read_str(data["end"]) if data.get("end") is not None else None,
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        start=read_str(data["start"]) if data.get("start") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_FxConversion(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FxConversion:
    data = read_object(value)
    return FxConversion(
        converted=read_decimal(data["converted"]),
        from_=read_str(data["from"]),
        market_session=read_str(data["market_session"]),
        rate=read_decimal(data["rate"]),
        stale=read_bool(data["stale"]),
        timestamp=read_str(data["timestamp"]),
        to=read_str(data["to"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_FxHistoricalObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FxHistoricalObservation:
    data = read_object(value)
    return FxHistoricalObservation(
        date=read_str(data["date"]),
        rates=[decode_FxHistoricalRate(item0) for item0 in read_list(data["rates"])],
    )


def decode_FxHistoricalRate(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FxHistoricalRate:
    data = read_object(value)
    return FxHistoricalRate(
        currency=read_str(data["currency"]),
        rate=read_decimal(data["rate"]),
    )


def decode_FxHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FxHistory:
    data = read_object(value)
    return FxHistory(
        base=read_str(data["base"]),
        end_date=read_str(data["end_date"])
        if data.get("end_date") is not None
        else None,
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_FxHistoricalObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        start_date=read_str(data["start_date"])
        if data.get("start_date") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_FxRate(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FxRate:
    data = read_object(value)
    return FxRate(
        currency=read_str(data["currency"]),
        rate=read_decimal(data["rate"]),
        stale=read_bool(data["stale"]),
        timestamp=read_str(data["timestamp"]),
    )


def decode_FxRates(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FxRates:
    data = read_object(value)
    return FxRates(
        base=read_str(data["base"]),
        market_session=read_str(data["market_session"]),
        rates=[decode_FxRate(item0) for item0 in read_list(data["rates"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_Gdp(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> Gdp:
    data = read_object(value)
    return Gdp(
        annualized=read_bool(data["annualized"])
        if data.get("annualized") is not None
        else None,
        country=read_str(data["country"]),
        currency=read_str(data["currency"]),
        not_seasonally_adjusted=read_bool(data["not_seasonally_adjusted"])
        if data.get("not_seasonally_adjusted") is not None
        else None,
        period=read_str(data["period"]),
        released_on=read_str(data["released_on"]),
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        value=read_decimal(data["value"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_GdpGrowth(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> GdpGrowth:
    data = read_object(value)
    return GdpGrowth(
        annualized=read_bool(data["annualized"])
        if data.get("annualized") is not None
        else None,
        country=read_str(data["country"]),
        not_seasonally_adjusted=read_bool(data["not_seasonally_adjusted"])
        if data.get("not_seasonally_adjusted") is not None
        else None,
        period=read_str(data["period"]),
        quarter_over_quarter=read_decimal(data["quarter_over_quarter"]),
        quarter_over_quarter_not_seasonally_adjusted=read_bool(
            data["quarter_over_quarter_not_seasonally_adjusted"]
        )
        if data.get("quarter_over_quarter_not_seasonally_adjusted") is not None
        else None,
        released_on=read_str(data["released_on"]),
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        year_over_year=read_decimal(data["year_over_year"]),
        year_over_year_not_seasonally_adjusted=read_bool(
            data["year_over_year_not_seasonally_adjusted"]
        )
        if data.get("year_over_year_not_seasonally_adjusted") is not None
        else None,
        year_to_date=read_decimal(data["year_to_date"])
        if data.get("year_to_date") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_GdpGrowthHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> GdpGrowthHistory:
    data = read_object(value)
    return GdpGrowthHistory(
        annualized=read_bool(data["annualized"])
        if data.get("annualized") is not None
        else None,
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        country=read_str(data["country"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        not_seasonally_adjusted=read_bool(data["not_seasonally_adjusted"])
        if data.get("not_seasonally_adjusted") is not None
        else None,
        observations=[
            decode_GdpGrowthHistoryObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        quarter_over_quarter_not_seasonally_adjusted=read_bool(
            data["quarter_over_quarter_not_seasonally_adjusted"]
        )
        if data.get("quarter_over_quarter_not_seasonally_adjusted") is not None
        else None,
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        start=read_str(data["start"]) if data.get("start") is not None else None,
        year_over_year_not_seasonally_adjusted=read_bool(
            data["year_over_year_not_seasonally_adjusted"]
        )
        if data.get("year_over_year_not_seasonally_adjusted") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_GdpGrowthHistoryObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> GdpGrowthHistoryObservation:
    data = read_object(value)
    return GdpGrowthHistoryObservation(
        period=read_str(data["period"]),
        quarter_over_quarter=read_decimal(data["quarter_over_quarter"])
        if data.get("quarter_over_quarter") is not None
        else None,
        year_over_year=read_decimal(data["year_over_year"])
        if data.get("year_over_year") is not None
        else None,
        year_to_date=read_decimal(data["year_to_date"])
        if data.get("year_to_date") is not None
        else None,
    )


def decode_GdpHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> GdpHistory:
    data = read_object(value)
    return GdpHistory(
        annualized=read_bool(data["annualized"])
        if data.get("annualized") is not None
        else None,
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        country=read_str(data["country"]),
        currency=read_str(data["currency"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        not_seasonally_adjusted=read_bool(data["not_seasonally_adjusted"])
        if data.get("not_seasonally_adjusted") is not None
        else None,
        observations=[
            decode_GdpHistoryObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        start=read_str(data["start"]) if data.get("start") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_GdpHistoryObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> GdpHistoryObservation:
    data = read_object(value)
    return GdpHistoryObservation(
        period=read_str(data["period"]),
        value=read_decimal(data["value"]),
    )


def decode_Inflation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> Inflation:
    data = read_object(value)
    return Inflation(
        country=read_str(data["country"]),
        month_over_month=read_decimal(data["month_over_month"]),
        period=read_str(data["period"]),
        released_on=read_str(data["released_on"]),
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        year_over_year=read_decimal(data["year_over_year"]),
        year_to_date=read_decimal(data["year_to_date"])
        if data.get("year_to_date") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_InflationHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> InflationHistory:
    data = read_object(value)
    return InflationHistory(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        country=read_str(data["country"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_InflationHistoryObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        start=read_str(data["start"]) if data.get("start") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_InflationHistoryObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> InflationHistoryObservation:
    data = read_object(value)
    return InflationHistoryObservation(
        month_over_month=read_decimal(data["month_over_month"])
        if data.get("month_over_month") is not None
        else None,
        period=read_str(data["period"]),
        year_over_year=read_decimal(data["year_over_year"])
        if data.get("year_over_year") is not None
        else None,
        year_to_date=read_decimal(data["year_to_date"])
        if data.get("year_to_date") is not None
        else None,
    )


def decode_LabourForceParticipation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> LabourForceParticipation:
    data = read_object(value)
    return LabourForceParticipation(
        country=read_str(data["country"]),
        period=read_str(data["period"]),
        rate=read_decimal(data["rate"]),
        released_on=read_str(data["released_on"]),
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_NoContent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> NoContent:
    read_object(value)
    return NoContent(
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PalmoilFfbMarketHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilFfbMarketHistory:
    data = read_object(value)
    return PalmoilFfbMarketHistory(
        currency=read_str(data["currency"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_PalmoilFfbObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        series_id=read_str(data["series_id"]),
        unit=read_str(data["unit"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PalmoilFfbMarketPrice(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilFfbMarketPrice:
    data = read_object(value)
    return PalmoilFfbMarketPrice(
        currency=read_str(data["currency"]),
        period_end=read_str(data["period_end"]),
        period_start=read_str(data["period_start"]),
        price=read_decimal(data["price"]),
        revision=read_int(data["revision"]),
        series_id=read_str(data["series_id"]),
        unit=read_str(data["unit"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PalmoilFfbObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilFfbObservation:
    data = read_object(value)
    return PalmoilFfbObservation(
        period_end=read_str(data["period_end"]),
        period_start=read_str(data["period_start"]),
        price=read_decimal(data["price"]),
        revision=read_int(data["revision"]),
    )


def decode_PalmoilMarketHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilMarketHistory:
    data = read_object(value)
    return PalmoilMarketHistory(
        currency=read_str(data["currency"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_PalmoilMarketObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        series_id=read_str(data["series_id"]),
        unit=read_str(data["unit"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PalmoilMarketObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilMarketObservation:
    data = read_object(value)
    return PalmoilMarketObservation(
        period_end=read_str(data["period_end"]),
        period_start=read_str(data["period_start"]),
        price=read_decimal(data["price"]),
        price_month=read_str(data["price_month"]),
        revision=read_int(data["revision"]),
    )


def decode_PalmoilMarketPrice(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilMarketPrice:
    data = read_object(value)
    return PalmoilMarketPrice(
        currency=read_str(data["currency"]),
        period_end=read_str(data["period_end"]),
        period_start=read_str(data["period_start"]),
        price=read_decimal(data["price"]),
        price_month=read_str(data["price_month"]),
        revision=read_int(data["revision"]),
        series_id=read_str(data["series_id"]),
        unit=read_str(data["unit"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PalmoilScalarHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilScalarHistory:
    data = read_object(value)
    return PalmoilScalarHistory(
        currency=read_str(data["currency"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_PalmoilScalarObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        series_id=read_str(data["series_id"]),
        unit=read_str(data["unit"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PalmoilScalarObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilScalarObservation:
    data = read_object(value)
    return PalmoilScalarObservation(
        period_end=read_str(data["period_end"]),
        period_start=read_str(data["period_start"]),
        price=read_decimal(data["price"]),
        revision=read_int(data["revision"]),
    )


def decode_PalmoilScalarPrice(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilScalarPrice:
    data = read_object(value)
    return PalmoilScalarPrice(
        currency=read_str(data["currency"]),
        period_end=read_str(data["period_end"]),
        period_start=read_str(data["period_start"]),
        price=read_decimal(data["price"]),
        revision=read_int(data["revision"]),
        series_id=read_str(data["series_id"]),
        unit=read_str(data["unit"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PalmoilScalarSeries(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilScalarSeries:
    data = read_object(value)
    return PalmoilScalarSeries(
        area=read_str(data["area"]) if data.get("area") is not None else None,
        country=read_str(data["country"]),
        coverage_end=read_str(data["coverage_end"]),
        coverage_start=read_str(data["coverage_start"]),
        currency=read_str(data["currency"]),
        frequency=read_str(data["frequency"]),
        observation_type=read_str(data["observation_type"]),
        period_type=read_str(data["period_type"]),
        price_type=read_str(data["price_type"]),
        product=read_str(data["product"]),
        series_id=read_str(data["series_id"]),
        unit=read_str(data["unit"]),
    )


def decode_PalmoilScheduleHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilScheduleHistory:
    data = read_object(value)
    return PalmoilScheduleHistory(
        currency=read_str(data["currency"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_PalmoilScheduleObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        series_id=read_str(data["series_id"]),
        unit=read_str(data["unit"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PalmoilScheduleObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilScheduleObservation:
    data = read_object(value)
    return PalmoilScheduleObservation(
        period_end=read_str(data["period_end"]),
        period_start=read_str(data["period_start"]),
        prices=[
            decode_CommodityOilPalmFfbAgePrice(item0)
            for item0 in read_list(data["prices"])
        ],
        revision=read_int(data["revision"]),
    )


def decode_PalmoilSchedulePrice(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilSchedulePrice:
    data = read_object(value)
    return PalmoilSchedulePrice(
        currency=read_str(data["currency"]),
        period_end=read_str(data["period_end"]),
        period_start=read_str(data["period_start"]),
        prices=[
            decode_CommodityOilPalmFfbAgePrice(item0)
            for item0 in read_list(data["prices"])
        ],
        revision=read_int(data["revision"]),
        series_id=read_str(data["series_id"]),
        unit=read_str(data["unit"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PalmoilScheduleSeries(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilScheduleSeries:
    data = read_object(value)
    return PalmoilScheduleSeries(
        area=read_str(data["area"]) if data.get("area") is not None else None,
        country=read_str(data["country"]),
        coverage_end=read_str(data["coverage_end"]),
        coverage_start=read_str(data["coverage_start"]),
        currency=read_str(data["currency"]),
        frequency=read_str(data["frequency"]),
        observation_type=read_str(data["observation_type"]),
        period_type=read_str(data["period_type"]),
        price_type=read_str(data["price_type"]),
        producer_arrangement=read_str(data["producer_arrangement"])
        if data.get("producer_arrangement") is not None
        else None,
        product=read_str(data["product"]),
        series_id=read_str(data["series_id"]),
        unit=read_str(data["unit"]),
    )


def decode_PalmoilSeriesDiscovery(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilSeriesDiscovery:
    data = read_object(value)
    return PalmoilSeriesDiscovery(
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        series=[decode_PalmoilSeries(item0) for item0 in read_list(data["series"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PhysicalLatest(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PhysicalLatest:
    data = read_object(value)
    return PhysicalLatest(
        attribution=read_str(data["attribution"]),
        currency=read_str(data["currency"]),
        period_end=read_str(data["period_end"]),
        period_start=read_str(data["period_start"]),
        price=read_decimal(data["price"]),
        published_on=read_str(data["published_on"])
        if data.get("published_on") is not None
        else None,
        revision=read_int(data["revision"]),
        series_id=read_str(data["series_id"]),
        unit=read_str(data["unit"]),
        unit_quantity=read_decimal(data["unit_quantity"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PhysicalObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PhysicalObservation:
    data = read_object(value)
    return PhysicalObservation(
        period_end=read_str(data["period_end"]),
        period_start=read_str(data["period_start"]),
        price=read_decimal(data["price"]),
        published_on=read_str(data["published_on"])
        if data.get("published_on") is not None
        else None,
        revision=read_int(data["revision"]),
    )


def decode_PhysicalObservations(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PhysicalObservations:
    data = read_object(value)
    return PhysicalObservations(
        attribution=read_str(data["attribution"]),
        currency=read_str(data["currency"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_PhysicalObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        series_id=read_str(data["series_id"]),
        unit=read_str(data["unit"]),
        unit_quantity=read_decimal(data["unit_quantity"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PhysicalSeries(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PhysicalSeries:
    data = read_object(value)
    return PhysicalSeries(
        area=read_str(data["area"]) if data.get("area") is not None else None,
        attribution=read_str(data["attribution"]),
        basis=read_str(data["basis"]) if data.get("basis") is not None else None,
        category=read_str(data["category"]),
        commodity=read_str(data["commodity"]),
        country=read_str(data["country"]),
        coverage_end=read_str(data["coverage_end"]),
        coverage_start=read_str(data["coverage_start"]),
        currency=read_str(data["currency"]),
        description=read_str(data["description"]),
        frequency=read_str(data["frequency"]),
        price_type=read_str(data["price_type"]),
        product=read_str(data["product"]),
        series_id=read_str(data["series_id"]),
        unit=read_str(data["unit"]),
        unit_quantity=read_decimal(data["unit_quantity"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PhysicalSeriesPage(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PhysicalSeriesPage:
    data = read_object(value)
    return PhysicalSeriesPage(
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        series=[decode_PhysicalSeries(item0) for item0 in read_list(data["series"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PolicyPath(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PolicyPath:
    data = read_object(value)
    return PolicyPath(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        meetings=[
            decode_PolicyPathMeeting(item0) for item0 in read_list(data["meetings"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PolicyPathDay(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PolicyPathDay:
    data = read_object(value)
    return PolicyPathDay(
        date=read_str(data["date"]),
        meetings=[
            decode_PolicyPathOdds(item0) for item0 in read_list(data["meetings"])
        ],
    )


def decode_PolicyPathHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PolicyPathHistory:
    data = read_object(value)
    return PolicyPathHistory(
        days=[decode_PolicyPathDay(item0) for item0 in read_list(data["days"])],
        meeting_dates=[
            decode_PolicyPathMeetingDate(item0)
            for item0 in read_list(data["meeting_dates"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PolicyPathMeeting(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PolicyPathMeeting:
    data = read_object(value)
    return PolicyPathMeeting(
        cumulative_change_bps=read_decimal(data["cumulative_change_bps"]),
        event_id=read_str(data["event_id"]),
        expected_change_bps=read_decimal(data["expected_change_bps"]),
        p_cut=read_str(data["p_cut"]),
        p_hike=read_str(data["p_hike"]),
        p_hold=read_str(data["p_hold"]),
        resolves_at=read_str(data["resolves_at"])
        if data.get("resolves_at") is not None
        else None,
    )


def decode_PolicyPathMeetingDate(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PolicyPathMeetingDate:
    data = read_object(value)
    return PolicyPathMeetingDate(
        event_id=read_str(data["event_id"]),
        resolves_at=read_str(data["resolves_at"])
        if data.get("resolves_at") is not None
        else None,
    )


def decode_PolicyPathOdds(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PolicyPathOdds:
    data = read_object(value)
    return PolicyPathOdds(
        cumulative_change_bps=read_decimal(data["cumulative_change_bps"]),
        event_id=read_str(data["event_id"]),
        expected_change_bps=read_decimal(data["expected_change_bps"]),
        p_cut=read_str(data["p_cut"]),
        p_hike=read_str(data["p_hike"]),
        p_hold=read_str(data["p_hold"]),
    )


def decode_PredictionBar(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionBar:
    data = read_object(value)
    return PredictionBar(
        close=read_str(data["close"]),
        high=read_str(data["high"]) if data.get("high") is not None else None,
        low=read_str(data["low"]) if data.get("low") is not None else None,
        open=read_str(data["open"]) if data.get("open") is not None else None,
        timestamp=read_str(data["timestamp"]),
    )


def decode_PredictionEventSummary(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionEventSummary:
    data = read_object(value)
    return PredictionEventSummary(
        closes_at=read_str(data["closes_at"])
        if data.get("closes_at") is not None
        else None,
        event_id=read_str(data["event_id"]),
        question=read_str(data["question"]),
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resolves_at=read_str(data["resolves_at"])
        if data.get("resolves_at") is not None
        else None,
        result=decode_PredictionResultSummary(data["result"])
        if data.get("result") is not None
        else None,
        shape=read_str(data["shape"]),
        status=read_str(data["status"]),
        topic_id=read_str(data["topic_id"]),
    )


def decode_PredictionEventsPage(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionEventsPage:
    data = read_object(value)
    return PredictionEventsPage(
        events=[
            decode_PredictionEventSummary(item0) for item0 in read_list(data["events"])
        ],
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PredictionHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionHistory:
    data = read_object(value)
    return PredictionHistory(
        backfill_venue=read_str(data["backfill_venue"])
        if data.get("backfill_venue") is not None
        else None,
        end=read_str(data["end"]) if data.get("end") is not None else None,
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        series=[decode_PredictionSeries(item0) for item0 in read_list(data["series"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PredictionResult(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionResult:
    data = read_object(value)
    return PredictionResult(
        amended_at=read_str(data["amended_at"])
        if data.get("amended_at") is not None
        else None,
        final=read_bool(data["final"]),
        settled_at=read_str(data["settled_at"])
        if data.get("settled_at") is not None
        else None,
        venues=[
            decode_PredictionResultVenue(item0) for item0 in read_list(data["venues"])
        ],
    )


def decode_PredictionResultMarket(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionResultMarket:
    data = read_object(value)
    return PredictionResultMarket(
        market_id=read_str(data["market_id"]),
        outcome=read_str(data["outcome"]),
        value=read_decimal(data["value"]) if data.get("value") is not None else None,
    )


def decode_PredictionResultSummary(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionResultSummary:
    data = read_object(value)
    return PredictionResultSummary(
        amended_at=read_str(data["amended_at"])
        if data.get("amended_at") is not None
        else None,
        final=read_bool(data["final"]),
        settled_at=read_str(data["settled_at"])
        if data.get("settled_at") is not None
        else None,
    )


def decode_PredictionResultVenue(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionResultVenue:
    data = read_object(value)
    return PredictionResultVenue(
        amended_at=read_str(data["amended_at"])
        if data.get("amended_at") is not None
        else None,
        final=read_bool(data["final"]) if data.get("final") is not None else None,
        markets=[
            decode_PredictionResultMarket(item0) for item0 in read_list(data["markets"])
        ],
        settled_at=read_str(data["settled_at"])
        if data.get("settled_at") is not None
        else None,
        unavailable=read_bool(data["unavailable"])
        if data.get("unavailable") is not None
        else None,
        venue=read_str(data["venue"]),
    )


def decode_PredictionSeries(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionSeries:
    data = read_object(value)
    return PredictionSeries(
        active_from=read_str(data["active_from"]),
        active_to=read_str(data["active_to"])
        if data.get("active_to") is not None
        else None,
        bars=[decode_PredictionBar(item0) for item0 in read_list(data["bars"])],
        key=read_str(data["key"]),
    )


def decode_PredictionTopic(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionTopic:
    data = read_object(value)
    return PredictionTopic(
        calendar=decode_TopicCalendar(data["calendar"])
        if data.get("calendar") is not None
        else None,
        group=read_str(data["group"]),
        next_event_id=read_str(data["next_event_id"])
        if data.get("next_event_id") is not None
        else None,
        resolution_kind=read_str(data["resolution_kind"]),
        shape=read_str(data["shape"]),
        title=read_str(data["title"]),
        topic_id=read_str(data["topic_id"]),
        unit=read_str(data["unit"]) if data.get("unit") is not None else None,
        venues=[read_str(item0) for item0 in read_list(data["venues"])],
    )


def decode_PredictionTopicDetail(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionTopicDetail:
    data = read_object(value)
    return PredictionTopicDetail(
        calendar=decode_TopicCalendar(data["calendar"])
        if data.get("calendar") is not None
        else None,
        events=[
            decode_PredictionTopicEvent(item0) for item0 in read_list(data["events"])
        ],
        group=read_str(data["group"]),
        resolution_kind=read_str(data["resolution_kind"]),
        shape=read_str(data["shape"]),
        title=read_str(data["title"]),
        topic_id=read_str(data["topic_id"]),
        unit=read_str(data["unit"]) if data.get("unit") is not None else None,
        venues=[read_str(item0) for item0 in read_list(data["venues"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PredictionTopicEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionTopicEvent:
    data = read_object(value)
    return PredictionTopicEvent(
        closes_at=read_str(data["closes_at"])
        if data.get("closes_at") is not None
        else None,
        event_id=read_str(data["event_id"]),
        question=read_str(data["question"]),
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resolves_at=read_str(data["resolves_at"])
        if data.get("resolves_at") is not None
        else None,
        result=decode_PredictionResultSummary(data["result"])
        if data.get("result") is not None
        else None,
        status=read_str(data["status"]),
    )


def decode_PredictionTopics(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionTopics:
    data = read_object(value)
    return PredictionTopics(
        topics=[decode_PredictionTopic(item0) for item0 in read_list(data["topics"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PredictionVenue(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionVenue:
    data = read_object(value)
    return PredictionVenue(
        excluded_reason=read_str(data["excluded_reason"])
        if data.get("excluded_reason") is not None
        else None,
        match=decode_VenueMatch(data["match"])
        if data.get("match") is not None
        else None,
        open_interest_usd=read_decimal(data["open_interest_usd"])
        if data.get("open_interest_usd") is not None
        else None,
        rules_text=read_str(data["rules_text"])
        if data.get("rules_text") is not None
        else None,
        rules_url=read_str(data["rules_url"])
        if data.get("rules_url") is not None
        else None,
        settlement=read_str(data["settlement"])
        if data.get("settlement") is not None
        else None,
        settlement_source=read_str(data["settlement_source"])
        if data.get("settlement_source") is not None
        else None,
        url=read_str(data["url"]),
        venue=read_str(data["venue"]),
        volume_24h_usd=read_decimal(data["volume_24h_usd"])
        if data.get("volume_24h_usd") is not None
        else None,
        weight=read_str(data["weight"]) if data.get("weight") is not None else None,
    )


def decode_PredictionWebhookEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionWebhookEvent:
    data = read_object(value)
    return PredictionWebhookEvent(
        closes_at=read_str(data["closes_at"])
        if data.get("closes_at") is not None
        else None,
        prediction_event_id=read_str(data["prediction_event_id"]),
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resolves_at=read_str(data["resolves_at"])
        if data.get("resolves_at") is not None
        else None,
        settlements=[
            decode_PredictionWebhookSettlement(item0)
            for item0 in read_list(data["settlements"])
        ],
        shape=read_str(data["shape"]),
        status=read_str(data["status"]),
        topic_id=read_str(data["topic_id"]),
    )


def decode_PredictionWebhookSettlement(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionWebhookSettlement:
    data = read_object(value)
    return PredictionWebhookSettlement(
        status=read_str(data["status"]),
        venue=read_str(data["venue"]),
    )


def decode_Problem(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> Problem:
    data = read_object(value)
    return Problem(
        code=read_str(data["code"]),
        detail=read_str(data["detail"]),
        request_id=read_str(data["request_id"]),
        status=read_int(data["status"]),
        title=read_str(data["title"]),
        type=read_str(data["type"]),
    )


def decode_Quote(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> Quote:
    data = read_object(value)
    return Quote(
        market_ids=[read_str(item0) for item0 in read_list(data["market_ids"])],
        probability=read_str(data["probability"]),
        venue=read_str(data["venue"]),
    )


def decode_RateHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> RateHistory:
    data = read_object(value)
    return RateHistory(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        country=read_str(data["country"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_RateHistoryObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        start=read_str(data["start"]) if data.get("start") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_RateHistoryObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> RateHistoryObservation:
    data = read_object(value)
    return RateHistoryObservation(
        period=read_str(data["period"]),
        rate=read_decimal(data["rate"]),
    )


def decode_ResourceHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ResourceHistory:
    data = read_object(value)
    return ResourceHistory(
        country=read_str(data["country"]),
        currency=read_str(data["currency"])
        if data.get("currency") is not None
        else None,
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_ResourceObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        series_id=read_str(data["series_id"]),
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        unit=read_str(data["unit"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_ResourceObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ResourceObservation:
    data = read_object(value)
    return ResourceObservation(
        period=read_str(data["period"]),
        released_on=read_str(data["released_on"])
        if data.get("released_on") is not None
        else None,
        status=read_str(data["status"]) if data.get("status") is not None else None,
        value=read_decimal(data["value"]),
    )


def decode_ScalarEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ScalarEvent:
    data = read_object(value)
    return ScalarEvent(
        above=[read_str(item0) for item0 in read_list(data["above"])],
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        closes_at=read_str(data["closes_at"])
        if data.get("closes_at") is not None
        else None,
        event_id=read_str(data["event_id"]),
        median=read_decimal(data["median"]) if data.get("median") is not None else None,
        outcomes=[decode_ScalarOutcome(item0) for item0 in read_list(data["outcomes"])],
        p10=read_decimal(data["p10"]) if data.get("p10") is not None else None,
        p90=read_decimal(data["p90"]) if data.get("p90") is not None else None,
        question=read_str(data["question"]),
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resolution=read_str(data["resolution"]),
        resolves_at=read_str(data["resolves_at"])
        if data.get("resolves_at") is not None
        else None,
        resolves_with=read_str(data["resolves_with"])
        if data.get("resolves_with") is not None
        else None,
        result=decode_PredictionResult(data["result"])
        if data.get("result") is not None
        else None,
        stale=read_bool(data["stale"]) if data.get("stale") is not None else None,
        status=read_str(data["status"]),
        topic_id=read_str(data["topic_id"]),
        unit=read_str(data["unit"]) if data.get("unit") is not None else None,
        venues=[decode_PredictionVenue(item0) for item0 in read_list(data["venues"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_ScalarOutcome(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ScalarOutcome:
    data = read_object(value)
    return ScalarOutcome(
        key=read_str(data["key"]),
        label=read_str(data["label"]),
        lower=read_decimal(data["lower"]) if data.get("lower") is not None else None,
        probability=read_str(data["probability"])
        if data.get("probability") is not None
        else None,
        quotes=[decode_Quote(item0) for item0 in read_list(data["quotes"])],
        upper=read_decimal(data["upper"]) if data.get("upper") is not None else None,
    )


def decode_SeriesSource(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> SeriesSource:
    data = read_object(value)
    return SeriesSource(
        distributor=read_str(data["distributor"]),
        publisher=read_str(data["publisher"]),
    )


def decode_TimingEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> TimingEvent:
    data = read_object(value)
    return TimingEvent(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        closes_at=read_str(data["closes_at"])
        if data.get("closes_at") is not None
        else None,
        event_id=read_str(data["event_id"]),
        not_within_window=read_str(data["not_within_window"])
        if data.get("not_within_window") is not None
        else None,
        question=read_str(data["question"]),
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resolution=read_str(data["resolution"]),
        resolves_at=read_str(data["resolves_at"])
        if data.get("resolves_at") is not None
        else None,
        resolves_with=read_str(data["resolves_with"])
        if data.get("resolves_with") is not None
        else None,
        result=decode_PredictionResult(data["result"])
        if data.get("result") is not None
        else None,
        stale=read_bool(data["stale"]) if data.get("stale") is not None else None,
        status=read_str(data["status"]),
        steps=[decode_TimingStep(item0) for item0 in read_list(data["steps"])],
        topic_id=read_str(data["topic_id"]),
        unit=read_str(data["unit"]) if data.get("unit") is not None else None,
        venues=[decode_PredictionVenue(item0) for item0 in read_list(data["venues"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_TimingStep(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> TimingStep:
    data = read_object(value)
    return TimingStep(
        by=read_str(data["by"]),
        key=read_str(data["key"]),
        kind=read_str(data["kind"]),
        label=read_str(data["label"]),
        probability=read_str(data["probability"])
        if data.get("probability") is not None
        else None,
        quotes=[decode_Quote(item0) for item0 in read_list(data["quotes"])],
    )


def decode_TopicCalendar(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> TopicCalendar:
    data = read_object(value)
    return TopicCalendar(
        country=read_str(data["country"]),
        family=read_str(data["family"]),
    )


def decode_TradeHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> TradeHistory:
    data = read_object(value)
    return TradeHistory(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        country=read_str(data["country"]),
        currency=read_str(data["currency"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_TradeHistoryObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        start=read_str(data["start"]) if data.get("start") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_TradeHistoryObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> TradeHistoryObservation:
    data = read_object(value)
    return TradeHistoryObservation(
        exports=read_decimal(data["exports"])
        if data.get("exports") is not None
        else None,
        imports=read_decimal(data["imports"])
        if data.get("imports") is not None
        else None,
        period=read_str(data["period"]),
    )


def decode_TradeSummary(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> TradeSummary:
    data = read_object(value)
    return TradeSummary(
        balance=read_decimal(data["balance"]),
        country=read_str(data["country"]),
        currency=read_str(data["currency"]),
        exports=read_decimal(data["exports"]),
        imports=read_decimal(data["imports"]),
        period=read_str(data["period"]),
        released_on=read_str(data["released_on"]),
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_Unemployment(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> Unemployment:
    data = read_object(value)
    return Unemployment(
        country=read_str(data["country"]),
        period=read_str(data["period"]),
        rate=read_decimal(data["rate"]),
        released_on=read_str(data["released_on"]),
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_VenueMatch(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> VenueMatch:
    data = read_object(value)
    return VenueMatch(
        differences=[read_str(item0) for item0 in read_list(data["differences"])],
        note=read_str(data["note"]) if data.get("note") is not None else None,
    )


def decode_WebhookConfigurationHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookConfigurationHistory:
    data = read_object(value)
    return WebhookConfigurationHistory(
        config_version=read_int(data["config_version"]),
        countries=[read_str(item0) for item0 in read_list(data["countries"])],
        enabled=read_bool(data["enabled"]),
        families=[read_str(item0) for item0 in read_list(data["families"])],
        recorded_at=read_str(data["recorded_at"]),
        url=read_str(data["url"]),
    )


def decode_WebhookDeliveriesResponse(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookDeliveriesResponse:
    data = read_object(value)
    return WebhookDeliveriesResponse(
        deliveries=[
            decode_WebhookDelivery(item0) for item0 in read_list(data["deliveries"])
        ],
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_WebhookDelivery(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookDelivery:
    data = read_object(value)
    return WebhookDelivery(
        attempts=read_int(data["attempts"]),
        config_version=read_int(data["config_version"]),
        created_at=read_str(data["created_at"]),
        delivery_id=read_str(data["delivery_id"]),
        event_cursor=read_int(data["event_cursor"])
        if data.get("event_cursor") is not None
        else None,
        is_test=read_bool(data["is_test"]) if data.get("is_test") is not None else None,
        last_error=read_str(data["last_error"])
        if data.get("last_error") is not None
        else None,
        last_status=read_int(data["last_status"])
        if data.get("last_status") is not None
        else None,
        next_attempt_at=read_str(data["next_attempt_at"])
        if data.get("next_attempt_at") is not None
        else None,
        replays=read_int(data["replays"]) if data.get("replays") is not None else None,
        retry_until=read_str(data["retry_until"])
        if data.get("retry_until") is not None
        else None,
        state=read_str(data["state"]),
        updated_at=read_str(data["updated_at"]),
    )


def decode_WebhookDestinationCreated(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookDestinationCreated:
    data = read_object(value)
    return WebhookDestinationCreated(
        config_version=read_int(data["config_version"]),
        countries=[read_str(item0) for item0 in read_list(data["countries"])],
        created_at=read_str(data["created_at"]),
        destination_id=read_str(data["destination_id"]),
        disabled_reason=read_str(data["disabled_reason"])
        if data.get("disabled_reason") is not None
        else None,
        enabled=read_bool(data["enabled"]),
        families=[read_str(item0) for item0 in read_list(data["families"])],
        secret=read_str(data["secret"]),
        secret_version=read_int(data["secret_version"]),
        updated_at=read_str(data["updated_at"]),
        url=read_str(data["url"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_WebhookDestinationInput(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookDestinationInput:
    data = read_object(value)
    return WebhookDestinationInput(
        countries=[read_str(item0) for item0 in read_list(data["countries"])],
        enabled=read_bool(data["enabled"]) if data.get("enabled") is not None else None,
        families=[read_str(item0) for item0 in read_list(data["families"])],
        url=read_str(data["url"]),
    )


def decode_WebhookDestinationList(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookDestinationList:
    data = read_object(value)
    return WebhookDestinationList(
        destination_limit=read_int(data["destination_limit"]),
        destinations=[
            decode_WebhookDestinationResponse(item0)
            for item0 in read_list(data["destinations"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_WebhookDestinationResponse(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookDestinationResponse:
    data = read_object(value)
    return WebhookDestinationResponse(
        config_version=read_int(data["config_version"]),
        countries=[read_str(item0) for item0 in read_list(data["countries"])],
        created_at=read_str(data["created_at"]),
        destination_id=read_str(data["destination_id"]),
        disabled_reason=read_str(data["disabled_reason"])
        if data.get("disabled_reason") is not None
        else None,
        enabled=read_bool(data["enabled"]),
        families=[read_str(item0) for item0 in read_list(data["families"])],
        secret_version=read_int(data["secret_version"]),
        updated_at=read_str(data["updated_at"]),
        url=read_str(data["url"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_WebhookEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookEvent:
    data = read_object(value)
    return WebhookEvent(
        country=read_str(data["country"]) if data.get("country") is not None else None,
        cursor=read_str(data["cursor"]) if data.get("cursor") is not None else None,
        event_id=read_str(data["event_id"]),
        family=read_str(data["family"]) if data.get("family") is not None else None,
        holiday_generation=read_int(data["holiday_generation"])
        if data.get("holiday_generation") is not None
        else None,
        holiday_year=read_int(data["holiday_year"])
        if data.get("holiday_year") is not None
        else None,
        prediction=decode_PredictionWebhookEvent(data["prediction"])
        if data.get("prediction") is not None
        else None,
        recorded_at=read_str(data["recorded_at"]),
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resource_id=read_str(data["resource_id"])
        if data.get("resource_id") is not None
        else None,
        resource_version=read_str(data["resource_version"])
        if data.get("resource_version") is not None
        else None,
        schema_version=read_str(data["schema_version"]),
        type=read_str(data["type"]),
    )


def decode_WebhookHistoryResponse(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookHistoryResponse:
    data = read_object(value)
    return WebhookHistoryResponse(
        history=[
            decode_WebhookConfigurationHistory(item0)
            for item0 in read_list(data["history"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_WebhookTestResponse(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookTestResponse:
    data = read_object(value)
    return WebhookTestResponse(
        delivery_id=read_str(data["delivery_id"])
        if data.get("delivery_id") is not None
        else None,
        retry_after_seconds=read_int(data["retry_after_seconds"])
        if data.get("retry_after_seconds") is not None
        else None,
        status=read_str(data["status"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_YieldCurve(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> YieldCurve:
    data = read_object(value)
    return YieldCurve(
        country=read_str(data["country"]),
        curve_type=read_str(data["curve_type"]),
        date=read_str(data["date"]),
        yields=[decode_YieldPoint(item0) for item0 in read_list(data["yields"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_YieldCurveHistoryObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> YieldCurveHistoryObservation:
    data = read_object(value)
    return YieldCurveHistoryObservation(
        date=read_str(data["date"]),
        yields=[decode_YieldPoint(item0) for item0 in read_list(data["yields"])],
    )


def decode_YieldCurveHistoryResponse(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> YieldCurveHistoryResponse:
    data = read_object(value)
    return YieldCurveHistoryResponse(
        country=read_str(data["country"]),
        curve_type=read_str(data["curve_type"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_YieldCurveHistoryObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_YieldPoint(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> YieldPoint:
    data = read_object(value)
    return YieldPoint(
        maturity=read_str(data["maturity"]),
        yield_percent=read_decimal(data["yield_percent"]),
    )


def decode_PalmoilHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilHistory:
    data = read_object(value)
    if data.get("next_cursor") is not None:
        read_cursor(data["next_cursor"])
    if data.get("unit") == "kilogram":
        return decode_PalmoilScheduleHistory(data, meta)
    if data.get("currency") == "MYR" and data.get("unit") == "metric_ton":
        return decode_PalmoilMarketHistory(data, meta)
    if data.get("currency") == "USD" and data.get("unit") == "metric_ton":
        return decode_PalmoilScalarHistory(data, meta)
    if data.get("unit") == "one_percent_oer":
        return decode_PalmoilFfbMarketHistory(data, meta)
    return PalmoilHistoryUnknown(
        data, meta if meta is not None else ResponseMeta(), raw_body
    )


def decode_PalmoilObservation(
    value: object,
    meta: ResponseMeta | None = None,
    raw_body: bytes = b"",
    *,
    page: object,
) -> PalmoilObservation:
    data = read_object(value)
    tags = read_object(page)
    if tags.get("unit") == "kilogram":
        return decode_PalmoilScheduleObservation(data, meta)
    if tags.get("currency") == "MYR" and tags.get("unit") == "metric_ton":
        return decode_PalmoilMarketObservation(data, meta)
    if tags.get("currency") == "USD" and tags.get("unit") == "metric_ton":
        return decode_PalmoilScalarObservation(data, meta)
    if tags.get("unit") == "one_percent_oer":
        return decode_PalmoilFfbObservation(data, meta)
    return PalmoilObservationUnknown(
        data, meta if meta is not None else ResponseMeta(), raw_body
    )


def decode_PalmoilPrice(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilPrice:
    data = read_object(value)
    if data.get("unit") == "kilogram":
        return decode_PalmoilSchedulePrice(data, meta)
    if data.get("currency") == "MYR" and data.get("unit") == "metric_ton":
        return decode_PalmoilMarketPrice(data, meta)
    if data.get("currency") == "USD" and data.get("unit") == "metric_ton":
        return decode_PalmoilScalarPrice(data, meta)
    if data.get("unit") == "one_percent_oer":
        return decode_PalmoilFfbMarketPrice(data, meta)
    return PalmoilPriceUnknown(
        data, meta if meta is not None else ResponseMeta(), raw_body
    )


def decode_PalmoilSeries(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PalmoilSeries:
    data = read_object(value)
    if data.get("observation_type") == "age_schedule":
        return decode_PalmoilScheduleSeries(data, meta)
    if data.get("observation_type") == "scalar":
        return decode_PalmoilScalarSeries(data, meta)
    return PalmoilSeriesUnknown(
        data, meta if meta is not None else ResponseMeta(), raw_body
    )

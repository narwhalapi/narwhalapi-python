# Generated from spec/live/openapi.json sha256 549d8458a8dcfbbccea3ea4b23f7d9163c6525ce932e4c5f6657fdd9b728985c. Do not edit.
# Generated from spec/next/openapi.json sha256 549d8458a8dcfbbccea3ea4b23f7d9163c6525ce932e4c5f6657fdd9b728985c. Do not edit.
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


class Annualization:
    """Known values; response fields also accept future strings."""

    ANNUALIZED: Literal["annualized"] = "annualized"
    NOT_ANNUALIZED: Literal["not_annualized"] = "not_annualized"


class BarInterval:
    """Known values; response fields also accept future strings."""

    V15M: Literal["15m"] = "15m"
    V1D: Literal["1d"] = "1d"
    V1H: Literal["1h"] = "1h"
    V1M: Literal["1m"] = "1m"
    V4H: Literal["4h"] = "4h"
    V5M: Literal["5m"] = "5m"


class CentralBank:
    """Known values; response fields also accept future strings."""

    BANK_INDONESIA: Literal["bank-indonesia"] = "bank-indonesia"
    BANK_OF_CANADA: Literal["bank-of-canada"] = "bank-of-canada"
    BANK_OF_ENGLAND: Literal["bank-of-england"] = "bank-of-england"
    BANK_OF_JAPAN: Literal["bank-of-japan"] = "bank-of-japan"
    EUROPEAN_CENTRAL_BANK: Literal["european-central-bank"] = "european-central-bank"
    FEDERAL_RESERVE: Literal["federal-reserve"] = "federal-reserve"
    RESERVE_BANK_OF_AUSTRALIA: Literal["reserve-bank-of-australia"] = (
        "reserve-bank-of-australia"
    )


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


class ExtremeObservation:
    """Known values; response fields also accept future strings."""

    ANY_RELEASE: Literal["any_release"] = "any_release"
    ANY_TRADE: Literal["any_trade"] = "any_trade"
    CLOSE: Literal["close"] = "close"


class GrowthSeasonalAdjustment:
    """Known values; response fields also accept future strings."""

    MIXED: Literal["mixed"] = "mixed"
    NOT_SEASONALLY_ADJUSTED: Literal["not_seasonally_adjusted"] = (
        "not_seasonally_adjusted"
    )
    SEASONALLY_ADJUSTED: Literal["seasonally_adjusted"] = "seasonally_adjusted"


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


class IndicatorValueStatus:
    """Known values; response fields also accept future strings."""

    AVAILABLE: Literal["available"] = "available"
    NOT_RELEASED: Literal["not_released"] = "not_released"
    PENDING_CAPTURE: Literal["pending_capture"] = "pending_capture"
    UNAVAILABLE: Literal["unavailable"] = "unavailable"


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


class PredictionInterval:
    """Known values; response fields also accept future strings."""

    V1D: Literal["1d"] = "1d"
    V1H: Literal["1h"] = "1h"
    V1M: Literal["1m"] = "1m"
    V5M: Literal["5m"] = "5m"


class PredictionShape:
    """Known values; response fields also accept future strings."""

    BINARY: Literal["binary"] = "binary"
    CATEGORICAL: Literal["categorical"] = "categorical"
    EXTREME: Literal["extreme"] = "extreme"
    SCALAR: Literal["scalar"] = "scalar"
    SET: Literal["set"] = "set"
    TIMING: Literal["timing"] = "timing"


class ProducerArrangement:
    """Known values; response fields also accept future strings."""

    PURCHASE_AGREEMENT: Literal["purchase_agreement"] = "purchase_agreement"
    SUPPORTED_SCHEME: Literal["supported_scheme"] = "supported_scheme"


class QuoteFreshness:
    """Known values; response fields also accept future strings."""

    LIVE: Literal["live"] = "live"
    NO_LIVE_QUOTES: Literal["no_live_quotes"] = "no_live_quotes"
    STALE: Literal["stale"] = "stale"


class QuoteRole:
    """Known values; response fields also accept future strings."""

    BLENDED: Literal["blended"] = "blended"
    EXCLUDED: Literal["excluded"] = "excluded"


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


class SchedulePrecision:
    """Known values; response fields also accept future strings."""

    DATE: Literal["date"] = "date"
    DEADLINE: Literal["deadline"] = "deadline"
    ESTIMATED_RANGE: Literal["estimated_range"] = "estimated_range"
    EXACT: Literal["exact"] = "exact"
    UNKNOWN: Literal["unknown"] = "unknown"


class ScheduleTimeBasis:
    """Known values; response fields also accept future strings."""

    CALENDAR: Literal["calendar"] = "calendar"
    STANDARD_TIME: Literal["standard_time"] = "standard_time"


class SeasonalAdjustment:
    """Known values; response fields also accept future strings."""

    NOT_SEASONALLY_ADJUSTED: Literal["not_seasonally_adjusted"] = (
        "not_seasonally_adjusted"
    )
    SEASONALLY_ADJUSTED: Literal["seasonally_adjusted"] = "seasonally_adjusted"


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


class ValueScale:
    """Known values; response fields also accept future strings."""

    BILLIONS: Literal["billions"] = "billions"
    HUNDRED_MILLIONS: Literal["hundred_millions"] = "hundred_millions"
    MILLIONS: Literal["millions"] = "millions"
    THOUSANDS: Literal["thousands"] = "thousands"
    UNITS: Literal["units"] = "units"


class ValueTransformation:
    """Known values; response fields also accept future strings."""

    CHANGE: Literal["change"] = "change"
    LEVEL: Literal["level"] = "level"
    MONTH_OVER_MONTH: Literal["month_over_month"] = "month_over_month"
    QUARTER_OVER_QUARTER: Literal["quarter_over_quarter"] = "quarter_over_quarter"
    THREE_MONTH_ON_THREE_MONTH: Literal["three_month_on_three_month"] = (
        "three_month_on_three_month"
    )
    YEAR_OVER_YEAR: Literal["year_over_year"] = "year_over_year"


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
class BinaryBody:
    deadline: str | None = None
    labels: BinaryLabels
    probability: str | None = None
    quotes: list[Quote]


@dataclass(frozen=True, slots=True, kw_only=True)
class BinaryEvent:
    as_of: str | None = None
    body: BinaryBody
    closes_at: str | None = None
    event_id: str
    quality: PredictionQuality
    question: str
    release_id: str | None = None
    resolution: PredictionResolution
    resolves_at: str | None = None
    shape: str
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
    nationwide: bool
    scope: str
    subdivision_codes: list[str] | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class CalendarHoliday:
    date: str
    local_name: str | None = None
    name: str
    nationwide: bool
    observed: bool | None = None
    scope: str
    subdivision_codes: list[str] | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class CalendarHolidays:
    country: str
    coverage: list[CalendarCoverage]
    holidays: list[CalendarHoliday]
    year: int
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CalendarHolidaysOnDate:
    country: str
    coverage: list[CalendarCoverage]
    date: str
    holidays: list[CalendarHoliday]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CalendarNextHoliday:
    country: str
    coverage: list[CalendarCoverage]
    from_date: str
    holiday: CalendarHoliday | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CalendarSubscriptionCreated:
    expires_at: str
    refresh_note: str | None = None
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
class CalendarSubscriptionRevoked:
    revoked: bool | None = None
    subscription_id: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


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
    end: str
    interval: str
    next_cursor: str | None = None
    start: str
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
    base_period: str
    base_value: Decimal
    country: str
    period: str
    released_on: str
    source: SeriesSource | None = None
    value: Decimal
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class DeliveryEvent:
    country: str
    cursor: str
    event_id: str
    event_type: str
    family: str
    holiday_country: str | None = None
    holiday_generation: int | None = None
    holiday_year: int | None = None
    publication_id: str | None = None
    recorded_at: str
    release_id: str | None = None
    resource_id: str | None = None
    resource_version: str | None = None
    schema_version: str | None = None
    type: str


@dataclass(frozen=True, slots=True, kw_only=True)
class EconomicCalendar:
    as_of: str
    next_cursor: str | None = None
    releases: list[EconomicRelease]
    snapshot: str
    status: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EconomicRelease:
    country: str
    family: str
    indicators: list[EconomicReleaseIndicator] | None = None
    name: str
    notice: str | None = None
    observed_at: str | None = None
    officially_published_at: str | None = None
    reference_period: str | None = None
    release_id: str
    revision: int | None = None
    schedule: EconomicReleaseSchedule
    series_id: str | None = None
    stage: str | None = None
    status: str
    title: str
    topic: str | None = None
    variant: str | None = None
    version: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EconomicReleaseIndicator:
    actual: Decimal | None = None
    actual_as_of: str | None = None
    annualization: str | None = None
    currency: str | None = None
    index_base: str | None = None
    measure: str
    period: str
    previous: Decimal | None = None
    previous_as_of: str | None = None
    previous_before_revision: Decimal | None = None
    previous_period: str
    scale: str | None = None
    seasonal_adjustment: str
    title: str
    transformation: str
    unit: str
    value_status: str


@dataclass(frozen=True, slots=True, kw_only=True)
class EconomicReleaseSchedule:
    at: str | None = None
    date: str | None = None
    local_date: str | None = None
    precision: str
    time_basis: str | None = None
    timezone: str | None = None
    until: str | None = None
    until_date: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class EventDetail:
    event: DeliveryEvent
    status: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EventsPage:
    cursor: str
    events: list[DeliveryEvent]
    next_cursor: str | None = None
    status: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class ExtremeBody:
    down: list[ExtremeLevel]
    observation: str
    up: list[ExtremeLevel]
    window: ExtremeWindow


@dataclass(frozen=True, slots=True, kw_only=True)
class ExtremeEvent:
    as_of: str | None = None
    body: ExtremeBody
    closes_at: str | None = None
    event_id: str
    quality: PredictionQuality
    question: str
    release_id: str | None = None
    resolution: PredictionResolution
    resolves_at: str | None = None
    shape: str
    status: str
    topic_id: str
    unit: str | None = None
    venues: list[PredictionVenue]
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
    end: str
    interval: str
    next_cursor: str | None = None
    start: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class FxConversion:
    amount: Decimal
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
    end_date: str
    has_more: bool
    next_cursor: str | None = None
    observations: list[FxHistoricalObservation]
    start_date: str
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
    annualization: str
    country: str
    currency: str
    period: str
    price_basis: str
    released_on: str
    seasonal_adjustment: str
    source: SeriesSource | None = None
    value: Decimal
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class GdpGrowth:
    annualization: str
    country: str
    period: str
    price_basis: str
    quarter_over_quarter: Decimal
    quarter_over_quarter_seasonal_adjustment: str | None = None
    released_on: str
    seasonal_adjustment: str
    source: SeriesSource | None = None
    unit: str
    year_over_year: Decimal
    year_over_year_seasonal_adjustment: str | None = None
    year_to_date: Decimal | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class HistoricalEconomicsResponse:
    as_of: str | None = None
    next_cursor: str | None = None
    observations: list[HistoricalObservation]
    source: SeriesSource | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class HistoricalObservation:
    country: str
    measure: str
    period: str
    transformation: str
    unit: str
    value: Decimal


@dataclass(frozen=True, slots=True, kw_only=True)
class Inflation:
    country: str
    month_over_month: Decimal
    period: str
    released_on: str
    source: SeriesSource | None = None
    unit: str
    year_over_year: Decimal
    year_to_date: Decimal | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class LabourForceParticipation:
    country: str
    period: str
    rate: Decimal
    released_on: str
    source: SeriesSource | None = None
    unit: str
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
    commodity: str
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
    commodity: str
    country: str
    coverage_end: str
    coverage_start: str
    currency: str
    frequency: str
    observation_type: str
    period_type: str
    price_type: str
    producer_arrangement: str | None = None
    producer_type: str
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
    attribution: str | None = None
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
    attribution: str | None = None
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
    attribution: str | None = None
    basis: str | None = None
    category: str
    commodity: str
    coverage_end: str
    coverage_start: str
    currency: str
    description: str
    frequency: str
    market: str
    price_type: str
    product: str
    publisher: str
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
    authority: str
    meetings: list[PolicyPathMeeting]
    method: str
    unit: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PolicyPathDay:
    date: str
    meetings: list[PolicyPathMeeting]


@dataclass(frozen=True, slots=True, kw_only=True)
class PolicyPathHistory:
    authority: str
    days: list[PolicyPathDay]
    method: str
    unit: str
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
class PredictionBar:
    close: str
    end: str
    high: str | None = None
    low: str | None = None
    open: str | None = None
    start: str


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionEventSummary:
    as_of: str | None = None
    closes_at: str | None = None
    event_id: str
    question: str
    release_id: str | None = None
    resolves_at: str | None = None
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
    captured_from: str | None = None
    end: str
    event_id: str
    interval: str
    series: list[PredictionSeries]
    shape: str
    start: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionQuality:
    freshness: str
    monotone_repairs: int
    rows_merged: int


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionResolution:
    description: str
    resolves_with: str | None = None


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
    events: list[PredictionEventSummary]
    group: str
    next_event_id: str | None = None
    resolution_kind: str
    shape: str
    title: str
    topic_id: str
    unit: str | None = None
    venues: list[str]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionTopics:
    topics: list[PredictionTopic]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class PredictionVenue:
    depth_usd: Decimal | None = None
    excluded_reason: str | None = None
    fetched_at: str | None = None
    match: VenueMatch
    open_interest_usd: Decimal | None = None
    role: str
    rules_text: str | None = None
    rules_url: str | None = None
    settlement: VenueSettlement
    settlement_source: str | None = None
    url: str
    venue: str
    venue_event_id: str
    volume_24h_usd: Decimal | None = None
    weight: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class Problem:
    code: str
    detail: str
    instance: str | None = None
    ok: bool | None = None
    request_id: str
    status: int
    title: str
    type: str


@dataclass(frozen=True, slots=True, kw_only=True)
class Quote:
    market_ids: list[str]
    probability: str
    role: str
    venue: str


@dataclass(frozen=True, slots=True, kw_only=True)
class ScalarBody:
    outcomes: list[ScalarOutcome]
    scale: int
    summary: ScalarSummary | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class ScalarEvent:
    as_of: str | None = None
    body: ScalarBody
    closes_at: str | None = None
    event_id: str
    quality: PredictionQuality
    question: str
    release_id: str | None = None
    resolution: PredictionResolution
    resolves_at: str | None = None
    shape: str
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
class ScalarSummary:
    bounds: ScalarSummaryBounds | None = None
    median: Decimal | None = None
    method: str
    p10: Decimal | None = None
    p90: Decimal | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class ScalarSummaryBounds:
    median: str | None = None
    p10: str | None = None
    p90: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class SeriesSource:
    distributor: str
    publisher: str
    released_on_basis: str


@dataclass(frozen=True, slots=True, kw_only=True)
class TimingBody:
    not_within_window: str | None = None
    steps: list[TimingStep]


@dataclass(frozen=True, slots=True, kw_only=True)
class TimingEvent:
    as_of: str | None = None
    body: TimingBody
    closes_at: str | None = None
    event_id: str
    quality: PredictionQuality
    question: str
    release_id: str | None = None
    resolution: PredictionResolution
    resolves_at: str | None = None
    shape: str
    status: str
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
    variant: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class TradeExports:
    country: str
    coverage: str
    currency: str
    flow: str
    partner: str | None = None
    period: str
    product: TradeProductFilter | None = None
    released_on: str
    source: SeriesSource | None = None
    value: Decimal
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class TradeImports:
    country: str
    coverage: str
    currency: str
    flow: str
    partner: str | None = None
    period: str
    product: TradeProductFilter | None = None
    released_on: str
    source: SeriesSource | None = None
    value: Decimal
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class TradeProductFilter:
    classification: str
    code: str


@dataclass(frozen=True, slots=True, kw_only=True)
class TradeSummary:
    balance: Decimal
    country: str
    coverage: str
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
    unit: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class VenueMatch:
    differences: list[str]
    note: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class VenueSettlement:
    status: str


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookConfigurationHistory:
    activation_snapshot: str
    countries: list[str]
    destination_id: str
    enabled: bool
    families: list[str]
    recorded_at: str
    url: str
    version: int


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookDeleteResponse:
    deleted: bool | None = None
    destination_id: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookDeliveriesResponse:
    deliveries: list[WebhookDelivery]
    limit: int
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
    next_attempt_at: str
    replays: int
    retry_until: str
    state: str
    updated_at: str


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookDestinationCreated:
    config_version: int
    countries: list[str]
    created_at: str
    destination_id: str
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
    destinations: list[WebhookDestinationResponse]
    limit: int
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookDestinationResponse:
    config_version: int
    countries: list[str]
    created_at: str
    destination_id: str
    enabled: bool
    families: list[str]
    secret_version: int
    updated_at: str
    url: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookHistoryResponse:
    history: list[WebhookConfigurationHistory]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookReplayResponse:
    delivery_id: str
    replayed: bool
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class WebhookTestResponse:
    delivery_id: str | None = None
    destination_id: str
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


def decode_BinaryBody(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> BinaryBody:
    data = read_object(value)
    return BinaryBody(
        deadline=read_str(data["deadline"])
        if data.get("deadline") is not None
        else None,
        labels=decode_BinaryLabels(data["labels"]),
        probability=read_str(data["probability"])
        if data.get("probability") is not None
        else None,
        quotes=[decode_Quote(item0) for item0 in read_list(data["quotes"])],
    )


def decode_BinaryEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> BinaryEvent:
    data = read_object(value)
    return BinaryEvent(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        body=decode_BinaryBody(data["body"]),
        closes_at=read_str(data["closes_at"])
        if data.get("closes_at") is not None
        else None,
        event_id=read_str(data["event_id"]),
        quality=decode_PredictionQuality(data["quality"]),
        question=read_str(data["question"]),
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resolution=decode_PredictionResolution(data["resolution"]),
        resolves_at=read_str(data["resolves_at"])
        if data.get("resolves_at") is not None
        else None,
        shape=read_str(data["shape"]),
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
        nationwide=read_bool(data["nationwide"]),
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
        nationwide=read_bool(data["nationwide"]),
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
        year=read_int(data["year"]),
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
        date=read_str(data["date"]),
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
        from_date=read_str(data["from_date"]),
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
        refresh_note=read_str(data["refresh_note"])
        if data.get("refresh_note") is not None
        else None,
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


def decode_CalendarSubscriptionRevoked(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CalendarSubscriptionRevoked:
    data = read_object(value)
    return CalendarSubscriptionRevoked(
        revoked=read_bool(data["revoked"]) if data.get("revoked") is not None else None,
        subscription_id=read_str(data["subscription_id"]),
        meta=meta if meta is not None else ResponseMeta(),
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
        end=read_str(data["end"]),
        interval=read_str(data["interval"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        start=read_str(data["start"]),
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
        base_period=read_str(data["base_period"]),
        base_value=read_decimal(data["base_value"]),
        country=read_str(data["country"]),
        period=read_str(data["period"]),
        released_on=read_str(data["released_on"]),
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        value=read_decimal(data["value"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_DeliveryEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> DeliveryEvent:
    data = read_object(value)
    return DeliveryEvent(
        country=read_str(data["country"]),
        cursor=read_str(data["cursor"]),
        event_id=read_str(data["event_id"]),
        event_type=read_str(data["event_type"]),
        family=read_str(data["family"]),
        holiday_country=read_str(data["holiday_country"])
        if data.get("holiday_country") is not None
        else None,
        holiday_generation=read_int(data["holiday_generation"])
        if data.get("holiday_generation") is not None
        else None,
        holiday_year=read_int(data["holiday_year"])
        if data.get("holiday_year") is not None
        else None,
        publication_id=read_str(data["publication_id"])
        if data.get("publication_id") is not None
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
        schema_version=read_str(data["schema_version"])
        if data.get("schema_version") is not None
        else None,
        type=read_str(data["type"]),
    )


def decode_EconomicCalendar(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EconomicCalendar:
    data = read_object(value)
    return EconomicCalendar(
        as_of=read_str(data["as_of"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        releases=[
            decode_EconomicRelease(item0) for item0 in read_list(data["releases"])
        ],
        snapshot=read_str(data["snapshot"]),
        status=read_str(data["status"]) if data.get("status") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EconomicRelease(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EconomicRelease:
    data = read_object(value)
    return EconomicRelease(
        country=read_str(data["country"]),
        family=read_str(data["family"]),
        indicators=[
            decode_EconomicReleaseIndicator(item0)
            for item0 in read_list(data["indicators"])
        ]
        if data.get("indicators") is not None
        else None,
        name=read_str(data["name"]),
        notice=read_str(data["notice"]) if data.get("notice") is not None else None,
        observed_at=read_str(data["observed_at"])
        if data.get("observed_at") is not None
        else None,
        officially_published_at=read_str(data["officially_published_at"])
        if data.get("officially_published_at") is not None
        else None,
        reference_period=read_str(data["reference_period"])
        if data.get("reference_period") is not None
        else None,
        release_id=read_str(data["release_id"]),
        revision=read_int(data["revision"])
        if data.get("revision") is not None
        else None,
        schedule=decode_EconomicReleaseSchedule(data["schedule"]),
        series_id=read_str(data["series_id"])
        if data.get("series_id") is not None
        else None,
        stage=read_str(data["stage"]) if data.get("stage") is not None else None,
        status=read_str(data["status"]),
        title=read_str(data["title"]),
        topic=read_str(data["topic"]) if data.get("topic") is not None else None,
        variant=read_str(data["variant"]) if data.get("variant") is not None else None,
        version=read_str(data["version"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EconomicReleaseIndicator(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EconomicReleaseIndicator:
    data = read_object(value)
    return EconomicReleaseIndicator(
        actual=read_decimal(data["actual"]) if data.get("actual") is not None else None,
        actual_as_of=read_str(data["actual_as_of"])
        if data.get("actual_as_of") is not None
        else None,
        annualization=read_str(data["annualization"])
        if data.get("annualization") is not None
        else None,
        currency=read_str(data["currency"])
        if data.get("currency") is not None
        else None,
        index_base=read_str(data["index_base"])
        if data.get("index_base") is not None
        else None,
        measure=read_str(data["measure"]),
        period=read_str(data["period"]),
        previous=read_decimal(data["previous"])
        if data.get("previous") is not None
        else None,
        previous_as_of=read_str(data["previous_as_of"])
        if data.get("previous_as_of") is not None
        else None,
        previous_before_revision=read_decimal(data["previous_before_revision"])
        if data.get("previous_before_revision") is not None
        else None,
        previous_period=read_str(data["previous_period"]),
        scale=read_str(data["scale"]) if data.get("scale") is not None else None,
        seasonal_adjustment=read_str(data["seasonal_adjustment"]),
        title=read_str(data["title"]),
        transformation=read_str(data["transformation"]),
        unit=read_str(data["unit"]),
        value_status=read_str(data["value_status"]),
    )


def decode_EconomicReleaseSchedule(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EconomicReleaseSchedule:
    data = read_object(value)
    return EconomicReleaseSchedule(
        at=read_str(data["at"]) if data.get("at") is not None else None,
        date=read_str(data["date"]) if data.get("date") is not None else None,
        local_date=read_str(data["local_date"])
        if data.get("local_date") is not None
        else None,
        precision=read_str(data["precision"]),
        time_basis=read_str(data["time_basis"])
        if data.get("time_basis") is not None
        else None,
        timezone=read_str(data["timezone"])
        if data.get("timezone") is not None
        else None,
        until=read_str(data["until"]) if data.get("until") is not None else None,
        until_date=read_str(data["until_date"])
        if data.get("until_date") is not None
        else None,
    )


def decode_EventDetail(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EventDetail:
    data = read_object(value)
    return EventDetail(
        event=decode_DeliveryEvent(data["event"]),
        status=read_str(data["status"]) if data.get("status") is not None else None,
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
        status=read_str(data["status"]) if data.get("status") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_ExtremeBody(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ExtremeBody:
    data = read_object(value)
    return ExtremeBody(
        down=[decode_ExtremeLevel(item0) for item0 in read_list(data["down"])],
        observation=read_str(data["observation"]),
        up=[decode_ExtremeLevel(item0) for item0 in read_list(data["up"])],
        window=decode_ExtremeWindow(data["window"]),
    )


def decode_ExtremeEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ExtremeEvent:
    data = read_object(value)
    return ExtremeEvent(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        body=decode_ExtremeBody(data["body"]),
        closes_at=read_str(data["closes_at"])
        if data.get("closes_at") is not None
        else None,
        event_id=read_str(data["event_id"]),
        quality=decode_PredictionQuality(data["quality"]),
        question=read_str(data["question"]),
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resolution=decode_PredictionResolution(data["resolution"]),
        resolves_at=read_str(data["resolves_at"])
        if data.get("resolves_at") is not None
        else None,
        shape=read_str(data["shape"]),
        status=read_str(data["status"]),
        topic_id=read_str(data["topic_id"]),
        unit=read_str(data["unit"]) if data.get("unit") is not None else None,
        venues=[decode_PredictionVenue(item0) for item0 in read_list(data["venues"])],
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
        end=read_str(data["end"]),
        interval=read_str(data["interval"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        start=read_str(data["start"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_FxConversion(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FxConversion:
    data = read_object(value)
    return FxConversion(
        amount=read_decimal(data["amount"]),
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
        end_date=read_str(data["end_date"]),
        has_more=read_bool(data["has_more"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_FxHistoricalObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        start_date=read_str(data["start_date"]),
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
        annualization=read_str(data["annualization"]),
        country=read_str(data["country"]),
        currency=read_str(data["currency"]),
        period=read_str(data["period"]),
        price_basis=read_str(data["price_basis"]),
        released_on=read_str(data["released_on"]),
        seasonal_adjustment=read_str(data["seasonal_adjustment"]),
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
        annualization=read_str(data["annualization"]),
        country=read_str(data["country"]),
        period=read_str(data["period"]),
        price_basis=read_str(data["price_basis"]),
        quarter_over_quarter=read_decimal(data["quarter_over_quarter"]),
        quarter_over_quarter_seasonal_adjustment=read_str(
            data["quarter_over_quarter_seasonal_adjustment"]
        )
        if data.get("quarter_over_quarter_seasonal_adjustment") is not None
        else None,
        released_on=read_str(data["released_on"]),
        seasonal_adjustment=read_str(data["seasonal_adjustment"]),
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        unit=read_str(data["unit"]),
        year_over_year=read_decimal(data["year_over_year"]),
        year_over_year_seasonal_adjustment=read_str(
            data["year_over_year_seasonal_adjustment"]
        )
        if data.get("year_over_year_seasonal_adjustment") is not None
        else None,
        year_to_date=read_decimal(data["year_to_date"])
        if data.get("year_to_date") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_HistoricalEconomicsResponse(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> HistoricalEconomicsResponse:
    data = read_object(value)
    return HistoricalEconomicsResponse(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_HistoricalObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_HistoricalObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> HistoricalObservation:
    data = read_object(value)
    return HistoricalObservation(
        country=read_str(data["country"]),
        measure=read_str(data["measure"]),
        period=read_str(data["period"]),
        transformation=read_str(data["transformation"]),
        unit=read_str(data["unit"]),
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
        unit=read_str(data["unit"]),
        year_over_year=read_decimal(data["year_over_year"]),
        year_to_date=read_decimal(data["year_to_date"])
        if data.get("year_to_date") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
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
        unit=read_str(data["unit"]),
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
        commodity=read_str(data["commodity"]),
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
        commodity=read_str(data["commodity"]),
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
        producer_type=read_str(data["producer_type"]),
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
        attribution=read_str(data["attribution"])
        if data.get("attribution") is not None
        else None,
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
        attribution=read_str(data["attribution"])
        if data.get("attribution") is not None
        else None,
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
        attribution=read_str(data["attribution"])
        if data.get("attribution") is not None
        else None,
        basis=read_str(data["basis"]) if data.get("basis") is not None else None,
        category=read_str(data["category"]),
        commodity=read_str(data["commodity"]),
        coverage_end=read_str(data["coverage_end"]),
        coverage_start=read_str(data["coverage_start"]),
        currency=read_str(data["currency"]),
        description=read_str(data["description"]),
        frequency=read_str(data["frequency"]),
        market=read_str(data["market"]),
        price_type=read_str(data["price_type"]),
        product=read_str(data["product"]),
        publisher=read_str(data["publisher"]),
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
        authority=read_str(data["authority"]),
        meetings=[
            decode_PolicyPathMeeting(item0) for item0 in read_list(data["meetings"])
        ],
        method=read_str(data["method"]),
        unit=read_str(data["unit"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PolicyPathDay(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PolicyPathDay:
    data = read_object(value)
    return PolicyPathDay(
        date=read_str(data["date"]),
        meetings=[
            decode_PolicyPathMeeting(item0) for item0 in read_list(data["meetings"])
        ],
    )


def decode_PolicyPathHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PolicyPathHistory:
    data = read_object(value)
    return PolicyPathHistory(
        authority=read_str(data["authority"]),
        days=[decode_PolicyPathDay(item0) for item0 in read_list(data["days"])],
        method=read_str(data["method"]),
        unit=read_str(data["unit"]),
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


def decode_PredictionBar(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionBar:
    data = read_object(value)
    return PredictionBar(
        close=read_str(data["close"]),
        end=read_str(data["end"]),
        high=read_str(data["high"]) if data.get("high") is not None else None,
        low=read_str(data["low"]) if data.get("low") is not None else None,
        open=read_str(data["open"]) if data.get("open") is not None else None,
        start=read_str(data["start"]),
    )


def decode_PredictionEventSummary(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionEventSummary:
    data = read_object(value)
    return PredictionEventSummary(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
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
        captured_from=read_str(data["captured_from"])
        if data.get("captured_from") is not None
        else None,
        end=read_str(data["end"]),
        event_id=read_str(data["event_id"]),
        interval=read_str(data["interval"]),
        series=[decode_PredictionSeries(item0) for item0 in read_list(data["series"])],
        shape=read_str(data["shape"]),
        start=read_str(data["start"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_PredictionQuality(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionQuality:
    data = read_object(value)
    return PredictionQuality(
        freshness=read_str(data["freshness"]),
        monotone_repairs=read_int(data["monotone_repairs"]),
        rows_merged=read_int(data["rows_merged"]),
    )


def decode_PredictionResolution(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PredictionResolution:
    data = read_object(value)
    return PredictionResolution(
        description=read_str(data["description"]),
        resolves_with=read_str(data["resolves_with"])
        if data.get("resolves_with") is not None
        else None,
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
            decode_PredictionEventSummary(item0) for item0 in read_list(data["events"])
        ],
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
        meta=meta if meta is not None else ResponseMeta(),
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
        depth_usd=read_decimal(data["depth_usd"])
        if data.get("depth_usd") is not None
        else None,
        excluded_reason=read_str(data["excluded_reason"])
        if data.get("excluded_reason") is not None
        else None,
        fetched_at=read_str(data["fetched_at"])
        if data.get("fetched_at") is not None
        else None,
        match=decode_VenueMatch(data["match"]),
        open_interest_usd=read_decimal(data["open_interest_usd"])
        if data.get("open_interest_usd") is not None
        else None,
        role=read_str(data["role"]),
        rules_text=read_str(data["rules_text"])
        if data.get("rules_text") is not None
        else None,
        rules_url=read_str(data["rules_url"])
        if data.get("rules_url") is not None
        else None,
        settlement=decode_VenueSettlement(data["settlement"]),
        settlement_source=read_str(data["settlement_source"])
        if data.get("settlement_source") is not None
        else None,
        url=read_str(data["url"]),
        venue=read_str(data["venue"]),
        venue_event_id=read_str(data["venue_event_id"]),
        volume_24h_usd=read_decimal(data["volume_24h_usd"])
        if data.get("volume_24h_usd") is not None
        else None,
        weight=read_str(data["weight"]) if data.get("weight") is not None else None,
    )


def decode_Problem(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> Problem:
    data = read_object(value)
    return Problem(
        code=read_str(data["code"]),
        detail=read_str(data["detail"]),
        instance=read_str(data["instance"])
        if data.get("instance") is not None
        else None,
        ok=read_bool(data["ok"]) if data.get("ok") is not None else None,
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
        role=read_str(data["role"]),
        venue=read_str(data["venue"]),
    )


def decode_ScalarBody(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ScalarBody:
    data = read_object(value)
    return ScalarBody(
        outcomes=[decode_ScalarOutcome(item0) for item0 in read_list(data["outcomes"])],
        scale=read_int(data["scale"]),
        summary=decode_ScalarSummary(data["summary"])
        if data.get("summary") is not None
        else None,
    )


def decode_ScalarEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ScalarEvent:
    data = read_object(value)
    return ScalarEvent(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        body=decode_ScalarBody(data["body"]),
        closes_at=read_str(data["closes_at"])
        if data.get("closes_at") is not None
        else None,
        event_id=read_str(data["event_id"]),
        quality=decode_PredictionQuality(data["quality"]),
        question=read_str(data["question"]),
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resolution=decode_PredictionResolution(data["resolution"]),
        resolves_at=read_str(data["resolves_at"])
        if data.get("resolves_at") is not None
        else None,
        shape=read_str(data["shape"]),
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


def decode_ScalarSummary(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ScalarSummary:
    data = read_object(value)
    return ScalarSummary(
        bounds=decode_ScalarSummaryBounds(data["bounds"])
        if data.get("bounds") is not None
        else None,
        median=read_decimal(data["median"]) if data.get("median") is not None else None,
        method=read_str(data["method"]),
        p10=read_decimal(data["p10"]) if data.get("p10") is not None else None,
        p90=read_decimal(data["p90"]) if data.get("p90") is not None else None,
    )


def decode_ScalarSummaryBounds(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ScalarSummaryBounds:
    data = read_object(value)
    return ScalarSummaryBounds(
        median=read_str(data["median"]) if data.get("median") is not None else None,
        p10=read_str(data["p10"]) if data.get("p10") is not None else None,
        p90=read_str(data["p90"]) if data.get("p90") is not None else None,
    )


def decode_SeriesSource(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> SeriesSource:
    data = read_object(value)
    return SeriesSource(
        distributor=read_str(data["distributor"]),
        publisher=read_str(data["publisher"]),
        released_on_basis=read_str(data["released_on_basis"]),
    )


def decode_TimingBody(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> TimingBody:
    data = read_object(value)
    return TimingBody(
        not_within_window=read_str(data["not_within_window"])
        if data.get("not_within_window") is not None
        else None,
        steps=[decode_TimingStep(item0) for item0 in read_list(data["steps"])],
    )


def decode_TimingEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> TimingEvent:
    data = read_object(value)
    return TimingEvent(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        body=decode_TimingBody(data["body"]),
        closes_at=read_str(data["closes_at"])
        if data.get("closes_at") is not None
        else None,
        event_id=read_str(data["event_id"]),
        quality=decode_PredictionQuality(data["quality"]),
        question=read_str(data["question"]),
        release_id=read_str(data["release_id"])
        if data.get("release_id") is not None
        else None,
        resolution=decode_PredictionResolution(data["resolution"]),
        resolves_at=read_str(data["resolves_at"])
        if data.get("resolves_at") is not None
        else None,
        shape=read_str(data["shape"]),
        status=read_str(data["status"]),
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
        variant=read_str(data["variant"]) if data.get("variant") is not None else None,
    )


def decode_TradeExports(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> TradeExports:
    data = read_object(value)
    return TradeExports(
        country=read_str(data["country"]),
        coverage=read_str(data["coverage"]),
        currency=read_str(data["currency"]),
        flow=read_str(data["flow"]),
        partner=read_str(data["partner"]) if data.get("partner") is not None else None,
        period=read_str(data["period"]),
        product=decode_TradeProductFilter(data["product"])
        if data.get("product") is not None
        else None,
        released_on=read_str(data["released_on"]),
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        value=read_decimal(data["value"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_TradeImports(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> TradeImports:
    data = read_object(value)
    return TradeImports(
        country=read_str(data["country"]),
        coverage=read_str(data["coverage"]),
        currency=read_str(data["currency"]),
        flow=read_str(data["flow"]),
        partner=read_str(data["partner"]) if data.get("partner") is not None else None,
        period=read_str(data["period"]),
        product=decode_TradeProductFilter(data["product"])
        if data.get("product") is not None
        else None,
        released_on=read_str(data["released_on"]),
        source=decode_SeriesSource(data["source"])
        if data.get("source") is not None
        else None,
        value=read_decimal(data["value"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_TradeProductFilter(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> TradeProductFilter:
    data = read_object(value)
    return TradeProductFilter(
        classification=read_str(data["classification"]),
        code=read_str(data["code"]),
    )


def decode_TradeSummary(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> TradeSummary:
    data = read_object(value)
    return TradeSummary(
        balance=read_decimal(data["balance"]),
        country=read_str(data["country"]),
        coverage=read_str(data["coverage"]),
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
        unit=read_str(data["unit"]),
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


def decode_VenueSettlement(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> VenueSettlement:
    data = read_object(value)
    return VenueSettlement(
        status=read_str(data["status"]),
    )


def decode_WebhookConfigurationHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookConfigurationHistory:
    data = read_object(value)
    return WebhookConfigurationHistory(
        activation_snapshot=read_str(data["activation_snapshot"]),
        countries=[read_str(item0) for item0 in read_list(data["countries"])],
        destination_id=read_str(data["destination_id"]),
        enabled=read_bool(data["enabled"]),
        families=[read_str(item0) for item0 in read_list(data["families"])],
        recorded_at=read_str(data["recorded_at"]),
        url=read_str(data["url"]),
        version=read_int(data["version"]),
    )


def decode_WebhookDeleteResponse(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookDeleteResponse:
    data = read_object(value)
    return WebhookDeleteResponse(
        deleted=read_bool(data["deleted"]) if data.get("deleted") is not None else None,
        destination_id=read_str(data["destination_id"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_WebhookDeliveriesResponse(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookDeliveriesResponse:
    data = read_object(value)
    return WebhookDeliveriesResponse(
        deliveries=[
            decode_WebhookDelivery(item0) for item0 in read_list(data["deliveries"])
        ],
        limit=read_int(data["limit"]),
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
        next_attempt_at=read_str(data["next_attempt_at"]),
        replays=read_int(data["replays"]),
        retry_until=read_str(data["retry_until"]),
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
        destinations=[
            decode_WebhookDestinationResponse(item0)
            for item0 in read_list(data["destinations"])
        ],
        limit=read_int(data["limit"]),
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
        enabled=read_bool(data["enabled"]),
        families=[read_str(item0) for item0 in read_list(data["families"])],
        secret_version=read_int(data["secret_version"]),
        updated_at=read_str(data["updated_at"]),
        url=read_str(data["url"]),
        meta=meta if meta is not None else ResponseMeta(),
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


def decode_WebhookReplayResponse(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> WebhookReplayResponse:
    data = read_object(value)
    return WebhookReplayResponse(
        delivery_id=read_str(data["delivery_id"]),
        replayed=read_bool(data["replayed"]),
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
        destination_id=read_str(data["destination_id"]),
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

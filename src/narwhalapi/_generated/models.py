# Generated from spec/live/openapi.json sha256 5071bd97e9507eb56b344d00a24ba056ce1340fe1184faa4d755fe7e407e1cf6. Do not edit.
# Generated from spec/next/openapi.json sha256 5071bd97e9507eb56b344d00a24ba056ce1340fe1184faa4d755fe7e407e1cf6. Do not edit.
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
class _FundPrice:
    pass


@dataclass(frozen=True, slots=True)
class _FundPriceItem:
    pass


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


@dataclass(frozen=True, slots=True)
class _PolicyRate:
    pass


@dataclass(frozen=True, slots=True)
class _PolicyRateObservation:
    pass


class BarInterval:
    """Known values; response fields also accept future strings."""

    V15M: Literal["15m"] = "15m"
    V1D: Literal["1d"] = "1d"
    V1H: Literal["1h"] = "1h"
    V1M: Literal["1m"] = "1m"
    V4H: Literal["4h"] = "4h"
    V5M: Literal["5m"] = "5m"


class CatalogueLatestFrequency:
    """Known values; response fields also accept future strings."""

    ANNUAL: Literal["annual"] = "annual"
    DAILY: Literal["daily"] = "daily"
    MONTHLY: Literal["monthly"] = "monthly"
    QUARTERLY: Literal["quarterly"] = "quarterly"


class CatalogueLatestSeasonalAdjustment:
    """Known values; response fields also accept future strings."""

    NOT_APPLICABLE: Literal["not_applicable"] = "not_applicable"
    NOT_SEASONALLY_ADJUSTED: Literal["not_seasonally_adjusted"] = (
        "not_seasonally_adjusted"
    )
    NOT_STATED: Literal["not_stated"] = "not_stated"
    SEASONALLY_ADJUSTED: Literal["seasonally_adjusted"] = "seasonally_adjusted"


class CentralBankBalanceSheetScale:
    """Known values; response fields also accept future strings."""

    MILLIONS: Literal["millions"] = "millions"
    UNITS: Literal["units"] = "units"


class CommodityUnit:
    """Known values; response fields also accept future strings."""

    BARREL: Literal["barrel"] = "barrel"
    POUND: Literal["pound"] = "pound"
    TROY_OUNCE: Literal["troy_ounce"] = "troy_ounce"


class CompanyRelationKind:
    """Known values; response fields also accept future strings."""

    CROSS_LISTED: Literal["cross_listed"] = "cross_listed"
    PREDECESSOR: Literal["predecessor"] = "predecessor"
    SUCCESSOR: Literal["successor"] = "successor"


class CompanySearchMatch:
    """Known values; response fields also accept future strings."""

    CODE: Literal["code"] = "code"
    FORMER_CODE: Literal["former_code"] = "former_code"
    FORMER_NAME: Literal["former_name"] = "former_name"
    ID: Literal["id"] = "id"
    NAME: Literal["name"] = "name"


class CompanyStandard:
    """Known values; response fields also accept future strings."""

    IFRS: Literal["ifrs"] = "ifrs"
    J_GAAP: Literal["j_gaap"] = "j_gaap"
    JMIS: Literal["jmis"] = "jmis"
    K_GAAP: Literal["k_gaap"] = "k_gaap"
    US_GAAP: Literal["us_gaap"] = "us_gaap"


class CostEquityRiskPremiumBasis:
    """Known values; response fields also accept future strings."""

    MODELLED: Literal["modelled"] = "modelled"
    OBSERVED: Literal["observed"] = "observed"
    TABLE: Literal["table"] = "table"


class CostEquityRiskPremiumSource:
    """Known values; response fields also accept future strings."""

    CALLER: Literal["caller"] = "caller"
    NARWHAL: Literal["narwhal"] = "narwhal"


class CostOfCapitalBeta:
    """Known values; response fields also accept future strings."""

    ADJUSTED: Literal["adjusted"] = "adjusted"
    RAW: Literal["raw"] = "raw"


class CostOfCapitalFrequency:
    """Known values; response fields also accept future strings."""

    MONTHLY: Literal["monthly"] = "monthly"
    WEEKLY: Literal["weekly"] = "weekly"


class CostOfCapitalPeriod:
    """Known values; response fields also accept future strings."""

    ANNUAL: Literal["annual"] = "annual"
    TTM: Literal["ttm"] = "ttm"


class CostOfCapitalWindow:
    """Known values; response fields also accept future strings."""

    V2Y: Literal["2y"] = "2y"
    V5Y: Literal["5y"] = "5y"


class CostOfDebtBasis:
    """Known values; response fields also accept future strings."""

    OURS: Literal["ours"] = "ours"
    TABLE: Literal["table"] = "table"


class CostRiskFreeBasis:
    """Known values; response fields also accept future strings."""

    CALLER: Literal["caller"] = "caller"
    OURS: Literal["ours"] = "ours"


class CostRiskFreeSource:
    """Known values; response fields also accept future strings."""

    CALLER: Literal["caller"] = "caller"
    YIELD_CURVE: Literal["yield_curve"] = "yield_curve"


class CostTaxRateBasis:
    """Known values; response fields also accept future strings."""

    CALLER: Literal["caller"] = "caller"
    TABLE: Literal["table"] = "table"


class CostTaxRateSource:
    """Known values; response fields also accept future strings."""

    CALLER: Literal["caller"] = "caller"
    COUNTRY_TABLE: Literal["country_table"] = "country_table"


class CryptoBarInterval:
    """Known values; response fields also accept future strings."""

    V1D: Literal["1d"] = "1d"
    V1M: Literal["1m"] = "1m"


class CryptoPriceErrorCode:
    """Known values; response fields also accept future strings."""

    NOT_COVERED: Literal["not_covered"] = "not_covered"
    NOT_FOUND: Literal["not_found"] = "not_found"
    UPSTREAM_BUSY: Literal["upstream_busy"] = "upstream_busy"


class CryptoQuote:
    """Known values; response fields also accept future strings."""

    EUR: Literal["EUR"] = "EUR"
    GBP: Literal["GBP"] = "GBP"
    USD: Literal["USD"] = "USD"


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


class EquityEarningTime:
    """Known values; response fields also accept future strings."""

    AFTER_CLOSE: Literal["after_close"] = "after_close"
    BEFORE_OPEN: Literal["before_open"] = "before_open"
    DURING: Literal["during"] = "during"


class EquityMarketSession:
    """Known values; response fields also accept future strings."""

    CLOSED: Literal["closed"] = "closed"
    OPEN: Literal["open"] = "open"
    POST: Literal["post"] = "post"
    PRE: Literal["pre"] = "pre"


class EquityType:
    """Known values; response fields also accept future strings."""

    CLOSED_END_FUND: Literal["closed_end_fund"] = "closed_end_fund"
    COMMON_STOCK: Literal["common_stock"] = "common_stock"
    DEPOSITARY_RECEIPT: Literal["depositary_receipt"] = "depositary_receipt"
    OTHER: Literal["other"] = "other"
    PREFERRED_STOCK: Literal["preferred_stock"] = "preferred_stock"
    REIT: Literal["reit"] = "reit"
    RIGHT: Literal["right"] = "right"
    UNIT: Literal["unit"] = "unit"
    WARRANT: Literal["warrant"] = "warrant"


class ExtremeObservation:
    """Known values; response fields also accept future strings."""

    ANY_RELEASE: Literal["any_release"] = "any_release"
    ANY_TRADE: Literal["any_trade"] = "any_trade"
    CLOSE: Literal["close"] = "close"


class FilingEventType:
    """Known values; response fields also accept future strings."""

    ANNUAL: Literal["annual"] = "annual"
    EVENT: Literal["event"] = "event"
    OWNERSHIP: Literal["ownership"] = "ownership"
    QUARTERLY: Literal["quarterly"] = "quarterly"
    SEMIANNUAL: Literal["semiannual"] = "semiannual"


class FilingType:
    """Known values; response fields also accept future strings."""

    ANNUAL: Literal["annual"] = "annual"
    EVENT: Literal["event"] = "event"
    INSIDER: Literal["insider"] = "insider"
    OTHER: Literal["other"] = "other"
    OWNERSHIP: Literal["ownership"] = "ownership"
    QUARTERLY: Literal["quarterly"] = "quarterly"
    SEMIANNUAL: Literal["semiannual"] = "semiannual"


class FinancialStatement:
    """Known values; response fields also accept future strings."""

    BALANCE: Literal["balance"] = "balance"
    CASH_FLOW: Literal["cash_flow"] = "cash_flow"
    INCOME: Literal["income"] = "income"
    OTHER: Literal["other"] = "other"
    PER_SHARE: Literal["per_share"] = "per_share"
    SHARES: Literal["shares"] = "shares"


class FinancialsBasis:
    """Known values; response fields also accept future strings."""

    CONSOLIDATED: Literal["consolidated"] = "consolidated"
    STANDALONE: Literal["standalone"] = "standalone"


class FinancialsPeriod:
    """Known values; response fields also accept future strings."""

    ANNUAL: Literal["annual"] = "annual"
    QUARTERLY: Literal["quarterly"] = "quarterly"
    SEMIANNUAL: Literal["semiannual"] = "semiannual"


class FinancialsVersion:
    """Known values; response fields also accept future strings."""

    FIRST_REPORTED: Literal["first_reported"] = "first_reported"
    LATEST: Literal["latest"] = "latest"


class FiscalPeriod:
    """Known values; response fields also accept future strings."""

    FY: Literal["FY"] = "FY"
    H1: Literal["H1"] = "H1"
    H2: Literal["H2"] = "H2"
    Q1: Literal["Q1"] = "Q1"
    Q2: Literal["Q2"] = "Q2"
    Q3: Literal["Q3"] = "Q3"
    Q4: Literal["Q4"] = "Q4"


class FundDistributionKind:
    """Known values; response fields also accept future strings."""

    CAPITAL_GAIN: Literal["capital_gain"] = "capital_gain"
    INCOME: Literal["income"] = "income"


class FundType:
    """Known values; response fields also accept future strings."""

    ETF: Literal["etf"] = "etf"
    MUTUAL_FUND: Literal["mutual_fund"] = "mutual_fund"


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


class Language:
    """Known values; response fields also accept future strings."""

    EN: Literal["en"] = "en"
    ORIGINAL: Literal["original"] = "original"


class MarketSession:
    """Known values; response fields also accept future strings."""

    INTERBANK_CLOSED: Literal["interbank_closed"] = "interbank_closed"
    OPEN: Literal["open"] = "open"
    WEEKEND: Literal["weekend"] = "weekend"


class MoversDirection:
    """Known values; response fields also accept future strings."""

    ACTIVE: Literal["active"] = "active"
    GAINERS: Literal["gainers"] = "gainers"
    LOSERS: Literal["losers"] = "losers"


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


class PointPolicyRateQualifier:
    """Known values; response fields also accept future strings."""

    AROUND: Literal["around"] = "around"
    EXACT: Literal["exact"] = "exact"


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


class Registry:
    """Known values; response fields also accept future strings."""

    AUT: Literal["aut"] = "aut"
    BEL: Literal["bel"] = "bel"
    CYP: Literal["cyp"] = "cyp"
    CZE: Literal["cze"] = "cze"
    DNK: Literal["dnk"] = "dnk"
    ESP: Literal["esp"] = "esp"
    EST: Literal["est"] = "est"
    FIN: Literal["fin"] = "fin"
    FRA: Literal["fra"] = "fra"
    GBR: Literal["gbr"] = "gbr"
    GRC: Literal["grc"] = "grc"
    HRV: Literal["hrv"] = "hrv"
    HUN: Literal["hun"] = "hun"
    ISL: Literal["isl"] = "isl"
    ITA: Literal["ita"] = "ita"
    JPN: Literal["jpn"] = "jpn"
    KOR: Literal["kor"] = "kor"
    LTU: Literal["ltu"] = "ltu"
    LUX: Literal["lux"] = "lux"
    LVA: Literal["lva"] = "lva"
    MLT: Literal["mlt"] = "mlt"
    NLD: Literal["nld"] = "nld"
    NOR: Literal["nor"] = "nor"
    POL: Literal["pol"] = "pol"
    PRT: Literal["prt"] = "prt"
    ROU: Literal["rou"] = "rou"
    SVK: Literal["svk"] = "svk"
    SVN: Literal["svn"] = "svn"
    SWE: Literal["swe"] = "swe"
    TWN: Literal["twn"] = "twn"
    USA: Literal["usa"] = "usa"


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


class SecurityType:
    """Known values; response fields also accept future strings."""

    ADR: Literal["adr"] = "adr"
    COMMON: Literal["common"] = "common"
    OTHER: Literal["other"] = "other"
    PREFERRED: Literal["preferred"] = "preferred"


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
    FILING_PUBLISHED: Literal["filing.published"] = "filing.published"
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
    FILINGS: Literal["filings"] = "filings"
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
class AsReportedConcept:
    concept: str
    label: str | None = None
    taxonomy: str
    unit: str
    values: list[AsReportedValue]


@dataclass(frozen=True, slots=True, kw_only=True)
class AsReportedPage:
    concepts: list[AsReportedConcept]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class AsReportedValue:
    end: str
    start: str | None = None
    value: Decimal


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
class CatalogueBulkLatest:
    missing: list[str]
    observations: list[CatalogueLatest]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CatalogueEntry:
    country: str | None = None
    first_period: str | None = None
    frequency: str | None = None
    id: str | None = None
    id_template: str | None = None
    last_period: str | None = None
    source: str
    title: str
    unit_label: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class CatalogueHistory:
    attribution: str
    base_period: str | None = None
    country: str | None = None
    currency: str | None = None
    fetched_at: str
    frequency: str
    id: str
    licence_url: str
    next_cursor: str | None = None
    observations: list[ResourceObservation]
    scale: str | None = None
    seasonal_adjustment: str
    stale: bool | None = None
    title: str
    unit: str
    unit_label: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CatalogueLatest:
    attribution: str
    base_period: str | None = None
    country: str | None = None
    currency: str | None = None
    fetched_at: str
    first_reported_at: str | None = None
    frequency: str
    id: str
    licence_url: str
    period: str
    released_on: str | None = None
    scale: str | None = None
    seasonal_adjustment: str
    stale: bool | None = None
    status: str | None = None
    title: str
    unit: str
    unit_label: str
    value: Decimal


@dataclass(frozen=True, slots=True, kw_only=True)
class CatalogueSearchPage:
    next_cursor: str | None = None
    results: list[CatalogueEntry]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CatalogueSeries:
    attribution: str
    base_period: str | None = None
    country: str | None = None
    currency: str | None = None
    fetched_at: str
    first_period: str
    frequency: str
    id: str
    last_period: str
    licence_url: str
    scale: str | None = None
    seasonal_adjustment: str
    stale: bool | None = None
    title: str
    unit: str
    unit_label: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CentralBankBalanceSheet:
    country: str
    currency: str
    period: str
    released_on: str
    scale: str
    value: Decimal
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CentralBankReserves:
    country: str
    currency: str
    period: str
    released_on: str
    scale: str
    value: Decimal
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
class CompanyFilingsPage:
    filed_from: str | None = None
    filings: list[ListedFiling]
    id: str
    next_cursor: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CompanyIndustry:
    industry: str | None = None
    isic: str | None = None
    sector: str | None = None
    source_code: str | None = None
    source_scheme: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class CompanyNameSpan:
    from_: str | None = None
    name: str
    to: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class CompanyRelation:
    id: str
    kind: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CompanySearchHit:
    code: str | None = None
    country: str | None = None
    delisted: bool | None = None
    former_code: bool | None = None
    former_name: str | None = None
    id: str
    matched: str | None = None
    mic: str | None = None
    name: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CompanySearchPage:
    companies: list[CompanySearchHit]
    coverage: list[RegistryCoverage] | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CompanySecurity:
    adr_ratio: Decimal | None = None
    class_: str
    figi: str | None = None
    isin: str | None = None
    listings: list[SecurityListing]
    primary: bool | None = None
    title: str | None = None
    type: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CompanyWithListings:
    country: str | None = None
    delisted: bool | None = None
    fiscal_year_end: str | None = None
    id: str
    industry: CompanyIndustry | None = None
    jp_corporate_number: str | None = None
    lei: str | None = None
    listings: list[str] | None = None
    name: str
    names: list[CompanyNameSpan]
    related: list[CompanyRelation]
    securities: list[CompanySecurity]
    standard: str | None = None
    standard_variant: str | None = None
    status_date: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CostBenchmark:
    default: bool | None = None
    id: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CostBeta:
    adjusted: Decimal
    benchmark: CostBenchmark
    end: str
    frequency: str
    observations: int
    r_squared: Decimal
    raw: Decimal
    start: str
    std_error: Decimal
    used: str
    window: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CostEquityRiskPremium:
    as_of: str | None = None
    basis: str | None = None
    country: str | None = None
    rate: Decimal
    source: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CostOfDebt:
    after_tax: Decimal | None = None
    average_debt: Decimal
    basis: str
    closing_debt: Decimal
    default_spread: Decimal | None = None
    interest_coverage: Decimal | None = None
    interest_expense: Decimal
    opening_debt: Decimal | None = None
    period: str
    period_end: str
    pre_tax: Decimal
    table: str | None = None
    table_update: str | None = None
    table_url: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class CostRiskFree:
    as_of: str | None = None
    basis: str
    country: str | None = None
    curve_type: str | None = None
    maturity: str | None = None
    rate: Decimal
    source: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CostTaxRate:
    basis: str
    country: str | None = None
    rate: Decimal
    source: str
    table: str | None = None
    table_update: str | None = None
    table_url: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class CostWarning:
    code: str
    message: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CostWeights:
    debt: Decimal
    equity: Decimal
    market_cap: Decimal
    market_cap_as_of: str
    total_debt: Decimal
    total_debt_as_of: str


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
    first_reported_at: str | None = None
    period: str
    value: Decimal


@dataclass(frozen=True, slots=True, kw_only=True)
class CryptoBar:
    close: Decimal
    high: Decimal
    low: Decimal
    open: Decimal
    timestamp: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CryptoBars:
    bars: list[CryptoBar]
    end: str | None = None
    next_cursor: str | None = None
    pair: str
    start: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CryptoPair:
    base: str
    name: str
    pair: str
    quote: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CryptoPairs:
    pairs: list[CryptoPair]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CryptoPrice:
    base: str
    change_24h: Decimal | None = None
    change_24h_percent: Decimal | None = None
    delayed: bool | None = None
    pair: str
    price: Decimal
    quote: str
    stale: bool
    timestamp: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class CryptoPriceError:
    code: str
    id: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CryptoPrices:
    errors: list[CryptoPriceError]
    prices: list[CryptoPrice]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


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
class DividendsCalendar:
    entries: list[DividendsCalendarEntry]
    next_cursor: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class DividendsCalendarEntry:
    amount: Decimal
    currency: str
    ex_date: str
    id: str
    name: str
    symbol: str


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
class EquityBar:
    close: Decimal
    date: str | None = None
    high: Decimal
    low: Decimal
    open: Decimal
    timestamp: str
    volume: Decimal | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityBars:
    adjusted: bool
    bars: list[EquityBar]
    currency: str
    end: str | None = None
    id: str
    next_cursor: str | None = None
    start: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityCostOfCapital:
    beta: CostBeta
    company_id: str
    cost_of_debt: CostOfDebt | None = None
    cost_of_equity: Decimal
    currency: str
    equity_risk_premium: CostEquityRiskPremium
    id: str
    methodology_url: str
    risk_free: CostRiskFree
    tax_rate: CostTaxRate | None = None
    wacc: Decimal | None = None
    warnings: list[CostWarning]
    weights: CostWeights
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityDividend:
    amount: Decimal
    currency: str
    ex_date: str
    pay_date: str | None = None
    record_date: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityDividends:
    dividends: list[EquityDividend]
    id: str
    next_cursor: str | None = None
    start: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityEarning:
    date: str
    eps_actual: Decimal | None = None
    eps_estimate: Decimal | None = None
    filing_id: str | None = None
    surprise: Decimal | None = None
    surprise_percent: Decimal | None = None
    time: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityEarnings:
    earnings: list[EquityEarning]
    id: str
    next_cursor: str | None = None
    start: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityMover:
    change_percent: Decimal
    id: str
    name: str
    price: Decimal
    symbol: str
    volume: Decimal


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityMovers:
    direction: str
    market: str
    movers: list[EquityMover]
    timestamp: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityPrice:
    change: Decimal | None = None
    change_percent: Decimal | None = None
    currency: str
    delayed: bool | None = None
    id: str
    market_session: str
    previous_close: Decimal | None = None
    price: Decimal
    stale: bool
    symbol: str
    timestamp: str
    volume: Decimal | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityPriceError:
    code: str
    id: str


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityPrices:
    errors: list[EquityPriceError]
    prices: list[EquityPrice]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityProfile:
    company_id: str | None = None
    country: str | None = None
    currency: str
    id: str
    industry: str | None = None
    logo_url: str | None = None
    mic: str
    name: str
    sector: str | None = None
    symbol: str
    type: str
    website: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityRiskPremium:
    as_of: str
    basis: EquityRiskPremiumBasis
    country: str
    country_default_spread: Decimal
    country_risk_premium: Decimal
    mature_erp: Decimal
    methodology_url: str | None = None
    total_erp: Decimal
    unit: str
    volatility_ratio: Decimal | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityRiskPremiumBasis:
    country_default_spread: str
    country_risk_premium: str
    mature_erp: str
    total_erp: str
    volatility_ratio: str


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityRiskPremiumHistoryResponse:
    country: str
    next_cursor: str | None = None
    observations: list[EquityRiskPremium]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityRiskPremiumList:
    countries: list[EquityRiskPremium]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquitySearchResult:
    company_id: str | None = None
    country: str | None = None
    currency: str
    id: str
    mic: str
    name: str
    symbol: str
    type: str


@dataclass(frozen=True, slots=True, kw_only=True)
class EquitySearchResults:
    next_cursor: str | None = None
    results: list[EquitySearchResult]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquitySplit:
    date: str
    ratio: str


@dataclass(frozen=True, slots=True, kw_only=True)
class EquitySplits:
    id: str
    splits: list[EquitySplit]
    start: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityValuation:
    company_id: str
    currency: str
    dividend_per_share_ttm: Decimal | None = None
    dividend_yield: Decimal | None = None
    dividends_period_end: str | None = None
    eps_period_end: str | None = None
    eps_ttm: Decimal | None = None
    equity_as_of: str | None = None
    id: str
    market_cap: Decimal | None = None
    pb_ratio: Decimal | None = None
    pe_ratio: Decimal | None = None
    ps_ratio: Decimal | None = None
    revenue_period_end: str | None = None
    revenue_ttm: Decimal | None = None
    shares_as_of: str | None = None
    shares_outstanding: Decimal | None = None
    timestamp: str
    total_equity: Decimal | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityValuationHistory:
    company_id: str
    currency: str
    id: str
    points: list[EquityValuationPoint]
    start: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class EquityValuationPoint:
    date: str
    dividend_yield: Decimal | None = None
    market_cap: Decimal | None = None
    pb_ratio: Decimal | None = None
    pe_ratio: Decimal | None = None
    price: Decimal | None = None
    price_date: str | None = None
    ps_ratio: Decimal | None = None


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
class Filing:
    amends: str | None = None
    company_id: str
    filed_at: str
    filer_id: str | None = None
    form: str
    fp: str | None = None
    fy: int | None = None
    id: str
    period_end: str | None = None
    title: str | None = None
    type: str
    url: str | None = None
    withdrawn: bool | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class FilingWebhookEvent:
    company_id: str
    filed_at: str
    filing_id: str
    form: str
    fp: str | None = None
    fy: int | None = None
    period_end: str | None = None
    subject_id: str | None = None
    type: str


@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialRow:
    currency: str | None = None
    derived: list[str] | None = None
    end: str
    fh: int | None = None
    fq: int | None = None
    fy: int
    items: dict[str, Decimal] = field(default_factory=dict)


@dataclass(frozen=True, slots=True, kw_only=True)
class Financials:
    annual: list[FinancialRow] | None = None
    as_of: str | None = None
    basis: str | None = None
    currency: str | None = None
    from_fy: int | None = None
    id: str
    quarterly: list[FinancialRow] | None = None
    semiannual: list[FinancialRow] | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class FundDistribution:
    amount: Decimal
    currency: str
    ex_date: str
    kind: str | None = None
    pay_date: str | None = None
    record_date: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class FundDistributions:
    distributions: list[FundDistribution]
    id: str
    next_cursor: str | None = None
    start: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class FundEtfPrice(_FundPriceItem):
    kind: ClassVar[Literal["FundEtfPrice"]] = "FundEtfPrice"
    change: Decimal | None = None
    change_percent: Decimal | None = None
    currency: str
    delayed: bool | None = None
    id: str
    market_session: str
    previous_close: Decimal | None = None
    price: Decimal
    stale: bool
    symbol: str
    timestamp: str
    type: str
    volume: Decimal | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class FundNavPrice(_FundPriceItem):
    kind: ClassVar[Literal["FundNavPrice"]] = "FundNavPrice"
    change: Decimal | None = None
    change_percent: Decimal | None = None
    currency: str
    date: str
    id: str
    nav: Decimal
    previous_nav: Decimal | None = None
    stale: bool
    symbol: str
    type: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class FundPriceError:
    code: str
    id: str


@dataclass(frozen=True, slots=True, kw_only=True)
class FundPrices:
    errors: list[FundPriceError]
    prices: list[FundPriceItem]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class FundProfile:
    country: str | None = None
    currency: str
    id: str
    mic: str | None = None
    name: str
    symbol: str
    type: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class FundSearchResult:
    country: str | None = None
    currency: str
    id: str
    mic: str | None = None
    name: str
    symbol: str
    type: str


@dataclass(frozen=True, slots=True, kw_only=True)
class FundSearchResults:
    next_cursor: str | None = None
    results: list[FundSearchResult]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class FxBar:
    close: Decimal
    high: Decimal
    low: Decimal
    open: Decimal
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
    first_reported_at: str | None = None
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
    first_reported_at: str | None = None
    period: str
    value: Decimal


@dataclass(frozen=True, slots=True, kw_only=True)
class Holder:
    event_date: str | None = None
    filed: str
    filing_id: str
    holder: str
    percent: Decimal | None = None
    security: HolderSecurity | None = None
    shares: Decimal | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class HolderSecurity:
    class_: str | None = None
    isin: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class HoldersPage:
    filed_from: str | None = None
    holders: list[Holder]
    id: str
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


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
    first_reported_at: str | None = None
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
class LatestFiling:
    company_id: str
    filed: str
    form: str
    id: str
    title: str | None = None
    type: str


@dataclass(frozen=True, slots=True, kw_only=True)
class LatestFilingsPage:
    filings: list[LatestFiling]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class ListedFiling:
    filed: str
    form: str
    id: str
    period_end: str | None = None
    title: str | None = None
    type: str


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
class PointPolicyRate(_PolicyRateObservation):
    kind: ClassVar[Literal["PointPolicyRate"]] = "PointPolicyRate"
    announced_on: str | None = None
    authority: str
    country: str
    currency: str
    effective_on: str | None = None
    instrument: str
    observed_on: str | None = None
    qualifier: str
    rate: Decimal
    rate_type: str
    unit: str
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
class PolicyRateHistoryResponse:
    country: str
    next_cursor: str | None = None
    observations: list[PolicyRateObservation]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


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
class RangePolicyRate(_PolicyRateObservation):
    kind: ClassVar[Literal["RangePolicyRate"]] = "RangePolicyRate"
    announced_on: str | None = None
    authority: str
    country: str
    currency: str
    effective_on: str | None = None
    instrument: str
    lower_bound: Decimal
    observed_on: str | None = None
    rate_type: str
    unit: str
    upper_bound: Decimal
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


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
    first_reported_at: str | None = None
    period: str
    rate: Decimal


@dataclass(frozen=True, slots=True, kw_only=True)
class RegistryCoverage:
    companies: int
    registry: str


@dataclass(frozen=True, slots=True, kw_only=True)
class ResourceHistory:
    as_of: str | None = None
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
    first_reported_at: str | None = None
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
class SecurityListing:
    code: str
    from_: str | None = None
    mic: str
    to: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class SeriesSource:
    distributor: str
    publisher: str


@dataclass(frozen=True, slots=True, kw_only=True)
class SplitsCalendar:
    entries: list[SplitsCalendarEntry]
    next_cursor: str | None = None
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)


@dataclass(frozen=True, slots=True, kw_only=True)
class SplitsCalendarEntry:
    date: str
    id: str
    name: str
    ratio: str
    symbol: str


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
    first_reported_at: str | None = None
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
    companies: list[str] | None = None
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
    companies: list[str] | None = None
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
    companies: list[str] | None = None
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
    filing: FilingWebhookEvent | None = None
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
class FundPriceUnknown(_FundPrice):
    kind: ClassVar[Literal["unknown"]] = "unknown"
    raw: dict[str, object]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)
    _raw_body: bytes = field(default=b"", repr=False, compare=False)


FundPrice: TypeAlias = FundEtfPrice | FundNavPrice | FundPriceUnknown


@dataclass(frozen=True, slots=True)
class FundPriceItemUnknown(_FundPriceItem):
    kind: ClassVar[Literal["unknown"]] = "unknown"
    raw: dict[str, object]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)
    _raw_body: bytes = field(default=b"", repr=False, compare=False)


FundPriceItem: TypeAlias = FundEtfPrice | FundNavPrice | FundPriceItemUnknown


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


@dataclass(frozen=True, slots=True)
class PolicyRateUnknown(_PolicyRate):
    kind: ClassVar[Literal["unknown"]] = "unknown"
    raw: dict[str, object]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)
    _raw_body: bytes = field(default=b"", repr=False, compare=False)


PolicyRate: TypeAlias = PointPolicyRate | RangePolicyRate | PolicyRateUnknown


@dataclass(frozen=True, slots=True)
class PolicyRateObservationUnknown(_PolicyRateObservation):
    kind: ClassVar[Literal["unknown"]] = "unknown"
    raw: dict[str, object]
    meta: ResponseMeta = field(default_factory=ResponseMeta, compare=False)
    _raw_body: bytes = field(default=b"", repr=False, compare=False)


PolicyRateObservation: TypeAlias = (
    PointPolicyRate | RangePolicyRate | PolicyRateObservationUnknown
)


def decode_AsReportedConcept(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> AsReportedConcept:
    data = read_object(value)
    return AsReportedConcept(
        concept=read_str(data["concept"]),
        label=read_str(data["label"]) if data.get("label") is not None else None,
        taxonomy=read_str(data["taxonomy"]),
        unit=read_str(data["unit"]),
        values=[decode_AsReportedValue(item0) for item0 in read_list(data["values"])],
    )


def decode_AsReportedPage(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> AsReportedPage:
    data = read_object(value)
    return AsReportedPage(
        concepts=[
            decode_AsReportedConcept(item0) for item0 in read_list(data["concepts"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_AsReportedValue(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> AsReportedValue:
    data = read_object(value)
    return AsReportedValue(
        end=read_str(data["end"]),
        start=read_str(data["start"]) if data.get("start") is not None else None,
        value=read_decimal(data["value"]),
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


def decode_CatalogueBulkLatest(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CatalogueBulkLatest:
    data = read_object(value)
    return CatalogueBulkLatest(
        missing=[read_str(item0) for item0 in read_list(data["missing"])],
        observations=[
            decode_CatalogueLatest(item0) for item0 in read_list(data["observations"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CatalogueEntry(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CatalogueEntry:
    data = read_object(value)
    return CatalogueEntry(
        country=read_str(data["country"]) if data.get("country") is not None else None,
        first_period=read_str(data["first_period"])
        if data.get("first_period") is not None
        else None,
        frequency=read_str(data["frequency"])
        if data.get("frequency") is not None
        else None,
        id=read_str(data["id"]) if data.get("id") is not None else None,
        id_template=read_str(data["id_template"])
        if data.get("id_template") is not None
        else None,
        last_period=read_str(data["last_period"])
        if data.get("last_period") is not None
        else None,
        source=read_str(data["source"]),
        title=read_str(data["title"]),
        unit_label=read_str(data["unit_label"])
        if data.get("unit_label") is not None
        else None,
    )


def decode_CatalogueHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CatalogueHistory:
    data = read_object(value)
    return CatalogueHistory(
        attribution=read_str(data["attribution"]),
        base_period=read_str(data["base_period"])
        if data.get("base_period") is not None
        else None,
        country=read_str(data["country"]) if data.get("country") is not None else None,
        currency=read_str(data["currency"])
        if data.get("currency") is not None
        else None,
        fetched_at=read_str(data["fetched_at"]),
        frequency=read_str(data["frequency"]),
        id=read_str(data["id"]),
        licence_url=read_str(data["licence_url"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_ResourceObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        scale=read_str(data["scale"]) if data.get("scale") is not None else None,
        seasonal_adjustment=read_str(data["seasonal_adjustment"]),
        stale=read_bool(data["stale"]) if data.get("stale") is not None else None,
        title=read_str(data["title"]),
        unit=read_str(data["unit"]),
        unit_label=read_str(data["unit_label"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CatalogueLatest(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CatalogueLatest:
    data = read_object(value)
    return CatalogueLatest(
        attribution=read_str(data["attribution"]),
        base_period=read_str(data["base_period"])
        if data.get("base_period") is not None
        else None,
        country=read_str(data["country"]) if data.get("country") is not None else None,
        currency=read_str(data["currency"])
        if data.get("currency") is not None
        else None,
        fetched_at=read_str(data["fetched_at"]),
        first_reported_at=read_str(data["first_reported_at"])
        if data.get("first_reported_at") is not None
        else None,
        frequency=read_str(data["frequency"]),
        id=read_str(data["id"]),
        licence_url=read_str(data["licence_url"]),
        period=read_str(data["period"]),
        released_on=read_str(data["released_on"])
        if data.get("released_on") is not None
        else None,
        scale=read_str(data["scale"]) if data.get("scale") is not None else None,
        seasonal_adjustment=read_str(data["seasonal_adjustment"]),
        stale=read_bool(data["stale"]) if data.get("stale") is not None else None,
        status=read_str(data["status"]) if data.get("status") is not None else None,
        title=read_str(data["title"]),
        unit=read_str(data["unit"]),
        unit_label=read_str(data["unit_label"]),
        value=read_decimal(data["value"]),
    )


def decode_CatalogueSearchPage(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CatalogueSearchPage:
    data = read_object(value)
    return CatalogueSearchPage(
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        results=[decode_CatalogueEntry(item0) for item0 in read_list(data["results"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CatalogueSeries(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CatalogueSeries:
    data = read_object(value)
    return CatalogueSeries(
        attribution=read_str(data["attribution"]),
        base_period=read_str(data["base_period"])
        if data.get("base_period") is not None
        else None,
        country=read_str(data["country"]) if data.get("country") is not None else None,
        currency=read_str(data["currency"])
        if data.get("currency") is not None
        else None,
        fetched_at=read_str(data["fetched_at"]),
        first_period=read_str(data["first_period"]),
        frequency=read_str(data["frequency"]),
        id=read_str(data["id"]),
        last_period=read_str(data["last_period"]),
        licence_url=read_str(data["licence_url"]),
        scale=read_str(data["scale"]) if data.get("scale") is not None else None,
        seasonal_adjustment=read_str(data["seasonal_adjustment"]),
        stale=read_bool(data["stale"]) if data.get("stale") is not None else None,
        title=read_str(data["title"]),
        unit=read_str(data["unit"]),
        unit_label=read_str(data["unit_label"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CentralBankBalanceSheet(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CentralBankBalanceSheet:
    data = read_object(value)
    return CentralBankBalanceSheet(
        country=read_str(data["country"]),
        currency=read_str(data["currency"]),
        period=read_str(data["period"]),
        released_on=read_str(data["released_on"]),
        scale=read_str(data["scale"]),
        value=read_decimal(data["value"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CentralBankReserves(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CentralBankReserves:
    data = read_object(value)
    return CentralBankReserves(
        country=read_str(data["country"]),
        currency=read_str(data["currency"]),
        period=read_str(data["period"]),
        released_on=read_str(data["released_on"]),
        scale=read_str(data["scale"]),
        value=read_decimal(data["value"]),
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


def decode_CompanyFilingsPage(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CompanyFilingsPage:
    data = read_object(value)
    return CompanyFilingsPage(
        filed_from=read_str(data["filed_from"])
        if data.get("filed_from") is not None
        else None,
        filings=[decode_ListedFiling(item0) for item0 in read_list(data["filings"])],
        id=read_str(data["id"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CompanyIndustry(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CompanyIndustry:
    data = read_object(value)
    return CompanyIndustry(
        industry=read_str(data["industry"])
        if data.get("industry") is not None
        else None,
        isic=read_str(data["isic"]) if data.get("isic") is not None else None,
        sector=read_str(data["sector"]) if data.get("sector") is not None else None,
        source_code=read_str(data["source_code"])
        if data.get("source_code") is not None
        else None,
        source_scheme=read_str(data["source_scheme"])
        if data.get("source_scheme") is not None
        else None,
    )


def decode_CompanyNameSpan(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CompanyNameSpan:
    data = read_object(value)
    return CompanyNameSpan(
        from_=read_str(data["from"]) if data.get("from") is not None else None,
        name=read_str(data["name"]),
        to=read_str(data["to"]) if data.get("to") is not None else None,
    )


def decode_CompanyRelation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CompanyRelation:
    data = read_object(value)
    return CompanyRelation(
        id=read_str(data["id"]),
        kind=read_str(data["kind"]),
    )


def decode_CompanySearchHit(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CompanySearchHit:
    data = read_object(value)
    return CompanySearchHit(
        code=read_str(data["code"]) if data.get("code") is not None else None,
        country=read_str(data["country"]) if data.get("country") is not None else None,
        delisted=read_bool(data["delisted"])
        if data.get("delisted") is not None
        else None,
        former_code=read_bool(data["former_code"])
        if data.get("former_code") is not None
        else None,
        former_name=read_str(data["former_name"])
        if data.get("former_name") is not None
        else None,
        id=read_str(data["id"]),
        matched=read_str(data["matched"]) if data.get("matched") is not None else None,
        mic=read_str(data["mic"]) if data.get("mic") is not None else None,
        name=read_str(data["name"]),
    )


def decode_CompanySearchPage(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CompanySearchPage:
    data = read_object(value)
    return CompanySearchPage(
        companies=[
            decode_CompanySearchHit(item0) for item0 in read_list(data["companies"])
        ],
        coverage=[
            decode_RegistryCoverage(item0) for item0 in read_list(data["coverage"])
        ]
        if data.get("coverage") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CompanySecurity(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CompanySecurity:
    data = read_object(value)
    return CompanySecurity(
        adr_ratio=read_decimal(data["adr_ratio"])
        if data.get("adr_ratio") is not None
        else None,
        class_=read_str(data["class"]),
        figi=read_str(data["figi"]) if data.get("figi") is not None else None,
        isin=read_str(data["isin"]) if data.get("isin") is not None else None,
        listings=[
            decode_SecurityListing(item0) for item0 in read_list(data["listings"])
        ],
        primary=read_bool(data["primary"]) if data.get("primary") is not None else None,
        title=read_str(data["title"]) if data.get("title") is not None else None,
        type=read_str(data["type"]),
    )


def decode_CompanyWithListings(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CompanyWithListings:
    data = read_object(value)
    return CompanyWithListings(
        country=read_str(data["country"]) if data.get("country") is not None else None,
        delisted=read_bool(data["delisted"])
        if data.get("delisted") is not None
        else None,
        fiscal_year_end=read_str(data["fiscal_year_end"])
        if data.get("fiscal_year_end") is not None
        else None,
        id=read_str(data["id"]),
        industry=decode_CompanyIndustry(data["industry"])
        if data.get("industry") is not None
        else None,
        jp_corporate_number=read_str(data["jp_corporate_number"])
        if data.get("jp_corporate_number") is not None
        else None,
        lei=read_str(data["lei"]) if data.get("lei") is not None else None,
        listings=[read_str(item0) for item0 in read_list(data["listings"])]
        if data.get("listings") is not None
        else None,
        name=read_str(data["name"]),
        names=[decode_CompanyNameSpan(item0) for item0 in read_list(data["names"])],
        related=[decode_CompanyRelation(item0) for item0 in read_list(data["related"])],
        securities=[
            decode_CompanySecurity(item0) for item0 in read_list(data["securities"])
        ],
        standard=read_str(data["standard"])
        if data.get("standard") is not None
        else None,
        standard_variant=read_str(data["standard_variant"])
        if data.get("standard_variant") is not None
        else None,
        status_date=read_str(data["status_date"])
        if data.get("status_date") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CostBenchmark(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CostBenchmark:
    data = read_object(value)
    return CostBenchmark(
        default=read_bool(data["default"]) if data.get("default") is not None else None,
        id=read_str(data["id"]),
    )


def decode_CostBeta(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CostBeta:
    data = read_object(value)
    return CostBeta(
        adjusted=read_decimal(data["adjusted"]),
        benchmark=decode_CostBenchmark(data["benchmark"]),
        end=read_str(data["end"]),
        frequency=read_str(data["frequency"]),
        observations=read_int(data["observations"]),
        r_squared=read_decimal(data["r_squared"]),
        raw=read_decimal(data["raw"]),
        start=read_str(data["start"]),
        std_error=read_decimal(data["std_error"]),
        used=read_str(data["used"]),
        window=read_str(data["window"]),
    )


def decode_CostEquityRiskPremium(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CostEquityRiskPremium:
    data = read_object(value)
    return CostEquityRiskPremium(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        basis=read_str(data["basis"]) if data.get("basis") is not None else None,
        country=read_str(data["country"]) if data.get("country") is not None else None,
        rate=read_decimal(data["rate"]),
        source=read_str(data["source"]),
    )


def decode_CostOfDebt(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CostOfDebt:
    data = read_object(value)
    return CostOfDebt(
        after_tax=read_decimal(data["after_tax"])
        if data.get("after_tax") is not None
        else None,
        average_debt=read_decimal(data["average_debt"]),
        basis=read_str(data["basis"]),
        closing_debt=read_decimal(data["closing_debt"]),
        default_spread=read_decimal(data["default_spread"])
        if data.get("default_spread") is not None
        else None,
        interest_coverage=read_decimal(data["interest_coverage"])
        if data.get("interest_coverage") is not None
        else None,
        interest_expense=read_decimal(data["interest_expense"]),
        opening_debt=read_decimal(data["opening_debt"])
        if data.get("opening_debt") is not None
        else None,
        period=read_str(data["period"]),
        period_end=read_str(data["period_end"]),
        pre_tax=read_decimal(data["pre_tax"]),
        table=read_str(data["table"]) if data.get("table") is not None else None,
        table_update=read_str(data["table_update"])
        if data.get("table_update") is not None
        else None,
        table_url=read_str(data["table_url"])
        if data.get("table_url") is not None
        else None,
    )


def decode_CostRiskFree(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CostRiskFree:
    data = read_object(value)
    return CostRiskFree(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        basis=read_str(data["basis"]),
        country=read_str(data["country"]) if data.get("country") is not None else None,
        curve_type=read_str(data["curve_type"])
        if data.get("curve_type") is not None
        else None,
        maturity=read_str(data["maturity"])
        if data.get("maturity") is not None
        else None,
        rate=read_decimal(data["rate"]),
        source=read_str(data["source"]),
    )


def decode_CostTaxRate(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CostTaxRate:
    data = read_object(value)
    return CostTaxRate(
        basis=read_str(data["basis"]),
        country=read_str(data["country"]) if data.get("country") is not None else None,
        rate=read_decimal(data["rate"]),
        source=read_str(data["source"]),
        table=read_str(data["table"]) if data.get("table") is not None else None,
        table_update=read_str(data["table_update"])
        if data.get("table_update") is not None
        else None,
        table_url=read_str(data["table_url"])
        if data.get("table_url") is not None
        else None,
    )


def decode_CostWarning(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CostWarning:
    data = read_object(value)
    return CostWarning(
        code=read_str(data["code"]),
        message=read_str(data["message"]),
    )


def decode_CostWeights(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CostWeights:
    data = read_object(value)
    return CostWeights(
        debt=read_decimal(data["debt"]),
        equity=read_decimal(data["equity"]),
        market_cap=read_decimal(data["market_cap"]),
        market_cap_as_of=read_str(data["market_cap_as_of"]),
        total_debt=read_decimal(data["total_debt"]),
        total_debt_as_of=read_str(data["total_debt_as_of"]),
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
        first_reported_at=read_str(data["first_reported_at"])
        if data.get("first_reported_at") is not None
        else None,
        period=read_str(data["period"]),
        value=read_decimal(data["value"]),
    )


def decode_CryptoBar(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CryptoBar:
    data = read_object(value)
    return CryptoBar(
        close=read_decimal(data["close"]),
        high=read_decimal(data["high"]),
        low=read_decimal(data["low"]),
        open=read_decimal(data["open"]),
        timestamp=read_str(data["timestamp"]),
    )


def decode_CryptoBars(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CryptoBars:
    data = read_object(value)
    return CryptoBars(
        bars=[decode_CryptoBar(item0) for item0 in read_list(data["bars"])],
        end=read_str(data["end"]) if data.get("end") is not None else None,
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        pair=read_str(data["pair"]),
        start=read_str(data["start"]) if data.get("start") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CryptoPair(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CryptoPair:
    data = read_object(value)
    return CryptoPair(
        base=read_str(data["base"]),
        name=read_str(data["name"]),
        pair=read_str(data["pair"]),
        quote=read_str(data["quote"]),
    )


def decode_CryptoPairs(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CryptoPairs:
    data = read_object(value)
    return CryptoPairs(
        pairs=[decode_CryptoPair(item0) for item0 in read_list(data["pairs"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CryptoPrice(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CryptoPrice:
    data = read_object(value)
    return CryptoPrice(
        base=read_str(data["base"]),
        change_24h=read_decimal(data["change_24h"])
        if data.get("change_24h") is not None
        else None,
        change_24h_percent=read_decimal(data["change_24h_percent"])
        if data.get("change_24h_percent") is not None
        else None,
        delayed=read_bool(data["delayed"]) if data.get("delayed") is not None else None,
        pair=read_str(data["pair"]),
        price=read_decimal(data["price"]),
        quote=read_str(data["quote"]),
        stale=read_bool(data["stale"]),
        timestamp=read_str(data["timestamp"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_CryptoPriceError(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CryptoPriceError:
    data = read_object(value)
    return CryptoPriceError(
        code=read_str(data["code"]),
        id=read_str(data["id"]),
    )


def decode_CryptoPrices(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> CryptoPrices:
    data = read_object(value)
    return CryptoPrices(
        errors=[decode_CryptoPriceError(item0) for item0 in read_list(data["errors"])],
        prices=[decode_CryptoPrice(item0) for item0 in read_list(data["prices"])],
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


def decode_DividendsCalendar(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> DividendsCalendar:
    data = read_object(value)
    return DividendsCalendar(
        entries=[
            decode_DividendsCalendarEntry(item0) for item0 in read_list(data["entries"])
        ],
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_DividendsCalendarEntry(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> DividendsCalendarEntry:
    data = read_object(value)
    return DividendsCalendarEntry(
        amount=read_decimal(data["amount"]),
        currency=read_str(data["currency"]),
        ex_date=read_str(data["ex_date"]),
        id=read_str(data["id"]),
        name=read_str(data["name"]),
        symbol=read_str(data["symbol"]),
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


def decode_EquityBar(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityBar:
    data = read_object(value)
    return EquityBar(
        close=read_decimal(data["close"]),
        date=read_str(data["date"]) if data.get("date") is not None else None,
        high=read_decimal(data["high"]),
        low=read_decimal(data["low"]),
        open=read_decimal(data["open"]),
        timestamp=read_str(data["timestamp"]),
        volume=read_decimal(data["volume"]) if data.get("volume") is not None else None,
    )


def decode_EquityBars(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityBars:
    data = read_object(value)
    return EquityBars(
        adjusted=read_bool(data["adjusted"]),
        bars=[decode_EquityBar(item0) for item0 in read_list(data["bars"])],
        currency=read_str(data["currency"]),
        end=read_str(data["end"]) if data.get("end") is not None else None,
        id=read_str(data["id"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        start=read_str(data["start"]) if data.get("start") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquityCostOfCapital(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityCostOfCapital:
    data = read_object(value)
    return EquityCostOfCapital(
        beta=decode_CostBeta(data["beta"]),
        company_id=read_str(data["company_id"]),
        cost_of_debt=decode_CostOfDebt(data["cost_of_debt"])
        if data.get("cost_of_debt") is not None
        else None,
        cost_of_equity=read_decimal(data["cost_of_equity"]),
        currency=read_str(data["currency"]),
        equity_risk_premium=decode_CostEquityRiskPremium(data["equity_risk_premium"]),
        id=read_str(data["id"]),
        methodology_url=read_str(data["methodology_url"]),
        risk_free=decode_CostRiskFree(data["risk_free"]),
        tax_rate=decode_CostTaxRate(data["tax_rate"])
        if data.get("tax_rate") is not None
        else None,
        wacc=read_decimal(data["wacc"]) if data.get("wacc") is not None else None,
        warnings=[decode_CostWarning(item0) for item0 in read_list(data["warnings"])],
        weights=decode_CostWeights(data["weights"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquityDividend(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityDividend:
    data = read_object(value)
    return EquityDividend(
        amount=read_decimal(data["amount"]),
        currency=read_str(data["currency"]),
        ex_date=read_str(data["ex_date"]),
        pay_date=read_str(data["pay_date"])
        if data.get("pay_date") is not None
        else None,
        record_date=read_str(data["record_date"])
        if data.get("record_date") is not None
        else None,
    )


def decode_EquityDividends(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityDividends:
    data = read_object(value)
    return EquityDividends(
        dividends=[
            decode_EquityDividend(item0) for item0 in read_list(data["dividends"])
        ],
        id=read_str(data["id"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        start=read_str(data["start"]) if data.get("start") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquityEarning(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityEarning:
    data = read_object(value)
    return EquityEarning(
        date=read_str(data["date"]),
        eps_actual=read_decimal(data["eps_actual"])
        if data.get("eps_actual") is not None
        else None,
        eps_estimate=read_decimal(data["eps_estimate"])
        if data.get("eps_estimate") is not None
        else None,
        filing_id=read_str(data["filing_id"])
        if data.get("filing_id") is not None
        else None,
        surprise=read_decimal(data["surprise"])
        if data.get("surprise") is not None
        else None,
        surprise_percent=read_decimal(data["surprise_percent"])
        if data.get("surprise_percent") is not None
        else None,
        time=read_str(data["time"]) if data.get("time") is not None else None,
    )


def decode_EquityEarnings(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityEarnings:
    data = read_object(value)
    return EquityEarnings(
        earnings=[decode_EquityEarning(item0) for item0 in read_list(data["earnings"])],
        id=read_str(data["id"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        start=read_str(data["start"]) if data.get("start") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquityMover(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityMover:
    data = read_object(value)
    return EquityMover(
        change_percent=read_decimal(data["change_percent"]),
        id=read_str(data["id"]),
        name=read_str(data["name"]),
        price=read_decimal(data["price"]),
        symbol=read_str(data["symbol"]),
        volume=read_decimal(data["volume"]),
    )


def decode_EquityMovers(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityMovers:
    data = read_object(value)
    return EquityMovers(
        direction=read_str(data["direction"]),
        market=read_str(data["market"]),
        movers=[decode_EquityMover(item0) for item0 in read_list(data["movers"])],
        timestamp=read_str(data["timestamp"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquityPrice(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityPrice:
    data = read_object(value)
    return EquityPrice(
        change=read_decimal(data["change"]) if data.get("change") is not None else None,
        change_percent=read_decimal(data["change_percent"])
        if data.get("change_percent") is not None
        else None,
        currency=read_str(data["currency"]),
        delayed=read_bool(data["delayed"]) if data.get("delayed") is not None else None,
        id=read_str(data["id"]),
        market_session=read_str(data["market_session"]),
        previous_close=read_decimal(data["previous_close"])
        if data.get("previous_close") is not None
        else None,
        price=read_decimal(data["price"]),
        stale=read_bool(data["stale"]),
        symbol=read_str(data["symbol"]),
        timestamp=read_str(data["timestamp"]),
        volume=read_decimal(data["volume"]) if data.get("volume") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquityPriceError(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityPriceError:
    data = read_object(value)
    return EquityPriceError(
        code=read_str(data["code"]),
        id=read_str(data["id"]),
    )


def decode_EquityPrices(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityPrices:
    data = read_object(value)
    return EquityPrices(
        errors=[decode_EquityPriceError(item0) for item0 in read_list(data["errors"])],
        prices=[decode_EquityPrice(item0) for item0 in read_list(data["prices"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquityProfile(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityProfile:
    data = read_object(value)
    return EquityProfile(
        company_id=read_str(data["company_id"])
        if data.get("company_id") is not None
        else None,
        country=read_str(data["country"]) if data.get("country") is not None else None,
        currency=read_str(data["currency"]),
        id=read_str(data["id"]),
        industry=read_str(data["industry"])
        if data.get("industry") is not None
        else None,
        logo_url=read_str(data["logo_url"])
        if data.get("logo_url") is not None
        else None,
        mic=read_str(data["mic"]),
        name=read_str(data["name"]),
        sector=read_str(data["sector"]) if data.get("sector") is not None else None,
        symbol=read_str(data["symbol"]),
        type=read_str(data["type"]),
        website=read_str(data["website"]) if data.get("website") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquityRiskPremium(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityRiskPremium:
    data = read_object(value)
    return EquityRiskPremium(
        as_of=read_str(data["as_of"]),
        basis=decode_EquityRiskPremiumBasis(data["basis"]),
        country=read_str(data["country"]),
        country_default_spread=read_decimal(data["country_default_spread"]),
        country_risk_premium=read_decimal(data["country_risk_premium"]),
        mature_erp=read_decimal(data["mature_erp"]),
        methodology_url=read_str(data["methodology_url"])
        if data.get("methodology_url") is not None
        else None,
        total_erp=read_decimal(data["total_erp"]),
        unit=read_str(data["unit"]),
        volatility_ratio=read_decimal(data["volatility_ratio"])
        if data.get("volatility_ratio") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquityRiskPremiumBasis(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityRiskPremiumBasis:
    data = read_object(value)
    return EquityRiskPremiumBasis(
        country_default_spread=read_str(data["country_default_spread"]),
        country_risk_premium=read_str(data["country_risk_premium"]),
        mature_erp=read_str(data["mature_erp"]),
        total_erp=read_str(data["total_erp"]),
        volatility_ratio=read_str(data["volatility_ratio"]),
    )


def decode_EquityRiskPremiumHistoryResponse(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityRiskPremiumHistoryResponse:
    data = read_object(value)
    return EquityRiskPremiumHistoryResponse(
        country=read_str(data["country"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_EquityRiskPremium(item0) for item0 in read_list(data["observations"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquityRiskPremiumList(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityRiskPremiumList:
    data = read_object(value)
    return EquityRiskPremiumList(
        countries=[
            decode_EquityRiskPremium(item0) for item0 in read_list(data["countries"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquitySearchResult(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquitySearchResult:
    data = read_object(value)
    return EquitySearchResult(
        company_id=read_str(data["company_id"])
        if data.get("company_id") is not None
        else None,
        country=read_str(data["country"]) if data.get("country") is not None else None,
        currency=read_str(data["currency"]),
        id=read_str(data["id"]),
        mic=read_str(data["mic"]),
        name=read_str(data["name"]),
        symbol=read_str(data["symbol"]),
        type=read_str(data["type"]),
    )


def decode_EquitySearchResults(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquitySearchResults:
    data = read_object(value)
    return EquitySearchResults(
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        results=[
            decode_EquitySearchResult(item0) for item0 in read_list(data["results"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquitySplit(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquitySplit:
    data = read_object(value)
    return EquitySplit(
        date=read_str(data["date"]),
        ratio=read_str(data["ratio"]),
    )


def decode_EquitySplits(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquitySplits:
    data = read_object(value)
    return EquitySplits(
        id=read_str(data["id"]),
        splits=[decode_EquitySplit(item0) for item0 in read_list(data["splits"])],
        start=read_str(data["start"]) if data.get("start") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquityValuation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityValuation:
    data = read_object(value)
    return EquityValuation(
        company_id=read_str(data["company_id"]),
        currency=read_str(data["currency"]),
        dividend_per_share_ttm=read_decimal(data["dividend_per_share_ttm"])
        if data.get("dividend_per_share_ttm") is not None
        else None,
        dividend_yield=read_decimal(data["dividend_yield"])
        if data.get("dividend_yield") is not None
        else None,
        dividends_period_end=read_str(data["dividends_period_end"])
        if data.get("dividends_period_end") is not None
        else None,
        eps_period_end=read_str(data["eps_period_end"])
        if data.get("eps_period_end") is not None
        else None,
        eps_ttm=read_decimal(data["eps_ttm"])
        if data.get("eps_ttm") is not None
        else None,
        equity_as_of=read_str(data["equity_as_of"])
        if data.get("equity_as_of") is not None
        else None,
        id=read_str(data["id"]),
        market_cap=read_decimal(data["market_cap"])
        if data.get("market_cap") is not None
        else None,
        pb_ratio=read_decimal(data["pb_ratio"])
        if data.get("pb_ratio") is not None
        else None,
        pe_ratio=read_decimal(data["pe_ratio"])
        if data.get("pe_ratio") is not None
        else None,
        ps_ratio=read_decimal(data["ps_ratio"])
        if data.get("ps_ratio") is not None
        else None,
        revenue_period_end=read_str(data["revenue_period_end"])
        if data.get("revenue_period_end") is not None
        else None,
        revenue_ttm=read_decimal(data["revenue_ttm"])
        if data.get("revenue_ttm") is not None
        else None,
        shares_as_of=read_str(data["shares_as_of"])
        if data.get("shares_as_of") is not None
        else None,
        shares_outstanding=read_decimal(data["shares_outstanding"])
        if data.get("shares_outstanding") is not None
        else None,
        timestamp=read_str(data["timestamp"]),
        total_equity=read_decimal(data["total_equity"])
        if data.get("total_equity") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquityValuationHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityValuationHistory:
    data = read_object(value)
    return EquityValuationHistory(
        company_id=read_str(data["company_id"]),
        currency=read_str(data["currency"]),
        id=read_str(data["id"]),
        points=[
            decode_EquityValuationPoint(item0) for item0 in read_list(data["points"])
        ],
        start=read_str(data["start"]) if data.get("start") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_EquityValuationPoint(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> EquityValuationPoint:
    data = read_object(value)
    return EquityValuationPoint(
        date=read_str(data["date"]),
        dividend_yield=read_decimal(data["dividend_yield"])
        if data.get("dividend_yield") is not None
        else None,
        market_cap=read_decimal(data["market_cap"])
        if data.get("market_cap") is not None
        else None,
        pb_ratio=read_decimal(data["pb_ratio"])
        if data.get("pb_ratio") is not None
        else None,
        pe_ratio=read_decimal(data["pe_ratio"])
        if data.get("pe_ratio") is not None
        else None,
        price=read_decimal(data["price"]) if data.get("price") is not None else None,
        price_date=read_str(data["price_date"])
        if data.get("price_date") is not None
        else None,
        ps_ratio=read_decimal(data["ps_ratio"])
        if data.get("ps_ratio") is not None
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


def decode_Filing(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> Filing:
    data = read_object(value)
    return Filing(
        amends=read_str(data["amends"]) if data.get("amends") is not None else None,
        company_id=read_str(data["company_id"]),
        filed_at=read_str(data["filed_at"]),
        filer_id=read_str(data["filer_id"])
        if data.get("filer_id") is not None
        else None,
        form=read_str(data["form"]),
        fp=read_str(data["fp"]) if data.get("fp") is not None else None,
        fy=read_int(data["fy"]) if data.get("fy") is not None else None,
        id=read_str(data["id"]),
        period_end=read_str(data["period_end"])
        if data.get("period_end") is not None
        else None,
        title=read_str(data["title"]) if data.get("title") is not None else None,
        type=read_str(data["type"]),
        url=read_str(data["url"]) if data.get("url") is not None else None,
        withdrawn=read_bool(data["withdrawn"])
        if data.get("withdrawn") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_FilingWebhookEvent(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FilingWebhookEvent:
    data = read_object(value)
    return FilingWebhookEvent(
        company_id=read_str(data["company_id"]),
        filed_at=read_str(data["filed_at"]),
        filing_id=read_str(data["filing_id"]),
        form=read_str(data["form"]),
        fp=read_str(data["fp"]) if data.get("fp") is not None else None,
        fy=read_int(data["fy"]) if data.get("fy") is not None else None,
        period_end=read_str(data["period_end"])
        if data.get("period_end") is not None
        else None,
        subject_id=read_str(data["subject_id"])
        if data.get("subject_id") is not None
        else None,
        type=read_str(data["type"]),
    )


def decode_FinancialRow(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FinancialRow:
    data = read_object(value)
    return FinancialRow(
        currency=read_str(data["currency"])
        if data.get("currency") is not None
        else None,
        derived=[read_str(item0) for item0 in read_list(data["derived"])]
        if data.get("derived") is not None
        else None,
        end=read_str(data["end"]),
        fh=read_int(data["fh"]) if data.get("fh") is not None else None,
        fq=read_int(data["fq"]) if data.get("fq") is not None else None,
        fy=read_int(data["fy"]),
        items={
            key: read_decimal(item)
            for key, item in data.items()
            if item is not None
            and key not in ["currency", "derived", "end", "fh", "fq", "fy"]
        },
    )


def decode_Financials(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> Financials:
    data = read_object(value)
    return Financials(
        annual=[decode_FinancialRow(item0) for item0 in read_list(data["annual"])]
        if data.get("annual") is not None
        else None,
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
        basis=read_str(data["basis"]) if data.get("basis") is not None else None,
        currency=read_str(data["currency"])
        if data.get("currency") is not None
        else None,
        from_fy=read_int(data["from_fy"]) if data.get("from_fy") is not None else None,
        id=read_str(data["id"]),
        quarterly=[decode_FinancialRow(item0) for item0 in read_list(data["quarterly"])]
        if data.get("quarterly") is not None
        else None,
        semiannual=[
            decode_FinancialRow(item0) for item0 in read_list(data["semiannual"])
        ]
        if data.get("semiannual") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_FundDistribution(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FundDistribution:
    data = read_object(value)
    return FundDistribution(
        amount=read_decimal(data["amount"]),
        currency=read_str(data["currency"]),
        ex_date=read_str(data["ex_date"]),
        kind=read_str(data["kind"]) if data.get("kind") is not None else None,
        pay_date=read_str(data["pay_date"])
        if data.get("pay_date") is not None
        else None,
        record_date=read_str(data["record_date"])
        if data.get("record_date") is not None
        else None,
    )


def decode_FundDistributions(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FundDistributions:
    data = read_object(value)
    return FundDistributions(
        distributions=[
            decode_FundDistribution(item0) for item0 in read_list(data["distributions"])
        ],
        id=read_str(data["id"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        start=read_str(data["start"]) if data.get("start") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_FundEtfPrice(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FundEtfPrice:
    data = read_object(value)
    return FundEtfPrice(
        change=read_decimal(data["change"]) if data.get("change") is not None else None,
        change_percent=read_decimal(data["change_percent"])
        if data.get("change_percent") is not None
        else None,
        currency=read_str(data["currency"]),
        delayed=read_bool(data["delayed"]) if data.get("delayed") is not None else None,
        id=read_str(data["id"]),
        market_session=read_str(data["market_session"]),
        previous_close=read_decimal(data["previous_close"])
        if data.get("previous_close") is not None
        else None,
        price=read_decimal(data["price"]),
        stale=read_bool(data["stale"]),
        symbol=read_str(data["symbol"]),
        timestamp=read_str(data["timestamp"]),
        type=read_str(data["type"]),
        volume=read_decimal(data["volume"]) if data.get("volume") is not None else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_FundNavPrice(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FundNavPrice:
    data = read_object(value)
    return FundNavPrice(
        change=read_decimal(data["change"]) if data.get("change") is not None else None,
        change_percent=read_decimal(data["change_percent"])
        if data.get("change_percent") is not None
        else None,
        currency=read_str(data["currency"]),
        date=read_str(data["date"]),
        id=read_str(data["id"]),
        nav=read_decimal(data["nav"]),
        previous_nav=read_decimal(data["previous_nav"])
        if data.get("previous_nav") is not None
        else None,
        stale=read_bool(data["stale"]),
        symbol=read_str(data["symbol"]),
        type=read_str(data["type"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_FundPriceError(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FundPriceError:
    data = read_object(value)
    return FundPriceError(
        code=read_str(data["code"]),
        id=read_str(data["id"]),
    )


def decode_FundPrices(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FundPrices:
    data = read_object(value)
    return FundPrices(
        errors=[decode_FundPriceError(item0) for item0 in read_list(data["errors"])],
        prices=[decode_FundPriceItem(item0) for item0 in read_list(data["prices"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_FundProfile(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FundProfile:
    data = read_object(value)
    return FundProfile(
        country=read_str(data["country"]) if data.get("country") is not None else None,
        currency=read_str(data["currency"]),
        id=read_str(data["id"]),
        mic=read_str(data["mic"]) if data.get("mic") is not None else None,
        name=read_str(data["name"]),
        symbol=read_str(data["symbol"]),
        type=read_str(data["type"]),
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_FundSearchResult(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FundSearchResult:
    data = read_object(value)
    return FundSearchResult(
        country=read_str(data["country"]) if data.get("country") is not None else None,
        currency=read_str(data["currency"]),
        id=read_str(data["id"]),
        mic=read_str(data["mic"]) if data.get("mic") is not None else None,
        name=read_str(data["name"]),
        symbol=read_str(data["symbol"]),
        type=read_str(data["type"]),
    )


def decode_FundSearchResults(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FundSearchResults:
    data = read_object(value)
    return FundSearchResults(
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        results=[
            decode_FundSearchResult(item0) for item0 in read_list(data["results"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_FxBar(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FxBar:
    data = read_object(value)
    return FxBar(
        close=read_decimal(data["close"]),
        high=read_decimal(data["high"]),
        low=read_decimal(data["low"]),
        open=read_decimal(data["open"]),
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
        first_reported_at=read_str(data["first_reported_at"])
        if data.get("first_reported_at") is not None
        else None,
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
        first_reported_at=read_str(data["first_reported_at"])
        if data.get("first_reported_at") is not None
        else None,
        period=read_str(data["period"]),
        value=read_decimal(data["value"]),
    )


def decode_Holder(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> Holder:
    data = read_object(value)
    return Holder(
        event_date=read_str(data["event_date"])
        if data.get("event_date") is not None
        else None,
        filed=read_str(data["filed"]),
        filing_id=read_str(data["filing_id"]),
        holder=read_str(data["holder"]),
        percent=read_decimal(data["percent"])
        if data.get("percent") is not None
        else None,
        security=decode_HolderSecurity(data["security"])
        if data.get("security") is not None
        else None,
        shares=read_decimal(data["shares"]) if data.get("shares") is not None else None,
    )


def decode_HolderSecurity(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> HolderSecurity:
    data = read_object(value)
    return HolderSecurity(
        class_=read_str(data["class"]) if data.get("class") is not None else None,
        isin=read_str(data["isin"]) if data.get("isin") is not None else None,
    )


def decode_HoldersPage(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> HoldersPage:
    data = read_object(value)
    return HoldersPage(
        filed_from=read_str(data["filed_from"])
        if data.get("filed_from") is not None
        else None,
        holders=[decode_Holder(item0) for item0 in read_list(data["holders"])],
        id=read_str(data["id"]),
        meta=meta if meta is not None else ResponseMeta(),
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
        first_reported_at=read_str(data["first_reported_at"])
        if data.get("first_reported_at") is not None
        else None,
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


def decode_LatestFiling(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> LatestFiling:
    data = read_object(value)
    return LatestFiling(
        company_id=read_str(data["company_id"]),
        filed=read_str(data["filed"]),
        form=read_str(data["form"]),
        id=read_str(data["id"]),
        title=read_str(data["title"]) if data.get("title") is not None else None,
        type=read_str(data["type"]),
    )


def decode_LatestFilingsPage(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> LatestFilingsPage:
    data = read_object(value)
    return LatestFilingsPage(
        filings=[decode_LatestFiling(item0) for item0 in read_list(data["filings"])],
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_ListedFiling(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ListedFiling:
    data = read_object(value)
    return ListedFiling(
        filed=read_str(data["filed"]),
        form=read_str(data["form"]),
        id=read_str(data["id"]),
        period_end=read_str(data["period_end"])
        if data.get("period_end") is not None
        else None,
        title=read_str(data["title"]) if data.get("title") is not None else None,
        type=read_str(data["type"]),
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


def decode_PointPolicyRate(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PointPolicyRate:
    data = read_object(value)
    return PointPolicyRate(
        announced_on=read_str(data["announced_on"])
        if data.get("announced_on") is not None
        else None,
        authority=read_str(data["authority"]),
        country=read_str(data["country"]),
        currency=read_str(data["currency"]),
        effective_on=read_str(data["effective_on"])
        if data.get("effective_on") is not None
        else None,
        instrument=read_str(data["instrument"]),
        observed_on=read_str(data["observed_on"])
        if data.get("observed_on") is not None
        else None,
        qualifier=read_str(data["qualifier"]),
        rate=read_decimal(data["rate"]),
        rate_type=read_str(data["rate_type"]),
        unit=read_str(data["unit"]),
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


def decode_PolicyRateHistoryResponse(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PolicyRateHistoryResponse:
    data = read_object(value)
    return PolicyRateHistoryResponse(
        country=read_str(data["country"]),
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        observations=[
            decode_PolicyRateObservation(item0)
            for item0 in read_list(data["observations"])
        ],
        meta=meta if meta is not None else ResponseMeta(),
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


def decode_RangePolicyRate(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> RangePolicyRate:
    data = read_object(value)
    return RangePolicyRate(
        announced_on=read_str(data["announced_on"])
        if data.get("announced_on") is not None
        else None,
        authority=read_str(data["authority"]),
        country=read_str(data["country"]),
        currency=read_str(data["currency"]),
        effective_on=read_str(data["effective_on"])
        if data.get("effective_on") is not None
        else None,
        instrument=read_str(data["instrument"]),
        lower_bound=read_decimal(data["lower_bound"]),
        observed_on=read_str(data["observed_on"])
        if data.get("observed_on") is not None
        else None,
        rate_type=read_str(data["rate_type"]),
        unit=read_str(data["unit"]),
        upper_bound=read_decimal(data["upper_bound"]),
        meta=meta if meta is not None else ResponseMeta(),
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
        first_reported_at=read_str(data["first_reported_at"])
        if data.get("first_reported_at") is not None
        else None,
        period=read_str(data["period"]),
        rate=read_decimal(data["rate"]),
    )


def decode_RegistryCoverage(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> RegistryCoverage:
    data = read_object(value)
    return RegistryCoverage(
        companies=read_int(data["companies"]),
        registry=read_str(data["registry"]),
    )


def decode_ResourceHistory(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> ResourceHistory:
    data = read_object(value)
    return ResourceHistory(
        as_of=read_str(data["as_of"]) if data.get("as_of") is not None else None,
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
        first_reported_at=read_str(data["first_reported_at"])
        if data.get("first_reported_at") is not None
        else None,
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


def decode_SecurityListing(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> SecurityListing:
    data = read_object(value)
    return SecurityListing(
        code=read_str(data["code"]),
        from_=read_str(data["from"]) if data.get("from") is not None else None,
        mic=read_str(data["mic"]),
        to=read_str(data["to"]) if data.get("to") is not None else None,
    )


def decode_SeriesSource(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> SeriesSource:
    data = read_object(value)
    return SeriesSource(
        distributor=read_str(data["distributor"]),
        publisher=read_str(data["publisher"]),
    )


def decode_SplitsCalendar(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> SplitsCalendar:
    data = read_object(value)
    return SplitsCalendar(
        entries=[
            decode_SplitsCalendarEntry(item0) for item0 in read_list(data["entries"])
        ],
        next_cursor=read_cursor(data["next_cursor"])
        if data.get("next_cursor") is not None
        else None,
        meta=meta if meta is not None else ResponseMeta(),
    )


def decode_SplitsCalendarEntry(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> SplitsCalendarEntry:
    data = read_object(value)
    return SplitsCalendarEntry(
        date=read_str(data["date"]),
        id=read_str(data["id"]),
        name=read_str(data["name"]),
        ratio=read_str(data["ratio"]),
        symbol=read_str(data["symbol"]),
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
        first_reported_at=read_str(data["first_reported_at"])
        if data.get("first_reported_at") is not None
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
        companies=[read_str(item0) for item0 in read_list(data["companies"])]
        if data.get("companies") is not None
        else None,
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
        companies=[read_str(item0) for item0 in read_list(data["companies"])]
        if data.get("companies") is not None
        else None,
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
        companies=[read_str(item0) for item0 in read_list(data["companies"])]
        if data.get("companies") is not None
        else None,
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
        filing=decode_FilingWebhookEvent(data["filing"])
        if data.get("filing") is not None
        else None,
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


def decode_FundPrice(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FundPrice:
    data = read_object(value)
    if data.get("type") == "etf":
        return decode_FundEtfPrice(data, meta)
    if data.get("type") == "mutual_fund":
        return decode_FundNavPrice(data, meta)
    return FundPriceUnknown(
        data, meta if meta is not None else ResponseMeta(), raw_body
    )


def decode_FundPriceItem(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> FundPriceItem:
    data = read_object(value)
    if data.get("type") == "etf":
        return decode_FundEtfPrice(data, meta)
    if data.get("type") == "mutual_fund":
        return decode_FundNavPrice(data, meta)
    return FundPriceItemUnknown(
        data, meta if meta is not None else ResponseMeta(), raw_body
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


def decode_PolicyRate(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PolicyRate:
    data = read_object(value)
    if data.get("rate_type") == "point":
        return decode_PointPolicyRate(data, meta)
    if data.get("rate_type") == "range":
        return decode_RangePolicyRate(data, meta)
    return PolicyRateUnknown(
        data, meta if meta is not None else ResponseMeta(), raw_body
    )


def decode_PolicyRateObservation(
    value: object, meta: ResponseMeta | None = None, raw_body: bytes = b""
) -> PolicyRateObservation:
    data = read_object(value)
    if data.get("rate_type") == "point":
        return decode_PointPolicyRate(data, meta)
    if data.get("rate_type") == "range":
        return decode_RangePolicyRate(data, meta)
    return PolicyRateObservationUnknown(
        data, meta if meta is not None else ResponseMeta(), raw_body
    )

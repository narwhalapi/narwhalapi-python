# Generated from spec/live/openapi.json sha256 5071bd97e9507eb56b344d00a24ba056ce1340fe1184faa4d755fe7e407e1cf6. Do not edit.
# Generated from spec/next/openapi.json sha256 5071bd97e9507eb56b344d00a24ba056ce1340fe1184faa4d755fe7e407e1cf6. Do not edit.
from __future__ import annotations

import builtins
from collections.abc import AsyncIterator, Iterator
from decimal import Decimal

from .._pagination import iterate, iterate_async, unknown_page
from .._transport import (
    UNSET,
    AsyncTransport,
    Query,
    SyncTransport,
    Unset,
    encode_body,
    encode_path,
    encode_query,
)
from . import models

LIVE_SPEC_SHA = "5071bd97e9507eb56b344d00a24ba056ce1340fe1184faa4d755fe7e407e1cf6"


class CalendarSubscriptions:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(
        self,
        *,
        countries: builtins.list[str],
        end_date: str,
        families: builtins.list[str] | None | Unset = UNSET,
        include_holidays: bool | None | Unset = UNSET,
        include_releases: bool | None | Unset = UNSET,
        scope: str | None | Unset = UNSET,
        start_date: str,
    ) -> models.CalendarSubscriptionCreated:
        """Create Calendar Subscription

        Stability: stable.

        Args:
            countries: Required body parameter.
            end_date: Required body parameter.
            families: Optional body parameter.
            include_holidays: Optional body parameter.
            include_releases: Optional body parameter.
            scope: Optional body parameter.
            start_date: Required body parameter.

        Returns:
            CalendarSubscriptionCreated: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "POST",
            encode_path("/v1/calendars/subscriptions", {}),
            _query,
            encode_body(
                {
                    "countries": countries,
                    "end_date": end_date,
                    "families": families,
                    "include_holidays": include_holidays,
                    "include_releases": include_releases,
                    "scope": scope,
                    "start_date": start_date,
                }
            ),
            models.decode_CalendarSubscriptionCreated,
        )

    def revoke(self, subscription_id: str) -> models.NoContent:
        """Revoke Calendar Subscription

        Stability: stable.

        Args:
            subscription_id: Required path parameter. Calendar subscription ID (UUID).

        Returns:
            NoContent: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "DELETE",
            encode_path(
                "/v1/calendars/subscriptions/{subscription_id}",
                {"subscription_id": subscription_id},
            ),
            _query,
            None,
            models.decode_NoContent,
        )

    def feed_url(self, token: str) -> str:
        """Read Calendar Subscription

        Revocable calendar-only token URL returned once on subscription creation.

        Stability: stable.

        Args:
            token: Required path parameter.

        Returns:
            str: Calendar feed URL. No request is made.
        """
        return self._transport.base_url + encode_path(
            "/v1/calendars/subscriptions/{token}.ics", {"token": token}
        )


class Calendars:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def holidays_on_date(
        self, country: str, date: str, *, scope: str | None = None
    ) -> models.CalendarHolidaysOnDate:
        """Get Calendar Holidays On Date

        Published public holidays on one date. Returns 404 when no calendar is published for the country, year or scope.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            date: Required path parameter. Date, YYYY-MM-DD. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            scope: Optional query parameter. Only holidays and coverage of this scope, for example national_public.

        Returns:
            CalendarHolidaysOnDate: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("scope", scope, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/calendars/holidays/{country}/on/{date}",
                {"country": country, "date": date},
            ),
            _query,
            None,
            models.decode_CalendarHolidaysOnDate,
        )

    def next_holiday(
        self, country: str, *, from_date: str, scope: str | None = None
    ) -> models.CalendarNextHoliday:
        """Get Calendar Next Holiday

        Next published public holiday on or after a date. Returns 404 when no calendar is published for the country, year or scope.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            from_date: Required query parameter. Date to search from, YYYY-MM-DD. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            scope: Optional query parameter. Only holidays and coverage of this scope, for example national_public.

        Returns:
            CalendarNextHoliday: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("from_date", from_date, "single", required=True, decimal=False)
        )
        _query.extend(
            encode_query("scope", scope, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/calendars/holidays/{country}/next", {"country": country}),
            _query,
            None,
            models.decode_CalendarNextHoliday,
        )

    def list_holidays(
        self,
        country: str,
        year: int,
        *,
        scope: str | None = None,
        version_id: str | None = None,
    ) -> models.CalendarHolidays:
        """List Calendar Holidays

        Published public holidays for a country and year, with the calendar coverage. An empty `subdivision_codes` list means the holiday applies nationwide. Returns 404 when no calendar is published for the country, year or scope.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            year: Required path parameter. Calendar year. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            scope: Optional query parameter. Only holidays and coverage of this scope, for example national_public.
            version_id: Optional query parameter. Immutable calendar version from a holiday event.

        Returns:
            CalendarHolidays: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("scope", scope, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/calendars/holidays/{country}/{year}",
                {"country": country, "year": year},
            ),
            _query,
            None,
            models.decode_CalendarHolidays,
        )


class Commodities:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def palmoil_physical_observations(
        self,
        series_id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        price_month: str | None = None,
        start: str | None = None,
    ) -> models.PalmoilHistory:
        """Get Palmoil Observations

        Palm-oil prices of one series by native period. Supply start and end together.

        Stability: stable.

        Args:
            series_id: Required path parameter. Palm-oil series ID.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. First day to exclude from the range. Supply start and end together.
            limit: Optional query parameter. Maximum rows per page.
            price_month: Optional query parameter. Month to read, YYYY-MM. MPOB CPO series only.
            start: Optional query parameter. First date to include. Supply start and end together.

        Returns:
            PalmoilHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "price_month", price_month, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/palmoil/physical/{series_id}/observations",
                {"series_id": series_id},
            ),
            _query,
            None,
            models.decode_PalmoilHistory,
        )

    def palmoil_physical_observations_iter(
        self,
        series_id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        price_month: str | None = None,
        start: str | None = None,
    ) -> Iterator[models.PalmoilObservation]:
        """Get Palmoil Observations

        Palm-oil prices of one series by native period. Supply start and end together.

        Stability: stable.

        Args:
            series_id: Required path parameter. Palm-oil series ID.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. First day to exclude from the range. Supply start and end together.
            limit: Optional query parameter. Maximum rows per page.
            price_month: Optional query parameter. Month to read, YYYY-MM. MPOB CPO series only.
            start: Optional query parameter. First date to include. Supply start and end together.

        Returns:
            Iterator[PalmoilObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PalmoilObservation], str | None]:
            result = self.palmoil_physical_observations(
                series_id=series_id,
                cursor=next_cursor,
                end=end,
                limit=limit,
                price_month=price_month,
                start=start,
            )
            if isinstance(result, models.PalmoilHistoryUnknown):
                return unknown_page(
                    result.raw,
                    "observations",
                    "next_cursor",
                    lambda value: models.decode_PalmoilObservation(
                        value, page=result.raw
                    ),
                    result._raw_body,
                )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def palmoil_physical_price(
        self, series_id: str, *, price_month: str | None = None
    ) -> models.PalmoilPrice:
        """Get Palmoil Physical

        Latest approved palm-oil price of one series: a single CPO price or a full FFB age schedule.

        Stability: stable.

        Args:
            series_id: Required path parameter. Palm-oil series ID.
            price_month: Optional query parameter. Month to read, YYYY-MM. MPOB CPO series only.

        Returns:
            PalmoilPrice: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "price_month", price_month, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/palmoil/physical/{series_id}", {"series_id": series_id}
            ),
            _query,
            None,
            models.decode_PalmoilPrice,
        )

    def physical_latest(self, series_id: str) -> models.PhysicalLatest:
        """Get Physical Latest

        Latest published price of one physical price series.

        Stability: stable.

        Args:
            series_id: Required path parameter. Series ID. `latest` is not a series ID.

        Returns:
            PhysicalLatest: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/physical/series/{series_id}/latest",
                {"series_id": series_id},
            ),
            _query,
            None,
            models.decode_PhysicalLatest,
        )

    def physical_observations(
        self,
        series_id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.PhysicalObservations:
        """Get Physical Observations

        Published prices of one physical price series. `start` is inclusive and `end` is exclusive. Supply start and end together.

        Stability: stable.

        Args:
            series_id: Required path parameter. Series ID. `latest` is not a series ID.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. First day to exclude from the range. Supply start and end together.
            limit: Optional query parameter. Maximum rows per page.
            start: Optional query parameter. First day to include. Supply start and end together.

        Returns:
            PhysicalObservations: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/physical/series/{series_id}/observations",
                {"series_id": series_id},
            ),
            _query,
            None,
            models.decode_PhysicalObservations,
        )

    def physical_observations_iter(
        self,
        series_id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> Iterator[models.PhysicalObservation]:
        """Get Physical Observations

        Published prices of one physical price series. `start` is inclusive and `end` is exclusive. Supply start and end together.

        Stability: stable.

        Args:
            series_id: Required path parameter. Series ID. `latest` is not a series ID.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. First day to exclude from the range. Supply start and end together.
            limit: Optional query parameter. Maximum rows per page.
            start: Optional query parameter. First day to include. Supply start and end together.

        Returns:
            Iterator[PhysicalObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PhysicalObservation], str | None]:
            result = self.physical_observations(
                series_id=series_id,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def get_physical_series(self, series_id: str) -> models.PhysicalSeries:
        """Get Physical Series

        Definition of one physical price series: commodity, category, product, country, area, price type, basis, currency, unit, unit_quantity, frequency, description, attribution, coverage_start and coverage_end.

        Stability: stable.

        Args:
            series_id: Required path parameter. Series ID. `latest` is not a series ID.

        Returns:
            PhysicalSeries: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/physical/series/{series_id}", {"series_id": series_id}
            ),
            _query,
            None,
            models.decode_PhysicalSeries,
        )

    def price_history(
        self,
        commodity: str,
        currency: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        limit: int | None = None,
        start: str,
    ) -> models.CommodityBars:
        """Get Commodity Price History

        Closed price bars for one commodity and quote currency, from one minute to one day. A request may span at most 3 days of 1m bars, 14 days of 5m bars, 60 days of 15m bars; a longer range returns 400. Wider intervals have no cap.

        Stability: stable.

        Args:
            commodity: Required path parameter.
            currency: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            limit: Optional query parameter.
            start: Required query parameter.

        Returns:
            CommodityBars: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/spot/{commodity}/{currency}/bars",
                {"commodity": commodity, "currency": currency},
            ),
            _query,
            None,
            models.decode_CommodityBars,
        )

    def price_history_iter(
        self,
        commodity: str,
        currency: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        limit: int | None = None,
        start: str,
    ) -> Iterator[models.CommodityBar]:
        """Get Commodity Price History

        Closed price bars for one commodity and quote currency, from one minute to one day. A request may span at most 3 days of 1m bars, 14 days of 5m bars, 60 days of 15m bars; a longer range returns 400. Wider intervals have no cap.

        Stability: stable.

        Args:
            commodity: Required path parameter.
            currency: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            limit: Optional query parameter.
            start: Required query parameter.

        Returns:
            Iterator[CommodityBar]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.CommodityBar], str | None]:
            result = self.price_history(
                commodity=commodity,
                currency=currency,
                cursor=next_cursor,
                end=end,
                interval=interval,
                limit=limit,
                start=start,
            )
            return [item for item in result.bars], result.next_cursor

        return iterate(page, cursor)

    def spot_price(self, commodity: str, currency: str) -> models.CommoditySpot:
        """Get Commodity Spot

        Stability: stable.

        Args:
            commodity: Required path parameter.
            currency: Required path parameter.

        Returns:
            CommoditySpot: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/spot/{commodity}/{currency}",
                {"commodity": commodity, "currency": currency},
            ),
            _query,
            None,
            models.decode_CommoditySpot,
        )

    def list_palmoil_physical_series(
        self,
        *,
        area: str | None = None,
        country: str | None = None,
        currency: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        price_type: str | None = None,
        producer_arrangement: str | None = None,
        producer_type: str | None = None,
        product: str | None = None,
    ) -> models.PalmoilSeriesDiscovery:
        """List Palmoil Physical

        List approved palm-oil price series. Filters combine. A filter that matches nothing returns an empty list.

        Stability: stable.

        Args:
            area: Optional query parameter. Area code inside the country.
            country: Optional query parameter. ISO 3166-1 alpha-3 country code.
            currency: Optional query parameter. Quote currency, ISO 4217 code.
            cursor: Optional query parameter. The next_cursor from the previous page.
            limit: Optional query parameter. Maximum rows per page.
            price_type: Optional query parameter. Price definition.
            producer_arrangement: Optional query parameter. Producer arrangement: purchase_agreement or supported_scheme.
            producer_type: Optional query parameter. Producer type; only smallholder is supported.
            product: Optional query parameter. ffb (fresh fruit bunches) or cpo (crude palm oil).

        Returns:
            PalmoilSeriesDiscovery: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("area", area, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("currency", currency, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "price_type", price_type, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query(
                "producer_arrangement",
                producer_arrangement,
                "single",
                required=False,
                decimal=False,
            )
        )
        _query.extend(
            encode_query(
                "producer_type", producer_type, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("product", product, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/commodities/palmoil/physical", {}),
            _query,
            None,
            models.decode_PalmoilSeriesDiscovery,
        )

    def list_palmoil_physical_series_iter(
        self,
        *,
        area: str | None = None,
        country: str | None = None,
        currency: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        price_type: str | None = None,
        producer_arrangement: str | None = None,
        producer_type: str | None = None,
        product: str | None = None,
    ) -> Iterator[models.PalmoilSeries]:
        """List Palmoil Physical

        List approved palm-oil price series. Filters combine. A filter that matches nothing returns an empty list.

        Stability: stable.

        Args:
            area: Optional query parameter. Area code inside the country.
            country: Optional query parameter. ISO 3166-1 alpha-3 country code.
            currency: Optional query parameter. Quote currency, ISO 4217 code.
            cursor: Optional query parameter. The next_cursor from the previous page.
            limit: Optional query parameter. Maximum rows per page.
            price_type: Optional query parameter. Price definition.
            producer_arrangement: Optional query parameter. Producer arrangement: purchase_agreement or supported_scheme.
            producer_type: Optional query parameter. Producer type; only smallholder is supported.
            product: Optional query parameter. ffb (fresh fruit bunches) or cpo (crude palm oil).

        Returns:
            Iterator[PalmoilSeries]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PalmoilSeries], str | None]:
            result = self.list_palmoil_physical_series(
                area=area,
                country=country,
                currency=currency,
                cursor=next_cursor,
                limit=limit,
                price_type=price_type,
                producer_arrangement=producer_arrangement,
                producer_type=producer_type,
                product=product,
            )
            return [item for item in result.series], result.next_cursor

        return iterate(page, cursor)

    def list_physical_series(
        self,
        *,
        category: str | None = None,
        commodity: str | None = None,
        country: str | None = None,
        currency: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        price_type: str | None = None,
    ) -> models.PhysicalSeriesPage:
        """List Physical Series

        List published physical and official reference price series. Filters combine. A filter that matches nothing returns an empty list.

        Stability: stable.

        Args:
            category: Optional query parameter. Commodity category.
            commodity: Optional query parameter. Commodity slug, for example wheat.
            country: Optional query parameter. Market: ISO 3166-1 alpha-3 code, WLD (world) or EUU (European Union).
            currency: Optional query parameter. Quote currency, ISO 4217 code.
            cursor: Optional query parameter. The next_cursor from the previous page.
            limit: Optional query parameter. Maximum rows per page.
            price_type: Optional query parameter. Price type, for example retail_average.

        Returns:
            PhysicalSeriesPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("category", category, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "commodity", commodity, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("currency", currency, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "price_type", price_type, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/commodities/physical/series", {}),
            _query,
            None,
            models.decode_PhysicalSeriesPage,
        )

    def list_physical_series_iter(
        self,
        *,
        category: str | None = None,
        commodity: str | None = None,
        country: str | None = None,
        currency: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        price_type: str | None = None,
    ) -> Iterator[models.PhysicalSeries]:
        """List Physical Series

        List published physical and official reference price series. Filters combine. A filter that matches nothing returns an empty list.

        Stability: stable.

        Args:
            category: Optional query parameter. Commodity category.
            commodity: Optional query parameter. Commodity slug, for example wheat.
            country: Optional query parameter. Market: ISO 3166-1 alpha-3 code, WLD (world) or EUU (European Union).
            currency: Optional query parameter. Quote currency, ISO 4217 code.
            cursor: Optional query parameter. The next_cursor from the previous page.
            limit: Optional query parameter. Maximum rows per page.
            price_type: Optional query parameter. Price type, for example retail_average.

        Returns:
            Iterator[PhysicalSeries]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PhysicalSeries], str | None]:
            result = self.list_physical_series(
                category=category,
                commodity=commodity,
                country=country,
                currency=currency,
                cursor=next_cursor,
                limit=limit,
                price_type=price_type,
            )
            return [item for item in result.series], result.next_cursor

        return iterate(page, cursor)


class CompanyCalendars:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def dividends(
        self,
        *,
        country: str | None = None,
        end: str | None = None,
        start: str | None = None,
    ) -> models.DividendsCalendar:
        """Company dividends calendar

        Dividends going ex in the window: the ex-date, the amount per share and its currency. `start` and `end` are inclusive days (YYYY-MM-DD); left out, `start` is today (UTC) and `end` is `start`. Dates run from 30 days back to 90 days ahead (400 invalid_query outside), and a request spans at most 7 days (400 range_too_large). `country` is USA, the only country for now (404 not_covered). Only companies in our symbol list appear, with our id and name; units and share classes of one issuer are one row. Open to every plan and one call a request.

        Stability: stable.

        Args:
            country: Optional query parameter. Three-letter country code of the listing. Left out means USA, the only country for now (another one is 404 not_covered).
            end: Optional query parameter. Last day, inclusive. Left out means `start`. At most 7 days from `start` (400 range_too_large).
            start: Optional query parameter. First day (YYYY-MM-DD), inclusive. Left out means today (UTC). Between 30 days back and 90 days ahead.

        Returns:
            DividendsCalendar: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/calendars/dividends", {}),
            _query,
            None,
            models.decode_DividendsCalendar,
        )

    def splits(
        self,
        *,
        country: str | None = None,
        end: str | None = None,
        start: str | None = None,
    ) -> models.SplitsCalendar:
        """Company splits calendar

        Stock splits taking effect in the window, with the ratio as new shares for old (4:1 gives four for one; 1:10 is a reverse split). `start` and `end` are inclusive days (YYYY-MM-DD); left out, `start` is today (UTC) and `end` is `start`. Dates run from 30 days back to 90 days ahead (400 invalid_query outside), and a request spans at most 7 days (400 range_too_large). `country` is USA, the only country for now (404 not_covered). Only companies in our symbol list appear, with our id and name; units and share classes of one issuer are one row. Open to every plan and one call a request.

        Stability: stable.

        Args:
            country: Optional query parameter. Three-letter country code of the listing. Left out means USA, the only country for now (another one is 404 not_covered).
            end: Optional query parameter. Last day, inclusive. Left out means `start`. At most 7 days from `start` (400 range_too_large).
            start: Optional query parameter. First day (YYYY-MM-DD), inclusive. Left out means today (UTC). Between 30 days back and 90 days ahead.

        Returns:
            SplitsCalendar: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/calendars/splits", {}),
            _query,
            None,
            models.decode_SplitsCalendar,
        )


class Crypto:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def bars(
        self,
        pair: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        interval: str | None = None,
        start: str | None = None,
    ) -> models.CryptoBars:
        """Price bars of one crypto pair

        Daily (`1d`, one UTC day, closing at 00:00 UTC) or one-minute (`1m`) bars, oldest first. A day's bar is out at 00:00 UTC (Free: 15 minutes later, and `end` comes back when that cut the range); today's partial bar is never shown. One-minute bars are for Basic and Pro (Free gets 403 plan_upgrade_required). History: Free 12 months, Basic 5 years, Pro everything; `start` is sent back when the plan raised it. Up to 5,000 bars a page, with `next_cursor`; a cursor that no longer matches the prices is 409 cursor_expired. One call a page.

        Stability: stable.

        Args:
            pair: Required path parameter. Crypto pair: the coin, a dash and the quote currency, for example BTC-USD or ETH-EUR. Any case; a slash in place of the dash is accepted. The answer carries the canonical pair.
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same parameters.
            end: Optional query parameter. Last bar. `1d`: a date, inclusive; left out means the latest finished day. `1m`: a UTC time, exclusive; left out means now, or five days after `start`. At most 5 days between `start` and `end` for `1m` (400 range_too_large).
            interval: Optional query parameter. `1d` (one bar per UTC day, closing at 00:00 UTC) or `1m` (one-minute bars, Basic and Pro only). Anything else is 400 invalid_interval.
            start: Optional query parameter. First bar. `1d`: a date (YYYY-MM-DD), inclusive; left out means the oldest bar your plan reaches. `1m`: a UTC time (YYYY-MM-DDTHH:MM:SSZ, or a date for 00:00 UTC), inclusive; left out means one day before `end`.

        Returns:
            CryptoBars: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/crypto/{pair}/bars", {"pair": pair}),
            _query,
            None,
            models.decode_CryptoBars,
        )

    def bars_iter(
        self,
        pair: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        interval: str | None = None,
        start: str | None = None,
    ) -> Iterator[models.CryptoBar]:
        """Price bars of one crypto pair

        Daily (`1d`, one UTC day, closing at 00:00 UTC) or one-minute (`1m`) bars, oldest first. A day's bar is out at 00:00 UTC (Free: 15 minutes later, and `end` comes back when that cut the range); today's partial bar is never shown. One-minute bars are for Basic and Pro (Free gets 403 plan_upgrade_required). History: Free 12 months, Basic 5 years, Pro everything; `start` is sent back when the plan raised it. Up to 5,000 bars a page, with `next_cursor`; a cursor that no longer matches the prices is 409 cursor_expired. One call a page.

        Stability: stable.

        Args:
            pair: Required path parameter. Crypto pair: the coin, a dash and the quote currency, for example BTC-USD or ETH-EUR. Any case; a slash in place of the dash is accepted. The answer carries the canonical pair.
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same parameters.
            end: Optional query parameter. Last bar. `1d`: a date, inclusive; left out means the latest finished day. `1m`: a UTC time, exclusive; left out means now, or five days after `start`. At most 5 days between `start` and `end` for `1m` (400 range_too_large).
            interval: Optional query parameter. `1d` (one bar per UTC day, closing at 00:00 UTC) or `1m` (one-minute bars, Basic and Pro only). Anything else is 400 invalid_interval.
            start: Optional query parameter. First bar. `1d`: a date (YYYY-MM-DD), inclusive; left out means the oldest bar your plan reaches. `1m`: a UTC time (YYYY-MM-DDTHH:MM:SSZ, or a date for 00:00 UTC), inclusive; left out means one day before `end`.

        Returns:
            Iterator[CryptoBar]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.CryptoBar], str | None]:
            result = self.bars(
                pair=pair, cursor=next_cursor, end=end, interval=interval, start=start
            )
            return [item for item in result.bars], result.next_cursor

        return iterate(page, cursor)

    def price(self, pair: str) -> models.CryptoPrice:
        """Latest price of one crypto pair

        The latest composite price of a pair, with the 24-hour change (left out on Free and when it is not known). Crypto trades all day, so there is no market session; `stale` is true when the price is more than 5 minutes old. Free sees the price 15 minutes late and the answer carries `delayed: true`. `change_24h_percent` is in percent.

        Stability: stable.

        Args:
            pair: Required path parameter. Crypto pair: the coin, a dash and the quote currency, for example BTC-USD or ETH-EUR. Any case; a slash in place of the dash is accepted. The answer carries the canonical pair.

        Returns:
            CryptoPrice: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path("/v1/crypto/{pair}/price", {"pair": pair}),
            _query,
            None,
            models.decode_CryptoPrice,
        )

    def prices(self, *, pairs: str) -> models.CryptoPrices:
        """Latest prices for up to 50 crypto pairs

        Latest price of each listed pair (Free sees them 15 minutes late). One call is counted for each pair that returns a price, taken in one step: if fewer calls are left than pairs that resolved, the whole request is refused with 429 quota_exceeded. Pairs that return no price are listed in `errors` (as `id`) and cost nothing. `change_24h_percent` is in percent.

        Stability: stable.

        Args:
            pairs: Required query parameter. Comma-separated pairs, at most 50 after duplicates are removed. Each pair follows the same rules as the single-price route. One call is counted for each pair that returns a price.

        Returns:
            CryptoPrices: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("pairs", pairs, "single", required=True, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/crypto/prices", {}),
            _query,
            None,
            models.decode_CryptoPrices,
        )

    def list_pairs(self, *, quote: str | None = None) -> models.CryptoPairs:
        """Crypto pairs we price

        Every pair we price, by pair (`BTC-USD` style). Optional `quote` (USD, EUR or GBP). A pair is listed while it trades at least once every 30 seconds and dropped when it falls below once every 2 minutes. Read from our own pair list, so it is open to every plan and counts one call.

        Stability: stable.

        Args:
            quote: Optional query parameter. Only pairs quoted in this currency (USD, EUR or GBP).

        Returns:
            CryptoPairs: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("quote", quote, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/crypto/pairs", {}),
            _query,
            None,
            models.decode_CryptoPairs,
        )


class Economics:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def central_bank_balance_sheet(
        self, country: str, *, period: str | None = None
    ) -> models.CentralBankBalanceSheet:
        """Get Central Bank Balance Sheet

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.

        Returns:
            CentralBankBalanceSheet: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/central-bank/balance-sheet",
                {"country": country},
            ),
            _query,
            None,
            models.decode_CentralBankBalanceSheet,
        )

    def central_bank_reserves(
        self, country: str, *, period: str | None = None
    ) -> models.CentralBankReserves:
        """Get Central Bank Reserves

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.

        Returns:
            CentralBankReserves: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/central-bank/reserves", {"country": country}
            ),
            _query,
            None,
            models.decode_CentralBankReserves,
        )

    def cpi(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Cpi:
        """Get Cpi

        Latest headline consumer price index for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY-MM. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            Cpi: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/cpi", {"country": country}),
            _query,
            None,
            models.decode_Cpi,
        )

    def cpi_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.CpiHistory:
        """Get Cpi History

        The headline consumer price index by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            CpiHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/cpi/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_CpiHistory,
        )

    def cpi_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> Iterator[models.CpiHistoryObservation]:
        """Get Cpi History

        The headline consumer price index by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            Iterator[CpiHistoryObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.CpiHistoryObservation], str | None]:
            result = self.cpi_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def get_equity_risk_premium(
        self, country: str, *, date: str | None = None
    ) -> models.EquityRiskPremium:
        """Get Equity Risk Premium

        Stability: stable.

        Args:
            country: Required path parameter.
            date: Optional query parameter.

        Returns:
            EquityRiskPremium: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("date", date, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/equity-risk-premium", {"country": country}
            ),
            _query,
            None,
            models.decode_EquityRiskPremium,
        )

    def equity_risk_premium_history(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.EquityRiskPremiumHistoryResponse:
        """Get Equity Risk Premium History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            EquityRiskPremiumHistoryResponse: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/equity-risk-premium/history",
                {"country": country},
            ),
            _query,
            None,
            models.decode_EquityRiskPremiumHistoryResponse,
        )

    def equity_risk_premium_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> Iterator[models.EquityRiskPremium]:
        """Get Equity Risk Premium History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            Iterator[EquityRiskPremium]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EquityRiskPremium], str | None]:
            result = self.equity_risk_premium_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def gdp(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Gdp:
        """Get Gdp

        Latest GDP at current prices for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY-QN. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            Gdp: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/gdp", {"country": country}),
            _query,
            None,
            models.decode_Gdp,
        )

    def gdp_growth(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.GdpGrowth:
        """Get Gdp Growth

        Latest real GDP growth for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY-QN. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            GdpGrowth: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/gdp-growth", {"country": country}),
            _query,
            None,
            models.decode_GdpGrowth,
        )

    def gdp_growth_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.GdpGrowthHistory:
        """Get Gdp Growth History

        The real GDP growth by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            GdpGrowthHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/gdp-growth/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_GdpGrowthHistory,
        )

    def gdp_growth_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> Iterator[models.GdpGrowthHistoryObservation]:
        """Get Gdp Growth History

        The real GDP growth by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            Iterator[GdpGrowthHistoryObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.GdpGrowthHistoryObservation], str | None]:
            result = self.gdp_growth_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def gdp_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.GdpHistory:
        """Get Gdp History

        The GDP at current prices by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            GdpHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/gdp/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_GdpHistory,
        )

    def gdp_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> Iterator[models.GdpHistoryObservation]:
        """Get Gdp History

        The GDP at current prices by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            Iterator[GdpHistoryObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.GdpHistoryObservation], str | None]:
            result = self.gdp_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def inflation(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Inflation:
        """Get Inflation

        Latest headline inflation for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY-MM. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            Inflation: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/inflation", {"country": country}),
            _query,
            None,
            models.decode_Inflation,
        )

    def inflation_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.InflationHistory:
        """Get Inflation History

        The headline inflation by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            InflationHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/inflation/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_InflationHistory,
        )

    def inflation_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> Iterator[models.InflationHistoryObservation]:
        """Get Inflation History

        The headline inflation by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            Iterator[InflationHistoryObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.InflationHistoryObservation], str | None]:
            result = self.inflation_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def labour_force_participation(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.LabourForceParticipation:
        """Get Labour Force Participation

        Latest labour-force participation rate for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY, YYYY-MM or YYYY-QN. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            LabourForceParticipation: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/labour-force-participation",
                {"country": country},
            ),
            _query,
            None,
            models.decode_LabourForceParticipation,
        )

    def labour_force_participation_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.RateHistory:
        """Get Labour Force Participation History

        The labour-force participation rate by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            RateHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/labour-force-participation/observations",
                {"country": country},
            ),
            _query,
            None,
            models.decode_RateHistory,
        )

    def labour_force_participation_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> Iterator[models.RateHistoryObservation]:
        """Get Labour Force Participation History

        The labour-force participation rate by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            Iterator[RateHistoryObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.RateHistoryObservation], str | None]:
            result = self.labour_force_participation_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def policy_rate(
        self, country: str, *, date: str | None = None
    ) -> models.PolicyRate:
        """Get Policy Rate

        Stability: stable.

        Args:
            country: Required path parameter.
            date: Optional query parameter.

        Returns:
            PolicyRate: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("date", date, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/central-bank/policy-rate", {"country": country}
            ),
            _query,
            None,
            models.decode_PolicyRate,
        )

    def policy_rate_history(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.PolicyRateHistoryResponse:
        """Get Policy Rate History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            PolicyRateHistoryResponse: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/central-bank/policy-rate/history",
                {"country": country},
            ),
            _query,
            None,
            models.decode_PolicyRateHistoryResponse,
        )

    def policy_rate_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> Iterator[models.PolicyRateObservation]:
        """Get Policy Rate History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            Iterator[PolicyRateObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PolicyRateObservation], str | None]:
            result = self.policy_rate_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def get_release(
        self, release_id: str, *, version_id: str | None = None
    ) -> models.EconomicReleaseDetail:
        """Get Economic Release

        One release calendar entry by release ID.

        Stability: stable.

        Args:
            release_id: Required path parameter. Release ID (UUID).
            version_id: Optional query parameter. Immutable release version to read. Omit it for the current one.

        Returns:
            EconomicReleaseDetail: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/calendar/{release_id}", {"release_id": release_id}
            ),
            _query,
            None,
            models.decode_EconomicReleaseDetail,
        )

    def trade(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.TradeSummary:
        """Get Trade

        Latest merchandise trade for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY or YYYY-MM. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            TradeSummary: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/trade", {"country": country}),
            _query,
            None,
            models.decode_TradeSummary,
        )

    def trade_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.TradeHistory:
        """Get Trade History

        The merchandise trade by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            TradeHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/trade/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_TradeHistory,
        )

    def trade_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> Iterator[models.TradeHistoryObservation]:
        """Get Trade History

        The merchandise trade by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            Iterator[TradeHistoryObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.TradeHistoryObservation], str | None]:
            result = self.trade_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def unemployment(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Unemployment:
        """Get Unemployment

        Latest unemployment rate for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY, YYYY-MM or YYYY-QN. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            Unemployment: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/unemployment", {"country": country}),
            _query,
            None,
            models.decode_Unemployment,
        )

    def unemployment_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.RateHistory:
        """Get Unemployment History

        The unemployment rate by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            RateHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/unemployment/observations",
                {"country": country},
            ),
            _query,
            None,
            models.decode_RateHistory,
        )

    def unemployment_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> Iterator[models.RateHistoryObservation]:
        """Get Unemployment History

        The unemployment rate by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            Iterator[RateHistoryObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.RateHistoryObservation], str | None]:
            result = self.unemployment_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def yield_curve(
        self,
        country: str,
        *,
        date: str | None = None,
        maturity: builtins.list[str] | None = None,
        version_id: str | None = None,
    ) -> models.YieldCurve:
        """Get Yield Curve

        Government bond yield curve for one source date, in percent. `curve_type` shows how the country's source defines the curve. Omit `date` for the latest curve.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            date: Optional query parameter. Source date, YYYY-MM-DD. Omit it for the latest curve. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            maturity: Optional query parameter. Comma-separated maturities to return, for example 2y,10y. Omit for all.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current one.

        Returns:
            YieldCurve: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("date", date, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "maturity", maturity, "comma_join", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/yield-curve", {"country": country}),
            _query,
            None,
            models.decode_YieldCurve,
        )

    def yield_curve_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        maturity: builtins.list[str] | None = None,
        start: str | None = None,
    ) -> models.YieldCurveHistoryResponse:
        """Get Yield Curve History

        Government bond yield curves by source date, oldest first, in percent.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The curves as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last source date to include, YYYY-MM-DD.
            limit: Optional query parameter. Maximum rows per page.
            maturity: Optional query parameter. Comma-separated maturities to return, for example 2y,10y. Omit for all.
            start: Optional query parameter. First source date to include, YYYY-MM-DD.

        Returns:
            YieldCurveHistoryResponse: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "maturity", maturity, "comma_join", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/yield-curve/history", {"country": country}
            ),
            _query,
            None,
            models.decode_YieldCurveHistoryResponse,
        )

    def yield_curve_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        maturity: builtins.list[str] | None = None,
        start: str | None = None,
    ) -> Iterator[models.YieldCurveHistoryObservation]:
        """Get Yield Curve History

        Government bond yield curves by source date, oldest first, in percent.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The curves as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last source date to include, YYYY-MM-DD.
            limit: Optional query parameter. Maximum rows per page.
            maturity: Optional query parameter. Comma-separated maturities to return, for example 2y,10y. Omit for all.
            start: Optional query parameter. First source date to include, YYYY-MM-DD.

        Returns:
            Iterator[YieldCurveHistoryObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.YieldCurveHistoryObservation], str | None]:
            result = self.yield_curve_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                maturity=maturity,
                start=start,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def list_equity_risk_premium(self) -> models.EquityRiskPremiumList:
        """List Equity Risk Premium

        Stability: stable.

        Returns:
            EquityRiskPremiumList: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/equity-risk-premium", {}),
            _query,
            None,
            models.decode_EquityRiskPremiumList,
        )

    def list_releases(
        self,
        *,
        countries: builtins.list[str] | None = None,
        cursor: str | None = None,
        end_date: str | None = None,
        limit: int | None = None,
        start_date: str | None = None,
    ) -> models.EconomicCalendar:
        """List Economic Releases

        Release calendar entries for the chosen countries within a date window.

        Stability: stable.

        Args:
            countries: Optional query parameter. Uppercase three-letter country codes (EMU for the euro area). Omit for all.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end_date: Optional query parameter. Last date of the window.
            limit: Optional query parameter. Maximum rows per page.
            start_date: Optional query parameter. First date of the window.

        Returns:
            EconomicCalendar: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "countries", countries, "repeat", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("end_date", end_date, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "start_date", start_date, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/calendar", {}),
            _query,
            None,
            models.decode_EconomicCalendar,
        )

    def list_releases_iter(
        self,
        *,
        countries: builtins.list[str] | None = None,
        cursor: str | None = None,
        end_date: str | None = None,
        limit: int | None = None,
        start_date: str | None = None,
    ) -> Iterator[models.EconomicReleaseSummary]:
        """List Economic Releases

        Release calendar entries for the chosen countries within a date window.

        Stability: stable.

        Args:
            countries: Optional query parameter. Uppercase three-letter country codes (EMU for the euro area). Omit for all.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end_date: Optional query parameter. Last date of the window.
            limit: Optional query parameter. Maximum rows per page.
            start_date: Optional query parameter. First date of the window.

        Returns:
            Iterator[EconomicReleaseSummary]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EconomicReleaseSummary], str | None]:
            result = self.list_releases(
                countries=countries,
                cursor=next_cursor,
                end_date=end_date,
                limit=limit,
                start_date=start_date,
            )
            return [item for item in result.releases], result.next_cursor

        return iterate(page, cursor)

    def read_catalogue_latest_batch(self, *, ids: str) -> models.CatalogueBulkLatest:
        """Read Catalogue Latest Batch

        Stability: stable.

        Args:
            ids: Required query parameter.

        Returns:
            CatalogueBulkLatest: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("ids", ids, "single", required=True, decimal=False))
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/catalogue/latest", {}),
            _query,
            None,
            models.decode_CatalogueBulkLatest,
        )

    def read_catalogue_observations(
        self,
        *,
        cursor: str | None = None,
        end: str | None = None,
        id: str,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.CatalogueHistory:
        """Read Catalogue History

        Stability: stable.

        Args:
            cursor: Optional query parameter.
            end: Optional query parameter.
            id: Required query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            CatalogueHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(encode_query("id", id, "single", required=True, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/catalogue/series/observations", {}),
            _query,
            None,
            models.decode_CatalogueHistory,
        )

    def read_catalogue_observations_iter(
        self,
        *,
        cursor: str | None = None,
        end: str | None = None,
        id: str,
        limit: int | None = None,
        start: str | None = None,
    ) -> Iterator[models.ResourceObservation]:
        """Read Catalogue History

        Stability: stable.

        Args:
            cursor: Optional query parameter.
            end: Optional query parameter.
            id: Required query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            Iterator[ResourceObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.ResourceObservation], str | None]:
            result = self.read_catalogue_observations(
                cursor=next_cursor, end=end, id=id, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def read_catalogue_series(self, *, id: str) -> models.CatalogueSeries:
        """Read Catalogue Series

        Stability: stable.

        Args:
            id: Required query parameter.

        Returns:
            CatalogueSeries: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("id", id, "single", required=True, decimal=False))
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/catalogue/series", {}),
            _query,
            None,
            models.decode_CatalogueSeries,
        )

    def read_series_observations(
        self,
        series_id: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.ResourceHistory:
        """Read Resource History

        Observations of one economic series, oldest first.

        Stability: stable.

        Args:
            series_id: Required path parameter. Series ID (UUID).
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last observation period to include.
            limit: Optional query parameter. Maximum rows per page.
            start: Optional query parameter. First observation period to include.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            ResourceHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/series/{series_id}/observations",
                {"series_id": series_id},
            ),
            _query,
            None,
            models.decode_ResourceHistory,
        )

    def read_series_observations_iter(
        self,
        series_id: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> Iterator[models.ResourceObservation]:
        """Read Resource History

        Observations of one economic series, oldest first.

        Stability: stable.

        Args:
            series_id: Required path parameter. Series ID (UUID).
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last observation period to include.
            limit: Optional query parameter. Maximum rows per page.
            start: Optional query parameter. First observation period to include.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            Iterator[ResourceObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.ResourceObservation], str | None]:
            result = self.read_series_observations(
                series_id=series_id,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def search_catalogue(
        self,
        *,
        country: str | None = None,
        cursor: str | None = None,
        frequency: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        source: str | None = None,
    ) -> models.CatalogueSearchPage:
        """Search Series Catalogue

        Stability: stable.

        Args:
            country: Optional query parameter.
            cursor: Optional query parameter.
            frequency: Optional query parameter.
            limit: Optional query parameter.
            q: Optional query parameter.
            source: Optional query parameter.

        Returns:
            CatalogueSearchPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "frequency", frequency, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("q", q, "single", required=False, decimal=False))
        _query.extend(
            encode_query("source", source, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/catalogue", {}),
            _query,
            None,
            models.decode_CatalogueSearchPage,
        )

    def search_catalogue_iter(
        self,
        *,
        country: str | None = None,
        cursor: str | None = None,
        frequency: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        source: str | None = None,
    ) -> Iterator[models.CatalogueEntry]:
        """Search Series Catalogue

        Stability: stable.

        Args:
            country: Optional query parameter.
            cursor: Optional query parameter.
            frequency: Optional query parameter.
            limit: Optional query parameter.
            q: Optional query parameter.
            source: Optional query parameter.

        Returns:
            Iterator[CatalogueEntry]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.CatalogueEntry], str | None]:
            result = self.search_catalogue(
                country=country,
                cursor=next_cursor,
                frequency=frequency,
                limit=limit,
                q=q,
                source=source,
            )
            return [item for item in result.results], result.next_cursor

        return iterate(page, cursor)


class Equities:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def bars(
        self,
        id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        interval: str | None = None,
        start: str | None = None,
    ) -> models.EquityBars:
        """Price bars of one stock

        Daily (`1d`) or one-minute (`1m`) bars, oldest first, adjusted for splits and dividends. History: Free 12 months, Basic 5 years, Pro everything; `start` is sent back when the plan raised it. One-minute bars are for Basic and Pro (Free gets 403 plan_upgrade_required), reach back to 2020 and cover at most 5 days a call (400 range_too_large). Today's daily bar appears after the exchange closes, and for Free 15 minutes after; `end` is sent back when that cut the range. Up to 5,000 bars a page, with `next_cursor`; a cursor that no longer matches the prices is 409 cursor_expired. One call a page.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters. A cursor stops working when the prices behind it changed (a split or dividend): 409 cursor_expired.
            end: Optional query parameter. Last bar. `1d`: a date, inclusive; left out means the latest session whose bar is out. `1m`: a UTC time, exclusive; left out means now, or five days after `start`. At most 5 days between `start` and `end` for `1m` (400 range_too_large).
            interval: Optional query parameter. `1d` (one bar per session) or `1m` (one-minute bars, Basic and Pro only). Anything else is 400 invalid_interval.
            start: Optional query parameter. First bar. `1d`: a date (YYYY-MM-DD), inclusive; left out means the oldest bar your plan reaches. `1m`: a UTC time (YYYY-MM-DDTHH:MM:SSZ, or a date for 00:00 UTC), inclusive; left out means one day before `end`.

        Returns:
            EquityBars: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/bars", {"id": id}),
            _query,
            None,
            models.decode_EquityBars,
        )

    def bars_iter(
        self,
        id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        interval: str | None = None,
        start: str | None = None,
    ) -> Iterator[models.EquityBar]:
        """Price bars of one stock

        Daily (`1d`) or one-minute (`1m`) bars, oldest first, adjusted for splits and dividends. History: Free 12 months, Basic 5 years, Pro everything; `start` is sent back when the plan raised it. One-minute bars are for Basic and Pro (Free gets 403 plan_upgrade_required), reach back to 2020 and cover at most 5 days a call (400 range_too_large). Today's daily bar appears after the exchange closes, and for Free 15 minutes after; `end` is sent back when that cut the range. Up to 5,000 bars a page, with `next_cursor`; a cursor that no longer matches the prices is 409 cursor_expired. One call a page.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters. A cursor stops working when the prices behind it changed (a split or dividend): 409 cursor_expired.
            end: Optional query parameter. Last bar. `1d`: a date, inclusive; left out means the latest session whose bar is out. `1m`: a UTC time, exclusive; left out means now, or five days after `start`. At most 5 days between `start` and `end` for `1m` (400 range_too_large).
            interval: Optional query parameter. `1d` (one bar per session) or `1m` (one-minute bars, Basic and Pro only). Anything else is 400 invalid_interval.
            start: Optional query parameter. First bar. `1d`: a date (YYYY-MM-DD), inclusive; left out means the oldest bar your plan reaches. `1m`: a UTC time (YYYY-MM-DDTHH:MM:SSZ, or a date for 00:00 UTC), inclusive; left out means one day before `end`.

        Returns:
            Iterator[EquityBar]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EquityBar], str | None]:
            result = self.bars(
                id=id, cursor=next_cursor, end=end, interval=interval, start=start
            )
            return [item for item in result.bars], result.next_cursor

        return iterate(page, cursor)

    def cost_of_capital(
        self,
        id: str,
        *,
        benchmark: str | None = None,
        beta: str | None = None,
        erp: str | None = None,
        frequency: str | None = None,
        period: str | None = None,
        risk_free: str | None = None,
        tax_rate: str | None = None,
        window: str | None = None,
    ) -> models.EquityCostOfCapital:
        """Beta, cost of equity, cost of debt and WACC of one stock

        Beta of one US or Korean stock against a benchmark ETF (weekly returns over two years by default, from prices adjusted for splits and dividends), the risk-free rate (the 10-year point of the country's government yield curve, or yours), the cost of equity (risk-free plus beta times the equity risk premium: yours in `erp`, or by default our own published total premium of the stock's country), the cost of debt (interest expense over average total debt from company filings, or, where that cannot be used, the risk-free rate plus a public table's default spread for the company's interest coverage; before and after tax, with the country's corporate tax rate from a public table unless you send `tax_rate`) and WACC, weighted by market cap and total debt. Every input is in the answer with its value, its basis and its date. Banks and insurers are 422 not_applicable; an input that cannot be worked out correctly is named in 422 inputs_unavailable, never repaired; a number that is shown but needs care comes with a `warnings` entry. Basic and Pro only (Free gets 403 plan_upgrade_required). One call.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            benchmark: Optional query parameter. Listing id of the market proxy beta is measured against: an ETF, fund or stock priced in the same currency as the stock. Left out, it is ARCX:SPY for a US stock, XKRX:069500 for a Korean one and XTKS:1306 for a Japanese one; any other market needs it.
            beta: Optional query parameter. Which beta feeds the cost of equity: `raw` (default) or `adjusted` (0.67 raw plus 0.33). Both are always in the answer.
            erp: Optional query parameter. Your equity risk premium, in percent (5 means 5%). Left out, it is our own published total equity risk premium of the stock's country (the answer names its date and basis). Where we publish none, without it the answer is 400 erp_required. Above 0 and at most 25.
            frequency: Optional query parameter. Return interval: `weekly` (default; the last common trading day of each ISO week) or `monthly`.
            period: Optional query parameter. Period of interest expense: the last 12 months (`ttm`, default) or the latest full fiscal year (`annual`). Korea and Japan have annual figures only, so `annual` is what they get.
            risk_free: Optional query parameter. Your own risk-free rate, in percent. Left out, it is the 10-year point of the country's government yield curve. Needed where we have no curve (Korea): without it the answer is 422 risk_free_unavailable.
            tax_rate: Optional query parameter. Your own tax rate for the debt shield, in percent. Left out, it is the corporate tax rate of the stock's country from Damodaran's public table (PwC rates). Between 0 and 60.
            window: Optional query parameter. How far back the returns reach: `2y` (default) or `5y`.

        Returns:
            EquityCostOfCapital: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "benchmark", benchmark, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("beta", beta, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("erp", erp, "single", required=False, decimal=False))
        _query.extend(
            encode_query(
                "frequency", frequency, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "risk_free", risk_free, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("tax_rate", tax_rate, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("window", window, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/cost-of-capital", {"id": id}),
            _query,
            None,
            models.decode_EquityCostOfCapital,
        )

    def dividends(
        self, id: str, *, cursor: str | None = None
    ) -> models.EquityDividends:
        """Dividends of one stock

        Cash dividends of one listing, newest ex-date first, paged. The list may include announced future rows. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full. `start` is sent only when older rows were cut off; upcoming rows are never cut. Each request counts one call. An unknown id is 404 not_found; a market without data yet is 404 not_covered.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            cursor: Optional query parameter.

        Returns:
            EquityDividends: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/dividends", {"id": id}),
            _query,
            None,
            models.decode_EquityDividends,
        )

    def dividends_iter(
        self, id: str, *, cursor: str | None = None
    ) -> Iterator[models.EquityDividend]:
        """Dividends of one stock

        Cash dividends of one listing, newest ex-date first, paged. The list may include announced future rows. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full. `start` is sent only when older rows were cut off; upcoming rows are never cut. Each request counts one call. An unknown id is 404 not_found; a market without data yet is 404 not_covered.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            cursor: Optional query parameter.

        Returns:
            Iterator[EquityDividend]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EquityDividend], str | None]:
            result = self.dividends(id=id, cursor=next_cursor)
            return [item for item in result.dividends], result.next_cursor

        return iterate(page, cursor)

    def earnings(self, id: str, *, cursor: str | None = None) -> models.EquityEarnings:
        """Earnings of one stock

        Past earnings reports of one listing (dated today or earlier at the exchange), with estimate, actual and surprise, newest first, paged. Upcoming report dates are not included yet. `surprise_percent` is in percent. `eps_actual` is on the market data basis and can differ from the filings EPS in the valuation. `filing_id` names the annual or quarterly report that covers a past report when we hold it. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full. `start` is sent only when older rows were cut off. Each request counts one call. An unknown id is 404 not_found; a market without data yet is 404 not_covered.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            cursor: Optional query parameter.

        Returns:
            EquityEarnings: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/earnings", {"id": id}),
            _query,
            None,
            models.decode_EquityEarnings,
        )

    def earnings_iter(
        self, id: str, *, cursor: str | None = None
    ) -> Iterator[models.EquityEarning]:
        """Earnings of one stock

        Past earnings reports of one listing (dated today or earlier at the exchange), with estimate, actual and surprise, newest first, paged. Upcoming report dates are not included yet. `surprise_percent` is in percent. `eps_actual` is on the market data basis and can differ from the filings EPS in the valuation. `filing_id` names the annual or quarterly report that covers a past report when we hold it. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full. `start` is sent only when older rows were cut off. Each request counts one call. An unknown id is 404 not_found; a market without data yet is 404 not_covered.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            cursor: Optional query parameter.

        Returns:
            Iterator[EquityEarning]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EquityEarning], str | None]:
            result = self.earnings(id=id, cursor=next_cursor)
            return [item for item in result.earnings], result.next_cursor

        return iterate(page, cursor)

    def movers(
        self, *, direction: str | None = None, market: str | None = None
    ) -> models.EquityMovers:
        """Top US stock movers

        The top 25 US stocks and ETFs by `direction`: `gainers`, `losers` or `active` (most traded by value among the day's biggest gainers and losers, not the whole market). Only ordinary shares and ETFs priced at $1 or more, with at least 100,000 shares and $1 million traded today; ranked by us and cached for 10 minutes. `change_percent` is in percent. Basic and Pro only (Free gets 403 plan_upgrade_required). `market` is `us` for now; another market is 404 not_covered, an unknown `direction` is 400 invalid_query. One call.

        Stability: stable.

        Args:
            direction: Optional query parameter. `gainers` (biggest rise), `losers` (biggest fall) or `active` (most traded by value among the day's biggest gainers and losers, not the whole market). Anything else is 400 invalid_query.
            market: Optional query parameter. Market to rank. Only `us` for now; another market is 404 not_covered.

        Returns:
            EquityMovers: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "direction", direction, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("market", market, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/equities/movers", {}),
            _query,
            None,
            models.decode_EquityMovers,
        )

    def price(self, id: str) -> models.EquityPrice:
        """Latest price of one stock

        Latest price of one listing. Free plans see the price 15 minutes late and the answer carries `delayed: true`. `change_percent` is in percent. An unknown id is 404 not_found; a market without prices yet is 404 not_covered.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.

        Returns:
            EquityPrice: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/price", {"id": id}),
            _query,
            None,
            models.decode_EquityPrice,
        )

    def prices(self, *, ids: str) -> models.EquityPrices:
        """Latest prices for up to 50 stocks

        Latest price of each listed id. One call is counted for each id that returns a price, taken in one step: if fewer calls are left than ids that resolved, the whole request is refused with 429 quota_exceeded. Ids that return no price are listed in `errors` and cost nothing. Free plans see prices 15 minutes late. `change_percent` is in percent.

        Stability: stable.

        Args:
            ids: Required query parameter. Comma-separated listing ids, at most 50 after duplicates are removed. Each id follows the same rules as the single-price route. One call is counted for each id that returns a price.

        Returns:
            EquityPrices: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("ids", ids, "single", required=True, decimal=False))
        return self._transport.request(
            "GET",
            encode_path("/v1/equities/prices", {}),
            _query,
            None,
            models.decode_EquityPrices,
        )

    def profile(self, id: str) -> models.EquityProfile:
        """Profile of one stock

        The listing (symbol, name, type, exchange, country, currency), the company's sector, industry and website, and `company_id` when the listing matches a company in our filings. Open to every plan. Japan listings carry only name, exchange, country, currency and `company_id`. Fields that are not known are left out.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.

        Returns:
            EquityProfile: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}", {"id": id}),
            _query,
            None,
            models.decode_EquityProfile,
        )

    def splits(self, id: str) -> models.EquitySplits:
        """Splits of one stock

        Share splits of one listing, newest first. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full. `start` is sent only when older rows were cut off; upcoming rows are never cut. Each request counts one call. An unknown id is 404 not_found; a market without data yet is 404 not_covered.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.

        Returns:
            EquitySplits: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/splits", {"id": id}),
            _query,
            None,
            models.decode_EquitySplits,
        )

    def valuation(self, id: str) -> models.EquityValuation:
        """Market cap, P/E, P/S, P/B and dividend yield of one stock

        Market cap (latest price times shares outstanding), P/E (latest price over trailing 12-month diluted EPS from company filings, GAAP or IFRS as reported), P/S (market cap over trailing 12-month revenue), P/B (market cap over total equity of the latest balance sheet) and dividend yield (trailing 12-month dividends per share over the price, in percent) of one US or Korean listing, with the inputs and the dates they are as of. Korea has P/E only for now; market cap, P/S, P/B and yield come with share counts and dividends. A figure that cannot be worked out correctly is left out, never sent as 0: market cap after a split since the share count, for several share classes without a count each, and for a depositary receipt or foreign filer; P/E when EPS is negative or under 0.01, reported in another currency, or for a depositary receipt. Another class of a company, such as a preferred line, has no figures of its own and shows none. Basic and Pro only (Free gets 403 plan_upgrade_required). A listing outside the US and Korea, or without a clean company match, is 404 not_covered. One call; paid plans see live prices.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.

        Returns:
            EquityValuation: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/valuation", {"id": id}),
            _query,
            None,
            models.decode_EquityValuation,
        )

    def valuation_history(self, id: str) -> models.EquityValuationHistory:
        """Valuation history of one stock

        Market cap, P/E, P/S, P/B and dividend yield at every fiscal period end (quarter or year end) of one US or Korean listing, oldest first. Each point is the closing price on or just before that day, adjusted for splits only, and the figures filed for that period (trailing 12-month EPS, revenue and dividends, total equity, the nearest share count), so a later restatement is in it. A figure that cannot be worked out is left out, never sent as 0, by the same rules as the valuation. History: Basic 5 years, Pro everything; `start` is sent back when the plan cut older periods. Basic and Pro only (Free gets 403 plan_upgrade_required). A listing outside the US and Korea, or without a clean company match, is 404 not_covered. One call.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.

        Returns:
            EquityValuationHistory: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/valuation/history", {"id": id}),
            _query,
            None,
            models.decode_EquityValuationHistory,
        )

    def search(
        self,
        *,
        country: str | None = None,
        cursor: str | None = None,
        q: str,
        type: str | None = None,
    ) -> models.EquitySearchResults:
        """Search stocks by ticker or name

        Listings whose ticker or name starts with `q`, any case: an exact ticker first, then other tickers, then names. Optional `country` (three letters) and `type` filters. Up to 50 a page, with `next_cursor`. Read from our own symbol list, so it is open to every plan and counts one call.

        Stability: stable.

        Args:
            country: Optional query parameter. Only listings in this country, three letters (USA, KOR).
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters.
            q: Required query parameter. Start of a ticker or of a company name, any case, at least 2 characters (for example `ms` or `micro`). Order: the exact ticker, other tickers, the start of a name, then the start of a later word of a name; US primary listings first within each.
            type: Optional query parameter. Only this kind of listing.

        Returns:
            EquitySearchResults: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("q", q, "single", required=True, decimal=False))
        _query.extend(
            encode_query("type", type, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/equities/search", {}),
            _query,
            None,
            models.decode_EquitySearchResults,
        )

    def search_iter(
        self,
        *,
        country: str | None = None,
        cursor: str | None = None,
        q: str,
        type: str | None = None,
    ) -> Iterator[models.EquitySearchResult]:
        """Search stocks by ticker or name

        Listings whose ticker or name starts with `q`, any case: an exact ticker first, then other tickers, then names. Optional `country` (three letters) and `type` filters. Up to 50 a page, with `next_cursor`. Read from our own symbol list, so it is open to every plan and counts one call.

        Stability: stable.

        Args:
            country: Optional query parameter. Only listings in this country, three letters (USA, KOR).
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters.
            q: Required query parameter. Start of a ticker or of a company name, any case, at least 2 characters (for example `ms` or `micro`). Order: the exact ticker, other tickers, the start of a name, then the start of a later word of a name; US primary listings first within each.
            type: Optional query parameter. Only this kind of listing.

        Returns:
            Iterator[EquitySearchResult]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EquitySearchResult], str | None]:
            result = self.search(country=country, cursor=next_cursor, q=q, type=type)
            return [item for item in result.results], result.next_cursor

        return iterate(page, cursor)


class Events:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get(self, event_id: str) -> models.EventDetail:
        """Get Delivery Event

        One delivery event by ID.

        Stability: stable.

        Args:
            event_id: Required path parameter. Event ID (UUID).

        Returns:
            EventDetail: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path("/v1/events/{event_id}", {"event_id": event_id}),
            _query,
            None,
            models.decode_EventDetail,
        )

    def list(
        self,
        *,
        countries: builtins.list[str] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> models.EventsPage:
        """List Delivery Events

        A page of delivery events, oldest first. `next_cursor` is null at the head.

        Stability: stable.

        Args:
            countries: Optional query parameter. Uppercase three-letter country codes (EMU for the euro area). Omit for all.
            cursor: Optional query parameter. Event position to read from: the cursor or next_cursor of an earlier page.
            limit: Optional query parameter. Maximum events per page.

        Returns:
            EventsPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "countries", countries, "repeat", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET", encode_path("/v1/events", {}), _query, None, models.decode_EventsPage
        )

    def list_iter(
        self,
        *,
        countries: builtins.list[str] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> Iterator[models.DeliveryEvent]:
        """List Delivery Events

        A page of delivery events, oldest first. `next_cursor` is null at the head.

        Stability: stable.

        Args:
            countries: Optional query parameter. Uppercase three-letter country codes (EMU for the euro area). Omit for all.
            cursor: Optional query parameter. Event position to read from: the cursor or next_cursor of an earlier page.
            limit: Optional query parameter. Maximum events per page.

        Returns:
            Iterator[DeliveryEvent]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.DeliveryEvent], str | None]:
            result = self.list(countries=countries, cursor=next_cursor, limit=limit)
            return [item for item in result.events], result.next_cursor

        return iterate(page, cursor)


class Filings:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def as_reported(self, filing_id: str) -> models.AsReportedPage:
        """Get As Reported

        Stability: stable.

        Args:
            filing_id: Required path parameter.

        Returns:
            AsReportedPage: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/filings/{filing_id}/financials/as-reported",
                {"filing_id": filing_id},
            ),
            _query,
            None,
            models.decode_AsReportedPage,
        )

    def company(
        self, company_id: str, *, as_of: str | None = None, lang: str | None = None
    ) -> models.CompanyWithListings:
        """Get Company

        Stability: stable.

        Args:
            company_id: Required path parameter.
            as_of: Optional query parameter.
            lang: Optional query parameter.

        Returns:
            CompanyWithListings: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("lang", lang, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/companies/{company_id}", {"company_id": company_id}),
            _query,
            None,
            models.decode_CompanyWithListings,
        )

    def filing(self, filing_id: str, *, lang: str | None = None) -> models.Filing:
        """Get Filing

        Stability: stable.

        Args:
            filing_id: Required path parameter.
            lang: Optional query parameter.

        Returns:
            Filing: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("lang", lang, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/filings/{filing_id}", {"filing_id": filing_id}),
            _query,
            None,
            models.decode_Filing,
        )

    def financials(
        self,
        company_id: str,
        *,
        as_of: str | None = None,
        basis: str | None = None,
        fields: str | None = None,
        fiscal_year: int | None = None,
        period: str | None = None,
        statement: str | None = None,
        version: str | None = None,
    ) -> models.Financials:
        """Get Financials

        Stability: stable.

        Args:
            company_id: Required path parameter.
            as_of: Optional query parameter. Pro plan only.
            basis: Optional query parameter.
            fields: Optional query parameter.
            fiscal_year: Optional query parameter.
            period: Optional query parameter.
            statement: Optional query parameter.
            version: Optional query parameter. first_reported is Pro plan only.

        Returns:
            Financials: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("basis", basis, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("fields", fields, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "fiscal_year", fiscal_year, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "statement", statement, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/companies/{company_id}/financials", {"company_id": company_id}
            ),
            _query,
            None,
            models.decode_Financials,
        )

    def list_company_filings(
        self,
        company_id: str,
        *,
        cursor: str | None = None,
        filed_from: str | None = None,
        filed_to: str | None = None,
        form: str | None = None,
        include_amendments: bool | None = None,
        lang: str | None = None,
        limit: int | None = None,
        type: str | None = None,
    ) -> models.CompanyFilingsPage:
        """List Company Filings

        Stability: stable.

        Args:
            company_id: Required path parameter.
            cursor: Optional query parameter.
            filed_from: Optional query parameter.
            filed_to: Optional query parameter.
            form: Optional query parameter.
            include_amendments: Optional query parameter.
            lang: Optional query parameter.
            limit: Optional query parameter.
            type: Optional query parameter.

        Returns:
            CompanyFilingsPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "filed_from", filed_from, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("filed_to", filed_to, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("form", form, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "include_amendments",
                include_amendments,
                "single",
                required=False,
                decimal=False,
            )
        )
        _query.extend(
            encode_query("lang", lang, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("type", type, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/companies/{company_id}/filings", {"company_id": company_id}
            ),
            _query,
            None,
            models.decode_CompanyFilingsPage,
        )

    def list_company_filings_iter(
        self,
        company_id: str,
        *,
        cursor: str | None = None,
        filed_from: str | None = None,
        filed_to: str | None = None,
        form: str | None = None,
        include_amendments: bool | None = None,
        lang: str | None = None,
        limit: int | None = None,
        type: str | None = None,
    ) -> Iterator[models.ListedFiling]:
        """List Company Filings

        Stability: stable.

        Args:
            company_id: Required path parameter.
            cursor: Optional query parameter.
            filed_from: Optional query parameter.
            filed_to: Optional query parameter.
            form: Optional query parameter.
            include_amendments: Optional query parameter.
            lang: Optional query parameter.
            limit: Optional query parameter.
            type: Optional query parameter.

        Returns:
            Iterator[ListedFiling]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.ListedFiling], str | None]:
            result = self.list_company_filings(
                company_id=company_id,
                cursor=next_cursor,
                filed_from=filed_from,
                filed_to=filed_to,
                form=form,
                include_amendments=include_amendments,
                lang=lang,
                limit=limit,
                type=type,
            )
            return [item for item in result.filings], result.next_cursor

        return iterate(page, cursor)

    def list_holders(
        self,
        company_id: str,
        *,
        lang: str | None = None,
        limit: int | None = None,
        security: str | None = None,
    ) -> models.HoldersPage:
        """List Holders

        Stability: stable.

        Args:
            company_id: Required path parameter.
            lang: Optional query parameter.
            limit: Optional query parameter.
            security: Optional query parameter.

        Returns:
            HoldersPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("lang", lang, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("security", security, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/companies/{company_id}/holders", {"company_id": company_id}
            ),
            _query,
            None,
            models.decode_HoldersPage,
        )

    def list_latest_filings(
        self,
        *,
        country: str | None = None,
        lang: str | None = None,
        limit: int | None = None,
        type: str | None = None,
    ) -> models.LatestFilingsPage:
        """List Latest Filings

        Stability: stable.

        Args:
            country: Optional query parameter.
            lang: Optional query parameter.
            limit: Optional query parameter.
            type: Optional query parameter.

        Returns:
            LatestFilingsPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("lang", lang, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("type", type, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/filings/latest", {}),
            _query,
            None,
            models.decode_LatestFilingsPage,
        )

    def search_companies(
        self,
        *,
        as_of: str | None = None,
        country: str | None = None,
        lang: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        registry: str | None = None,
    ) -> models.CompanySearchPage:
        """Search Companies

        Stability: stable.

        Args:
            as_of: Optional query parameter.
            country: Optional query parameter.
            lang: Optional query parameter.
            limit: Optional query parameter.
            q: Optional query parameter.
            registry: Optional query parameter.

        Returns:
            CompanySearchPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("lang", lang, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("q", q, "single", required=False, decimal=False))
        _query.extend(
            encode_query("registry", registry, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/companies", {}),
            _query,
            None,
            models.decode_CompanySearchPage,
        )


class Funds:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def bars(
        self,
        id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        interval: str | None = None,
        start: str | None = None,
    ) -> models.EquityBars:
        """Price bars of one fund

        Daily (`1d`) or one-minute (`1m`) bars, oldest first, in the stock bar shape. A mutual fund's daily bar is its daily NAV (open, high, low and close are the NAV, no volume); it has no one-minute bars (400 invalid_interval). One-minute bars are for ETFs on Basic and Pro (Free gets 403 plan_upgrade_required). History: Free 12 months, Basic 5 years, Pro everything; `start` is sent back when the plan raised it. Up to 5,000 bars a page, with `next_cursor`; a cursor that no longer matches the prices is 409 cursor_expired. One call a page.

        Stability: stable.

        Args:
            id: Required path parameter. Fund id. An ETF is its listing id: the exchange's four-letter code, a colon and the ticker (ARCX:SPY). A mutual fund is FUND, a colon and its ticker (FUND:VFIAX). A bare US ticker such as SPY also works when it names one US listing; the answer carries the canonical id.
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters. A cursor stops working when the prices behind it changed (a split or dividend): 409 cursor_expired.
            end: Optional query parameter. Last bar. `1d`: a date, inclusive; left out means the latest session whose bar is out. `1m`: a UTC time, exclusive; left out means now, or five days after `start`. At most 5 days between `start` and `end` for `1m` (400 range_too_large).
            interval: Optional query parameter. `1d` (one bar per session; a mutual fund's bar is its daily NAV) or `1m` (one-minute bars: ETFs only, Basic and Pro only). Anything else is 400 invalid_interval.
            start: Optional query parameter. First bar. `1d`: a date (YYYY-MM-DD), inclusive; left out means the oldest bar your plan reaches. `1m`: a UTC time (YYYY-MM-DDTHH:MM:SSZ, or a date for 00:00 UTC), inclusive; left out means one day before `end`.

        Returns:
            EquityBars: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/funds/{id}/bars", {"id": id}),
            _query,
            None,
            models.decode_EquityBars,
        )

    def bars_iter(
        self,
        id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        interval: str | None = None,
        start: str | None = None,
    ) -> Iterator[models.EquityBar]:
        """Price bars of one fund

        Daily (`1d`) or one-minute (`1m`) bars, oldest first, in the stock bar shape. A mutual fund's daily bar is its daily NAV (open, high, low and close are the NAV, no volume); it has no one-minute bars (400 invalid_interval). One-minute bars are for ETFs on Basic and Pro (Free gets 403 plan_upgrade_required). History: Free 12 months, Basic 5 years, Pro everything; `start` is sent back when the plan raised it. Up to 5,000 bars a page, with `next_cursor`; a cursor that no longer matches the prices is 409 cursor_expired. One call a page.

        Stability: stable.

        Args:
            id: Required path parameter. Fund id. An ETF is its listing id: the exchange's four-letter code, a colon and the ticker (ARCX:SPY). A mutual fund is FUND, a colon and its ticker (FUND:VFIAX). A bare US ticker such as SPY also works when it names one US listing; the answer carries the canonical id.
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters. A cursor stops working when the prices behind it changed (a split or dividend): 409 cursor_expired.
            end: Optional query parameter. Last bar. `1d`: a date, inclusive; left out means the latest session whose bar is out. `1m`: a UTC time, exclusive; left out means now, or five days after `start`. At most 5 days between `start` and `end` for `1m` (400 range_too_large).
            interval: Optional query parameter. `1d` (one bar per session; a mutual fund's bar is its daily NAV) or `1m` (one-minute bars: ETFs only, Basic and Pro only). Anything else is 400 invalid_interval.
            start: Optional query parameter. First bar. `1d`: a date (YYYY-MM-DD), inclusive; left out means the oldest bar your plan reaches. `1m`: a UTC time (YYYY-MM-DDTHH:MM:SSZ, or a date for 00:00 UTC), inclusive; left out means one day before `end`.

        Returns:
            Iterator[EquityBar]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EquityBar], str | None]:
            result = self.bars(
                id=id, cursor=next_cursor, end=end, interval=interval, start=start
            )
            return [item for item in result.bars], result.next_cursor

        return iterate(page, cursor)

    def distributions(
        self, id: str, *, cursor: str | None = None
    ) -> models.FundDistributions:
        """Distributions of one fund

        Distributions of one fund, newest ex-date first, paged. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full; `start` is sent only when older rows were cut off. Each request counts one call. An unknown id is 404 not_found.

        Stability: stable.

        Args:
            id: Required path parameter. Fund id. An ETF is its listing id: the exchange's four-letter code, a colon and the ticker (ARCX:SPY). A mutual fund is FUND, a colon and its ticker (FUND:VFIAX). A bare US ticker such as SPY also works when it names one US listing; the answer carries the canonical id.
            cursor: Optional query parameter.

        Returns:
            FundDistributions: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/funds/{id}/distributions", {"id": id}),
            _query,
            None,
            models.decode_FundDistributions,
        )

    def distributions_iter(
        self, id: str, *, cursor: str | None = None
    ) -> Iterator[models.FundDistribution]:
        """Distributions of one fund

        Distributions of one fund, newest ex-date first, paged. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full; `start` is sent only when older rows were cut off. Each request counts one call. An unknown id is 404 not_found.

        Stability: stable.

        Args:
            id: Required path parameter. Fund id. An ETF is its listing id: the exchange's four-letter code, a colon and the ticker (ARCX:SPY). A mutual fund is FUND, a colon and its ticker (FUND:VFIAX). A bare US ticker such as SPY also works when it names one US listing; the answer carries the canonical id.
            cursor: Optional query parameter.

        Returns:
            Iterator[FundDistribution]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.FundDistribution], str | None]:
            result = self.distributions(id=id, cursor=next_cursor)
            return [item for item in result.distributions], result.next_cursor

        return iterate(page, cursor)

    def price(self, id: str) -> models.FundPrice:
        """Latest price of one fund

        An ETF's last price, in the stock price shape plus `type: etf` (Free sees it 15 minutes late and the answer carries `delayed: true`), or a mutual fund's latest NAV (`type: mutual_fund`: `nav`, `previous_nav`, `change`, `change_percent` and the NAV's `date`; an end-of-day value, never delayed, `stale` once it is older than the next business day). `change_percent` is in percent. A stock id is 404 not_found.

        Stability: stable.

        Args:
            id: Required path parameter. Fund id. An ETF is its listing id: the exchange's four-letter code, a colon and the ticker (ARCX:SPY). A mutual fund is FUND, a colon and its ticker (FUND:VFIAX). A bare US ticker such as SPY also works when it names one US listing; the answer carries the canonical id.

        Returns:
            FundPrice: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path("/v1/funds/{id}/price", {"id": id}),
            _query,
            None,
            models.decode_FundPrice,
        )

    def prices(self, *, ids: str) -> models.FundPrices:
        """Latest prices for up to 50 funds

        Latest price of each listed fund: an ETF's last price (Free sees it 15 minutes late) or a mutual fund's latest NAV. One call is counted for each id that returns a price, taken in one step: if fewer calls are left than ids that resolved, the whole request is refused with 429 quota_exceeded. Ids that return no price are listed in `errors` and cost nothing. `change_percent` is in percent.

        Stability: stable.

        Args:
            ids: Required query parameter. Comma-separated fund ids, at most 50 after duplicates are removed. Each id follows the same rules as the single-price route. One call is counted for each id that returns a price.

        Returns:
            FundPrices: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("ids", ids, "single", required=True, decimal=False))
        return self._transport.request(
            "GET",
            encode_path("/v1/funds/prices", {}),
            _query,
            None,
            models.decode_FundPrices,
        )

    def profile(self, id: str) -> models.FundProfile:
        """Profile of one fund

        The fund's symbol, name, type (`etf` or `mutual_fund`), exchange (ETFs only), country and currency, as our symbol list holds them. Open to every plan. Fields that are not known are left out.

        Stability: stable.

        Args:
            id: Required path parameter. Fund id. An ETF is its listing id: the exchange's four-letter code, a colon and the ticker (ARCX:SPY). A mutual fund is FUND, a colon and its ticker (FUND:VFIAX). A bare US ticker such as SPY also works when it names one US listing; the answer carries the canonical id.

        Returns:
            FundProfile: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path("/v1/funds/{id}", {"id": id}),
            _query,
            None,
            models.decode_FundProfile,
        )

    def search(
        self,
        *,
        country: str | None = None,
        cursor: str | None = None,
        q: str,
        type: str | None = None,
    ) -> models.FundSearchResults:
        """Search ETFs and mutual funds by ticker or name

        Funds whose ticker or name starts with `q`, any case: an exact ticker first, then other tickers, then names. Optional `type` (`etf` or `mutual_fund`) and `country` (three letters) filters. Up to 50 a page, with `next_cursor`. Read from our own symbol list, so it is open to every plan and counts one call.

        Stability: stable.

        Args:
            country: Optional query parameter. Only funds in this country, three letters (USA).
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters.
            q: Required query parameter. Start of a ticker or of a fund name, any case, at least 2 characters (for example `vf` or `vanguard 500`). Order: the exact ticker, other tickers, the start of a name, then the start of a later word of a name.
            type: Optional query parameter. Only ETFs or only mutual funds.

        Returns:
            FundSearchResults: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("q", q, "single", required=True, decimal=False))
        _query.extend(
            encode_query("type", type, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/funds/search", {}),
            _query,
            None,
            models.decode_FundSearchResults,
        )

    def search_iter(
        self,
        *,
        country: str | None = None,
        cursor: str | None = None,
        q: str,
        type: str | None = None,
    ) -> Iterator[models.FundSearchResult]:
        """Search ETFs and mutual funds by ticker or name

        Funds whose ticker or name starts with `q`, any case: an exact ticker first, then other tickers, then names. Optional `type` (`etf` or `mutual_fund`) and `country` (three letters) filters. Up to 50 a page, with `next_cursor`. Read from our own symbol list, so it is open to every plan and counts one call.

        Stability: stable.

        Args:
            country: Optional query parameter. Only funds in this country, three letters (USA).
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters.
            q: Required query parameter. Start of a ticker or of a fund name, any case, at least 2 characters (for example `vf` or `vanguard 500`). Order: the exact ticker, other tickers, the start of a name, then the start of a later word of a name.
            type: Optional query parameter. Only ETFs or only mutual funds.

        Returns:
            Iterator[FundSearchResult]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.FundSearchResult], str | None]:
            result = self.search(country=country, cursor=next_cursor, q=q, type=type)
            return [item for item in result.results], result.next_cursor

        return iterate(page, cursor)


class Fx:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def convert_currency(
        self, *, amount: Decimal | str, from_: str, to: str
    ) -> models.FxConversion:
        """Convert Fx

        Stability: stable.

        Args:
            amount: Required query parameter.
            from_: Required query parameter.
            to: Required query parameter.

        Returns:
            FxConversion: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("amount", amount, "single", required=True, decimal=True)
        )
        _query.extend(
            encode_query("from", from_, "single", required=True, decimal=False)
        )
        _query.extend(encode_query("to", to, "single", required=True, decimal=False))
        return self._transport.request(
            "GET",
            encode_path("/v1/fx/convert", {}),
            _query,
            None,
            models.decode_FxConversion,
        )

    def rate_bars(
        self,
        base: str,
        *,
        currency: str,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        limit: int | None = None,
        start: str,
    ) -> models.FxBars:
        """Get Fx Rate Bars

        Closed open-high-low-close bars for one currency against USD, from one minute to one day. A request may span at most 3 days of 1m bars, 14 days of 5m bars, 60 days of 15m bars; a longer range returns 400. Wider intervals have no cap.

        Stability: stable.

        Args:
            base: Required path parameter.
            currency: Required query parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            limit: Optional query parameter.
            start: Required query parameter.

        Returns:
            FxBars: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("currency", currency, "single", required=True, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/fx/rates/{base}/bars", {"base": base}),
            _query,
            None,
            models.decode_FxBars,
        )

    def rate_bars_iter(
        self,
        base: str,
        *,
        currency: str,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        limit: int | None = None,
        start: str,
    ) -> Iterator[models.FxBar]:
        """Get Fx Rate Bars

        Closed open-high-low-close bars for one currency against USD, from one minute to one day. A request may span at most 3 days of 1m bars, 14 days of 5m bars, 60 days of 15m bars; a longer range returns 400. Wider intervals have no cap.

        Stability: stable.

        Args:
            base: Required path parameter.
            currency: Required query parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            limit: Optional query parameter.
            start: Required query parameter.

        Returns:
            Iterator[FxBar]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.FxBar], str | None]:
            result = self.rate_bars(
                base=base,
                currency=currency,
                cursor=next_cursor,
                end=end,
                interval=interval,
                limit=limit,
                start=start,
            )
            return [item for item in result.bars], result.next_cursor

        return iterate(page, cursor)

    def rate_history(
        self,
        base: str,
        *,
        currencies: builtins.list[str],
        cursor: str | None = None,
        end_date: str,
        limit: int | None = None,
        start_date: str,
    ) -> models.FxHistory:
        """Get Fx Rate History

        Stability: stable.

        Args:
            base: Required path parameter.
            currencies: Required query parameter.
            cursor: Optional query parameter.
            end_date: Required query parameter.
            limit: Optional query parameter.
            start_date: Required query parameter.

        Returns:
            FxHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "currencies", currencies, "comma_join", required=True, decimal=False
            )
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("end_date", end_date, "single", required=True, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "start_date", start_date, "single", required=True, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/fx/rates/{base}/observations", {"base": base}),
            _query,
            None,
            models.decode_FxHistory,
        )

    def rate_history_iter(
        self,
        base: str,
        *,
        currencies: builtins.list[str],
        cursor: str | None = None,
        end_date: str,
        limit: int | None = None,
        start_date: str,
    ) -> Iterator[models.FxHistoricalObservation]:
        """Get Fx Rate History

        Stability: stable.

        Args:
            base: Required path parameter.
            currencies: Required query parameter.
            cursor: Optional query parameter.
            end_date: Required query parameter.
            limit: Optional query parameter.
            start_date: Required query parameter.

        Returns:
            Iterator[FxHistoricalObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.FxHistoricalObservation], str | None]:
            result = self.rate_history(
                base=base,
                currencies=currencies,
                cursor=next_cursor,
                end_date=end_date,
                limit=limit,
                start_date=start_date,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def rates(
        self, base: str, *, currencies: builtins.list[str] | None = None
    ) -> models.FxRates:
        """Get Fx Rates

        Stability: stable.

        Args:
            base: Required path parameter.
            currencies: Optional query parameter.

        Returns:
            FxRates: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "currencies", currencies, "comma_join", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/fx/rates/{base}", {"base": base}),
            _query,
            None,
            models.decode_FxRates,
        )


class Predictions:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def binary(self, event_id: str, *, at: str | None = None) -> models.BinaryEvent:
        """Get Binary Prediction

        Stability: stable.

        Args:
            event_id: Required path parameter.
            at: Optional query parameter.

        Returns:
            BinaryEvent: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("at", at, "single", required=False, decimal=False))
        return self._transport.request(
            "GET",
            encode_path("/v1/predictions/binary/{event_id}", {"event_id": event_id}),
            _query,
            None,
            models.decode_BinaryEvent,
        )

    def binary_history(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> models.PredictionHistory:
        """Get Binary Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/predictions/binary/{event_id}/history", {"event_id": event_id}
            ),
            _query,
            None,
            models.decode_PredictionHistory,
        )

    def binary_history_iter(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> Iterator[models.PredictionSeries]:
        """Get Binary Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            Iterator[PredictionSeries]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PredictionSeries], str | None]:
            result = self.binary_history(
                event_id=event_id,
                cursor=next_cursor,
                end=end,
                interval=interval,
                start=start,
            )
            return [item for item in result.series], result.next_cursor

        return iterate(page, cursor)

    def extreme(self, event_id: str, *, at: str | None = None) -> models.ExtremeEvent:
        """Get Extreme Prediction

        Stability: stable.

        Args:
            event_id: Required path parameter.
            at: Optional query parameter.

        Returns:
            ExtremeEvent: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("at", at, "single", required=False, decimal=False))
        return self._transport.request(
            "GET",
            encode_path("/v1/predictions/extreme/{event_id}", {"event_id": event_id}),
            _query,
            None,
            models.decode_ExtremeEvent,
        )

    def extreme_history(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> models.PredictionHistory:
        """Get Extreme Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/predictions/extreme/{event_id}/history", {"event_id": event_id}
            ),
            _query,
            None,
            models.decode_PredictionHistory,
        )

    def extreme_history_iter(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> Iterator[models.PredictionSeries]:
        """Get Extreme Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            Iterator[PredictionSeries]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PredictionSeries], str | None]:
            result = self.extreme_history(
                event_id=event_id,
                cursor=next_cursor,
                end=end,
                interval=interval,
                start=start,
            )
            return [item for item in result.series], result.next_cursor

        return iterate(page, cursor)

    def policy_path(self, authority: str) -> models.PolicyPath:
        """Get Policy Path

        Stability: stable.

        Args:
            authority: Required path parameter.

        Returns:
            PolicyPath: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/predictions/policy-paths/{authority}", {"authority": authority}
            ),
            _query,
            None,
            models.decode_PolicyPath,
        )

    def policy_path_history(
        self, authority: str, *, end: str, start: str
    ) -> models.PolicyPathHistory:
        """Get Policy Path History

        Stability: stable.

        Args:
            authority: Required path parameter.
            end: Required query parameter.
            start: Required query parameter.

        Returns:
            PolicyPathHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/predictions/policy-paths/{authority}/history",
                {"authority": authority},
            ),
            _query,
            None,
            models.decode_PolicyPathHistory,
        )

    def scalar(self, event_id: str, *, at: str | None = None) -> models.ScalarEvent:
        """Get Scalar Prediction

        Stability: stable.

        Args:
            event_id: Required path parameter.
            at: Optional query parameter.

        Returns:
            ScalarEvent: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("at", at, "single", required=False, decimal=False))
        return self._transport.request(
            "GET",
            encode_path("/v1/predictions/scalar/{event_id}", {"event_id": event_id}),
            _query,
            None,
            models.decode_ScalarEvent,
        )

    def scalar_history(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> models.PredictionHistory:
        """Get Scalar Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/predictions/scalar/{event_id}/history", {"event_id": event_id}
            ),
            _query,
            None,
            models.decode_PredictionHistory,
        )

    def scalar_history_iter(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> Iterator[models.PredictionSeries]:
        """Get Scalar Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            Iterator[PredictionSeries]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PredictionSeries], str | None]:
            result = self.scalar_history(
                event_id=event_id,
                cursor=next_cursor,
                end=end,
                interval=interval,
                start=start,
            )
            return [item for item in result.series], result.next_cursor

        return iterate(page, cursor)

    def timing(self, event_id: str, *, at: str | None = None) -> models.TimingEvent:
        """Get Timing Prediction

        Stability: stable.

        Args:
            event_id: Required path parameter.
            at: Optional query parameter.

        Returns:
            TimingEvent: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("at", at, "single", required=False, decimal=False))
        return self._transport.request(
            "GET",
            encode_path("/v1/predictions/timing/{event_id}", {"event_id": event_id}),
            _query,
            None,
            models.decode_TimingEvent,
        )

    def timing_history(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> models.PredictionHistory:
        """Get Timing Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/predictions/timing/{event_id}/history", {"event_id": event_id}
            ),
            _query,
            None,
            models.decode_PredictionHistory,
        )

    def timing_history_iter(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> Iterator[models.PredictionSeries]:
        """Get Timing Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            Iterator[PredictionSeries]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PredictionSeries], str | None]:
            result = self.timing_history(
                event_id=event_id,
                cursor=next_cursor,
                end=end,
                interval=interval,
                start=start,
            )
            return [item for item in result.series], result.next_cursor

        return iterate(page, cursor)

    def get_topic(self, topic_id: str) -> models.PredictionTopicDetail:
        """Get Prediction Topic

        Stability: stable.

        Args:
            topic_id: Required path parameter.

        Returns:
            PredictionTopicDetail: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path("/v1/predictions/topics/{topic_id}", {"topic_id": topic_id}),
            _query,
            None,
            models.decode_PredictionTopicDetail,
        )

    def list_events(
        self,
        *,
        cursor: str | None = None,
        from_: str | None = None,
        limit: int | None = None,
        release_id: str | None = None,
        shape: str | None = None,
        status: str | None = None,
        to: str | None = None,
        topic: str | None = None,
    ) -> models.PredictionEventsPage:
        """List Prediction Events

        Stability: stable.

        Args:
            cursor: Optional query parameter.
            from_: Optional query parameter.
            limit: Optional query parameter.
            release_id: Optional query parameter.
            shape: Optional query parameter.
            status: Optional query parameter.
            to: Optional query parameter.
            topic: Optional query parameter.

        Returns:
            PredictionEventsPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("from", from_, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "release_id", release_id, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("shape", shape, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("status", status, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("to", to, "single", required=False, decimal=False))
        _query.extend(
            encode_query("topic", topic, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/predictions/events", {}),
            _query,
            None,
            models.decode_PredictionEventsPage,
        )

    def list_events_iter(
        self,
        *,
        cursor: str | None = None,
        from_: str | None = None,
        limit: int | None = None,
        release_id: str | None = None,
        shape: str | None = None,
        status: str | None = None,
        to: str | None = None,
        topic: str | None = None,
    ) -> Iterator[models.PredictionEventSummary]:
        """List Prediction Events

        Stability: stable.

        Args:
            cursor: Optional query parameter.
            from_: Optional query parameter.
            limit: Optional query parameter.
            release_id: Optional query parameter.
            shape: Optional query parameter.
            status: Optional query parameter.
            to: Optional query parameter.
            topic: Optional query parameter.

        Returns:
            Iterator[PredictionEventSummary]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PredictionEventSummary], str | None]:
            result = self.list_events(
                cursor=next_cursor,
                from_=from_,
                limit=limit,
                release_id=release_id,
                shape=shape,
                status=status,
                to=to,
                topic=topic,
            )
            return [item for item in result.events], result.next_cursor

        return iterate(page, cursor)

    def list_topics(self, *, group: str | None = None) -> models.PredictionTopics:
        """List Prediction Topics

        Stability: stable.

        Args:
            group: Optional query parameter.

        Returns:
            PredictionTopics: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("group", group, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/predictions/topics", {}),
            _query,
            None,
            models.decode_PredictionTopics,
        )


class Webhooks:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def configuration_history(
        self, destination_id: str
    ) -> models.WebhookHistoryResponse:
        """Configuration History

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).

        Returns:
            WebhookHistoryResponse: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}/history",
                {"destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_WebhookHistoryResponse,
        )

    def create_destination(
        self,
        *,
        companies: builtins.list[str] | None | Unset = UNSET,
        countries: builtins.list[str],
        enabled: bool | None | Unset = UNSET,
        families: builtins.list[str],
        url: str,
    ) -> models.WebhookDestinationCreated:
        """Create Destination

        Stability: stable.

        Args:
            companies: Optional body parameter. Companies to watch, as `usa:0000320193`. Required with the `filings` family and refused without it: only filings of a listed company (or, for 13D/G, its subject) are sent. Basic 50, Pro 1,000.
            countries: Required body parameter. Countries from the active profile's catalogue.
            enabled: Optional body parameter.
            families: Required body parameter.
            url: Required body parameter.

        Returns:
            WebhookDestinationCreated: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "POST",
            encode_path("/v1/webhooks/destinations", {}),
            _query,
            encode_body(
                {
                    "companies": companies,
                    "countries": countries,
                    "enabled": enabled,
                    "families": families,
                    "url": url,
                }
            ),
            models.decode_WebhookDestinationCreated,
        )

    def delete_destination(self, destination_id: str) -> models.NoContent:
        """Delete Destination

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).

        Returns:
            NoContent: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "DELETE",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}",
                {"destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_NoContent,
        )

    def delivery_history(
        self,
        destination_id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> models.WebhookDeliveriesResponse:
        """Delivery History

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).
            cursor: Optional query parameter.
            limit: Optional query parameter.

        Returns:
            WebhookDeliveriesResponse: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}/deliveries",
                {"destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_WebhookDeliveriesResponse,
        )

    def delivery_history_iter(
        self,
        destination_id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> Iterator[models.WebhookDelivery]:
        """Delivery History

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).
            cursor: Optional query parameter.
            limit: Optional query parameter.

        Returns:
            Iterator[WebhookDelivery]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.WebhookDelivery], str | None]:
            result = self.delivery_history(
                destination_id=destination_id, cursor=next_cursor, limit=limit
            )
            return [item for item in result.deliveries], result.next_cursor

        return iterate(page, cursor)

    def get_destination(self, destination_id: str) -> models.WebhookDestinationResponse:
        """Get Destination

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).

        Returns:
            WebhookDestinationResponse: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}",
                {"destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_WebhookDestinationResponse,
        )

    def list_destinations(self) -> models.WebhookDestinationList:
        """List Destinations

        Stability: stable.

        Returns:
            WebhookDestinationList: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "GET",
            encode_path("/v1/webhooks/destinations", {}),
            _query,
            None,
            models.decode_WebhookDestinationList,
        )

    def replay_delivery(
        self, delivery_id: str, destination_id: str
    ) -> models.NoContent:
        """Replay Delivery

        Stability: stable.

        Args:
            delivery_id: Required path parameter. Delivery ID (UUID).
            destination_id: Required path parameter. Webhook destination ID (UUID).

        Returns:
            NoContent: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "POST",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}/deliveries/{delivery_id}/replay",
                {"delivery_id": delivery_id, "destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_NoContent,
        )

    def rotate_secret(self, destination_id: str) -> models.WebhookDestinationCreated:
        """Rotate Secret

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).

        Returns:
            WebhookDestinationCreated: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "POST",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}/rotate-secret",
                {"destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_WebhookDestinationCreated,
        )

    def test_destination(self, destination_id: str) -> models.WebhookTestResponse:
        """Test Destination

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).

        Returns:
            WebhookTestResponse: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "POST",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}/test",
                {"destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_WebhookTestResponse,
        )

    def update_destination(
        self,
        destination_id: str,
        *,
        companies: builtins.list[str] | None | Unset = UNSET,
        countries: builtins.list[str],
        enabled: bool | None,
        families: builtins.list[str],
        url: str,
    ) -> models.WebhookDestinationResponse:
        """Update Destination

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).
            companies: Optional body parameter. Companies to watch, as `usa:0000320193`. Required with the `filings` family and refused without it: only filings of a listed company (or, for 13D/G, its subject) are sent. Basic 50, Pro 1,000.
            countries: Required body parameter. Countries from the active profile's catalogue.
            enabled: Required body parameter.
            families: Required body parameter.
            url: Required body parameter.

        Returns:
            WebhookDestinationResponse: Decoded response with header metadata.
        """
        _query: Query = []
        return self._transport.request(
            "PATCH",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}",
                {"destination_id": destination_id},
            ),
            _query,
            encode_body(
                {
                    "companies": companies,
                    "countries": countries,
                    "enabled": enabled,
                    "families": families,
                    "url": url,
                }
            ),
            models.decode_WebhookDestinationResponse,
        )


class StableOperations:
    def __init__(self, transport: SyncTransport) -> None:
        self.calendar_subscriptions = CalendarSubscriptions(transport)
        self.calendars = Calendars(transport)
        self.commodities = Commodities(transport)
        self.company_calendars = CompanyCalendars(transport)
        self.crypto = Crypto(transport)
        self.economics = Economics(transport)
        self.equities = Equities(transport)
        self.events = Events(transport)
        self.filings = Filings(transport)
        self.funds = Funds(transport)
        self.fx = Fx(transport)
        self.predictions = Predictions(transport)
        self.webhooks = Webhooks(transport)
        self.unstable = UnstableOperations(transport)


class UnstableOperations:
    def __init__(self, transport: SyncTransport) -> None:
        pass


class AsyncCalendarSubscriptions:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self,
        *,
        countries: builtins.list[str],
        end_date: str,
        families: builtins.list[str] | None | Unset = UNSET,
        include_holidays: bool | None | Unset = UNSET,
        include_releases: bool | None | Unset = UNSET,
        scope: str | None | Unset = UNSET,
        start_date: str,
    ) -> models.CalendarSubscriptionCreated:
        """Create Calendar Subscription

        Stability: stable.

        Args:
            countries: Required body parameter.
            end_date: Required body parameter.
            families: Optional body parameter.
            include_holidays: Optional body parameter.
            include_releases: Optional body parameter.
            scope: Optional body parameter.
            start_date: Required body parameter.

        Returns:
            CalendarSubscriptionCreated: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "POST",
            encode_path("/v1/calendars/subscriptions", {}),
            _query,
            encode_body(
                {
                    "countries": countries,
                    "end_date": end_date,
                    "families": families,
                    "include_holidays": include_holidays,
                    "include_releases": include_releases,
                    "scope": scope,
                    "start_date": start_date,
                }
            ),
            models.decode_CalendarSubscriptionCreated,
        )

    async def revoke(self, subscription_id: str) -> models.NoContent:
        """Revoke Calendar Subscription

        Stability: stable.

        Args:
            subscription_id: Required path parameter. Calendar subscription ID (UUID).

        Returns:
            NoContent: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "DELETE",
            encode_path(
                "/v1/calendars/subscriptions/{subscription_id}",
                {"subscription_id": subscription_id},
            ),
            _query,
            None,
            models.decode_NoContent,
        )

    def feed_url(self, token: str) -> str:
        """Read Calendar Subscription

        Revocable calendar-only token URL returned once on subscription creation.

        Stability: stable.

        Args:
            token: Required path parameter.

        Returns:
            str: Calendar feed URL. No request is made.
        """
        return self._transport.base_url + encode_path(
            "/v1/calendars/subscriptions/{token}.ics", {"token": token}
        )


class AsyncCalendars:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def holidays_on_date(
        self, country: str, date: str, *, scope: str | None = None
    ) -> models.CalendarHolidaysOnDate:
        """Get Calendar Holidays On Date

        Published public holidays on one date. Returns 404 when no calendar is published for the country, year or scope.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            date: Required path parameter. Date, YYYY-MM-DD. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            scope: Optional query parameter. Only holidays and coverage of this scope, for example national_public.

        Returns:
            CalendarHolidaysOnDate: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("scope", scope, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/calendars/holidays/{country}/on/{date}",
                {"country": country, "date": date},
            ),
            _query,
            None,
            models.decode_CalendarHolidaysOnDate,
        )

    async def next_holiday(
        self, country: str, *, from_date: str, scope: str | None = None
    ) -> models.CalendarNextHoliday:
        """Get Calendar Next Holiday

        Next published public holiday on or after a date. Returns 404 when no calendar is published for the country, year or scope.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            from_date: Required query parameter. Date to search from, YYYY-MM-DD. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            scope: Optional query parameter. Only holidays and coverage of this scope, for example national_public.

        Returns:
            CalendarNextHoliday: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("from_date", from_date, "single", required=True, decimal=False)
        )
        _query.extend(
            encode_query("scope", scope, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/calendars/holidays/{country}/next", {"country": country}),
            _query,
            None,
            models.decode_CalendarNextHoliday,
        )

    async def list_holidays(
        self,
        country: str,
        year: int,
        *,
        scope: str | None = None,
        version_id: str | None = None,
    ) -> models.CalendarHolidays:
        """List Calendar Holidays

        Published public holidays for a country and year, with the calendar coverage. An empty `subdivision_codes` list means the holiday applies nationwide. Returns 404 when no calendar is published for the country, year or scope.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            year: Required path parameter. Calendar year. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            scope: Optional query parameter. Only holidays and coverage of this scope, for example national_public.
            version_id: Optional query parameter. Immutable calendar version from a holiday event.

        Returns:
            CalendarHolidays: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("scope", scope, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/calendars/holidays/{country}/{year}",
                {"country": country, "year": year},
            ),
            _query,
            None,
            models.decode_CalendarHolidays,
        )


class AsyncCommodities:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def palmoil_physical_observations(
        self,
        series_id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        price_month: str | None = None,
        start: str | None = None,
    ) -> models.PalmoilHistory:
        """Get Palmoil Observations

        Palm-oil prices of one series by native period. Supply start and end together.

        Stability: stable.

        Args:
            series_id: Required path parameter. Palm-oil series ID.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. First day to exclude from the range. Supply start and end together.
            limit: Optional query parameter. Maximum rows per page.
            price_month: Optional query parameter. Month to read, YYYY-MM. MPOB CPO series only.
            start: Optional query parameter. First date to include. Supply start and end together.

        Returns:
            PalmoilHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "price_month", price_month, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/palmoil/physical/{series_id}/observations",
                {"series_id": series_id},
            ),
            _query,
            None,
            models.decode_PalmoilHistory,
        )

    def palmoil_physical_observations_iter(
        self,
        series_id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        price_month: str | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.PalmoilObservation]:
        """Get Palmoil Observations

        Palm-oil prices of one series by native period. Supply start and end together.

        Stability: stable.

        Args:
            series_id: Required path parameter. Palm-oil series ID.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. First day to exclude from the range. Supply start and end together.
            limit: Optional query parameter. Maximum rows per page.
            price_month: Optional query parameter. Month to read, YYYY-MM. MPOB CPO series only.
            start: Optional query parameter. First date to include. Supply start and end together.

        Returns:
            AsyncIterator[PalmoilObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PalmoilObservation], str | None]:
            result = await self.palmoil_physical_observations(
                series_id=series_id,
                cursor=next_cursor,
                end=end,
                limit=limit,
                price_month=price_month,
                start=start,
            )
            if isinstance(result, models.PalmoilHistoryUnknown):
                return unknown_page(
                    result.raw,
                    "observations",
                    "next_cursor",
                    lambda value: models.decode_PalmoilObservation(
                        value, page=result.raw
                    ),
                    result._raw_body,
                )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def palmoil_physical_price(
        self, series_id: str, *, price_month: str | None = None
    ) -> models.PalmoilPrice:
        """Get Palmoil Physical

        Latest approved palm-oil price of one series: a single CPO price or a full FFB age schedule.

        Stability: stable.

        Args:
            series_id: Required path parameter. Palm-oil series ID.
            price_month: Optional query parameter. Month to read, YYYY-MM. MPOB CPO series only.

        Returns:
            PalmoilPrice: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "price_month", price_month, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/palmoil/physical/{series_id}", {"series_id": series_id}
            ),
            _query,
            None,
            models.decode_PalmoilPrice,
        )

    async def physical_latest(self, series_id: str) -> models.PhysicalLatest:
        """Get Physical Latest

        Latest published price of one physical price series.

        Stability: stable.

        Args:
            series_id: Required path parameter. Series ID. `latest` is not a series ID.

        Returns:
            PhysicalLatest: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/physical/series/{series_id}/latest",
                {"series_id": series_id},
            ),
            _query,
            None,
            models.decode_PhysicalLatest,
        )

    async def physical_observations(
        self,
        series_id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.PhysicalObservations:
        """Get Physical Observations

        Published prices of one physical price series. `start` is inclusive and `end` is exclusive. Supply start and end together.

        Stability: stable.

        Args:
            series_id: Required path parameter. Series ID. `latest` is not a series ID.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. First day to exclude from the range. Supply start and end together.
            limit: Optional query parameter. Maximum rows per page.
            start: Optional query parameter. First day to include. Supply start and end together.

        Returns:
            PhysicalObservations: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/physical/series/{series_id}/observations",
                {"series_id": series_id},
            ),
            _query,
            None,
            models.decode_PhysicalObservations,
        )

    def physical_observations_iter(
        self,
        series_id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.PhysicalObservation]:
        """Get Physical Observations

        Published prices of one physical price series. `start` is inclusive and `end` is exclusive. Supply start and end together.

        Stability: stable.

        Args:
            series_id: Required path parameter. Series ID. `latest` is not a series ID.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. First day to exclude from the range. Supply start and end together.
            limit: Optional query parameter. Maximum rows per page.
            start: Optional query parameter. First day to include. Supply start and end together.

        Returns:
            AsyncIterator[PhysicalObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PhysicalObservation], str | None]:
            result = await self.physical_observations(
                series_id=series_id,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def get_physical_series(self, series_id: str) -> models.PhysicalSeries:
        """Get Physical Series

        Definition of one physical price series: commodity, category, product, country, area, price type, basis, currency, unit, unit_quantity, frequency, description, attribution, coverage_start and coverage_end.

        Stability: stable.

        Args:
            series_id: Required path parameter. Series ID. `latest` is not a series ID.

        Returns:
            PhysicalSeries: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/physical/series/{series_id}", {"series_id": series_id}
            ),
            _query,
            None,
            models.decode_PhysicalSeries,
        )

    async def price_history(
        self,
        commodity: str,
        currency: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        limit: int | None = None,
        start: str,
    ) -> models.CommodityBars:
        """Get Commodity Price History

        Closed price bars for one commodity and quote currency, from one minute to one day. A request may span at most 3 days of 1m bars, 14 days of 5m bars, 60 days of 15m bars; a longer range returns 400. Wider intervals have no cap.

        Stability: stable.

        Args:
            commodity: Required path parameter.
            currency: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            limit: Optional query parameter.
            start: Required query parameter.

        Returns:
            CommodityBars: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/spot/{commodity}/{currency}/bars",
                {"commodity": commodity, "currency": currency},
            ),
            _query,
            None,
            models.decode_CommodityBars,
        )

    def price_history_iter(
        self,
        commodity: str,
        currency: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        limit: int | None = None,
        start: str,
    ) -> AsyncIterator[models.CommodityBar]:
        """Get Commodity Price History

        Closed price bars for one commodity and quote currency, from one minute to one day. A request may span at most 3 days of 1m bars, 14 days of 5m bars, 60 days of 15m bars; a longer range returns 400. Wider intervals have no cap.

        Stability: stable.

        Args:
            commodity: Required path parameter.
            currency: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            limit: Optional query parameter.
            start: Required query parameter.

        Returns:
            AsyncIterator[CommodityBar]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.CommodityBar], str | None]:
            result = await self.price_history(
                commodity=commodity,
                currency=currency,
                cursor=next_cursor,
                end=end,
                interval=interval,
                limit=limit,
                start=start,
            )
            return [item for item in result.bars], result.next_cursor

        return iterate_async(page, cursor)

    async def spot_price(self, commodity: str, currency: str) -> models.CommoditySpot:
        """Get Commodity Spot

        Stability: stable.

        Args:
            commodity: Required path parameter.
            currency: Required path parameter.

        Returns:
            CommoditySpot: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/commodities/spot/{commodity}/{currency}",
                {"commodity": commodity, "currency": currency},
            ),
            _query,
            None,
            models.decode_CommoditySpot,
        )

    async def list_palmoil_physical_series(
        self,
        *,
        area: str | None = None,
        country: str | None = None,
        currency: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        price_type: str | None = None,
        producer_arrangement: str | None = None,
        producer_type: str | None = None,
        product: str | None = None,
    ) -> models.PalmoilSeriesDiscovery:
        """List Palmoil Physical

        List approved palm-oil price series. Filters combine. A filter that matches nothing returns an empty list.

        Stability: stable.

        Args:
            area: Optional query parameter. Area code inside the country.
            country: Optional query parameter. ISO 3166-1 alpha-3 country code.
            currency: Optional query parameter. Quote currency, ISO 4217 code.
            cursor: Optional query parameter. The next_cursor from the previous page.
            limit: Optional query parameter. Maximum rows per page.
            price_type: Optional query parameter. Price definition.
            producer_arrangement: Optional query parameter. Producer arrangement: purchase_agreement or supported_scheme.
            producer_type: Optional query parameter. Producer type; only smallholder is supported.
            product: Optional query parameter. ffb (fresh fruit bunches) or cpo (crude palm oil).

        Returns:
            PalmoilSeriesDiscovery: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("area", area, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("currency", currency, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "price_type", price_type, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query(
                "producer_arrangement",
                producer_arrangement,
                "single",
                required=False,
                decimal=False,
            )
        )
        _query.extend(
            encode_query(
                "producer_type", producer_type, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("product", product, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/commodities/palmoil/physical", {}),
            _query,
            None,
            models.decode_PalmoilSeriesDiscovery,
        )

    def list_palmoil_physical_series_iter(
        self,
        *,
        area: str | None = None,
        country: str | None = None,
        currency: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        price_type: str | None = None,
        producer_arrangement: str | None = None,
        producer_type: str | None = None,
        product: str | None = None,
    ) -> AsyncIterator[models.PalmoilSeries]:
        """List Palmoil Physical

        List approved palm-oil price series. Filters combine. A filter that matches nothing returns an empty list.

        Stability: stable.

        Args:
            area: Optional query parameter. Area code inside the country.
            country: Optional query parameter. ISO 3166-1 alpha-3 country code.
            currency: Optional query parameter. Quote currency, ISO 4217 code.
            cursor: Optional query parameter. The next_cursor from the previous page.
            limit: Optional query parameter. Maximum rows per page.
            price_type: Optional query parameter. Price definition.
            producer_arrangement: Optional query parameter. Producer arrangement: purchase_agreement or supported_scheme.
            producer_type: Optional query parameter. Producer type; only smallholder is supported.
            product: Optional query parameter. ffb (fresh fruit bunches) or cpo (crude palm oil).

        Returns:
            AsyncIterator[PalmoilSeries]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PalmoilSeries], str | None]:
            result = await self.list_palmoil_physical_series(
                area=area,
                country=country,
                currency=currency,
                cursor=next_cursor,
                limit=limit,
                price_type=price_type,
                producer_arrangement=producer_arrangement,
                producer_type=producer_type,
                product=product,
            )
            return [item for item in result.series], result.next_cursor

        return iterate_async(page, cursor)

    async def list_physical_series(
        self,
        *,
        category: str | None = None,
        commodity: str | None = None,
        country: str | None = None,
        currency: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        price_type: str | None = None,
    ) -> models.PhysicalSeriesPage:
        """List Physical Series

        List published physical and official reference price series. Filters combine. A filter that matches nothing returns an empty list.

        Stability: stable.

        Args:
            category: Optional query parameter. Commodity category.
            commodity: Optional query parameter. Commodity slug, for example wheat.
            country: Optional query parameter. Market: ISO 3166-1 alpha-3 code, WLD (world) or EUU (European Union).
            currency: Optional query parameter. Quote currency, ISO 4217 code.
            cursor: Optional query parameter. The next_cursor from the previous page.
            limit: Optional query parameter. Maximum rows per page.
            price_type: Optional query parameter. Price type, for example retail_average.

        Returns:
            PhysicalSeriesPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("category", category, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "commodity", commodity, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("currency", currency, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "price_type", price_type, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/commodities/physical/series", {}),
            _query,
            None,
            models.decode_PhysicalSeriesPage,
        )

    def list_physical_series_iter(
        self,
        *,
        category: str | None = None,
        commodity: str | None = None,
        country: str | None = None,
        currency: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        price_type: str | None = None,
    ) -> AsyncIterator[models.PhysicalSeries]:
        """List Physical Series

        List published physical and official reference price series. Filters combine. A filter that matches nothing returns an empty list.

        Stability: stable.

        Args:
            category: Optional query parameter. Commodity category.
            commodity: Optional query parameter. Commodity slug, for example wheat.
            country: Optional query parameter. Market: ISO 3166-1 alpha-3 code, WLD (world) or EUU (European Union).
            currency: Optional query parameter. Quote currency, ISO 4217 code.
            cursor: Optional query parameter. The next_cursor from the previous page.
            limit: Optional query parameter. Maximum rows per page.
            price_type: Optional query parameter. Price type, for example retail_average.

        Returns:
            AsyncIterator[PhysicalSeries]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PhysicalSeries], str | None]:
            result = await self.list_physical_series(
                category=category,
                commodity=commodity,
                country=country,
                currency=currency,
                cursor=next_cursor,
                limit=limit,
                price_type=price_type,
            )
            return [item for item in result.series], result.next_cursor

        return iterate_async(page, cursor)


class AsyncCompanyCalendars:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def dividends(
        self,
        *,
        country: str | None = None,
        end: str | None = None,
        start: str | None = None,
    ) -> models.DividendsCalendar:
        """Company dividends calendar

        Dividends going ex in the window: the ex-date, the amount per share and its currency. `start` and `end` are inclusive days (YYYY-MM-DD); left out, `start` is today (UTC) and `end` is `start`. Dates run from 30 days back to 90 days ahead (400 invalid_query outside), and a request spans at most 7 days (400 range_too_large). `country` is USA, the only country for now (404 not_covered). Only companies in our symbol list appear, with our id and name; units and share classes of one issuer are one row. Open to every plan and one call a request.

        Stability: stable.

        Args:
            country: Optional query parameter. Three-letter country code of the listing. Left out means USA, the only country for now (another one is 404 not_covered).
            end: Optional query parameter. Last day, inclusive. Left out means `start`. At most 7 days from `start` (400 range_too_large).
            start: Optional query parameter. First day (YYYY-MM-DD), inclusive. Left out means today (UTC). Between 30 days back and 90 days ahead.

        Returns:
            DividendsCalendar: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/calendars/dividends", {}),
            _query,
            None,
            models.decode_DividendsCalendar,
        )

    async def splits(
        self,
        *,
        country: str | None = None,
        end: str | None = None,
        start: str | None = None,
    ) -> models.SplitsCalendar:
        """Company splits calendar

        Stock splits taking effect in the window, with the ratio as new shares for old (4:1 gives four for one; 1:10 is a reverse split). `start` and `end` are inclusive days (YYYY-MM-DD); left out, `start` is today (UTC) and `end` is `start`. Dates run from 30 days back to 90 days ahead (400 invalid_query outside), and a request spans at most 7 days (400 range_too_large). `country` is USA, the only country for now (404 not_covered). Only companies in our symbol list appear, with our id and name; units and share classes of one issuer are one row. Open to every plan and one call a request.

        Stability: stable.

        Args:
            country: Optional query parameter. Three-letter country code of the listing. Left out means USA, the only country for now (another one is 404 not_covered).
            end: Optional query parameter. Last day, inclusive. Left out means `start`. At most 7 days from `start` (400 range_too_large).
            start: Optional query parameter. First day (YYYY-MM-DD), inclusive. Left out means today (UTC). Between 30 days back and 90 days ahead.

        Returns:
            SplitsCalendar: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/calendars/splits", {}),
            _query,
            None,
            models.decode_SplitsCalendar,
        )


class AsyncCrypto:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def bars(
        self,
        pair: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        interval: str | None = None,
        start: str | None = None,
    ) -> models.CryptoBars:
        """Price bars of one crypto pair

        Daily (`1d`, one UTC day, closing at 00:00 UTC) or one-minute (`1m`) bars, oldest first. A day's bar is out at 00:00 UTC (Free: 15 minutes later, and `end` comes back when that cut the range); today's partial bar is never shown. One-minute bars are for Basic and Pro (Free gets 403 plan_upgrade_required). History: Free 12 months, Basic 5 years, Pro everything; `start` is sent back when the plan raised it. Up to 5,000 bars a page, with `next_cursor`; a cursor that no longer matches the prices is 409 cursor_expired. One call a page.

        Stability: stable.

        Args:
            pair: Required path parameter. Crypto pair: the coin, a dash and the quote currency, for example BTC-USD or ETH-EUR. Any case; a slash in place of the dash is accepted. The answer carries the canonical pair.
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same parameters.
            end: Optional query parameter. Last bar. `1d`: a date, inclusive; left out means the latest finished day. `1m`: a UTC time, exclusive; left out means now, or five days after `start`. At most 5 days between `start` and `end` for `1m` (400 range_too_large).
            interval: Optional query parameter. `1d` (one bar per UTC day, closing at 00:00 UTC) or `1m` (one-minute bars, Basic and Pro only). Anything else is 400 invalid_interval.
            start: Optional query parameter. First bar. `1d`: a date (YYYY-MM-DD), inclusive; left out means the oldest bar your plan reaches. `1m`: a UTC time (YYYY-MM-DDTHH:MM:SSZ, or a date for 00:00 UTC), inclusive; left out means one day before `end`.

        Returns:
            CryptoBars: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/crypto/{pair}/bars", {"pair": pair}),
            _query,
            None,
            models.decode_CryptoBars,
        )

    def bars_iter(
        self,
        pair: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        interval: str | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.CryptoBar]:
        """Price bars of one crypto pair

        Daily (`1d`, one UTC day, closing at 00:00 UTC) or one-minute (`1m`) bars, oldest first. A day's bar is out at 00:00 UTC (Free: 15 minutes later, and `end` comes back when that cut the range); today's partial bar is never shown. One-minute bars are for Basic and Pro (Free gets 403 plan_upgrade_required). History: Free 12 months, Basic 5 years, Pro everything; `start` is sent back when the plan raised it. Up to 5,000 bars a page, with `next_cursor`; a cursor that no longer matches the prices is 409 cursor_expired. One call a page.

        Stability: stable.

        Args:
            pair: Required path parameter. Crypto pair: the coin, a dash and the quote currency, for example BTC-USD or ETH-EUR. Any case; a slash in place of the dash is accepted. The answer carries the canonical pair.
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same parameters.
            end: Optional query parameter. Last bar. `1d`: a date, inclusive; left out means the latest finished day. `1m`: a UTC time, exclusive; left out means now, or five days after `start`. At most 5 days between `start` and `end` for `1m` (400 range_too_large).
            interval: Optional query parameter. `1d` (one bar per UTC day, closing at 00:00 UTC) or `1m` (one-minute bars, Basic and Pro only). Anything else is 400 invalid_interval.
            start: Optional query parameter. First bar. `1d`: a date (YYYY-MM-DD), inclusive; left out means the oldest bar your plan reaches. `1m`: a UTC time (YYYY-MM-DDTHH:MM:SSZ, or a date for 00:00 UTC), inclusive; left out means one day before `end`.

        Returns:
            AsyncIterator[CryptoBar]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.CryptoBar], str | None]:
            result = await self.bars(
                pair=pair, cursor=next_cursor, end=end, interval=interval, start=start
            )
            return [item for item in result.bars], result.next_cursor

        return iterate_async(page, cursor)

    async def price(self, pair: str) -> models.CryptoPrice:
        """Latest price of one crypto pair

        The latest composite price of a pair, with the 24-hour change (left out on Free and when it is not known). Crypto trades all day, so there is no market session; `stale` is true when the price is more than 5 minutes old. Free sees the price 15 minutes late and the answer carries `delayed: true`. `change_24h_percent` is in percent.

        Stability: stable.

        Args:
            pair: Required path parameter. Crypto pair: the coin, a dash and the quote currency, for example BTC-USD or ETH-EUR. Any case; a slash in place of the dash is accepted. The answer carries the canonical pair.

        Returns:
            CryptoPrice: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path("/v1/crypto/{pair}/price", {"pair": pair}),
            _query,
            None,
            models.decode_CryptoPrice,
        )

    async def prices(self, *, pairs: str) -> models.CryptoPrices:
        """Latest prices for up to 50 crypto pairs

        Latest price of each listed pair (Free sees them 15 minutes late). One call is counted for each pair that returns a price, taken in one step: if fewer calls are left than pairs that resolved, the whole request is refused with 429 quota_exceeded. Pairs that return no price are listed in `errors` (as `id`) and cost nothing. `change_24h_percent` is in percent.

        Stability: stable.

        Args:
            pairs: Required query parameter. Comma-separated pairs, at most 50 after duplicates are removed. Each pair follows the same rules as the single-price route. One call is counted for each pair that returns a price.

        Returns:
            CryptoPrices: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("pairs", pairs, "single", required=True, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/crypto/prices", {}),
            _query,
            None,
            models.decode_CryptoPrices,
        )

    async def list_pairs(self, *, quote: str | None = None) -> models.CryptoPairs:
        """Crypto pairs we price

        Every pair we price, by pair (`BTC-USD` style). Optional `quote` (USD, EUR or GBP). A pair is listed while it trades at least once every 30 seconds and dropped when it falls below once every 2 minutes. Read from our own pair list, so it is open to every plan and counts one call.

        Stability: stable.

        Args:
            quote: Optional query parameter. Only pairs quoted in this currency (USD, EUR or GBP).

        Returns:
            CryptoPairs: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("quote", quote, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/crypto/pairs", {}),
            _query,
            None,
            models.decode_CryptoPairs,
        )


class AsyncEconomics:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def central_bank_balance_sheet(
        self, country: str, *, period: str | None = None
    ) -> models.CentralBankBalanceSheet:
        """Get Central Bank Balance Sheet

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.

        Returns:
            CentralBankBalanceSheet: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/central-bank/balance-sheet",
                {"country": country},
            ),
            _query,
            None,
            models.decode_CentralBankBalanceSheet,
        )

    async def central_bank_reserves(
        self, country: str, *, period: str | None = None
    ) -> models.CentralBankReserves:
        """Get Central Bank Reserves

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.

        Returns:
            CentralBankReserves: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/central-bank/reserves", {"country": country}
            ),
            _query,
            None,
            models.decode_CentralBankReserves,
        )

    async def cpi(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Cpi:
        """Get Cpi

        Latest headline consumer price index for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY-MM. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            Cpi: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/cpi", {"country": country}),
            _query,
            None,
            models.decode_Cpi,
        )

    async def cpi_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.CpiHistory:
        """Get Cpi History

        The headline consumer price index by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            CpiHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/cpi/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_CpiHistory,
        )

    def cpi_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> AsyncIterator[models.CpiHistoryObservation]:
        """Get Cpi History

        The headline consumer price index by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            AsyncIterator[CpiHistoryObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.CpiHistoryObservation], str | None]:
            result = await self.cpi_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def get_equity_risk_premium(
        self, country: str, *, date: str | None = None
    ) -> models.EquityRiskPremium:
        """Get Equity Risk Premium

        Stability: stable.

        Args:
            country: Required path parameter.
            date: Optional query parameter.

        Returns:
            EquityRiskPremium: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("date", date, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/equity-risk-premium", {"country": country}
            ),
            _query,
            None,
            models.decode_EquityRiskPremium,
        )

    async def equity_risk_premium_history(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.EquityRiskPremiumHistoryResponse:
        """Get Equity Risk Premium History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            EquityRiskPremiumHistoryResponse: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/equity-risk-premium/history",
                {"country": country},
            ),
            _query,
            None,
            models.decode_EquityRiskPremiumHistoryResponse,
        )

    def equity_risk_premium_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.EquityRiskPremium]:
        """Get Equity Risk Premium History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            AsyncIterator[EquityRiskPremium]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EquityRiskPremium], str | None]:
            result = await self.equity_risk_premium_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def gdp(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Gdp:
        """Get Gdp

        Latest GDP at current prices for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY-QN. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            Gdp: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/gdp", {"country": country}),
            _query,
            None,
            models.decode_Gdp,
        )

    async def gdp_growth(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.GdpGrowth:
        """Get Gdp Growth

        Latest real GDP growth for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY-QN. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            GdpGrowth: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/gdp-growth", {"country": country}),
            _query,
            None,
            models.decode_GdpGrowth,
        )

    async def gdp_growth_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.GdpGrowthHistory:
        """Get Gdp Growth History

        The real GDP growth by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            GdpGrowthHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/gdp-growth/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_GdpGrowthHistory,
        )

    def gdp_growth_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> AsyncIterator[models.GdpGrowthHistoryObservation]:
        """Get Gdp Growth History

        The real GDP growth by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            AsyncIterator[GdpGrowthHistoryObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.GdpGrowthHistoryObservation], str | None]:
            result = await self.gdp_growth_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def gdp_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.GdpHistory:
        """Get Gdp History

        The GDP at current prices by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            GdpHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/gdp/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_GdpHistory,
        )

    def gdp_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> AsyncIterator[models.GdpHistoryObservation]:
        """Get Gdp History

        The GDP at current prices by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            AsyncIterator[GdpHistoryObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.GdpHistoryObservation], str | None]:
            result = await self.gdp_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def inflation(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Inflation:
        """Get Inflation

        Latest headline inflation for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY-MM. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            Inflation: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/inflation", {"country": country}),
            _query,
            None,
            models.decode_Inflation,
        )

    async def inflation_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.InflationHistory:
        """Get Inflation History

        The headline inflation by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            InflationHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/inflation/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_InflationHistory,
        )

    def inflation_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> AsyncIterator[models.InflationHistoryObservation]:
        """Get Inflation History

        The headline inflation by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            AsyncIterator[InflationHistoryObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.InflationHistoryObservation], str | None]:
            result = await self.inflation_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def labour_force_participation(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.LabourForceParticipation:
        """Get Labour Force Participation

        Latest labour-force participation rate for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY, YYYY-MM or YYYY-QN. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            LabourForceParticipation: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/labour-force-participation",
                {"country": country},
            ),
            _query,
            None,
            models.decode_LabourForceParticipation,
        )

    async def labour_force_participation_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.RateHistory:
        """Get Labour Force Participation History

        The labour-force participation rate by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            RateHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/labour-force-participation/observations",
                {"country": country},
            ),
            _query,
            None,
            models.decode_RateHistory,
        )

    def labour_force_participation_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> AsyncIterator[models.RateHistoryObservation]:
        """Get Labour Force Participation History

        The labour-force participation rate by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            AsyncIterator[RateHistoryObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.RateHistoryObservation], str | None]:
            result = await self.labour_force_participation_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def policy_rate(
        self, country: str, *, date: str | None = None
    ) -> models.PolicyRate:
        """Get Policy Rate

        Stability: stable.

        Args:
            country: Required path parameter.
            date: Optional query parameter.

        Returns:
            PolicyRate: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("date", date, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/central-bank/policy-rate", {"country": country}
            ),
            _query,
            None,
            models.decode_PolicyRate,
        )

    async def policy_rate_history(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.PolicyRateHistoryResponse:
        """Get Policy Rate History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            PolicyRateHistoryResponse: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/central-bank/policy-rate/history",
                {"country": country},
            ),
            _query,
            None,
            models.decode_PolicyRateHistoryResponse,
        )

    def policy_rate_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.PolicyRateObservation]:
        """Get Policy Rate History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            AsyncIterator[PolicyRateObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PolicyRateObservation], str | None]:
            result = await self.policy_rate_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def get_release(
        self, release_id: str, *, version_id: str | None = None
    ) -> models.EconomicReleaseDetail:
        """Get Economic Release

        One release calendar entry by release ID.

        Stability: stable.

        Args:
            release_id: Required path parameter. Release ID (UUID).
            version_id: Optional query parameter. Immutable release version to read. Omit it for the current one.

        Returns:
            EconomicReleaseDetail: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/calendar/{release_id}", {"release_id": release_id}
            ),
            _query,
            None,
            models.decode_EconomicReleaseDetail,
        )

    async def trade(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.TradeSummary:
        """Get Trade

        Latest merchandise trade for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY or YYYY-MM. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            TradeSummary: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/trade", {"country": country}),
            _query,
            None,
            models.decode_TradeSummary,
        )

    async def trade_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.TradeHistory:
        """Get Trade History

        The merchandise trade by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            TradeHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/trade/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_TradeHistory,
        )

    def trade_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> AsyncIterator[models.TradeHistoryObservation]:
        """Get Trade History

        The merchandise trade by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            AsyncIterator[TradeHistoryObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.TradeHistoryObservation], str | None]:
            result = await self.trade_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def unemployment(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Unemployment:
        """Get Unemployment

        Latest unemployment rate for a country, or one period with `period`.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            period: Optional query parameter. Period to read: YYYY, YYYY-MM or YYYY-QN. Omit it for the latest period. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current version.

        Returns:
            Unemployment: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/unemployment", {"country": country}),
            _query,
            None,
            models.decode_Unemployment,
        )

    async def unemployment_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.RateHistory:
        """Get Unemployment History

        The unemployment rate by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            RateHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/unemployment/observations",
                {"country": country},
            ),
            _query,
            None,
            models.decode_RateHistory,
        )

    def unemployment_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> AsyncIterator[models.RateHistoryObservation]:
        """Get Unemployment History

        The unemployment rate by period, oldest first.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last period to include: YYYY, YYYY-MM or YYYY-QN.
            limit: Optional query parameter. Maximum periods per page.
            start: Optional query parameter. First period to include: YYYY, YYYY-MM or YYYY-QN.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            AsyncIterator[RateHistoryObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.RateHistoryObservation], str | None]:
            result = await self.unemployment_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def yield_curve(
        self,
        country: str,
        *,
        date: str | None = None,
        maturity: builtins.list[str] | None = None,
        version_id: str | None = None,
    ) -> models.YieldCurve:
        """Get Yield Curve

        Government bond yield curve for one source date, in percent. `curve_type` shows how the country's source defines the curve. Omit `date` for the latest curve.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            date: Optional query parameter. Source date, YYYY-MM-DD. Omit it for the latest curve. Plan history window - Free: the last 12 months. Basic: the last 5 years. Pro: full history.
            maturity: Optional query parameter. Comma-separated maturities to return, for example 2y,10y. Omit for all.
            version_id: Optional query parameter. Immutable publication version to read. Omit it for the current one.

        Returns:
            YieldCurve: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("date", date, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "maturity", maturity, "comma_join", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/yield-curve", {"country": country}),
            _query,
            None,
            models.decode_YieldCurve,
        )

    async def yield_curve_history(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        maturity: builtins.list[str] | None = None,
        start: str | None = None,
    ) -> models.YieldCurveHistoryResponse:
        """Get Yield Curve History

        Government bond yield curves by source date, oldest first, in percent.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The curves as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last source date to include, YYYY-MM-DD.
            limit: Optional query parameter. Maximum rows per page.
            maturity: Optional query parameter. Comma-separated maturities to return, for example 2y,10y. Omit for all.
            start: Optional query parameter. First source date to include, YYYY-MM-DD.

        Returns:
            YieldCurveHistoryResponse: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "maturity", maturity, "comma_join", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/{country}/yield-curve/history", {"country": country}
            ),
            _query,
            None,
            models.decode_YieldCurveHistoryResponse,
        )

    def yield_curve_history_iter(
        self,
        country: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        maturity: builtins.list[str] | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.YieldCurveHistoryObservation]:
        """Get Yield Curve History

        Government bond yield curves by source date, oldest first, in percent.

        Stability: stable.

        Args:
            country: Required path parameter. Uppercase three-letter country code, for example USA.
            as_of: Optional query parameter. The curves as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last source date to include, YYYY-MM-DD.
            limit: Optional query parameter. Maximum rows per page.
            maturity: Optional query parameter. Comma-separated maturities to return, for example 2y,10y. Omit for all.
            start: Optional query parameter. First source date to include, YYYY-MM-DD.

        Returns:
            AsyncIterator[YieldCurveHistoryObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.YieldCurveHistoryObservation], str | None]:
            result = await self.yield_curve_history(
                country=country,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                maturity=maturity,
                start=start,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def list_equity_risk_premium(self) -> models.EquityRiskPremiumList:
        """List Equity Risk Premium

        Stability: stable.

        Returns:
            EquityRiskPremiumList: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/equity-risk-premium", {}),
            _query,
            None,
            models.decode_EquityRiskPremiumList,
        )

    async def list_releases(
        self,
        *,
        countries: builtins.list[str] | None = None,
        cursor: str | None = None,
        end_date: str | None = None,
        limit: int | None = None,
        start_date: str | None = None,
    ) -> models.EconomicCalendar:
        """List Economic Releases

        Release calendar entries for the chosen countries within a date window.

        Stability: stable.

        Args:
            countries: Optional query parameter. Uppercase three-letter country codes (EMU for the euro area). Omit for all.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end_date: Optional query parameter. Last date of the window.
            limit: Optional query parameter. Maximum rows per page.
            start_date: Optional query parameter. First date of the window.

        Returns:
            EconomicCalendar: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "countries", countries, "repeat", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("end_date", end_date, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "start_date", start_date, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/calendar", {}),
            _query,
            None,
            models.decode_EconomicCalendar,
        )

    def list_releases_iter(
        self,
        *,
        countries: builtins.list[str] | None = None,
        cursor: str | None = None,
        end_date: str | None = None,
        limit: int | None = None,
        start_date: str | None = None,
    ) -> AsyncIterator[models.EconomicReleaseSummary]:
        """List Economic Releases

        Release calendar entries for the chosen countries within a date window.

        Stability: stable.

        Args:
            countries: Optional query parameter. Uppercase three-letter country codes (EMU for the euro area). Omit for all.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end_date: Optional query parameter. Last date of the window.
            limit: Optional query parameter. Maximum rows per page.
            start_date: Optional query parameter. First date of the window.

        Returns:
            AsyncIterator[EconomicReleaseSummary]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EconomicReleaseSummary], str | None]:
            result = await self.list_releases(
                countries=countries,
                cursor=next_cursor,
                end_date=end_date,
                limit=limit,
                start_date=start_date,
            )
            return [item for item in result.releases], result.next_cursor

        return iterate_async(page, cursor)

    async def read_catalogue_latest_batch(
        self, *, ids: str
    ) -> models.CatalogueBulkLatest:
        """Read Catalogue Latest Batch

        Stability: stable.

        Args:
            ids: Required query parameter.

        Returns:
            CatalogueBulkLatest: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("ids", ids, "single", required=True, decimal=False))
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/catalogue/latest", {}),
            _query,
            None,
            models.decode_CatalogueBulkLatest,
        )

    async def read_catalogue_observations(
        self,
        *,
        cursor: str | None = None,
        end: str | None = None,
        id: str,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.CatalogueHistory:
        """Read Catalogue History

        Stability: stable.

        Args:
            cursor: Optional query parameter.
            end: Optional query parameter.
            id: Required query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            CatalogueHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(encode_query("id", id, "single", required=True, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/catalogue/series/observations", {}),
            _query,
            None,
            models.decode_CatalogueHistory,
        )

    def read_catalogue_observations_iter(
        self,
        *,
        cursor: str | None = None,
        end: str | None = None,
        id: str,
        limit: int | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.ResourceObservation]:
        """Read Catalogue History

        Stability: stable.

        Args:
            cursor: Optional query parameter.
            end: Optional query parameter.
            id: Required query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            AsyncIterator[ResourceObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.ResourceObservation], str | None]:
            result = await self.read_catalogue_observations(
                cursor=next_cursor, end=end, id=id, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def read_catalogue_series(self, *, id: str) -> models.CatalogueSeries:
        """Read Catalogue Series

        Stability: stable.

        Args:
            id: Required query parameter.

        Returns:
            CatalogueSeries: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("id", id, "single", required=True, decimal=False))
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/catalogue/series", {}),
            _query,
            None,
            models.decode_CatalogueSeries,
        )

    async def read_series_observations(
        self,
        series_id: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> models.ResourceHistory:
        """Read Resource History

        Observations of one economic series, oldest first.

        Stability: stable.

        Args:
            series_id: Required path parameter. Series ID (UUID).
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last observation period to include.
            limit: Optional query parameter. Maximum rows per page.
            start: Optional query parameter. First observation period to include.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            ResourceHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/economics/series/{series_id}/observations",
                {"series_id": series_id},
            ),
            _query,
            None,
            models.decode_ResourceHistory,
        )

    def read_series_observations_iter(
        self,
        series_id: str,
        *,
        as_of: str | None = None,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        version: str | None = None,
    ) -> AsyncIterator[models.ResourceObservation]:
        """Read Resource History

        Observations of one economic series, oldest first.

        Stability: stable.

        Args:
            series_id: Required path parameter. Series ID (UUID).
            as_of: Optional query parameter. The series as published up to the end of this UTC day. Pro plan only.
            cursor: Optional query parameter. The next_cursor from the previous page.
            end: Optional query parameter. Last observation period to include.
            limit: Optional query parameter. Maximum rows per page.
            start: Optional query parameter. First observation period to include.
            version: Optional query parameter. first_reported: the first value stored per period. Pro plan only.

        Returns:
            AsyncIterator[ResourceObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.ResourceObservation], str | None]:
            result = await self.read_series_observations(
                series_id=series_id,
                as_of=as_of,
                cursor=next_cursor,
                end=end,
                limit=limit,
                start=start,
                version=version,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def search_catalogue(
        self,
        *,
        country: str | None = None,
        cursor: str | None = None,
        frequency: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        source: str | None = None,
    ) -> models.CatalogueSearchPage:
        """Search Series Catalogue

        Stability: stable.

        Args:
            country: Optional query parameter.
            cursor: Optional query parameter.
            frequency: Optional query parameter.
            limit: Optional query parameter.
            q: Optional query parameter.
            source: Optional query parameter.

        Returns:
            CatalogueSearchPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "frequency", frequency, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("q", q, "single", required=False, decimal=False))
        _query.extend(
            encode_query("source", source, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/catalogue", {}),
            _query,
            None,
            models.decode_CatalogueSearchPage,
        )

    def search_catalogue_iter(
        self,
        *,
        country: str | None = None,
        cursor: str | None = None,
        frequency: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        source: str | None = None,
    ) -> AsyncIterator[models.CatalogueEntry]:
        """Search Series Catalogue

        Stability: stable.

        Args:
            country: Optional query parameter.
            cursor: Optional query parameter.
            frequency: Optional query parameter.
            limit: Optional query parameter.
            q: Optional query parameter.
            source: Optional query parameter.

        Returns:
            AsyncIterator[CatalogueEntry]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.CatalogueEntry], str | None]:
            result = await self.search_catalogue(
                country=country,
                cursor=next_cursor,
                frequency=frequency,
                limit=limit,
                q=q,
                source=source,
            )
            return [item for item in result.results], result.next_cursor

        return iterate_async(page, cursor)


class AsyncEquities:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def bars(
        self,
        id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        interval: str | None = None,
        start: str | None = None,
    ) -> models.EquityBars:
        """Price bars of one stock

        Daily (`1d`) or one-minute (`1m`) bars, oldest first, adjusted for splits and dividends. History: Free 12 months, Basic 5 years, Pro everything; `start` is sent back when the plan raised it. One-minute bars are for Basic and Pro (Free gets 403 plan_upgrade_required), reach back to 2020 and cover at most 5 days a call (400 range_too_large). Today's daily bar appears after the exchange closes, and for Free 15 minutes after; `end` is sent back when that cut the range. Up to 5,000 bars a page, with `next_cursor`; a cursor that no longer matches the prices is 409 cursor_expired. One call a page.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters. A cursor stops working when the prices behind it changed (a split or dividend): 409 cursor_expired.
            end: Optional query parameter. Last bar. `1d`: a date, inclusive; left out means the latest session whose bar is out. `1m`: a UTC time, exclusive; left out means now, or five days after `start`. At most 5 days between `start` and `end` for `1m` (400 range_too_large).
            interval: Optional query parameter. `1d` (one bar per session) or `1m` (one-minute bars, Basic and Pro only). Anything else is 400 invalid_interval.
            start: Optional query parameter. First bar. `1d`: a date (YYYY-MM-DD), inclusive; left out means the oldest bar your plan reaches. `1m`: a UTC time (YYYY-MM-DDTHH:MM:SSZ, or a date for 00:00 UTC), inclusive; left out means one day before `end`.

        Returns:
            EquityBars: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/bars", {"id": id}),
            _query,
            None,
            models.decode_EquityBars,
        )

    def bars_iter(
        self,
        id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        interval: str | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.EquityBar]:
        """Price bars of one stock

        Daily (`1d`) or one-minute (`1m`) bars, oldest first, adjusted for splits and dividends. History: Free 12 months, Basic 5 years, Pro everything; `start` is sent back when the plan raised it. One-minute bars are for Basic and Pro (Free gets 403 plan_upgrade_required), reach back to 2020 and cover at most 5 days a call (400 range_too_large). Today's daily bar appears after the exchange closes, and for Free 15 minutes after; `end` is sent back when that cut the range. Up to 5,000 bars a page, with `next_cursor`; a cursor that no longer matches the prices is 409 cursor_expired. One call a page.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters. A cursor stops working when the prices behind it changed (a split or dividend): 409 cursor_expired.
            end: Optional query parameter. Last bar. `1d`: a date, inclusive; left out means the latest session whose bar is out. `1m`: a UTC time, exclusive; left out means now, or five days after `start`. At most 5 days between `start` and `end` for `1m` (400 range_too_large).
            interval: Optional query parameter. `1d` (one bar per session) or `1m` (one-minute bars, Basic and Pro only). Anything else is 400 invalid_interval.
            start: Optional query parameter. First bar. `1d`: a date (YYYY-MM-DD), inclusive; left out means the oldest bar your plan reaches. `1m`: a UTC time (YYYY-MM-DDTHH:MM:SSZ, or a date for 00:00 UTC), inclusive; left out means one day before `end`.

        Returns:
            AsyncIterator[EquityBar]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EquityBar], str | None]:
            result = await self.bars(
                id=id, cursor=next_cursor, end=end, interval=interval, start=start
            )
            return [item for item in result.bars], result.next_cursor

        return iterate_async(page, cursor)

    async def cost_of_capital(
        self,
        id: str,
        *,
        benchmark: str | None = None,
        beta: str | None = None,
        erp: str | None = None,
        frequency: str | None = None,
        period: str | None = None,
        risk_free: str | None = None,
        tax_rate: str | None = None,
        window: str | None = None,
    ) -> models.EquityCostOfCapital:
        """Beta, cost of equity, cost of debt and WACC of one stock

        Beta of one US or Korean stock against a benchmark ETF (weekly returns over two years by default, from prices adjusted for splits and dividends), the risk-free rate (the 10-year point of the country's government yield curve, or yours), the cost of equity (risk-free plus beta times the equity risk premium: yours in `erp`, or by default our own published total premium of the stock's country), the cost of debt (interest expense over average total debt from company filings, or, where that cannot be used, the risk-free rate plus a public table's default spread for the company's interest coverage; before and after tax, with the country's corporate tax rate from a public table unless you send `tax_rate`) and WACC, weighted by market cap and total debt. Every input is in the answer with its value, its basis and its date. Banks and insurers are 422 not_applicable; an input that cannot be worked out correctly is named in 422 inputs_unavailable, never repaired; a number that is shown but needs care comes with a `warnings` entry. Basic and Pro only (Free gets 403 plan_upgrade_required). One call.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            benchmark: Optional query parameter. Listing id of the market proxy beta is measured against: an ETF, fund or stock priced in the same currency as the stock. Left out, it is ARCX:SPY for a US stock, XKRX:069500 for a Korean one and XTKS:1306 for a Japanese one; any other market needs it.
            beta: Optional query parameter. Which beta feeds the cost of equity: `raw` (default) or `adjusted` (0.67 raw plus 0.33). Both are always in the answer.
            erp: Optional query parameter. Your equity risk premium, in percent (5 means 5%). Left out, it is our own published total equity risk premium of the stock's country (the answer names its date and basis). Where we publish none, without it the answer is 400 erp_required. Above 0 and at most 25.
            frequency: Optional query parameter. Return interval: `weekly` (default; the last common trading day of each ISO week) or `monthly`.
            period: Optional query parameter. Period of interest expense: the last 12 months (`ttm`, default) or the latest full fiscal year (`annual`). Korea and Japan have annual figures only, so `annual` is what they get.
            risk_free: Optional query parameter. Your own risk-free rate, in percent. Left out, it is the 10-year point of the country's government yield curve. Needed where we have no curve (Korea): without it the answer is 422 risk_free_unavailable.
            tax_rate: Optional query parameter. Your own tax rate for the debt shield, in percent. Left out, it is the corporate tax rate of the stock's country from Damodaran's public table (PwC rates). Between 0 and 60.
            window: Optional query parameter. How far back the returns reach: `2y` (default) or `5y`.

        Returns:
            EquityCostOfCapital: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "benchmark", benchmark, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("beta", beta, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("erp", erp, "single", required=False, decimal=False))
        _query.extend(
            encode_query(
                "frequency", frequency, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "risk_free", risk_free, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("tax_rate", tax_rate, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("window", window, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/cost-of-capital", {"id": id}),
            _query,
            None,
            models.decode_EquityCostOfCapital,
        )

    async def dividends(
        self, id: str, *, cursor: str | None = None
    ) -> models.EquityDividends:
        """Dividends of one stock

        Cash dividends of one listing, newest ex-date first, paged. The list may include announced future rows. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full. `start` is sent only when older rows were cut off; upcoming rows are never cut. Each request counts one call. An unknown id is 404 not_found; a market without data yet is 404 not_covered.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            cursor: Optional query parameter.

        Returns:
            EquityDividends: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/dividends", {"id": id}),
            _query,
            None,
            models.decode_EquityDividends,
        )

    def dividends_iter(
        self, id: str, *, cursor: str | None = None
    ) -> AsyncIterator[models.EquityDividend]:
        """Dividends of one stock

        Cash dividends of one listing, newest ex-date first, paged. The list may include announced future rows. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full. `start` is sent only when older rows were cut off; upcoming rows are never cut. Each request counts one call. An unknown id is 404 not_found; a market without data yet is 404 not_covered.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            cursor: Optional query parameter.

        Returns:
            AsyncIterator[EquityDividend]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EquityDividend], str | None]:
            result = await self.dividends(id=id, cursor=next_cursor)
            return [item for item in result.dividends], result.next_cursor

        return iterate_async(page, cursor)

    async def earnings(
        self, id: str, *, cursor: str | None = None
    ) -> models.EquityEarnings:
        """Earnings of one stock

        Past earnings reports of one listing (dated today or earlier at the exchange), with estimate, actual and surprise, newest first, paged. Upcoming report dates are not included yet. `surprise_percent` is in percent. `eps_actual` is on the market data basis and can differ from the filings EPS in the valuation. `filing_id` names the annual or quarterly report that covers a past report when we hold it. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full. `start` is sent only when older rows were cut off. Each request counts one call. An unknown id is 404 not_found; a market without data yet is 404 not_covered.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            cursor: Optional query parameter.

        Returns:
            EquityEarnings: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/earnings", {"id": id}),
            _query,
            None,
            models.decode_EquityEarnings,
        )

    def earnings_iter(
        self, id: str, *, cursor: str | None = None
    ) -> AsyncIterator[models.EquityEarning]:
        """Earnings of one stock

        Past earnings reports of one listing (dated today or earlier at the exchange), with estimate, actual and surprise, newest first, paged. Upcoming report dates are not included yet. `surprise_percent` is in percent. `eps_actual` is on the market data basis and can differ from the filings EPS in the valuation. `filing_id` names the annual or quarterly report that covers a past report when we hold it. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full. `start` is sent only when older rows were cut off. Each request counts one call. An unknown id is 404 not_found; a market without data yet is 404 not_covered.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.
            cursor: Optional query parameter.

        Returns:
            AsyncIterator[EquityEarning]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EquityEarning], str | None]:
            result = await self.earnings(id=id, cursor=next_cursor)
            return [item for item in result.earnings], result.next_cursor

        return iterate_async(page, cursor)

    async def movers(
        self, *, direction: str | None = None, market: str | None = None
    ) -> models.EquityMovers:
        """Top US stock movers

        The top 25 US stocks and ETFs by `direction`: `gainers`, `losers` or `active` (most traded by value among the day's biggest gainers and losers, not the whole market). Only ordinary shares and ETFs priced at $1 or more, with at least 100,000 shares and $1 million traded today; ranked by us and cached for 10 minutes. `change_percent` is in percent. Basic and Pro only (Free gets 403 plan_upgrade_required). `market` is `us` for now; another market is 404 not_covered, an unknown `direction` is 400 invalid_query. One call.

        Stability: stable.

        Args:
            direction: Optional query parameter. `gainers` (biggest rise), `losers` (biggest fall) or `active` (most traded by value among the day's biggest gainers and losers, not the whole market). Anything else is 400 invalid_query.
            market: Optional query parameter. Market to rank. Only `us` for now; another market is 404 not_covered.

        Returns:
            EquityMovers: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "direction", direction, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("market", market, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/equities/movers", {}),
            _query,
            None,
            models.decode_EquityMovers,
        )

    async def price(self, id: str) -> models.EquityPrice:
        """Latest price of one stock

        Latest price of one listing. Free plans see the price 15 minutes late and the answer carries `delayed: true`. `change_percent` is in percent. An unknown id is 404 not_found; a market without prices yet is 404 not_covered.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.

        Returns:
            EquityPrice: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/price", {"id": id}),
            _query,
            None,
            models.decode_EquityPrice,
        )

    async def prices(self, *, ids: str) -> models.EquityPrices:
        """Latest prices for up to 50 stocks

        Latest price of each listed id. One call is counted for each id that returns a price, taken in one step: if fewer calls are left than ids that resolved, the whole request is refused with 429 quota_exceeded. Ids that return no price are listed in `errors` and cost nothing. Free plans see prices 15 minutes late. `change_percent` is in percent.

        Stability: stable.

        Args:
            ids: Required query parameter. Comma-separated listing ids, at most 50 after duplicates are removed. Each id follows the same rules as the single-price route. One call is counted for each id that returns a price.

        Returns:
            EquityPrices: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("ids", ids, "single", required=True, decimal=False))
        return await self._transport.request(
            "GET",
            encode_path("/v1/equities/prices", {}),
            _query,
            None,
            models.decode_EquityPrices,
        )

    async def profile(self, id: str) -> models.EquityProfile:
        """Profile of one stock

        The listing (symbol, name, type, exchange, country, currency), the company's sector, industry and website, and `company_id` when the listing matches a company in our filings. Open to every plan. Japan listings carry only name, exchange, country, currency and `company_id`. Fields that are not known are left out.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.

        Returns:
            EquityProfile: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}", {"id": id}),
            _query,
            None,
            models.decode_EquityProfile,
        )

    async def splits(self, id: str) -> models.EquitySplits:
        """Splits of one stock

        Share splits of one listing, newest first. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full. `start` is sent only when older rows were cut off; upcoming rows are never cut. Each request counts one call. An unknown id is 404 not_found; a market without data yet is 404 not_covered.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.

        Returns:
            EquitySplits: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/splits", {"id": id}),
            _query,
            None,
            models.decode_EquitySplits,
        )

    async def valuation(self, id: str) -> models.EquityValuation:
        """Market cap, P/E, P/S, P/B and dividend yield of one stock

        Market cap (latest price times shares outstanding), P/E (latest price over trailing 12-month diluted EPS from company filings, GAAP or IFRS as reported), P/S (market cap over trailing 12-month revenue), P/B (market cap over total equity of the latest balance sheet) and dividend yield (trailing 12-month dividends per share over the price, in percent) of one US or Korean listing, with the inputs and the dates they are as of. Korea has P/E only for now; market cap, P/S, P/B and yield come with share counts and dividends. A figure that cannot be worked out correctly is left out, never sent as 0: market cap after a split since the share count, for several share classes without a count each, and for a depositary receipt or foreign filer; P/E when EPS is negative or under 0.01, reported in another currency, or for a depositary receipt. Another class of a company, such as a preferred line, has no figures of its own and shows none. Basic and Pro only (Free gets 403 plan_upgrade_required). A listing outside the US and Korea, or without a clean company match, is 404 not_covered. One call; paid plans see live prices.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.

        Returns:
            EquityValuation: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/valuation", {"id": id}),
            _query,
            None,
            models.decode_EquityValuation,
        )

    async def valuation_history(self, id: str) -> models.EquityValuationHistory:
        """Valuation history of one stock

        Market cap, P/E, P/S, P/B and dividend yield at every fiscal period end (quarter or year end) of one US or Korean listing, oldest first. Each point is the closing price on or just before that day, adjusted for splits only, and the figures filed for that period (trailing 12-month EPS, revenue and dividends, total equity, the nearest share count), so a later restatement is in it. A figure that cannot be worked out is left out, never sent as 0, by the same rules as the valuation. History: Basic 5 years, Pro everything; `start` is sent back when the plan cut older periods. Basic and Pro only (Free gets 403 plan_upgrade_required). A listing outside the US and Korea, or without a clean company match, is 404 not_covered. One call.

        Stability: stable.

        Args:
            id: Required path parameter. Listing id: the exchange's four-letter code, a colon and the ticker, for example XNAS:MSFT or XNYS:BRK.B. A bare US ticker such as MSFT also works when it names one US listing; the answer carries the canonical id. Share classes use a dot (BRK.B); BRK-B is accepted.

        Returns:
            EquityValuationHistory: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path("/v1/equities/{id}/valuation/history", {"id": id}),
            _query,
            None,
            models.decode_EquityValuationHistory,
        )

    async def search(
        self,
        *,
        country: str | None = None,
        cursor: str | None = None,
        q: str,
        type: str | None = None,
    ) -> models.EquitySearchResults:
        """Search stocks by ticker or name

        Listings whose ticker or name starts with `q`, any case: an exact ticker first, then other tickers, then names. Optional `country` (three letters) and `type` filters. Up to 50 a page, with `next_cursor`. Read from our own symbol list, so it is open to every plan and counts one call.

        Stability: stable.

        Args:
            country: Optional query parameter. Only listings in this country, three letters (USA, KOR).
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters.
            q: Required query parameter. Start of a ticker or of a company name, any case, at least 2 characters (for example `ms` or `micro`). Order: the exact ticker, other tickers, the start of a name, then the start of a later word of a name; US primary listings first within each.
            type: Optional query parameter. Only this kind of listing.

        Returns:
            EquitySearchResults: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("q", q, "single", required=True, decimal=False))
        _query.extend(
            encode_query("type", type, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/equities/search", {}),
            _query,
            None,
            models.decode_EquitySearchResults,
        )

    def search_iter(
        self,
        *,
        country: str | None = None,
        cursor: str | None = None,
        q: str,
        type: str | None = None,
    ) -> AsyncIterator[models.EquitySearchResult]:
        """Search stocks by ticker or name

        Listings whose ticker or name starts with `q`, any case: an exact ticker first, then other tickers, then names. Optional `country` (three letters) and `type` filters. Up to 50 a page, with `next_cursor`. Read from our own symbol list, so it is open to every plan and counts one call.

        Stability: stable.

        Args:
            country: Optional query parameter. Only listings in this country, three letters (USA, KOR).
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters.
            q: Required query parameter. Start of a ticker or of a company name, any case, at least 2 characters (for example `ms` or `micro`). Order: the exact ticker, other tickers, the start of a name, then the start of a later word of a name; US primary listings first within each.
            type: Optional query parameter. Only this kind of listing.

        Returns:
            AsyncIterator[EquitySearchResult]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EquitySearchResult], str | None]:
            result = await self.search(
                country=country, cursor=next_cursor, q=q, type=type
            )
            return [item for item in result.results], result.next_cursor

        return iterate_async(page, cursor)


class AsyncEvents:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get(self, event_id: str) -> models.EventDetail:
        """Get Delivery Event

        One delivery event by ID.

        Stability: stable.

        Args:
            event_id: Required path parameter. Event ID (UUID).

        Returns:
            EventDetail: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path("/v1/events/{event_id}", {"event_id": event_id}),
            _query,
            None,
            models.decode_EventDetail,
        )

    async def list(
        self,
        *,
        countries: builtins.list[str] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> models.EventsPage:
        """List Delivery Events

        A page of delivery events, oldest first. `next_cursor` is null at the head.

        Stability: stable.

        Args:
            countries: Optional query parameter. Uppercase three-letter country codes (EMU for the euro area). Omit for all.
            cursor: Optional query parameter. Event position to read from: the cursor or next_cursor of an earlier page.
            limit: Optional query parameter. Maximum events per page.

        Returns:
            EventsPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "countries", countries, "repeat", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET", encode_path("/v1/events", {}), _query, None, models.decode_EventsPage
        )

    def list_iter(
        self,
        *,
        countries: builtins.list[str] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> AsyncIterator[models.DeliveryEvent]:
        """List Delivery Events

        A page of delivery events, oldest first. `next_cursor` is null at the head.

        Stability: stable.

        Args:
            countries: Optional query parameter. Uppercase three-letter country codes (EMU for the euro area). Omit for all.
            cursor: Optional query parameter. Event position to read from: the cursor or next_cursor of an earlier page.
            limit: Optional query parameter. Maximum events per page.

        Returns:
            AsyncIterator[DeliveryEvent]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.DeliveryEvent], str | None]:
            result = await self.list(
                countries=countries, cursor=next_cursor, limit=limit
            )
            return [item for item in result.events], result.next_cursor

        return iterate_async(page, cursor)


class AsyncFilings:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def as_reported(self, filing_id: str) -> models.AsReportedPage:
        """Get As Reported

        Stability: stable.

        Args:
            filing_id: Required path parameter.

        Returns:
            AsReportedPage: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/filings/{filing_id}/financials/as-reported",
                {"filing_id": filing_id},
            ),
            _query,
            None,
            models.decode_AsReportedPage,
        )

    async def company(
        self, company_id: str, *, as_of: str | None = None, lang: str | None = None
    ) -> models.CompanyWithListings:
        """Get Company

        Stability: stable.

        Args:
            company_id: Required path parameter.
            as_of: Optional query parameter.
            lang: Optional query parameter.

        Returns:
            CompanyWithListings: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("lang", lang, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/companies/{company_id}", {"company_id": company_id}),
            _query,
            None,
            models.decode_CompanyWithListings,
        )

    async def filing(self, filing_id: str, *, lang: str | None = None) -> models.Filing:
        """Get Filing

        Stability: stable.

        Args:
            filing_id: Required path parameter.
            lang: Optional query parameter.

        Returns:
            Filing: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("lang", lang, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/filings/{filing_id}", {"filing_id": filing_id}),
            _query,
            None,
            models.decode_Filing,
        )

    async def financials(
        self,
        company_id: str,
        *,
        as_of: str | None = None,
        basis: str | None = None,
        fields: str | None = None,
        fiscal_year: int | None = None,
        period: str | None = None,
        statement: str | None = None,
        version: str | None = None,
    ) -> models.Financials:
        """Get Financials

        Stability: stable.

        Args:
            company_id: Required path parameter.
            as_of: Optional query parameter. Pro plan only.
            basis: Optional query parameter.
            fields: Optional query parameter.
            fiscal_year: Optional query parameter.
            period: Optional query parameter.
            statement: Optional query parameter.
            version: Optional query parameter. first_reported is Pro plan only.

        Returns:
            Financials: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("basis", basis, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("fields", fields, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "fiscal_year", fiscal_year, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "statement", statement, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("version", version, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/companies/{company_id}/financials", {"company_id": company_id}
            ),
            _query,
            None,
            models.decode_Financials,
        )

    async def list_company_filings(
        self,
        company_id: str,
        *,
        cursor: str | None = None,
        filed_from: str | None = None,
        filed_to: str | None = None,
        form: str | None = None,
        include_amendments: bool | None = None,
        lang: str | None = None,
        limit: int | None = None,
        type: str | None = None,
    ) -> models.CompanyFilingsPage:
        """List Company Filings

        Stability: stable.

        Args:
            company_id: Required path parameter.
            cursor: Optional query parameter.
            filed_from: Optional query parameter.
            filed_to: Optional query parameter.
            form: Optional query parameter.
            include_amendments: Optional query parameter.
            lang: Optional query parameter.
            limit: Optional query parameter.
            type: Optional query parameter.

        Returns:
            CompanyFilingsPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "filed_from", filed_from, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("filed_to", filed_to, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("form", form, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "include_amendments",
                include_amendments,
                "single",
                required=False,
                decimal=False,
            )
        )
        _query.extend(
            encode_query("lang", lang, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("type", type, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/companies/{company_id}/filings", {"company_id": company_id}
            ),
            _query,
            None,
            models.decode_CompanyFilingsPage,
        )

    def list_company_filings_iter(
        self,
        company_id: str,
        *,
        cursor: str | None = None,
        filed_from: str | None = None,
        filed_to: str | None = None,
        form: str | None = None,
        include_amendments: bool | None = None,
        lang: str | None = None,
        limit: int | None = None,
        type: str | None = None,
    ) -> AsyncIterator[models.ListedFiling]:
        """List Company Filings

        Stability: stable.

        Args:
            company_id: Required path parameter.
            cursor: Optional query parameter.
            filed_from: Optional query parameter.
            filed_to: Optional query parameter.
            form: Optional query parameter.
            include_amendments: Optional query parameter.
            lang: Optional query parameter.
            limit: Optional query parameter.
            type: Optional query parameter.

        Returns:
            AsyncIterator[ListedFiling]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.ListedFiling], str | None]:
            result = await self.list_company_filings(
                company_id=company_id,
                cursor=next_cursor,
                filed_from=filed_from,
                filed_to=filed_to,
                form=form,
                include_amendments=include_amendments,
                lang=lang,
                limit=limit,
                type=type,
            )
            return [item for item in result.filings], result.next_cursor

        return iterate_async(page, cursor)

    async def list_holders(
        self,
        company_id: str,
        *,
        lang: str | None = None,
        limit: int | None = None,
        security: str | None = None,
    ) -> models.HoldersPage:
        """List Holders

        Stability: stable.

        Args:
            company_id: Required path parameter.
            lang: Optional query parameter.
            limit: Optional query parameter.
            security: Optional query parameter.

        Returns:
            HoldersPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("lang", lang, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("security", security, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/companies/{company_id}/holders", {"company_id": company_id}
            ),
            _query,
            None,
            models.decode_HoldersPage,
        )

    async def list_latest_filings(
        self,
        *,
        country: str | None = None,
        lang: str | None = None,
        limit: int | None = None,
        type: str | None = None,
    ) -> models.LatestFilingsPage:
        """List Latest Filings

        Stability: stable.

        Args:
            country: Optional query parameter.
            lang: Optional query parameter.
            limit: Optional query parameter.
            type: Optional query parameter.

        Returns:
            LatestFilingsPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("lang", lang, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("type", type, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/filings/latest", {}),
            _query,
            None,
            models.decode_LatestFilingsPage,
        )

    async def search_companies(
        self,
        *,
        as_of: str | None = None,
        country: str | None = None,
        lang: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        registry: str | None = None,
    ) -> models.CompanySearchPage:
        """Search Companies

        Stability: stable.

        Args:
            as_of: Optional query parameter.
            country: Optional query parameter.
            lang: Optional query parameter.
            limit: Optional query parameter.
            q: Optional query parameter.
            registry: Optional query parameter.

        Returns:
            CompanySearchPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("as_of", as_of, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("lang", lang, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("q", q, "single", required=False, decimal=False))
        _query.extend(
            encode_query("registry", registry, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/companies", {}),
            _query,
            None,
            models.decode_CompanySearchPage,
        )


class AsyncFunds:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def bars(
        self,
        id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        interval: str | None = None,
        start: str | None = None,
    ) -> models.EquityBars:
        """Price bars of one fund

        Daily (`1d`) or one-minute (`1m`) bars, oldest first, in the stock bar shape. A mutual fund's daily bar is its daily NAV (open, high, low and close are the NAV, no volume); it has no one-minute bars (400 invalid_interval). One-minute bars are for ETFs on Basic and Pro (Free gets 403 plan_upgrade_required). History: Free 12 months, Basic 5 years, Pro everything; `start` is sent back when the plan raised it. Up to 5,000 bars a page, with `next_cursor`; a cursor that no longer matches the prices is 409 cursor_expired. One call a page.

        Stability: stable.

        Args:
            id: Required path parameter. Fund id. An ETF is its listing id: the exchange's four-letter code, a colon and the ticker (ARCX:SPY). A mutual fund is FUND, a colon and its ticker (FUND:VFIAX). A bare US ticker such as SPY also works when it names one US listing; the answer carries the canonical id.
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters. A cursor stops working when the prices behind it changed (a split or dividend): 409 cursor_expired.
            end: Optional query parameter. Last bar. `1d`: a date, inclusive; left out means the latest session whose bar is out. `1m`: a UTC time, exclusive; left out means now, or five days after `start`. At most 5 days between `start` and `end` for `1m` (400 range_too_large).
            interval: Optional query parameter. `1d` (one bar per session; a mutual fund's bar is its daily NAV) or `1m` (one-minute bars: ETFs only, Basic and Pro only). Anything else is 400 invalid_interval.
            start: Optional query parameter. First bar. `1d`: a date (YYYY-MM-DD), inclusive; left out means the oldest bar your plan reaches. `1m`: a UTC time (YYYY-MM-DDTHH:MM:SSZ, or a date for 00:00 UTC), inclusive; left out means one day before `end`.

        Returns:
            EquityBars: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=False, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/funds/{id}/bars", {"id": id}),
            _query,
            None,
            models.decode_EquityBars,
        )

    def bars_iter(
        self,
        id: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        interval: str | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.EquityBar]:
        """Price bars of one fund

        Daily (`1d`) or one-minute (`1m`) bars, oldest first, in the stock bar shape. A mutual fund's daily bar is its daily NAV (open, high, low and close are the NAV, no volume); it has no one-minute bars (400 invalid_interval). One-minute bars are for ETFs on Basic and Pro (Free gets 403 plan_upgrade_required). History: Free 12 months, Basic 5 years, Pro everything; `start` is sent back when the plan raised it. Up to 5,000 bars a page, with `next_cursor`; a cursor that no longer matches the prices is 409 cursor_expired. One call a page.

        Stability: stable.

        Args:
            id: Required path parameter. Fund id. An ETF is its listing id: the exchange's four-letter code, a colon and the ticker (ARCX:SPY). A mutual fund is FUND, a colon and its ticker (FUND:VFIAX). A bare US ticker such as SPY also works when it names one US listing; the answer carries the canonical id.
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters. A cursor stops working when the prices behind it changed (a split or dividend): 409 cursor_expired.
            end: Optional query parameter. Last bar. `1d`: a date, inclusive; left out means the latest session whose bar is out. `1m`: a UTC time, exclusive; left out means now, or five days after `start`. At most 5 days between `start` and `end` for `1m` (400 range_too_large).
            interval: Optional query parameter. `1d` (one bar per session; a mutual fund's bar is its daily NAV) or `1m` (one-minute bars: ETFs only, Basic and Pro only). Anything else is 400 invalid_interval.
            start: Optional query parameter. First bar. `1d`: a date (YYYY-MM-DD), inclusive; left out means the oldest bar your plan reaches. `1m`: a UTC time (YYYY-MM-DDTHH:MM:SSZ, or a date for 00:00 UTC), inclusive; left out means one day before `end`.

        Returns:
            AsyncIterator[EquityBar]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EquityBar], str | None]:
            result = await self.bars(
                id=id, cursor=next_cursor, end=end, interval=interval, start=start
            )
            return [item for item in result.bars], result.next_cursor

        return iterate_async(page, cursor)

    async def distributions(
        self, id: str, *, cursor: str | None = None
    ) -> models.FundDistributions:
        """Distributions of one fund

        Distributions of one fund, newest ex-date first, paged. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full; `start` is sent only when older rows were cut off. Each request counts one call. An unknown id is 404 not_found.

        Stability: stable.

        Args:
            id: Required path parameter. Fund id. An ETF is its listing id: the exchange's four-letter code, a colon and the ticker (ARCX:SPY). A mutual fund is FUND, a colon and its ticker (FUND:VFIAX). A bare US ticker such as SPY also works when it names one US listing; the answer carries the canonical id.
            cursor: Optional query parameter.

        Returns:
            FundDistributions: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/funds/{id}/distributions", {"id": id}),
            _query,
            None,
            models.decode_FundDistributions,
        )

    def distributions_iter(
        self, id: str, *, cursor: str | None = None
    ) -> AsyncIterator[models.FundDistribution]:
        """Distributions of one fund

        Distributions of one fund, newest ex-date first, paged. The plan sets how far back the past goes: Free 12 months, Basic 5 years, Pro full; `start` is sent only when older rows were cut off. Each request counts one call. An unknown id is 404 not_found.

        Stability: stable.

        Args:
            id: Required path parameter. Fund id. An ETF is its listing id: the exchange's four-letter code, a colon and the ticker (ARCX:SPY). A mutual fund is FUND, a colon and its ticker (FUND:VFIAX). A bare US ticker such as SPY also works when it names one US listing; the answer carries the canonical id.
            cursor: Optional query parameter.

        Returns:
            AsyncIterator[FundDistribution]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.FundDistribution], str | None]:
            result = await self.distributions(id=id, cursor=next_cursor)
            return [item for item in result.distributions], result.next_cursor

        return iterate_async(page, cursor)

    async def price(self, id: str) -> models.FundPrice:
        """Latest price of one fund

        An ETF's last price, in the stock price shape plus `type: etf` (Free sees it 15 minutes late and the answer carries `delayed: true`), or a mutual fund's latest NAV (`type: mutual_fund`: `nav`, `previous_nav`, `change`, `change_percent` and the NAV's `date`; an end-of-day value, never delayed, `stale` once it is older than the next business day). `change_percent` is in percent. A stock id is 404 not_found.

        Stability: stable.

        Args:
            id: Required path parameter. Fund id. An ETF is its listing id: the exchange's four-letter code, a colon and the ticker (ARCX:SPY). A mutual fund is FUND, a colon and its ticker (FUND:VFIAX). A bare US ticker such as SPY also works when it names one US listing; the answer carries the canonical id.

        Returns:
            FundPrice: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path("/v1/funds/{id}/price", {"id": id}),
            _query,
            None,
            models.decode_FundPrice,
        )

    async def prices(self, *, ids: str) -> models.FundPrices:
        """Latest prices for up to 50 funds

        Latest price of each listed fund: an ETF's last price (Free sees it 15 minutes late) or a mutual fund's latest NAV. One call is counted for each id that returns a price, taken in one step: if fewer calls are left than ids that resolved, the whole request is refused with 429 quota_exceeded. Ids that return no price are listed in `errors` and cost nothing. `change_percent` is in percent.

        Stability: stable.

        Args:
            ids: Required query parameter. Comma-separated fund ids, at most 50 after duplicates are removed. Each id follows the same rules as the single-price route. One call is counted for each id that returns a price.

        Returns:
            FundPrices: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("ids", ids, "single", required=True, decimal=False))
        return await self._transport.request(
            "GET",
            encode_path("/v1/funds/prices", {}),
            _query,
            None,
            models.decode_FundPrices,
        )

    async def profile(self, id: str) -> models.FundProfile:
        """Profile of one fund

        The fund's symbol, name, type (`etf` or `mutual_fund`), exchange (ETFs only), country and currency, as our symbol list holds them. Open to every plan. Fields that are not known are left out.

        Stability: stable.

        Args:
            id: Required path parameter. Fund id. An ETF is its listing id: the exchange's four-letter code, a colon and the ticker (ARCX:SPY). A mutual fund is FUND, a colon and its ticker (FUND:VFIAX). A bare US ticker such as SPY also works when it names one US listing; the answer carries the canonical id.

        Returns:
            FundProfile: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path("/v1/funds/{id}", {"id": id}),
            _query,
            None,
            models.decode_FundProfile,
        )

    async def search(
        self,
        *,
        country: str | None = None,
        cursor: str | None = None,
        q: str,
        type: str | None = None,
    ) -> models.FundSearchResults:
        """Search ETFs and mutual funds by ticker or name

        Funds whose ticker or name starts with `q`, any case: an exact ticker first, then other tickers, then names. Optional `type` (`etf` or `mutual_fund`) and `country` (three letters) filters. Up to 50 a page, with `next_cursor`. Read from our own symbol list, so it is open to every plan and counts one call.

        Stability: stable.

        Args:
            country: Optional query parameter. Only funds in this country, three letters (USA).
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters.
            q: Required query parameter. Start of a ticker or of a fund name, any case, at least 2 characters (for example `vf` or `vanguard 500`). Order: the exact ticker, other tickers, the start of a name, then the start of a later word of a name.
            type: Optional query parameter. Only ETFs or only mutual funds.

        Returns:
            FundSearchResults: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("country", country, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("q", q, "single", required=True, decimal=False))
        _query.extend(
            encode_query("type", type, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/funds/search", {}),
            _query,
            None,
            models.decode_FundSearchResults,
        )

    def search_iter(
        self,
        *,
        country: str | None = None,
        cursor: str | None = None,
        q: str,
        type: str | None = None,
    ) -> AsyncIterator[models.FundSearchResult]:
        """Search ETFs and mutual funds by ticker or name

        Funds whose ticker or name starts with `q`, any case: an exact ticker first, then other tickers, then names. Optional `type` (`etf` or `mutual_fund`) and `country` (three letters) filters. Up to 50 a page, with `next_cursor`. Read from our own symbol list, so it is open to every plan and counts one call.

        Stability: stable.

        Args:
            country: Optional query parameter. Only funds in this country, three letters (USA).
            cursor: Optional query parameter. `next_cursor` of the previous page, with the same other parameters.
            q: Required query parameter. Start of a ticker or of a fund name, any case, at least 2 characters (for example `vf` or `vanguard 500`). Order: the exact ticker, other tickers, the start of a name, then the start of a later word of a name.
            type: Optional query parameter. Only ETFs or only mutual funds.

        Returns:
            AsyncIterator[FundSearchResult]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.FundSearchResult], str | None]:
            result = await self.search(
                country=country, cursor=next_cursor, q=q, type=type
            )
            return [item for item in result.results], result.next_cursor

        return iterate_async(page, cursor)


class AsyncFx:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def convert_currency(
        self, *, amount: Decimal | str, from_: str, to: str
    ) -> models.FxConversion:
        """Convert Fx

        Stability: stable.

        Args:
            amount: Required query parameter.
            from_: Required query parameter.
            to: Required query parameter.

        Returns:
            FxConversion: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("amount", amount, "single", required=True, decimal=True)
        )
        _query.extend(
            encode_query("from", from_, "single", required=True, decimal=False)
        )
        _query.extend(encode_query("to", to, "single", required=True, decimal=False))
        return await self._transport.request(
            "GET",
            encode_path("/v1/fx/convert", {}),
            _query,
            None,
            models.decode_FxConversion,
        )

    async def rate_bars(
        self,
        base: str,
        *,
        currency: str,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        limit: int | None = None,
        start: str,
    ) -> models.FxBars:
        """Get Fx Rate Bars

        Closed open-high-low-close bars for one currency against USD, from one minute to one day. A request may span at most 3 days of 1m bars, 14 days of 5m bars, 60 days of 15m bars; a longer range returns 400. Wider intervals have no cap.

        Stability: stable.

        Args:
            base: Required path parameter.
            currency: Required query parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            limit: Optional query parameter.
            start: Required query parameter.

        Returns:
            FxBars: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("currency", currency, "single", required=True, decimal=False)
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/fx/rates/{base}/bars", {"base": base}),
            _query,
            None,
            models.decode_FxBars,
        )

    def rate_bars_iter(
        self,
        base: str,
        *,
        currency: str,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        limit: int | None = None,
        start: str,
    ) -> AsyncIterator[models.FxBar]:
        """Get Fx Rate Bars

        Closed open-high-low-close bars for one currency against USD, from one minute to one day. A request may span at most 3 days of 1m bars, 14 days of 5m bars, 60 days of 15m bars; a longer range returns 400. Wider intervals have no cap.

        Stability: stable.

        Args:
            base: Required path parameter.
            currency: Required query parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            limit: Optional query parameter.
            start: Required query parameter.

        Returns:
            AsyncIterator[FxBar]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.FxBar], str | None]:
            result = await self.rate_bars(
                base=base,
                currency=currency,
                cursor=next_cursor,
                end=end,
                interval=interval,
                limit=limit,
                start=start,
            )
            return [item for item in result.bars], result.next_cursor

        return iterate_async(page, cursor)

    async def rate_history(
        self,
        base: str,
        *,
        currencies: builtins.list[str],
        cursor: str | None = None,
        end_date: str,
        limit: int | None = None,
        start_date: str,
    ) -> models.FxHistory:
        """Get Fx Rate History

        Stability: stable.

        Args:
            base: Required path parameter.
            currencies: Required query parameter.
            cursor: Optional query parameter.
            end_date: Required query parameter.
            limit: Optional query parameter.
            start_date: Required query parameter.

        Returns:
            FxHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "currencies", currencies, "comma_join", required=True, decimal=False
            )
        )
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("end_date", end_date, "single", required=True, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "start_date", start_date, "single", required=True, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/fx/rates/{base}/observations", {"base": base}),
            _query,
            None,
            models.decode_FxHistory,
        )

    def rate_history_iter(
        self,
        base: str,
        *,
        currencies: builtins.list[str],
        cursor: str | None = None,
        end_date: str,
        limit: int | None = None,
        start_date: str,
    ) -> AsyncIterator[models.FxHistoricalObservation]:
        """Get Fx Rate History

        Stability: stable.

        Args:
            base: Required path parameter.
            currencies: Required query parameter.
            cursor: Optional query parameter.
            end_date: Required query parameter.
            limit: Optional query parameter.
            start_date: Required query parameter.

        Returns:
            AsyncIterator[FxHistoricalObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.FxHistoricalObservation], str | None]:
            result = await self.rate_history(
                base=base,
                currencies=currencies,
                cursor=next_cursor,
                end_date=end_date,
                limit=limit,
                start_date=start_date,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def rates(
        self, base: str, *, currencies: builtins.list[str] | None = None
    ) -> models.FxRates:
        """Get Fx Rates

        Stability: stable.

        Args:
            base: Required path parameter.
            currencies: Optional query parameter.

        Returns:
            FxRates: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "currencies", currencies, "comma_join", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/fx/rates/{base}", {"base": base}),
            _query,
            None,
            models.decode_FxRates,
        )


class AsyncPredictions:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def binary(
        self, event_id: str, *, at: str | None = None
    ) -> models.BinaryEvent:
        """Get Binary Prediction

        Stability: stable.

        Args:
            event_id: Required path parameter.
            at: Optional query parameter.

        Returns:
            BinaryEvent: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("at", at, "single", required=False, decimal=False))
        return await self._transport.request(
            "GET",
            encode_path("/v1/predictions/binary/{event_id}", {"event_id": event_id}),
            _query,
            None,
            models.decode_BinaryEvent,
        )

    async def binary_history(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> models.PredictionHistory:
        """Get Binary Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/predictions/binary/{event_id}/history", {"event_id": event_id}
            ),
            _query,
            None,
            models.decode_PredictionHistory,
        )

    def binary_history_iter(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> AsyncIterator[models.PredictionSeries]:
        """Get Binary Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            AsyncIterator[PredictionSeries]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PredictionSeries], str | None]:
            result = await self.binary_history(
                event_id=event_id,
                cursor=next_cursor,
                end=end,
                interval=interval,
                start=start,
            )
            return [item for item in result.series], result.next_cursor

        return iterate_async(page, cursor)

    async def extreme(
        self, event_id: str, *, at: str | None = None
    ) -> models.ExtremeEvent:
        """Get Extreme Prediction

        Stability: stable.

        Args:
            event_id: Required path parameter.
            at: Optional query parameter.

        Returns:
            ExtremeEvent: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("at", at, "single", required=False, decimal=False))
        return await self._transport.request(
            "GET",
            encode_path("/v1/predictions/extreme/{event_id}", {"event_id": event_id}),
            _query,
            None,
            models.decode_ExtremeEvent,
        )

    async def extreme_history(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> models.PredictionHistory:
        """Get Extreme Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/predictions/extreme/{event_id}/history", {"event_id": event_id}
            ),
            _query,
            None,
            models.decode_PredictionHistory,
        )

    def extreme_history_iter(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> AsyncIterator[models.PredictionSeries]:
        """Get Extreme Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            AsyncIterator[PredictionSeries]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PredictionSeries], str | None]:
            result = await self.extreme_history(
                event_id=event_id,
                cursor=next_cursor,
                end=end,
                interval=interval,
                start=start,
            )
            return [item for item in result.series], result.next_cursor

        return iterate_async(page, cursor)

    async def policy_path(self, authority: str) -> models.PolicyPath:
        """Get Policy Path

        Stability: stable.

        Args:
            authority: Required path parameter.

        Returns:
            PolicyPath: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/predictions/policy-paths/{authority}", {"authority": authority}
            ),
            _query,
            None,
            models.decode_PolicyPath,
        )

    async def policy_path_history(
        self, authority: str, *, end: str, start: str
    ) -> models.PolicyPathHistory:
        """Get Policy Path History

        Stability: stable.

        Args:
            authority: Required path parameter.
            end: Required query parameter.
            start: Required query parameter.

        Returns:
            PolicyPathHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/predictions/policy-paths/{authority}/history",
                {"authority": authority},
            ),
            _query,
            None,
            models.decode_PolicyPathHistory,
        )

    async def scalar(
        self, event_id: str, *, at: str | None = None
    ) -> models.ScalarEvent:
        """Get Scalar Prediction

        Stability: stable.

        Args:
            event_id: Required path parameter.
            at: Optional query parameter.

        Returns:
            ScalarEvent: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("at", at, "single", required=False, decimal=False))
        return await self._transport.request(
            "GET",
            encode_path("/v1/predictions/scalar/{event_id}", {"event_id": event_id}),
            _query,
            None,
            models.decode_ScalarEvent,
        )

    async def scalar_history(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> models.PredictionHistory:
        """Get Scalar Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/predictions/scalar/{event_id}/history", {"event_id": event_id}
            ),
            _query,
            None,
            models.decode_PredictionHistory,
        )

    def scalar_history_iter(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> AsyncIterator[models.PredictionSeries]:
        """Get Scalar Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            AsyncIterator[PredictionSeries]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PredictionSeries], str | None]:
            result = await self.scalar_history(
                event_id=event_id,
                cursor=next_cursor,
                end=end,
                interval=interval,
                start=start,
            )
            return [item for item in result.series], result.next_cursor

        return iterate_async(page, cursor)

    async def timing(
        self, event_id: str, *, at: str | None = None
    ) -> models.TimingEvent:
        """Get Timing Prediction

        Stability: stable.

        Args:
            event_id: Required path parameter.
            at: Optional query parameter.

        Returns:
            TimingEvent: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(encode_query("at", at, "single", required=False, decimal=False))
        return await self._transport.request(
            "GET",
            encode_path("/v1/predictions/timing/{event_id}", {"event_id": event_id}),
            _query,
            None,
            models.decode_TimingEvent,
        )

    async def timing_history(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> models.PredictionHistory:
        """Get Timing Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("end", end, "single", required=True, decimal=False))
        _query.extend(
            encode_query("interval", interval, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("start", start, "single", required=True, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/predictions/timing/{event_id}/history", {"event_id": event_id}
            ),
            _query,
            None,
            models.decode_PredictionHistory,
        )

    def timing_history_iter(
        self,
        event_id: str,
        *,
        cursor: str | None = None,
        end: str,
        interval: str | None = None,
        start: str,
    ) -> AsyncIterator[models.PredictionSeries]:
        """Get Timing Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            cursor: Optional query parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            AsyncIterator[PredictionSeries]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PredictionSeries], str | None]:
            result = await self.timing_history(
                event_id=event_id,
                cursor=next_cursor,
                end=end,
                interval=interval,
                start=start,
            )
            return [item for item in result.series], result.next_cursor

        return iterate_async(page, cursor)

    async def get_topic(self, topic_id: str) -> models.PredictionTopicDetail:
        """Get Prediction Topic

        Stability: stable.

        Args:
            topic_id: Required path parameter.

        Returns:
            PredictionTopicDetail: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path("/v1/predictions/topics/{topic_id}", {"topic_id": topic_id}),
            _query,
            None,
            models.decode_PredictionTopicDetail,
        )

    async def list_events(
        self,
        *,
        cursor: str | None = None,
        from_: str | None = None,
        limit: int | None = None,
        release_id: str | None = None,
        shape: str | None = None,
        status: str | None = None,
        to: str | None = None,
        topic: str | None = None,
    ) -> models.PredictionEventsPage:
        """List Prediction Events

        Stability: stable.

        Args:
            cursor: Optional query parameter.
            from_: Optional query parameter.
            limit: Optional query parameter.
            release_id: Optional query parameter.
            shape: Optional query parameter.
            status: Optional query parameter.
            to: Optional query parameter.
            topic: Optional query parameter.

        Returns:
            PredictionEventsPage: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("from", from_, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "release_id", release_id, "single", required=False, decimal=False
            )
        )
        _query.extend(
            encode_query("shape", shape, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("status", status, "single", required=False, decimal=False)
        )
        _query.extend(encode_query("to", to, "single", required=False, decimal=False))
        _query.extend(
            encode_query("topic", topic, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/predictions/events", {}),
            _query,
            None,
            models.decode_PredictionEventsPage,
        )

    def list_events_iter(
        self,
        *,
        cursor: str | None = None,
        from_: str | None = None,
        limit: int | None = None,
        release_id: str | None = None,
        shape: str | None = None,
        status: str | None = None,
        to: str | None = None,
        topic: str | None = None,
    ) -> AsyncIterator[models.PredictionEventSummary]:
        """List Prediction Events

        Stability: stable.

        Args:
            cursor: Optional query parameter.
            from_: Optional query parameter.
            limit: Optional query parameter.
            release_id: Optional query parameter.
            shape: Optional query parameter.
            status: Optional query parameter.
            to: Optional query parameter.
            topic: Optional query parameter.

        Returns:
            AsyncIterator[PredictionEventSummary]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.PredictionEventSummary], str | None]:
            result = await self.list_events(
                cursor=next_cursor,
                from_=from_,
                limit=limit,
                release_id=release_id,
                shape=shape,
                status=status,
                to=to,
                topic=topic,
            )
            return [item for item in result.events], result.next_cursor

        return iterate_async(page, cursor)

    async def list_topics(self, *, group: str | None = None) -> models.PredictionTopics:
        """List Prediction Topics

        Stability: stable.

        Args:
            group: Optional query parameter.

        Returns:
            PredictionTopics: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("group", group, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/predictions/topics", {}),
            _query,
            None,
            models.decode_PredictionTopics,
        )


class AsyncWebhooks:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def configuration_history(
        self, destination_id: str
    ) -> models.WebhookHistoryResponse:
        """Configuration History

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).

        Returns:
            WebhookHistoryResponse: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}/history",
                {"destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_WebhookHistoryResponse,
        )

    async def create_destination(
        self,
        *,
        companies: builtins.list[str] | None | Unset = UNSET,
        countries: builtins.list[str],
        enabled: bool | None | Unset = UNSET,
        families: builtins.list[str],
        url: str,
    ) -> models.WebhookDestinationCreated:
        """Create Destination

        Stability: stable.

        Args:
            companies: Optional body parameter. Companies to watch, as `usa:0000320193`. Required with the `filings` family and refused without it: only filings of a listed company (or, for 13D/G, its subject) are sent. Basic 50, Pro 1,000.
            countries: Required body parameter. Countries from the active profile's catalogue.
            enabled: Optional body parameter.
            families: Required body parameter.
            url: Required body parameter.

        Returns:
            WebhookDestinationCreated: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "POST",
            encode_path("/v1/webhooks/destinations", {}),
            _query,
            encode_body(
                {
                    "companies": companies,
                    "countries": countries,
                    "enabled": enabled,
                    "families": families,
                    "url": url,
                }
            ),
            models.decode_WebhookDestinationCreated,
        )

    async def delete_destination(self, destination_id: str) -> models.NoContent:
        """Delete Destination

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).

        Returns:
            NoContent: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "DELETE",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}",
                {"destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_NoContent,
        )

    async def delivery_history(
        self,
        destination_id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> models.WebhookDeliveriesResponse:
        """Delivery History

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).
            cursor: Optional query parameter.
            limit: Optional query parameter.

        Returns:
            WebhookDeliveriesResponse: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query("cursor", cursor, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("limit", limit, "single", required=False, decimal=False)
        )
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}/deliveries",
                {"destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_WebhookDeliveriesResponse,
        )

    def delivery_history_iter(
        self,
        destination_id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> AsyncIterator[models.WebhookDelivery]:
        """Delivery History

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).
            cursor: Optional query parameter.
            limit: Optional query parameter.

        Returns:
            AsyncIterator[WebhookDelivery]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.WebhookDelivery], str | None]:
            result = await self.delivery_history(
                destination_id=destination_id, cursor=next_cursor, limit=limit
            )
            return [item for item in result.deliveries], result.next_cursor

        return iterate_async(page, cursor)

    async def get_destination(
        self, destination_id: str
    ) -> models.WebhookDestinationResponse:
        """Get Destination

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).

        Returns:
            WebhookDestinationResponse: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}",
                {"destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_WebhookDestinationResponse,
        )

    async def list_destinations(self) -> models.WebhookDestinationList:
        """List Destinations

        Stability: stable.

        Returns:
            WebhookDestinationList: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "GET",
            encode_path("/v1/webhooks/destinations", {}),
            _query,
            None,
            models.decode_WebhookDestinationList,
        )

    async def replay_delivery(
        self, delivery_id: str, destination_id: str
    ) -> models.NoContent:
        """Replay Delivery

        Stability: stable.

        Args:
            delivery_id: Required path parameter. Delivery ID (UUID).
            destination_id: Required path parameter. Webhook destination ID (UUID).

        Returns:
            NoContent: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "POST",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}/deliveries/{delivery_id}/replay",
                {"delivery_id": delivery_id, "destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_NoContent,
        )

    async def rotate_secret(
        self, destination_id: str
    ) -> models.WebhookDestinationCreated:
        """Rotate Secret

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).

        Returns:
            WebhookDestinationCreated: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "POST",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}/rotate-secret",
                {"destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_WebhookDestinationCreated,
        )

    async def test_destination(self, destination_id: str) -> models.WebhookTestResponse:
        """Test Destination

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).

        Returns:
            WebhookTestResponse: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "POST",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}/test",
                {"destination_id": destination_id},
            ),
            _query,
            None,
            models.decode_WebhookTestResponse,
        )

    async def update_destination(
        self,
        destination_id: str,
        *,
        companies: builtins.list[str] | None | Unset = UNSET,
        countries: builtins.list[str],
        enabled: bool | None,
        families: builtins.list[str],
        url: str,
    ) -> models.WebhookDestinationResponse:
        """Update Destination

        Stability: stable.

        Args:
            destination_id: Required path parameter. Webhook destination ID (UUID).
            companies: Optional body parameter. Companies to watch, as `usa:0000320193`. Required with the `filings` family and refused without it: only filings of a listed company (or, for 13D/G, its subject) are sent. Basic 50, Pro 1,000.
            countries: Required body parameter. Countries from the active profile's catalogue.
            enabled: Required body parameter.
            families: Required body parameter.
            url: Required body parameter.

        Returns:
            WebhookDestinationResponse: Decoded response with header metadata.
        """
        _query: Query = []
        return await self._transport.request(
            "PATCH",
            encode_path(
                "/v1/webhooks/destinations/{destination_id}",
                {"destination_id": destination_id},
            ),
            _query,
            encode_body(
                {
                    "companies": companies,
                    "countries": countries,
                    "enabled": enabled,
                    "families": families,
                    "url": url,
                }
            ),
            models.decode_WebhookDestinationResponse,
        )


class AsyncStableOperations:
    def __init__(self, transport: AsyncTransport) -> None:
        self.calendar_subscriptions = AsyncCalendarSubscriptions(transport)
        self.calendars = AsyncCalendars(transport)
        self.commodities = AsyncCommodities(transport)
        self.company_calendars = AsyncCompanyCalendars(transport)
        self.crypto = AsyncCrypto(transport)
        self.economics = AsyncEconomics(transport)
        self.equities = AsyncEquities(transport)
        self.events = AsyncEvents(transport)
        self.filings = AsyncFilings(transport)
        self.funds = AsyncFunds(transport)
        self.fx = AsyncFx(transport)
        self.predictions = AsyncPredictions(transport)
        self.webhooks = AsyncWebhooks(transport)
        self.unstable = AsyncUnstableOperations(transport)


class AsyncUnstableOperations:
    def __init__(self, transport: AsyncTransport) -> None:
        pass

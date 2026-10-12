# Generated from spec/live/openapi.json sha256 549d8458a8dcfbbccea3ea4b23f7d9163c6525ce932e4c5f6657fdd9b728985c. Do not edit.
# Generated from spec/next/openapi.json sha256 549d8458a8dcfbbccea3ea4b23f7d9163c6525ce932e4c5f6657fdd9b728985c. Do not edit.
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

LIVE_SPEC_SHA = "549d8458a8dcfbbccea3ea4b23f7d9163c6525ce932e4c5f6657fdd9b728985c"


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

    def revoke(self, subscription_id: str) -> models.CalendarSubscriptionRevoked:
        """Revoke Calendar Subscription

        Stability: stable.

        Args:
            subscription_id: Required path parameter.

        Returns:
            CalendarSubscriptionRevoked: Decoded response with header metadata.
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
            models.decode_CalendarSubscriptionRevoked,
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

        Stability: stable.

        Args:
            country: Required path parameter.
            date: Required path parameter.
            scope: Optional query parameter.

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

        Stability: stable.

        Args:
            country: Required path parameter.
            from_date: Required query parameter.
            scope: Optional query parameter.

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

        Stability: stable.

        Args:
            country: Required path parameter.
            year: Required path parameter.
            scope: Optional query parameter.
            version_id: Optional query parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            price_month: Optional query parameter.
            start: Optional query parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            price_month: Optional query parameter.
            start: Optional query parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.
            price_month: Optional query parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.

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

        Stability: stable.

        Args:
            area: Optional query parameter.
            country: Optional query parameter.
            currency: Optional query parameter.
            cursor: Optional query parameter.
            limit: Optional query parameter.
            price_type: Optional query parameter.
            producer_arrangement: Optional query parameter.
            producer_type: Optional query parameter.
            product: Optional query parameter.

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

        Stability: stable.

        Args:
            area: Optional query parameter.
            country: Optional query parameter.
            currency: Optional query parameter.
            cursor: Optional query parameter.
            limit: Optional query parameter.
            price_type: Optional query parameter.
            producer_arrangement: Optional query parameter.
            producer_type: Optional query parameter.
            product: Optional query parameter.

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
        market: str | None = None,
        price_type: str | None = None,
    ) -> models.PhysicalSeriesPage:
        """List Physical Series

        Stability: stable.

        Args:
            category: Optional query parameter.
            commodity: Optional query parameter.
            country: Optional query parameter.
            currency: Optional query parameter.
            cursor: Optional query parameter.
            limit: Optional query parameter.
            market: Optional query parameter.
            price_type: Optional query parameter.

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
            encode_query("market", market, "single", required=False, decimal=False)
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
        market: str | None = None,
        price_type: str | None = None,
    ) -> Iterator[models.PhysicalSeries]:
        """List Physical Series

        Stability: stable.

        Args:
            category: Optional query parameter.
            commodity: Optional query parameter.
            country: Optional query parameter.
            currency: Optional query parameter.
            cursor: Optional query parameter.
            limit: Optional query parameter.
            market: Optional query parameter.
            price_type: Optional query parameter.

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
                market=market,
                price_type=price_type,
            )
            return [item for item in result.series], result.next_cursor

        return iterate(page, cursor)


class Economics:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def cpi(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Cpi:
        """Get Cpi

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/cpi/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def cpi_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> Iterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            Iterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = self.cpi_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def gdp(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Gdp:
        """Get Gdp

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/gdp-growth/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def gdp_growth_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> Iterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            Iterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = self.gdp_growth_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def gdp_history(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/gdp/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def gdp_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> Iterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            Iterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = self.gdp_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def inflation(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Inflation:
        """Get Inflation

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/inflation/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def inflation_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> Iterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            Iterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = self.inflation_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def labour_force_participation(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.LabourForceParticipation:
        """Get Labour Force Participation

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/labour-force-participation/observations",
                {"country": country},
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def labour_force_participation_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> Iterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            Iterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = self.labour_force_participation_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def get_release(
        self, release_id: str, *, version_id: str | None = None
    ) -> models.EconomicRelease:
        """Get Economic Release

        Stability: stable.

        Args:
            release_id: Required path parameter.
            version_id: Optional query parameter.

        Returns:
            EconomicRelease: Decoded response with header metadata.
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
            models.decode_EconomicRelease,
        )

    def trade(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.TradeSummary:
        """Get Trade

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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

    def trade_exports(
        self,
        country: str,
        *,
        classification: str | None = None,
        partner: str | None = None,
        period: str | None = None,
        product: str | None = None,
        version_id: str | None = None,
    ) -> models.TradeExports:
        """Get Trade Exports

        Stability: stable.

        Args:
            country: Required path parameter.
            classification: Optional query parameter.
            partner: Optional query parameter.
            period: Optional query parameter.
            product: Optional query parameter.
            version_id: Optional query parameter.

        Returns:
            TradeExports: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "classification",
                classification,
                "single",
                required=False,
                decimal=False,
            )
        )
        _query.extend(
            encode_query("partner", partner, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("product", product, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/trade/exports", {"country": country}),
            _query,
            None,
            models.decode_TradeExports,
        )

    def trade_exports_history(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/trade/exports/observations",
                {"country": country},
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def trade_exports_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> Iterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            Iterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = self.trade_exports_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def trade_history(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/trade/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def trade_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> Iterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            Iterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = self.trade_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def trade_imports(
        self,
        country: str,
        *,
        classification: str | None = None,
        partner: str | None = None,
        period: str | None = None,
        product: str | None = None,
        version_id: str | None = None,
    ) -> models.TradeImports:
        """Get Trade Imports

        Stability: stable.

        Args:
            country: Required path parameter.
            classification: Optional query parameter.
            partner: Optional query parameter.
            period: Optional query parameter.
            product: Optional query parameter.
            version_id: Optional query parameter.

        Returns:
            TradeImports: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "classification",
                classification,
                "single",
                required=False,
                decimal=False,
            )
        )
        _query.extend(
            encode_query("partner", partner, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("product", product, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/trade/imports", {"country": country}),
            _query,
            None,
            models.decode_TradeImports,
        )

    def trade_imports_history(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/trade/imports/observations",
                {"country": country},
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def trade_imports_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> Iterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            Iterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = self.trade_imports_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

    def unemployment(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Unemployment:
        """Get Unemployment

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/unemployment/observations",
                {"country": country},
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def unemployment_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> Iterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            Iterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = self.unemployment_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
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

        Stability: stable.

        Args:
            country: Required path parameter.
            date: Optional query parameter.
            maturity: Optional query parameter.
            version_id: Optional query parameter.

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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        maturity: builtins.list[str] | None = None,
        start: str | None = None,
    ) -> models.YieldCurveHistoryResponse:
        """Get Yield Curve History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            maturity: Optional query parameter.
            start: Optional query parameter.

        Returns:
            YieldCurveHistoryResponse: Decoded response with header metadata.
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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        maturity: builtins.list[str] | None = None,
        start: str | None = None,
    ) -> Iterator[models.YieldCurveHistoryObservation]:
        """Get Yield Curve History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            maturity: Optional query parameter.
            start: Optional query parameter.

        Returns:
            Iterator[YieldCurveHistoryObservation]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.YieldCurveHistoryObservation], str | None]:
            result = self.yield_curve_history(
                country=country,
                cursor=next_cursor,
                end=end,
                limit=limit,
                maturity=maturity,
                start=start,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate(page, cursor)

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

        Stability: stable.

        Args:
            countries: Optional query parameter.
            cursor: Optional query parameter.
            end_date: Optional query parameter.
            limit: Optional query parameter.
            start_date: Optional query parameter.

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
        _query.append(("view", "full"))
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
    ) -> Iterator[models.EconomicRelease]:
        """List Economic Releases

        Stability: stable.

        Args:
            countries: Optional query parameter.
            cursor: Optional query parameter.
            end_date: Optional query parameter.
            limit: Optional query parameter.
            start_date: Optional query parameter.

        Returns:
            Iterator[EconomicRelease]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EconomicRelease], str | None]:
            result = self.list_releases(
                countries=countries,
                cursor=next_cursor,
                end_date=end_date,
                limit=limit,
                start_date=start_date,
            )
            return [item for item in result.releases], result.next_cursor

        return iterate(page, cursor)


class Events:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get(self, event_id: str) -> models.EventDetail:
        """Get Delivery Event

        Stability: stable.

        Args:
            event_id: Required path parameter.

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

        Stability: stable.

        Args:
            countries: Optional query parameter.
            cursor: Optional query parameter.
            limit: Optional query parameter.

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

        Stability: stable.

        Args:
            countries: Optional query parameter.
            cursor: Optional query parameter.
            limit: Optional query parameter.

        Returns:
            Iterator[DeliveryEvent]: Items yielded lazily across pages.
        """

        def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.DeliveryEvent], str | None]:
            result = self.list(countries=countries, cursor=next_cursor, limit=limit)
            return [item for item in result.events], result.next_cursor

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
        """Get Prediction

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
        self, event_id: str, *, end: str, interval: str | None = None, start: str
    ) -> models.PredictionHistory:
        """Get Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
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

    def extreme(self, event_id: str, *, at: str | None = None) -> models.ExtremeEvent:
        """Get Prediction

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
        self, event_id: str, *, end: str, interval: str | None = None, start: str
    ) -> models.PredictionHistory:
        """Get Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
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
        """Get Prediction

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
        self, event_id: str, *, end: str, interval: str | None = None, start: str
    ) -> models.PredictionHistory:
        """Get Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
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

    def timing(self, event_id: str, *, at: str | None = None) -> models.TimingEvent:
        """Get Prediction

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
        self, event_id: str, *, end: str, interval: str | None = None, start: str
    ) -> models.PredictionHistory:
        """Get Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
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
            destination_id: Required path parameter.

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
        countries: builtins.list[str],
        enabled: bool | None | Unset = UNSET,
        families: builtins.list[str],
        url: str,
    ) -> models.WebhookDestinationCreated:
        """Create Destination

        Stability: stable.

        Args:
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
                    "countries": countries,
                    "enabled": enabled,
                    "families": families,
                    "url": url,
                }
            ),
            models.decode_WebhookDestinationCreated,
        )

    def delete_destination(self, destination_id: str) -> models.WebhookDeleteResponse:
        """Delete Destination

        Stability: stable.

        Args:
            destination_id: Required path parameter.

        Returns:
            WebhookDeleteResponse: Decoded response with header metadata.
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
            models.decode_WebhookDeleteResponse,
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
            destination_id: Required path parameter.
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
            destination_id: Required path parameter.
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
            destination_id: Required path parameter.

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
    ) -> models.WebhookReplayResponse:
        """Replay Delivery

        Stability: stable.

        Args:
            delivery_id: Required path parameter.
            destination_id: Required path parameter.

        Returns:
            WebhookReplayResponse: Decoded response with header metadata.
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
            models.decode_WebhookReplayResponse,
        )

    def rotate_secret(self, destination_id: str) -> models.WebhookDestinationCreated:
        """Rotate Secret

        Stability: stable.

        Args:
            destination_id: Required path parameter.

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
            destination_id: Required path parameter.

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
        countries: builtins.list[str],
        enabled: bool | None,
        families: builtins.list[str],
        url: str,
    ) -> models.WebhookDestinationResponse:
        """Update Destination

        Stability: stable.

        Args:
            destination_id: Required path parameter.
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
        self.economics = Economics(transport)
        self.events = Events(transport)
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

    async def revoke(self, subscription_id: str) -> models.CalendarSubscriptionRevoked:
        """Revoke Calendar Subscription

        Stability: stable.

        Args:
            subscription_id: Required path parameter.

        Returns:
            CalendarSubscriptionRevoked: Decoded response with header metadata.
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
            models.decode_CalendarSubscriptionRevoked,
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

        Stability: stable.

        Args:
            country: Required path parameter.
            date: Required path parameter.
            scope: Optional query parameter.

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

        Stability: stable.

        Args:
            country: Required path parameter.
            from_date: Required query parameter.
            scope: Optional query parameter.

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

        Stability: stable.

        Args:
            country: Required path parameter.
            year: Required path parameter.
            scope: Optional query parameter.
            version_id: Optional query parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            price_month: Optional query parameter.
            start: Optional query parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            price_month: Optional query parameter.
            start: Optional query parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.
            price_month: Optional query parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

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

        Stability: stable.

        Args:
            series_id: Required path parameter.

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

        Stability: stable.

        Args:
            area: Optional query parameter.
            country: Optional query parameter.
            currency: Optional query parameter.
            cursor: Optional query parameter.
            limit: Optional query parameter.
            price_type: Optional query parameter.
            producer_arrangement: Optional query parameter.
            producer_type: Optional query parameter.
            product: Optional query parameter.

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

        Stability: stable.

        Args:
            area: Optional query parameter.
            country: Optional query parameter.
            currency: Optional query parameter.
            cursor: Optional query parameter.
            limit: Optional query parameter.
            price_type: Optional query parameter.
            producer_arrangement: Optional query parameter.
            producer_type: Optional query parameter.
            product: Optional query parameter.

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
        market: str | None = None,
        price_type: str | None = None,
    ) -> models.PhysicalSeriesPage:
        """List Physical Series

        Stability: stable.

        Args:
            category: Optional query parameter.
            commodity: Optional query parameter.
            country: Optional query parameter.
            currency: Optional query parameter.
            cursor: Optional query parameter.
            limit: Optional query parameter.
            market: Optional query parameter.
            price_type: Optional query parameter.

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
            encode_query("market", market, "single", required=False, decimal=False)
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
        market: str | None = None,
        price_type: str | None = None,
    ) -> AsyncIterator[models.PhysicalSeries]:
        """List Physical Series

        Stability: stable.

        Args:
            category: Optional query parameter.
            commodity: Optional query parameter.
            country: Optional query parameter.
            currency: Optional query parameter.
            cursor: Optional query parameter.
            limit: Optional query parameter.
            market: Optional query parameter.
            price_type: Optional query parameter.

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
                market=market,
                price_type=price_type,
            )
            return [item for item in result.series], result.next_cursor

        return iterate_async(page, cursor)


class AsyncEconomics:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def cpi(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Cpi:
        """Get Cpi

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/cpi/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def cpi_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            AsyncIterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = await self.cpi_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def gdp(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Gdp:
        """Get Gdp

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/gdp-growth/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def gdp_growth_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            AsyncIterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = await self.gdp_growth_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def gdp_history(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/gdp/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def gdp_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            AsyncIterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = await self.gdp_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def inflation(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Inflation:
        """Get Inflation

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/inflation/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def inflation_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            AsyncIterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = await self.inflation_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def labour_force_participation(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.LabourForceParticipation:
        """Get Labour Force Participation

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/labour-force-participation/observations",
                {"country": country},
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def labour_force_participation_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            AsyncIterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = await self.labour_force_participation_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def get_release(
        self, release_id: str, *, version_id: str | None = None
    ) -> models.EconomicRelease:
        """Get Economic Release

        Stability: stable.

        Args:
            release_id: Required path parameter.
            version_id: Optional query parameter.

        Returns:
            EconomicRelease: Decoded response with header metadata.
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
            models.decode_EconomicRelease,
        )

    async def trade(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.TradeSummary:
        """Get Trade

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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

    async def trade_exports(
        self,
        country: str,
        *,
        classification: str | None = None,
        partner: str | None = None,
        period: str | None = None,
        product: str | None = None,
        version_id: str | None = None,
    ) -> models.TradeExports:
        """Get Trade Exports

        Stability: stable.

        Args:
            country: Required path parameter.
            classification: Optional query parameter.
            partner: Optional query parameter.
            period: Optional query parameter.
            product: Optional query parameter.
            version_id: Optional query parameter.

        Returns:
            TradeExports: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "classification",
                classification,
                "single",
                required=False,
                decimal=False,
            )
        )
        _query.extend(
            encode_query("partner", partner, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("product", product, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/trade/exports", {"country": country}),
            _query,
            None,
            models.decode_TradeExports,
        )

    async def trade_exports_history(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/trade/exports/observations",
                {"country": country},
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def trade_exports_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            AsyncIterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = await self.trade_exports_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def trade_history(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/trade/observations", {"country": country}
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def trade_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            AsyncIterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = await self.trade_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def trade_imports(
        self,
        country: str,
        *,
        classification: str | None = None,
        partner: str | None = None,
        period: str | None = None,
        product: str | None = None,
        version_id: str | None = None,
    ) -> models.TradeImports:
        """Get Trade Imports

        Stability: stable.

        Args:
            country: Required path parameter.
            classification: Optional query parameter.
            partner: Optional query parameter.
            period: Optional query parameter.
            product: Optional query parameter.
            version_id: Optional query parameter.

        Returns:
            TradeImports: Decoded response with header metadata.
        """
        _query: Query = []
        _query.extend(
            encode_query(
                "classification",
                classification,
                "single",
                required=False,
                decimal=False,
            )
        )
        _query.extend(
            encode_query("partner", partner, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("period", period, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query("product", product, "single", required=False, decimal=False)
        )
        _query.extend(
            encode_query(
                "version_id", version_id, "single", required=False, decimal=False
            )
        )
        return await self._transport.request(
            "GET",
            encode_path("/v1/economics/{country}/trade/imports", {"country": country}),
            _query,
            None,
            models.decode_TradeImports,
        )

    async def trade_imports_history(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/trade/imports/observations",
                {"country": country},
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def trade_imports_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            AsyncIterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = await self.trade_imports_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

    async def unemployment(
        self, country: str, *, period: str | None = None, version_id: str | None = None
    ) -> models.Unemployment:
        """Get Unemployment

        Stability: stable.

        Args:
            country: Required path parameter.
            period: Optional query parameter.
            version_id: Optional query parameter.

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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> models.HistoricalEconomicsResponse:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            HistoricalEconomicsResponse: Decoded response with header metadata.
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
                "/v1/economics/{country}/unemployment/observations",
                {"country": country},
            ),
            _query,
            None,
            models.decode_HistoricalEconomicsResponse,
        )

    def unemployment_history_iter(
        self,
        country: str,
        *,
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.HistoricalObservation]:
        """Get Economics History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            start: Optional query parameter.

        Returns:
            AsyncIterator[HistoricalObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.HistoricalObservation], str | None]:
            result = await self.unemployment_history(
                country=country, cursor=next_cursor, end=end, limit=limit, start=start
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

        Stability: stable.

        Args:
            country: Required path parameter.
            date: Optional query parameter.
            maturity: Optional query parameter.
            version_id: Optional query parameter.

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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        maturity: builtins.list[str] | None = None,
        start: str | None = None,
    ) -> models.YieldCurveHistoryResponse:
        """Get Yield Curve History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            maturity: Optional query parameter.
            start: Optional query parameter.

        Returns:
            YieldCurveHistoryResponse: Decoded response with header metadata.
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
        cursor: str | None = None,
        end: str | None = None,
        limit: int | None = None,
        maturity: builtins.list[str] | None = None,
        start: str | None = None,
    ) -> AsyncIterator[models.YieldCurveHistoryObservation]:
        """Get Yield Curve History

        Stability: stable.

        Args:
            country: Required path parameter.
            cursor: Optional query parameter.
            end: Optional query parameter.
            limit: Optional query parameter.
            maturity: Optional query parameter.
            start: Optional query parameter.

        Returns:
            AsyncIterator[YieldCurveHistoryObservation]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.YieldCurveHistoryObservation], str | None]:
            result = await self.yield_curve_history(
                country=country,
                cursor=next_cursor,
                end=end,
                limit=limit,
                maturity=maturity,
                start=start,
            )
            return [item for item in result.observations], result.next_cursor

        return iterate_async(page, cursor)

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

        Stability: stable.

        Args:
            countries: Optional query parameter.
            cursor: Optional query parameter.
            end_date: Optional query parameter.
            limit: Optional query parameter.
            start_date: Optional query parameter.

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
        _query.append(("view", "full"))
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
    ) -> AsyncIterator[models.EconomicRelease]:
        """List Economic Releases

        Stability: stable.

        Args:
            countries: Optional query parameter.
            cursor: Optional query parameter.
            end_date: Optional query parameter.
            limit: Optional query parameter.
            start_date: Optional query parameter.

        Returns:
            AsyncIterator[EconomicRelease]: Items yielded lazily across pages.
        """

        async def page(
            next_cursor: str | None,
        ) -> tuple[builtins.list[models.EconomicRelease], str | None]:
            result = await self.list_releases(
                countries=countries,
                cursor=next_cursor,
                end_date=end_date,
                limit=limit,
                start_date=start_date,
            )
            return [item for item in result.releases], result.next_cursor

        return iterate_async(page, cursor)


class AsyncEvents:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get(self, event_id: str) -> models.EventDetail:
        """Get Delivery Event

        Stability: stable.

        Args:
            event_id: Required path parameter.

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

        Stability: stable.

        Args:
            countries: Optional query parameter.
            cursor: Optional query parameter.
            limit: Optional query parameter.

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

        Stability: stable.

        Args:
            countries: Optional query parameter.
            cursor: Optional query parameter.
            limit: Optional query parameter.

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
        """Get Prediction

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
        self, event_id: str, *, end: str, interval: str | None = None, start: str
    ) -> models.PredictionHistory:
        """Get Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
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

    async def extreme(
        self, event_id: str, *, at: str | None = None
    ) -> models.ExtremeEvent:
        """Get Prediction

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
        self, event_id: str, *, end: str, interval: str | None = None, start: str
    ) -> models.PredictionHistory:
        """Get Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
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
        """Get Prediction

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
        self, event_id: str, *, end: str, interval: str | None = None, start: str
    ) -> models.PredictionHistory:
        """Get Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
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

    async def timing(
        self, event_id: str, *, at: str | None = None
    ) -> models.TimingEvent:
        """Get Prediction

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
        self, event_id: str, *, end: str, interval: str | None = None, start: str
    ) -> models.PredictionHistory:
        """Get Prediction History

        Stability: stable.

        Args:
            event_id: Required path parameter.
            end: Required query parameter.
            interval: Optional query parameter.
            start: Required query parameter.

        Returns:
            PredictionHistory: Decoded response with header metadata.
        """
        _query: Query = []
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
            destination_id: Required path parameter.

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
        countries: builtins.list[str],
        enabled: bool | None | Unset = UNSET,
        families: builtins.list[str],
        url: str,
    ) -> models.WebhookDestinationCreated:
        """Create Destination

        Stability: stable.

        Args:
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
                    "countries": countries,
                    "enabled": enabled,
                    "families": families,
                    "url": url,
                }
            ),
            models.decode_WebhookDestinationCreated,
        )

    async def delete_destination(
        self, destination_id: str
    ) -> models.WebhookDeleteResponse:
        """Delete Destination

        Stability: stable.

        Args:
            destination_id: Required path parameter.

        Returns:
            WebhookDeleteResponse: Decoded response with header metadata.
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
            models.decode_WebhookDeleteResponse,
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
            destination_id: Required path parameter.
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
            destination_id: Required path parameter.
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
            destination_id: Required path parameter.

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
    ) -> models.WebhookReplayResponse:
        """Replay Delivery

        Stability: stable.

        Args:
            delivery_id: Required path parameter.
            destination_id: Required path parameter.

        Returns:
            WebhookReplayResponse: Decoded response with header metadata.
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
            models.decode_WebhookReplayResponse,
        )

    async def rotate_secret(
        self, destination_id: str
    ) -> models.WebhookDestinationCreated:
        """Rotate Secret

        Stability: stable.

        Args:
            destination_id: Required path parameter.

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
            destination_id: Required path parameter.

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
        countries: builtins.list[str],
        enabled: bool | None,
        families: builtins.list[str],
        url: str,
    ) -> models.WebhookDestinationResponse:
        """Update Destination

        Stability: stable.

        Args:
            destination_id: Required path parameter.
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
        self.economics = AsyncEconomics(transport)
        self.events = AsyncEvents(transport)
        self.fx = AsyncFx(transport)
        self.predictions = AsyncPredictions(transport)
        self.webhooks = AsyncWebhooks(transport)
        self.unstable = AsyncUnstableOperations(transport)


class AsyncUnstableOperations:
    def __init__(self, transport: AsyncTransport) -> None:
        pass

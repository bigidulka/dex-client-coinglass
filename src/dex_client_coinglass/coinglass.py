from __future__ import annotations
from typing import Any
from .core import BaseClient, Json

class CoinGlassClient(BaseClient):
    def __init__(self, *, fapi_base_url: str = "https://fapi.coinglass.com", capi_base_url: str = "https://capi.coinglass.com", timeout: float = 10.0):
        super().__init__(fapi_base_url, timeout=timeout, headers={"Accept": "application/json, text/plain, */*", "Origin": "https://www.coinglass.com", "Referer": "https://www.coinglass.com/currencies/BTC"})
        self.fapi_base_url = fapi_base_url.rstrip("/")
        self.capi_base_url = capi_base_url.rstrip("/")

    def _fapi(self, path: str, params: dict[str, Any] | None = None) -> Json: return self.get(self.fapi_base_url + path, params=params)
    def _capi(self, path: str, params: dict[str, Any] | None = None) -> Json: return self.get(self.capi_base_url + path, params=params)
    def _sym(self, symbol: str) -> dict[str, str]: return {"symbol": (symbol or "BTC").upper()}

    def search(self, q: str) -> Json: return self._capi("/api/coin/search", {"q": q.upper()})
    def info(self, symbol: str) -> Json: return self._fapi("/api/coin/v2/info", self._sym(symbol))
    def profile(self, symbol: str) -> Json: return self._fapi("/api/coin/profile", self._sym(symbol))
    def related(self, symbol: str) -> Json: return self._fapi("/api/coin/related", self._sym(symbol))
    def performance(self, symbol: str) -> Json: return self._fapi("/api/coin/performance", self._sym(symbol))
    def history(self, symbol: str, range: str = "7d") -> Json: return self._fapi("/api/coin/history", {**self._sym(symbol), "range": range})
    def money_flow(self, symbol: str) -> Json: return self._fapi("/api/moneyFlow/coin", self._sym(symbol))
    def volume_heatmap(self, symbol: str) -> Json: return self._fapi("/api/coin/vol/heatmap", self._sym(symbol))
    def funding_detail(self, symbol: str) -> Json: return self._fapi("/api/fundingRate/coin/detail", self._sym(symbol))
    def open_interest(self, symbol: str) -> Json: return self._fapi("/api/openInterest/info", self._sym(symbol))
    def liquidation_chart(self, symbol: str, range: str = "7d") -> Json: return self._fapi("/api/futures/liquidation/chart", {**self._sym(symbol), "range": range})
    def coin_liquidation(self, symbol: str) -> Json: return self._fapi("/api/coin/liquidation", self._sym(symbol))
    def liquidation_today(self, symbol: str) -> Json: return self._fapi("/api/futures/liquidation/today", self._sym(symbol))

    def spot_info(self, symbol: str) -> Json: return self._capi("/api/spot/coin/info", self._sym(symbol))
    def spot_symbol(self, symbol: str) -> Json: return self._capi("/api/spot/coin/symbol", self._sym(symbol))
    def spot_markets(self, symbol: str) -> Json: return self._capi("/api/spot/coin/markets", self._sym(symbol))
    def spot_out_in(self, symbol: str) -> Json: return self._capi("/api/spot/coin/outIn", self._sym(symbol))
    def futures_tickers(self, symbol: str) -> Json: return self._capi("/api/futures/select/coins/tickers", self._sym(symbol))
    def futures_top_tickers(self, symbol: str) -> Json: return self._capi("/api/futures/top/coins/tickers", self._sym(symbol))
    def futures_flow_table(self, symbol: str) -> Json: return self._capi("/api/futures/flow/table", self._sym(symbol))
    def futures_flow_category(self, symbol: str) -> Json: return self._capi("/api/futures/flow/category", self._sym(symbol))
    def price(self, symbol: str, interval: str = "1m") -> Json: return self._capi("/api/price", {**self._sym(symbol), "interval": interval})
    def price_and_indicator(self, symbol: str) -> Json: return self._capi("/api/priceAndIndicator", self._sym(symbol))
    def support_symbol(self, symbol: str) -> Json: return self._capi("/api/support/symbol", self._sym(symbol))
    def support_symbol_v2(self, symbol: str) -> Json: return self._capi("/api/v2/support/symbol", self._sym(symbol))
    def coin_tickers(self, symbol: str) -> Json: return self._capi("/api/coin/tickers", self._sym(symbol))
    def coin_market(self, symbol: str) -> Json: return self._capi("/api/coin/market", self._sym(symbol))
    def futures_home_statistics(self) -> Json: return self._capi("/api/futures/home/statistics")
    def ip_country(self) -> Json: return self._capi("/api/ip/country")

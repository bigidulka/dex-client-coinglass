        # CoinGlass Reverse Client

        Python client for endpoints used by [https://www.coinglass.com](https://www.coinglass.com). The implementation is browser/reverse-engineered and mirrors the internal clients used in local DEX modules.

        ## Install

        ```bash
        pip install git+https://github.com/bigidulka/dex-client-coinglass.git
        ```

        For local development:

        ```bash
        pip install -e '.[dev]'
        pytest
        ```

        ## Quick start

        ```python
        from dex_client_coinglass import CoinGlassClient

        client = CoinGlassClient()
        # call any method below; all methods return decoded JSON dict/list payloads
        ```

        ## Methods

        - `search`
- `info`
- `profile`
- `related`
- `performance`
- `history`
- `money_flow`
- `volume_heatmap`
- `funding_detail`
- `open_interest`
- `liquidation_chart`
- `coin_liquidation`
- `liquidation_today`
- `spot_info`
- `spot_symbol`
- `spot_markets`
- `spot_out_in`
- `futures_tickers`
- `futures_top_tickers`
- `futures_flow_table`
- `futures_flow_category`
- `price`
- `price_and_indicator`
- `support_symbol`
- `support_symbol_v2`
- `coin_tickers`
- `coin_market`
- `futures_home_statistics`
- `ip_country`

        ## Endpoint inventory

        Extracted from existing Local clients and rechecked with browser-harness network capture where the site allowed capture.

        - `['GET', '/api/coin/search', 'search']`
- `['GET', '/api/coin/v2/info', 'info']`
- `['GET', '/api/coin/profile', 'profile']`
- `['GET', '/api/coin/related', 'related']`
- `['GET', '/api/coin/performance', 'performance']`
- `['GET', '/api/coin/history', 'history']`
- `['GET', '/api/moneyFlow/coin', 'money flow']`
- `['GET', '/api/spot/coin/info', 'spot info']`
- `['GET', '/api/spot/coin/symbol', 'spot symbol']`
- `['GET', '/api/spot/coin/markets', 'spot markets']`
- `['GET', '/api/spot/coin/outIn', 'spot out/in']`
- `['GET', '/api/coin/vol/heatmap', 'volume heatmap']`
- `['GET', '/api/futures/select/coins/tickers', 'futures tickers']`
- `['GET', '/api/futures/top/coins/tickers', 'top futures tickers']`
- `['GET', '/api/futures/flow/table', 'futures flow table']`
- `['GET', '/api/futures/flow/category', 'futures flow category']`
- `['GET', '/api/fundingRate/coin/detail', 'funding detail']`
- `['GET', '/api/openInterest/info', 'open interest']`
- `['GET', '/api/futures/liquidation/chart', 'liquidation chart']`
- `['GET', '/api/coin/liquidation', 'coin liquidation']`
- `['GET', '/api/futures/liquidation/today', 'liquidation today']`
- `['GET', '/api/price', 'price']`
- `['GET', '/api/priceAndIndicator', 'price and indicator']`
- `['GET', '/api/support/symbol', 'support symbol']`
- `['GET', '/api/v2/support/symbol', 'support symbol v2']`
- `['GET', '/api/coin/tickers', 'coin tickers']`
- `['GET', '/api/coin/market', 'coin market']`

        Full details: [`endpoint_inventory.json`](endpoint_inventory.json).

        ## Notes

        - No official SDK is used.
        - Some endpoints require Cloudflare/browser behavior; pass `use_curl_cffi=True` where available.
        - Auth/session-only methods need your own cookies/tokens. Do not commit secrets.
        - These clients are thin transport wrappers; normalize data in your application layer.

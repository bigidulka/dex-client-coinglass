import inspect
from dex_client_coinglass import CoinGlassClient


def test_client_imports_and_instantiates():
    client = CoinGlassClient()
    assert client is not None


def test_public_methods_present():
    methods = [name for name, value in inspect.getmembers(CoinGlassClient, inspect.isfunction) if not name.startswith('_')]
    assert set(['search', 'info', 'profile', 'related', 'performance', 'history', 'money_flow', 'volume_heatmap', 'funding_detail', 'open_interest', 'liquidation_chart', 'coin_liquidation', 'liquidation_today', 'spot_info', 'spot_symbol', 'spot_markets', 'spot_out_in', 'futures_tickers', 'futures_top_tickers', 'futures_flow_table', 'futures_flow_category', 'price', 'price_and_indicator', 'support_symbol', 'support_symbol_v2', 'coin_tickers', 'coin_market', 'futures_home_statistics', 'ip_country']) <= set(methods)

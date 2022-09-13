def test_import():
    from binance_historical_data import BinanceDataDumper

def test_main_class_init():
    from binance_historical_data import BinanceDataDumper
    from datetime import date, timedelta

    data_dumper = BinanceDataDumper(
        path_dir_where_to_dump=".",
        data_type="klines",  # aggTrades, klines, trades
        data_frequency="1m",  # argument for data_type="klines"
    )
    
    data_dumper.dump_data(
        tickers=["ETHUSDT"],
        date_start=date.today() - timedelta(days=7),
        date_end=None,
        is_to_update_existing=False,
        tickers_to_exclude=[],
    )
    
def test_s3_init():
    from binance_historical_data import BinanceDataDumper
    from datetime import date, timedelta

    data_dumper = BinanceDataDumper(
        path_dir_where_to_dump="s3://azel-labs-market-data/data-dumper",
        data_type="klines",  # aggTrades, klines, trades
        data_frequency="1m",  # argument for data_type="klines"
        multi_threading=False,
    )
    
    data_dumper.dump_data(
        tickers=["ETHUSDT"],
        date_start=date.today() - timedelta(days=7),
        date_end=None,
        is_to_update_existing=False,
        tickers_to_exclude=[],
    )
    

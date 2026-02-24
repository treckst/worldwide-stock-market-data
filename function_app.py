import logging
import pandas as pd
import requests 
import datetime as dt
import os
import azure.functions as func

app = func.FunctionApp()

@app.timer_trigger(schedule="0 0 14 * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def StockandExtract(myTimer: func.TimerRequest):
    today = dt.date.today().isoformat()
    name = 'worldstockdata'
    key = os.environ['STORAGE_KEY']
    api_key = os.environ['API_KEY']

    try:
        params = {'access_key': api_key,
              'symbols': 'NVDA,AAPL,GOOGL,MSFT,AMZN,META,TSLA'}
        url = 'https://api.marketstack.com/v2/eod/latest'
        r = requests.get(url, params=params)
        data = r.json()
        df = pd.DataFrame(data["data"]).reset_index()
        df.set_index("symbol", inplace=True)
        df.drop(labels= ["index", "adj_low", "adj_high", "adj_open", "adj_close", "dividend", "split_factor", "adj_volume"], axis=1, inplace=True)

        path = f'abfss://bronze@{name}.dfs.core.windows.net/stocksdata/stocksTOP7USA/date={today}/data.parquet'
        df.to_parquet(path, storage_options={'account_name': name, 'account_key': key})
        
    except Exception as e:
        print(f"Extraction failed: {e}")

    
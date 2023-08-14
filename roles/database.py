import pandas as pd

def write(data: dict, path: str, mode: str='parquet'):
    if mode == 'parquet':
        pd.DataFrame([data]).to_parquet(path, engine='pyarrow', compression='snappy', index=False)

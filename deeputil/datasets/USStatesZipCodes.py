import pandas as pd
import io
import requests


def load_data_as_pandas_df():
    dataset_url = "https://raw.githubusercontent.com/Avkash/mldl/master/data/us_states_zip_codes.csv"
    streamData=requests.get(dataset_url).content
    pdObj=pd.read_csv(io.StringIO(streamData.decode('utf-8')))
    print("Downloaded 2.3 MB dataset with 42741 rows and 6 columns..........")
    assert len(pdObj) == 42741
    assert len(pdObj.columns) == 6
    return pdObj

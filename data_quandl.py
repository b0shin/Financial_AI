import quandl

def fetch_quandl_data(dataset_code, api_key):
    quandl.ApiConfig.api_key = api_key
    data = quandl.get(dataset_code)
    return data
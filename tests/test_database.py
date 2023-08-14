import os
import pandas as pd
import pytest

from roles import database

@pytest.fixture
def data():
    return {
        "permalink": "konsus",
        "website_url": "https://www.superside.com/",
        "updated_at": "2022-07-19T02:44:23Z",
        "linkedin_url": "https://www.linkedin.com/company/superside",
        "city": "Palo Alto",
        "region": "California",
        "country": "United States"
    }

def test_written_file_exists(data):
    database.write(data, 'output.parquet')
    assert os.path.exists('output.parquet') == True

def test_saved_file_contents(data):
    test_df = pd.DataFrame([data])
    file_df = pd.read_parquet('output.parquet', engine='pyarrow')

    assert test_df.equals(file_df)

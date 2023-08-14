# Crunchbase API request

This codes tests a few situations using the Crunchbase API as initial step. The scenarios executed are described below.

For running every case a Crunchbase API key is needed. Create your account to fetch yours. 

## Read data from the organization `konsus` and save to a parquet file

For virtual environment creation for this case conda were used. To create a similar environment run the following:

```
conda create -n crunchbase python=3.11
conda activate crunchbase
pip install -r requirements.txt
```

For unit test cases execution run:

```
CRUNCHBASE_API_KEY=<YOUR-API-KEY-HERE> pytest
```

For running the main code use:

```
CRUNCHBASE_API_KEY=<YOUR-API-KEY-HERE> pytpython main.py
```

## Execute the api request and saving the results as an airflow DAG

For airflow environment docker were used, move to the `airflow` directory and run airflow with the command:

```docker compose up -d```

airflow will be available at http://127.0.0.1:8080 with username `airflow` and password `airflow`
to finish the environment setup go to Admin -> Variables and add the API key as the variable `crunchbase_api_key`




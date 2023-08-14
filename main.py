from roles import api_requests
from roles import database

data = api_requests.request_organization('konsus')
database.write(data, 'output.parquet')

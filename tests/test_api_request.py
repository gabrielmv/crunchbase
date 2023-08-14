import pytest
from roles import api_requests

@pytest.fixture
def konsus_response_fixture():
    return {
        "properties": {
            "identifier": {
                "uuid": "845c51da-c6c9-a090-e3ac-36ac02728bea",
                "value": "Superside",
                "image_id": "wwvrxnw1b7yctvwxvt1g",
                "permalink": "konsus",
                "entity_def_id": "organization"
            },
            "linkedin": {
                "value": "https://www.linkedin.com/company/superside"
            },
            "location_identifiers": [
                {
                    "uuid": "0d81d68c-9c59-f14f-0116-3ad9ce7145ca",
                    "value": "Palo Alto",
                    "permalink": "palo-alto-california",
                    "entity_def_id": "location",
                    "location_type": "city"
                },
                {
                    "uuid": "eb879a83-c91a-121e-0bb8-829782dbcf04",
                    "value": "California",
                    "permalink": "california-united-states",
                    "entity_def_id": "location",
                    "location_type": "region"
                },
                {
                    "uuid": "f110fca2-1055-99f6-996d-011c198b3928",
                    "value": "United States",
                    "permalink": "united-states",
                    "entity_def_id": "location",
                    "location_type": "country"
                },
                {
                    "uuid": "b25caef9-a1b8-3a5d-6232-93b2dfb6a1d1",
                    "value": "North America",
                    "permalink": "north-america",
                    "entity_def_id": "location",
                    "location_type": "continent"
                }
            ],
            "website_url": "https://www.superside.com/",
            "updated_at": "2022-07-19T02:44:23Z"
        }
    }

@pytest.fixture
def konsus_result_fixture():
    return {
        "permalink": "konsus",
        "website_url": "https://www.superside.com/",
        "updated_at": "2022-07-19T02:44:23Z",
        "linkedin_url": "https://www.linkedin.com/company/superside",
        "city": "Palo Alto",
        "region": "California",
        "country": "United States"
    }

def test_konsus_request(requests_mock, konsus_response_fixture, konsus_result_fixture):
    requests_mock.get(
            f'https://api.crunchbase.com/api/v4/entities/organizations/konsus',
            status_code=200,
            json=konsus_response_fixture
        )

    assert konsus_result_fixture == api_requests.request_organization('konsus')

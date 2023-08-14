import requests

from os import environ


def request_organization(organization_id: str, crunchbase_api_key: str) -> dict:
    headers = {
        'accept': 'application/json',
        'X-cb-user-key': f'{crunchbase_api_key}',
    }
    params = {
        'field_ids': 'linkedin,location_identifiers,updated_at,website_url',
    }

    response = requests.get(
            f'https://api.crunchbase.com/api/v4/entities/organizations/{organization_id}', 
            headers=headers,
            params=params
        )

    if response.status_code == 200:
        response_data = response.json()
    else:
        response.raise_for_status()

    return {
        'permalink': response_data['properties']['identifier']['permalink'],
        'website_url': response_data['properties']['website_url'],
        'updated_at': response_data['properties']['updated_at'],
        'linkedin_url': response_data['properties']['linkedin']['value'],
        'city': [location for location in response_data['properties']['location_identifiers'] if location['location_type']=='city'][0]['value'],
        'region': [location for location in response_data['properties']['location_identifiers'] if location['location_type']=='region'][0]['value'],
        'country': [location for location in response_data['properties']['location_identifiers'] if location['location_type']=='country'][0]['value']
    }

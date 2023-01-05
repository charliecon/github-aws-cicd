import PureCloudPlatformClientV2, os, time
from PureCloudPlatformClientV2.rest import ApiException

CLIENT_ID = os.environ['GENESYSCLOUD_OAUTHCLIENT_ID']
CLIENT_SECRET = os.environ['GENESYSCLOUD_OAUTHCLIENT_SECRET']
CLIENT_REGION = os.environ['GENESYSCLOUD_REGION']
GENESYSCLOUD_API_REGION = os.environ['GENESYSCLOUD_API_REGION']

PureCloudPlatformClientV2.configuration.host = GENESYSCLOUD_API_REGION
api_client = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token(CLIENT_ID, CLIENT_SECRET)
routing_api = PureCloudPlatformClientV2.RoutingApi(api_client)

def find_wrapupcode(name):
    try:
        response = routing_api.get_routing_wrapupcodes(name=name)
        if len(response.entities)==1:
            return response.entities[0]
        return None
    except ApiException as e:
        print('Exception when calling GetRoutingWrapupcodesRequest->get_routing_wrapupcodes: %s\n' % e)
        return None

def start():
    time.sleep(5)
    wrapupcode_name = 'test_wrapupcode2411'
    wrapupcode = find_wrapupcode(wrapupcode_name)
    assert not(wrapupcode is None)
    assert (wrapupcode.name==wrapupcode_name)==True, 'Returned wrapup code name does not match'

if __name__ == '__main__':
    start()
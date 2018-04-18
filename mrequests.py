import requests
import json
import yaml

class MattermostRequests:

    def __init__(self, credentials_json_path, api_yaml_path):
        with open('../mattermost_credentials.json') as file:
            login_data = json.load(file)
            self.api_url = login_data['api_url']
            self.login_id = login_data['login_id']
            self.password = login_data['password']
            
        with open('mattermost-openapi-v4.yaml') as file:
            self.api_data = yaml.load(file)

    def login(self, login_id=None, password=None):
        login_id = login_id if login_id is not None else self.login_id
        password = password if password is not None else self.password

        login_data = { 'login_id': login_id, 'password': password }
        token = requests.post(self.api_url + '/users/login', data=json.dumps(login_data)).headers['token']
        return { 'Authorization': 'Bearer ' + token }

    def send_request(self, path, method, get_headers=False, **kwargs):
        api_params = self.api_data['paths'][path][method]['parameters']
       
        # Check parameters
        for param in api_params:
            if 'required' in param and (param['required'] is True or type(param['required']) is list):
                # Quers string parameters
                if param['in'] == 'query' and param['name'] not in kwargs:
                    raise Exception('Missing argument: ' + param['name'])
                # Body parameters
                if param['in'] == 'body':
                    for sch_param in param['schema']['required']:
                        if sch_param not in kwargs:
                            raise Exception('Missing argument: ' + sch_param)
        
        # Set body parameters
        query_params = {}
        for param in api_params:
            if param['in'] == 'body':
                query_params.update({ name: kwargs[name] for name, _ in param['schema']['properties'].items() if name in kwargs})

        # Set parameters header (only the auth header...)
        auth_header = kwargs['auth_header'] if 'auth_header' in kwargs else None
        
        # Set query parameters
        url = path.format(**kwargs)
        
        # Send requests
        if method.lower() == 'get':
            response = requests.get(self.api_url + url, headers=auth_header)
        elif method.lower() == 'post':
            response = requests.post(self.api_url + url, data=json.dumps(query_params), headers=auth_header)
        elif method.lower() == 'put':
            response = requests.put(self.api_url + url, data=json.dumps(query_params), headers=auth_header)
        
        # Parse result and return
        if get_headers:  
            return response.headers, json.loads(response.text)
        else:
            return json.loads(response.text)

    def get_team_id(self, auth_header):
        data = self.send_request('/teams', 'get', auth_header=auth_header)
        return data[0]['id']

    def get_channel_list(self, auth_header, team_id):
        data = self.send_request('/teams/{team_id}/channels', 'get', team_id=team_id, auth_header=auth_header)
        return { x['id']: x['name'] for x in data }

    def post_message_to_channel(self, auth_header, channel_id, message):
        return self.send_request('/posts', 'post', channel_id=channel_id, message=message, auth_header=auth_header)

    def get_users_info(self, auth_header):
        return self.send_request('/users', 'get', auth_header=auth_header)

    def get_user_info(self, auth_header, user_id):
        return self.send_request('/users/{user_id}', 'get', user_id=user_id, auth_header=auth_header)
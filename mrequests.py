import requests
import json
import yaml

class MattermostRequests:

    def __init__(self, credentials_json_path, api_yaml_path, skip_login=False):
        with open('../mattermost_credentials.json') as file:
            login_data = json.load(file)
            self.api_url = login_data['api_url']
            self.login_id = login_data['login_id']
            self.password = login_data['password']
            
        with open('mattermost-openapi-v4.yaml') as file:
            self.api_data = yaml.load(file)

        self.auth_header = self.login(force_login=True) if not skip_login else None

    def login(self, login_id=None, password=None, force_login=False):
        if force_login:
            login_id = login_id if login_id is not None else self.login_id
            password = password if password is not None else self.password

            login_data = { 'login_id': login_id, 'password': password }
            token = requests.post(self.api_url + '/users/login', data=json.dumps(login_data)).headers['token']
            self.auth_header =  { 'Authorization': 'Bearer ' + token }
        return self.auth_header

    def send_request(self, path, method, get_headers=False, **kwargs):
        api_params = self.api_data['paths'][path][method]['parameters']
       
        # Check parameters
        for param in api_params:
            if 'required' in param and (param['required'] is True or type(param['required']) is list):
                # Path parameters
                if param['in'] == 'path' and param['name'] not in kwargs:
                    raise Exception('Missing argument: ' + param['name'])
                # Body parameters
                if param['in'] == 'body' and 'required' in param['schema']:
                    for sch_param in param['schema']['required']:
                        if sch_param not in kwargs:
                            raise Exception('Missing argument: ' + sch_param)
                # Query string parameters
                if param['in'] == 'query' and 'required' in param and param['required'] is True and param['name'] not in kwargs:
                    raise Exception('Missing argument: ' + param['name'])

        # Set query parameters
        url = path.format(**kwargs)

        # Set query string parameters
        query_params = { param['name']: kwargs[param['name']] for param in api_params if param['in'] == 'query' and param['name'] in kwargs } or None

        # Set parameters header (currently only the auth header...)
        auth_header = kwargs['auth_header'] if 'auth_header' in kwargs else self.auth_header
        if auth_header is None:
            print('Warning: No auth header is passed...')
        
        # Set body parameters
        body_params = {}
        for param in api_params:
            if param['in'] == 'body':
                schema = param['schema']

                if '$ref' in schema:  # schema is given by reference....
                    ref_type, ref_name = tuple(schema['$ref'].split('/')[1:])
                    schema = self.api_data[ref_type][ref_name]

                body_params.update({ name: kwargs[name] for name, _ in schema['properties'].items() if name in kwargs })
        body_params = body_params or None        

        # Send requests
        request_method = getattr(requests, method.lower())
        response = request_method(self.api_url + url, params=query_params, headers=auth_header, data=json.dumps(body_params))
        
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

    def get_users(self, **kwargs):
        """ Get a page of a list of users. Based on query string parameters, select users from a team,
            channel, or select users not in a specific channel. """
        return self.send_request('/users', 'get', **kwargs)

    def get_user(self, **kwargs):
        """ Get a user a object. Sensitive information will be sanitized out. """
        return self.send_request('/users/{user_id}', 'get', **kwargs)

    def update_user(self, **kwargs):
        """ Partially update a user by providing only the fields you want to update. Omitted fields will 
            not be updated. The fields that can be updated are defined in the request body, all other provided 
            fields will be ignored. """
        return self.send_request('/users/{user_id}/patch', 'put', **kwargs)

    def get_teams(self, **kwargs):
        """ For regular users only returns open teams. Users with the "manage_system" permission will 
            return teams regardless of type. """
        return self.send_request('/teams', 'get', **kwargs)

    def get_team(self, **kwargs):
        """ Get a team on the system. """
        return self.send_request('/teams/{team_id}', 'get', **kwargs)

    def update_team(self, **kwargs):
        """ Partially update a team by providing only the fields you want to update. Omitted fields will not 
            be updated. The fields that can be updated are defined in the request body, all other provided 
            fields will be ignored. """
        return self.send_request('/teams/{team_id}/patch', 'put', **kwargs)

    def get_team_members(self, **kwargs):
        """ Get a page team members list based on query string parameters - team id, page and per page. """
        return self.send_request('/teams/{team_id}/members', 'get', **kwargs)

    def create_team(self, **kwargs):
        """ Create a new team on the system. """
        return self.send_request('/teams', 'post', **kwargs)

    def delete_team(self, **kwargs):
        """ Soft deletes a team, by marking the team as deleted in the database. Soft deleted teams will 
            not be accessible in the user interface. """
        return self.send_request('/teams/{team_id}', 'delete', **kwargs)


    def add_user_to_team(self, **kwargs):
        """ Add user to the team by user_id. """
        return self.send_request('/teams/{team_id}/members', 'post', **kwargs)

    def remove_user_from_team(self, **kwargs):
        """ Delete the team member object for a user, effectively removing them from a team. """
        return self.send_request('/teams/{team_id}/members/{user_id}', 'delete', **kwargs)


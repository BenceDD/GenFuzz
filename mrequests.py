import requests
import json

from yamlhandler import YAMLHandler

class MattermostRequests:

    def __init__(self, credentials_json_path, api_yaml_path, skip_login=False):
        with open(credentials_json_path) as file:
            login_data = json.load(file)
            self.api_url = login_data['api_url']
            self.login_id = login_data['login_id']
            self.password = login_data['password']
            
        self.handler = YAMLHandler(api_yaml_path)
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
        api_params = self.handler.get_request_params(path, method)
       
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
            print('No auth header is passed...')
        
        # Set body parameters
        body_params = {}
        for param in api_params:
            if param['in'] == 'body':
                schema = param['schema']

                if '$ref' in schema:
                    raise Exception('Not implemented!')

                if schema['type'] != 'object':  # TODO
                    raise Exception('Passing non object arguments are not implemented!')

                body_params.update({ name: kwargs[name] for name in schema['properties'] if name in kwargs })
        body_params = body_params or None        

        # Send requests
        request_method = getattr(requests, method.lower())
        response = request_method(self.api_url + url, params=query_params, headers=auth_header, data=json.dumps(body_params))

        # Parse result and return
        if get_headers:  
            return response.headers, json.loads(response.text)
        else:
            return json.loads(response.text)

    def __getattr__(self, name):
        selected_methods = self.handler.get_matching_methods(name) # There are multiple methods with same name but with different params.
        
        if len(selected_methods) == 0:
            raise AttributeError('There is no such method: ' + name + ' (All exceptions catched...)')
        
        def method_wrapper(**kwargs):
            message = []
            for path, method in selected_methods:
                try:
                    return self.send_request(path, method, **kwargs)
                except Exception as e:
                    message.append(str(e))
            raise Exception(" OR ".join(message))
        return method_wrapper

    def get_methods(self):
        return self.handler.get_methods()


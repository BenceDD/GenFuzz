import yaml
import re

class YAMLHandler:

    def __init__(self, api_yaml_path):
        with open(api_yaml_path) as file:
            self.api_data = yaml.load(file)

    def __convert_name(self, name):
        return re.sub('[^a-zA-Z ]+', '', name + ' ')[:-1].replace(' ', '_').lower()

    def __follow_ref(self, ref):
        ref_type, ref_name = tuple(ref.split('/')[1:])
        return self.api_data[ref_type][ref_name]

    def __create_param(self, in_field, required, param_type):
        return {
            'in': in_field,
            'required': required is True,
            'type': param_type
        }

    def __process_schema(self, schema):
        if '$ref' in schema['schema']:
            schema['schema'] = self.__follow_ref(schema['schema']['$ref'])
            
        parameters = {}
        
        if schema['schema']['type'] == 'object':
            required_params = schema['schema']['required'] if 'required' in schema['schema'] and type(schema['schema']['required']) is list else []
            
            for name, desc in schema['schema']['properties'].items():
                if '$ref' in desc:
                    desc = self.__follow_ref(desc['$ref'])  # TODO!!
                parameters[name] = self.__create_param(schema['in'], name in required_params, desc['type'])
        
        elif schema['schema']['type'] == 'array':
            pass  # TODO!
            
        return parameters

    def get_matching_methods(self, name):
        selected_methods = []  # There are multiple methods with same name but with different params.
        for path, methods in self.api_data['paths'].items():
            for method, method_params in methods.items():
                if self.__convert_name(method_params['summary']) == name:
                    selected_methods.append((path, method))           
        return selected_methods

    def get_call_params(self, path, method_type):
        parameters = {}
        method = self.api_data['paths'][path][method_type]
        if 'parameters' in method:      
            for param in method['parameters']:
                if 'schema' in param:
                    parameters.update(self.__process_schema(param))
                else:
                    required = 'required' in param and param['required'] is True
                    parameters[param['name']] = self.__create_param(param['in'], required, param['type'])
        return parameters

    def get_methods(self):
        methods = []
        for path, method in self.api_data['paths'].items():
            for method_name, method_params in method.items():
                methods.append((self.__convert_name(method_params['summary']), self.get_call_params(path, method_name)))
        return sorted(methods, key=lambda x: x[0])
        
    def get_return_params(self, path, method):
        pass


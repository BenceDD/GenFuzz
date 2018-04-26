import yaml
import re
import copy

class YAMLHandler:

    def __init__(self, api_yaml_path):
        with open(api_yaml_path) as file:
            self.api_data = yaml.load(file)

    def __convert_name(self, name):
        return re.sub('[^a-zA-Z ]+', '', name + ' ')[:-1].replace(' ', '_').lower()

    def __follow_ref(self, ref):
        ref_type, ref_name = tuple(ref.split('/')[1:])
        return self.api_data[ref_type][ref_name]   

    def __replace_ref(self, obj):
        while(self.__replace_ref_recursively(obj)):
            pass
        return obj

    def __follow_ref(self, ref):
        ref_type, ref_name = tuple(ref.split('/')[1:])
        return self.api_data[ref_type][ref_name]
        
    def __replace_ref_recursively(self, obj):
        if type(obj) is list:
            for elem in obj:
                if self.__replace_ref_recursively(elem):
                    return True
                
        elif type(obj) is dict:
            if '$ref' in obj:
                obj.update(copy.deepcopy(self.__follow_ref(obj['$ref'])))
                obj.pop('$ref')
                return True
            else:
                for dv in obj.values():  # dict value
                    if self.__replace_ref_recursively(dv):
                        return True          
        return False

    def get_request_params(self, path, method_type):
        return self.__replace_ref(copy.deepcopy(self.api_data['paths'][path][method_type]['parameters']))

    def get_response_params(self, path, method_type):
        return self.__replace_ref(copy.deepcopy(self.api_data['paths'][path][method_type]['responses']))

    def get_matching_methods(self, name):
        selected_methods = []  # There are multiple methods with same name but with different params.
        for path, methods in self.api_data['paths'].items():
            for method, method_params in methods.items():
                if self.__convert_name(method_params['summary']) == name:
                    selected_methods.append((path, method))           
        return selected_methods

    def get_methods(self):
        methods = []
        for path, method in self.api_data['paths'].items():
            for method_name, method_params in method.items():
                params = [v['name'] for v in method_params['parameters']] if 'parameters' in method_params else []
                methods.append((self.__convert_name(method_params['summary']), params))
        return sorted(methods, key=lambda x: x[0])


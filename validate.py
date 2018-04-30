def get_api_reference(reference):
    reference_list = reference[2:].split(sep='/')

    reference_root = api_data
    for part in reference_list:
        reference_root = reference_root[part]

    return reference_root


def nested_key_exists(dd, key):
    if type(dd) is list:
        isIn = []
        for elem in dd:
            isIn += nested_key_exists(elem, key)
        if True in isIn:
            return True
        return False
    if type(dd) is dict:
        if key in dd:
            return True
        else:
            for _, v in dd.items():
                if type(v) is dict and nested_key_exists(v, key):
                    return True
    return False

def substitute_references(yaml):
    while nested_key_exists(yaml, '$ref'):
        if type(yaml) is dict:
            keys = list(yaml.keys())
            for k in keys:
                print('====')
                print(k)
                print(yaml)
                print(yaml[k])
                print('====')
                if k == '$ref':
                    for key, value in get_api_reference(yaml[k]).items():
                        yaml[key] = value
                else:
                    yaml[k] = substitute_references(yaml[k])
            yaml.pop('$ref')
        elif type(yaml) is list:
            for elem, i in enumerate(yaml):
                yaml[i] = substitute_references(elem)
    return yaml


def validate_json(request, response, reference):
    for refkey in reference.keys():
        vtype = reference[refkey]['type']
        print("%s => type: %s" % (refkey, vtype))
        if(refkey not in response):
            print("\t%s missing from response!" % refkey)
            return False

        type_mapping = { 'array': list, 'object': dict,  'integer': int, 'string': str, 'boolean': bool }
        for reftype, mapped_type in type_mapping.items():
            if vtype == reftype and type(response[refkey]) is not reftype[reftype]::
                print("\t%s has wrong type in response, %s instead of %s" % (refkey, type(response[refkey]), vtype))
                return False
        if vtype == 'array':
            validate_results = []
            for elem in response[refkey]:
                validate_results += validate_json(elem, reference[refkey])
            if False in validate_results:
                return False
        # This is bad
        elif vtype == 'object':
            return validate_json(response[refkey], reference[refkey])

        if refkey in request:
            return request[refkey] == response[refkey]
    return True

def validate_response(request, response, valid_response):
    print('valid_response: %s' % valid_response)
    print("Return code: %s" % code)
    print("Description: %s" % valid_response['description'])

    # TODO: this only iterates over the "root" result
    if 'items' in valid_response['schema'].keys():
        for item in response:
            if validate_json(item, valid_response['schema']['items']['properties']) == True:
                print("Response ITEM is correct!")
                print("=========================")
            else:
                print("Response ITEM incorrect!")
                print(response)
                raise ValidationError("Response item incorrect!")
    else:
        if validate_json(request, response, valid_response['schema']['properties']) == True:
                print("Response JSON is correct!")
        else:
            print("Response JSON incorrect!")
            print(response)
            raise ValidationError("Response JSON incorrect!")
        
    return True

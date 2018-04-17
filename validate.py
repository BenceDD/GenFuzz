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


def validate_json(tester, good):
    for gk in good.keys():
        vtype = good[gk]['type']
        print("%s => type: %s" % (gk, vtype))
        if(gk not in tester):
            print("\t%s missing from response!" % gk)
            return False
        if vtype == 'array':
            pass
            # TODO
        # This is bad
        if vtype == 'integer' and type(tester[gk]) is not int:
            print("\t%s has wrong type in response, %s instead of %s" % (gk, type(tester[gk]), vtype))
            return False
        if vtype == 'string' and type(tester[gk]) is not str:
            print("\t%s has wrong type in response, %s instead of %s" % (gk, type(tester[gk]), vtype))
            return False
        if vtype == 'boolean' and type(tester[gk]) is not bool:
            print("\t%s has wrong type in response, %s instead of %s" % (gk, type(tester[gk]), vtype))
            return False
        if vtype == 'array' and type(tester[gk]) is not list:
            print("\t%s has wrong type in response, %s instead of %s" % (gk, type(tester[gk]), vtype))
            return False
        if vtype == 'object' and type(tester[gk]) is not dict:
            print("\t%s has wrong type in response, %s instead of %s" % (gk, type(tester[gk]), vtype))    
            return False
    return True

def validate_response(path, method, response, code):
    valid_response = api_data['paths'][path][method]['responses'][code]
    substitute_references(valid_response)

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
                print("=========================")
    else:
        if validate_json(response, valid_response['schema']['properties']) == True:
                print("Response JSON is correct!")
        else:
            print("Response JSON incorrect!")
            print(response)

    return valid_response

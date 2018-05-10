import os
import json
import random
from yamlhandler import YAMLHandler

class JSONFuzzer:

    def __init__(self):
        self.samples = None

    def __read_samples(self):
        parsing = "./json_for_fuzzing/test_parsing/"
        transform = "./json_for_fuzzing/test_transform/"
        json_pieces = []
        self.samples = []
        
        self.__fill_samples(self.samples, parsing)
        self.__fill_samples(self.samples, transform)   
        
        for json_filename in self.samples:
            #print(json_filename)
            with open(json_filename) as file:
                try:
                    #print(file.name)
                    json_pieces.append(file.read())
                except Exception as e:
                    print(e)

        return json_pieces


    def __fill_samples(self, samples, directory):
        for json_filename in os.listdir(directory):
            # Only the ones which are supposed to fail on the parser
            if(json_filename.startswith("n_")):
                samples.append(directory + json_filename)

    def __get_random_element(self, dictionary):
        return random.choice(list(dictionary))

    def __get_random_failing_sample(self):
        return self.samples[random.randint(0, samples_length - 1)]

    def json_fuzzer(self, path, method_type):
        
        handler = YAMLHandler("./mattermost-openapi-v4.yaml")
        handled_request = handler.get_request_params(path, method_type)
        
        random_item = self.__get_random_element(handled_request[0])
        random_sample = self.__get_random_failing_sample()

        print('RANDOM ITEM: {0} - SAMPLE: {1}'.format(random_item, random_sample))
        
        handled_request[0][random_item] = random_sample
        
        return json.dumps(handled_request)

fuzzer = JSONFuzzer()
samples = fuzzer.__read_samples()  # ez nem fog menni, mert privát
samples_length = len(samples)

fuzzer.test_cases()
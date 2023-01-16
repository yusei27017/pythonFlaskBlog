import json

import db.mongodb as mongoDB

res = ""

def mainApi(json_param):
    params = json.loads(json_param)
    func_return_dict_data = excution_func[params["api_type"]](params['params'])
    result = {"data": func_return_dict_data}
    # print(result)
    res = json.dumps(result)
    return res

def get_mongodb_data(params):

    search_result = mongoDB.find_log_by_sort(params['sort'])
    return search_result

def test(data):
    return data

excution_func ={
    "test" : test,
    "get_mongodb_data" : get_mongodb_data
}

if __name__ == "__main__":
    data = {
        "api_type": "test",
        "data": {
            "param1": "value",
            "param2": 1,
        }
    }
    json_data = json.dumps(data)
    res = mainApi(json_data)
    print(res)
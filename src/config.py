import json



def load():
    with open("../config/config.json") as raw_data_file:
        raw_data = json.load(raw_data_file)
        values = dict(raw_data)
        return values

def get_value(key):
    data = load()
    key = str(key)
    if key in data:
        return data[key]
    else:
        ex = Exception("Config does not containkey: " + key)
        raise ex

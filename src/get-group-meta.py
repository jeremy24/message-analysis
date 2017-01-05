## imports
import json
import urllib2
from config import get_value

## globals
token = get_value("groupme_api")

def serialize(item):
    try:
        clean = vars(dict(item))
        return clean
    except Exception as ex:
        print ex 
        raise ex

def get_meta( id ):
    url = "https://api.groupme.com/v3/groups/" + str(id) + "?token=" + str(token)
    res = urllib2.urlopen(url)
    res = json.load(res)

    if int(res["meta"]["code"]) == 200:
        return dict(res["response"])
    else:
        raise Exception("Non 200 error code from get:  " + str(res["meta"]["code"]) )

def get_ids():
    with open("../raw_data/raw-groups.json") as raw_data_file:
        raw_data = json.load(raw_data_file)
    l = list(raw_data)
    ret = list()
    print l
    ret.append( l[0] )
    print ret
    return ret


def write_meta(meta):
    out_file = "../clean_data/clean-groups.json"
    clean = list()
    
    clean = map(serialize, meta)

    out = dict()
    out["groups"] = clean

    json.dump(out, out_file)

def main():
    group_meta = dict()
    group_ids = get_ids()
    
    data = map(get_meta, group_ids)

    j = 0

    # for i in data:
    #     group_meta[ "a" ] = data[i]
    #     j += 1

    print group_meta
    write_meta(group_meta)

main()


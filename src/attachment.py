import json

class Attachment:
    def __init__(self):
        self.user_ids = list()
        self.loci = list()
        self.type = None
    
    def __str__(self):
        return json.dumps(vars(self))

    def serialize(self):
        return vars(self)

def map_raw_to_attachment(raw):
    ret = Attachment()
    try:      
        m = raw["m"]
        # loci = raw["loci"]
        i_loci = m["loci"]["l"]
        i_ids = m["user_ids"]["l"]
        ret.type = m["type"]["s"]

        for tmp in i_ids:
            ret.user_ids.append(tmp["s"])
        for tmp in i_loci:
            tmp = tmp["l"]
            for inner_tmp in tmp:
                ret.loci.append(inner_tmp["n"])
    except Exception as ex:
        print "ERROR mapping raw: ", ex
        raise ex

    return ret

import json

class Attachment:
    def __init__(self):
        self.user_ids = list()
        self.loci = list()
        self.type = None
        self.file_id = None
    
    def __str__(self):
        return json.dumps(vars(self))

    def serialize(self):
        return vars(self)

def map_raw_to_attachment(raw):
    ret = Attachment()
    try:      
        m = raw["m"]
        # loci = raw["loci"]

        print "m:  ", m.keys()

        if ( "loci" in m ):
            i_loci = m["loci"]["l"]
            for tmp in i_loci:
                print "key: ", tmp
                print "value: ", tmp["l"]
                for item in tmp["l"]:
                    print "item to append: ", item["n"]
                    ret.loci.append(item["n"])
            print "loci:  ", m["loci"]["l"]

        if "user_ids" in m:
            i_ids = m["user_ids"]["l"]
            for tmp in i_ids:
                ret.user_ids.append(tmp["s"])
           
        if "type" in m:
            ret.type = m["type"]["s"]

        if "file_id" in m:
            print "file_id:  ", m["file_id"]
            ret.file_id = m["file_id"]["s"]

    except Exception as ex:
        print "ERROR mapping raw: ", ex
        raise ex

    return ret

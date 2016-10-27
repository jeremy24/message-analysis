
import json as json
from pprint import pprint
import sys


class Message:
    def __init__(self):
        self.user_id = None
        self.name = None
        self.source_guid = None
        self.text = None
        self.created_at = None
        self.sender_id = None
        self.system = None
        self.sender_type = None
        self.avatar_url = None
        self.processed_at = None
        self.group_id = None
        self.id = None
        self.attachments = None
    
    def __str__(self):
        return json.dumps(vars(self))
    
    def serialize(self):
        return vars(self)

    
def map_raw_to_message(raw):
    ret = Message()
    try:    
        ret.attachments  = raw["attachments"]["l"]
        try:
            ret.avatar_url  = raw["avatar_url"]["s"] 
        except KeyError as key_er:
            try:
                value = raw["avatar_url"]
                if "nULLValue" in value:
                    ret.avatar_url = None
                    print "avatar url is null"
                else:
                    print "ERROR: unknown key in avatar url ", value
            except Exception as inner_er:
                raise inner_er  
        except Exception as er:
            print "ERROR: unexpected ex parsing avatar url ", er

        ret.created_at   = raw["created_at"]["n"]
        ret.group_id     = raw["group_id"]["n"]
        ret.id           = raw["id"]["n"]
        ret.name         = raw["name"]["s"]
        ret.processed_at = raw["processed_at"]["n"]
        ret.sender_id    = raw["sender_id"]["n"]
        ret.sender_type  = raw["sender_type"]["s"]
        ret.source_guid  = raw["source_guid"]["s"]
        ret.system       = raw["system"]["bOOL"]
        ret.text         = raw["text"]["s"]
        ret.user_id      = raw["user_id"]["n"]
    except KeyError as key_er:
        print "ERROR: invalid dict key in mapping:  ", key_er, "   ", sys.exc_info()
        pprint(raw)
        print "\n"
    except:
        print "ERROR: error mapping raw data to class", sys.exc_info()[0]

    return ret

    

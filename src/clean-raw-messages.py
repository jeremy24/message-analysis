
import json
import time
from pprint import pprint
from message import map_raw_to_message
from message import Message
from attachment import Attachment
from attachment import map_raw_to_attachment

with open("../raw_data/raw-messages.json") as raw_data_file:
    raw_data = json.load(raw_data_file)

print "length", len(raw_data)
print "type", type(raw_data[0])
pprint(raw_data[0])
print "\n"
print raw_data[0].keys()

print "\n"
data = map(map_raw_to_message, raw_data)
print "data len:", len(data)

p_data = map(Message.serialize, data)

for tmp in p_data:
    if len(tmp["attachments"]):
        t_arr = list()
        for i_tmp in tmp["attachments"]:
            a = map_raw_to_attachment(i_tmp)
            t_arr.append(a)
        #     print "made attachment: ", a
        # print "made the attachment list:  ", t_arr
        try:
            tmp["attachments"] = map(Attachment.serialize, t_arr)
        except Exception as ex:
            print "ERROR:  ",  ex


print p_data[0]
with open("../clean_data/clean-messages.json", "w") as out_file:
    out = dict()
    out["messages"] = p_data
    out["length"] = len(p_data)
    out["created"] = time.strftime("%H:%M:%S")
    # json_str = json.dumps(p_data)
    # json_str = json.load(json_str)
    json.dump(out, out_file)

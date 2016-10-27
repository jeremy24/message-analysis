import json

with open("../data/clean-messages.json") as data_file:
    data = json.load(data_file)
    tmp_l = data["messages"]
    messages = list(tmp_l)
  
print "The file has", data["length"], "items and was made on", data["created"]

users = dict()

max_len = 0

for item in messages:
    name = item["name"]
    if len(name) > max:
        max_len = len(name)
    if name in users:
        users[name] = users[name] + 1
    else:
        users[name] = 1

print "\n\n"
i = 0

user_list = list(users)
print "There are", len(user_list), "users.\n"

user_list.sort(cmp=lambda x,y: cmp(unicode(x).encode("utf8"),unicode(y).encode("utf8")))
user_list.sort(cmp=lambda x,y: cmp(users[x], users[y]) )
# sorted(user_list,cmp=lambda x,y: cmp(x,y))

i = 1
for user in user_list:
    l_count = users[user]
    l_percent = 100 * (float(l_count)/float(len(messages)))
    l_percent = round(l_percent,2)
    l_percent = str(l_percent)
    print( "{}:  {}  {}  {}").format( str(i).zfill(3), unicode(user).encode("utf8").ljust(50), str( l_percent + "%" ).zfill(3).ljust(5), str(l_count) )
    i+=1
    if i % 10 == 0: 
        print ''    

# for key in users.keys():
#     print unicode(key).encode('utf8')
#     print("{}: {} {}").format(str(i).rjust(3), unicode(key).encode('utf8').ljust(25), users[key])
#     i+=1

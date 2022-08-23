import json
from pickletools import read_stringnl_noescape_pair

# file_open = open("Jason_text.txt", 'r')
# json_content = json.load(file_open)
# file_open.close()
# #print(json_content["friends"])
# cars = [
#     {
#         "name":"Maruti Suzuki",
#         "model":"Alto 800"
#     },
#     {
#         "name":"Tata",
#         "model":"Punch"
#     }
# ]
# json_write = open("Jason_op.txt",'w')
# json.dump(cars,json_write)
# json_write.close()

read_json = '[{"name": "Maruti Suzuki", "model": "Alto 800"}, {"name": "Tata", "model": "Punch"}]'
rd_op = json.loads(read_json)


print(rd_op)
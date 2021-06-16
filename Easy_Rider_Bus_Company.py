import itertools
import json, re

bus_stops_128 = 0
bus_stops_256 = 0
bus_stops_512 = 0
bus_stops_1024 = 0

bus_id = 0
stop_id = 0
stop_name = 0
next_stop = 0
stop_type = 0
a_time = 0

json_string = ""
total_error = 0

# json_string = input()
[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"}, {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:17"}, {"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:07"}, {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"}, {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"}, {"bus_id" : 256, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 7, "stop_type" : "", "a_time" : "09:44"}, {"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"}, {"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]

json_str = json.loads(input())

# start = set()
# transit = set()
# transfer_128 = []
# transfer_256 = []
# transfer_512 = []
# transfer_1024 = []
# finish = set()
# check = False
# control_output = False
# json_str = input()
# start_128 = []
# finish_128 = []
# start_256 = []
# finish_256 = []
# start_512 = []
# finish_512 = []
# start_1024 = []
# finish_1024 = []
# 128 Prospekt Avenue, Elm Street, Sunset Boulevard, Sesame Street
# 256 Pilotow Street, Elm Street, Fifth Avenue, Sesame Street
# 512 Sunset Boulevard, Bourbon Street
# check_128 = False
# check_256 = False
# check_512 = False
# check_1024 = False
#
# time_128 = []
# time_256 = []
# time_512 = []
# time_1024 = []
#
#
# x = 0
# a = ""
# b = ""
# c = ""
# d = ""

# tmp_128 = ""
# tmp_256 = ""
# tmp_512 = ""
# tmp_1024 = ""
#
# result_time_128 = ""
# result_time_256 = ""
# result_time_512 = ""
# result_time_1024 = ""
#
start_128 = ["Prospekt Avenue"]
transfer_128 = ["Sunset Boulevard", "Elm Street"]
finish_128 = ["Sesame Street"]

merged_128 = ["Prospekt Avenue", "Sunset Boulevard", "Elm Street", "Sesame Street"]

type_issue = set()


start_256 = ["Pilotow Street"]
transfer_256 = ["Elm Street", "Sesame Street"]
finish_256 = ["Sesame Street"]

merged_256 = ["Pilotow Street", "Elm Street", "Sesame Street"]



start_512 = ["Bourbon Street"]
finish_512 = ["Sunset Boulvard"]
transfer_512 = ["Sunset Boulvard"]

all_known_station = ["Bourbon Street", "Sunset Boulvard", "Pilotow Street","Fifth Avenue", "Elm Street", "Sesame Street", "Prospekt Avenue", "Sunset Boulevard", "Elm Street", "Sesame Street"]




for i in range(len(json_str)):
    if json_str[i]["bus_id"] == 128 and json_str[i]["stop_type"] == "O":
        if json_str[i]["stop_name"] in transfer_128 or json_str[i]["stop_name"] in transfer_256 or json_str[i]["stop_name"] in transfer_512:

        # if json_str[i]["stop_name"] in transfer_128:
             # or   json_str[i]["stop_name"] in finish_128 or json_str[i]["stop_name"] not in all_known_station:
            type_issue.add(json_str[i]["stop_name"])
#         tmp_128 = json_str[i]["a_time"]
#         if tmp_128 <= a:
#             time_128.append(json_str[i]["stop_name"])
#         else:
#             a = json_str[i]["a_time"]
    elif json_str[i]["bus_id"] == 256 and json_str[i]["stop_type"] == "O":
        if json_str[i]["stop_name"] in transfer_128 or json_str[i]["stop_name"] in transfer_256 or json_str[i]["stop_name"] in transfer_512:
        # if json_str[i]["stop_name"] in transfer_256:
             # or   json_str[i]["stop_name"] in finish_256 or json_str[i]["stop_name"] not in all_known_station:
            type_issue.add(json_str[i]["stop_name"])
#         tmp_256 = json_str[i]["a_time"]
#         if tmp_256 <= b:
#             time_256.append(json_str[i]["stop_name"])
#         else:
#             b = json_str[i]["a_time"]
    elif json_str[i]["bus_id"] == 512 and json_str[i]["stop_type"] == "O":
        if json_str[i]["stop_name"] in transfer_128 or json_str[i]["stop_name"] in transfer_256 or json_str[i]["stop_name"] in transfer_512:

        # if json_str[i]["stop_name"] in transfer_512:
            type_issue.add(json_str[i]["stop_name"])
    elif json_str[i]["bus_id"] == 1024 and json_str[i]["stop_type"] == "O":
        if json_str[i]["stop_name"] in transfer_128 or json_str[i]["stop_name"] in transfer_256 or json_str[i]["stop_name"] in transfer_512:
            type_issue.add(json_str[i]["stop_name"])
#         tmp_512 = json_str[i]["a_time"]
#         if tmp_512 <= c:
#             time_512.append(json_str[i]["stop_name"])
#         else:
#             c = json_str[i]["a_time"]
#     elif json_str[i]["bus_id"] == 1024:
#         tmp_1024 = json_str[i]["a_time"]
#         if tmp_1024 <= d:
#             time_1024.append(json_str[i]["stop_name"])
#         else:
#             d = json_str[i]["a_time"]
#
# if len(time_128) == 0 and len(time_256) == 0 and len(time_512) == 0 and len(time_1024) == 0:
#     print("Arrival time test:")
#     print("OK")
# else:
#     if len(time_128) != 0:
#         result_time_128 = f"bus_id line 128: wrong time on station {time_128.pop(0)}"
#     if len(time_256) != 0:
#         result_time_256 = f"bus_id line 256: wrong time on station {time_256.pop(0)}"
#     if len(time_512) != 0:
#         result_time_512 = f"bus_id line 512: wrong time on station {time_512.pop(0)}"
#     if len(time_1024) != 0:
#         result_time_1024 = f"bus_id line 1024: wrong time on station {time_1024.pop(0)}"
#
#
# if len(time_128) != 0 or len(time_256) != 0 or len(time_512) != 0 or len(time_1024) != 0:
#     print("Arrival time test:")
# if result_time_128 != "":
#     print(result_time_128)
# if result_time_256 != "":
#     print(result_time_256)
# if result_time_512 != "":
#     print(result_time_512)
# if result_time_1024 != "":
#     print(result_time_1024)

# if len(time_128) != 0:
#     print(result_time_128)
# if len(time_256) != 0:
#     print(result_time_256)
# if len(time_512) != 0:
#     print(result_time_512)
# if len(time_1024) != 0:
#     print(result_time_1024)

[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "O", "a_time" : "08:19"}, {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, {"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"}, {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"}, {"bus_id" : 256, "stop_id" : 6, "stop_name" : "Abbey Road", "next_stop" : 7, "stop_type" : "O", "a_time" : "09:59"}, {"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"}, {"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Abbey Road", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]
[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "Abbey Road", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "08:25"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 11, "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "09:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 14, "stop_type" : "", "a_time" : "09:45"},  {"bus_id" : 128, "stop_id" : 14, "stop_name" : "Bourbon Street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:13"},  {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : "", "a_time" : "08:16"},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08:44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 13, "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : "Orchard Road", "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  {"bus_id" : 256, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 17, "stop_type" : "O", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "O", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "S", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska Street", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:56"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Avenue", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : "", "a_time" : "14:00"},  {"bus_id" : 1024, "stop_id" : 21, "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : "13:01"},  {"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:00"},  {"bus_id" : 512, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]


print("On demand stops test:")
if len(type_issue) == 0:
    print("OK")
else:
    r = list(type_issue)
    r.sort()
    # result
    print(f"Wrong stop type: {r}")
    # print(','.join(type_issue))













    # if json_str[i]["bus_id"] == 128 and json_str[i]['stop_type'] == "S":
    #     start.add(json_str[i]["stop_name"])
    #     start_128.append(json_str[i]["stop_name"])
    # elif json_str[i]["bus_id"] == 128 and (json_str[i]['stop_type'] == ""  or json_str[i]['stop_type'] == "O"):
    #     check_128 = True
    #     transit.add(json_str[i]["stop_name"])
    #     transfer_128.append(json_str[i]["stop_name"])
    # elif json_str[i]["bus_id"] == 128 and json_str[i]['stop_type'] == "F":
    #     check = True
    #     finish.add(json_str[i]["stop_name"])
    #     finish_128.append(json_str[i]["stop_name"])
        # elif check == False :
        #       print(f"There is no start or end stop for the line: {json_str[i]['bus_id']}.")
        #       control_output = True
        #       break

        # and (json_str[i]["stop_name"] == "Prospekt Avenue" or \
        # json_str[i]["stop_name"] == "Elm Street" or json_str[i]["stop_name"] == "Sunset Boulevard" or \
        # json_str[i]["stop_name"] == "Sesame Street"):
        # bus_stops_128 += 1
        # if json_str[i]["bus_id"] == 256:
    # elif json_str[i]["bus_id"] == 256 and json_str[i]['stop_type'] == "S":
    #
    #     start.add(json_str[i]["stop_name"])
    #     start_256.append(json_str[i]["stop_name"])
    # elif json_str[i]["bus_id"] == 256 and (json_str[i]['stop_type'] == "" or json_str[i]['stop_type'] == "O"):
    #     check_256 = True
    #     transit.add(json_str[i]["stop_name"])
    #     transfer_256.append(json_str[i]["stop_name"])
    # elif json_str[i]["bus_id"] == 256 and json_str[i]['stop_type'] == "F":
    #     check = True
    #     finish.add(json_str[i]["stop_name"])
    #     finish_256.append(json_str[i]["stop_name"])
        # elif check == False:
        #     print(f"There is no start or end stop for the line: {json_str[i]['bus_id']}.")
        #     control_output = True
        #     break
        # and (json_str[i]["stop_name"] == "Pilotow Street" or \
        # json_str[i]["stop_name"] == "Elm Street" or json_str[i]["stop_name"] == "Fifth Avenue" or \
        # json_str[i]["stop_name"] == "Sesame Street"):
        # bus_stops_256 += 1
        # if json_str[i]["bus_id"] == 512:
    # elif json_str[i]["bus_id"] == 512 and json_str[i]['stop_type'] == "S":
        # check_512 = True
    #     start.add(json_str[i]["stop_name"])
    #     start_512.append(json_str[i]["stop_name"])
    # elif json_str[i]["bus_id"] == 512 and (json_str[i]['stop_type'] == "" or json_str[i]['stop_type'] == "O"):
    #     check_512 = True
    #     transit.add(json_str[i]["stop_name"])
    #     transfer_512.append(json_str[i]["stop_name"])
    # elif json_str[i]["bus_id"] == 512 and json_str[i]['stop_type'] == "F":
        # check_512 = True
        # check = True
        # finish.add(json_str[i]["stop_name"])
        # finish_512.append(json_str[i]["stop_name"])

        # elif check == False:
        #     print(f"There is no start or end stop for the line: {json_str[i]['bus_id']}.")
        #     control_output = True
        #     break
        # and (json_str[i]["stop_name"] == "Bourbon Street" or \
        #     json_str[i]["stop_name"] == "Sunset Boulevard"):
        # bus_stops_512 += 1
        # if json_str[i]["bus_id"] == 1024:
    # elif json_str[i]["bus_id"] == 1024 and json_str[i]['stop_type'] == "S":
    #     start.add(json_str[i]["stop_name"])
    #     start_1024.append(json_str[i]["stop_name"])
    # elif json_str[i]["bus_id"] == 1024 and (json_str[i]['stop_type'] == "" or json_str[i]['stop_type'] == "O"):
    #     check_1024 = True
    #     transit.add(json_str[i]["stop_name"])
    #     transfer_1024.append(json_str[i]["stop_name"])
    # elif json_str[i]["bus_id"] == 1024 and json_str[i]['stop_type'] == "F":
    #     check = True
    #     finish.add(json_str[i]["stop_name"])
    #     finish_1024.append(json_str[i]["stop_name"])
        # elif check == False:
        #     print(f"There is no start or end stop for the line: {json_str[i]['bus_id']}.")
        #     control_output = True
        #     break
        # bus_stops_1024 += 1

# transit = list(transit)
# transit.sort()
# start = list(start)
# start.sort()
# finish = list(finish)
# finish.sort()
# temp_transfer = []
#
#
# for a in itertools.chain(start_128, finish_128, start_256, finish_256, start_512, finish_512, start_1024, finish_1024, transfer_128, transfer_256, transfer_512, transfer_1024):
#         temp_transfer.append(a)
# transfer = {x for x in temp_transfer if temp_transfer.count(x) > 1}
#
# transfer_result = list(transfer)
# transfer_result.sort()
#
#
# if check_128 == True and (len(start_128) == 0 or len(finish_128) == 0):
#     x = 128
#     print(f"There is no start or end stop for the line: {x}.")
# elif check_256 == True and (len(start_256) == 0 or len(finish_256) == 0):
#     x = 256
#     print(f"There is no start or end stop for the line: {x}.")
# elif check_512 == True and (len(start_512) == 0 or len(finish_512) == 0):
#     x = 512
#     print(f"There is no start or end stop for the line: {x}.")
# elif check_1024 == True and (len(start_1024) == 0 or len(finish_1024) == 0):
#     x = 1024
#     print(f"There is no start or end stop for the line: {x}.")
# else:
#     print(f"Start stops: {len(start)}", start)
#     # print(f"Transfer stops: {len(transit)}", transit)
#     print(f"Transfer stops: {len(transfer)}", transfer_result)
#     print(f"Finish stops: {len(finish)}", finish)

#
# print(check_128)
# print(check_256)
# print(check_512)
# print(check_1024)

# print(start_1024)
# print(start_512)
# print(start_256)
# print(start_128)
# print("boo")
# print(finish_1024)
# print(finish_512)
# print(finish_256)
# print(finish_128)


# if len(start_1024) == 0 or len(finish_1024) == 0 or len(start_512) == 0 or len(finish_512) == 0 or len(
#         start_256) == 0 or len(finish_256) == 0 \
#         or len(start_128) == 0 or len(finish_128) == 0:
#     print(f"There is no start or end stop for the line: {x}.")
# else:
#     print(f"Start stops: {len(start)}", start)
#     print(f"Transfer stops: {len(transit)}", transit)
#     print(f"Finish stops: {len(finish)}", finish)

# Start stops: 3 ['Bourbon Street', 'Pilotow Street', 'Prospekt Avenue']
# Transfer stops: 3 ['Elm Street', 'Sesame Street', 'Sunset Boulevard']
# Finish stops: 2 ['Sesame Street', 'Sunset Boulevard']


# bus_id: 128, stops: 4

# print("Line names and number of stops:")
# print(f"bus_id: 128, stops: {bus_stops_128}")
# print(f"bus_id: 256, stops: {bus_stops_256}")
# print(f"bus_id: 512, stops: {bus_stops_512}")
# print(f"bus_id: 1024, stops: {bus_stops_1024}")


# for i in range(len(json_str)):
#     if type(json_str[i]["bus_id"]) != int or re.match("(128|256|512)", json_str[i]['bus_id']) is None:
#         bus_id += 1
#     if type(json_str[i]["stop_id"]) != int:
#         stop_id += 1
#     if type(json_str[i]["stop_name"]) != str or  json_str[i]["stop_name"] == "" or re.match("[A-Z].+ (Road|Street|Avenue|Boulevard)$", json_str[i]["stop_name"]) is None:
#         stop_name += 1
#     if type(json_str[i]["next_stop"]) != int:
#         next_stop += 1
#     if type(json_str[i]["stop_type"]) != str or re.match(r"[SOF]{0,1}$", json_str[i]["stop_type"]) is None: # len(json_str[i]["stop_type"]) > 1 and :
#         stop_type += 1
#     if type(json_str[i]["a_time"]) != str or re.match(r"[01]{1}[0-9]{1}\:[0-5]{1}[0-9]{1}$", json_str[i]["a_time"]) is None:#or  json_str[i]["a_time"] == "":
#         a_time += 1

# total_error = bus_id + stop_id + stop_name + next_stop + stop_type + a_time

# print(f"Type and required field validation: {total_error} errors")
# print(f"bus_id: {bus_id}")
# print(f"stop_id: {stop_id}")
# print(f"stop_name: {stop_name}")
# print(f"next_stop: {next_stop}")
# print(f"stop_type: {stop_type}")
# print(f"a_time: {a_time}")

# Format validation: 9 errors
# stop_name: 3
# stop_type: 2
# a_time: 4

# print(f"Format validation: {total_error} errors")
# print(f"stop_name: {stop_name}")
# print(f"stop_type: {stop_type}")
# print(f"a_time: {a_time}")

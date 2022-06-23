

t = { "value" : 3,
      "lvl" : 0,
     "children" : [
            { "value": 5,
               "lvl" : 1,
              "children": [
                    {"value":1,  "lvl" : 2, "children": []},
                    {"value": 4, "lvl" : 2, "children": []}
                ]
            },
        {"value":9, "lvl":1, "children": []},
        {"value":7, "lvl":1, "children": [
            {"value":8, "lvl":2, "children": []},
        ]},
    ]}
# # lvl = 0
# # tmpParent = self.parent
# # while tmpParent:
# #     lvl += 1
# #     tmpParent = tmpParent.parent

def getLvl():
    lvl = 0
    tmpChild = t.get("lvl")
    print("lvl",tmpChild)


def printTree(t):
    space = "\t" + " |___" * t["lvl"]
    if len(t["children"]) == 0:
        print(space ,t["value"])
    else:
        print(space ,t["value"])
        for child in t["children"]:
            printTree(child)




printTree(t)

fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)
# key
# data
# parrent

dict = {
    "root" : { "value": 0,
               "anak": { "img" : {
                                "value": "AKUIMAGE",
                                "anak": {
                                        "keyAnak1" : "valueAnak",
                                        "keyAnak2": "valueAnak",
                                        "keyAnak3": {}
                                        }
                                },
                        "doc" : {
                                "value": 1,
                                "anak": {
                                        "keyAnak1" : "valueAnak",
                                        "keyAnak2": "valueAnak",
                                        "keyAnak3": {}
                                        }
                                }
                        }
}
}

def create_node(value, parent):
    value = None
    anak = None
    parent = dict["root"]["anak"]["video"]

# lvl = 0
# dc = {}
# dc["root"] = {}
# dc["root"]["value"] = "iniroot"
# dc["root"]["anak"] = {}
# print(dc)
#
#
#
#
# print(dict)
# if len(dict) == 0: # cek apkah sudah ada root atau belum
#     print("lvl 0")
# else:
#     print(dict["root"]["anak"]["img"])
#


# def get_lvl():
#     lvl = 0
#     tmpParent = t["children"]
#
# def printTree(t):
#     lvl = 0
#     if len(t["children"]) == 0:
#         print(t["value"])
#         lvl = 1
#     else:
#         print(t["value"])
#         for child in t["children"]:
#             lvl += 1
#             # print("lvl ke", lvl)
#             printTree(child)
#
#
# # lvl = 0
# # tmpParent = self.parent
# # while tmpParent:
# #     lvl += 1
# #     tmpParent = tmpParent.parent
#
# printTree(t)

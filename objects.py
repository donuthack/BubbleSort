import random


#
# list = []
# for i in range(random.randint(0, 100)):
#     list.append({
#         "teatype": random.randint(1, 11),
#         "capacity": random.randint(250, 1000),
#         "water": random.randint(100, 1000)
#     })
# print(list)
#
# '''sort water from biggest to smallest'''
#
# # def getValue(list):
# #     return list['water']
# #
# #
# # list.sort(key=getValue, reverse=True)
# # print(list)
#
# '''teatype, capacity, water, list => return True or False in bool look using sort, decrease increase'''
#
#


''''''
def BubbleSort(array):
    for ind2, i in enumerate(array):
        for ind, j in enumerate(array):
            if len(array) - 1 == ind:
                break
            if array[ind2] < array[ind]:
                array[ind2], array[ind] = array[ind], array[ind2]
    return array


array = []
for i in range(random.randint(0, 20)):
    array.append(random.randint(0, 20))
print(array)

print(BubbleSort(array))

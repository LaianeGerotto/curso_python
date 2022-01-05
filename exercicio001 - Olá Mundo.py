# print("Olá Mundo!!")

# my_list = ['Mary', 'had', 'a', 'litle', 'lamb']
#
#
# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'
#
# print(my_list(my_list))
################################################
# dct = {'1': '2', '3': '1', '2': '3'}
# v = dct['3']
#
# for k in range(len(dct)):
#     v = dct[v]
#
# print(v)
###############################################
# def fun(inp=2, out=3):
#     return inp * out
# print(fun(out=2))

####################

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2
# print(fun(fun(2)))

################################################
# my_list = [x * x for x in range(5)]

# def fun(lst):
#     del lst[lst[2]]
#     return lst
#
# print(fun(my_list))

# my_list = [1,2]
#
# for v in range(2):
#     my_list.insert(-1, my_list[v])
#
# print(my_list)3

a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)
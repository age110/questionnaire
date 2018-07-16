from django.test import TestCase

# Create your tests here.
# temp = [
#     {"name":"a","age":20
#     },
#      {"name":"a","age":30
#     },
#      {"name":"a","age":25
#     }
# ]

# def list(temp):
#     return temp.sort(key=lambda x :x['age'])
# # # a = temp.sort(key=lambda x:x['age'])
# # # # list1 = map(lambda x:sorted('age'),temp)

# list(temp)
# print(temp)

# def shun_xu(list):
#     for i in range(len(list)-1): #控制循环次数
#         # 以此和后面的进行比较
#         for k in range(i+1,len(list)):
#             if list[i] > list[k]:
#                 list[i],list[k] = list[k],list[i]
#     return list

# list = [1,6,3,4,8,9,2]

# print(shun_xu(list))


# 将字符串转换成 abc,def,ghi变为 ihg,fed,cba
# str = 'abc,def,ghi'
# def index(str):
#     return str[::
# -1]
# print(index(str))
# print(index(str))

# def reverse_str(str):
#     order = []
#     for i in str:
#         order.append(i)
#     order.reverse()
#     return ''.join(order)
# print(reverse_str(str))
# reverse_str('abc,def,ghi')

# def del_list_same(list):
#     list1 = []
#     for i in list:
#         if i not in list1:
#             list1.append(i)
#     return list1

# print(del_list_same([1,9,6,4,5,7,8,6,4]))

# 连续字母与连续数字交替两次，字母长度与数字不限，列入
# abc123edfg45687 字符串变为：123abc45687defg


# import re
# string = 'abc123edfg45687'
# pattern = re.compile(r'([a-z]+)([0-9]+)')
# ret01 = pattern.findall(string)
# print(ret01)
# l=[]
# for i in ret01:
#     a = list(i)
#     a.reverse()
#     print(a)
#     for j in a:
#         l.append(j)
# print(''.join(l))


# n = 9
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()



# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{j}*{i}={}'.format(j,i,j*i),end=' ')
#     print()

# lt = [
#     {'name':'小王', 'age':18, 'info':[('phone', '123'), ('dizhi', '广州')]},
#     {'name':'小芳', 'age':19, 'info':[('phone', '789'), ('dizhi', '深圳')]},
#     {'name':'小杜', 'age':22, 'info':[('phone', '567'), ('dizhi', '北京')]},
#     {'name':'小孟', 'age':28, 'info':[('phone', '000'), ('dizhi', '上海')]},
#     {'name':'小乔', 'age':26, 'info':[('phone', '111'), ('dizhi', '河南')]},
# ]

# 打印结果
# for i in lt:
    
#     print('我叫{},今年{}岁,我来自{}'.format(i.get('name'),i.get('age'),i.get('info')[1][1]))


# def var_len_args(a, b, name='默认名称', *args, **kwargs):
#     print(a)
#     print(b)
#     print(name)
#     # args是一个元组，用来存放所有的多出来的位置参数
#     print(args)
#     # kwargs是一个字典，用来存放所有的多出来的默认参数
#     print(kwargs)

# var_len_args(1, 2, 3, 4, age=18) 

# def str(str_length=6):
#     import random
#     base = 'abcdefjhijklmnopqrstuvwsyz0123456789'
#     return ''.join(random.choice(base) for i in range(str_length))

# a = str(str_length=6)
# print(a)
# 先按accuracy_rate升序排序，如果accury_rate的值相同时按value降序排序

# data = [
#     {"name":"Linux", "value":12,"accuracy_rate":"44"},
#     {"name":"Windows", "value":21,"accuracy_rate":"76"},
#     {"name":"IOS", "value":60,"accuracy_rate":"44"},
#     {"name":"Android", "value":8,"accuracy_rate":"90"},
#     {"name":"OS X", "value":32,"accuracy_rate":"90"},
# ]


# data = select * from data order by accuracy_rate asc, value by value desc

# a = sorted(data,key = lambda x:x['accuracy_rate'])
# a.sort(key=lambda x:x["value"],reverse=True)

# print(a)
# def d_key(d):
#     if d['accuracy_rate'] == d['accuracy_rate']:
#         pass

# data.sort(key=lambda x:x["accuracy_rate"] if )

# data.sort(key=lambda x:x["value"],reverse=True)

# print(data)
# data.sort(key=lambda x:(int(x["accuracy_rate"]),-(x["value"])))
# print(data)

# import socket
# import time

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('10.8.159.15',9653))
# s.listen(2)
# conn, addr = s.accept()

# print('Got connection from:' addr)

# while 1:
#     data = conn.recv(1024)
#     print('Get data:' data)
#     if not data:
#         time.sleep(1)
#         break
#         conn.sendall('hello')

# conn.close()

'''
'''
# 斐波那契数列(1,1,2,3,5,8,13,21,34,...)

# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)


# print(fib(5))
# print(fib(6))
# print(fib(7))

# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(2))

# def model_dp(str1):
#     result=print(str1)
#     return result
# str1="hello World"
# model_dp(str1)
 
# def model_dp(str1):
#     result="hello world"
#     return result

# def model_dp(str1):

#     result= print(str1)

#     return result
# str1= ["Hello", "world"]
# model_dp(str1)
# import pandas as pd
# col=[102,30,40,50,54]
# col=col.apply(lambda x : int(x))
# print(col)

# col_str=["29",20.6,21,'sahoo']


# def string_treatment(col, decimals_round):
#     if col[0].isdigit():
#         col_val= col.apply(lambda x: int(x))
#         print(col_val)
#     elif col[0].replace(".", "", 1).isdigit():
#         col = col.apply(lambda x: float(x))
#         col = col.round(decimals_round)
    
#     return col
# string_treatment(col_str,4.6)

# add_dict={"name":"san","age":26,"keep":23}
# clean_result=add_dict[next(iter(add_dict))][1]
# print(clean_result)
# import datetime
# copy_pay={'payload0': {'week_end_date': '5/26/2018', 'sku': 'SS372C', 'account': 'Amazon-Proper'},'payload02':{'week_end': '10/26/2018', 'sku_id': 'SS372C', 'account_name': 'Amazon-Prop'}}

# for k,v in copy_pay.items():
#     for k1,v1 in v.items():
#         print(v1)
#         if isinstance(v1, datetime):
#             stay=copy_pay[k].update({k1: str(v1)})
#             print(stay)

# def ch_prime(n):
#     if n==1:
#         print('Next')
#     i=2
#     while i <= n/n :
#         if n/i ==0:
#             break
#         i+=1
#     return True
# ch_prime(7)          

# def show(num):
#     flag=False
#     if num > 1 :
#         for i in range(2,num):
#             if num % i == 0 :
#                 flag=True
#                 break
#     if flag:
#         print('Its not a prime number')
#     else:
#         print('Its a prime')
# show(27)


# def show_prime(num):
#     flag=True
#     if num==1:
#         return False
#     i=2
#     while i*i <=num:
#         if num % i ==0:
#             flag = False
#             break
#         i+=1
#     if flag:
#         print('Its prime number')
#     else:
#         print('Its not a prime')
# show_prime(8)

from asyncio import shield
from dis import dis
from inspect import stack
from re import T


# def show(num):
#     result=num*(num+1) // 2
#     print(result)
#     return result
# show(50)

# class Stack_use:
#     def __init__(self) -> None:
#         self.stack=[]
#     def add(self,dataval):
#         if dataval not in self.stack:
#             self.stack.append(dataval)
#             return True
#         else:
#             return False
#     def remove(self):
#         if len(self.stack) <= 0:
#             return ("There is no element")
#         else:
#             return self.stack.pop(0)
# Astack=Stack_use()
# Astack.add('mon')
# Astack.add('tue')
# Astack.add('wed')
# print(Astack.remove())
# print(Astack.remove())

# class Pop_ele:
#     def __init__(self) -> None:
#         self.pop_val=list()
    
#     def adding_ele(self,dataval):
#         if dataval not in self.pop_val:
#             self.pop_val.insert(0,dataval)
#             return True
#         else:
#             return False
#     def remove_ele(self):
#         if len(self.pop_val) < 0:
#             print('There is no element')
#         else:
#             return self.pop_val.pop()

# P=Pop_ele()
# P.adding_ele('sanjay')
# P.adding_ele('tue')
# P.adding_ele('wed')
# print(P.remove_ele())

# def show(n,i):
#     if ((n >> 1 ) & 1  == 1):
#         print('its set ')
#     else:
#         print('Its unset')
# print((29>>3) & 1)
# show(29,3)

from threading import *
import threading

# def disp_val():
#     for i in range(4):
#         print('Threads Are Running')

# t=Thread(target=disp_val)
# t.start()

# for i in range(4):
#     print('Things are different')


# class Hotel:
#     def __init__(self,t) -> None:
#         self.t=t
#     def food(self):
#         for i in range(1,5):
#             print(self.t,i)
# t1=Hotel('Take order from Table')
# t2 = Hotel('Serve order to table')
# t1=Thread(target=t1.food)
# t2=Thread(target=t2.food)
# t1.start()
# t2.start()

# def disp():
#     print("1st Thread is : ", current_thread().getName())
#     current_thread().setName('My Thread')
#     print('Set New Thread Name ' , current_thread().getName())

# t=Thread(target=disp)

# t.start()
# print("2nd Thread is : ", current_thread().getName())
# current_thread().setName('New Multi Thread')
# print('Set New Main Thread Name ' , current_thread().getName())

# def disp():
#     pass

# t=Thread(target=disp)
# print(t.getName())
# t.setName('Doc Thread')
# print('new',t.getName())

import requests
# headers = {
#   'Accept': 'application/json',
#   'X-ZAP-API-Key': 'API_KEY'
# } 
# r = requests.get ('https://randomuser.me/api/')
# print(r.text)

# r = requests.get ('https://randomuser.me/api/')
# print(r.text)

# apikey = request.ge


#!/usr/bin/env python
# A basic ZAP Python API example which spiders and scans a target URL

# import time
# from pprint import pprint
# from zapv2 import ZAPv2

# target = 'https://demo.testfire.net/'
# apikey = 'changeme' # Change to match the API key set in ZAP, or use None if the API key is disabled
# #
# # By default ZAP API client will connect to port 8080
# zap = ZAPv2(apikey=apikey)
# # Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
# # zap = ZAPv2(apikey=apikey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

# # Proxy a request to the target so that ZAP has something to deal with
# print('Accessing target {}'.format(target))
# zap.urlopen(target)
# # Give the sites tree a chance to get updated
# time.sleep(2)

# print('Spidering target {}'.format(target))
# scanid = zap.spider.scan(target)
# # Give the Spider a chance to start
# time.sleep(2)
# while (int(zap.spider.status(scanid)) < 100):
#     # Loop until the spider has finished
#     print('Spider progress %: {}'.format(zap.spider.status(scanid)))
#     time.sleep(2)

# print ('Spider completed')

# while (int(zap.pscan.records_to_scan) > 0):
#       print ('Records to passive scan : {}'.format(zap.pscan.records_to_scan))
#       time.sleep(2)

# print ('Passive Scan completed')

# print ('Active Scanning target {}'.format(target))
# scanid = zap.ascan.scan(target)
# while (int(zap.ascan.status(scanid)) < 100):
#     # Loop until the scanner has finished
#     print ('Scan progress %: {}'.format(zap.ascan.status(scanid)))
#     time.sleep(5)

# print ('Active Scan completed')

# # Report the results

# print ('Hosts: {}'.format(', '.join(zap.core.hosts)))
# print ('Alerts: ')
# pprint (zap.core.alerts())
from fpdf import FPDF

response = requests.get('http://localhost:8080/JSON/spider/view/fullResults/?apikey=o8eol4for0jmbtgh8tlq3530f3&scanId=https://demo.testfire.net/')
# print(response.json())
str_for=response.json()
print(str_for)
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=15)
# pdf.cell(2000, 10, txt = str_for,
#                  )
# output= pdf.output("Zap_Report.pdf")






























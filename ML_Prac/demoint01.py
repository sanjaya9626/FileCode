str_val = 's a n j a y'
spl_str=str_val.split()
i=0
emp_str=''
while i<len(spl_str):
    emp_str+=spl_str[i]
    i=i+2
output=''.join(emp_str)
print(emp_str)
from oops_and_sorting import count

# str_list='d2f3g4g5'
# emp_str=''
# for each in str_list:
#     if each.isalpha():
#         char_var=each
#     else:
#         int_var=int(each)
#         emp_str+=(char_var*int_var)
# print(emp_str)

# list1=[10,20,30,40,50,60,70]
# s=list1.index(10)
# print(s)

# spl_chr='s2d3f5g2'
# emp_str=''
# for each in spl_chr:
#     if each.isalpha():
#         emp_str+=each
#         str_val=each
#     else:
#         int_val=int(each)
#         new_char=chr(ord(str_val)+int_val)
#         emp_str += new_char
# print(emp_str)

#remove duplicate from given string
# str_lets='aaassssjjjsjsjsjsnnsns'
# emp_str=''
# for x in str_lets:
#     if x not in emp_str:
#         emp_str+=x
# print(emp_str)

#remove duplicate from given string
str1='sanjay kumar kumar sanjay sahoo sahoo'
spl_str=str1.split()
emp_str=''
for x in spl_str:
    if x not in emp_str:
        emp_str+=' '+x
print(emp_str.lstrip())
for ch in spl_str:
    print('{} occurs {} times'.format(ch, spl_str.count(ch)))

# a=[10,20,30,40,50]
# b=[10,20,30,40,50]
# print(a is b)
# c=a
# print(a is c)
# print(a==c)

# a=10
# b=20
# max_num=a if a >b else b
# print(max_num)

# import sys

# l={10,20,30,40,50,60}
# print(sys.getsizeof(l))

# str_input='one two three four five six'
# spl_chr= str_input.split()
# i=0
# emp_lis=[]
# while i < len(spl_chr):
#     if i % 2==0:
#         emp_lis.append(spl_chr[i])
#     else:
#         emp_lis.append(spl_chr[i][::-1])
#     i+=1
# print(emp_lis)


# str1='sanjaoiaaiiy'
# vowels=['a','e','i','o','u']
# emp_str=''
# for x in vowels:
#     if x in str1:
#         emp_str+=x
# for k in emp_str:
#     print(' {} occurs {} times '.format(k,str1.count(k)))
# print(emp_str)

# str1='sanjaoiaaiiy'
# vowels=['a','e','i','o','u']
# emp_dic={}
# for x in str1:
#     if x in vowels:
#         emp_dic[x]=emp_dic.get(x,0)+1
# for k,v in sorted(emp_dic.items()):
#     print(k ,'occur' ,v, 'times')


# squares={x*2:x*3 for x in range(1,10)}
# print(squares)

# def factorial(i):
#     if i==0:
#         result = 1
#     else: 
#         result = i*factorial(i-1)
#     return result
# print(factorial(5))

# list1=[10,20,30,40,50,60]
# list1.insert(len(list1)//2,10)
# print(list1)

# def show(num):
#     for x in range(2,num):
#         if x % 2==0:
#             yield x
# print(list(show(100)))

a={'m':2,'q':5,'w':8,'d':3}
# sort_val=dict(sorted(a.items(),reverse=False))
# print(sort_val)
# sort_key={key:val for key,val in sorted(a.items(),reverse=False)}
# print(sort_key)

# a={'m':2,'q':5,'w':8,'d':3}
# sortbyval={k:v for k,v in sorted(a.items(),key=lambda v : v[1],reverse=False)}
# print(sortbyval)

# class portal():
#     def __init__(self):
#         self.__name=''
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,val):
#         self.__name=val
# p=portal()
# p.name='geeksforgeeks'
# print(p.name)


temp=[1,2,3,4,5,6,7,8,9,10]
# even_num= list(filter(lambda  x: x%2==0,temp))
# print(even_num)

# square=list(map(lambda x : x*2,temp))
# print(square)

# square=[x for x in temp if x %2 ==0]
# print(square)

# from itertools import combinations

# s=[1,2,3,4,5]
# def show(arr,r):
#     return combinations(arr,r)
# print(list(show(s,2)))

# lis=['ram','shyam','mohan']
# print(lis[-2][2])

# arr=['sanjay kumar sahoo']
# str_ltr=[x[:-3] for x in arr]
# print(str_ltr)

# list_sort=["1","3","9","6","5"]
# sorted_list=sorted(list_sort,reverse=False)
# print(sorted_list)

# lst=[(a,b) for a in range(3) for b in range(a)]
# print(lst)

# li=('even','odd','even','odd','even','odd','even')
# ev=[]
# od=[]
# for x in range(len(li)):
    
#     if li.count(li[x])%2!=0:
#         od.append(li[x])
# print(od)

# def outer(fun):
#     def inner(a,b):
#         if a> b:
#             return a+b
#         else:
#             fun(a,b)
#     return inner
# @outer
# def sub(a,b):
#     return a-b
# print(sub(5,10))

# def fibo(n):
#     if n<=1:
#         return 1
#     else:
#         return (fibo(n-1)+fibo(n-2))
# n=10
# for x in range(n):
#     print(fibo(x))

# def recur_fibo(n):
#     if n<=1:
#         return 1
#     else:
#         return (recur_fibo(n-1)+recur_fibo(n-2))
# n=10
# for x in range(n):
#     print(recur_fibo(x))

# def missing(arr):
#     size=len(arr)
#     missing_form=(size+1)*(size+2)//2
#     total_sum=sum(arr)
#     miss_num=missing_form-total_sum
#     return miss_num
# arr=[1,2,3,5,6,7]
# print(missing(arr))

# dict1={9:[2,11,7,15]}
# ky=0
# for x in dict1:
#     ky=x
# val=dict1[ky]

# for ch in val:
#     for each in range(1,len(val)):
#         if ch+val[each]== ky:
#             print(val.index(ch),val.index(val[each]))

# emp_dict={}
# a={100:'sanjay',200:'kumar',300:'sahoo',400:'Natia',500:'batia'}
# for x in a.keys():
#     emp_dict[x]=emp_dict.get(x,0)+1
# for k,v in emp_dict.items():
#     print(k,'occurs',v, 'times')
# print(emp_dict)

# pyth='aaaannnbbbvvv'
# emp_dict={}
# for each in pyth:
#     emp_dict[each]=emp_dict.get(each,0)+1
# for k,v in emp_dict.items():
#     print(k,'occurs',v,'times')
# print(emp_dict)

# test_dict = {'gfg' : [5, 6, 7, 8],
#               'is' : [10, 11, 7, 5],
#               'best' : [6, 12, 10, 8],
#               'for' : [1, 2, 5]}
# sorted_list=list(sorted(ele for x in test_dict.values() for ele in x))
# print(sorted_list)

# test_dict = {"Arushi" :22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
# sort_dict={x:y for x,y in test_dict.items() if x!="Mani"}
# print(sort_dict)

# lis = {{ "name" : "Nandini", "age" : 20},
# { "name" : "Manjeet", "age" : 20 },
# { "name" : "Nikhil" , "age" : 19 }}

# sort_dict=sorted(lis,key= lambda i : (i['name'],i['age']))
# print(sort_dict)

# dict6 = {'a': 10, 'b': 8}
# dict7 = {'d': 6, 'c': 4}
# dict8={'e':3,'f': 7}

# def dictio(dic1,dic2,dic3):
#     res={**dic1,**dic2,**dic3}
#     return res
# print(dictio(dict6,dict7,dict8))

# test_dict = {'month' : [1, 2, 3],
#               'name' : ['Jan', 'Feb', 'March']}
# res_dict=dict(zip(test_dict['month'],test_dict['name']))
# print(test_dict)

# test_dict = {"Gfg" : 1, "is" :  3, "Best" : 2}
# res=list(test_dict.keys())+list(test_dict.values())
# print(res)

# test_dict = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
# res=dict()
# for i in sorted(test_dict):
#     res[i] = sorted(test_dict[i])
# print(res)

# test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
# lis=[]
# emp_dic=dict()
# for key,val in test_dict.items():
#     if val not in lis:
#         lis.append(val)
#         emp_dic[key]=val
# print(emp_dic)

# list1=['sanjay','kumar','sukesh','mukesh','ravi','mohan']
# list2=['ram','shyam','sanjay','mukesh','ravi','sahoo','rrr']

# def show(list1,list2):
#     for each in list1:
#         if each in list2:
#             return ''.join(list(each))
# print(show(list1,list2))

# input_list=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1]
# from collections import Counter
# res=Counter(input_list)
# print(res)

# pali_str='sanjay'
# emp_str=''
# for x in pali_str:
#     emp_str=x+emp_str
# if emp_str==pali_str:
#     print('Its a palindrom')
# else:
#     print("Its not a palindrom")

# list=["Gfg is True","Gfg will Return",
#       "its A global win","try Gfg"]
# emp_list=[]
# for x in list:
#     for ele in x.split():
#         if keyword.iskeyword(ele):
#             emp_list.append(ele)
# print(emp_list)

# list=["Gfg is True","Gfg will Return",
#       "its A global win","try Gfg"]

# sort_keyword=[ele for x in list for ele in x.split() if keyword.iskeyword(ele)]
# print(sort_keyword)

# max_num=lambda a ,b : a if a>b else b
# print(max_num(10,5))

# s='sanjay'
# i=0
# for x in s:
#     print('The element at positive index at {} and -ve index at {}'.format(i,(i-len(s))))
#     i=i+1

# emp_str=''
# spl_str=s.split()
# for x in spl_str:
#     emp_str=emp_str+x[::-1]
# print(emp_str)

# emp_str=''
# spl_str=s.split()
# for x in spl_str:
#     emp_str=emp_str+' '+x[::-1]
# print(emp_str)

# str1='sanjay kumar'
# spl_str=str1.split()
# emp_str=''
# i=len(str1)-1
# while i>=0:
#     emp_str=emp_str+str1[i]
#     i=i-1
# print(emp_str)

# content='Sanjaya kumar sahoo'
# sub_content='sahoo'
# try:
#     print(content.index('sub_content'))
# except ValueError:
#     print('Substring Not found')
# else:
#     print('Substring Found')

# s='sanjay + kumar + sahoo' 
# spl_chr=s.split('+')
# print(spl_chr)

# sum=0
# matcher=re.finditer('sa','sasasasanansnansasa')
# for each in matcher:
#     sum=sum+1
#     print(each.start(),'.....',each.end(),'....',each.group())
# print('The number of occurence is',sum)

# import re
# matcher=re.finditer("x","a7b@k9z")
# for match in matcher:
#     print(match.start(),"......",match.group())

# class Test:
#     x=10
#     _y=20
#     __z=30
#     def m1(self):
#         print(Test.x)
#         print(Test._y)
#         print(Test.__z)
# t=Test()
# t.m1()

# words=['sanjay','kumar','sahoo','python']
# s1=[w[0] for w in words]
# print(s1)

# emp_lis=[]
# def fifo(arr):
#     for x in arr:
#         if emp_lis.append(x)==emp_lis.pop(arr[x][-1]):
#             print('Its valid')
#         else:
#             print('Its not valid')
# f=fifo('{ [ < >] }')

# words = "the quick brown fox jumps over the lazy dog"
# spl = words.split()
# link = [[w.upper(),len(w)] for w in spl]
# print (link)

# str1='sanjay'
# list_comp = [x for x in range(len(str1)-1) str1[x].lower if x %2==0 else str1[x] ]
# print(list_comp)

# s='durga'
# int_ans=s[::-1]
# print(int_ans) 

# str_01='durga'
# j=reversed(str_01)
# jon_num=''.join(j)
# print(jon_num)

# str_list='Durga sofware solution'
# spl_word=str_list.split()
# emp_li=[]
# for each in spl_word:
#     emp_li.append(each[::-1])
# join_spl=' '.join(emp_li)
# print(join_spl)

# num_list='one two three four five six'
# spl_list= num_list.split()
# emp_str=''
# for each in range(len(spl_list)):
#     if each%2==0:
#         emp_str=emp_str+spl_list[each]+' '
#     else:
#         emp_str=emp_str+spl_list[each][::-1]+' '
# print(emp_str)

# list1=[10,9,23,43,8]
# for each in range(len(list1)-1):
#     for every in range(len(list1)-1):
#         if list1[every]>list1[every+1]:
#             list1[every],list1[every+1]=list1[every+1],list1[every]
# print("sorted list :",list1)

# list1=[10,9,23,43,8,8]
# print(list1)
# for each in range(len(list1)):
#     min_val=min(list1[each:])
#     min_val_ind=list1.index(min_val,each)
#     list1[each],list1[min_val_ind]=list1[min_val_ind],list1[each]
# print(list1)

# a=10
# b=10
# b=a
# a=99
# print(a)
# print(b)
# import copy
# nos=[[10,20],[30,40],50]
# val=copy.deepcopy(nos)
# print(nos)
# print(val)
# nos[1][1]=99
# print(nos)
# print(val)

# import pickle
# idno=100
# name='sanjay'
# age=87
# fo=open('myscore.txt','wb') 
# pickle.dump(idno,fo)
# pickle.dump(name,fo)
# pickle.dump(age,fo)
# fo.close()
# print('Data written to file')

# file=open('myscore.txt','rb')
# id=pickle.load(file)
# name=pickle.load(file)
# age=pickle.load(file)
# print(id,name,age)
# file.close()

# with open('openfile.txt','w') as file:
#     file.write('This is a good boy')
#     file.close()
#     print('File written')

# with open('openfile.txt','r') as file :
#     for word in file:
        
#         for each in word.split():
#             print(each)

# file=open('openfile.txt','r')
# while 1:
#     char = file.read(1)

#     if not char:
#         break
#     print(char)

# file.close()
# import json
# details_id={'Coin':'H',
#             'Coin':'T',
#             'Coin':'H',
#             'Coin':'H',
#             'Coin':'H',
#             'Coin':'T',
#             'Coin':'H',
#             'Coin':'T',
#             'Coin':'H',
#             'Coin':'H'}

# with open('smell.txt','w') as file:
#     for key,value in details_id.items():
#         file.write('%s:%s\n' % (key,value))
#     file.close()
#     print('Word written successfully')
# dict_obj=dict()
# for res in file:
#     res.strip()
#     res.lower()
#     res.split()

# for line in res:
#     if line in dict_obj:
#         dict_obj[line] = dict_obj[line]+1
#     else:
#         dict_obj[line] = 1
# file.close()

# for key in list(dict_obj.keys()):
#     print("The count of {} is {} ". format(key,dict_obj[key]))


sort_dict={"name": "Nandini", "age": 20}
    #    {"name": "Manjeet", "age": 20},
    #    {"name": "Nikhil", "age": 19}]

# print(sorted(sort_dict, key=itemgetter('age')))

# sort_val= sorted(sort_dict, key= lambda val :val['name'],reverse=False)
# print(sort_val)

coin_dict= {'Cpin':'H','Coin':'T'}

# def merge(dict1,dict2):
#     return dict2.update(dict1)

# print(merge(sort_dict,coin_dict))
# print(coin_dict)

# def merge(dict1,dict2):
#     res={**dict1,**dict2}
#     return res
# print(merge(sort_dict,coin_dict))

# test_dict = {'month' : [1, 2, 3],
#              'name' : ['Jan', 'Feb', 'March']}
# flat_dic=dict(zip(test_dict['month'],test_dict['name']))
# print(flat_dic)

# from ast import pattern
# from collections import OrderedDict
# import imp
# from tkinter.messagebox import NO

# original_dict = {'akshat':1, 'manjeet':2}
# inorder_dict= OrderedDict([('akshat',1),('nikhil', 2)])

# inorder_dict.update({'manjeet':'3'})
# inorder_dict.move_to_end('manjeet',last=False) 
# print(str(inorder_dict))

# test_dict={5 : 'sahoo', 4 : 2, 8 : 3}
# ans=list(test_dict.keys())+list(test_dict.values())

# print(ans)

# test_dict={5 : 'sahoo', 4 : 2, 8 : 3}
# print(sorted(test_dict.keys()))

# test_dict = {'gfg': [7, 6, 3], 
#              'is': [2, 10, 3], 
#              'best': [19, 4]}
# res=dict()
# for key in sorted(test_dict):
#     res[key]=sorted(test_dict[key])

# print(res)

# d = { 'a' : 1 , 'b' : 2 }
# print(d.get('a','notfound'))

# arr = ['cat', 'dog', 'tac', 'god', 'act']


# def allAnagram(input):
#     dict={}
#     for call in input:
#         key = ''.join(sorted(call))

#         if key in dict.keys():
#            dict[key].append(call)
#         else:
#             dict[key]=[]
#             dict[key].append(call)
#     output=''
#     for key,val in dict.items():
#         output=output+''+''.join(val)+' '
#     return output
# if __name__=="__main__":
#     input = ['cat', 'dog', 'tac', 'god', 'act']
#     print(allAnagram(input))

# tuple_item=[('A', 1), ('B', 2), ('C', 3)]

# def convert(tup,di):
#     for a,b in tup:
#         di.setdefault(a,[]).append(b)

#     return di
# dic={}
# print(convert(tuple_item,dic))

# input = 'Geeks for Geeks'
# def sharp(input):
#     input=input.split()
#     uniqw= Counter(input)
#     ser=' '.join(uniqw.keys())
#     print(ser)
# sharp(input)

# def disp(input):
#     for x in range(0,input):
#         if x %2 ==0:
#             yield x
# even=disp(10)
# print(next(even))
# print(next(even))
# print(next(even))
# print(next(even))

# od=list(even)
# print(type(od))
# print(even)
# for y in od:
#     print(y)

# def show(a,b):
#     while a<=b:
#         yield a
#         a+=1
# s=show(1,5)
# print(next(s))
# print(next(s))
# print(next(s))

# my_list=[10,20,30,40,50]
# os=iter(my_list)
# while True:
#     try:
#         print(next(os))
#     except StopIteration:
#         break

# def fibo():
#     a , b=0,1
#     while True:
#         yield a
#         a ,b=b,a+b
# for x in fibo():
#     if x <100:
        
#         print(x)

# charac='python_laptop'
# spl_chr=charac.split('_')
# emp_lis=[]
# for x in spl_chr:
#     emp_lis.append(x[::-1])
#     output=' '.join(emp_lis)
# print(output)

# import re
# count=0
# matcher=re.finditer('ab','ababababaa')
# for ex in matcher:
#     print('start :{},end:{},group:{}'.format(ex.start(),ex.end(),ex.group()))
#     count+=1
# print(count)

# match_item=re.finditer('a$','abaabababa')
# for ex in match_item:
#     print(ex.start(),'............',ex.group())

# pattern=re.findall('[\W]','abc2ds35&era')
# print(pattern)

# pattern = re.split(' ','sahoosanjayakumar096@gmail.com')
# for x in pattern:
#     print(x)

# str_1st=input('Enter the identifiers to validate : ')
# pattern=re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',str_1st)
# if pattern !=None:
#     print(str_1st,'Is the valid identifiers')
# else:
#     print(str_1st,'Is not a valid identifiers')

# mob_num= input('Enter your mobile num : ')
# pattern=re.fullmatch('[6-9]\d{9}',mob_num)
# if pattern!=None:
#     print('This is valid mobile number')
# else:
#     print('Ths is not a valid mob number')

# class Author:
#     def __init__(self,sales,quantity) -> None:
#         self.sales=sales
#         self.quantity=quantity
    
#     def show(self,name,age):
#         self.name=name
#         self.age=age
# class Company(Author):
#     def __init__(self, sales, quantity,owner) -> None:
#         super().__init__(sales, quantity)
#         self.owner=owner
#     def show(self,name,age):
#         super().show(name,age)
#     def display(self):
#         print('The number of sales is:',self.sales)
#         print('The Quantity is:',self.quantity)
#         print('The name of author is',self.name)
#         print('The age of the author is ',self.age)
#         print('The company owner name is ',self.owner)
# c=Company(120,2,'kumar')
# c.show('sanjay',26)
# c.display()

# class Proper:
#     a=10
#     def __init__(self) -> None:
#         self.b=20
#     @classmethod
#     def class_method(cls,name):
#         cls.name=name
#     @staticmethod
#     def static_method():
#         age=26
        
# class Display(Proper):
#     def __init__(self,title,name) -> None:
#         super().__init__()
#         self.title=title
#         super().class_method(name)
#         super().static_method()
#         print(super().a)
#     def display_details(self):
#         print('The name of your employee is:' ,Display.name)
#         print('The title of your employee is',self.title)

# d=Display('sahoo','sanjay')
# d.display_details()

# class A:
#     @staticmethod
#     def m1():
#         print('This is static class')
# class B(A):
#     @staticmethod
#     def m2():
#         super(B,B).m1()
# a=B()
# a.m2()

from abc import ABC, abstractmethod

# class Test:
#     @abstractmethod
#     def m1(self):
#         print('Sarbratra,sarbada,sarbasreshta')
# t=Test()
# t.m1()

# class Test(ABC):
#     def m1():
#         pass
# t=Test()

# class DBInterface(ABC):
#     @abstractmethod
#     def connect():
#         pass  
#     @abstractmethod
#     def disconnect():
#         pass
# class Oracle(DBInterface):
#     def connect(self):
#         print('Connecting to oracle database')
#     def disconnect(self):
#         print('Disconnecting from oracle database')
# class Sybase(DBInterface):
#     def connect(self):
#         print('Connecting to sybase database')
#     def disconnect(self):
#         print('Disconnecting from Sybase database')
# Dbname=input('Enter your db name:' )
# classname=globals()[Dbname]
# x=classname()
# x.connect()
# x.disconnect()

# class Test:
#     x=10
#     _y=20
#     __z=30
#     def m1(self):
#         print(Test.x)
#         print(Test._y)
#         print(Test.__z)
# t=Test()
# t.m1()

# class Test:
#     _x=20
#     def m1(self):
#         pass
# t=Test()
# print(t._Test__x)






print('sanjay')

































































































































































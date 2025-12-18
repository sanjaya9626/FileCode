#define fibonacci series using

# def fibo():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for x in fibo():
#     if x <100:
#         print(x)

# reverse the character using while loop
# charac='python_laptop'
# emp_str=''
# word=len(charac)-1
# while word>=0:
#     emp_str=emp_str+charac[word]
#     word-=1
# print(emp_str)
#
#reverse the string

# string='sanjay'
# rever_char=reversed(string)
# output=''.join(rever_char)
# print(output)

#reverse the character
# s='sanjaykumar'
# split_char=s.split()
# emp_lis=[]
# for x in split_char:
#     emp_lis.append(x[::-1])
# print(emp_lis)
# output=''.join(emp_lis)
# print(output)

# #wrong programme
# str_lets='kumarsanjay'
# spl_str=str_lets.split()
# even=[]
# odd=[]
# i=0
# while i<len(spl_str):
#     if i %2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

#findout even position value
# s = 'san kum sah kus ctc ods'
# spl = s.split()
# i=0
# p=''
# while i<len(spl):
#     p=p+spl[i]
#     i=i+2
# output=''.join(p)
# print(output)

#to findout even postion letter
# s='s a n j a y k u m a r'
# spli_lets=s.split()
# emp_str=''
# i=0
# while i<len(spli_lets):
#     emp_str+=spli_lets[i]
#     i=i+2
# output=''.join(emp_str)
# print(output)

#findout even postion value
# s='sanjay'
# emp_str=''
# i=1
# while i <len(s):
#     emp_str+=s[i]
#     i+=2
# print(emp_str)

#convert this string into full string
# str1='f2r3t1y6'
# emp_str=''
# for x in str1:
#     if x.isalpha():
#         alpha_char=x
#     else:
#         int_char=int(x)
#         emp_str=emp_str+(alpha_char*int_char)
# print(emp_str)

#give the string of given number present in below string
# spl_chr='s2d3f5g2'
# emp_str=''
# for x in spl_chr:
#     if x.isalpha():
#         emp_str=emp_str+x
#         st_value=x
#     else:
#         int_val=int(x)
#         newchar=chr(ord(st_value)+int_val)
#         emp_str=emp_str+newchar
# print(emp_str)
#
#
# s='aaaaaasssssffffgggg'
# emp_str=''
# for x in s:
#     if x not in emp_str:
#         emp_str+=x
# print(emp_str)

# str1='sanjay kumar kumar sanjay sahoo sahoo'
# spl_str=str1.split()
# emp_str=''
# for each in spl_str:
#     if each not in emp_str:
#         emp_str+=each
# print(emp_str)

# s='sssdddffffrrrewww'
# set1=set(s)
# output=''.join(set1)
# print(output)

# str1='aaaaddddfffffgggg'
# emp_str=''
# for ch in str1:
#     if ch not in emp_str:
#         emp_str+=ch
# for ch in emp_str:
#     print('{} occurs {} times'.format(ch,str1.count(ch)))
#
# dic={'a':100,'b':200,'c':400,'d':900}
# dic['e']=760
# print(dic)
# print(dic.get('k',1000))
# print(dic)

# dic['a']=dic.get('a',3999)+30
# print(dic)
#
# for k,v in dic.items():
#     print(k,v)

# a=[10,20,30,40,50]
# b=[10,20,30,40,50]
# print(a is b)
# c=a
# print(a is c)
# print(a==c)

# a=10
# b=20
# max=a if a >b else b
# print(max)

# a=input("Enter 1st Number")
# b=input('Enter Second Number')
# c=input('Enter Third Number')
#
# maxavlue=a if a>b and a>c else  b if b>c else c
# print('biggest number is ',maxavlue)
#
# import sys

# l={10,20,30,40,50,60}
# print(sys.getsizeof(l))
# import keyword
# import pickle
# import re
# import time

list1=[10,20,30,40,50,60,70,80]
list2=[29,39,94,59,69,79,89,34]
#
# # s1=list(map(lambda x : x*2 ,list1))
# # print(s1)
#
# s2=list(map(lambda x,y : x+y+5,list1,list2))
# print(s2)
#
# l1=[20,50,60,70,26,54,80,98,97]
# s2=list(filter(lambda n : n>70,l1))
# for x in s2:
#     print(x)
#
# from functools import reduce
#
# l1=[20,50,60,70,26,54,80,98,97]
# s2=reduce(lambda m,n : m+n,l1)
# print(s2)

# s='sanjay kumar sahoo'
# spl_chr=s.split()
# emp_lis=[] 
# for x in spl_chr:
#     emp_lis.append(x[::-1])
# output=' '.join(emp_lis)
# print(output)
#
s1='sanjay kumar sahoo'
spl_chr=s1.split()
emp_str=''
i=len(spl_chr)-1
while i>=0:
    emp_str=emp_str+spl_chr[i]
    i=i-1
output=''.join(emp_str)
print(output)

# def reverse(str1):
#     emp_str=''
#     for ch in str1:
#         emp_str=ch+emp_str
#     return emp_str
# str2='sanjaykumar'
# print('The reverse function is',reverse(str2))
#
# reverse all odd position string value 
# str_input='one two three four five six'
# str_spl=str_input.split()
# emp_lis=[]
# count=0
# while count <len(str_spl):
#     if count%2==0:
#         emp_lis.append(str_spl[count])
#     else:
#         emp_lis.append(str_spl[count][::-1])
#     count+=1
# for_join=' '.join(emp_lis)
# print(for_join)

# findout the number of vowel present in the given string
# str1='sanjaoiaaiiy'
# vowels=['a','e','i','o','u']
# emp_dic={}
# def show(s,v):
#     for x in s:
#         if x in v:
#             emp_dic[x]=emp_dic.get(x,0)+1
#     for k,v in sorted(emp_dic.items()):
#         print(k,' occurs' ,v ,'times')
# show(str1,vowels) 
#
#multiply value of specific dictionary
# squares={x:x*3 for x in range(1,10)}
# print(squares)

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         result=n* factorial(n-1)
#     return result
# sum=5
# print('The Factorial is ',factorial(sum))

#INSERT A ELEMENT IN THE MIDDLE OF A LIST
# list1=[10,20,30,40,50,60]
# list1.insert(len(list1)//2,10)
# print(list1)

#find out even number upto 100
# def show(num):
#     for x in range(2,num):
#         if x %2==0:
#             yield x
# print(list(show(100)))
#
a={'m':2,'q':5,'w':8,'d':3}
# sort_val = dict((sorted(a.items(),reverse=False)))
# print(sort_val)
# sort_key={key:val for key,val in sorted(a.items(),reverse=True)}
# print(sort_key)

# sortybyval={k:v for k,v in sorted(a.items(),key=lambda v : v[1],reverse=True)}
# print(sortybyval)
#
s='lenovolaptop'
ans=s[-3:]
print(ans)

# length=len(s)
# obj=s[length-3]
# print(obj)

# def index(s, sub):
#     start = 0
#     end = 0
#     while start < len(s):
#         if s[start+end] != sub[end]:
#             start += 1
#             end = 0
#             continue
#         end += 1
#         if end == len(sub):
#             return start
#         return -1

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
# even_num=list(filter(lambda n : n%2==0 ,temp))
# print(even_num)
#
# squre=list(map(lambda x : x**2 ,temp))
# print(squre)
#
# square= [x**2 for x in range(1,10)]
# print(square)
#
# even_num=[x for x in range(10) if x %2==0]
# print(even_num)
#
# from itertools import combinations
# s=[1,2,3,4,5]
# def show(arr,r):
#     return combinations(arr,r)
# print(list(show(s,2)))

# lis=['ram','shyam','mohan']
# print(lis[-2][2])

# emp_dic=dict()
# def store_val(arr):
#     even=[]
#     odd=[]
#     for x in range(arr):
#         if x %2==0:
#             even.append(x)
#         else:
#             odd.append(x)
#     emp_dic=tuple(even)
#     emp_dic=tuple(odd)
# store_val(10)
# print(emp_dic)
#
# arr=['sanjay kumar sahoo']
# sp=[x[:-3] for x in arr]
# print(sp)

# list1 = ["1", "4", "0", "6", "9"]
# sort_lis=sorted(list1,reverse=True)
# print(sort_lis)
#store even num and num in dic ?


# def add(fun):
#     def inner(a,b):
#         fun()
#         return a+b
#     return inner
# @add
# def sub(a,b):
#     return a-b
# sub(5,4)

# a=[1,3,5]
# mul=(lambda x,y,z:x*y*z)
# print(mul)
#
# lst = [(a,b) for a in range(3) for b in range(a)]
# print(lst)

# li=('even','odd','even','odd','even','odd','even')
# ev=[]
# od=[]
# for x in range(len(li)):
#     if li.count(li[x])%2!=0:
#         od.append(li[x])
# print(od)
#
def outer(func):
    def inner(a,b):
        if a>b:
            return a-b
        else:
            func(a,b)
    return inner
@outer
def show(a,b):
    return a+b
# print(show(5,1))
#
# def recur_fibo(n):
#     if n<=1:
#         return 1
#     else:
#         return (recur_fibo(n-1)+recur_fibo(n-2))
# n=10
# for x in range(n):
#     print(recur_fibo(x))

# def miss_num(A):
#     n=len(A)
#     miss_form=(n+1)*(n+2)//2
#     total_sum=sum(A)
#     missing_number=miss_form-total_sum
#     return missing_number
# A=[1,2,3,4,6,7]
# print(miss_num(A))

# dict1={9:[2, 7, 11, 15]}
# target = 9

# ky=0
# for x in dict1:
#     ky=x
# val=dict1[ky]
#
# for ch in val:
#     for ev in range(1,len(val)):
#         if ch+val[ev]==ky:
#             print(val.index(ch),val.index(val[ev]))

# class a():
#     def show(self):
#         print('This is a ')
# class b(a):
#     def show1(self):
#         print('This is b')
# class c(b):
#     def show2(self):
#         print('This is c')
#
# c1=c()
# c1.show()
# c1.show1()
# c1.show2()

# def fibo_func(n):
#     if n<=1:
#         return 1
#     else:
#         return (fibo_func(n-1)+fibo_func(n-2))
# n=10
# for x in range(n):
#     print(fibo_func(x))

# list1=[10,3,76,54,31,9]
# print('The unsortedlist',list1)
# def show(arr):
# num=[10,3,76,54,31,9]
# for each in range(len(num)-1):
#     for every in range(len(num)-1):
#         if num[every]>num[every+1]:
#             num[every],num[every+1]=num[every+1],num[every]
# print(num)
#
# s={100:'sanjay',200:'kumar',300:'sahoo',400:'Natia'}
# # s.clear()
# # del s[300]
# print(s)
#
# a={100:'sanjay',200:'kumar',300:'sahoo',400:'Natia',500:'batia'}
# print(a.popitem())
#
# print(a.setdefault(600,'python'))
# print(a)
# s1={'a':10,'b':20}
# sum=0
# for x in s1.values():
#     sum=sum+x
# print(sum)
#
# #reverse The order of the string not the character
# str1='Sanjay kumar sahoo'
# split_str=str1.split()
# emp_str=''
# for each in split_str:
#     emp_str=each+' '+emp_str
# print(emp_str)
#
# emp_dict={}
# a={100:'sanjay',200:'kumar',300:'sahoo',400:'Natia',500:'batia'}
# for s in a.keys():
#     emp_dict[s]=emp_dict.get(s,0)+1
# for k,v in emp_dict.items():
#     print(k ,'occurs', v,'times')
# b=emp_dict.copy()
# print(b)
# print(emp_dict)
# print(id(b))
# print(id(emp_dict))

# l='aaaannnbbbvvv'
# emp_dic={}
# for x in l:
#     emp_dic[x]=emp_dic.get(x,0)+1
# for k,v in emp_dic.items():
#     print(k,'Occurs',v,'times')
#
test_dict = {'gfg' : [5, 6, 7, 8],
              'is' : [10, 11, 7, 5],
              'best' : [6, 12, 10, 8],
              'for' : [1, 2, 5]}
#
# u_values=list(sorted({ele for x in test_dict.values() for  ele in x}))
# print(u_values)
#
# test_dict = {"Arushi" :22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
# new_dict={key:val for key,val in test_dict.items() if key!="Mani"}
# print(new_dict)

lis = {{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }}

# sort_lis=sorted(lis,key=lambda i : (i['age'],i['name']))
# print(sort_lis)

# dict6 = {'a': 10, 'b': 8}
# dict7 = {'d': 6, 'c': 4}

# def dictio(dict1,dict2):
#     res={**dict1,**dict2}
#     return res
# print(dictio(dict6,dict7))
#
# test_dict = {'month' : [1, 2, 3],
#               'name' : ['Jan', 'Feb', 'March']}
#
# res_dict=dict(zip(test_dict['month'],test_dict['name']))
# print(res_dict)
#
# test_dict = {"Gfg" : 1, "is" :  3, "Best" : 2}
# output:['Gfg', 'is', 'Best', 1, 3, 2]
# res=list(test_dict.keys())+list(test_dict.values())
# print(res)

# test_dict = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
# res=dict()
# for i in sorted(test_dict):
#     res[i]=sorted(test_dict[i])
# print(res)
#
# test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
# lis=[]
# emp_dic=dict()
# for key,val in test_dict.items():
#     if val not in lis:
#         lis.append(val)
#         emp_dic[key]=val
# print(emp_dic)
#
# list1=['sanjay','kumar','sukesh','mukesh','ravi','mohan']
# list2=['ram','shyam','sanjay','mukesh','ravi','sahoo','rrr']

# def common(m,n):
#     for each in list1:
#         if each in list2:
#             return ''.join(list(each))
# print(common(list1,list2))
#
# dict1=[("akash", 10), ("gaurav", 12), ("anand", 14),
#          ("suraj", 20), ("akhil", 25), ("ashish", 30)]

# dic={}
# def common(tup,dict_obj):
#     for key,val in tup:
#         dict_obj.setdefault(key,val)
#     return dict_obj
# print(common(dict1,dic))
#
# input_list=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1]
# from collections import  Counter
# c=Counter(input_list)
# print(c)
#
# test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
#
# emp_dic={}
# def threat(test_dict,dic):
#     for key,val in test_dict.items():
#         emp_dic.setdefault(val,key)
#     return  emp_dic
# print(threat(test_dict,emp_dic))
#
# pali_str='malayalam'
#
# emp_lis=''
#
# for x in pali_str:
#     emp_lis=x+emp_lis
# if emp_lis==pali_str:
#     print('Its A palindrom')
# else:
#     print('Not Palindrom')

# from collections import defaultdict
# str1='sanjaykumar'
# d=defaultdict(lambda:2)
# for c,e in str1:
#     d.setdefault(c)
# print(d)

# list1=['sanjay','kumar','sukesh','mukesh','ravi','mohan']
# list2=['ram','shyam','sanjay','mukesh','ravi','sahoo','rrr']
# list_comp=[x for x in list1 if x not in list2]
# print(list_comp)
#
# test_dict = {'gfg' : [1, 2, 3], 'is' : [1, 4], 'best' : [4, 2]}

# from collections import defaultdict
# res=defaultdict(list)
# for key, val in test_dict.items():
#     for ele in val:
#         res[ele].append(key)
# print(res)

# test_dict = {'gfg' : [1, 2, 3], 'is' : [1, 4], 'best' : [4, 2]}
# res=dict()
# for key in  test_dict:
#     res[key]=sorted(test_dict[key])
# print(res)

# def gene(num):
#     while num >0:
#         yield  num
#         num=num-1
# gen=gene(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for x in gen:
#     print(x)

# lis=[x*x for x in range(30) ]
# print(lis)
#
# list=["Gfg is True","Gfg will Return",
#       "its A global win","try Gfg"]

# emp_lis=[]
# for x in list:
#     for y in x.split():
#         if keyword.iskeyword(y):
#             emp_lis.append(y)
# print(emp_lis)

# lis_comp=[ele for x in list for ele in x.split() if keyword.iskeyword(ele)]
# print(lis_comp)
#
# def exceptt():
#     try:
#         print(10/0)
#     except (ZeroDivisionError ,ValueError) as msg:
#         print('The Above exception is ',msg)
# print(exceptt())
#
# print('stmnt-1')
# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print('Zero is not divisible by ',msg)
#     print(10/2)
#     print('stmnt-3')

# class  TooYoungException(Exception):
#     def __init__(self,arg):
#         self.msg=arg
#
# class TooYoungException(Exception):
#     def __init__(self,arg):
#         self.msg=arg
#
# def dob():
#     try:
#         if age>21:
#             raise TooYoungException('Candidate is not eligible')


# def rev(no):
#     data=0
#     val=0
#     while no:
#         num=no%10
#         data=str(num)
#         no=no//10
#         val=val+1
#     return int(data)
# print(rev(-1234))

# def squ(num):
#     print('The Square of a number is ',num*num)
# squ(10)
# squ(4)
#
# def fact(num):
#     result=1
#     while num>=1:
#         result=result*num
#     return num
# print(fact(5))
#
# a=10
# def sam():
#     a=100
#     print(a)
#     print(globals()['a'])
# sam()
#
# max_num=lambda a,b : a if a>b else b
# print(max_num(10,20))
#
# def double(m):
#     return 2*m
# list1=[10,20,30,40,50]
# print(list(map(double,list1)))

# s=[10,20,30,40,50]
# s1=[2,4,6,8,10]
# mult=list(map(lambda x,y :x*y ,s,s1))
# print(mult)

# d1=[10,20,30,40,50]
# from functools import *
# l2=reduce(lambda x,y :x*y ,range(1,10))
# print(l2)
#
# def sqe(x):
#     print('hii',x,'Good Morning')
# greet=sqe
# del sqe
# print(greet('sanjay'))

# class student():
#     def __init__(self,name,age,rollno):
#         self.x=name
#         self.y=age
#         self.z=rollno
#     def display(self):
#         print('Student Name:',self.x ,'\n age is :',self.y ,'roll no is:',self.z)
#
# s1=student('sanjay',25,222)
# s1.display()
#
#
# class dict_obj():
#     def __init__(self):
#         self.name='sanjay'
#         self.age=25
# s1=dict_obj
# print(list(s1.__dict__))
#
# s='sanjay'
# i=0
# for x in s:
#     print('The Character present at positive index {} and at -ve index {}'
#           .format(i,i-len(s)))
#     i=i+1
#
# s1='python is very easy to learn'
# print(s1[1:12:2])
# print(s1[10:3:-1])
#
emp_str=''
spl_str=s1.split()
for x in spl_str:
    emp_str=emp_str+' '+x[::-1]
print(emp_str)


# i=len(s1)-1
# while i >=0:
#     emp_str=emp_str+s1[i]
#     i=i-1
# print(emp_str)

# name='sanjay kumar'
# spl_chr=name.split()
# emp_str=''
# i=len(spl_chr)-1
# while i >=0:
#     emp_str=emp_str+spl_chr[i][::-1]
#     i=i-1
# print(emp_str)
#
# s=':::::sanjay:::::'
# print(s.strip(':'))

content='Sanjaya kumar sahoo'
# sub_content='sahoo'
# try:
#     print(content.index(sub_content))
# except ValueError:
#     print('Substring Not found')
# else:
#     print('Substring found ')

# print(content.count('a'))
# print(content.count('a',1,10))
#
# print(content.replace('a','s'))
#
# s='sanjay + kumar + sahoo'
# spl_chr=s.split('+')
# print(spl_chr)
#
# s='SaNjaAy AkYMar saHoO'
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())
#
# s='Learning python is very easy'
# print(s.startswith('Learning'))
# print(s.endswith('Easy'))

# f=open('one.txt','w')
# print('The file Name Is',f.name)
# print('The Mode of file is ',f.mode)
# print('The Fil Is Readable or not',f.readable())
# print('The file is writable or not ',f.writable())
# print('The file is close or not',f.closed)
# f.close()
# print('The file is close or not',f.closed)
#
# f=open('two.txt','w')
# # f.write('This is python language\n')
# f.write('easy coding')
# f.close()1
# print('The file successfully closed')
# f=open('two.txt','r')
# reading=f.read()
# print(reading)

# with open('one.txt','w') as f:
#     f.write('There is pyhton language')
#     f.close()
#     print('The File Is Closed or not', f.closed)
#
# f=open('one.txt','r')
# print(f.tell())
# print(f.read(9))

# class student:
#     def __init__(self,name,age,rollno):
#         self.x=name
#         self.y=age
#         self.w=rollno
#     def show(self):
#         print('The Name is ',self.x)
#         print('The age is ',self.y)
#         del self.w
#         print('The roll no is',self.w)
# t=student('sanjay',24,222)
# t.show()
# t.z=1234
# print(t.x)
# print(t.__dict__)

# class student:
#     def __init__(self):
#         self.x=10
#         self.y=20
#         self.z=30
    # def m1(self):
    #     del self.z
# s=student()
# print(s.__dict__)
# s.m1()
# print(s.__dict__)

# class test():
#     x=10
#     def show(self):
#         self.y=30
# t=test()
# t.show()
# print('t values',t.x)
# test.x=20
# print(t.x)
#
#
# class Student:
#     def m1(self,marks):
#         self.marks=marks
#     def m2(self):
#         return self.marks
#     def setname(self,name):
#         self.name=name
#     def getname(self):
#         return self.name
#
# s=Student()
# s.m1(200)
# print(s.m2())
# s.setname('sanjay')
# print(s.getname())
#
# class animal:
#     iegg=4
#     @classmethod
#     def clsmethod(cls,name):
#         print('animal name is {} gives egg{}'.format(name,cls.iegg))
# a1=animal()
# a1.clsmethod('dog')
#
# class test:
#     count = 0
#     def __init__(self):
#         test.count=test.count+1
#     @classmethod
#     def testcount(cls):
#         print('The test object count is ',cls.count)
# t1=test()
# t1.testcount()

# class testobj:
#     @staticmethod
#     def testsum(x,y):
#         print('The Sumis ',x+y)
#     @staticmethod
#     def product(x,y):
#         print('The product Is ',x*y)
# t1=testobj
# t1.testsum(10,20)
# t1.product(5,10)

# class Employee:
#     def __init__(self,name,age,sal):
#         self.name=name
#         self.age=age
#         self.sal=sal
#     def display(self):
#         print('The Name os the student is',self.name)
#         print('The age is',self.age)
#         print('The salary is',self.sal)
# class details:
#     def show(self):
#         self.sal=self.sal+1000
#         self.display()
# e=Employee('sanjay',22,10000)
# details.show(e)

# class outer:
#     def __init__(self):
#         print('outer Class Constructor')
#     class inner:
#         def __init__(self):
#             print('Inner class constructor')
#         def m1(self):
#             print('Inner class method')
# o=outer().inner()
# o.m1()
#
# class test:
#     def __init__(self):
#         print("Object initialization")
#     def __del__(self):
#         print("fullfilling last wish and performing last activities")
# t1=test()
# t1=None
# time.sleep(5)
# print('End of application')

# class Engine:
#     a=10
#     def __init__(self):
#         self.b=20
#     def m1(self):
#         print('Engine is specifically for car')
#         print('The Value os b is',self.b)
# class Car:
#     def __init__(self):
#         self.engine=Engine()
#     def m2(self):
#         print('The Enfine is m2')
#         self.engine.m1()
# c=Car()
# c.m2()

# class C:
#     def __init__(self):
#         print('THis is construvtor')
#         self.a=10
#     @staticmethod
#     def m1():
#         print('This is static method')
#     @classmethod
#     def m2(cls):
#         print('The classmethid is a decorator')
# class p(C):
#     pass
#
# p1=p()
# print(p1.a)
# p1.m1()
# p1.m2()

# class p:
#     def m1(self):
#         print('This p class method')
# class s(p):
#     def m2(self):
#         print('This is s class method')
# class r(s):
#     def m3(self):
#         print('This r claas method')
# R=r()
# R.m1()
# R.m2()
# R.m3()

# class hier:
#     def m1(self):
#         print('kkk')
# class syer(hier):
#     def m2(self):
#         print('jjj')
# class byerr(hier):
#     def m3(self):
#         print('sss')
# B=byerr()
# s=syer()
# s.m1()
# s.m2()
# B.m1()
# B.m3()

# class c:
#     def m1(self):
#         print('This is m1 method')
# class d:
#     def m2(self):
#         print('This is m2 method')
# class e(c,d):
#     def m3(self):
#         print('This is m3 Method')
# c1=e()
# c1.m1()
# c1.m2()
# c1.m3()

# class employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def dis(self):
#         print('The Name is',self.name)
#         print('The age is ',self.age)
# class student(employee):
#     def __init__(self,name,age,rollno,stand):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.stand=stand
#     def display(self):
#         super().dis()
#         print('The rollno is',self.rollno)
#         print('The stand is ',self.stand)
#
# e=student('sanjay',25,122,18)
# e.display()

# class cog:
#     def __init__(self):
#         print('This is constructor')
#     @staticmethod
#     def m1():
#         print('This is static method')
#     @classmethod
#     def m2(cls):
#         print('This is class method')
# class dyna(cog):
#     def __init__(self):
#         super().__init__()
#         super().m1()
#         super().m2()
#     def show(self):
#
#         super().m1()
#         super().m2()

# d=dyna()
# d.m1()
# d.m2()

# class stu:
#     def property(self):
#         print('This is property method')
#     def sign(self):
#         print('This is sign method')
# class teach(stu):
#     def sign(self):
#         super().sign()
#         print('THis is sign method')
#
# s=teach()
# s.property()
# s.sign()

# pattern=re.compile('ab')
# print(pattern)
# matcher=pattern.finditer('ababababbbbaaabb')
#
# import re
# count=0
# pattern=re.compile('ab')
# matcher=pattern.finditer('ababababbbbaaabb')
# for match in matcher:
#     count=count+1
#     print(match.start(),'....',match.end(),'....',match.group())
# print('The Number Of occurrences',count)
#
# import re
# sum=0
# match_pat=re.finditer('sa','sasasasasannnsannansansa')
# for match in match_pat:
#     sum=sum+1
#     print(match.start(),'...',match.end(),'...',match.group())
# print('The number of occrences is ',sum)
#
# import re
# matcher=re.finditer("x","a7b@k9z")
# for match in matcher:
#     print(match.start(),"......",match.group())

# f=open('abc.txt','w')
# f.write('pyhton language is easy')
# f.close()
# f1=open('abc.txt','r')
# data1=f1.read(8)
# print(data1)
# print(f1.tell())
# print(f.seek(14))
# print('Is it readable',f1.readable())
# print('Is it readable',f1.readlines())
# f.close()
#
# import os
# dd=os.stat('abc.txt')
# print(dd)

# An abstract method is a method that has a declaration but does not have an implementation.
# When we want to provide a common interface for different implementations of a component,
# we use an abstract class.

from abc import *
# class test:
#     @abstractmethod
#     def show(self):
#         print('Hello')
#
# t1=test()
# t1.show()

# class vehicle(ABC):
#     @abstractmethod
#     def noofwheels(self):
#         pass
# class bus(vehicle):
#     def noofwheels(self):
#         return 8
# class auto(vehicle):
#     def noofwheels(self):
#         return 3
# b=bus()
# print(b.noofwheels())
# a=auto()
# print(a.noofwheels())

# in general if an abstract class contain only abstract method
# then such type of class is called interface

# class test:
#     x=10
#     _y=20
#     __z=30
#     def m1(self):
#         print(test.x)
#         print(test._y)
#         print(test.__z)
# t=test()
# t.m1()
# print(test.x)
# print(test._y)
# print(t._test__z)
#
# def magic():
#     try:
#         print('Try block')
#     except:
#         print('Except block')
#     finally:
#         print('Finally block will execute')
# r=magic()

# import os,sys
# fname=input("Enter The file name")
# if os.path.isfile(fname):
#     print('The file is exist',fname)
#     f=open(fname,'r')
# else:
#     print('file doesnt exist')
#     sys.exit(0)
# print('The content of the file is ')
# data=f.read()
# print(data)

# class employee:
#     def __init__(self,name,age,sal):
#         self.name=name
#         self.age=age
#         self.sal=sal
#     def display(self):
#         print('The name is ',self.name)
#         print('The age is ',self.age)
#         print('The sal is ',self.sal)
# with open('emp.dat','wb') as f:
#     e=employee('sanjay',24,2000)
#     pickle.dump(e,f)
#     print('Pickling of employee object is completed')
#
# with open('emp.dat','rb') as f:
#     obj=pickle.load(f)
#     obj.display()
#
# s='sanjay kuamr sahoo'
# spl=s.split()
# print(spl)

# list1=[10,20,30,40,50,20,20]
# print(list1[4])
# print(list1.count(20))
# list2=list1[1:3:1]
# print(list2)
# print(list1.index(50))

# list1.append(100)
# print(list1)
# list1.insert(3,299)
# print(list1)
#
# order1=[10,20,30,40,50,60]
# order2=[20,30,405,60,70]
# order1.extend(order2)
# print(order1)
# order1.extend('Mushroom')
# print(order1)
# order1.remove(30)
# print(order1)
# # print(order1.remove(100))
# print(order1.pop())
# print(order1.pop(4))
# order1.reverse()
# print(order1)
# order1.sort()
# print(order1)

# x=[10,20,30,40,50,60,70]
# y=x
# y[2]=900
# print(x)
# print(id(x))
# print(id(y))
# y=x.copy()
# y[3]=300
# print(y)
# x.clear()
# print(x)
#
# words=['sanjay','kumar','sahoo','python']
# s=[w[0] for w in words]
# print(s)

# words="the quick brown fox jumps over the lazy dog"
# spl=words.split()
# link=[[w.upper(),len(w)] for w in spl]
# print(link)

vowels=['a','e','i','o','u']
# str1='sanjay kumar sahoo'
# str_spl=str1.split()
# emp_chr=[]
# for x in str1:
#     if x  in vowels:
#         if x not in emp_chr:
#             emp_chr.append(x)
# print(emp_chr)
# print('The number of different vowels present in str1 ',vowels,'is',len(emp_chr))

# l1=[1,2,3]
# l2=l1
# l1.append(4)
# print(l1)
# l2.append(4)
# print(l2)

# list1=[1,2,3,4]
# s=str(list1)
# print(s)

# def fifo(arr):
#     emp_lis=[]
#     for x in arr:
#         if emp_lis.append(x)==emp_lis.pop(arr[x][-1]):
#             print('Its valid')
#         else:
#             print('Its not valid')
# f=fifo('{ [ < > ] }')
#
# new_dic_a={'a':20,'b':30,'c':40}
# new_dic_b={'d':50,'e':60,'f':70}

# def dic_val(a,b):

# def deco(func):
#     def inner(name):
#         func()
#         if name == 'sanjay':
#             print('Good morning')
#     return  inner
# @deco
# def show():
#     print('Good evening')
# show('sanjay')
#
# def show(*args,**kwargs):
#
# import re
# re.match('ab','abbbb')
#
# s = "abcabcbb"
# def get_long_subs_without_repeat(name):
#     spl_chr=
#
#
# from itertools import combinations
# list1=[1,2,3,4,5,6,7,8,9,10]
# sum=7

# count=list1.combinations()
# dic={}
# dic[sum]=dic[list1]
#
# for x in list1:
#
#
# input_str='malayalam'
# emp_str=''
# for x in input_str:
#     emp_str=x+emp_str
# if emp_str==input_str:
#     print('Its palidrome')
# else:
#     print('Its not')

# list1=[1,2,4,6,7,5,8,3,9,10]
#
# for each in range(len(list1)-1):
#     for every in range(len(list1)-1):
#         if list1[every]<list1[every+1]:
#             list1[every],list1[every+1]=list1[every+1],list1[every]
# print(list1)


# 3rd_sal=users.object.get(sal)

# class demo:
#     counter=1
#     def dummy(self):
#         print(self.counter)
#         self.counter=2
#         print(self.counter)
#         print(demo.counter)
# d=demo 
# d.dummy()

# def show(str1):
#
#     len_str1=len(str1)
#     emp_str=''
#     for each in range(len_str1):
#         if each %2 ==0:
#             emp_str=emp_str+str1[each].lower()
#         else:
#             emp_str=emp_str+str1[each].upper()
# s=show('sanjay')
#
# str1 = 'sanjay'
# list_comp = [x for x in range(len(str1)-1) str1[x].lower if x %2==0 else str1[x]]
#
# arr=[1,1,2,2,4,5] 
# st_len=len(arr)//2
# for each in arr:
#     arr[each],arr[each+1]=arr[each+1],arr[each]

# def prime_num(num):
#     if num%1 or num% num==0:
#         print('Its a prime')
#     else:
#         print('Its not a prime number')
# prime_num(8)


# lis=[1,2,3,4,5,6,7,8]
# sum=7
# def show(arr):
#     emp_list=[]
#     for x in range(1,len(arr)-1):
#         for y in arr:
#             if arr[x]+y==sum:
#                 emp_list.append((arr[x],y))
#     return emp_list

# print(show(lis))

# num_list=[2,3,48,12,32,65,99,71,61,86]

# def display(num: list):
#     for x in range(len(num_list)):
#         if num[x]%2!=0:
#             num.insert(-1,num[x])
#             num.pop(x)
#         else:
#             num.insert(0,num[x])
#             num.pop(x)
#         if num[-1]%2==0:
#             num.insert(0,num[-1])
#             num.pop(-1)
#     return num
# print(display(num_list))

# name = "sanjaykumarsahoo"
# # spl_chr=name.split()
# emp_dic={}
# for x in name:
#     emp_dic[x]=emp_dic.get(x,0)+1
# for key,val in emp_dic.items():
#     print(key ,'occurs',val,'times')

# a=10
# b=a
# print(a)
# print(b)

# def fibo():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for x in fibo():
#     if x > 100:
#         break
#     print(x)

print('sanjau')































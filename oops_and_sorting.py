import re


def test_global():
    global number_store
    number_store = 444
    # print(number_store)

def display_global():
    # print(number_store)
    pass

test_global()
display_global()

x = 109

def show():
    x = 88
    print(x)
    print(globals()['x'])
# show()

square_num = lambda x:x*x
# print(square_num(5))


add_num = lambda m,n:m+n
# print(add_num(4,5))

list_ele = [4,5,6,6,7,8]
find_even = list(filter(lambda i: i%2==0, list_ele))
# print(find_even)

from functools import *

s1 = reduce(lambda x,y : x+y, range(0,100))
# print(s1)

l=[1,9,6,5,3]
l.reverse()
# print(l)

sorting_list = l.sort(reverse=False)
# print(sorting_list)

some=["Balaiah","Nag","Chiranjeve","Somendra"]
second_word = [w[:2] for w in some]
# print(second_word)

srs_1=[10,20,30,304,50,60]
srs_2=[10,30,44,55,66,77,88]

remove_duplicate = [dup for dup in srs_1 if dup not in srs_2 ]
# print(remove_duplicate)

class MyClass:
    def __init__(self, name):
        self.name = name

    def show_data(self):
        return self.name

# my_class_obj = MyClass("sanjay")

# from django.core.management.base import BaseCommand
#
# class Command(BaseCommand):
#     help= 'integer123'
#
#     def add_argument(self, parser):
#         parser.add_arguments('args', type=int, help='integer123')

class MyClass:
    @staticmethod
    def static_method():
        return 'This is static method'
obj= MyClass()
# print(obj.static_method())

class MyClass:
    class_var = 'This is class method'

    @classmethod
    def class_method(cls):
        return cls.class_var

# print(MyClass.class_method())


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError('It cant be less than zero')
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius


circle = Circle(5)
# print(circle.radius)

circle.radius = 10
# print(circle.radius)

# del circle.radius
#
# print(circle.radius)

def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
fact = factorial(5)
# print(fact)

# select salary from (
#     select salary, ROW_NUMBER() OVER (order by salary DESC) as row_num
#     from employees
# ) as temp
# where row_num =2
#
#
# select salary
# from employee
# order by salary DESC
# limit 1 offset1
#
# create index idx_salaru on emp(salary);
#
# create INDEX idx_salary_col ON EMP (salary, Department);
#
# CREATE FULLTEXT INDEX fulltext_index_col ON EMP (salary);
#
# CREATE UNIQUE INDEX unique_idx_col ON EMP(salary);
#
# CREATE CLUSTERED INDEX idx_clustered_col  ON EMP(salary);
#
# CREATE INDEX non_clus_idx_col on emp(salary);
#
# select salary, id, from emp
# INNER JOIN dept on emp.id=dept.id

import itertools
x=0
y=1
z=1
n=1

args = [x,y,z,n]

permutation = [perm for perm in itertools.permutations(args)]
# print(permutation)

sum=0
# for num in permutation:
#     for sum_val in num:
#         sum += sum_val
#         if sum <= 3:
#             print(num)


list_val = [0, 45, 45, 32, 21, 29]

for element in range(len(list_val)-1):
    max_val = max(list_val[element:])
    max_val_index = list_val.index(max_val, element)
    if list_val[element] != list_val[max_val_index]:
        list_val[element], list_val[max_val_index] = list_val[max_val_index], list_val[element]
# print("sorted val is",list_val)

for num in range(len(list_val)):
    min_val = list_val[num]

    for ele in range(num+1, len(list_val)):
        if list_val[ele] < min_val:
            min_val = list_val[ele]
    min_val_index = list_val.index(min_val, num)
    if list_val[num] != min_val:
        list_val[num], list_val[min_val_index] = list_val[min_val_index], list_val[num]
# print(list_val)

def is_leap(year):
    # leap = False

    # Write your logic here
    print(year/4)
    if year % 4 == 0 and year % 400 == 0:
        leap = True
    else:
        leap = False
    return leap
leap_year = is_leap(2400)
# print('leap year value', leap_year)

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __mul__(self, other):
        if isinstance(other,Vector):
            return Vector(self.x*other.x, self.y*other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

obj = Vector(1,2)
obj1 = Vector(3,4)
ans = obj*obj1
# print(ans)

class Share:
    def property(self):
        print("Gold+cash+car")
    def marry(self):
        print("Sunny leone")
class Dont_share(Share):
    def marry(self):
        print("Dani daniels")

# cls_obj = Dont_share()
# cls_obj.property()
# cls_obj.marry()


class MyClass:
    def account(self):
        print("I have no money")
    def bank_balance(self):
        print("I have one account")
class HerClass(MyClass):
    def bank_balance(self):
        print("I Have multiple accounts")
        super().bank_balance()

cls_obj_over = HerClass()
cls_obj_over.account()
cls_obj_over.bank_balance()


class StudentMark:
    def __init__(self, name, age):
        print("His name is {} and age is {}".format(name,age))
class StudentFace(StudentMark):
    def __init__(self, name, age, face, lips):
        super().__init__(name,age)
        self.face=face
        self.lips = lips
        print("His name is {} and age is {}".format(face, lips))

# sf= StudentFace('sanjay', 27, "fair", "red")

pattern = re.compile('ab')
matcher = pattern.finditer('ababababa')
count = 0
for pat in matcher:
    count+=1
    # print(pat.start(), pat.end(), pat.group())
# print(count)


# pattern = re.compile('ab')
matcher = re.finditer("[\w]",'"a7b@k9zS 3$')

for pat in matcher:
    # print(pat.start(), pat.end(), pat.group())
    pass

# m = re.match("de", "abcabdefg")
# if m != None:
#     print("Match is available at the beginning of the String")
#     print("Start Index:", m.start(), "and End Index:", m.end())
# else:
#     print("Match is not available at the beginning of the String")


m = re.fullmatch("de", "abcabdefg")
if m != None:
    # print("Match is available full part of the String")
    # print("Start Index:", m.start(), "and End Index:", m.end())
    pass
else:
    # print("Match is not available full part of the String")
    pass


m = re.search('aa', 'aabcdbaa')
if m!=None:
    print('Match is available search part of string')
    print("Start Index:", m.start(), "and End Index:", m.end())
else:
    print('Match is not available in search')


my_pattern = re.findall('[0-9]', "a3b2b5jk")
# print(my_pattern)
if my_pattern!=None:
    # print('find all the occurence')
    pass
else:
    # print('dont find any where')
    pass
itr = re.finditer('[A-Z]', "asdm475FAk4A")
for itr in itr:
    # print(itr.start(), itr.end(), itr.group())
    pass
my_pattern = re.sub('[a-z]', "$", 'as3fdFs45')
# print("Pattern bro",my_pattern)

subn_pattern = re.subn('[a-z]', "%", 'sde4rfk&')
# print(subn_pattern)

first_pattern = re.findall('^easy', 'easy rest body')
# print(first_pattern)

last_pattern = re.findall('match$', 'this is a intersting match')
# print(last_pattern)

mob= '91783029558'
mob_num = re.findall('[0-9]\d{9}',mob)
# print(mob_num)

email = "fhjhb98@gmail.com"
valid_email = re.findall('\w[a-zA_Z0-9_.]*@gmail[.]com', email)
# print(valid_email)

phone_num = 91678276372
# valid_phone = re.fullmatch('[0|91]')

def convert_to_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
@convert_to_upper
def display_name(name):
    return name
# print(display_name('sanjay'))


# class Author(models.Model):
#     name = models.charfield(max_length =50)
#
# class Book(models.Model):
#     name = models.Charfield(max_length=50)
#     author = models.ForeignKey(Author, on_delete=model.CASCADE)

# result = Book.objects.select_related('Author').all()


from abc import ABC, abstractmethod

class Army(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def gun(self):
        pass
    @abstractmethod
    def tank(self):
        pass

    def show(self):
        print('Concrete method')

class Navy(Army):
    def gun(self):
        print('This is child class')
        print("This is abstract method ")

class Air(Navy):
    def tank(self):
        print("This is Tank abstract method ")

# A1 = Air()
# A1.gun()
# A1.tank()

# Polymorphsim:
# =============
class Animal:
    def sound(self):
        return "Some sound"
class Dog(Animal):
    def sound(self):
        return "Bow Bow"
class Cat(Animal):
    def sound(self):
        return "Meow Meow"
def make_sound(animal):
    print(animal.sound())

dog=Dog()
cat=Cat()
animal=Animal()
make_sound(dog)
make_sound(cat)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third
llist.print_list()


def convert_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs).upper()
        return result
    return wrapper

@convert_upper
def display(name):
    return name
print(display('sanjay'))




lis = [1, 3, 4, 10, 4]

import itertools, functools
from functools import reduce
# print(list(itertools.accumulate(lis, lambda x, y: x+y)))

# print(functools.reduce(lambda x, y: x+y, lis))

iterable_func = iter(lis)
# print(next(iterable_func))
# print(next(iterable_func))
# print(next(iterable_func))

# [satbatcatmat]
#
#
# polls.objects.filter(contains='who').filter(Q (pub_date='2005-05-02') | Q(pub_date = '2005-05-06'))
#
# polls
#
# author
# name = models.Many(polls, on_delete=Model.cascade)

# whatis method resolution oder
# what are you using for django security
# what is csrf
# what is django authentication
# what is session authentication
# what is garbage collections used in django
# what is first class function in python
# what is encapsulation
# how can we increase performance of a django application
# what is token authentication
# what is jwt token authentication
# what is benefit of generator
# what is the method we will use if we define a iterator class
# what is serializer
# what is deserializer
# what method we are using for deserializing
# what is reference count
# what is prefetch_related
# what is model serializer in django
# what is validator in django
# how to create a API in django


# What is the difference between sort and sorted
# how to update dictionary key value
# question on custom middleware. If i create two custom middleware
# can i call the abstract class which is inherited in ABC class
# does python support multi threading
# what is return type of get method in DJANGO ORM
# I have one table . In that i have 5 column and i have 2 rows of data. In Name column I have same name,
# If query like table.objects.filter(name='sanjay') Then which row data will come as both name column is same name
#

# what is difference between class and structure
# what is difference between abstarct class and iterface
# what is difference between multilevel inheritance and multiple inheritance show method ambiguity
# i have 2 num is adding write a decorator so that it should add another numbers
# what is the difference between protected and protected access modified
# what is the difference between generator and list comphrension
# write a code to show sum of sqaure of all numbers  in a fibonacci series using generator
# Use *args sum all the numbers passed into it
# what is polymorphisym and what is runtime and static time polymorphism
# How to prevent python overriding
# find second highest salary if same employee have same salary also
# what is the difference between function and stored procedure
# make a ajax call in view and get list of numbers and findout even number from it and render it
# how to do form validation
# write a code for caching mechanism in django , and for trasanction manageement and also for pagination
# what is scalar function and what is the use of it
# write a property function to show getter and setter method with example
# write a code for developed a calculator using method overloading
# anagram question
# List of tuple. extract tuple , recursion
# nested list question
# Decorator
# Lambda Function Question
a= 10
b =20
# a,b =b,a


a = a+b
b = a-b
a = a-b
# print("a =", a)
# print("b =", b)


str1 = "my name is avinash and i m from kerala"
# output :1
# my name is
# name is avinash
# is avinash and
# avinash and i
# and i m
# i m from
# m from kerala
split_str = str1.split()


for ex in range(len(split_str)-2):
    # print('result is',split_str[ex:ex+3])
    pass
str1 = "my name is avinash and i m from kerala"
step = 2
for ex in range(0, len(split_str), step):
    # print(split_str[ex:ex+step])
    pass
list_val = [0, 45, 45, 32, 21, 29]
for ex in range(len(list_val)-1):
    for every in range(len(list_val)-1):
        if list_val[every] > list_val[every + 1]:
            list_val[every], list_val[every+1]=list_val[every+1], list_val[every]
# print(list_val)

# highest_salary = Employee.objects.aggregate(max('salary'))['salary__max']
# second_highest_salary = Employee.objects.filter(salary__lt=highest_salary).aggregate(max('salary'))['salary__max']

# class A:
#     def method(self):
#         print('A')
#
# class B(A):
#     def method(self):
#         print('B')
#
# class C(B):
#     def method(self):
#         print('C')
# class D(B,C):
#     pass

# print(D.__mro__)

lst = [1, 2, 3]
result = [lst.append(x) for x in range(3)]
# print(lst)  #[1,2,3,0,1,2]
# print(result) #[1,2,3,0,1,2]

l1 = [1,2,3,4,5]
output_list= []
output = ["odd", "even", "odd" ,"even", "odd"]
# Use list comprehension
find_number_type = ["odd" if x%2!=0 else "even" for x in l1]
# print(find_number_type)

# Given an array of integers numbers that is sorted in non-decreasing
# order. Return the indices of two numbers, [index1, index2], such that
# they add up to a given target number target and index1 < index2. Note
# that index1 and index2 cannot be equal, therefore you may not use the
# same element twice. There will always be exactly one valid solution. Your
# solution must use O(1) additional space. Example 1: Input: numbers = [1,2,3,4], target = 3 Output: [0,1]

numbers = [1,2,3,4]
target = 3

result = []

for x in range(len(numbers)):
    for y in range(x+1, len(numbers)):
        if numbers[x]+numbers[y]==target:
            result.append((numbers[x], numbers[y]))
# print(result)

# for key in range(len(val_dict
# .values())):
#     # print(val_dict[target][2])
#     # print(key)
#     if val_dict[target][key]+val_dict[target][key] == target:
#         print('Done')

def add_num(*args, default=10):
    total_sum = 0
    for ex in args:
        total_sum += ex
    default_val = default+total_sum
    return default_val
# print(add_num(1,2,4))

def reverse_alpha(str1):
    no_spl_chr = [chr for chr in str1 if chr.isalpha()]
    reverse_chr = no_spl_chr[::-1]
    iter_statement = iter(reverse_chr)
    final_output = ''.join(next(iter_statement) if chr.isalpha() else chr for chr in str1)
    return final_output

s = 'ch,od@i!'
print(reverse_alpha(s))

def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b=b, a+b
obj = fibonacci()

for x in range(100):
    # print("fibo series", next(obj))
    pass
numbers = [1, 2, 3, 4, 5]
squared_number = list(map(lambda x:x*x, numbers))
# print(squared_number)

filter_number = list(filter(lambda x:x%2==0, numbers))
# print(filter_number)

from functools import reduce
reduce_example = reduce(lambda x,y :x+y, numbers)
# print(reduce_example)

# select order, price
# from order
# where customer_id in (select customer_id from customer where city = 'New York' )
#
# select salary
# from emp
# where salary > (select MAX(salary) from emp)

# Create a Django management command to delete users who have been inactive for over a year.

# django_inactive_user.py
# ========================
# def command(BaseCommand):
#     user = get_user_model()
#     one_year_ago = now() - datetime.timedelta(days=365)
#
#     inactive_user = user.objects.filter(last_login__lt=one_year_ago)
#     if inactive_user.exists():
#         count , _ = inactive_user.delete()
#         self.stdout.write(f'{count} inactive user(s) deleted.')
#     else:
#         self.stdout.write('No inactive users found.')
#
# django manage.py django_inactive_user

# Write a Django query to find the top 5 most active users based on the number of posts they have made. Assume you have
# User and Post models, where Post has a foreign key to User
# top_post = user.objects.annotate(post_count = Count('post')).order_by('_post_count')[:5]

# def can_distribute_bananas(N):
#     # We need at least 2 monkeys (1 monkey cannot receive all bananas)
#     # Each monkey should get more than 1 banana.
#
#     for monkeys in range(2, N // 2 + 1):
#         if N % monkeys == 0:
#             bananas_per_monkey = N // monkeys
#             if bananas_per_monkey > 1:
#                 return True
#     return False


# Example usage
# N = int(input("Enter the number of bananas: "))
# result = can_distribute_bananas(N)
# print(result)

def trailing_zero_number(n):
    fact = n

    while n>1:
        fact *= n-1
        n-=1

    result = 0
    for i in str(fact)[::-1]:
        if i =='0':
            result+=1
        else:
            break
    return result
print("trailing zero count ",trailing_zero_number(5))

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

singleton1 = Singleton(10)
singleton2 = Singleton(20)

print(singleton1 is singleton2)

def outer(func):
    def wrapper(a,b,c):
        return func(a,b)+c
    return wrapper
@outer
def add(a,b):
    return a+b
# print(add(3,4,5))

# def show_fibo(n):
#     a,b=0,1
#     for _ in range(n):
#         yield a
#         a,b = b,a+b
#
# def sum_fibo(n):
#     return sum(x**2 for x in show_fibo(n))
#
# print(sum_fibo(5))

# @cache_page(60*5)
# def my_view(request):
#     model = model.objecta.all()
#     return  render(request, index.html, {'data':data})
#
# def my_view(request):
#     data = cache.get('mydata')
#     if not data:
#         data = model.objecs.all()
#         cache.set('my_data', data, timeout=60*5)
#
# from django.core.paginator
#
# def show_paginator(request):
#     model = models.objects.all()
#     paginate = paginator(model,5)
#     page_number = request.get.GET('page')
#     page_obj = paginator.get_page(page_number)

from functools import reduce
numbers = [2,3,4,5,6]
mul_num = reduce(lambda x,y: x*y, numbers)
print(mul_num)

def sum_num(*args):
    result = 0
    for x in args:
        result=result+x
    return result

print(sum_num(2,3,4))

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @property
    def set_salary(self, value):
        if value<0:
            raise ValueError('Salary cannot be negative')
    salary = property(salary, set_salary)
emp= Employee('sanjay', '10000')

def show_even(request):
    if request.method=='GET' and request.is_ajax():
        numbers = request.get.getlist('numbers[]')
        numbers=list(map(int, numbers))
        even_numbers = [num for num in numbers if num % 2 == 0]
        return JsonResponse({"even_numbers":even_numbers})
    return JsonResponse({'error':"Invalid request"}, status = 400)

def remove_duplicate(list_num):
    emp_dict = {}
    count = 0
    for num in list_num:
        emp_dict[num]=emp_dict.get(num,0)+1
    # print('my dict',emp_dict)
    for key, val in emp_dict.items():
        if val == 1:
            print(key)

list_num = [1,2,2,3,4,5,5,6]
# print(remove_duplicate(list_num))
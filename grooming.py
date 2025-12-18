# print all even letter from below string
import time

str_val = 's a n j a y'
# var_length = len(str_val)
spl_data = str_val.split(' ')
# print(spl_data)
length_var = len(spl_data)
actual_val = ''
for index_num in range(length_var):
    if index_num % 2 == 0:
        actual_val += spl_data[index_num]
# print(actual_val)

# multiply given string with its alphabet given inside the string
#output should be "ddfffggggggggg"

str_list='d2f3g4g5'
actual_str = ''
var_length = len(str_list)

for alphabet in str_list:
    if alphabet.isalpha():
        char_var = alphabet
    else:
        int_var = int(alphabet)
        actual_str += char_var*int_var
# print(actual_str)

#find the index number of particular number
list1=[10,20,30,40,50,60,70]
index_num = list1.index(20)
# print(index_num)

spl_chr='s2d3f5g2'
char_str = ''
for each in spl_chr:
    if each.isalpha():
        var_list = each
    else:
        int_var = int(each)
        char_str += var_list * int_var
print(char_str)

#remove duplicate from given string
str_one='aaassssjjjsjsjsjsnnsns'
unique_str = ''
for each_str in str_one:
    if each_str not in unique_str:
        unique_str += each_str
# print(unique_str)

#remove duplicate from given string
str1='sanjay kumar kumar sanjay sahoo sahoo'

spl_chr = str1.split()
each_chr = ''
for each_word in spl_chr:
    if each_word not in each_chr:
        each_chr+=' ' + each_word
# print(each_chr)

#find out maximum number
a=10
b=20
max_num = a if a>b else b
# print(max_num)

# findout size of a number
import sys
list_of_num = (10,20,30,40,50)
length_num = sys.getsizeof(list_of_num)
# print(length_num)

#reverse the odd number in the follow string
str_input = 'one two three four five six'
split_chr = str_input.split()
actual_str = ''
actual_chr = ''
for each_index in range(len(split_chr)):
    if each_index % 2 == 0:
        actual_str += " " + split_chr[each_index]
    else:
        actual_str +=" " + split_chr[each_index][::-1]
# print(actual_str)

# findout the how many times vowel presents in given string
# random_string = 'sanjaoiaaiiy'
# vowels=['a','e','i','o','u']
# emp_str = ''
#
# for vowel in vowels:
#     if vowel in random_string:
#         emp_str+=vowel
#
# for each_str in emp_str:
#     print('{} occurs {} times'.format(each_str, random_string.count(each_str)))


# findout the how many times vowel presents in given string
# random_string = 'sanjaoiaaiiy'
# vowels=['a','e','i','o','u']
# store_dict = {}
# for x in random_string:
#     if x in vowels:
#         store_dict[x] = store_dict.get(x, 0)+1
#
# for k,v in store_dict.items():
#     print('{} occurs {} times'.format(k,v))


# output : {2: 3, 4: 6, 6: 9, 8: 12, 10: 15, 12: 18, 14: 21, 16: 24, 18: 27}
# square_variable = {x*2:x*3 for x in range(1,10)}
# print(square_variable)


#findout the factorial of a number
def factorial_of_number(num):
    if num == 0:
        result = 1
    else:
        result = num * factorial_of_number(num-1)
    return result
# print(factorial_of_number(5))


# insert a number between inside a list
list1=[10,20,30,40,50,60]
insert_num = list1.insert(len(list1)//2, 15)
# print(list1)

# findout all the even number within 100
def findout_even(num):
    for each_num in range(0,num):
        if each_num % 2 == 0:
            yield each_num
# print(list(findout_even(100)))


# sort the given dictionary
dict_value = {'m':2,'q':5,'w':8,'d':3}
sorted_val = dict(sorted(dict_value.items()))
# print(sorted_val)

sorted_key = {x:y for x,y in sorted(dict_value.items(), reverse=False)}
# print(sorted_key)

#findout even number using lambda function
temp=[1,2,3,4,5,6,7,8,9,10]
even_num = list(filter(lambda x : x%2==0, temp))
# print(even_num)

#findout sqaure of all number given in the list of array

square_num = list(map(lambda x:x*2, temp))
# print(square_num)

from itertools import combinations
s=[1,2,3,4,5]
def show_combination(arr, r):
    return combinations(arr, r)
# print(list(show_combination(s, 2)))

arr=['sanjay kumar sahoo']
modified_list = []

for x in arr:
    array_is = modified_list.append(x[:-3])
# print(modified_list)

# print(arr[0][:-6])

list_sort=["1","3","9","6","5"]
sorted_list = sorted(list_sort, reverse=False)
# print(sorted_list)

# for a in range(3):
#     for b in range(a):
        # print(a,b)

def fibo():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a+b

for x in fibo():
    if x < 100:
        # print(x)
        break


def fibonacci_series(n):
    emp_list = []
    first_term, second_term = 0, 1
    for _ in range(n):
        emp_list.append(first_term)
        new_term = first_term+second_term
        first_term = second_term
        second_term = new_term
    return emp_list
n = 10
fibo_result = fibonacci_series(n)
# print("Fibo result is", fibo_result)


def missing_number(arr):
    len_arr = len(arr)+1
    find_nth_sum = len_arr*(len_arr+1)//2
    total_sum = sum(arr)
    return find_nth_sum-total_sum
# print("missing_number is ", missing_number([1, 2, 4, 6, 3, 7, 8]))

dict1 = {9: [2, 11, 7, 15]}
keys= next(iter(dict1))

list_of_value = dict1[keys]
for val in range(len(list_of_value)):
    for each_val in range(val+1, len(list_of_value)):
        if list_of_value[val]+list_of_value[each_val] == keys:
            # print('{},{}'.format(list_of_value[val], list_of_value[each_val]))
            pass

a={100:'sanjay',200:'kumar',400:'sahoo',400:'Natia',500:'batia'}
emp_dict = []
for key in a.keys() :
    emp_dict .append(key)
# print(emp_dict)
for key in emp_dict:
    # print('{} occurs {} times'.format(key, emp_dict.count(key)))
    pass

test_string = 'aaaannnbbbvvv'
emp_dict={}
for x in test_string:
    emp_dict[x] = emp_dict.get(x, 0)+1
for key, val in emp_dict.items():
    # print('{} occurs {} times'.format(key, val))
    pass

test_dict = {'gfg' : [5, 6, 7, 8],
              'is' : [10, 11, 7, 5],
              'best' : [6, 12, 10, 8],
              'for' : [1, 2, 5]}

emp_list = []
for val in test_dict.values():
    for actual_val in val:
        emp_list.append(actual_val)
# print(sorted(emp_list))


test_dict = {"Arushi" :22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
sorted_dict = {key:val for key,val in test_dict.items() if key!='Mani'}
# print(sorted_dict)

dict6 = {'a': 10, 'b': 8}
dict7 = {'d': 6, 'c': 4}
dict8={'e':3,'f': 7}

def add_dict(dict1, dict2, dict3):
    result = {**dict6,**dict7, **dict8}
    return result
print(add_dict(dict6, dict7, dict8))

test_dict = {'month' : [1, 2, 3],
              'name' : ['Jan', 'Feb', 'March']}
month_with_digit = dict(zip(test_dict['month'], test_dict['name']))
print(month_with_digit)

test_dict = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
res = dict()
for x in sorted(test_dict):
    res[x] = sorted(test_dict[x])
# print(res)


test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
emp_lis = []
emp_dic = {}
for key, val in test_dict.items():
    if val not in emp_lis:
        emp_lis.append(val)
        emp_dic[key]=val
# print(emp_dic)

list1=['sanjay','kumar','sukesh','mukesh','ravi','mohan']
list2=['ram','shyam','sanjay','mukesh','ravi','sahoo','rrr']

for each in list1:
    if each in list2:
        # print(each)
        pass

input_list=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1]
from collections import Counter
res=Counter(input_list)
print("what",res)

pali_str='malayalam'
emp_str=''
for x in pali_str:
    emp_str = x+emp_str
# if pali_str == emp_str:
#     print("Its palindrome")
# else:
#     print("Its not a palindrome")

max_num = lambda a,b : a if a>b else b
# print(max_num(10, 5))

s='sanjay'
list_contain = ''
for chr in s:
    list_contain=chr+list_contain
# print(list_contain)

i = 0
length_char = len(s)
for chr in range(length_char,i):
    list_contain += s[chr]
    i = length_char-i
    if i >= 0:
        break
# print("99999999999999999",list_contain)


str1='sanjay kumar'
spl_char = str1.split()
emp_str = ''
length_char = len(spl_char)
for char in range(length_char):
    # print(spl_char[char])
    emp_str = spl_char[char] + ' '+ emp_str
# print(emp_str)

name_str = 'sanjay kumar sahoo'
spl_char = name_str.split()
emp_str = ''
length_char = len(spl_char)
for yes in range(0, len(spl_char)):
    emp_str =' '+ spl_char[yes][::-1] + emp_str
print("i know",emp_str)


content='Sanjaya kumar sahoo'
sub_content='sahoo'
split_content = content.split()
for yes in split_content:
    # if yes in sub_content:
    #     print("content found")
    # else:
    #     print("Not found")
    pass

name_mine='sanjay + kumar + sahoo'

spl_name = name_mine.split('sahoo')
# print(spl_name)

import re
given_string = 'sasasasanansnansasa'
sub_content = 'sa'
sum = 0
matcher = re.finditer(sub_content, given_string)
for occurence in matcher:
    sum = sum +1
# print(sum)

words=['sanjay','kumar','sahoo','python']
first_letter_word = [w[0] for w in words]
# print(first_letter_word)

emp_str = ''
for god in words:
    emp_str+=god[0]
# print(emp_str)


length_char = len(arr)
def fifo(arr):
    stack_list = []
    for num_length in range(length_char-1):
        stack_list.append(arr[len(arr)//2:])
    print("stack list", stack_list)

f=fifo('{ [ < >] }')

words = "the quick brown fox jumps over the lazy dog"
spl_word = words.split()
find_length = [[w.upper(), len(w)] for w in spl_word]
# print(find_length)

str1='sanjay'
length = len(str1)
str_store = ''
for each_index in range(length):
    if each_index % 2 == 0:
        str_store+=str1[each_index].upper()
    else:
        str_store += str1[each_index]
# print(str_store)

str_01='durga'
reverse_string = reversed(str_01)
join_str1 = ''.join(reverse_string)
# print(join_str1)

num_list='one two three four five six'
emp_str = ''
split_str = num_list.split()
string_length = len(split_str)

for each_index in range(string_length):
    if each_index % 2==0:
        emp_str += split_str[each_index]
    else:
        emp_str += ' ' + split_str[each_index][::-1] + ' '
# print(emp_str)


my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

# print(next(my_iter))

def count_up_to(n):
    count =1
    while count <=n:
        yield count
        count+=1
iterate_obj = count_up_to(6)
# print(iterate_obj)
# print(next(iterate_obj))
# print(next(iterate_obj))
# print(next(iterate_obj))
# print(next(iterate_obj))
# print(next(iterate_obj))
# print(next(iterate_obj))
# print(next(iterate_obj))

def total_time_taken(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        print('total time taken by this function ', time_taken)
        return result
    return wrapper

@total_time_taken
def count_number(n):
    count = 0
    for i in range(n):
        count+=i**2
    return count

# print(count_number(100))

def convert_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@convert_upper
def display_name(name):
    return name
# print(display_name('sanjay'))


#shallow copy
list1 = [10,20,30,40,50]
new_list=list1
# print(list1)
# print(new_list[1])
# new_list[1] = 345
# print(new_list)
# print(list1)

new_list = list1.copy()
new_list[2]=234
# print(new_list)
# print(list1)
import copy
# deep copy
deep_list = [[10, 20, 30, 40, 50], [45, 55, 65, 75, 85]]
deep_list2 = copy.deepcopy(deep_list)
# deep_list.append([32,42,52,62,72])
deep_list2[1][2] = 120
# print(deep_list2)
# print(deep_list)

import pickle
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# print(type(data))
with open('data.pickle', 'wb') as file:
    dump_data = pickle.dump(data, file)


with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)
# print(type(loaded_data))
# print(loaded_data)

# file=open('GYM_Competition.txt','rb')
# id = pickle.load(file)
# print(id)


with open('myfile_written.txt', 'w') as file:
    file_store = file.write('This is file handling operation')
    # print(file_store)
import pickle
movie_list = ["RRR", "Pushpa", "KGF", "Jawan", "Dangal"]

# movie = "movie_list.pkl"
# with open(movie, 'wb') as file:
#     pickle.dump(movie_list, file)

# with open(movie, 'rb') as file:
#     movie_data = pickle.load(file)
# print(movie_data)

with open('bike_test.txt', 'w') as file:
    file.write('This is a good boy')

with open('bike_test.txt', 'r') as file:
    # for each in file:
    #     print(each)
    pass

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
#
# with open('dict_file.txt', 'w') as file:
#     for key, val in details_id.items():
#         file.write('%s:%s\n' % (key, val))
#     print('Word written successfully')

def merge(dict1,dict2):
    dict1.update(dict2)
    return dict1

dict1 = {'nas':12, 'das':23, 'sas':34}
dict2 = {'fas':82, 'jas':73, 'ras':64}

def_obj = merge(dict1, dict2)
# print(def_obj)

def merge(dict1, dict2):
    res = {**dict2, **dict1}
    return res
dict_result = merge(dict1, dict2)
# print(dict_result)

test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
zip_dict = dict(zip(test_dict['month'], test_dict['name']))
# print(zip_dict)

from collections import OrderedDict
inorder_dict= OrderedDict([('akshat',1),('nikhil', 2)])
inorder_dict.update({'manjeet':4})
# print("waht order here", inorder_dict)
inorder_dict.move_to_end('manjeet', last=True)
# print(inorder_dict)

test_dict={5 : 'sahoo', 4 : 2, 8 : 3}
sum_of_dict = list(test_dict.keys())+list(test_dict.values())
# print(sum_of_dict)

arr_list = ["chi", "beta", "anyone"]

sort_value = sorted(arr_list, reverse=False)
# print(sort_value)

python_students = [['Harry', 37.21], ['Berry', 37.12], ['Tina', 37.43], ['Akriti', 41], ['Harsh', 39]]

first = ['', float('-inf')]
second = ['', float('-inf')]

# Iterate through the list to find the top two students
for student in python_students:
    name, marks = student
    # print(name)
    # print(marks)
    # print(first[1])
    if marks > first[1]:
        second = first  # Update second place
        first = [name, marks]  # Update first place
    elif marks > second[1]:
        second = [name, marks]  # Update second place



list1 = [56, 3, 2, 78, 6,0]

# print(min_val)
for run in range(len(list1)):
    min_val = min(list1[run:])
    min_val_index = list1.index(min_val)
    list1[run], list1[min_val_index] = list1[min_val_index], list1[run]

# print(list1)

for ex in range(len(list1)-1):
    for every in range(len(list1)-1):
        if list1[every] > list1[every+1]:
            list1[every], list1[every+1] = list1[every+1], list1[every]
# print(list1)

def change_char(arr):
    rev_store_str  = ''
    for ex in arr:
        if ex.isalnum():
            print("This is alnum", ex)
            rev_store_str = ex+rev_store_str
        else:
            spl_chr = ex
            rev_store_str = rev_store_str+spl_chr
    return rev_store_str

str_rev='sanjaykumar!'
# print(change_char(str_rev))


def reverse_alpha(arr):
    alpha_char = [chr for chr in arr if chr.isalpha()]
    print(alpha_char)
    reverse_str = alpha_char[::-1]
    iter_char = iter(reverse_str)
    apply_spr_chr = ''.join(next(iter_char) if chr.isalpha() else chr for chr in arr)

    return apply_spr_chr
s = 'sd,sa@An!'

# output_str = reverse_alpha(s)
# print(output_str)

def add_multiple_number(*args, default=10):
    total = 0
    for x in args:
        total += x
    default_val = total+default
    return default_val
# print(add_multiple_number(1,2,4))

word_days = ['sunday', 'monday', 'tuesday']
word = 'monda'
try:
    if word in word_days:
        print('yes')
    else:
        print('NO')
except:
    raise


class NoExceptionRaise:
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code  = error_code

    def __str__(self):
        if self.error_code:
            return f"[Error {self.error_code}]:{self.message}"
        return self.message
# try:
#     raise NoExceptionRaise("This is a custom exception raise", error_code=404)
# except NoExceptionRaise as e:
#     print(e)
fruits = ['apple', 'banana', 'cherry']
quantities = [5, 3, 7]

fruit_dict = {fruits[i]:quantities[i] for i in range(len(fruits))}
# print(fruit_dict)

find_square = {x:x**2 for x in range(1,11) if x%2==0}
# print(find_square)

fruits = ['apple', 'banana', 'cherry', 'grapes']
quantities = [5, 3, 7, 9]

filtered_dict = {fruits[i]:quantities[i] for i in range(len(fruits)) if quantities[i]>4}
# print(filtered_dict)

words = ['apple', 'banana', 'cherry']
number_list = [len(x) for x in words]
# print(number_list)

list_sqaures = [x**2 for x in range(1,6)]
# print(list_sqaures)

list_squares_condition = [x**2 for x in range(1,6) if x % 2==0]
# print(list_squares_condition)

matrix = [[x for x in range(1,4)] for y in range(1,4)]
# print(matrix)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = [(x,y) for x in list1 for y in list2 if x+y >5]
# print(combined_list)

list_val = [0, 45, 45, 32, 21, 29]
for ele in range(len(list_val)):
    min_val = min(list_val[ele:])
    min_val_index=list_val.index(min_val)
    if list_val[ele] != list_val[min_val_index]:
        list_val[ele],list_val[min_val_index]=list_val[min_val_index], list_val[ele]
# print(list_val)

def find_even_long(sentence):
    split_word = sentence.split()
    max_length = 0
    words = ''

    for word in split_word:
        if len(word)%2==0 and len(word) > max_length:
            words = word
            max_length = len(word)
    return words

sentence = "Find the longestdd even word in this sentence"
# print(find_even_long(sentence))


def find_even_longest(sentence):
    split_sentence = sentence.split()
    max_length_word = 0
    long_word = ''

    for word in split_sentence:
        if word.isalpha():
            if len(word) % 2 ==0 and len(word) > max_length_word:
                max_length_word = len(word)
                long_word = word
    return long_word
sentence = "Be not afraid of greatness, Some are born great, some acheive greatness, some have greatness thrust upon them."

# print(find_even_longest(sentence))

# input = 111 1 , 123

def find_unique_num(num):
    unique_list_num = []
    for unique_num in str(num):
        if unique_num not in unique_list_num:
            unique_list_num.append(unique_num)
    return len(unique_list_num)
# print(find_unique_num(111))


class A:
    def fun(self,p,q):
        return p+q
class B(A):
    def fun(self,p,q,r=1):
        super().fun(p,q)
        return p+q/r
b1=B()
# print(b1.fun(10,20))
# print(b1.fun(10,20,30))


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
# print(trailing_zero_number(5))

def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b, a+b

# for i in fibonacci(10):
#     print("jbcbckwbcikbckwbckb",i)


def can_distribute_banana(N):
    for monkeys in range(2,N//2+1):
        if N % monkeys == 0 :
            banana_per_monkey = N//monkeys
        if banana_per_monkey > 1:
            return True
        return False
N=6
print(can_distribute_banana(N))

list1 = "['['name1']', '['name2']']"

list_contain = []
cleaned_string = list1.replace("['", "").replace("']", "")
names_list = [name.strip() for name in cleaned_string.split("', '")]

# print(names_list)

import re
names_list = re.findall("\w+", list1)
print("Helooooo",names_list)

my_dict = [{'name':'sanjay'},{'Surname':'Sahoo'}]

for d in my_dict:
    print(d)
    if 'name' in d:
        d[(1,2,3)] = d.pop('name')
# print(my_dict)

# Python program to print the highest frequency character in a String

def highest_frequency_letter(str):
    char_freq = {}
    for char in str:
        char_freq[char] = char_freq.get(char, 0)+1
    # print("dict value is ", char_freq)
    max_freq = max(char_freq.values())
    for key, val in char_freq.items():
        if val == max_freq:
            return key
input_string = "end of the day"
high_freq_char = highest_frequency_letter(input_string)
print("High frq cHar is ", high_freq_char)

car_data = {
   "CAR1": {"COST": 500, "COLOR": "RED"},
   "CAR2": {"COST": 500, "COLOR": "Yellow"},
   "CAR3": {"COST": 5600,  "COLOR": "Blue"},
   "CAR4": {"COST": 5002,  "COLOR": "Green"},
   "CAR5": {"COST": 5002,  "COLOR": "RED"},
   "CAR6": {"COST": 5002,  "COLOR": "RED"},
   "CAR7": {"COST": 5002,  "COLOR": "RED"},
   "CAR8": {"COST": 5002,  "COLOR": "RED"},
   "CAR9": {"COST": 5005,  "COLOR": "RED"},
   "CAR10": {"COST": 5005, "COLOR": "RED"},
   "CAR11": {"COST": 5005, "COLOR": "RED"},
   "CAR12": {"COST": 5005, "COLOR": "RED"},
   "CAR13": {"COST": 5010, "COLOR": "RED"},
   "CAR14": {"COST": 5011, "COLOR": "RED"},
   "CAR15": {"COST": 5011, "COLOR": "RED"},
   "CAR16": {"COST": 5012, "COLOR": "RED"},
   "CAR17": {"COST": 5013, "COLOR": "RED"},
   "CAR20": {"COST": 500,  "COLOR": "RED"},
   "CAR21": {"COST": 500,  "COLOR": "Yellow"},
   "CAR22": {"COST": 5600, "COLOR": "Blue"},
   "CAR23": {"COST": 5002, "COLOR": "Green"},
   "CAR24": {"COST": 500,  "COLOR": "RED"},
   "CAR25": {"COST": 500,  "COLOR": "Yellow"},
   "CAR26": {"COST": 5600, "COLOR": "Blue"},
   "CAR27": {"COST": 5002, "COLOR": "Green"},
   "CAR28": {"COST": 500,  "COLOR": "RED"},
   "CAR29": {"COST": 500,  "COLOR": "Yellow"},
   "CAR30": {"COST": 5600, "COLOR": "Blue"},
   "CAR31": {"COST": 5002, "COLOR": "Green"},
   "CAR32": {"COST": 5002, "COLOR": "Green"},
   "CAR33": {"COST": 5002, "COLOR": "Green"},
   "CAR34": {"COST": 5002, "COLOR": "Green"},
   "CAR35": {"COST": 5002, "COLOR": "Green"}
 }

"""Python app development
Design a class to store a data of the vehicle available in the json file and design a class to
implement below public interface to display on std output and manipulate data.
show_vehicle_data
update vehicle data for field vehicle cost
has context menu"""

class CarStore:
    def extract_car_details(self, car):
      # self.car=car
      print(car_data[car]['COST'])
           # print()
    def update_cost(self, specific_car):
      car_data[specific_car]['COST'] = 1000
      print('New car cost is :', car_data[specific_car]['COST'])


c= CarStore()
c.extract_car_details('CAR1')
c.update_cost('CAR28')



find_odd = [num for num in range(0,100) if num%2 != 0]
# print(find_odd)

print(find_odd[-10:])

my_list = ['apple', 'banana', 'apple', 'orange']
freq_dict = {}

for item in my_list:
   if item in freq_dict:
      freq_dict[item] += 1
   else:
      freq_dict[item] = 1
print(freq_dict)

square_val = {x:x*2 for x in range(10)}
print(square_val)


def find_target(arr, target):
    arr.sort()  # Sorting takes O(n log n)
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            print('1st execute in if staement')
            return True
        elif current_sum < target:
            left += 1
            print(left)
            print('1st execute')
        else:
            right -= 1
    return False

arr = [0, -1, 2, -3, 7]
target = 0
f = find_target(arr, target)
# print(f)


def find_target(arr, target):
    for each in range(len(arr)):
        for every in range(each+1, len(arr)):
            if arr[each]+arr[every]==target:
                return True
    return False

arr = [0, -1, 2, -3, 7]
target = 0
f = find_target(arr, target)
print(f)


# from scalene import scalene_profiler
#
# scalene_profiler.start()
#
# def scalene_example():
#     import time
#     time.sleep(2)
#
#     num_display = [x for x in range(10000)]
#     return num_display
#
# scalene_example()
# scalene_profiler.stop()
#
# @profile
# def run_number():
#     time.sleep(2)
#
#     num_display = [x for x in range(10000)]
#     return num_display

def check_duplicate(sentence):
    seen_letter = set()
    for word in sentence.split():
        for letter in word:
            if letter in seen_letter:
                return True
            seen_letter.add(letter)
    return False


sentence = "please tell me what is the input and what is the output from this sentence"
check = check_duplicate(sentence)
print(check)

list1 = [12,11,13,12,11,13,15,16]
# remove duplicate entries from list.


set1 = {'Digit', True, 2,"hello"}
# print(set1)

my_list = [1,2,3]

def foo(l1):
    l1[1]=l1[1]*100

# print(my_list)
# print(foo(my_list))
# print(my_list)

def remove_duplicate(num_list):
    for num in range(len(num_list)-1):
        if num_list[num] in num_list[:num]:
            num_list.pop(num)
        return num_list

list1 = [12,11,13,12,11,13,15,16]
# print(remove_duplicate(list1))

list1 = [12,11,13,12,11,13,15,16]
length = len(list1)
# print(list1[:length])


import time

from itertools import combinations
def check_target(list_num, target):
    for i in range(1, len(list_num)+1):
        for combination in combinations(list_num, i):
            if sum(combination) == target:
                return list(combination)

list_int = [1,2,3,7,5]
target=12
# print(check_target(list_int, target))

def check_target_sum(list_num, target):
    length_of_list = len(list_num)
    for i in range(length_of_list):
        current_sum = 0
        sublist = []
        for ele in range(i, length_of_list):
            current_sum += list_num[ele]
            sublist.append(list_num[ele])
            if current_sum==target:
                return sublist
            elif current_sum > target:
                break

list_int = [1, 2, 3, 7, 5]

target = 12
# print(check_target_sum(list_int, target))

def timing_decorator(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f'total time taken{func.__name__}:{end_time-start_time} seconds')
    return wrapper

@timing_decorator
def example_function():
    time.sleep(2)
    print('Function execution completed')
# example_function()

# str1 = "babad"
Output: "bab"
# Explanation: "aba" is also a valid answer.

def find_longest_substring(str1):
    max_length = 0
    my_str= ''
    for chr in str1:
        my_str+=chr
        max_length+=1
        if my_str==my_str[::-1] and max_length>1:
            return my_str
    return []
str1 = "babad"
# print(find_longest_substring(str1))


def check_longest_palindrom(str1):
    max_length = 0
    longest_substring = []
    for chr in range(len(str1)+1):
        for ele in range(chr+1, len(str1)+1):
            sub = str1[chr:ele]
            if sub == sub[::-1]:
                if max_length<len(sub):
                    max_length=len(sub)
                    longest_substring=[sub]
                elif len(sub)==max_length:
                    longest_substring.append(sub)
    return longest_substring
str1 = "babad"
# print(check_longest_palindrom(str1))

#reverse interger
# Output: -321

def reverse_int(input):
    is_negative = input<0
    input = abs(input)
    str_list = ''
    for num in str(input):
        str_list = num+str_list
    result = int(str_list)
    return -result if is_negative else result

given_num = 87880
# print(reverse_int(given_num))

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
"""Input:"""

# Output: "fl"

def common_prefix(strs):
    prefix = strs[0]
    for chr in strs[1:]:
        while not chr.startswith(prefix):
            prefix = prefix[:-1]
            if prefix=="":
                return ""
    return prefix

strs = ["flower", "flow", "flight"]
# print(common_prefix(strs))


words_list = ["madam", "racecar", "apple", "noon", "level", "rotor"]
def find_longest_palindrom(data):
    longest_str = ''
    for ch in data:
        if ch == ch[::-1] and len(ch)>len(longest_str):
            longest_str = ch
        return ch
# print(find_longest_palindrom(words_list))

strs = ["flower", "flow", "flight"]
def find_common_prefix(data):
    prefix = data[0]
    for word in data:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
    return prefix
# print(find_common_prefix(strs))

s = 'ch,od@i!'

def reverse_alpha(str1):
    letters = []
    for ch in str1:
        if ch.isalpha():
            letters.append(ch)

    letters.reverse()
    letters_index=0

    result = ''
    for chr in str(str1):
        if chr.isalpha():
            result += letters[letters_index]
            letters_index+=1
        else:
            result+=chr
    return result
# print(reverse_alpha(s))

arr = [10, 4, 20, 15, 8]
def find_kth_largest(arr, k):
    n = len(arr)
    for each in range(k):
        for every in range(0, n-each-1):
            if arr[every] > arr[every+1]:
                arr[every], arr[every+1] = arr[every+1],arr[every]
    return arr[n-k]
print('largest is ',find_kth_largest(arr, 2))











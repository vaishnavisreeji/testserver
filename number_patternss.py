"""import math
def fact(num):
    return math.factorial(num)
num=5
print("factorial of"num"is",factorial(num))"""


"""inte="my string"
#inte=list(inte)
inte= inte.replace(' ','')
inte=list(inte)

print(inte)"""

"""def str_to_list(str):
    str=str.replace(' ','')
    str = ''.join([i for i in str if not i.isdigit()])
    str=list(str)
   
 
    print(str)


str_to_list("my string 8")"""


"""def str_to_list(str):
    str=str.replace(' ','')
    str=list(str)
    for i in str:
        if i>5:
            print(i)
    #str = ''.join([i for i in str if not i.isdigit()])
    str=list(str)
   
 
    print(str)


str_to_list(int(float("my string 8")))"""


#malyalam

"""str="MalaYalam"
nstr=str.casefold()
print(nstr)
rstr=reversed(nstr)
if list(nstr)==list(rstr):
    print("palindrome")
else:
    print("not palindrome")"""

"""n=int(input("enter:"))
temp=n
rev=0
while n>0:
    d=n%10
    print(d)
    rev=rev*10+d
    print(rev)
    n=n//10
    print(n)
if (temp==rev):
    print("palindrome")
else:
    print("not")"""

"""list1=[1,2,3,4,5]
list2=[5,6,6,7,8,8,9,10]
def test(data):
	if len(data)==len(set(data)):
		return True
	else:
		return False
print(test(list2)"""

"""def person(name,**data):
	print(name)
	for i,j in data.items():
		print(i,j)

person('sree',age=30,place="kkv")"""

"""def add_sub(x,y):
	a = x+y
	s = x-y
	return a,s
results=add_sub(5,4)	
print(results)"""

"""import random
list=[]
for i in range(5):
	x=random.randint(10,25)
	list.append(x)
print(list)"""

"""import numpy as np
#a=np.array([[1,3 ,4],[3,4,4]])
a=np.arange(4)

print(a)"""

"""import random
def rolldice(min,max):
	while True:
		n=random.randint(min,max)
		print("random number is {}".format(n))
		choice=input("Do u want to roll dice again (yes/no):")
		if choice == "no":
			break

rolldice(1,6)"""

"""check=input("enter:")
rever=check[::-1]
#rever=reversed(check)
if(check==rever):
	print("palindrome")
else:
	print("not ")"""

	#PALINDROME

"""num=int(input("enter the number that you want to check:"))
temp=num
rev=0
while num>0:
	dig=num%10
	rev=rev*10+dig
	num=num//10
if (temp==rev):
	print("palindrome")
else:
	print("not palindrome")"""

          #SWAPPING

"""list=[23.90,11,22,98,13,62]
for i in list:
	list.sort()
print("third large element is:",list[-3])

temp=list[0]
list[0]=list[-1]
list[-1]=temp

print("swapped list is:",list)"""

"""check=input("enter the string:")
#vowels=0
for i in check:
	if i =="a" or i=="e" or i=="i" or i=="o" or i=="u":
		print("it a vowel")"""

"""def vowelcheck(inputstring,vowel_list):
	number_vowels=[each for each in inputstring if each in vowel_list]
print(len(number_vowels)
inputstring="sreeshna"
vowel_list=AaEeIiOoUu
vowelcheck(string,vowel_list)"""

"""def swap(list):
	#size=len(list)
	temp=list[0]
	list[0]=list[-1]
	list[-1]=temp
	return list
list=[10,70,50,30,20]
print(list)
print(swap(list))"""

"""list=[1,2,3,4,5,6,7,8,9,10]
#n=2
#break_list=[list[i:i + n] for i in range(0,10, n) ] 
#print(break_list)
for i in range(0,10,3):
	print([list[i:i+3]])
	a=([list[i:i+3]])
print(a)"""


"""def fact(num):
	if num==1:
		return num
	else:
		return num*fact(num-1)
num=6
print(fact(num))"""

"""from collections import Counter
import heapq
list1=[10,70,46,30,89,79,20]
list2=[10,70,46,10,30,89,79,10,20]
largest=heapq.nlargest(2,list1)
smallest=heapq.nsmallest(2,list1)

common=Counter(list2)
most_co=common.most_common(1)
print(largest)
print(smallest)
print(most_co)"""

"""stocks={"google":520,"facebook":46,"yahoo":67,"amazon":34}
zipp1=zip(stocks.keys(),stocks.values())
zipp2=zip(stocks.values(),stocks.keys())
print(sorted(zipp1))
print(sorted(zipp2))"""

"""T=int(input())
for t in T:
	(a,b)=map(int,input().split(' '))
	sum=a+b
	print(sum)"""

""""
num=int(input("enter the number that you want to reverse:"))
temp=num
rev=0
while num>0:
	dig=num%10
	rev=rev*10+dig
	num=num//10
print("reverse is:",rev)"""

"""n=int(input("enter"))
arr=map(int,input().split())
a=sorted(set(arr))[-2]
print(a)"""

"""N=int(input("enter:"))
res=[]
grade=[]

for i in range(N):
    name=input()
    marks=int(input())
    res.append([name,marks])
    grade.append(marks)
print(res)
print(grade)
grade=sorted(set(grade))
print(grade)
mark=grade[1]
print(mark)
name=[]
for j in res:
	if mark==j[1]:
		name.append(j[0])
print(name)
name.sort()
print(name)
for nm in name:
	print(nm)"""




"""for j in res:
	if mark==j[1]:
		name.append(j[0])
print(name)
name.sort()
print(name)
for nm in name:
	print(nm)"""

"""n=int(input())
marks={}
for i in range(n):
	name,*line=input().split()		
	score=list(map(float,line))
marks[name]=score
query_name=input()
a=marks[query_name]
print("{:.2f}".format(sum(a)/3))"""
"""a=[10,23,56,[78]]
b=list(a)
a[3][0]=95
a[1]=34
print(b)"""
                                         #BASIC CODING
										 #SUM AND PRODUCT
"""a=int(input())
b=int(input())
c=a*b
d=a+b
if c<=1000:
	print(c)
else:
	print(d)"""

	                                       #CURRENT aND PREVIOUS
										
"""previ=0
for i in range(0,11):
	print("current:",i,"prev:",previ,"sum:",i+previ)
	previ=i"""
                                           #EVEN INDEX
"""a=str(input())
b=len(a)
for i in range(0,b-1,2):
	print(a[i])"""
	
"""a=str(input())	
lis=list(a)
for i in lis[0::2]:
	print(i)"""



"""user="Emma is good developer. Emma is a writer"
count=0
size=len(user)
print(size)
for i in range(size-1):
	count+=user[i:i+4]=="Emma"
print("Emma appeared ", count, "times")"""



"""n=5
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end=" ")
	print()"""




"""n=int(input())
temp=n
rev=0
while n>0:
	d=n%10
	rev=rev*10+d
	n=n//10
if temp==rev:
	print("Yes given number is palindrome")
else:
	print("No given number is not")"""


"""list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
newlist=[]
for i in (list1):
	if i%2!=0:
		newlist.append(i)
for j in (list2):
	if j%2==0:
		newlist.append(j)
print(newlist)"""

"""list1=[]
for i in range(5):
	a=float(input("enter:"))
	list1.append(a)
print(list1)"""

"""print("abc")"""



"""a=0
b=1
print(a)
print(b)
for i in range(2,10):
	c=a+b
	a=b
	b=c
	print(c)"""

"""def info(*args):
	for i in args:
		print(i)
info(40,70,78)"""

"""def calculation(a, b):
	sum=a+b
	sub=a-b
	return sum,sub
res = calculation(40, 10)
print(res)"""	

"""def show_employee(name,salary=10000):
	return name,salary
print(show_employee("sreeji",40000))
print(show_employee("vaishu"))"""

"""def outer_func(a,b):
	def adds(a,b):
		return a+b
	add=adds(a,b)
	return add+5
print(outer_func(5,8))"""

"""def display_student(name,age):
	return name,age
show_student=display_student
print(show_student("vaishu",25))"""

"""str1=input()
size=len(str1)
res=str1[0]
print(res)
mid=int(size/2)
res1=str1[mid]
total=res+res1
print(total)
tot=total+str1[ -1]
print(tot)"""


"""def mid_three(input_string):
	size=len(input_string)
	mid=int(size/2)
	mids=input_string[mid]
	print(mids)
	res=input_string[mid-1:mid+3]
	print(res)
	
print(mid_three("johndippeta"))"""

from audioop import reverse
from optparse import Values
from tkinter import Y


"""def append_str(str1,str2):
	str3=[]
	mid=int(len(str1)/2)
	mids=str1[mid]
	print(mids)
	x = str1[:mid]
	x=x+str2
	y=str1[mid:]
	y=x+y
	return y
print(append_str("ault","kelly"))"""

"""s1 = "America"
s2 = "Japan"
first=s1[0]+s2[0]
middle=s1[(int(len(s1)/2))]+s2[(int(len(s2)/2))]
last=s1[-1]+s2[-1]
result=first+middle+last
print(result)"""

"""str1 = input()
lower=[]
upper=[]
for i in str1:
	if i.isupper():
		upper.append(i)
	else:
		lower.append(i)

str2="".join(lower+upper)
print(str2)"""

"""str1 = "P@#yn26at^&i5ve"
a_count=0
d_count=0
s_count=0
for i in str1:
	if i.isalpha():
		a_count+=1
	elif i.isdigit():
		d_count+=1
	else:
		s_count+=1
print(a_count)
print(d_count)
print(s_count) """



"""import string
str1 = '/*Jon is @developer & musician!!'
#replace_char = '#'
for i in string.punctuation:
	str1=str1.replace(i ,"#")
print(str1)"""

"""s1 = "vaishu"
s2 = "sreejith"
size1=len(s1)
print(size1)
size2=len(s2)
print(size1)
length = size1 if size1 > size2 else size2
print(length)
result = ""

s2=s2[::-1]
for i in range(length):
    if i < size1:
        result = result + s1[i]
    if i < size2:
        result = result + s2[i]
print(result)"""


"""str1 = "Emma is a good developer,Emma is a actor"
str1=str1.rfind("Emma")
print(str1)"""

"""str1 = "Emma-is-a-data-scientist"
str1=str1.split("-")
for i in str1:
	print(i)"""
 
"""import string
str1="/*Jon is @developer & musician"
str2=str1.maketrans("","",string.punctuation)
str1=str1.translate(str2)
print(str1)"""

"""import re
str1="/*Jon is @developer & musician"
str1 = re.sub(r'[^\w\s]','',str1)
#res = re.sub(r'[^\w\s]', '', str1)
print(str1)
#print(res)"""

"""str1 = 'I am 25 years and 10 months old'

for i in str1:
	if i.isdigit():
		print(i,end="")"""

"""str1 = "Apple"

result=dict()
for i in str1:
	a = str1.count(i)
	
	result[i] = a
	
print(result)"""

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
"""nstr=[]
for i in str_list:
	if i:
		nstr.append(i)
print(nstr)	"""	

"""def isbalance(x,y):
    output=True
    for i in x:
        if i in y:
            continue
        else:
            output=False
    return output
print(isbalance("Yn","PYnative"))"""

"""str1 = "Welcome to USA. usa awesome, isn't it?"
str1=str1.lower()
a=str1.count("usa")
print(a)"""

"""str1 = "PYnative29@#8496"
sum=0
count=0
for i in str1:
	if i.isdigit():
		sum=sum+int(i)
		count+=1
avg=sum/count
print(sum)
print(avg)"""

"""str1 = "Emma25 is Data scientist50 and AI Expert"
res = []
temp = str1.split()
print(temp)
for i in temp:
    if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
        res.append(i)
for j in res:
    print(j)"""

"""l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]	
l3=[]
a=l1[1::2]
b=l2[0::2]
c=a+b
l3.extend(a)
l3.extend(b)	
print(l3)"""
	


"""first = [2, 3, 4, 5, 6, 7, 8]
second= [4, 9, 16, 25, 36, 49, 64]
a=zip(first,second)
a=set(a)
print(a)"""

"""first = {23, 42, 65, 57, 78, 83, 29}
second = {57, 83, 29, 67, 73, 43, 48}
inte=first.intersection(second)
for i in inte:
	first.remove(i)
print(first)
print(inte)"""

"""sample = [87, 45, 41, 65, 94, 41, 99, 94]
a=set(sample)
a=tuple(a)
b=min(a)
print(a)
print(b)"""

"""speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
s=speed.values()
print(s)
speed_list=[]
print(speed_list)
for i in s:
	if i not in speed_list:
		speed_list.append(i)
print(speed_list)"""

"""list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
for i,j in zip(list1,list2):
	a=i+j
	print(a,end=" ")"""

"""numbers = [1, 2, 3, 4, 5, 6, 7]
list1=[]
for i in numbers:
	list1.append(i*i)
print(list1)"""
		
"""list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
a=[i+j for i in list1 for j in list2]
print(a)"""
  

		





"""from datetime import datetime
a="Jan 20 2022 5:36PM"
s=datetime.strptime(a,"%b %d %Y %I:%M%p")
print(s)"""

"""from datetime import datetime,timedelta
given_date = datetime(2020, 2, 25)
a=given_date-timedelta(days=7)
print(a)"""

"""from datetime import datetime
given_date = datetime(2020, 2, 25)
a=given_date.strftime(' %A %d %B %Y')
print(a)"""

"""from datetime import datetime

given_date = datetime(2020, 7, 26)

# to get weekday as integer
print(given_date.today().weekday())

# To get the english name of the weekday
print(given_date.strftime('%A'))"""

"""from datetime import datetime,timedelta
given_date = datetime(2020, 3, 22, 10, 00, 00)
print(given_date+timedelta(days=7,hours=12))


from datetime import datetime


date_1 = datetime(2020, 2, 25).date()

date_2 = datetime(2020, 9, 17).date()

delta = ''
if date_1 > date_2:
   delta = date_1 - date_2
else:
    delta = date_2 - date_1
print(delta.days)"""

"""class Vehicles:
	def __init__(self,name,max_speed,mileage):
		self.name=name
		self.max=max_speed
		self.mil=mileage
	def seating_capacity(self,capacity):
		return "The seating capacity of a {0} is {1} passengers".format(self.name,capacity)
class Bus(Vehicles):
	def seating_capacity(self,capacity=50):
		 return super().seating_capacity(capacity=50)
obj=Bus("school bus",120,12)
print(obj.seating_capacity())"""



"""name="vaishnavi Sreejith"
first_name,last_name=name.split()

print(first_name,last_name,sep=",")"""

def add(a,
	    b,
	    c):
	return a+b
print(add(4,5,7))







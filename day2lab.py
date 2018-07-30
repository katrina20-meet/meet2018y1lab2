Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=10
>>> c=0
>>> a=b
>>> b=a
>>> a
10
>>> b
10
>>> a=5
>>> b=10
>>> a=b
>>> a
10
>>> b
10
>>> c=a
>>> a=b
>>> b=c
>>> a
10
>>> b
10
>>> a=5
>>> b=10
>>> c=a
>>> a=b
>>> b=c
>>> a
10
>>> b
5
>>> four= '4'
>>> print(four*3)
444
>>> five=4
>>> print(five)
4
>>> print(five*3)
12
>>> my_name='student'
>>> print("my name is' + 'my_name")
my name is' + 'my_name
>>> print("my name is" + my_name)
my name isstudent
>>> print ("my name is " + my_name)
my name is student
>>> my_name='student'
>>> print("hi," + myName')
	  
SyntaxError: EOL while scanning string literal
>>> my_name='student'
	  
>>> print("Hi, " + my_name)
	  
Hi, student
>>> my_age= 15
	  
>>> print('i am '+ my_age + 'yeaars old')
	  
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print('i am '+ my_age + 'yeaars old')
TypeError: must be str, not int
>>> my_age=15
	  
>>> my_age= str(my_age)
	  
>>> print("i am " + my_age + "years old")
	  
i am 15years old
>>> my_age=15
	  
>>> my_age= str(my_age)
	  
>>> print("i am " + my_age + " years old")
	  
i am 15 years old
>>> score=1
	  
>>> total= score + (count *2)
	  
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    total= score + (count *2)
NameError: name 'count' is not defined
>>> score=1
	  
>>> count=2
	  
>>> total= score + (count*2)
	  
>>> print (total)
	  
5
>>> 

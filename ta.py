Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=(1,2,3,4,5)
>>> a[1]=7
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a[1]=7
TypeError: 'tuple' object does not support item assignment
>>> a=[1,2,3,4,5,6]
>>> a[5]=7
>>> print(a)
[1, 2, 3, 4, 5, 7]
>>> a=[2,4,6,8]
>>> a[2]
6
>>> a=[1,3,5,7,9]
>>> a[4]
9
>>> 

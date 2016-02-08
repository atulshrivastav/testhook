#! /usr/bin/python
####################################################################
# data_exercise_1_2.py - script to demonstrate Python data types 
# and control strutures.
#
# R. Melton
# 9/25/15
####################################################################

import sys

####################################################################
# 1. explore str datatype
print '\nexplore str datatype'
a = 'abcdef'
# immutable
a[0] = 'b'  
print 'a', a,' type of a ',type(a),' length of a ',len(a)
for c in a:
   print '\t',c

#dynamically typed, strongly typed
a = a + 1

####################################################################
# 2. bytearray datatype - bytes considered as bytes, not characters
print '\nexplore bytearray datatype'
a = bytearray(b'abcdef')
print 'a', a,' type of a ',type(a),' length of a ',len(a)
for c in a:
   print '\t',c
# mutable
a[0] = 'b'  
print 'a', a,' type of a ',type(a),' length of a ',len(a)

####################################################################
# 3. bytes datatype - bytes considered as bytes, not characters
# seems to be the same as str datatype
print '\nexplore bytes datatype'
a = bytes(b'abcdef')
print 'a', a,' type of a ',type(a),' length of a ',len(a)
for c in a:
  print '\t',c
# immutable
a[0] = 'b' 
print 'a', a,' type of a ',type(a),' length of a ',len(a)

####################################################################
# 4. list datatype - mixed data types in a group
print '\nexplore list datatype'
a = [1,'abcdef',True]
print 'a', a,' type of a ',type(a),' length of a ',len(a)
for c in a:
   print '\t',c
   if type(c) == type(1):
      print '\tnumeric type found'
   elif type(c) == type('a'):
      print '\tstr type found'
   else:
      print '\tother type found'
# mutable
a[0] = 3
print 'a', a,' type of a ',type(a),' length of a ',len(a)
a.remove(3)
a.insert(0,1)
# strongly typed
b = a[1]+1
# list comprehension example, multiply any numbers in the list by 2
a = [1,2,3,4,5]
a = [ x*2 for x in a if x % 2 == 0 ]
print 'a', a,' type of a ',type(a),' length of a ',len(a)

####################################################################
# 5. tuple datatype - mixed data types in a group
print '\nexplore tuple datatype'
a = (1,'abcdef',True)
print 'a', a,' type of a ',type(a),' length of a ',len(a)
for c in a:
   print '\t',c
# immutable
a[0] = 3
a.remove(3)
a.insert(0,1)
# strongly typed
b = a[1]+1

# YOUR FIX HERE , add a 'while/exit' loop to print all elements in 'a' 
# and use the 'exit' block to print out the total number of elements in
# 'a'
sys.exit(1)
####################################################################
# 5. set datatype - mixed data types in an unordered group
print '\nexplore set datatype'
a = {1,'abcdef',5.0}
b = {2,'ghijkl',5.1}
print 'a', a,' type of a ',type(a),' length of a ',len(a)
for c in a:
   print '\t',c
   if 5.0 == c:
      print '\tfound 5.0'
# unordered - there is no a[0] 
a[0] = 3
# you can do normal set operations
c = a.add('4')
print 'a', a,' type of a ',type(a),' length of a ',len(a)
c = a.union(b)
print 'c', c,' type of c ',type(c),' length of c ',len(c)

####################################################################
# 6. frozenset datatype - mixed data types in an unorder group
print '\nexplore frozenset datatype'
a = frozenset([1,'abcdef',5.0])
print 'a', a,' type of a ',type(a),' length of a ',len(a)
for c in a:
   print '\t',c
if 5.0 == c:
   print '\tfound 5.0 in c'
# immutable
c = a.add('4')
print 'a', a,' type of a ',type(a),' length of a ',len(a)

####################################################################
# 7. dictionary datatype - name:value pairs (associative array)
print '\nexplore dictionary datatype'
a = {'key1':2.5, 'key2':'abcdef', 'key3':3.4}
print 'a', a,' type of a ',type(a),' length of a ',len(a)
for c in a:
   print '\t',c,a[c]
   if a[c] == 3.4:
      print '\tfound value 3.4'
if 'key1' in a:  # search the keys only
   print '\tfound value key1 in a'
# key is not mutable; value is mutable
a['key1'] = 2.6
a['key4'] = 2.7
print 'a',a,' type of a ',type(a),' length of a ',len(a)
# dictionary comprehension; multiply value of key numbers by 2
a = {x: x*2 for x in range(1,10)}
print 'a', a,' type of a ',type(a),' length of a ',len(a)

####################################################################
# 8. int datatype - whole number division, round toward negative infinity
# Other numerical data types such as float, complex exist but are 
# not covered here.
print '\nexplore int datatype'
a = 7
b = 4
print '7/4 = ',a/b
a = -7
print '-7/4 = ',a/b
# check floor division operator //
a = 7
b = 4
print '7//4 = ',a//b
a = -7
print '-7//4 = ',a//b






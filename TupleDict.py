'''
tuple concept: Same as list but immutable
'''

val =(12,'aditya',30)
#for i in val:print(i)

'''
 as tuple is immutable on the below code line 
 we get error as TypeError: 'tuple' object does not support item assignment
'''
#val[2]="ZOPE"


"""
DICTIONARY DATATYPE
When we enter key or value as STRING then it should be entered in double quotes
"""

dic ={"a":2, 3:"bcd", 5:"ADITYA", "c":"Hello World!"}

#for i in dic:print(dic[i])

print(dic[3])

print(dic["c"])


dict ={}

dict["first name"]= "RAHUL"
dict["last name"] ="Shetty"
print(dict)

dict["gender"]="Male"
print(dict)
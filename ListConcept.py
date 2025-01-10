"""
Basics of List and its methods
"""
# L1=[10,20,30,40,50,"Aditya","Zope","Sanjay"]
#
# for i in L1:print(i)
#
# """
# list can be manipulated
# """
# print(L1[0:4])
#
# L1[2]="Ling Tong"
#
# print(L1)

values =["sanjay",0,12,13,'aditya']
print(values)

values.insert(0,'SANJAY')  #inserting data
print(values)

values.append("END")   #adding data to the end
print(values)

values[2] ="ZOPE"  #updating values
print(values)

del values[0]   #to delete value ata specific index
print(values)

print(values[-1])  #prints last index
print(values[1:3])   #prints values from index  1 to 2 and excludes index 3

print(values[-4])
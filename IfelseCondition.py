'''
working of if else condition in python
'''

greeting ="Good Morning"

if greeting == "Good Morning":
     print("Condition matches")
else:
     print("condition didnt match")
print("if else block completed")

'''
Use of for loop in python
'''

obj =[2,3,5,7,9]

#for i in obj:print(i*2)

 #range(i,j)-> i to j-1
 # sum of  first natural numbers 1+2+3+4+5=15
sum1 =0
for j in range(1, 6):
     sum1=sum1+j
print(sum1)

print("###################################################")
# if you dont pass index value then by default k value will be incremented by 1
for k in range(1,100,5):
          print(k)

print("###################################################")
#skipping first index will give us output as 0123456789
for m in range(10):
     print(m)
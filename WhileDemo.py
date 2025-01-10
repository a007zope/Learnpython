it =4;

# while it>1:
#     if it !=3:
#         print(it)
#     it = it-1
#
# print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

'''
if your condition is met and now you want to come out of the code then use break keyword
'''
while it>1:
    if it ==3:
        print(it)
        break
    print(it)
    it = it-1

print('While loop execution is done')


'''
usage of continue statement: After continue statement it won't execute below code i e it will skip current or that particular iteration steps and 
it will continue with  the next iteration
'''
t =10
while t>1:
    if t ==9:
        t = t-1
        continue
    if t ==3:
        break
    print(t)
    t = t-1
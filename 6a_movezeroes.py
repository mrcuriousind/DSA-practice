nums = [0,1,0,3,12]
x = 0
temp = []
for i in nums:
    if i == 0:
        x +=1
    else:
        temp.append(i)
nums = temp + [0] * x
print(nums)
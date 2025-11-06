nums = [2, 7, 11, 15]
target = 9
temp = {}
for i in range(len(nums)):
    x=nums[i]
    temp[x] = i
    y = target - x
    if y in temp:
       print(x,y)
    
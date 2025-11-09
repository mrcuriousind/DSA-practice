nums = [2, 7, 11, 15]
target = 9
result= []
for i in range(len(nums)):
    x = nums[i]
    for j in range(len(nums)):
        y = nums[j]
        if i < j:
            if x+y == target:
                result.append(x)
                result.append(y)
print(result)

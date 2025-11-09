nums = [1, 2, 3, 1]
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1   # count how many times each number appears
    
print(freq)
        
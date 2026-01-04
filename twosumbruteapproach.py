def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

# 👇 Call the function and print the result
nums = [2, 7, 11, 15, 5]
target = 20 
print(twoSum(nums, target))
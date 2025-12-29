def twoSum(nums, target):
    seen = {}  # number -> index

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i

# 👇 Call the function and print the result
nums = [2, 7, 11, 15, 5]
target = 20
print(twoSum(nums, target))

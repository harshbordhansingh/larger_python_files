def sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key


nums = []
n = int(input("Enter numbers of elements:"))
for i in range(0, n):
    ele = int(input())
    nums.append(ele)
sort(nums)
print(nums)
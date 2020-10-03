def sort(nums):
    for i in range(n):
        minpos = i
        for j in range(i, n):
            if nums[j] < nums[minpos]:
                minpos = j

            temp = nums[i]
            nums[i] = nums[minpos]
            nums[minpos] = temp


nums = []
n = int(input("Enter numbers of elements:"))
for i in range(0, n):
    ele = int(input())
    nums.append(ele)
sort(nums)
print(nums)
nums = list(int(i) for i in input().split('+'))

nums.sort()
print(nums)
print('+'.join(str(i) for i in nums))
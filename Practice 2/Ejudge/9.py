a = int(input())
nums = list(map(int, input().split()))

mx = max(nums)
mn = min(nums)

for i in range(len(nums)):
    if nums[i] == mx:
        nums[i] = mn

print(*nums)
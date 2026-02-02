a = int(input())
nums = list(map(int, input().split()))

max = nums[0]
pos = 0 

for i in range(1, a):
    if max < nums[i]:
        max = nums[i]
        pos = i
        
print(pos+1)
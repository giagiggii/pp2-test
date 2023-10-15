def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

n=input()
num=list(map(int, n.split()))
result = spy_game(num)
print(result)  

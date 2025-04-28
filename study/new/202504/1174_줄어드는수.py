import sys
input = sys.stdin.readline

def gen():
    res = [i for i in range(10)]
    
    for len_ in range(2, 11):
        back(len_, 0, 0, res)
    
    return sorted(res)

def back(len_, idx, num, res):
    if idx == len_:
        res.append(num)
        return
    
    s = 1 if idx == 0 else 0
    e = 10
    
    if num > 0:
        prev = num % 10
        e = prev
    
    for x in range(s, e):
        back(len_, idx + 1, num * 10 + x, res)

def sol(n):
    nums = gen()

    if n > len(nums):
        return -1
    
    return nums[n-1]

n = int(input())
print(sol(n))
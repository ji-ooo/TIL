def solve(k):
    len_ = 1
    cnt = 0
    
    while cnt + 2**len_ < k:
        cnt += 2**len_
        len_ += 1
    
    pos = k - cnt - 1
    
    bi = bin(pos)[2:].zfill(len_)
    ans = ''
    
    for d in bi:
        if d == '0':
            ans += '4'
        else:
            ans += '7'
    
    return ans

k = int(input())

print(solve(k))
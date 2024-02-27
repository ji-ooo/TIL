X =list(map(str, input()))
ans = ''

i = 0
tmp = 0
while i < len(X):
    if X[i] == 'X':
        tmp += 1
        
    elif X[i] == '.':
        if tmp:
            if tmp%2 == 0:
                while tmp > 0:
                    if tmp >= 4:
                        ans += 'AAAA'
                        tmp -= 4
                    else:
                        ans += 'BB'
                        tmp -= 2
            else:
                ans = -1
                break
        
        ans += '.'
    i += 1
    
if tmp:
    if tmp%2 == 0:
        while tmp > 0:
            if tmp >= 4:
                ans += 'AAAA'
                tmp -= 4
            else:
                ans += 'BB'
                tmp -= 2
    else:
        ans = -1
print(ans)
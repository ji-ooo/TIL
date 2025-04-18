N = int(input())
arr = list(map(int, input().split()))
M = int(input())


def sol(N, M):
    ex_0 = co_0 = 1e9
    ex_idx = co_idx = 0

    for i in range(N-1, -1, -1):
        if co_0 > arr[i]:
            co_0 = arr[i]
            co_idx = i

            if i != 0:
                ex_0 = arr[i]
                ex_idx = i

    if ex_0 > M:
        return 0

    ans = [ex_idx]
    M -= ex_0
    
    if M:
        cnt = M // co_0
        ans.extend([co_idx for _ in range(cnt)])
        M -= co_0 * cnt
    
    length = len(ans)

    for i in range(length):
        now = ans[i]
        cost = arr[now]

        for nxt in range(N-1, -1, -1):
            nxt_cost = arr[nxt]
            diff = nxt_cost - cost

            if diff <= M:
                ans[i] = nxt
                M -= diff
                break
                
        if M == 0:
            break
    
    return int(''.join(map(str, ans)))


print(sol(N, M))

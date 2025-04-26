def sol(N, K):
    # 길이가 1이면 교환 불가능
    if len(N) == 1:
        return -1
    
    length = len(N)

    # 0으로 시작하는 숫자는 만들 수 없음 (문제 조건)
    if length == 2 and 0 in N:
        return -1
    
    # 앞에서 부터 교환, 교환하는 위치 저장하는 인덱스
    idx = 0
    # 위치를 바꾼 숫자가 중복되었는지 체크해야 함
    dupl = {}

    # idx가 끝까지 / K번 다 교환할 때 까지
    while idx < length and K > 0:
        # 현재 위치 이후부터 최댓값 찾기
        max_val = max(N[idx:])

        # 현재 값이 최대면 pass
        if max_val == N[idx]:
            idx += 1
            continue
        
        max_idx = idx

        # 뒤에서부터 최댓값 위치 찾기
        # 작은 수 뒤로 <--> 큰 수 앞으로 교환이라 뒤에서 부터 찾는게 유리하다
        for i in range(length-1, idx-1, -1):
            if N[i] == max_val:
                max_idx = i
                break
        
        # 교환 한 숫자의 원래 위치 저장
        if max_val not in dupl:
            dupl[max_val] = []
        dupl[max_val].append(max_idx)

        # 현재 값이랑, 최댓값 위치 교환
        N[idx], N[max_idx] = N[max_idx], N[idx]
        K -= 1
        idx += 1

    # 중복된 숫자를 교환하면, 교환한 수 끼리는 내림차순 정렬을 해줘야 함
    # 31299를 2번 바꾸면, 99213이 되어버리는데, 뒤에 1이랑 3은 서로 위치 바꿀 수 있음
    for _, pos in dupl.items():
        if len(pos) <= 1:
            continue
        
        now_v = []
        now_p = []

        for p in pos:
            if p >= idx:
                now_v.append(N[p])
                now_p.append(p)

        # reverse안하고 정렬, 숫자 바꿀 때 위치를 append했기 때문에 pos가 역순으로 들어있음
        now_v.sort()

        for i, p in enumerate(now_p):
            if i < len(now_v):
                N[p] = now_v[i]

    # 변경 다 한 뒤에 K가 남아있고, 홀수면 끝에 두 자리 스위칭
    if len(set(N)) == length and K and K%2:
        N[-1], N[-2] = N[-2], N[-1]

    return ''.join(map(str, N))


N, K = input().split()
N = list(map(int, N))
K = int(K)

print(sol(N, K))

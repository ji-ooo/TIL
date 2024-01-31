H, T, C, K, G  = map(int, input().split())
M = int(input())

choco_list = ['H','T','C','K','G']
choco_cnt = {'H':H,'T':T,'C':C,'K':K,'G':G}

total = H+T+C+K+G

for _ in range(M):
    H, T, C, K ,G = map(int, input().split())
    choco_cnt['H'] -= H
    choco_cnt['T'] -= T
    choco_cnt['C'] -= C
    choco_cnt['K'] -= K
    choco_cnt['G'] -= G
    
    tmp = total % 10 # 1의자리
    total = sum(list(choco_cnt.values()))
    
    cnt_list = list(choco_cnt.items())
    cnt_list.sort(key=lambda x: (-x[1], x[0]))

    # 1의자리가 0, 1이면 result에 str로 반환
    # 아니면 tmp진법으로 수정
    if tmp == 0 or tmp == 1:
        result = str(total)
    else:
        i = 0
        while tmp**i <= total:
            i += 1
        i -= 1

        tmp_total = total
        tmp_result = ''
        for j in range(i, -1, -1):
            if tmp_total >= tmp**j:
                tmp_result += str(tmp_total//tmp**j)
                tmp_total -= tmp**j * (tmp_total//tmp**j)
            else:
                tmp_result += '0'
        result = tmp_result

        if result == '':
            result = '0'
    print(result +'7H')

    tmp_cnt_list = ''
    for cnt in cnt_list:
        if cnt[1] != 0:
            tmp_cnt_list += cnt[0]

    if tmp_cnt_list:
        print(tmp_cnt_list)
    else: print('NULL')


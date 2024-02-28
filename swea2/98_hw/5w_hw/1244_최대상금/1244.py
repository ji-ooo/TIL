import sys
sys.stdin = open('1244.txt')

for tc in range(1, int(input())+1):
    # N, c => 숫자, 교환 횟수
    N, c = input().split()

    # 교환 횟수 정수형으로
    c = int(c)

    # 숫자 자릿수대로 리스트에 저장
    N = list(map(int, N))

    # 리스트 복사 및 정렬 => 교환 횟수가 적절하게 있다면, 정렬된 리스트가 정답
    srt_N = N[:]
    srt_N.sort(reverse=True)

    # 중복된 수가 있는지 체크하기 위해
    st_N = set(N)

    # 맨 앞자리로 가장 높은 수를 가져오는 것이 가장 기본적이라 생각
    # 현재 자리를 pos에 저장, 가장 높은 수가 현재 위치에 올 때 마다 한 자리씩 뒤로 이동
    pos = 0

    # 교환 횟수가 남아있는 동안
    while c > 0:
        # 현재 변경하려는 자리가 마지막 자리일 경우, 정렬이 다 되었다는 의미
        if pos == len(N)-1:
            # 남은 교환 횟수는 숫자에 중복된 수가 있다면 의미 없음 (서로 교환하면 됨)
            if len(N) != len(st_N):
                result = N
            else:
                # 중복된 수가 없다면 교환횟수 % 2 의 결과에 따라
                # 마지막 두 자리를 바꾸거나, 그대로 유지
                if c % 2 == 1:
                    N[-2], N[-1] = N[-1], N[-2]
                result = N
            # 교환 횟수에 상관 없이, 정답이 나왔으므로 break
            break

        # (현재 변경하려는 자리의 수)가 (정답의 같은 위치에 있는 수)와 다를 경우
        if N[pos] != srt_N[pos]:
            # 바꿀 지점을 찾을 변수
            target = 0

            # 보통의 경우, 멀리 있는 큰 수를 앞으로 가져오는 것이 유리
            # 뒤에서부터 순회
            for i in range(len(N)-1, -1, -1):
                # 변경 횟수가 1보다 많을 때,
                # 맨 앞으로 와야하는 수가 하나 이상일 경우
                # 한 번의 교환으로 정답에 일치하도록 하는 수를 찾아줌

                # ex)
                # 32888의 경우, 정답 리스트는 88832인데
                # 한 번 교환으로는 82883이 이득이지만
                # 위에서 한 번 더 교환해서는 88832를 만들 수 없다
                # 가장 멀리 있는 수 대신 교환하려는 수의 자리가 둘 다 일치할 때 인덱스를 target에 저장
                if N[i] == srt_N[pos] and N[pos] == srt_N[i] and c > 1:
                    target = i
                    break

            # 일치하는 자리가 없거나 교환 횟수가 1이라면
            # 멀리서부터 찾으며 인덱스를 target에 저장
            else:
                for i in range(len(N) - 1, -1, -1):
                    if N[i] == srt_N[pos]:
                        target = i
                        break

            # 현재 위치와 target 자리 교환
            N[pos], N[target] = N[target], N[pos]

            # 교환 횟수 -1
            c -= 1

        # 현재 자리수가 가장 최적의 값인 경우 or 자리를 교환 하고 최적으로 만든 경우 다음 자리로 이동
        pos += 1

    # 교환 횟수를 다 끝내고 while을 종료했을 때 결과 업데이트
    if c == 0:
        result = N

    print(f'#{tc}', ''.join(map(str, result)))
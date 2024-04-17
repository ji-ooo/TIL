import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for tc in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dp = [0] * (target+1)
    for coin in coins:
        dp[coin] = 1


    print(dp)
    '''
        target 을 만드는 방법 경우의 수 출력
    1 2
    2 3 / 3 4
    3 4 / 4 5 / 4 5 / 5 6
    
    '''
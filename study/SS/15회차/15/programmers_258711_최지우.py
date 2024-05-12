# 도넛과 막대그래프 lv2
from collections import deque


def solution(edges):
    answer = []

    edge = {}
    node = set()
    end_p = set()
    max_num = 0
    for s, e in edges:
        if s in edge:
            edge[s].append(e)
        else:
            edge[s] = [e]

        node.add(s)
        node.add(e)
        end_p.add(e)
        max_num = max(max_num, s, e)

    new_node = (node-end_p).pop()
    answer.append(new_node)
    print(edge)
    
    return answer

'''
    input: [방향 있는 간선 edges]
    output: [생성한 정점 번호, 도넛, 막대, 8자 그래프 수]
    
    나가는 점만 2개 이상 가진 정점: 생성한 부분
    나가는 점 2 들어오는 점 2 정점 => 도넛 두개 나오면 8자
    들어오는 점 1 => 마지막에 원점으로 오면 도넛 / 나가는 점 없어지면 막대
    
'''

edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
# edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

print(solution(edges))
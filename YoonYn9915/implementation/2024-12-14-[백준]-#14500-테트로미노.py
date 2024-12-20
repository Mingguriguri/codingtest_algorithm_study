'''
1. 완전 탐색으로 진행
    1.1 문제 요건에 따라 최악의 경우는
        500 * 500 * 5(테트로미노 종류) * 4(90도 회전 경우의 수) * 4(대칭한 후 90도 회전 경우의 수).
        N(1억)이 1초라고 가정한다면 2초면 충분하다고 판단.
2. 테트로미노의 종류별로, 회전과 대칭의 경우의 수를 모두 고려하여 모양 리스트를 만든다.
3. 이중 반복문에서 모든 칸을 순회하며 모든 모양 리스트를 검사하여 최댓값을 찾는다.

'''

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 가능한 모든 테트로미노 모양, 시작점을 기준으로 더해야 할 dx, dy임.
shape = [[(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)],
         [(0, 1), (1, 0), (1, 1)],
         [(1, 0), (1, 1), (2, 1)], [(0, -1), (1, -1), (1, -2)],
         [(1, 0), (1, -1), (2, -1)], [(0, 1), (1, 1), (1, 2)],
         [(1, 0), (2, 0), (2, 1)], [(0, 1), (0, 2), (1, 0)],
         [(0, 1), (1, 1), (2, 1)], [(0, 1), (0, 2), (-1, 2)],
         [(1, 0), (2, 0), (2, -1)], [(0, 1), (0, 2), (1, 2)],
         [(1, 0), (2, 0), (0, 1)], [(1, 0), (1, 1), (1, 2)],
         [(1, 0), (1, 1), (1, -1)], [(1, 0), (1, 1), (2, 0)],
         [(0, -1), (1, 0), (0, 1)], [(0, 1), (-1, 1), (1, 1)]
         ]


def calc(i, j, tet):
    sum = arr[i][j]
    for dx, dy in tet:
        newX = i + dx
        newY = j + dy
        #종이의 범위를 넘지 않았다면 종이 칸의 수 더하기
        if 0 <= newX < N and 0 <= newY < M:
            sum += arr[newX][newY]
        else:
            return 0
    return sum


ans = 0
for i in range(N):
    for j in range(M):
        for tet in shape:
            temp = calc(i, j, tet)  # 현재 위치에서 가능한 모든 모양의 합 계산
            ans = max(temp, ans)

print(ans)

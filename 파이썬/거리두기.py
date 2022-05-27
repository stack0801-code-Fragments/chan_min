import queue

D = ((-1, 0), (1, 0), (0, -1), (0, 1)) #상, 하, 좌, 우 이동용 델타값

def bfs(p, row, col):
    vis = [[False for y in range(5)] for x in range(5)] #방문위치 기록용
    q = queue.Queue()
    vis[row][col] = True #체크에서 P의 경우 들어오기때문에 시작위치 P 마킹
    q.put((row, col ,0))

    while not q.empty():
        dist = q.get()
        if dist[2] > 2: #거리 2초과 -> 잘지킴
            continue
        if dist[2] != 0 and p[dist[0]][dist[1]] == "P": #거리 2이하에서 P 못만나면 밑에 과정 다 스킵
            return False
        for i in range(4): #4방향 탐색
            new_row = dist[0] + D[i][0]
            new_col = dist[1] + D[i][1]
            if new_row < 0 or new_row > 4 or new_col < 0 or new_col > 4: #스킵용 컨테뉴
                continue
            if vis[new_row][new_col]: #방문자 체크 -> 있으면 스킵
                continue
            if p[new_row][new_col] == "X":
                continue
            vis[new_row][new_col] == True #방문 마킹
            q.put((new_row, new_col, dist[2]+1)) 

def check_P(p):
    for i in range(5):
        for j in range(5):
            if p[i][j] == "P":
                if bfs(p, i, j) == False:
                    return False
    return True

def solution(places):
    answer = []
    for p in places:
        if check_P(p):
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

#실패한 코드
#def check(coordinates, room): #멘헤튼 거리 체크와 거리두기 검사
#    for m in coordinates:
#        for n in coordinates:
#            x1, y1, x2, y2 = m[0], m[1], n[0], n[1]
#            dist = abs(x1 - x2) + abs(y1 - y2)
#            if dist == 0:
#                continue
#            elif dist == 1:
#                return 0
#            elif dist == 2:
#                if x1 == x2:
#                    if room[x1][(y1+y2)//2] == "O":
#                        return 0
#                elif y1 == y2:
#                    if room[(x1+x2)//2][y1] == "O":
#                        return 0
#    return 1

#def solution(places):
#    answer = []
#    for i in range(5):
#        coordinates = []
#        room = places[i]
#        for j in range(5):
#            row = room[j]
#            for k in range(5):
#                if row[k] == "P":
#                    coordinates.append((j,k))
#        if check(coordinates, room) == 1:
#            answer.append(1)
#        else:
#            answer.append(0)

#    return answer

#import itertools

#def solution(places):
#    answer = []
#    for p in places:
#        p_location = [] #p의 위치
#        for x in range(5):
#            for y in range(5):
#                if p[x][y] == "P":
#                    p_location.append((x, y))
                    #print("잘 지킨 사람들 위치 : ", p_location);
#        ok = 1 #모두가 잘지키고 있다면 1 아닌 씹새들 있으면 0
#        combin_arr = list(itertools.combinations(p_location, 2)) #p 2개의 위치 조합
        #print("조합 : ", combin_arr)

#        for i in range(len(combin_arr)):
#            x1, y1 = combin_arr[i][0][0], combin_arr[i][0][1]
#            x2, y2 = combin_arr[i][1][0], combin_arr[i][1][1]
#            distance = abs(x1 - x2) + abs(y1 - y2) #abs를 통해 절대값으로 멘헤튼 거리 구하기
            #print("거리 : ", distance)

#            if distance <= 2: #거리가 2이하로 앉으면 안되기 때문에 이상일때! 아래의 3조건을 만족하는거?
#                if x1 == x2 and p[x1][max(y1, y2) - 1] == "X" or y1 == y2 and p[max(x1, x2) - 1][y1] == "X" or abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
                    #1번 조건 : x1과 x2 사이의 거리가 2이상인데 중간에 파티션이 있는가? -> 가로
                    #2번 조건 : y1과 y1 사이의 거리가 2이상인데 중간에 파티션이 있는가? -> 세로
                    #3번 조건 : x1과 x2사이의 멘헤튼 거리가 1인가? y1과 y2사이의 멘헤튼 거리가 1인가? -> 대각선
#                    continue
#                ok = 0
#                break
#        answer.append(ok)
#    return answer
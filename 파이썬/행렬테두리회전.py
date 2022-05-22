def solution(rows, columns, queries):
    answer = []
    circle = []
    for i in range(rows): #1~36까지의 표 만들기
        circle.append([x for x in range(i*columns+1, (i+1) * columns + 1)])
        
    for q in queries:
        q = [i-1 for i in q] #0부터 1씩 빼주는 값

        arr = circle[q[0]][q[1]] #좌측 상단값 저장
        print("저장값 : ", arr)
        q_min = arr
        
        for i in range(q[0]+1, q[2]+1): #왼쪽 탐색
            circle[i-1][q[1]] = circle[i][q[1]]
            q_min = min(q_min, circle[i][q[1]]) #자리 바꿀때마다 작은거 비교
            print("왼쪽 탐색 중 작은 값 : ", q_min)

        for i in range(q[1] + 1, q[3] + 1): #아래쪽 탐색
            circle[q[2]][i-1] = circle[q[2]][i]
            q_min = min(q_min, circle[q[2]][i]) #자리 바꿀때마다 작은거 비교
            print("아래쪽 탐색 중 작은 값 : ", q_min)
        
        for i in range(q[2] - 1, q[0] - 1, -1): #오른쪽 탐색
            circle[i+1][q[3]] = circle[i][q[3]]
            q_min = min(q_min, circle[i][q[3]]) #자리 바꿀때마다 작은거 비교
            print("오른쪽 탐색 중 작은 값 : ", q_min)
        
        for i in range(q[3] - 1, q[1] - 1, -1): #위쪽 탐색
            circle[q[0]][i+1] = circle[q[0]][i]
            q_min = min(q_min, circle[q[0]][i]) #자리 바꿀때마다 작은거 비교
            print("위쪽 탐색 중 작은 값 : ", q_min)
        
        circle[q[0]][q[1]+1] = arr

        answer.append(q_min)

    return answer
    

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
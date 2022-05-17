def solution(numbers, target):
    answer= [0]
    for i in numbers: #넘버스 길이만큼
        bfs_stack = [] #BFS 저장
        for j in answer : #j를 i의 0값만큼 빙글빙글
            bfs_stack.append(j+i) #0부터 numbers만큼 i를 더함
            bfs_stack.append(j-i) #0부터 numbers만큼 i를 뺌
        answer = bfs_stack #bfs값을 answer로 옴김
    return answer.count(target) #타겟넘버만 카운트함
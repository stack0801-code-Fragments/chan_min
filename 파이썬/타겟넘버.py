def solution(numbers, target):
    answer= [0]
    cnt = 0
    for i in numbers: #넘버스 길이만큼
        bfs_stack = [] #BFS 저장
        for j in answer : #j를 i의 0값만큼 빙글빙글
            bfs_stack.append(j+i) #0부터 numbers만큼 i를 더함
            bfs_stack.append(j-i) #0부터 numbers만큼 i를 뺌
        answer = bfs_stack #bfs값을 answer로 옴김
        print("값 : ", bfs_stack)

    for i in range(len(answer)):
        if(answer[i] == target):#타겟넘버만 카운트함
            cnt += 1
    #return answer.count(target) -> count는 리스트내의 같은 수의 개수만을 샘
    return cnt

print(solution([1,1,1,1,1], 3))
print(solution([4,1,2,1], 4))
def solution(priorities, location):
    #문서의 중요도가 순서대로 담긴 배열 priorities
    #내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location
    answer = 0
    while(len(priorities) != 0):
        if location == 0: #내꺼 출력한다!
            if priorities[0] < max(priorities): #더 중요한거 있음?
                priorities.append(priorities.pop(0)) # 맨 뒤로
                print("내꺼 출력 : ", priorities)
                location = len(priorities) - 1 
                #location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.
                print("내꺼 출력할떄 로케이신 위치 : ", location)
            else: #더 우선 없으니까 내꺼 출력함
                return answer + 1
        else: #아직 내꺼 출력 힘듬
            if priorities[0] < max(priorities): #더 중요한거 있음?
                priorities.append(priorities.pop(0)) #맨 뒤로
                print("뒤로 보낸 값 값 : ", priorities)
                location -= 1 #앞에꺼 출력했으니 로케값 줄임
                print("출력 후 로케값 : ", location)
            else:
                priorities.pop(0) #맨앞이 출력
                print("출력 값 : ",priorities)
                location -= 1 #앞에꺼 출력했으니 로케값 줄임
                print("출력 후 로케 값 : ", location)
                answer += 1 #출력번째수 +1


solution([2, 1, 3, 2], 2)
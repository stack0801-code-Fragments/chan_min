def solution(priorities, location):
    printer = [(i, p) for i,p in enumerate(priorities)] #queue : enumerate를 이용하여 i에는 인덱스 값을 p에는 실제 값을 담음 -> 튜플 제조
    answer = 0
    while printer:
        job = printer.pop(0) #제일 앞에꺼 빼넴
        if any(job[1] < other_job[1] for other_job in printer): #제일 1번이랑 other_job(프린터의 남은 job)을 비교
            printer.append(job)#중요하지 않으면 제일 뒤로
        else:
            answer += 1
            if job[0] == location: #우리가 찾는게 맞는가?
                break
    return answer


print(solution([2, 1, 3, 2], 2))
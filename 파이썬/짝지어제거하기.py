def solution(s):
    answer = []
    
    for i in range(len(s)):
        if not answer: #stack 없음? -> 첫번째 비교를 위한 한개 넣기
            answer.append(s[i])
        else:
            if s[i] == answer[-1]: #제일 뒤스텍이랑 비교
                answer.pop() #맞으면 제일뒤 나가
                print(answer)
            else:
                answer.append(s[i]) #아니면 i번째 뒤로 붙어
                print(answer)
    
    if answer: 
        return 0 #남음
    else: 
        return 1 #안남음
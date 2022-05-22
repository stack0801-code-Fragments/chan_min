def solution(s):
    answer = []
    cut_s = eval(s[1: -1]) #양끝 세트값 삭제 {}
    print(cut_s)
    if len(cut_s) > 1:
        cut_s = sorted(cut_s, key = lambda la : sum(la)) #더합 값들의 오름차순 정렬
        print(cut_s)
    else:
        return list(cut_s) #한개짜리는 알아서 리턴하라고 빼줌
    
    for i in cut_s:
        for j in i:
            if j not in answer: #저장되어있지않는 값들만을 저장
                answer.append(j)

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
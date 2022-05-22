import re #정규식 표현용
import itertools #순열 및 조합 제조용

def solution(expression):
    operators = itertools.permutations(["-", "+", "*"], 3) #순열 제조
    expression = re.split("([-+*])", expression) #문자열 파싱
    print(expression)

    answer = []
    for i in operators:
        ex = expression[:]
        for j in i: #연산자 우선순위
            while j in ex:
                idx = ex.index(j)#연산자 위치
                ex[idx-1] = str(eval(ex[idx-1] + j + ex[idx+1])) #계산
                del ex[idx:idx+2]#삭제
        answer.append(abs(int(ex[0])))
    return max(answer)

print(solution("100-200*300-500+20"))
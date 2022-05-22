import re #정규식 표현용
import itertools #순열 및 조합 제조용

def solution(expression):
    operators = itertools.permutations(["-", "+", "*"], 3) #순열 제조
    expression = re.split("([-+*])", expression) #문자열 파싱
    print(expression)

    answer = []
    for operater in operators:
        exp = expression[:]
        for op in operater: #연산자 우선순위
            while op in exp:
                idx = exp.index(op)#연산자 위치
                exp[idx-1] = str(eval(exp[idx-1] + op + exp[idx+1])) #계산
                del exp[idx:idx+2]#삭제
        answer.append(abs(int(exp[0])))
    return max(answer)

print(solution("100-200*300-500+20"))
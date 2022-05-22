def cut(p): #p -> u, v로 분리
    open_p = 0 #시작 괄호
    close_p = 0 #종료 괄호
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1 #시작 괄호 개수
        else:
            close_p += 1 #종료 괄호 개수
        if open_p == close_p:
            print("괄호 동일할때 : ", p[:i + 1], p[i + 1:])
            return p[:i + 1], p[i + 1:]


def SaC(u): #u의 올바른 괄호인지 검사하며 체크
    stack = []
    for i in u:
        if i == '(':
            stack.append(i) #정상이면 스택에 추가
            print("정상인 스텍 : ", stack)
        else:
            if not stack: #정상아니면 밴
                return False
            stack.pop()
    return True


def solution(p):
    if not p: #비어있으면 빈거 반환 
        return ""

    u, v = cut(p) #u, v로 나누기 -> 주의사항 : u가 분리될 여지가 남으면 안됨 잘못하면 v 빈거됨 

    if SaC(u): #u가 정상이면 v를 자시 검사함
        print("u가 정상일때 v : ", u + solution(v))
        return u + solution(v) #u에다가 v검사한거 붙임  
    else: #u가 정상이 아니면 시작
        answer = '(' #첫번째로 붙임
        answer += solution(v) #v를 재귀로 다시 검사
        print("u비정상일때 v : ", solution(v))
        answer += ')' #마지막에 붙임

        for p in u[1:len(u) - 1]: #u에서 첫번째랑 마지막 없애고 나머지 괄호 뒤집어서 뒤에
            if p == "(":
                answer += ")"
            else:
                answer += "("
        
        return answer

print("최종값 : ",solution("(()())()"))
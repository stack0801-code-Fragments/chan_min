def solution(n):
    answer = ''
    while n:
        if n % 3: #n이 3의 배수가 아니라면 3진법을 구하는 것과 동일 3으로 나눈 나머지를 저장, n을 3으로 나눈 몫으로 저장
            answer += str(n % 3)
            n //= 3
        else: #n이 3의 배수라면 무조건 4를 추가, n을 3으로 나눈 몫에서 1을 뺀 값을 저장
            answer += "4"
            n = n//3 - 1
    return answer[::-1] #역순으로 뒤집기
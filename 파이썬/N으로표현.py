def solution(N, number):
    answer = [[N]]
    if N == number:
        return 1

    for i in range(2, 9):
        for j in range(1, i // 2 + 1):
            N_stack = []
            for k in answer[j - 1]:
                for p in answer[i - j - 1]:
                    N_stack.append(k + p)
                    N_stack.append(k - p)
                    N_stack.append(p - k)
                    N_stack.append(p * k)
                    if k != 0:
                        N_stack.append(p / k)
                    if p != 0:
                        N_stack.append(k / p)
            N_stack.append(int(str(N) * i))
            N_stack = list(set(N_stack))
            if number in N_stack:
                return i
            answer.append(N_stack)
    return -1

#print(solution(5, 12))
solution(5, 12)
#5번 예제가 안됨 실패한거임
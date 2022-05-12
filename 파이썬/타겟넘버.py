def solution(numbers, target):
    answer = 0
    n = len(numbers)
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n :
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else :
            if temp == target :
                answer += 1
    return answer

#def solution(numbers, target): 
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
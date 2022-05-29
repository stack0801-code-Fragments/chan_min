def solution(numbers):
    answer = ""
    numbers = list(map(str, numbers)) #문자열로 바꿈
    sort_num = sorted(numbers, key = lambda x : x*3, reverse= True) #내일차순 정렬을 하는데 각 키값을 3번씩 반복해서 값을 설정해서 한다 
    answer = ''.join(sort_num)
    if int(answer) == 0: #11번이 틀려서 보니까 0000이 처들어가서 문제라서 이걸 int형으로 한번바꾸면 0 하나로 귀결됨
        answer = "0"

    return answer
    
print(solution([3, 30, 34, 5, 9]))
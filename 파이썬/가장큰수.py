def solution(numbers):
    
    numbers = list(map(str,numbers))
    sort_num = sorted(numbers, key = lambda x : x*3, reverse= True)
    answer = ''.join(sort_num)
    if int(answer) == 0:
        answer = '0'

    return answer



def solution(numbers):
    numbers = list(map(str, numbers)) #문자열로 바꿈
    numbers.sort(key = lambda x : x*3, reverse=True) 
    #내일차순 정렬을 하는데 각 키값을 3번씩 반복해서 값을 설정해서 한다 
    #[3, 30, 34, 5, 9] -> 역정렬 -> [9,5,34,30,3] -> 3배씩 -> [999,555,343434,303030,333]
    #이게 문자열 시점에서 보면 첫번째거 비교하고 두번째꺼를 비교하는데 0~1000까지만 하기때문에 자릿수 넘는건 무시됨
    return str(int(''.join(numbers))) #정렬을 하는데 중간에 11번이 틀려서 보니까 0000이 처들어가서 문제라서 이걸 int형으로 한번 바꾸면 0 하나로 귀결됨
    
print(solution([3, 30, 34, 5, 9]))
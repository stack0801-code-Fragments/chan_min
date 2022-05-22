def solution(str1, str2):
    answer = 0
    set1 = []
    set2 = []
    for i in range(len(str1)-1): #문자열을 끊어서 다중집합으로 만들기
        str_arr = str1[i] + str1[i + 1]
        if str_arr.isalpha(): #알파벳인지 숫자인지 확인
            set1.append(str_arr.upper())
    for j in range(len(str2)-1): #문자열을 끊어서 다중집합으로 만들기
        str_arr = str2[j] + str2[j + 1]
        if str_arr.isalpha(): #알파벳인지 숫자인지 확인
            set2.append(str_arr.upper())

    count = 0 #교집합, 합집합 원소의 개수 구하기
    set_arr = set2.copy()
    for k in set1:
        if k in set_arr:
            count += 1
            set_arr.remove(k)
    count_union = len(set1) + len(set2) - count
    
    #자카드 유산도 계산
    if count_union == 0:
        answer = 1 * 65536
    else:
        answer = int(count * 65536 / count_union)
    return answer

print(solution("FRANCE", "french"))
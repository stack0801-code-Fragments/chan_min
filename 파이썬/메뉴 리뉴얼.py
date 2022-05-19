import itertools #combinations는 하나의 리스트 내에서 모든 조합을 구하는 라이브러리
import collections #Counter를 통해 리스트 내의 중복값을 모두 카운트한다

def solution(orders, course): #course만큼 반복 ex)[2,3,4]->2개 조합 3개조합 4개조합같은 형식
    answer = []
    for i in course:
        order_backup = []
        for j in orders: #오더 수만큼 반복
            com = itertools.combinations(sorted(j), i) #정렬하면서 오더 수만큼 코스 조합
            print("재조합 : ", com)
            order_backup += com
        cnt = collections.Counter(order_backup) #조합수 카운트
        print("카운터 : ", cnt)
        if len(cnt) != 0 and max(cnt.values()) != 1: #조합 안나오거나 주문한 사람이 한명 뿐이면 무시
            answer += [''.join(k) for k in cnt if cnt[k] == max(cnt.values())] #가장 많이 주문한거 추가
        
    print("추가할 코스 : ", answer)

    return sorted(answer)


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
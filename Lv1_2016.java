class Solution {
    public String solution(int a, int b) {
        String answer = "";
        String[] day = { "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU" };//2016년 1월 1일은 금요일 시작
        int[] date = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
                        //각각의 1~12(0~11)까지의 번호에 수룰 배부
        int allDate = 0;//지정 날짜까지의 일수
        for (int i = 0; i < a - 1; i++) {//지정일 전날까지
            allDate += date[i];//지정월의 전월의 모든 일수를 더함
        }
     allDate += (b - 1);//해당 개월의 그날까지의 진행
     answer = day[allDate % 7];//7로 나눈 수로 요일을 구함
        return answer;
    }
}

public class Lv1_2016 {
    public static void main(String[] args) {
        
    }
}

/*
// 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
// 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
import java.util.*;

class TryHelloWorld
{
    public String getDayName(int month, int day)
    {
        Calendar cal = new Calendar.Builder().setCalendarType("iso8601")
                        .setDate(2016, month - 1, day).build();
        return cal.getDisplayName(Calendar.DAY_OF_WEEK, Calendar.SHORT, new Locale("ko-KR")).toUpperCase();
    }
    public static void main(String[] args)
    {
        TryHelloWorld test = new TryHelloWorld();
        int a=5, b=24;
        System.out.println(test.getDayName(a,b));
    }
}
*/
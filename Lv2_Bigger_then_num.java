import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        ArrayList<String> strNum = new ArrayList(); // int -> String 배열변경
        for(Integer num : numbers){
            strNum.add(String.valueOf(num));
        }// 내림차순 정렬
        Collections.sort(strNum, (a, b) -> (b + a).compareTo(a + b));// 0이 중복이 되면 0 하나만 리턴
        if(strNum.get(0).startsWith("0")) return "0";// answer에 정렬된 것을 넣음
        for(String s : strNum){
            answer += s;
        }
        return answer;
    }
}

public class Lv2_Bigger_then_num {
    
}

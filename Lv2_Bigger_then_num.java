import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        ArrayList<String> strNumbers = new ArrayList(); // int -> String 배열변경
        for(Integer num : numbers){
            strNumbers.add(String.valueOf(num));
        }// 내림차순 정렬
        Collections.sort(strNumbers, (a, b) -> (b + a).compareTo(a + b));// 0이 중복이 되면 0 하나만 리턴
        if(strNumbers.get(0).startsWith("0")) return "0";// answer에 정렬된 것을 넣음
        for(String s : strNumbers){
            answer += s;
        }
        return answer;
    }
}

public class Lv2_Bigger_then_num {
    
}

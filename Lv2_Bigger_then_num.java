import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        // int -> String 배열로
        ArrayList<String> strNumbers = new ArrayList();
        for(Integer num : numbers){
            strNumbers.add(String.valueOf(num));
        }
        // 내림차순 정렬
        Collections.sort(strNumbers, (a, b) -> (b + a).compareTo(a + b));
        // numbers가 [0,0,0] 등으로 주어지는 경우는 "000"이 아닌 "0" 리턴
        if(strNumbers.get(0).startsWith("0")) return "0";
        // answer에 정렬된 것을 담기
        for(String s : strNumbers){
            answer += s;
        }
        return answer;
    }
}

public class Lv2_Bigger_then_num {
    
}

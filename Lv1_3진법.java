class Solution {
    public int solution(int n) {
        String answer = "";
		
		while(n >= 3) { //3보다 크거나 같을때
			answer += n % 3;//n을 3으로 나눈 값의 나머지
			n /= 3;//3으로 나누고
		}
		answer += n;//나눈수를 더하고
		
		return Integer.parseInt(answer, 3);//출력
    }
}

public class Lv1_3진법 {
    
}

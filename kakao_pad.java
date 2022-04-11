class Solution {
    public String solution(int[] numbers, String hand) {
        StringBuilder sb = new StringBuilder();
		int left=10, right=12;
		int L_dis, R_dis;
		for(int n : numbers) {
			L_dis = 0; R_dis = 0;
			if(n == 1 || n == 4 || n == 7) { //1 4 7 왼손
				sb.append("L");
				left = n; //왼손 현재 위치
			
			}else if(n == 3 || n == 6 || n == 9) { //3 6 9 오른손
				sb.append("R");
				right = n;//오른손 현재 위치
			
			}else {
				if(n==0){
                    n += 11;
                }
				L_dis = (Math.abs(n-left))/3 + (Math.abs(n-left))%3;
				R_dis = (Math.abs(right-n))/3 + (Math.abs(right-n))%3;
				if(L_dis == R_dis) {
					if(hand.equals("right")) {
						sb.append("R");
						right = n;
					}else {
						sb.append("L");
						left = n;
					}
				}else if(L_dis > R_dis) {
					sb.append("R");
					right = n;
				}else {
					sb.append("L");
					left = n;
				}
			}
		}	
		return sb.toString();
    }

}
public static void main(String[] args) {
    
}
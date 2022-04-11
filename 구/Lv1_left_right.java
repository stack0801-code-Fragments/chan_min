public class Lv1_left_right {
    public static void main(String[] args) {
        
    }
    class Solution {
        public int solution(int left, int right) {
            int answer = 0;
            for(int i = left; i <= right; i++) {
                int cnt = 0;
                
                for(int j = 1; j <= i; j++) {
                    if(i % j == 0) {
                        cnt++;
                    }
                }
                if(cnt % 2 == 0) {
                    answer += i;
                }
                else {
                    answer -= i;
                }
            }
            return answer;
        }
    }
}

/*
class Solution {
    public int solution(int left, int right) {
        int sum = 0;
        for (int i = left; i <= right; i++) {
            sum += i * ((countDenominators(i) % 2 == 0) ? 1 : -1);
        }
        return sum;
    }
    private int countDenominators(int num) {
        int count = 0;
        for (int i = 1; i <= num; i++) if (num % i == 0) count++;
        return count;
    }
}
*/
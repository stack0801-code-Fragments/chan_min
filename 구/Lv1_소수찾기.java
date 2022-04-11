class Solution { 
    public int solution(int n) { 
        int answer = 0; 
        for(int i = 2; i <= n; i++){ 
            boolean b = true; 
            for(int j = 2; j*j <= i; j++){ //배수 지우기 
                 if(i % j == 0){ 
                     b = false; 
                     break; 
                    } 
                } 
                if(b){ 
                    answer++; 
                } 
            } 
            return answer; 
        } 
    }

/*
class Solution {
    public int solution(int n) {
        int answer = 0; 
        boolean[] sosu =new boolean [n+1]; 
        for(int i=2; i<=n ; i++) 
            sosu[i]=true; 
        //2~n번째수를 true로 초기화 
        //제곱근 구하기 
        int root=(int)Math.sqrt(n); 
        for(int i=2; i<=root; i++){ 
            //2~루트n까지 검사 
            if(sosu[i]==true){ 
                //i번째의 수가 소수일 때 
                for(int j=i; i*j<=n; j++) 
                    //그 배수들을 다 false로 초기화(배수는 소수가 아니기 때문) 
                    sosu[i*j]=false; 
            } 
        } 
        for(int i =2; i<=n; i++) { 
            if(sosu[i]==true) 
                //소수의 개수 세기 
                answer++; 
        } 
        return answer;
    }
}
*/
public class Lv1_소수찾기 {
    
}
//https://wooaoe.tistory.com/50
//에라토스테네스의 체 방식을 사용
//모든 수의 제곱근의 소수가 될수없으므로 1~10사이의 소수인 2,3,5,7을 제곱근로 적용하여 문제를 푼다
//자신을 제외한 2,3,5,7의 제곱근을 모두 적용하고 2,4,6,8,0으로 끝나는 모든 수를 제외하여 남은 수들이 소수들이다.
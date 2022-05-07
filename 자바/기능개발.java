class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] temp = new int[100];//작업의 개수는 100개 이하이므로 100으로 선언
        int day = -1;//temp에 적용할 배포일 수
        for(int i = 0; i < progresses.length; i++){
            while(progresses[i] + (speeds[i] * day) < 100){
                day++;
            }
            temp[day]++;
        }
        int cnt = 0;
        //temp에 들어간 배열의 길이를 알기위한 코드임. 
        //temp는 초기에 0으로 선언되어 있으므로 0이 아닌 값만 측정하면 됨.
        for(int n : temp){//temp배열 값을 하나식 n에 적용
            if(n != 0) cnt++; //배열 값이 0이 아니라면
        }
        
        int[] answer = new int[cnt];//답을 리턴하기 위한 배열 answer 선언
        
        cnt = 0;//count 0 초기화
        for(int n : temp){
            if(n != 0) answer[cnt++] = n;//answer 배열에 temp 값 넣기
        }
        return answer;
    }
}
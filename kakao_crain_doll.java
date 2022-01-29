import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;//중복 인형 제거횟수
        Stack<Integer> stack = new Stack<>();//인형 stack       
        
        for(int i =0;i<moves.length;i++){//moves = 크레인 총 이동횟수
            for(int j=0;j<board.length;j++){//j = 보드의 행을 탐색. 열은 moves의 원소 이용 탐색.
                if(board[j][moves[i]-1] != 0 ) {//j행의 moves의 크레인위치 열에 인형이 있으면                  
                    if(!stack.empty() && stack.peek() == board[j][moves[i]-1]){
                        //stack이 비어있지 않고, 현재 스택의 최상단에 있는 인형과 크레인으로 뽑은 인형이 같다면
                        answer++;//인형들을 제거 횟수
                        stack.pop();//바구니에 있는 인형 제거
                        board[j][moves[i]-1] = 0;//크레인으로 뽑은 인형을 0으로 초기화
                        break;   
                    }else{// 나머지 인형을 바구니에 담은 후 0으로 초기화 
                        stack.push(board[j][moves[i]-1]);                      
                        board[j][moves[i]-1] = 0;
                        break;
                    }
                }                        
            }
        }         
        return answer*2;//뽑은 인형의 수 = 인형을 뽑은 수 * 2.
    }
}

public class kakao_crain_doll {
    
}

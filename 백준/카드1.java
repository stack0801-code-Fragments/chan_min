package 백준;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 카드1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
 
        Queue<Integer> card = new LinkedList<Integer>();
        
        /* 1부터 n까지 카드 삽입 */
        for (int i = 0; i < n; i++) {
            card.add(i+1);
        }
        
        while (card.size() > 1) {
            System.out.print(card.poll() + " "); // 제일 위에 있는 카드 바닥에 버리기
            
            card.add(card.poll()); // 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기
        }
        
        System.out.println(card.poll());
    }
}
//qqqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqqqqqqq
///qqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqqqqqqq
///qqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqqqqqqq
///qqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqqqqqqq
///qqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqqqqqqq
///qqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqqqqqqq
///qqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqqqqqqq
///qqqqqqqqqqqqqqqqqqqqqqq
//qqqqqqqqqqqqqqqqqqqq

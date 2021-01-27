package ch3;
import java.util.Scanner;

public class ex3_2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int cnt = 0, n;
		double sum = 0;
		
		System.out.println("정수를 입력하고 마지막에 0을 입력");
		while((n = sc.nextInt()) != 0) {
			sum += n;
			cnt++;
		}
		System.out.println("수의 개수는 "+cnt+"개, 평균은 "+sum/cnt);
		sc.close();
	}

}

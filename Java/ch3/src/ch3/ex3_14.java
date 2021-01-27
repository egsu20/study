package ch3;
import java.util.InputMismatchException;
import java.util.Scanner;

public class ex3_14 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("정수 3개 입력");
		
		int sum = 0, n;
		for(int i = 0 ; i < 3 ; i++) {
			System.out.print(i+">>");
			try {
				n = sc.nextInt();
				sum+=n;
			}catch(InputMismatchException e) {
				System.out.println("정수가 아닙니다. 다시 입력하세요!");
				sc.next();
				i--;
				continue;
			}
		}
		System.out.println("합은 "+sum);
		sc.close();
	}

}

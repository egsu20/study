package ch3;
import java.util.InputMismatchException;
import java.util.Scanner;

public class ex3_14 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("���� 3�� �Է�");
		
		int sum = 0, n;
		for(int i = 0 ; i < 3 ; i++) {
			System.out.print(i+">>");
			try {
				n = sc.nextInt();
				sum+=n;
			}catch(InputMismatchException e) {
				System.out.println("������ �ƴմϴ�. �ٽ� �Է��ϼ���!");
				sc.next();
				i--;
				continue;
			}
		}
		System.out.println("���� "+sum);
		sc.close();
	}

}

package ch3;
import java.util.Scanner;

public class ex3_2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int cnt = 0, n;
		double sum = 0;
		
		System.out.println("������ �Է��ϰ� �������� 0�� �Է�");
		while((n = sc.nextInt()) != 0) {
			sum += n;
			cnt++;
		}
		System.out.println("���� ������ "+cnt+"��, ����� "+sum/cnt);
		sc.close();
	}

}

package ch3;

import java.util.Scanner;

public class ex3_5 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int sum = 0, n;
		
		System.out.println("���� 5���� �Է��Ͻÿ�");
		
		for(int i = 0 ; i < 5 ; i++) {
			n = sc.nextInt();
			if(n < 0) continue;
			sum += n;
		}
		System.out.println("����� ���� "+sum);
		
		sc.close();
	}

}

package ch3;

import java.util.Scanner;

public class ex3_5 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int sum = 0, n;
		
		System.out.println("정수 5개를 입력하시오");
		
		for(int i = 0 ; i < 5 ; i++) {
			n = sc.nextInt();
			if(n < 0) continue;
			sum += n;
		}
		System.out.println("양수의 합은 "+sum);
		
		sc.close();
	}

}

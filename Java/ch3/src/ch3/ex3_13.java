package ch3;

import java.util.Scanner;

public class ex3_13 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int dividend, divisor;
		
		System.out.print("나뉨수 : ");
		dividend = sc.nextInt();
		System.out.print("나눗수 : ");
		divisor = sc.nextInt();
		
		try {
			System.out.println(dividend+"/"+divisor+"="+(dividend/divisor));
		} catch(ArithmeticException e) {
			System.out.println("0으로 나눌 수 없습니다.");
		}
		finally {
			sc.close();
		}
	}

}

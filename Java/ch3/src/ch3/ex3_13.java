package ch3;

import java.util.Scanner;

public class ex3_13 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int dividend, divisor;
		
		System.out.print("������ : ");
		dividend = sc.nextInt();
		System.out.print("������ : ");
		divisor = sc.nextInt();
		
		try {
			System.out.println(dividend+"/"+divisor+"="+(dividend/divisor));
		} catch(ArithmeticException e) {
			System.out.println("0���� ���� �� �����ϴ�.");
		}
		finally {
			sc.close();
		}
	}

}

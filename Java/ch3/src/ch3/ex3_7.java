package ch3;

import java.util.Scanner;

public class ex3_7 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("양수 5개를 입력하세요");
		
		int arr[] = new int[5];
		int max = 0;
		
		for(int i = 0 ; i < arr.length ; i++) {
			arr[i] = sc.nextInt();
			if(arr[i] > max) max = arr[i];
		}
		System.out.println("가장 큰 수는 "+max+"입니다.");
		sc.close();
	}

}

package ch3;

public class ex3_1 {

	public static void main(String[] args) {
		int sum = 0;
		
		for(int i = 1 ; i <= 10 ; i++) {
			System.out.print(i);
			
			if(i<=9) System.out.print("+");
			
			sum += i;
		}
		
		System.out.println("="+sum);
	}

}

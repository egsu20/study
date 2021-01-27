package ch3;

public class ex3_9 {
	public static void main(String []args) {
		int [] n = {1,2,3,4,5};
		int sum = 0;
		
		for(int k : n) {
			System.out.print(k+" ");
			sum+=k;
		}
		System.out.println("гую╨ "+sum);
		
		String f[] = {"apple", "banana", "mango"};
		for(String s : f) {
			System.out.print(s+" ");
		}
	}
}

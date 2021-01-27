package ch3;

public class ex3_11 {
	static int[] makeArr() {
		int temp[] = {1,2,3,4};
		return temp;
	}
	
	public static void main(String[] args) {
		int intArr[] = makeArr();
		
		for(int i = 0 ; i < intArr.length ; i++) {
			System.out.print(intArr[i] + " ");
		}
	}

}


public class PrintStar {
	
	public static void main(String[] args) {
		int max = 5;
		
		for(int i = 0 ; i < max ; i++) {
			for(int star = 0 ; star < i+1 ; star++) {
				System.out.print("*");
			}
			for(int space = max-1 ; space > i-1 ; space--) { 
				System.out.print(" ");
			}
			for(int star = max-1 ; star > i-1 ; star--){
				System.out.print("*");
			}
			System.out.println();
		}
	
	
	for(int i = 1 ; i < max+1 ; i++) {
		for(int space = max-1 ; space > i-1 ; space--) {
			System.out.print(" ");
		}
		for(int star = 0 ; star < i ; star++) {
			System.out.print("*");
		}
		for(int space = 0 ; space < i-1 ; space++) {
			System.out.print(" ");
		}
		for(int star = max ; star > i-1 ; star--) {
			System.out.print("*");
		}
		System.out.println();
	}
		
	}
}

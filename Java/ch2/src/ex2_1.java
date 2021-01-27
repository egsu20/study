
public class ex2_1 {

	public static int sum(int n, int m) { 
		// static인 main에서 호출하므로 static이 되어야함.
		return n + m;
	}
	
	public static void main(String[] args) {
		int s;
		char a;
		
		s = sum(20, 10);
		System.out.println(s);
		a = '!';
		System.out.println("Hello"+a);
	}

}

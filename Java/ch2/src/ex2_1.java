
public class ex2_1 {

	public static int sum(int n, int m) { 
		// static�� main���� ȣ���ϹǷ� static�� �Ǿ����.
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

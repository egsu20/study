class Calc{
	public static int abs(int a) {
		return a>0?a:-a;
	}
	public static int max(int a, int b) {
		return a>b?a:b;
	}
	public static int min(int a, int b) {
		return a>b?b:a;
	}
}

public class ex4_11 {

	public static void main(String[] args) {
		System.out.println(Calc.abs(-3));
		System.out.println(Calc.max(3, 5));
		System.out.println(Calc.min(2, 7));
	}

}

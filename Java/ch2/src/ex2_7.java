
public class ex2_7 {

	public static void main(String[] args) {
		int a = 3, b = 3, c = 3;
		// 복합 대입 연산자
		a += 3;
		b *= 3;
		c %= 2;
		System.out.println("a=" + a + ", b=" + b + ", c=" + c);
		
		int d=3;
		// 증감 연산자
		a = d++;
		System.out.println("a=" + a + ", d="+d);
		a = ++d;
		System.out.println("a=" + a + ", d="+d);
		a = d--;
		System.out.println("a=" + a + ", d="+d);
		a = --d;
		System.out.println("a=" + a + ", d="+d);

	}

}

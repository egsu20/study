
public class ex6_8 {

	public static void main(String []args) {
		System.out.println(Math.abs(-3.14)); // 절댓값
		System.out.println(Math.sqrt(9.0)); // 제곱근
		System.out.println(Math.exp(2)); // e의 2승
		System.out.println(Math.round(3.14)); // 반올림
		
		System.out.print("이번주 행운의 번호는 ");
		for(int i = 0 ; i < 5 ; i++) {
			System.out.print((int)(Math.random()*45+1) + " "); // 1부터 45 사이의 난수
		}
	}
}

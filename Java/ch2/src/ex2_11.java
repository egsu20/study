import java.util.Scanner;
public class ex2_11 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("나이 : ");
		int age = sc.nextInt();
		if((age>=20) && (age <30)) {
			System.out.println("20대입니다.");
		}
		else System.out.println("20대가 아닙니다");

		sc.close();
	}

}

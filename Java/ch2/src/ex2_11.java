import java.util.Scanner;
public class ex2_11 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("���� : ");
		int age = sc.nextInt();
		if((age>=20) && (age <30)) {
			System.out.println("20���Դϴ�.");
		}
		else System.out.println("20�밡 �ƴմϴ�");

		sc.close();
	}

}

import java.util.Scanner; 

public class ex2_5 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.print("�̸� : ");
		String name = sc.next();
		System.out.print("���� : ");
		String city = sc.next();
		System.out.print("���� : ");
		int age = sc.nextInt();
		System.out.print("ü�� : ");
		double weight = sc.nextDouble();
		System.out.print("���� ���� (true/false): ");
		boolean single = sc.nextBoolean();
		
		sc.close();
		
		System.out.println(name+", "+city+", "+age+", "+weight+", "+single);
	}

}

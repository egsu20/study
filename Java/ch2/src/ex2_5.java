import java.util.Scanner; 

public class ex2_5 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.print("이름 : ");
		String name = sc.next();
		System.out.print("도시 : ");
		String city = sc.next();
		System.out.print("나이 : ");
		int age = sc.nextInt();
		System.out.print("체중 : ");
		double weight = sc.nextDouble();
		System.out.print("독신 여부 (true/false): ");
		boolean single = sc.nextBoolean();
		
		sc.close();
		
		System.out.println(name+", "+city+", "+age+", "+weight+", "+single);
	}

}

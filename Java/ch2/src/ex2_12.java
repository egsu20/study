import java.util.Scanner;

public class ex2_12 {

	public static void main(String[] args) {
		char grade;
		Scanner sc = new Scanner(System.in);
		
		System.out.print("���� �Է�(0~100) : ");
		int score = sc.nextInt();
		
		if(score >= 90) grade='A';
		else if(score >= 80) grade = 'B';
		else if(score >= 70) grade = 'C';
		else grade = 'F';
		
		sc.close();
		System.out.println("����� ������ " + grade);
	}

}

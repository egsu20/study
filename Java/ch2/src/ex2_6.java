import java.util.Scanner;
public class ex2_6 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("���� �Է� : ");
		int time = sc.nextInt();
		
		System.out.print(time+"�ʴ� ");
		
		int second = time%60;
		time = time / 60;
		int min = time % 60;
		time = time / 60;
		int hour = time;
		
		System.out.print(hour+"�ð�, ");
		System.out.print(min+"��, ");
		System.out.print(second+"���Դϴ�.");
		sc.close();
	}

}

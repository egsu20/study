import java.util.Scanner;
public class ex2_6 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("정수 입력 : ");
		int time = sc.nextInt();
		
		System.out.print(time+"초는 ");
		
		int second = time%60;
		time = time / 60;
		int min = time % 60;
		time = time / 60;
		int hour = time;
		
		System.out.print(hour+"시간, ");
		System.out.print(min+"분, ");
		System.out.print(second+"초입니다.");
		sc.close();
	}

}

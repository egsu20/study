import java.util.StringTokenizer;
import java.util.Scanner;

public class ch4_4 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int sum = 0;
		
		String input = sc.nextLine(); // 공백 포함 한 줄 읽기
		
		StringTokenizer st = new StringTokenizer(input, "+");
		
		while(st.hasMoreTokens()) {
			String op = st.nextToken();
			int intVal = Integer.parseInt(op.trim());
			
			sum += intVal;
		}
		System.out.println("합은 " + sum);
		sc.close();

	}

}

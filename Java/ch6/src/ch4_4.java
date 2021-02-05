import java.util.StringTokenizer;
import java.util.Scanner;

public class ch4_4 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int sum = 0;
		
		String input = sc.nextLine(); // ���� ���� �� �� �б�
		
		StringTokenizer st = new StringTokenizer(input, "+");
		
		while(st.hasMoreTokens()) {
			String op = st.nextToken();
			int intVal = Integer.parseInt(op.trim());
			
			sum += intVal;
		}
		System.out.println("���� " + sum);
		sc.close();

	}

}

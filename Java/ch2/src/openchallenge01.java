import java.util.Scanner;

public class openchallenge01 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			System.out.println("����,����,�� �߿��� �Է�(����� bye)");
			
			System.out.print("A : ");
			String a = sc.next();
			System.out.print("B : ");
			String b = sc.next();
			
			if(a.equals("bye") || b.equals("bye")) break;
			
			switch(a) {
			case "����":
				if(b.equals("����")) 
					System.out.println("�����ϴ�.");
				else if(b.equals("����"))
					System.out.println("B�� �̰���ϴ�.");
				else
					System.out.println("A�� �̰���ϴ�.");
				break;
		
			case "����":
				if(b.equals("����")) 
					System.out.println("�����ϴ�.");
				else if(b.equals("��"))
					System.out.println("B�� �̰���ϴ�.");
				else
					System.out.println("A�� �̰���ϴ�.");
				break;
				
			case "��":
				if(b.equals("��")) 
					System.out.println("�����ϴ�.");
				else if(b.equals("����"))
					System.out.println("B�� �̰���ϴ�.");
				else
					System.out.println("A�� �̰���ϴ�.");
				break;
			}
		}
		
		sc.close();
	}

}

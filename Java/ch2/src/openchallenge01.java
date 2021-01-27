import java.util.Scanner;

public class openchallenge01 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			System.out.println("가위,바위,보 중에서 입력(종료는 bye)");
			
			System.out.print("A : ");
			String a = sc.next();
			System.out.print("B : ");
			String b = sc.next();
			
			if(a.equals("bye") || b.equals("bye")) break;
			
			switch(a) {
			case "가위":
				if(b.equals("가위")) 
					System.out.println("비겼습니다.");
				else if(b.equals("바위"))
					System.out.println("B가 이겼습니다.");
				else
					System.out.println("A가 이겼습니다.");
				break;
		
			case "바위":
				if(b.equals("바위")) 
					System.out.println("비겼습니다.");
				else if(b.equals("보"))
					System.out.println("B가 이겼습니다.");
				else
					System.out.println("A가 이겼습니다.");
				break;
				
			case "보":
				if(b.equals("보")) 
					System.out.println("비겼습니다.");
				else if(b.equals("가위"))
					System.out.println("B가 이겼습니다.");
				else
					System.out.println("A가 이겼습니다.");
				break;
			}
		}
		
		sc.close();
	}

}

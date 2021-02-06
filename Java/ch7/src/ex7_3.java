import java.util.*;

public class ex7_3 {

	public static void main(String[] args) {
		ArrayList<String> a = new ArrayList<String>();
		
		Scanner sc = new Scanner(System.in);
		
		for(int i = 0 ; i < 4 ; i++) {
			System.out.print("이름 입력 >> ");
			a.add(sc.next());
		}
		
		for(int i = 0 ; i < 4 ; i++) 
			System.out.print(a.get(i)+" ");
		System.out.println();
		
		String longName = "";
		for(int i = 0 ; i < 4 ; i++) {
			String name = a.get(i);
			if(longName.length() < name.length())
				longName = name;
		}
		
		System.out.println("가장 긴 이름은 : " + longName);
		
		sc.close();
	}

}

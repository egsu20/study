
public class ex6_6 {

	public static void main(String[] args) {
		String a = new String(" C#");
		String b = new String(",C++ ");
		
		System.out.println(a + "�� ���̴� " + a.length());
		System.out.println(a.contains("#"));
		
		a = a.concat(b); // ����
		System.out.println(a); 
		
		a = a.trim(); // �� �� ���� ����
		System.out.println(a);
		
		a = a.replace("C#", "Java");
		System.out.println(a);
		
		String s[] = a.split(","); // ,�� �������� �и�
		for (int i = 0 ; i < s.length ; i++)
			System.out.println(i+ " : " + s[i]);
		
		a = a.substring(5); // 5�� �ε������� ����
		System.out.println(a);
		
		char c = a.charAt(2); // 2�� �ε��� �� ����
		System.out.println(c);

	}

}

public class ex6_6 {

	public static void main(String[] args) {
		String a = new String(" C#");
		String b = new String(",C++ ");
		
		System.out.println(a + "의 길이는 " + a.length());
		System.out.println(a.contains("#"));
		
		a = a.concat(b); // 연결
		System.out.println(a); 
		
		a = a.trim(); // 앞 뒤 공백 제거
		System.out.println(a);
		
		a = a.replace("C#", "Java");
		System.out.println(a);
		
		String s[] = a.split(","); // ,를 기준으로 분리
		for (int i = 0 ; i < s.length ; i++)
			System.out.println(i+ " : " + s[i]);
		
		a = a.substring(5); // 5번 인덱스부터 리턴
		System.out.println(a);
		
		char c = a.charAt(2); // 2번 인덱스 값 리턴
		System.out.println(c);

	}

}

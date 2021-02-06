import java.util.*;

public class ex7_5 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		HashMap<String, String> dic = new HashMap<String, String>();
		dic.put("love","사랑");
		dic.put("apple","사과");
		dic.put("baby","아기");
		
		Set<String> keys = dic.keySet(); // 키 리스트 얻어냄
		Iterator<String> it = keys.iterator();
		
		while(it.hasNext()) {
			String key = it.next();
			String value = dic.get(key);
			System.out.print("(" + key + "," + value + ")");
		}
		System.out.println();
		
		for(int i = 0 ; i < 3 ; i++) {
			System.out.print("찾고 싶은 단어는? ");
			String input = sc.next();
			
			if(dic.containsKey(input)) 
				System.out.println(dic.get(input));
			else
				System.out.println(input+"는(은) 없는 단어입니다.");
			
		}

	}

}

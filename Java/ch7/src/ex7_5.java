import java.util.*;

public class ex7_5 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		HashMap<String, String> dic = new HashMap<String, String>();
		dic.put("love","���");
		dic.put("apple","���");
		dic.put("baby","�Ʊ�");
		
		Set<String> keys = dic.keySet(); // Ű ����Ʈ ��
		Iterator<String> it = keys.iterator();
		
		while(it.hasNext()) {
			String key = it.next();
			String value = dic.get(key);
			System.out.print("(" + key + "," + value + ")");
		}
		System.out.println();
		
		for(int i = 0 ; i < 3 ; i++) {
			System.out.print("ã�� ���� �ܾ��? ");
			String input = sc.next();
			
			if(dic.containsKey(input)) 
				System.out.println(dic.get(input));
			else
				System.out.println(input+"��(��) ���� �ܾ��Դϴ�.");
			
		}

	}

}

import java.util.StringTokenizer;

public class ex6_7 {

	public static void main(String[] args) {
		String query = "name=kitae&addr=seoul&age=21";
		StringTokenizer st = new StringTokenizer(query ,"&");
		
		int n = st.countTokens();
		System.out.println("토큰 개수 : "+n);
		while(st.hasMoreTokens()) {
			String token = st.nextToken();
			System.out.println(token);
		}
		System.out.println();
		
		StringTokenizer st2 = new StringTokenizer(query, "&=");
		
		int m = st2.countTokens();
		while(st2.hasMoreTokens()) {
			String token = st2.nextToken();
			System.out.println(token);
		}
	}

}

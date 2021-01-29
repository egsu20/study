import java.util.Scanner;

interface StackInterface{
	int length();
	String pop();
	boolean push(String ob);
}

class StringStack implements StackInterface {
	private String str[] = new String[5];
	private static int top = 0;
	
	public int length() {
		return top;
	}
	public String pop() {
		
		return str[--top];
	}
	public boolean push(String ob) {
		if(top == str.length) {
			return false;
		}
		
		str[top++] = ob;
		return true;
	}
}

public class ch5_5 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		StringStack stack = new StringStack();
		
		System.out.print(">> ");
		for(int i = 0 ; i < 5 ; i++) {
			stack.push(sc.next());
		}
		
		for(int i = 0 ; i < 5 ; i++) {
			System.out.print("("+stack.pop()+","+stack.length()+")");
		}
		
		sc.close();

	}

}

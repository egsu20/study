class GStack<T>{
	int tos; // 탑 포인터
	Object []stck;
	int size; // 스택의 크기 
	
	public GStack() {
		tos = 0;
		size = 10;
		stck = new Object[size];
	}
	public GStack(int n) {
		tos = 0;
		size = n;
		stck = new Object[size];
	}
	public void push(T item) {
		if(tos == size) // 스택이 꽉 참
			return;
		stck[tos] = item;
		tos++;
	}
	public T pop() {
		if(tos == 0)
			return null;
		tos--;
		return (T)stck[tos]; // stck는 Object 타입이므로 다운 캐스팅 필요
	}
}
public class ex7_6 {

	public static void main(String[] args) {
		GStack<String> strStack = new GStack<String>();
		strStack.push("seoul");
		strStack.push("busan");
		strStack.push("LA");
		
		for(int i = 0 ; i < 3 ; i++)
			System.out.println(strStack.pop());
		
		GStack<Integer> intStack = new GStack<Integer>();
		intStack.push(1);
		intStack.push(2);
		intStack.push(3);
		
		for(int i = 0 ; i < 3 ; i++)
			System.out.println(intStack.pop());

	}

}

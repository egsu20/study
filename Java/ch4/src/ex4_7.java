import java.util.Scanner;

class Book3 {
	String title, author;
	
	public Book3(String title, String author) {
		this.title = title;
		this.author = author;
	}
	
	void show() {
		System.out.println(title + ", " + author);
	}
}

public class ex4_7 {

	public static void main(String[] args) {
		Book3 [] book= new Book3[2];
		String title, author;
		Scanner sc = new Scanner(System.in);
		
		for(int i = 0 ; i < book.length ; i++) {
			System.out.print("제목>>");
			title = sc.nextLine();
			System.out.print("저자>>");
			author = sc.nextLine();
			
			book[i] = new Book3(title, author);
		}
		
		for (int i = 0 ; i < book.length ; i++) {
			book[i].show();
		}
		
		sc.close();
	}

}

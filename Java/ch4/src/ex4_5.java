class Book2 {
	String title, author;
	
	public Book2() {
		this("", "");
		System.out.println("������ ȣ���");
	}
	public Book2(String title) {
		this(title, "���ڹ̻�");
	}
	public Book2(String title, String author) {
		this.title = title;
		this.author = author;
	}
	
	void show() {
		System.out.println(title + " " + author);
	}
}

public class ex4_5 {

	public static void main(String[] args) {
		Book2 littlePrince = new Book2("�����","�������丮");
		Book2 loveStory = new Book2("������");
		Book2 emptyBook = new Book2();
		
		littlePrince.show();
		loveStory.show();
		emptyBook.show();
	}

}

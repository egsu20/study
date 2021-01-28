import java.util.Scanner;

class Rectangle{
	int width, height;
	public int getArea() {
		return width*height;
	}
}
public class ex4_2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		Rectangle rect = new Rectangle();
		
		System.out.print(">>");
		rect.width = sc.nextInt();
		rect.height = sc.nextInt();
		
		System.out.println("사각형의 면적은 " + rect.getArea());
		sc.close();
	}

}

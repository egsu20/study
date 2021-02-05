class Rectangle{
	private int w, h;
	public Rectangle(int w, int h) {
		this.w = w;
		this.h = h;
	}
	public String toString() {
		return "Rectangle width:" + w + ", height:" + h;
	}
}

public class ex6_2 {

	public static void main(String[] args) {
		Rectangle r = new Rectangle(3,2);
		System.out.println(r.toString());
		System.out.println(r);

	}

}

class Point{
	private int x, y;
	public Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
}
public class ex6_1 {

	public static void main(String[] args) {
		Point p = new Point(3,2);
		System.out.println(p.getClass().getName());
		System.out.println(p.hashCode());
		System.out.println(p.toString());
	}

}

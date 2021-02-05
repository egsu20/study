class Point2{
	private int x, y;
	public Point2(int x, int y) {
		this.x = x;
		this.y = y;
	}
	public boolean equals(Object obj) { // 업캐스팅
		Point2 p = (Point2)obj;
		if(x == p.x && y == p.y) return true;
		else return false;
	}
}
public class ex6_3 {

	public static void main(String[] args) {
		Point2 a = new Point2(2,3);
		Point2 b = new Point2(2,3);
		Point2 c = a;

		if(a == b) System.out.println("a==b");
		if(a == c) System.out.println("a==c");
		if(a.equals(b)) System.out.println("a is equal to b");
	}

}

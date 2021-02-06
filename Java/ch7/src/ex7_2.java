import java.util.Vector;

class Point{
	private int x, y;
	public Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
	public String toString() {
		return "(" + x + "," + y + ")";
	}
}

public class ex7_2 {
	public static void main(String[] args) {
		Vector<Point> v = new Vector<Point>(); // 타입매개변수로 Point 지정
		
		v.add(new Point(2, 3)); // Point 객체 생성, 삽입
		v.add(new Point(-5, 20));
		v.add(new Point(30, -8));
		
		v.remove(1);
		
		for(int i = 0 ; i < v.size(); i++) {
			Point p = v.get(i);
			System.out.println(p);
		}
	}
}

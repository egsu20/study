class Shape {
	public void draw() {
		System.out.println("Shape");
	}
}
class Line extends Shape {
	public void draw() {
		System.out.println("Line");
	}
}
class Rect extends Shape {
	public void draw() {
		System.out.println("Rectangle");
	}
}
class Circle extends Shape {
	public void draw() {
		System.out.println("Circle");
	}
}
public class ex5_4 {
	static void paint(Shape p) { // ��ĳ����
		p.draw();
	}
	
	public static void main(String[] args){
		Line line = new Line();
		paint(line);
		
		paint(new Shape());
		paint(new Line());
		paint(new Rect());
		paint(new Circle());
	}
}

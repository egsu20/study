class Circle3{
	int radius;
	public Circle3(int radius) {
		this.radius = radius;
	}
	public double getArea() {
		return radius * radius * 3.14;
	}
}
public class ex4_6 {

	public static void main(String[] args) {
		Circle3[] c = new Circle3[3];
		
		for(int i = 0 ; i < c.length ; i++) {
			c[i] = new Circle3(i);
		}
		
		for(int i = 0 ; i < c.length ; i++) {
			System.out.print((int)(c[i].getArea())+" ");
		}
	}

}

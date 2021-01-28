class Circle2 {
	int radius;
	String name;
	
	public Circle2() {
		this.radius = 1;
		this.name = "";
	}
	
	public Circle2(int radius, String name) {
		this.radius = radius;
		this.name = name;
	}
	
	public double getArea() {
		return 3.14*radius*radius;
	}
}

public class ex4_3 {

	public static void main(String[] args) {
		Circle2 pizza = new Circle2(10, "javaPizza");
		double area = pizza.getArea();
		System.out.println(pizza.name + "의 면적은 " + area);
		
		Circle2 donut = new Circle2();
		donut.name = "javaDonut";
		area = donut.getArea();
		System.out.println(donut.name + "의 면적은 " + area);
	}

}

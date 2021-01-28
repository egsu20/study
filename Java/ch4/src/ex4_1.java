class Circle{
	int radius;
	String name;
	
	public double getArea() {
		return radius * radius * 3.14;
	}
}

public class ex4_1 {

	public static void main(String[] args) {
		Circle pizza = new Circle();
		pizza = new Circle();
		pizza.radius = 10;
		pizza.name = "javaPizza";
		System.out.println(pizza.name+"의 면적은 "+pizza.getArea());
		
		Circle donut = new Circle();
		donut.radius = 2;
		donut.name = "javaDonut";
		System.out.println(donut.name+"의 면적은 "+donut.getArea());
	}

}

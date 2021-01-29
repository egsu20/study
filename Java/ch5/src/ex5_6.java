interface PhoneInterface {
	final int TIMEOUT = 1000;
	void sendCall();
	void receiveCall();
	default void printLogo() {
		System.out.println("** Phone **");
	}
}
class Calc {
	public int calculate(int x, int y) {
		return x + y;
	}
}
class SamsungPhone extends Calc implements PhoneInterface {
	public void sendCall() {
		System.out.println("�츮��");
	}
	public void receiveCall() {
		System.out.println("��ȭ�� �Խ��ϴ�.");
	}
	public void flash() {
		System.out.println("��ȭ�⿡ ���� �������ϴ�.");
	}
}

public class ex5_6 {

	public static void main(String[] args) {
		SamsungPhone phone = new SamsungPhone();
		phone.printLogo();
		phone.sendCall();
		phone.receiveCall();
		phone.flash();
		System.out.println("3 + 5 = " + phone.calculate(3, 5));
	}

}

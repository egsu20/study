
public class ex6_8 {

	public static void main(String []args) {
		System.out.println(Math.abs(-3.14)); // ����
		System.out.println(Math.sqrt(9.0)); // ������
		System.out.println(Math.exp(2)); // e�� 2��
		System.out.println(Math.round(3.14)); // �ݿø�
		
		System.out.print("�̹��� ����� ��ȣ�� ");
		for(int i = 0 ; i < 5 ; i++) {
			System.out.print((int)(Math.random()*45+1) + " "); // 1���� 45 ������ ����
		}
	}
}

import java.util.Vector;

public class ex7_1 {

	public static void main(String[] args) {
		Vector<Integer> v = new Vector<Integer>();
		v.add(5);
		v.add(7);
		v.add(-1);
		
		v.add(1,6); // 1�� ��ġ�� 6 ����
		
		System.out.println("���� ���� ��� ��ü �� : " + v.size());
		System.out.println("������ ���� �뷮 : " + v.capacity());
		
		for(int i = 0 ; i < v.size(); i++) {
			int n = v.get(i); // i��° ��� �˾Ƴ���
			System.out.println(n);
		}
		
		int sum = 0;
		for(int i = 0 ; i < v.size() ; i++) {
			int n = v.elementAt(i); // i��° ��� �˾Ƴ���
			sum += n;
		}
		System.out.println("���Ϳ� �ִ� ���� �� : " + sum);
	}

}

import java.util.*;

public class ex7_4 {

	public static void main(String[] args) {
		Vector<Integer> v = new Vector<Integer>();
		v.add(5);
		v.add(7);
		v.add(-1);
		v.add(1,6);
		
		Iterator<Integer> it = v.iterator(); // v�� ���ͷ����� ��ü�� ��
		int sum = 0;
		
		while(it.hasNext()) {
			int n = it.next();
			System.out.println(n);
			sum += n;
		}

		System.out.println("���� �� : " + sum);
	}

}

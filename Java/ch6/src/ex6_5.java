
public class ex6_5 {

	public static void main(String[] args) {
		System.out.println(Character.toLowerCase('A')); // �ҹ��ڷ�
		char c1 = '4', c2 = 'F';
		if(Character.isDigit(c1))
			System.out.println(c1 + "�� ����");
		if(Character.isAlphabetic(c2))
			System.out.println(c2 + "�� ������");
		
		System.out.println(Integer.parseInt("28"));
		System.out.println(Integer.toString(28));
		System.out.println(Integer.toBinaryString(28)); // 11100
		System.out.println(Integer.bitCount(28)); // 2������ ��ȯ�� �� �� 1�� ����
		
		Integer i = Integer.valueOf(28);
		System.out.println(i.doubleValue());
		
		Double d = Double.valueOf(3.14);
		System.out.println(d.toString());
		System.out.println(d.getClass().getName());
		
		boolean b = (4>3);
		System.out.println(Boolean.toString(b));
		System.out.println(Boolean.parseBoolean("false"));
		
	}

}

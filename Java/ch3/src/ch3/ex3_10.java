package ch3;

public class ex3_10 {

	public static void main(String[] args) {
		double score[][] = {{3.3, 3.4},
				{3.5, 3.6},
				{3.7, 4.0},
				{4.1, 4.2}};
		double sum=0;
		int n = score.length;
		int m = score[0].length;
		
		for(int year = 0 ; year < n ; year++) {
			for(int term = 0 ; term < m ; term++) {
				sum += score[year][term];
			}
		}
		
		System.out.println("4�� ��ü ���� ����� "+sum/(n*m));
	}

}

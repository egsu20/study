import java.awt.*;
import javax.swing.*;

public class ex8_5 extends JFrame {
	public ex8_5() {
		setTitle("ex8-5");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		c.setLayout(new GridLayout(3,3));
		
		for(int i = 1 ; i <= 9 ; i++) {
			c.add(new JButton(Integer.toString(i)));
		}
		
		
		setSize(300, 200);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new ex8_5();

	}

}

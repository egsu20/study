import java.awt.*;
import javax.swing.*;

public class ex8_6 extends JFrame {
	public ex8_6() {
		setTitle("ex8-6");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		c.setLayout(null);
		
		JLabel la = new JLabel("Hello, Press Button!");
		la.setBounds(130, 50, 200, 20);
		c.add(la);
		
		for(int i = 1 ; i <= 9 ; i++) {
			JButton b = new JButton(Integer.toString(i));
			b.setLocation(i*15, i*15);
			b.setSize(50, 20);
			c.add(b);
		}
		
		setSize(300, 200);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new ex8_6();

	}

}

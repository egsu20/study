import java.awt.*;
import javax.swing.*;

public class ex8_4 extends JFrame {
	public ex8_4() {
		setTitle("ex8-4");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		c.setLayout(new BorderLayout(30, 20));
		
		c.add(new JButton("WEST"), BorderLayout.WEST);
		c.add(new JButton("EAST"), BorderLayout.EAST);
		c.add(new JButton("SOUTH"), BorderLayout.SOUTH);
		c.add(new JButton("NORTH"), BorderLayout.NORTH);
		c.add(new JButton("CENTER"), BorderLayout.CENTER);
		
		setSize(300, 200);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new ex8_4();

	}

}

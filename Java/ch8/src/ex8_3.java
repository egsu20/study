import java.awt.*;
import javax.swing.*;

public class ex8_3 extends JFrame {
	public ex8_3() {
		setTitle("ex8-3");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container cp = getContentPane();
		cp.setLayout(new FlowLayout(FlowLayout.LEFT, 30, 40));
		
		cp.add(new JButton("add"));
		cp.add(new JButton("add"));
		cp.add(new JButton("add"));
		cp.add(new JButton("add"));
		cp.add(new JButton("add"));
		
		setSize(300,200);
		setVisible(true);
	}

	public static void main(String[] args) {
		new ex8_3();

	}

}

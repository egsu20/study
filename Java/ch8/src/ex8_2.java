import java.awt.*;
import javax.swing.*;

public class ex8_2 extends JFrame{
	public ex8_2() {
		setTitle("ContentPane & JFrame");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container cp = getContentPane();
		cp.setLayout(new FlowLayout());
		cp.setBackground(Color.ORANGE);
		
		cp.add(new JButton("OK"));
		cp.add(new JButton("Cancle"));
		cp.add(new JButton("Ignore"));
		
		setSize(300, 150);
		setVisible(true);
	}

	public static void main(String[] args) {
		new ex8_2();

	}

}

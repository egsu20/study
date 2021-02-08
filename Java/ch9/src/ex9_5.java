import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.event.*;

public class ex9_5 extends JFrame{
	public ex9_5() {
		setTitle("ex");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		c.setLayout(null);
		
		JLabel la = new JLabel("Hello");
		la.setBounds(30,30,50,20);
		c.add(la);
		
		c.addMouseListener(new MouseAdapter() { // 클래스이므로 extends
			public void mousePressed(MouseEvent e) {
				int x = e.getX();
				int y = e.getY();
				la.setLocation(x,y);
			}
		});
		
		setSize(200,200);
		setVisible(true);
	}
	
	public static void main(String []args) {
		new ex9_5();
	}
}

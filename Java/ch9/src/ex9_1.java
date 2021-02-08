import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.event.*;

class MyActionListener implements ActionListener{
	public void actionPerformed(ActionEvent e) {
		JButton btn = (JButton)e.getSource();
		
		if(btn.getText().equals("Action"))
			btn.setText("¾×¼Ç");
		else
			btn.setText("Action");
	}
}

public class ex9_1 extends JFrame{
	public ex9_1() {
		setTitle("Action Event");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		c.setLayout(new FlowLayout());
		
		JButton btn = new JButton("Action");	
		MyActionListener li = new MyActionListener();
		btn.addActionListener(li);
		c.add(btn);
		
		setSize(250, 120);
		setVisible(true);
	}
	public static void main(String[] args) {
		new ex9_1();
		
	}
	
}
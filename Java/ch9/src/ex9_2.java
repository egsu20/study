import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.event.*;

public class ex9_2 extends JFrame{
	
	class MyActionListener implements ActionListener{
		
		public void actionPerformed(ActionEvent e) {
			JButton btn = (JButton)e.getSource();
			
			if(btn.getText().equals("Action"))
				btn.setText("�׼�");
			else
				btn.setText("Action");
		}
	}

	public ex9_2() {
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
		new ex9_2();
		
	}
	
}
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.event.*;

public class ex9_7 extends JFrame{
   JLabel la = new JLabel("HELLO");
	
   public ex9_7() {
      setTitle("ex");
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      
      Container c = getContentPane();
      c.setLayout(null);
      
      la.setBounds(50, 50, 100, 20);
      c.add(la);
      
      c.addKeyListener(new MyListener());
      
      c.setFocusable(true);
      c.requestFocus();
      
      setSize(400,400);
      setVisible(true);
   }
   
   class MyListener extends KeyAdapter {
	   public void keyPressed(KeyEvent e) {
		   int x = la.getX();
		   int y = la.getY();
		   
		   switch(e.getKeyCode()) {
		   case KeyEvent.VK_UP:
			   la.setLocation(x, y-10);
			   break;
		   case KeyEvent.VK_DOWN:
			   la.setLocation(x, y+10);
			   break;
		   case KeyEvent.VK_LEFT:
			   la.setLocation(x-10, y);
			   break;
		   case KeyEvent.VK_RIGHT:
			   la.setLocation(x+10, y);
			   break;
		   }
	   }
   }
   
   public static void main(String []args) {
      new ex9_7();
   }
}
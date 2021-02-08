import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.Random;

import javax.swing.event.*;

public class ex9_6 extends JFrame{
	
   public ex9_6() {
      setTitle("ex");
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      
      Container c = getContentPane();
      c.setLayout(new FlowLayout());
      
      JLabel la = new JLabel("<Enter>키로 배경색이 바뀝니다.");
      c.add(la);
      
      c.setFocusable(true);
      c.requestFocus();
      
      c.addKeyListener(new KeyAdapter() {
    	  public void keyPressed(KeyEvent e) {
    		  int r = (int)(Math.random() * 256);
    		  int g = (int)(Math.random() * 256);
    		  int b = (int)(Math.random() * 256);
    		  
    		  if(e.getKeyCode() == KeyEvent.VK_ENTER) { // e.getKeyChar() == '\n'
    			  c.setBackground(new Color(r,g,b));
    		  }
    		  else if (e.getKeyChar() == 'q')
    			  System.exit(0);
    	  }
      });
      
      setSize(400,400);
      setVisible(true);
   }
   
   public static void main(String []args) {
      new ex9_6();
   }
}
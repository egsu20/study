import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.event.*;

public class ex9_8 extends JFrame{
   JLabel la = new JLabel("Move Me");
      
   public ex9_8() {
      setTitle("ex");
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      
      Container c = getContentPane();
      c.setLayout(null);
      
      la.setBounds(100, 80, 80, 20);
      c.add(la);
      c.addMouseListener(new MyListener());
      
      setSize(400,400);
      setVisible(true);
   }
   
   class MyListener implements MouseListener, MouseMotionListener {
		
		public void mousePressed(MouseEvent e) {
			int x = e.getX();
			int y = e.getY();
			
			la.setLocation(x, y);
			setTitle("MousePressed("+x+","+y+")");
		}
		public void mouseReleased(MouseEvent e) {
			int x = e.getX();
			int y = e.getY();
			
			la.setLocation(x, y);
			setTitle("MouseReleased("+x+","+y+")");
		}
		public void mouseEntered(MouseEvent e) {
			Component comp = e.getComponent();
			comp.setBackground(Color.YELLOW);
			setTitle("MouseEntered");
		}
		public void mouseExited(MouseEvent e) {
			Component comp = e.getComponent();
			comp.setBackground(Color.CYAN);
			setTitle("MouseExited");
		}
		public void mouseClicked(MouseEvent e) {
			
		}
		public void mouseDragged(MouseEvent e) {
			la.setLocation(e.getX(), e.getY());
			setTitle("MouseDragged("+e.getX()+","+e.getY()+")");
		}
		public void mouseMoved(MouseEvent e) {
			int x = e.getX();
			int y = e.getY();
			
			la.setLocation(x, y);
			setTitle("MouseMoved("+x+","+y+")");
		}
	}

   
   public static void main(String []args) {
      new ex9_8();
   }
}
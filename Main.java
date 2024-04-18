import javax.swing.*;
import java.awt.*;
 
class Main extends JFrame
{
 public static void main(String arg[])
 {
    Main rg=new Main();
    rg.setTitle("registration page");
    rg.getContentPane().setBackground(Color.BLUE);
    rg.setSize(500,500);
    rg.setVisible(true);
    rg.setLayout(null);
    rg.setDefaultCloseOperation(rg.EXIT_ON_CLOSE);
        JLabel l1=new JLabel("NAME");
        JLabel l2=new JLabel("USN");
        JLabel l3=new JLabel("SEM");
        JLabel l4=new JLabel("EMAIL");
        JLabel l5=new JLabel("PH NO");
           JTextField t1=new JTextField();
           JTextField t2=new JTextField();
           JTextField t3=new JTextField();
           JTextField t4=new JTextField();
           JTextField t5=new JTextField();
                JButton b1=new JButton("SUBMIT");
      l1.setBounds(50,50,100,50);
      l2.setBounds(50,130,100,50);
      l1.setBounds(50,200,100,50);
      l1.setBounds(50,270,100,50);
      l1.setBounds(50,330,100,50);
          t1.setBounds(200,50,100,50);
          t2.setBounds(200,120,100,50);
          t1.setBounds(200,180,100,50);
          t1.setBounds(200,240,100,50);
          t1.setBounds(200,300,100,50);
               b1.setBounds(200,200,100,50);
                    rg.add(l1); rg.add(l2); rg.add(l3); rg.add(l4); rg.add(l5);
                    rg.add(t1);rg.add(t2);rg.add(t3);rg.add(t4);rg.add(t5);
                    rg.add(b1);
      }
}         


         
           
            
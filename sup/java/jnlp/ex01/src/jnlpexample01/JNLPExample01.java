package jnlpexample01;

// reference:
// https://examples.javacodegeeks.com/java-basics/web-start/java-web-start-getting-started/
import javax.swing.JFrame;
import javax.swing.JLabel;

public class JNLPExample01 extends JFrame {

    private static final long serialVersionUID = 4968624166243565348L;

    private JLabel label = new JLabel("Hello from Java Code Geeks!");

    public JNLPExample01() {
        super("Jave Web Start Example");
        this.setSize(350, 200);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(null);
    }

    public void addButtons() {
        label.setSize(200, 30);
        label.setLocation(80, 50);
        this.getContentPane().add(label);
    }

    public static void main(String[] args) {
        JNLPExample01 exp = new JNLPExample01();
        exp.addButtons();
        exp.setLocationRelativeTo(null);
        exp.setVisible(true);
    }
}
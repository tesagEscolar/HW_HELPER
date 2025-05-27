import javax.swing.*;

public class Cylinder3DViewer extends JFrame {

    public Cylinder3DViewer() {
        setTitle("Cilindro 3D - Animación de Rotación");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(600, 600);
        setLocationRelativeTo(null); // Centrar la ventana

        CylinderPanel panel = new CylinderPanel();
        add(panel);

        setVisible(true);

        // Iniciar la animación después de que la ventana sea visible
        panel.startAnimation();
    }

    public static void main(String[] args) {
        // Ejecutar la GUI en el "Event Dispatch Thread" (EDT)
        SwingUtilities.invokeLater(() -> {
            new Cylinder3DViewer();
        });
    }
}
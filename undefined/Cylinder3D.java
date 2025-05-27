```java
import javax.swing.*;
import java.awt.*;

/**
 * Clase principal para ejecutar la aplicacion del cilindro 3D.
 */
public class Cylinder3D {

    public static void main(String[] args) {
        // Ejecutar la creacion de la GUI en el Event Dispatch Thread (EDT)
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Cilindro 3D con Rotacion");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setLayout(new BorderLayout());

            CylinderPanel cylinderPanel = new CylinderPanel();
            frame.add(cylinderPanel, BorderLayout.CENTER);

            frame.pack(); // Ajusta el tamaño de la ventana al contenido
            frame.setLocationRelativeTo(null); // Centra la ventana en la pantalla
            frame.setVisible(true);

            // Opcional: iniciar la animacion (ya se inicia en el constructor del panel)
            // cylinderPanel.startAnimation();
        });
    }
}
```
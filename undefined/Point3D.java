```java
/**
 * Clase simple para representar un punto en el espacio 3D.
 */
public class Point3D {
    double x, y, z;

    public Point3D(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    @Override
    public String toString() {
        return "Point3D{" +
               "x=" + x +
               ", y=" + y +
               ", z=" + z +
               '}';
    }
}
```
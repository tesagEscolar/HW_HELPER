# 03 Operación continua

**Elaborado por**: Daniel Tejeda Saavedra  
**Registro**: 22310431  
**Fecha**: 31 may 2025  
**Materia**: Gestión de servicios de TI (2025 Feb - Jun)  
**Profesor**: José Francisco Pérez Reyes  
**Indicaciones**: Configuración de un sistema de monitoreo utilizando herramientas como Prometheus y Grafana. Pueden practicar la definición de alertas y la visualización de métricas en tiempo real.

Nota: Las herramientas son sugerencia, puedes utilizar cualquier otra herramienta que cumpla con las funcionalidades requeridas.

Evidencia: Documento PDF.  

---
# # Configuración de un Sistema de Monitoreo con Prometheus y Grafana

## Introduction:
El monitoreo de sistemas informáticos es un componente crítico para asegurar la disponibilidad, rendimiento y fiabilidad de las infraestructuras tecnológicas. Permite la detección temprana de problemas, la optimización de recursos y la planificación de capacidad. El presente documento técnico detalla el proceso de configuración de un sistema de monitoreo robusto y escalable utilizando **Prometheus** como sistema de recolección y almacenamiento de métricas de series temporales, y **Grafana** como plataforma de visualización y alerting. Esta combinación de herramientas de código abierto se ha convertido en un estándar de facto en el ámbito del monitoreo de infraestructuras modernas, ofreciendo flexibilidad y potentes capacidades analíticas y de notificación.

---

## Development:
La implementación de un sistema de monitoreo basado en Prometheus y Grafana involucra varias etapas clave, comenzando por la instalación y configuración de los componentes principales, seguida por la instrumentación de los sistemas a monitorear, la definición de reglas de agregación y alerting en Prometheus, y finalmente, la creación de dashboards interactivos en Grafana.

**1. Arquitectura del Sistema:**
La arquitectura típica consiste en la instancia principal de Prometheus, que actúa como el servidor central que scrapea (recoge) métricas de diversas fuentes (targets). Estos targets son típicamente exportadores (exporters) que exponen métricas en un formato compatible con Prometheus (el formato de texto de Prometheus). Grafana se conecta a Prometheus como una fuente de datos (datasource) y utiliza la potente lenguaje de consulta **PromQL** (Prometheus Query Language) para recuperar, agregar y transformar las métricas para su visualización y alerting.

**2. Instalación y Configuración Inicial:**
Se requiere la instalación de los binarios o paquetes de Prometheus Server y Grafana Server en máquinas dedicadas o contenedores. La configuración de Prometheus se realiza mediante un archivo `prometheus.yml`, donde se definen los jobs de scraping, los targets, las reglas de grabación (recording rules) y las reglas de alerta (alerting rules). La configuración inicial de Grafana implica el acceso a su interfaz web para añadir a Prometheus como una nueva fuente de datos, especificando la URL del servidor Prometheus.

**3. Recolección de Métricas (Scraping):**
Prometheus recolecta métricas mediante un modelo pull, donde periódicamente scrapea endpoints HTTP configurados. Para monitorear diferentes tipos de sistemas (servidores Linux, bases de datos, aplicaciones personalizadas), se utilizan exporters específicos (ej. `node_exporter` para métricas del sistema operativo, `mysqld_exporter` para MySQL, `kube-state-metrics` para Kubernetes, o instrumentación directa de aplicaciones con librerías cliente de Prometheus). La configuración en `prometheus.yml` define los jobs de scraping, especificando la frecuencia (scrape_interval), el timeout y la lista de targets o mecanismos para descubrirlos (ej. service discovery).

**4. Definición de Reglas de Alerta:**
Prometheus maneja las alertas a través de reglas definidas en archivos `.rules` (referenciados en `prometheus.yml`). Estas reglas consisten en expresiones PromQL que, al evaluar a un valor verdadero o no vacío, activan una alerta. Las alertas se envían a un componente llamado **Alertmanager**, que se encarga de agrupar, silenciar y enviar notificaciones a través de diversos canales (ej. email, Slack, PagerDuty). La configuración de Alertmanager (`alertmanager.yml`) define los receptores y las políticas de enrutamiento de las alertas.

**5. Visualización de Métricas en Grafana:**
Grafana permite crear dashboards personalizados compuestos por paneles. Cada panel visualiza datos obtenidos de una fuente de datos (Prometheus). La creación de un panel implica seleccionar la fuente de datos, definir una consulta PromQL para obtener las métricas deseadas y configurar las opciones de visualización (tipo de gráfico, rangos de tiempo, leyendas, etc.). Grafana soporta una amplia variedad de tipos de paneles, incluyendo gráficos de series temporales (Graph), tablas (Table), indicadores (Gauge), mapas de calor (Heatmap), entre otros. La organización de paneles en filas y variables de dashboard permite crear visualizaciones dinámicas y reutilizables.

**6. Configuración de Alertas en Grafana:**
Aunque Prometheus es el motor de evaluación de alertas principal, Grafana también ofrece su propio sistema de alerting integrado que puede evaluar consultas de paneles. Esto permite definir condiciones de alerta directamente en los paneles del dashboard. Las alertas de Grafana también pueden ser configuradas para enviar notificaciones a través de múltiples canales de notificación configurados centralmente.

---

## Conclusion:
La implementación de un sistema de monitoreo utilizando Prometheus y Grafana proporciona una solución integral para la observación de la salud y el rendimiento de las infraestructuras tecnológicas. La combinación de la potente recolección y agregación de métricas de Prometheus con las flexibles capacidades de visualización y alerting de Grafana permite a los equipos de operaciones y desarrollo identificar y responder proactivamente a los problemas. Este enfoque basado en métricas es fundamental para mantener sistemas resilientes, optimizar la utilización de recursos y garantizar una experiencia de usuario satisfactoria. La capacidad de definir alertas basadas en reglas complejas y visualizar tendencias históricas facilita la toma de decisiones informadas y la mejora continua de los sistemas.

---

## References:
La información detallada para la instalación, configuración y operación de Prometheus y Grafana se encuentra disponible en la documentación oficial de los proyectos, así como en una vasta cantidad de tutoriales, blogs y repositorios de código en línea. Se recomienda consultar:

*   **Documentación Oficial de Prometheus:** [https://prometheus.io/docs/](https://prometheus.io/docs/)
*   **Documentación Oficial de Grafana:** [https://grafana.com/docs/](https://grafana.com/docs/)
*   **Documentación de Exporters Comunes:** Ej. node_exporter, Alertmanager.
*   **Comunidades y Foros en Línea:** Sitios como Stack Overflow, grupos de Google y canales de Slack dedicados a Prometheus y Grafana.

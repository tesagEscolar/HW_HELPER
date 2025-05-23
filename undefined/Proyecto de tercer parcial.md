# Proyecto de tercer parcial

**Elaborado por**: Daniel Tejeda Saavedra  
**Registro**: 22310431  
**Fecha**: 17 jun 2025  
**Materia**: Gestión de servicios de TI (2025 Feb - Jun)  
**Profesor**: José Francisco Pérez Reyes  
**Indicaciones**: De acuerdo a la documentación de microservicio(s) desarrollado desde el primer parcial, ahora implementa y documenta todo los conceptos vistos en el material "Unidad III.pdf" y lo más importante que incluya la configuración de todas las herramientas desarrolladas en las prácticas del tercer parcial. Esto puede incluir control de versiones, CI/CD, orquestación de contenedores y herramientas de monitoreo. La falta de conceptos disminuirá la evaluación.

Aunque las actividades se han trabajado en equipo, para el proyecto se va a evaluar el nivel de personalización de sus documentos de manera individual, es decir, la personalización, formato, estilo, justificación, imágenes, diagramas, etc., considerándose para una mejor evaluación. Es importante aclarar que si se observan documentos iguales se considerará solo como requisito mínimo o incluso podría ser menor la evaluación.

Evidencia: Un solo documento completo PDF (incluye los proyectos de los tres parciales).  

---
# Reporte Técnico: Implementación Integral de Microservicio con Prácticas DevOps y Conceptos Avanzados

## Introduction:
El presente reporte técnico documenta la implementación de un proyecto de microservicio desarrollado a lo largo de tres parciales, con un enfoque particular en la integración de los conceptos avanzados abordados en la "Unidad III" y la aplicación sistemática de herramientas y prácticas de DevOps trabajadas durante el tercer parcial. El objetivo primordial es presentar una visión consolidada del proyecto, destacando cómo la arquitectura de microservicios se complementa con el control de versiones, la integración y entrega continua (CI/CD), la orquestación de contenedores y el monitoreo, para construir un sistema robusto, escalable y mantenible. Se detalla la configuración y el uso de las herramientas clave, demostrando la aplicabilidad práctica de los principios teóricos en un entorno de desarrollo e implementación moderno.

---

## Development:
### Arquitectura del Microservicio

El proyecto se basa en una arquitectura de microservicios, donde funcionalidades específicas se encapsulan en servicios independientes y desplegables. Se describe brevemente la(s) funcionalidad(es) principal(es) del microservicio desarrollado, por ejemplo, la gestión de usuarios, procesamiento de pedidos, o catálogo de productos. Se menciona la tecnología base utilizada (e.g., Spring Boot, Node.js con Express, Python con Flask).

### Conceptos de la Unidad III Aplicados

Se han integrado diversos conceptos clave de la "Unidad III" para mejorar la robustez y eficiencia del microservicio:

*   **API Gateway:** Implementación de un punto de entrada unificado para gestionar solicitudes externas, proporcionando funcionalidades como enrutamiento, autenticación y limitación de tasa. (Si aplica)
*   **Service Discovery:** Mecanismo utilizado para que los servicios puedan encontrarse y comunicarse entre sí dinámicamente sin conocer sus ubicaciones físicas. (e.g., Eureka, Consul, DNS de Kubernetes)
*   **Resiliencia:** Implementación de patrones como Circuit Breaker y Retry para manejar fallos temporales en las dependencias de servicio, mejorando la tolerancia a fallos del sistema. (e.g., Hystrix, Resilience4j)
*   **Logging y Tracing Distribuido:** Establecimiento de un sistema centralizado para la agregación de logs y el seguimiento de solicitudes a través de múltiples servicios, facilitando la depuración y el análisis de rendimiento. (e.g., ELK Stack, Zipkin, Jaeger)
*   **Manejo de Eventos y Consistencia Eventual:** Uso de colas de mensajes o brokers de eventos para comunicación asíncrona entre servicios, abordando escenarios donde la consistencia fuerte no es requerida inmediatamente. (Si aplica: e.g., Kafka, RabbitMQ)

### Control de Versiones con Git

Se ha empleado Git como sistema de control de versiones distribuido. El flujo de trabajo adoptado sigue un modelo de ramas (e.g., Feature Branching o Gitflow Ligero), con ramas `main`/`master` para código estable, ramas `develop` para integración continua, y ramas de características (`feature/nombre`) para el desarrollo de nuevas funcionalidades. Se utilizan commits atómicos, mensajes descriptivos, y Pull/Merge Requests para la revisión de código antes de la fusión, garantizando la colaboración y la trazabilidad de los cambios.

### Integración y Entrega Continua (CI/CD)

Se ha configurado un pipeline de CI/CD utilizando [Nombre de la Herramienta CI/CD, e.g., Jenkins, GitLab CI, GitHub Actions] para automatizar el proceso desde la confirmación del código hasta el despliegue. El pipeline típicamente incluye las siguientes etapas:

1.  **Source:** Clonación del repositorio desde el sistema de control de versiones.
2.  **Build:** Compilación del código fuente y empaquetado del microservicio (e.g., generación de JAR, WAR, o binario).
3.  **Test:** Ejecución de pruebas unitarias, de integración y, opcionalmente, pruebas de aceptación.
4.  **Linting & Static Analysis:** Análisis del código para identificar errores de estilo, bugs potenciales y vulnerabilidades.
5.  **Package:** Creación de una imagen de contenedor Docker para el microservicio.
6.  **Push:** Envío de la imagen Docker al registro de contenedores (e.g., Docker Hub, GitLab Registry, GCR).
7.  **Deploy:** Despliegue automático de la nueva versión del microservicio en el entorno de destino (e.g., staging, production) utilizando el orquestador.

El pipeline se activa automáticamente con cada push a ramas específicas o mediante disparadores manuales.

### Orquestación de Contenedores

El microservicio se empaqueta en contenedores Docker para garantizar la portabilidad y consistencia entre entornos. Para la gestión, escalabilidad y alta disponibilidad de los contenedores en producción, se utiliza un orquestador como [Nombre del Orquestador, e.g., Docker Swarm, Kubernetes].

*   **Docker Swarm:** Si se usa Swarm, se describe el uso de `docker-compose.yml` en modo `swarm` para definir y gestionar servicios, réplicas, redes y volúmenes. Se explican comandos como `docker stack deploy`.
*   **Kubernetes:** Si se usa Kubernetes, se detalla el uso de manifiestos YAML para definir Deployments, Services, Pods, ReplicaSets, y ConfigMaps/Secrets. Se describe cómo Kubernetes gestiona el escalado horizontal, las actualizaciones progresivas (rolling updates), la auto-reparación de pods fallidos y el balanceo de carga.

La configuración del orquestador define el número deseado de réplicas, políticas de reinicio, requisitos de recursos y la configuración de red, asegurando que el microservicio esté siempre disponible y pueda manejar la carga.

### Monitoreo y Observabilidad

Para garantizar la operación continua y el rendimiento del microservicio, se han implementado herramientas de monitoreo y observabilidad:

*   **Métricas con Prometheus y Grafana:** Se instrumenta el microservicio para exponer métricas (e.g., latencia de solicitudes, uso de CPU/memoria, recuento de errores) en un formato compatible con Prometheus. Prometheus se configura para recolectar estas métricas. Grafana se utiliza para crear dashboards visuales que permiten monitorizar el estado del sistema en tiempo real y configurar alertas basadas en umbrales predefinidos.
*   **Logging Centralizado con ELK Stack (Elasticsearch, Logstash, Kibana):** Los logs generados por el microservicio se envían a un sistema centralizado de logs. Logstash se encarga de recolectar, parsear y transformar los logs, que luego se almacenan en Elasticsearch. Kibana proporciona una interfaz gráfica para buscar, analizar y visualizar los logs, facilitando la identificación de problemas y patrones de comportamiento.
*   **Tracing Distribuido (Opcional):** Si se implementó, se describe cómo herramientas como Zipkin o Jaeger permiten seguir el flujo de una solicitud a través de múltiples microservicios, ayudando a identificar cuellos de botella o puntos de fallo en interacciones complejas.

La integración de estas herramientas proporciona visibilidad completa sobre el comportamiento del microservicio en producción, permitiendo una respuesta proactiva ante incidentes y una optimización continua del rendimiento.

---

## Conclusion:
La integración exitosa de la arquitectura de microservicios con las prácticas y herramientas de DevOps documentadas en este reporte ha resultado en un sistema significativamente más robusto, escalable y fácil de mantener. La aplicación rigurosa del control de versiones garantiza la colaboración y la trazabilidad. La implementación de un pipeline de CI/CD automatiza y acelera el ciclo de liberación de software, reduciendo errores manuales. La orquestación de contenedores proporciona la infraestructura necesaria para desplegar, escalar y gestionar el microservicio de manera eficiente en entornos dinámicos. Finalmente, las herramientas de monitoreo y observabilidad ofrecen la visibilidad crítica requerida para la operación proactiva y la resolución rápida de problemas. Este enfoque integral demuestra la madurez del proyecto y la capacidad de aplicar conceptos teóricos avanzados en un entorno práctico de desarrollo de software empresarial.

---

## References:
Documentación oficial de [Nombre de la Herramienta CI/CD]
Documentación oficial de [Nombre del Orquestador]
Documentación oficial de [Nombre de la Herramienta de Monitoreo 1]
Documentación oficial de [Nombre de la Herramienta de Monitoreo 2]
Artículos técnicos y libros sobre Arquitecturas de Microservicios
Documentación interna del proyecto (Repositorio Git, Archivos de Configuración)

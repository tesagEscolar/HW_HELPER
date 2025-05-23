# 04 Fases del ciclo de vida del software

**Elaborado por**: Daniel Tejeda Saavedra  
**Registro**: 22310431  
**Fecha**: 07 jun 2025  
**Materia**: Gestión de servicios de TI (2025 Feb - Jun)  
**Profesor**: José Francisco Pérez Reyes  
**Indicaciones**: Construcción un Pipeline de CI/CD completo que cubra todas las fases del ciclo de vida del software. Incluye integración continua, entrega continua y operación continua en un flujo unificado.

Incluye la investigación y definición del concepto Pipeline de CI/CD.

Evidencia: Documento PDF.  

---
# Construcción de un Pipeline de CI/CD/CO Completo: Integración, Entrega y Operación Continua

## Introduction:
El ciclo de vida del desarrollo de software moderno exige agilidad, fiabilidad y eficiencia. La implementación de un pipeline de Integración Continua, Entrega Continua y Operación Continua (CI/CD/CO) emerge como una metodología fundamental para alcanzar estos objetivos. Este reporte técnico explora la conceptualización y la construcción de un pipeline completo que abarca todas las fases críticas: desde la integración temprana del código hasta la operación y monitorización en producción. Se define el concepto de pipeline de CI/CD y se detalla cómo la adición de la "Operación Continua" extiende su alcance para cubrir de manera integral el ciclo de vida, asegurando un flujo unificado y automatizado que reduce el tiempo de comercialización, minimiza los riesgos y mejora la calidad del software.

---

## Development:
## Concepto de Pipeline de CI/CD

Un pipeline de CI/CD es una serie automatizada de pasos que permite a los equipos de desarrollo y operaciones compilar, probar y desplegar su código de manera fiable y eficiente. Tradicionalmente, se enfoca en la integración continua (CI), donde los desarrolladores integran su código frecuentemente en un repositorio compartido, y la entrega continua (CD), que automatiza el proceso hasta dejar el software listo para ser desplegado en producción. La extensión a Operación Continua (CO) amplía este alcance para incluir la gestión post-despliegue, monitorización y retroalimentación.

## Fases del Pipeline Completo (CI/CD/CO)

Un pipeline completo integra las siguientes fases:

1.  **Integración Continua (CI):**
    *   **Commit:** Los desarrolladores suben cambios de código frecuentemente a un repositorio de control de versiones (ej. Git). Cada commit dispara el pipeline.
    *   **Build:** Se compila el código fuente, se resuelven dependencias y se generan artefactos ejecutables (ej. imágenes Docker, archivos WAR/JAR).
    *   **Test Automatizados (Unitarios, de Integración):** Se ejecutan pruebas automatizadas a nivel de código y componentes para verificar la funcionalidad básica y la integración entre módulos. Si alguna prueba falla, el pipeline se detiene, notificando al equipo.

2.  **Entrega Continua (CD):**
    *   **Packaging/Artefact Management:** Los artefactos generados se empaquetan y se almacenan en un repositorio de artefactos (ej. Nexus, Artifactory). Estos artefactos son inmutables y se utilizan en las fases subsiguientes.
    *   **Automated Testing (Funcionales, de Aceptación, de Performance, de Seguridad):** Se ejecutan pruebas más exhaustivas en un entorno que simula la producción. Esto incluye pruebas end-to-end, de carga, de estrés y análisis de seguridad estáticos y dinámicos.
    *   **Deployment to Staging/Pre-Production:** El artefacto validado se despliega automáticamente en un entorno de staging o pre-producción que replica fielmente el entorno de producción. Se pueden realizar pruebas manuales o automatizadas adicionales en este entorno.
    *   **Approval (Optional):** En algunos casos, puede requerirse una aprobación manual para proceder al despliegue en producción, aunque el objetivo de CD es que el despliegue sea *siempre posible* y *automatizable*.

3.  **Operación Continua (CO):**
    *   **Automated Deployment to Production:** Una vez que el artefacto ha pasado todas las validaciones anteriores (y opcionalmente ha sido aprobado), se despliega automáticamente en el entorno de producción. Técnicas como Blue/Green deployment, Canary releases o Rolling updates se emplean para minimizar el tiempo de inactividad y el riesgo.
    *   **Monitoring & Observability:** Se implementan herramientas de monitorización (ej. Prometheus, Nagios) y observabilidad (ej. ELK stack, Grafana, Jaeger) para recopilar métricas, logs y trazas del rendimiento y comportamiento de la aplicación en producción. Esto permite detectar problemas de forma proactiva y entender el estado del sistema.
    *   **Feedback Loop:** La información recopilada en producción (errores, rendimiento, uso) se retroalimenta a los equipos de desarrollo para informar futuras iteraciones y mejoras. Esto cierra el ciclo, asegurando que la operación impacte directamente en el desarrollo.
    *   **Incident Management & Healing:** Se establecen procesos y automatizaciones para gestionar incidentes, realizar rollbacks si es necesario y, en sistemas resilientes, activar mecanismos de auto-reparación.

## Integración en un Flujo Unificado

La clave de un pipeline completo es la automatización y la orquestación entre estas fases. Herramientas de orquestación de pipelines (ej. Jenkins, GitLab CI, GitHub Actions, Azure DevOps Pipelines, CircleCI) gestionan la ejecución secuencial y condicional de los pasos. Cada fase se desencadena automáticamente al completarse la anterior exitosamente. La falla en cualquier punto detiene el pipeline y notifica a los responsables, adhiriéndose al principio "fail fast". Esta integración total elimina las transiciones manuales propensas a errores y reduce drásticamente el tiempo desde la concepción de una característica hasta su operación estable en producción.

La infraestructura como código (IaC), la configuración como código (CaC) y la contenerización (ej. Docker) son facilitadores clave que aseguran la consistencia de los entornos a lo largo del pipeline, desde el desarrollo hasta la producción y la operación.

---

## Conclusion:
La construcción de un pipeline de CI/CD/CO completo representa una evolución crítica en las prácticas de ingeniería de software. Al unificar la integración, la entrega y la operación continua en un flujo automatizado, las organizaciones logran una cadencia de liberación más rápida, una mejora sustancial en la calidad del software a través de pruebas automatizadas extensivas, una reducción significativa en el riesgo de despliegue y una visibilidad operativa sin precedentes. La adopción de este enfoque holístico no es meramente una optimización técnica, sino una transformación cultural y procesal que posiciona a los equipos para responder con agilidad a las demandas del mercado y mantener sistemas resilientes y de alto rendimiento en producción. La inversión en automatización a lo largo de todo el ciclo de vida es indispensable para la sostenibilidad y el éxito en el panorama tecnológico actual.

---

## References:
Principios de Integración Continua (Martin Fowler).
Libro "Continuous Delivery" (Jez Humble & David Farley).
Documentación oficial de herramientas de CI/CD/CO (Jenkins, GitLab, GitHub Actions, etc.).
Conceptos de DevOps y SRE (Site Reliability Engineering).
Artículos técnicos y whitepapers sobre automatización del ciclo de vida del software.

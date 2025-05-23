# 01 Desarrollo continuo

**Elaborado por**: Daniel Tejeda Saavedra  
**Registro**: 22310431  
**Fecha**: 31 may 2025  
**Materia**: Gestión de servicios de TI (2025 Feb - Jun)  
**Profesor**: José Francisco Pérez Reyes  
**Indicaciones**: Configuración de un flujo de trabajo básico utilizando un repositorio Git y Jenkins. Esto puede incluir la configuración de ganchos de Git para desencadenar compilaciones automáticas en Jenkins.

Nota: Las herramientas son sugerencia, puedes utilizar cualquier otra herramienta que cumpla con las funcionalidades requeridas.

Evidencia: Documento PDF.  

---
# # Configuración de un Flujo de Trabajo Básico de Integración Continua con Git y Jenkins

## Introduction:
El presente documento técnico detalla la configuración de un flujo de trabajo fundamental para la Integración Continua (CI) utilizando un sistema de control de versiones distribuido como Git y un servidor de automatización como Jenkins. La integración de estas herramientas permite automatizar procesos clave del ciclo de vida del desarrollo de software, como la compilación, las pruebas y el despliegue, cada vez que se produce una modificación en el repositorio de código fuente. El objetivo principal es describir los pasos necesarios para establecer una conexión entre un repositorio Git y una instancia de Jenkins, de modo que las operaciones en el repositorio desencadenen automáticamente la ejecución de tareas predefinidas en Jenkins, optimizando así la eficiencia y la fiabilidad del proceso de desarrollo.

---

## Development:
La implementación de un flujo de trabajo básico de CI con Git y Jenkins requiere la configuración adecuada de ambas plataformas para que interactúen de manera efectiva. A continuación, se describen los componentes y pasos clave:

**1. Prerrequisitos:**
*   Disponer de un repositorio Git (local o remoto en una plataforma como GitHub, GitLab, Bitbucket, etc.).
*   Tener una instancia de Jenkins instalada y en funcionamiento.
*   Asegurarse de que Jenkins tiene acceso al repositorio Git (configuración de credenciales si es necesario).
*   Instalar los plugins necesarios en Jenkins, principalmente el plugin de Git y, si se usan webhooks, el plugin de Generic Webhook Trigger o el plugin específico de la plataforma Git (GitHub, GitLab, etc.).

**2. Configuración del Trabajo en Jenkins:**
*   Crear un nuevo trabajo (Item) en Jenkins (por ejemplo, un proyecto de estilo libre o un Pipeline).
*   En la sección 'Gestión de Código Fuente' (Source Code Management), seleccionar Git.
*   Configurar la URL del repositorio Git.
*   Especificar las credenciales si el repositorio es privado.
*   Configurar la rama o ramas que se desean monitorear (por ejemplo, `*/main` o `*/develop`).

**3. Configuración del Disparador de Compilación (Build Trigger):**
La automatización de la ejecución de tareas en Jenkins al detectar cambios en el repositorio Git se logra mediante disparadores. Existen varias estrategias:

*   **Sondeo (Polling):** Jenkins sondea periódicamente el repositorio Git en busca de cambios. Si se detectan, se inicia una compilación. Esta opción, configurada en la sección 'Disparar builds' (Build Triggers) con 'Poll SCM', puede generar carga innecesaria en el servidor Git si el intervalo es muy corto y no hay cambios frecuentes.
*   **Ganchos Git (Git Hooks):** Los ganchos son scripts que se ejecutan automáticamente en el servidor Git en respuesta a ciertos eventos (como un `push`). Un gancho `post-receive` en el servidor Git puede configurarse para notificar a Jenkins. Esto generalmente implica enviar una solicitud HTTP a una URL específica de Jenkins. La URL típica para disparar una compilación remota es `JENKINS_URL/job/YOUR_JOB_NAME/build?token=YOUR_AUTH_TOKEN`. Requiere configurar la opción 'Disparar builds' con 'Disparar compilaciones de forma remota (por ejemplo, desde un script)' y definir un token de autenticación.
*   **Webhooks (Recomendado para plataformas remotas):** La mayoría de las plataformas de hosting de repositorios (GitHub, GitLab, Bitbucket) soportan Webhooks. Se configura un Webhook en la configuración del repositorio remoto para que envíe una solicitud HTTP a una URL específica de Jenkins cada vez que ocurra un evento relevante (como un `push`). En Jenkins, se configura el trabajo para responder a este webhook, generalmente utilizando plugins como 'Generic Webhook Trigger' o los plugins específicos de la plataforma Git, seleccionando 'Disparar builds' con la opción correspondiente (ej. 'GitHub hook trigger for GITScm polling' o 'Build when a change is pushed to GitLab'). Esta es la estrategia más eficiente ya que el servidor Git notifica a Jenkins solo cuando hay cambios, eliminando la necesidad de sondeo.

**4. Configuración de las Etapas de Compilación (Build Steps):**
Definir las tareas que Jenkins debe ejecutar (compilar código, ejecutar pruebas, empaquetar artefactos, etc.). Esto se configura en la sección 'Etapas de ejecución' (Build Steps) o en el script del Pipeline.

**5. Ejecución y Monitoreo:**
Una vez configurado, cada `push` al repositorio Git (o según el disparador seleccionado) debería iniciar automáticamente una compilación en Jenkins. Se puede monitorear el estado y los resultados de las compilaciones en la interfaz de Jenkins.

La elección entre ganchos directos, polling o webhooks dependerá del entorno (repositorio local vs. remoto) y de las capacidades de las plataformas utilizadas. Los webhooks, cuando están disponibles, ofrecen la solución más escalable y eficiente para la integración en tiempo real.

---

## Conclusion:
La integración de Git y Jenkins mediante la configuración de disparadores de compilación, como ganchos post-receive o webhooks, establece un flujo de trabajo de Integración Continua robusto y automatizado. Esta configuración permite que cada modificación en el código fuente desencadene automáticamente el proceso de construcción y verificación en Jenkins, lo cual es fundamental para detectar problemas tempranamente, asegurar la calidad del código y agilizar el ciclo de entrega de software. Adoptar este enfoque no solo mejora la eficiencia operativa de los equipos de desarrollo, sino que también contribuye significativamente a la estabilidad y fiabilidad del producto final. Es una piedra angular para implementar prácticas de DevOps efectivas.

---

## References:
El contenido de este reporte se basa en la documentación oficial y las mejores prácticas comúnmente aceptadas para la configuración e integración de sistemas de control de versiones distribuidos (Git) y servidores de automatización (Jenkins). Se recomienda consultar las siguientes fuentes para profundizar:

*   Documentación oficial de Jenkins (jenkins.io/doc/)
*   Documentación oficial de Git (git-scm.com/doc)
*   Documentación de las plataformas de hosting de repositorios (GitHub, GitLab, Bitbucket) sobre la configuración de Webhooks.

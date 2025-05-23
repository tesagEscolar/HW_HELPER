# 02 Entrega continua

**Elaborado por**: Daniel Tejeda Saavedra  
**Registro**: 22310431  
**Fecha**: 31 may 2025  
**Materia**: Gestión de servicios de TI (2025 Feb - Jun)  
**Profesor**: José Francisco Pérez Reyes  
**Indicaciones**: Crear un entorno de entrega continua utilizando Docker. Incluye la creación de imágenes de contenedores, configuración de Jenkins para despliegues automáticos y prueba de la entrega continua con una aplicación de prueba.

Nota: Las herramientas son sugerencia, puedes utilizar cualquier otra herramienta que cumpla con las funcionalidades requeridas.

Evidencia: Documento PDF.  

---
# # Reporte Técnico: Implementación de un Entorno de Entrega Continua con Docker y Jenkins

## Introduction:
La entrega continua (CD) es una metodología de desarrollo de software que permite automatizar los pasos desde la integración hasta la producción. Su objetivo principal es minimizar el tiempo transcurrido entre la escritura de una línea de código y su puesta a disposición de los usuarios finales. La implementación efectiva de un pipeline de CD requiere la orquestación de diversas herramientas y procesos. En este reporte, se describe el proceso técnico para establecer un entorno de entrega continua robusto y escalable utilizando Docker como tecnología de contenerización y Jenkins como herramienta principal de automatización del pipeline. Se abordará la creación de imágenes de contenedores, la configuración de Jenkins para la automatización de despliegues y la validación del proceso mediante una aplicación de prueba, demostrando cómo estas tecnologías facilitan la construcción de un flujo de trabajo de desarrollo ágil y eficiente.

---

## Development:
## 1. Prerrequisitos y Herramientas

Para la implementación, se asumen los siguientes prerrequisitos:

*   Un sistema operativo compatible con Docker (Linux, Windows, macOS).
*   Docker Engine instalado y configurado.
*   Jenkins instalado y en ejecución. Se recomienda desplegar Jenkins en un contenedor Docker para simplificar su gestión.
*   Un sistema de control de versiones (SCM) como Git.
*   Una aplicación de prueba (ej. una simple aplicación web en Node.js, Python Flask, o Java Spring Boot).

## 2. Creación de Imágenes de Contenedores Docker

El primer paso en el pipeline de CD es encapsular la aplicación en un contenedor Docker. Esto se logra definiendo un `Dockerfile`. Este archivo especifica las instrucciones para construir la imagen, incluyendo la base de la imagen, la copia del código fuente, la instalación de dependencias, la exposición de puertos y el comando de inicio de la aplicación.

Ejemplo básico de `Dockerfile` para una aplicación Node.js:

```dockerfile
FROM node:14
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD [ "node", "index.js" ]
```

La imagen se construye utilizando el comando `docker build -t nombre-imagen:version .`. Es crucial etiquetar las imágenes con versiones o hashes de commit para garantizar la trazabilidad y la inmutabilidad.

## 3. Configuración de Jenkins para Entrega Continua

Jenkins actuará como el orquestador del pipeline. La configuración implica los siguientes pasos:

*   **Instalación de Plugins:** Instalar plugins relevantes como 'Docker Pipeline', 'Git', 'Pipeline', y otros necesarios para integrar con herramientas de testing o despliegue específicas.
*   **Configuración de Credenciales:** Configurar credenciales de acceso al repositorio SCM, al registro de contenedores (Docker Hub, GCR, ECR, etc.) y al entorno de despliegue.
*   **Creación de un Pipeline:** Se recomienda utilizar Jenkins Pipeline as Code definiendo el pipeline en un archivo `Jenkinsfile` en el repositorio del proyecto. Esto permite versionar el pipeline junto con el código de la aplicación.

Un `Jenkinsfile` típico incluiría etapas (`stages`) como:

*   **Checkout:** Clonar el código fuente del repositorio SCM.
*   **Build:** Construir la imagen Docker utilizando el `Dockerfile`. `docker build -t nombre-imagen:${BUILD_NUMBER} .`.
*   **Test:** Ejecutar pruebas unitarias, de integración y estáticas dentro de un contenedor o contra la imagen construida. `docker run --rm nombre-imagen:${BUILD_NUMBER} npm test`.
*   **Scan (Opcional):** Analizar la imagen en busca de vulnerabilidades de seguridad.
*   **Push:** Subir la imagen construida y etiquetada a un registro de contenedores. `docker push nombre-imagen:${BUILD_NUMBER}`.
*   **Deploy:** Desplegar la nueva versión de la aplicación utilizando la imagen recién subida. Esto puede implicar comandos `docker run`, `docker stack deploy` (Docker Swarm) o actualizaciones en Kubernetes (via `kubectl` o herramientas como Helm).

Ejemplo de estructura básica de `Jenkinsfile`:

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'YOUR_SCM_URL'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("nombre-imagen:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Test') {
            steps {
                sh 'docker run --rm nombre-imagen:${BUILD_NUMBER} npm test'
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.image("nombre-imagen:${env.BUILD_NUMBER}").push()
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stack deploy -c docker-compose.yml myapp'
            }
        }
    }
}
```

*   **Configuración de Triggers:** Configurar el job de Jenkins para que se dispare automáticamente ante cambios en el repositorio SCM (ej. un push a la rama `main`).

## 4. Prueba de la Entrega Continua

Para validar el pipeline de CD, se utiliza la aplicación de prueba:

1.  Realizar una pequeña modificación en el código fuente de la aplicación.
2.  Guardar y commitear los cambios.
3.  Hacer push de los cambios al repositorio SCM configurado en Jenkins.
4.  Verificar que el trigger de Jenkins detecta el cambio y inicia una nueva ejecución del pipeline.
5.  Monitorear la ejecución del pipeline en la interfaz de Jenkins, asegurando que cada etapa (Checkout, Build, Test, Push, Deploy) se complete exitosamente.
6.  Confirmar que la nueva versión de la aplicación ha sido desplegada y es accesible en el entorno de destino (ej. verificando la versión en el navegador o mediante una API).

Si alguna etapa falla (ej. las pruebas unitarias no pasan), el pipeline debe detenerse, impidiendo que la versión defectuosa sea desplegada. Esto demuestra la efectividad del pipeline para mantener la calidad del software.

---

## Conclusion:
La implementación de un entorno de entrega continua utilizando Docker y Jenkins proporciona una base sólida para acelerar el ciclo de desarrollo, mejorar la fiabilidad de los despliegues y reducir el riesgo asociado con los cambios en el software. Docker asegura la consistencia del entorno a través de todo el pipeline, desde el desarrollo hasta la producción, eliminando problemas de 'funciona en mi máquina'. Jenkins, por su parte, automatiza y orquesta el flujo de trabajo, permitiendo que los equipos se enfoquen en desarrollar nuevas funcionalidades en lugar de gestionar procesos manuales de despliegue. La combinación de estas herramientas facilita la adopción de prácticas DevOps, permitiendo entregas más frecuentes, predecibles y seguras, lo cual es fundamental en el panorama tecnológico actual.

---

## References:
1.  Documentación oficial de Docker: `https://docs.docker.com/`
2.  Documentación oficial de Jenkins: `https://www.jenkins.io/doc/`
3.  Jenkins Pipeline Documentation: `https://www.jenkins.io/doc/book/pipeline/`
4.  Ejemplos de Dockerfiles: `https://docs.docker.com/engine/examples/`
5.  Conceptos de Entrega Continua y DevOps.

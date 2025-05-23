# 05 Diferencias entre un proyecto y Continuous Delivery/DevOps

**Elaborado por**: Daniel Tejeda Saavedra  
**Registro**: 22310431  
**Fecha**: 14 jun 2025  
**Materia**: Gestión de servicios de TI (2025 Feb - Jun)  
**Profesor**: José Francisco Pérez Reyes  
**Indicaciones**: Elaborar un diagrama que compare visualmente el ciclo de vida de un proyecto tradicional con el enfoque de Continuous Delivery/DevOps.

Evidencia: Documento PDF.  

---
# Análisis Comparativo: Ciclo de Vida de Proyecto Tradicional vs. Enfoque Continuous Delivery/DevOps

## Introduction:
El ciclo de vida de un proyecto tradicional, frecuentemente asociado a metodologías secuenciales como Waterfall, se caracteriza por una progresión lineal a través de fases discretas y bien definidas. En contraste, el enfoque de Continuous Delivery (CD) y DevOps representa un paradigma moderno que enfatiza la colaboración, la automatización y la entrega continua de valor. Este reporte técnico tiene como objetivo analizar y comparar las características fundamentales de ambos modelos de ciclo de vida de proyecto, destacando sus diferencias estructurales, operacionales y culturales, con el fin de proporcionar una base conceptual para la elección y aplicación de la metodología más adecuada según el contexto del proyecto.

---

## Development:
El ciclo de vida tradicional se estructura en fases secuenciales típicas: Recopilación de Requisitos, Diseño, Implementación, Pruebas, Despliegue y Mantenimiento. La transición entre fases es unidireccional; una fase debe completarse antes de iniciar la siguiente. Esta estructura impone 'gates' formales y revisiones extensas entre etapas, lo que resulta en ciclos de desarrollo prolongados y una retroalimentación tardía sobre el producto. La comunicación y colaboración suelen ser departamentales, con handover significativos entre equipos (ej. Desarrollo a QA, QA a Operaciones).

Por otro lado, el enfoque Continuous Delivery/DevOps redefine el ciclo de vida como un flujo continuo e iterativo, a menudo visualizado como un bucle infinito (Planificar, Codificar, Construir, Probar, Liberar, Desplegar, Operar, Monitorizar). La distinción clave radica en la eliminación de barreras entre las fases mediante la automatización extensiva y la integración de equipos. La automatización abarca la integración continua (CI), las pruebas automatizadas, la gestión de configuración y el despliegue continuo. Los equipos son multifuncionales, fomentando la colaboración temprana y constante entre desarrollo, operaciones y otras áreas (ej. QA, seguridad). La retroalimentación es rápida y continua, obtenida a través de monitorización y métricas en tiempo real, permitiendo adaptaciones ágiles y la corrección temprana de defectos. Las entregas son pequeñas, incrementales y frecuentes, reduciendo el riesgo asociado a despliegues de gran envergadura típicos del modelo tradicional.

---

## Conclusion:
La comparación entre el ciclo de vida de proyecto tradicional y el enfoque Continuous Delivery/DevOps revela diferencias fundamentales en estructura, procesos y cultura. Mientras el modelo tradicional ofrece predictibilidad en entornos estáticos y requisitos estables a costa de flexibilidad y velocidad, CD/DevOps sobresale en entornos dinámicos que exigen adaptabilidad, entregas rápidas y alta calidad. La adopción de CD/DevOps implica una transformación cultural hacia la colaboración y un compromiso con la automatización a lo largo de todo el pipeline de entrega. La elección entre ambos enfoques debe basarse en una evaluación rigurosa de los requisitos del proyecto, la naturaleza del producto, la estabilidad del entorno y la madurez organizacional, reconociendo que CD/DevOps representa la evolución hacia prácticas de ingeniería de software más eficientes y resilientes para la era digital.

---

## References:
Los conceptos discutidos se basan en principios de gestión de proyectos (PMBOK, metodologías secuenciales), metodologías ágiles (Scrum, Kanban) y las prácticas y principios de DevOps y Continuous Delivery descritos en literatura técnica y estándares de la industria.


import streamlit as st


# Configuración de la página
st.set_page_config(
    page_title="Home - Dashboard Base de Datos SIU",
    page_icon="🏠",
    layout="wide"
)

# Título principal
st.title("🏠 Dashboard Base de Datos SIU")

# Introducción general
st.markdown(
    """
    Bienvenido al **Dashboard Base de Datos SIU**.  
    Este sistema permite visualizar y analizar información en tiempo real sobre la base de
    datos de la SIU alojada en Elektra

    """
)

# Sección 1: ¿Qué encontrarás en este dashboard?
st.header("📊 ¿Qué encontrará en este dashboard?")
st.markdown(
    """
    - **Listado de analizadores disponibles** en la base de datos.  
    - **Últimas calibraciones** realizadas, incluyendo parámetros como *offsetV*, *gainV*, etc.  
    - **Historial de cambios** en los paneles conectados a cada analizador.  
    - **Visualización de datos clave** para diagnóstico y mantenimiento.  
    - **Paneles Solares**: Detalles técnicos de los paneles instalados.
    - **Calibraciones**: Registros de calibraciones realizadas en los analizadores.
    - **Cambios de Conexión**: Historial de cambios en las conexiones de los paneles.
    - **Curvas I-V**: Visualización de curvas de voltaje-corriente registradas.
    """
)

# Sección 2: ¿Por qué es importante esta información?
st.header("⚡ ¿Por qué es importante?")
st.markdown(
    """
    Este dashboard ayuda a monitorear el estado de los analizadores, asegurando:  
    - **Calibraciones actualizadas** para mediciones precisas.  
    - **Registro de cambios** en los paneles conectados.  
    - **Optimización del rendimiento** de los equipos mediante análisis de datos históricos.  
    """
)

# # Sección 3: Cómo navegar en el dashboard
# st.header("🛠️ ¿Cómo usar este dashboard?")
# st.markdown(
#     """
#     - **🔍 Explora la pestaña de Analizadores** para ver la lista de equipos disponibles.  
#     - **📅 Consulta las calibraciones** para obtener detalles sobre las últimas mediciones.  
#     - **🔄 Revisa los cambios de paneles** para verificar qué dispositivos han sido conectados o modificados.  
#     - **📈 Usa las herramientas de filtrado y análisis** para extraer información relevante.  
#     """
# )

# # Pie de página
# st.markdown("---")
# st.markdown("🔹 *Este dashboard ha sido desarrollado como parte del proyecto de monitoreo de analizadores eléctricos.*")

# import streamlit as st

# # Configuración de la página
# st.set_page_config(page_title="Dashboard SIU - UdeA", layout="wide")

# # Título de la página
# st.title("Dashboard SIU - UdeA")
# st.markdown("---")

# # Sección 1: Resumen del Proyecto
# st.header("Resumen del Proyecto")
# st.write("""
# El proyecto **Rediseño del Sistema de Gestión de Datos en la SIU, UdeA** tiene como objetivo principal rediseñar e integrar un nuevo proceso para el manejo de datos relacionados con paneles solares, calibraciones, análisis y monitoreo. 
# La base de datos centralizada permite gestionar información técnica, como calibraciones de analizadores, parámetros de paneles solares, cambios de conexión y curvas de voltaje-corriente.
# """)

# # Sección 2: Objetivo Principal
# st.header("Objetivo Principal")
# st.write("""
# El objetivo es garantizar una gestión eficiente y escalable de los datos recopilados en la Sede de Investigación Universitaria (SIU) de la Universidad de Antioquia (UdeA), desde la obtención de datos hasta su procesamiento y almacenamiento en una base de datos estructurada.
# """)

# # Sección 5: Acceso Rápido a Datos
# st.header("Acceso Rápido a Datos")


# Footer

# import streamlit as st

# # Configuración de la página
# st.set_page_config(
#     page_title="Home - Dashboard de Datos",
#     page_icon="📊",
#     layout="wide"
# )

# # Título principal
# st.title("📊 Dashboard de Datos")

# # Introducción general
# st.markdown(
#     """
#     Bienvenido al **Dashboard de Datos**.  
#     Este sistema permite visualizar y analizar información relevante de manera interactiva, 
#     facilitando la toma de decisiones basada en datos.  
#     """
# )

# # Sección 1: ¿Qué encontrarás en este dashboard?
# st.header("🔎 ¿Qué encontrarás en este dashboard?")
# st.markdown(
#     """
#     - **Visualización de datos clave** a través de gráficos dinámicos.  
#     - **Exploración de tendencias y patrones** en los datos históricos.  
#     - **Análisis de indicadores relevantes** para la toma de decisiones.  
#     - **Herramientas de filtrado y segmentación** para un análisis más detallado.  
#     """
# )

# # Sección 2: ¿Por qué es importante esta información?
# st.header("📈 ¿Por qué es importante?")
# st.markdown(
#     """
#     Este dashboard facilita el análisis de datos para:  
#     - **Monitorear cambios y tendencias** en la información disponible.  
#     - **Optimizar procesos y mejorar el rendimiento** mediante análisis basados en datos.  
#     - **Facilitar la toma de decisiones** con información clara y estructurada.  
#     """
# )

# # Sección 3: Cómo navegar en el dashboard
# st.header("🛠️ ¿Cómo usar este dashboard?")
# st.markdown(
#     """
#     - **📊 Explora las secciones de gráficos** para visualizar información clave.  
#     - **🔎 Aplica filtros y segmentaciones** para enfocar el análisis en datos específicos.  
#     - **📅 Revisa tendencias históricas** para identificar patrones importantes.  
#     - **📥 Descarga y exporta datos** para su análisis externo si es necesario.  
#     """
# )

# # Pie de página
# st.markdown("---")
# st.markdown("🔹 *Este dashboard ha sido desarrollado para facilitar la exploración y análisis de datos de manera eficiente.*")

# st.markdown("---")
# st.write("GIMEL - Universidad de Antioquia")


# # Sección 3: Datos Clave del Proyecto
# st.header("Datos Clave del Proyecto")
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.subheader("Paneles Solares")
#     st.metric(label="Total de Paneles", value="6")
#     st.write("Tecnologías: CIGS, HIT, Monocristalino")

# with col2:
#     st.subheader("Calibraciones")
#     st.metric(label="Calibraciones Realizadas", value="7")
#     st.write("Última calibración: 30/12/2024")

# with col3:
#     st.subheader("Cambios de Conexión")
#     st.metric(label="Cambios Registrados", value="12")
#     st.write("Último cambio: 29/01/2023")

# # Sección 4: Visualización de Datos
# st.header("Visualización de Datos")
# st.write("""
# A continuación, se presentan gráficos y métricas clave para visualizar el estado actual de los datos recopilados en la base de datos.
# """)

# # Gráficos de ejemplo (placeholders)
# st.subheader("Progreso de Calibraciones")
# st.line_chart([1, 2, 3, 4, 5, 6, 7])  # Ejemplo de gráfico de progreso

# st.subheader("Distribución de Tecnologías de Paneles")
# st.bar_chart({
#     "CIGS": 3,
#     "HIT": 1,
#     "Monocristalino": 2
# })

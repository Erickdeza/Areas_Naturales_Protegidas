import streamlit as st
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools

# Título principal
st.title("Áreas Naturales Protegidas (ANP) de Administración Nacional Definitiva")

# Definir las opciones con botones dentro de un expander
with st.expander("Selecciona una opción:", expanded=True):
    opcion = st.radio("", ("Introducción a las Áreas Protegidas del Perú", "Distribución Regional de Áreas Protegidas", "Superficie territorial de las Áreas Protegidas en el Perú","Antigüedad Histórica de las Áreas Protegidas del Perú","Nosotros: Presentación del Grupo y su Compromiso con las Áreas Protegidas del Perú"), index=0, format_func=lambda x: x)

# Mostrar contenido según la opción seleccionada
if opcion == "Introducción a las Áreas Protegidas del Perú":
    with st.expander("Introducción"):
        st.write("""
        Las Áreas Naturales Protegidas (ANP) de Administración Nacional en Perú, gestionadas por el SERNANP, buscan conservar la biodiversidad, los ecosistemas y el patrimonio cultural. Protegen especies en peligro de extinción y sitios arqueológicos importantes. El SERNANP regula actividades humanas y fomenta el turismo sostenible y la investigación científica. La red de ANP incluye diversos ecosistemas, desde la Amazonía hasta los Andes y la costa, asegurando la preservación del patrimonio natural y cultural del país.
        """)
        # Mostrar la imagen
        imagen = "IMAGEN6.jpg"
        st.image(imagen, use_column_width=True)

    # Texto que aparecerá debajo de la imagen cuando se haga clic
    st.markdown("""
    *Las áreas naturales son la biblioteca más antigua y valiosa de la Tierra.*
    """)
    
    # Aquí deberías tener cargado tu DataFrame 'df' con los datos necesarios
    # Supongamos que 'df' contiene la columna 'ANP_CATE' que deseas graficar
    df = pd.read_excel("PARTE2.xlsx")

    # Conteo de categorías
    categorias = df['ANP_CATE'].value_counts()

    # Calcular porcentajes
    categorias_percentage = categorias / categorias.sum() * 100

    # Crear figura y ejes
    fig, ax = plt.subplots()

    # Definir una paleta de colores personalizada degradada (de amarillo oscuro a verde oscuro)
    colors = plt.cm.Oranges_r(categorias_percentage / max(categorias_percentage))

    # Graficar barras horizontales con colores personalizados y bordes negros
    bars = ax.barh(categorias_percentage.index, categorias_percentage.values, color=colors, edgecolor='black', linewidth=1.2)

    # Agregar etiquetas de porcentaje en las barras
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width:.2f}%', 
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0), 
                    textcoords='offset points',
                    ha='left', va='center', color='black')  

    # Configurar leyenda y ejes
    ax.set_xlabel('Porcentaje')
    ax.set_ylabel('Categoría de ANP')
    ax.set_title('Porcentaje de Áreas Naturales Protegidas por Categoría')

    # Cambiar el color y el borde de la barra 'Reserva Nacional'
    for i, bar in enumerate(bars):
        categoria = categorias_percentage.index[i]
        if categoria == 'Reserva Nacional':
            bar.set_color('#FFA500')  # Color naranja
            bar.set_edgecolor('black')  # Borde negro

    # Mostrar gráfico en Streamlit
    st.pyplot(fig)
    st.title("Tipos de Áreas Naturales Protegidas en Perú")
    with st.expander("1. Parque Nacional"):
        st.write("Área protegida para conservar biodiversidad y paisajes, con recreación controlada y educación ambiental.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video1.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("2. Reserva Nacional"):
        st.write("Área para conservación, investigación y uso sostenible de recursos naturales bajo normativas específicas.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video2.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("3. Santuario Nacional"):
        st.write("Área protegida para conservar especies o hábitats únicos, restringiendo la actividad humana para su preservación a largo plazo.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video3.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("4. Santuario Histórico"):
        st.write("Espacio designado para proteger y conservar sitios importantes relacionados con eventos, personas o culturas significativas de la historia.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video4.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("5. Refugio de Vida Silvestre"):
        st.write("Espacio para conservar hábitats y especies amenazadas, fomenta investigación y educación ambiental.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video5.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("6. Bosque de Protección"):
        st.write("Área forestal para conservar ecosistemas y biodiversidad.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video6.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("7. Reserva Paisajista"):
        st.write("Reserva que permite el uso y aprovechamiento sostenible de recursos por poblaciones locales mediante planes de manejo. Actualmente hay dos en Perú.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video7.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("8. Reserva Comunales"):
        st.write("Son áreas naturales protegidas de uso directo. Actualmente existen en el Perú 10 Reservas Comunales.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video8.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("9. Coto de Caza"):
        st.write("Espacios destinados al aprovechamiento de la fauna silvestre. Son áreas naturales protegidas de uso directo. Actualmente existen en el Perú 2 Cotos de Caza.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales”')
        video = open('video9.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)








elif opcion == "Distribución Regional de Áreas Protegidas":
    st.header("Áreas Protegidas por Regiones")
    st.write("""
    Aquí podrías proporcionar información detallada sobre las áreas protegidas por regiones en Perú.
    """)

    # Cargar los datos desde el archivo CSV
    import pandas as pd
    import matplotlib.pyplot as plt

    filename = 'PARTE3.csv'
    df = pd.read_csv("PARTE3.csv") #pd.read_excel("PARTE2.xlsx")

    # Obtener las opciones únicas de la columna ANP_UBPO (regiones)
    regiones = df['ANP_UBPO'].unique()

    # Mostrar el selector de regiones debajo del título
    st.header('Selecciona una región:')
    selected_region = st.selectbox('', regiones)

    # Filtrar el DataFrame por la región seleccionada
    filtered_data = df[df['ANP_UBPO'] == selected_region]

    # Calcular la cantidad de áreas protegidas por categoría
    category_counts = filtered_data['ANP_CATE'].value_counts()

    # Convertir a entero si no lo está y asegurarse de quitar los decimales
    category_counts = category_counts.astype(int)

    # Crear una gráfica de barras vertical con colores degradados de naranja a café
    fig, ax = plt.subplots()

    # Definir una paleta de colores personalizada degradada (de naranja a café)
    # Puedes ajustar los colores según tus preferencias
    n_colors = len(category_counts)
    colors = plt.cm.colors.LinearSegmentedColormap.from_list("custom", ['#FFA500', '#8B4513'], N=n_colors)

    # Graficar barras verticales con colores personalizados y bordes negros
    bars = ax.bar(category_counts.index, category_counts.values, color=colors(range(n_colors)), edgecolor='black', linewidth=1.2)

    # Agregar etiquetas de cantidad encima de las barras
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords='offset points',
                    ha='center', va='bottom', color='black')  # Ajustar color del texto a negro

    # Configurar leyenda y ejes
    ax.set_xlabel('Categoría de ANP')
    ax.set_ylabel('Cantidad de áreas protegidas')
    ax.set_title(f'Cantidad de áreas protegidas por categoría en {selected_region}')

    # Asegurar que la barra de 'Reserva Nacional' sea más visible cambiando su color específicamente
    # Iterar sobre las barras y comparar directamente el nombre de la categoría
    for i, bar in enumerate(bars):
        categoria = category_counts.index[i]
        if categoria == 'Reserva Nacional':
            bar.set_color('#8B4513')  # Cambiar a un color café más oscuro (puedes ajustar el color)

    # Rotar las etiquetas del eje x para mejorar la legibilidad
    plt.xticks(rotation=45, ha='right')

    # Mostrar gráfico en Streamlit
    st.pyplot(fig)

    # Mostrar el nombre de las áreas protegidas en un cuadro
    st.subheader(f'Áreas protegidas en {selected_region}:')
    areas_protegidas = filtered_data['ANP_NOMB'].unique()
    for area in areas_protegidas:
        st.markdown(f"- {area}")  # Mostrar cada área protegida como un elemento de lista




elif opcion == "Superficie territorial de las Áreas Protegidas en el Perú":
    # Datos de áreas protegidas (ejemplo ficticio)
    archivo = pd.read_csv('PARTE4.csv')
    areas = archivo['ANP_UBPO'].unique()

    # Frases sobre las ANP
    frases_anp = [
        "*Salvemos nuestra diversidad, salvemos las ANP.*",
        "*ANP: Protección a la vida silvestre.*",
        "*ANP, tesoro de nuestro país.*",
        "*“La conservación solo es sostenible si el poblador percibe que los ecosistemas adecuadamente manejados en las áreas naturales protegidas pueden brindar beneficios económicos tangibles para él y su familia.”*"
    ]

    # Mostrar el título y selección de áreas protegidas
    st.header('Extensión Territorial de las Áreas Protegidas en el Perú: Superficie en km²')
    area_seleccionada = st.selectbox('Selecciona una región', areas)

    # Filtrar datos según el área seleccionada
    data_area = archivo[archivo['ANP_UBPO'] == area_seleccionada]

    # Mostrar la selección de área
    st.write(f'Área seleccionada: {area_seleccionada}')

    # Selección rotativa de frases sobre ANP
    frase_index = st.session_state.get('frase_index', itertools.cycle(range(len(frases_anp))))

    # Crear gráfico usando seaborn en una figura de matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))  # Crear figura y ejes
    sns.barplot(x='ANP_CATE', y='ANP_SULEG', data=data_area, orient='v', palette='YlOrRd', ax=ax)

    # Mostrar los valores de ANP_SULEG encima de las barras
    for p in ax.patches:
        ax.annotate(f'{p.get_height():,.2f}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black', xytext=(0, 5),
                    textcoords='offset points')

    ax.set_title(f'Categorías de Áreas Protegidas en {area_seleccionada}')
    ax.set_xlabel('Categoría (ANP_CATE)')
    ax.set_ylabel('Superficie (ANP_SULEG)')
    plt.tight_layout()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

    # Actualizar la frase rotativa
    st.markdown("")
    st.markdown("*" + frases_anp[next(frase_index)] + "*")

    # Guardar el estado actual del índice de frase en la sesión
    st.session_state.frase_index = frase_index

    # Configuración de la aplicación Streamlit
    st.header('Preguntas sobre Áreas Naturales Protegidas')

    # Pregunta y opciones de respuesta
    pregunta1 = "¿Cuántas áreas naturales existen?"
    opciones = [
        "Existen 11 áreas naturales.",
        "Existen 7 áreas naturales.",
        "Existen 9 áreas naturales."
    ]

    # Mostrar la pregunta y las opciones de respuesta
    respuesta_usuario = st.radio(pregunta1, options=opciones)

    # Validar la respuesta
    respuesta_correcta = "Existen 9 áreas naturales."

    if respuesta_usuario == respuesta_correcta:
        st.success("Respuesta correcta.")
    else:
        st.error(f"Respuesta incorrecta. La respuesta correcta es: {respuesta_correcta}")
    import streamlit as st

    # Configuración de la aplicación Streamlit
    st.header('SERNANP - Servicio Nacional de Áreas Naturales Protegidas por el Estado')

    # Pregunta inicial
    st.write('Pregunta:')
    st.write("¿Cuándo fue creado el Servicio Nacional de Áreas Naturales Protegidas por el estado?")

    # Respuesta correcta
    respuesta_correcta = "El Servicio Nacional de Áreas Naturales Protegidas por el Estado (SERNANP) fue creado el 13 de mayo del año 2008, como organismo público técnico especializado adscrito al Ministerio del Ambiente y ente rector del Sistema Nacional de Áreas Naturales Protegidas por el Estado (SINANPE)."

    # Botón para mostrar la respuesta
    if st.button('Mostrar respuesta'):
        st.info(respuesta_correcta)
        st.image('IMAGEN2.jpeg', caption='Imagen relacionada')

    # Expander para información adicional
    with st.expander('Más información sobre SERNANP'):
        st.write("""
        El Servicio Nacional de Áreas Naturales Protegidas por el Estado (SERNANP) es el organismo público técnico especializado del Perú encargado de la gestión y conservación de las áreas naturales protegidas del país.
        
        Funciones principales del SERNANP:
        - Administración, conservación y uso sostenible de las áreas naturales protegidas.
        - Promoción de la investigación científica y la educación ambiental.
        - Desarrollo de actividades de ecoturismo y recreación compatible con la conservación.
        
        Para más detalles, visita [SERNANP](https://www.sernanp.gob.pe/).
        """)



elif opcion == "Antigüedad Histórica de las Áreas Protegidas del Perú":
         # Cargar el archivo CSV
    archivo_csv = 'parte6.csv'  # Reemplaza con el nombre correcto de tu archivo CSV
    archivo = pd.read_csv(archivo_csv)

    # Obtener las áreas únicas (ANP_UBPO)
    regiones = archivo['ANP_UBPO'].unique()

    # Configuración de la aplicación Streamlit
    st.title('Áreas Protegidas y su Antigüedad')

    # Selección de región desde la barra lateral
    region_seleccionada = st.selectbox('Seleccione su region', regiones)

    # Filtrar datos según la región seleccionada
    data_region = archivo[archivo['ANP_UBPO'] == region_seleccionada]

    # Mostrar la selección de región
    st.write(f'Región seleccionada: {region_seleccionada}')

    # Definir paleta de colores personalizada de rojo a amarillo
    colores = sns.color_palette("YlOrRd", len(data_region))

    # Crear gráfico interactivo usando seaborn en una figura de matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))  # Crear figura y ejes
    sns.barplot(x='ANP_CATE', y='AÑOS', data=data_region, palette=colores, ax=ax)

    # Estilizar el gráfico
    ax.set_title(f'Antigüedad de Áreas Protegidas en {region_seleccionada}')
    ax.set_xlabel('Categoría de Área Protegida (ANP_CATE)')
    ax.set_ylabel('Antigüedad en Años (AÑOS)')
    ax.grid(True, axis='y', linestyle='--')

    # Rotar etiquetas del eje X para mejor visualización
    plt.xticks(rotation=45)

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)
    import streamlit as st

    # Estilo CSS para alinear imágenes a la derecha
    st.markdown(
        """
        <style>
        .image-right {
            float: right;
            margin-left: 15px;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Pregunta 1 y respuesta con imagen
    st.write("PREGUNTA 1: ¿Cuál de las áreas Naturales y Protegidas es la más antigua en el Perú?")
    respuesta1 = """
    **Respuesta:**  
    La Reserva Nacional de Lachay es una de las áreas protegidas más antiguas del Perú. Fue establecida el 21 de junio de 1977 mediante el Decreto Supremo N° 310-77-AG. La reserva es conocida por sus bosques de niebla que albergan una gran diversidad de flora y fauna.
    """
    # Mostrar respuesta 1 con imagen alineada a la derecha
    if st.button('Mostrar respuesta 1'):
        st.info(respuesta1)


    # Pregunta 2 y respuesta con imagen
    st.write("DATOS CURIOSOS QUE DEBES CONOCER")
    st.write("1. Sabías que el Parque Nacional del Manu, ubicado en la región de Madre de Dios y establecido en 1973, es reconocido por la UNESCO como Reserva de Biosfera y Patrimonio de la Humanidad desde 1987.")

    # Pregunta 3 y respuesta con imagen
    st.write("2. Sabías que la Reserva Nacional de Pampa Galeras-Barbara D'Achille, ubicada en la región de Ayacucho, es conocida por ser un santuario para la conservación de la vicuña, una especie emblemática de los Andes peruanos. Esta reserva fue creada en 1967.")




elif opcion == "Nosotros: Presentación del Grupo y su Compromiso con las Áreas Protegidas del Perú":
        # Título principal
    st.title('Conoce a nuestro equipo de Ingeniería Ambiental')

    # Información de cada integrante
    integrantes = [
        {
            'nombre': 'Deza Mamani Erick Armando',
            'descripcion': 'Hola! Soy el integrante 1. Me apasiona la conservación de la biodiversidad y la gestión sostenible de recursos naturales.',
            'imagen': 'IMAGEN1.jpeg'
        },
        {
            'nombre': 'Flores Messco Fiorella Ingrid ',
            'descripcion': '¡Hola a todos! Soy el integrante 2. Mi interés principal es la calidad del aire y el impacto ambiental de las industrias.',
            'imagen': 'IMAGEN2.jpeg'
        },
        {
            'nombre': 'Huamani Huallpa Ibet Yesenia',
            'descripcion': 'Saludos! Soy el integrante 3. Me especializo en la gestión de residuos sólidos y la promoción de prácticas ecoamigables.',
            'imagen': 'IMAGEN3.jpg'
        },
        {
            'nombre': 'Sanchez Ticllasuca Brenda Estefany',
            'descripcion': 'Hola a todos! Soy el integrante 4. Mi enfoque está en la educación ambiental y la sensibilización comunitaria.',
            'imagen': 'IMAGEN4.jpg'
        }
    ]

    # Mostrar información de cada integrante
    for integrante in integrantes:
        st.header(integrante['nombre'])
        try:
            st.image(integrante['imagen'], caption=integrante['nombre'], use_column_width=True)
        except FileNotFoundError:
            st.write(f"No se pudo encontrar la imagen {integrante['imagen']}. Verifica la ruta y asegúrate de que el archivo esté disponible.")
        if st.checkbox(f"Mostrar descripción de {integrante['nombre']}"):
            st.write(integrante['descripcion'])
        st.markdown('---')  # Separador entre integrantes

    # Campo para comentarios o retroalimentación
    st.header('Comentarios y Retroalimentación')
    comentario = st.text_area('Escribe aquí tu comentario o retroalimentación:', height=150)
    if st.button('Enviar comentario'):
        # Aquí podrías guardar el comentario en una base de datos, archivo, enviar por correo, etc.
        st.success('¡Comentario enviado correctamente!')







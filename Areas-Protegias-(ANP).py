import streamlit as st
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools


st.title("Áreas Naturales Protegidas (ANP) de Administración Nacional Definitiva")

with st.expander("Selecciona una opción:", expanded=True):
    opcion = st.radio("", ("Introducción a las Áreas Protegidas del Perú", "Distribución de áreas naturales por departamento", "Superficie Territorial de Áreas Naturales Protegidas en el Perú","Antigüedad de Áreas Naturales Protegidas del Perú","Nosotros: Presentación del Grupo y su Compromiso con las Áreas Protegidas del Perú"), index=0, format_func=lambda x: x)

if opcion == "Introducción a las Áreas Protegidas del Perú":
    with st.expander("Introducción"):
        st.write("""
        El informe presenta un estudio sobre las Áreas Naturales Protegidas (ANP) de Administración Nacional Definitiva en Perú, subrayando su importancia en la conservación de la biodiversidad y la sostenibilidad ambiental. Utilizando datos del SERNANP, se ha creado una aplicación web interactiva con tecnologías como Streamlit y Visual Studio Code, que facilita la visualización y el análisis de la distribución y extensión de las ANP.
        """)
        imagen = "IMAGEN6.jpg"
        st.image(imagen, use_column_width=True)

    st.markdown("""
    *Las áreas naturales son la biblioteca más antigua y valiosa de la Tierra.*
    """)
    

    df = pd.read_excel("PARTE2.xlsx")

    categorias = df['ANP_CATE'].value_counts()

    categorias_percentage = categorias / categorias.sum() * 100

    fig, ax = plt.subplots()

    colors = plt.cm.Oranges_r(categorias_percentage / max(categorias_percentage))

    bars = ax.barh(categorias_percentage.index, categorias_percentage.values, color=colors, edgecolor='black', linewidth=1.2)

    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width:.2f}%', 
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0), 
                    textcoords='offset points',
                    ha='left', va='center', color='black')  

    ax.set_xlabel('Porcentaje')
    ax.set_ylabel('Categoría de ANP')
    ax.set_title('Porcentaje de Áreas Naturales Protegidas por Categoría')

    for i, bar in enumerate(bars):
        categoria = categorias_percentage.index[i]
        if categoria == 'Reserva Nacional':
            bar.set_color('#FFA500')  
            bar.set_edgecolor('black')  

    st.pyplot(fig)
    st.title("Tipos de Áreas Naturales Protegidas en Perú")
    with st.expander("1. Parque Nacional"):
        st.write("Área protegida para conservar biodiversidad y paisajes, con recreación controlada y educación ambiental.")
        st.subheader('"Explorar una reserva nacional es como abrir un cofre lleno de maravillas naturales.”')
        video = open('video1.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("2. Reserva Nacional"):
        st.write("Área para conservación, investigación y uso sostenible de recursos naturales bajo normativas específicas.")
        st.subheader('"Cuidar las áreas protegidas es un acto de amor hacia nuestro planeta."')
        video = open('video2.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("3. Santuario Nacional"):
        st.write("Área protegida para conservar especies o hábitats únicos, restringiendo la actividad humana para su preservación a largo plazo.")
        st.subheader('"Las áreas naturales protegidas son el santuario de la tierra."')
        video = open('video3.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("4. Santuario Histórico"):
        st.write("Espacio designado para proteger y conservar sitios importantes relacionados con eventos, personas o culturas significativas de la historia.")
        st.subheader('"Respeta y protege las áreas naturales para que las futuras generaciones también puedan disfrutar de su belleza."')
        video = open('video4.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("5. Refugio de Vida Silvestre"):
        st.write("Espacio para conservar hábitats y especies amenazadas, fomenta investigación y educación ambiental.")
        st.subheader('"La riqueza de una nación se mide por su capacidad de conservar sus áreas naturales."')
        video = open('video5.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("6. Bosque de Protección"):
        st.write("Área forestal para conservar ecosistemas y biodiversidad.")
        st.subheader('"Cada árbol, cada río, cada especie en una área protegida es un recordatorio de la belleza del planeta."')
        video = open('video6.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("7. Reserva Paisajista"):
        st.write("Reserva que permite el uso y aprovechamiento sostenible de recursos por poblaciones locales mediante planes de manejo. Actualmente hay dos en Perú.")
        st.subheader('“La naturaleza es la puerta al alma.”')
        video = open('video7.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("8. Reserva Comunales"):
        st.write("Son áreas naturales protegidas de uso directo. Actualmente existen en el Perú 10 Reservas Comunales.")
        st.subheader('“No existe nada más pacífico que la contemplación de la naturaleza.”')
        video = open('video8.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)
    with st.expander("9. Coto de Caza"):
        st.write("Espacios destinados al aprovechamiento de la fauna silvestre. Son áreas naturales protegidas de uso directo. Actualmente existen en el Perú 2 Cotos de Caza.")
        st.subheader('“Áreas protegidas, tesoros compartidos.”')
        video = open('video9.mp4', 'rb')
        video_1 = video.read()
        st.video(video_1)








elif opcion == "Distribución de áreas naturales por departamento":
    st.header("Áreas Protegidas por Regiones")
    st.write("""
    Aquí podrías proporcionar información detallada sobre las áreas protegidas por regiones en Perú.
    """)

    import pandas as pd
    import matplotlib.pyplot as plt

    filename = 'PARTE3.csv'
    df = pd.read_csv("PARTE3.csv") 

    regiones = df['ANP_UBPO'].unique()

    st.header('Selecciona una región:')
    selected_region = st.selectbox('', regiones)

    filtered_data = df[df['ANP_UBPO'] == selected_region]

    category_counts = filtered_data['ANP_CATE'].value_counts()

    category_counts = category_counts.astype(int)

    fig, ax = plt.subplots()


    n_colors = len(category_counts)
    colors = plt.cm.colors.LinearSegmentedColormap.from_list("custom", ['#FFA500', '#8B4513'], N=n_colors)

    bars = ax.bar(category_counts.index, category_counts.values, color=colors(range(n_colors)), edgecolor='black', linewidth=1.2)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords='offset points',
                    ha='center', va='bottom', color='black')  # Ajustar color del texto a negro

    ax.set_xlabel('Categoría de ANP')
    ax.set_ylabel('Cantidad de áreas protegidas')
    ax.set_title(f'Cantidad de áreas protegidas por categoría en {selected_region}')

    for i, bar in enumerate(bars):
        categoria = category_counts.index[i]
        if categoria == 'Reserva Nacional':
            bar.set_color('#8B4513')  # Cambiar a un color café más oscuro (puedes ajustar el color)

    plt.xticks(rotation=45, ha='right')

    st.pyplot(fig)

    st.subheader(f'Áreas protegidas en {selected_region}:')
    areas_protegidas = filtered_data['ANP_NOMB'].unique()
    for area in areas_protegidas:
        st.markdown(f"- {area}") 




elif opcion == "Superficie Territorial de Áreas Naturales Protegidas en el Perú":
    archivo = pd.read_csv('PARTE4.csv')
    areas = archivo['ANP_UBPO'].unique()

    frases_anp = [
        "*Salvemos nuestra diversidad, salvemos las ANP.*",
        "*ANP: Protección a la vida silvestre.*",
        "*ANP, tesoro de nuestro país.*",
        "*“La conservación solo es sostenible si el poblador percibe que los ecosistemas adecuadamente manejados en las áreas naturales protegidas pueden brindar beneficios económicos tangibles para él y su familia.”*"
    ]

    st.header('Extensión Territorial de las Áreas Protegidas en el Perú: Superficie en hectáreas(ha)')
    area_seleccionada = st.selectbox('Selecciona una región', areas)

    data_area = archivo[archivo['ANP_UBPO'] == area_seleccionada]

    st.write(f'Área seleccionada: {area_seleccionada}')

    frase_index = st.session_state.get('frase_index', itertools.cycle(range(len(frases_anp))))

    fig, ax = plt.subplots(figsize=(10, 6))  # Crear figura y ejes
    sns.barplot(x='ANP_CATE', y='ANP_SULEG', data=data_area, orient='v', palette='YlOrRd', ax=ax)

    for p in ax.patches:
        ax.annotate(f'{p.get_height():,.2f}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black', xytext=(0, 5),
                    textcoords='offset points')

    ax.set_title(f'Categorías de Áreas Naturales Protegidas en {area_seleccionada}')
    ax.set_xlabel('Áreas Naturales Protegidas(ANP)')
    ax.set_ylabel('Superficie territorial(ha).')
    plt.tight_layout()

    st.pyplot(fig)

    st.markdown("")
    st.markdown("*" + frases_anp[next(frase_index)] + "*")

    st.session_state.frase_index = frase_index

    st.header('Preguntas sobre Áreas Naturales Protegidas')

    pregunta1 = "¿Cuántas áreas naturales existen?"
    opciones = [
        "Existen 11 áreas naturales.",
        "Existen 7 áreas naturales.",
        "Existen 9 áreas naturales."
    ]

    respuesta_usuario = st.radio(pregunta1, options=opciones)

    respuesta_correcta = "Existen 9 áreas naturales."

    if respuesta_usuario == respuesta_correcta:
        st.success("Respuesta correcta.")
    else:
        st.error(f"Respuesta incorrecta. La respuesta correcta es: {respuesta_correcta}")
    import streamlit as st

    st.header('SERNANP - Servicio Nacional de Áreas Naturales Protegidas por el Estado')

    st.write('Pregunta:')
    st.write("Dato Curioso")

    respuesta_correcta = "Algunos datos extraídos del año 2011 (Datos recopilados 11 años antes) veamos la diferencia."

    if st.button('Mostrar Dato curioso'):
        st.info(respuesta_correcta)
        st.image('IMAGEN2.jpeg', caption='Elaboración de MINAM_2011(ANP)')

    with st.expander('Más información sobre SERNANP'):
        st.write("""
        El Servicio Nacional de Áreas Naturales Protegidas por el Estado (SERNANP) es el organismo público técnico especializado del Perú encargado de la gestión y conservación de las áreas naturales protegidas del país.
        
        Funciones principales del SERNANP:
        - Administración, conservación y uso sostenible de las áreas naturales protegidas.
        - Promoción de la investigación científica y la educación ambiental.
        - Desarrollo de actividades de ecoturismo y recreación compatible con la conservación.
        
        Para más detalles, visita [SERNANP](https://www.sernanp.gob.pe/).
        """)



elif opcion == "Antigüedad de Áreas Naturales Protegidas del Perú":
    archivo_csv = 'parte6.csv'  
    archivo = pd.read_csv(archivo_csv)

    regiones = archivo['ANP_UBPO'].unique()

    st.title('Áreas Protegidas y su Antigüedad')

    region_seleccionada = st.selectbox('Seleccione su region', regiones)

    data_region = archivo[archivo['ANP_UBPO'] == region_seleccionada]

    st.write(f'Región seleccionada: {region_seleccionada}')

    colores = sns.color_palette("YlOrRd", len(data_region))

    fig, ax = plt.subplots(figsize=(10, 6))  # Crear figura y ejes
    sns.barplot(x='ANP_CATE', y='AÑOS', data=data_region, palette=colores, ax=ax)

    ax.set_title(f'Antigüedad de Áreas Protegidas en {region_seleccionada}')
    ax.set_xlabel('Categoría de Área Protegida (ANP_CATE)')
    ax.set_ylabel('Antigüedad en Años (AÑOS)')
    ax.grid(True, axis='y', linestyle='--')

    plt.xticks(rotation=45)

    st.pyplot(fig)
    import streamlit as st

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

    st.write("PREGUNTA 1: ¿Qué Área Natural Protegida es la más antigua en el Perú?")
    respuesta1 = """
    **Respuesta:**  
    El Parque Nacional de Cutervo, establecido en 1961, es el parque nacional más antiguo del Perú. Ubicado en la región de Cajamarca, este parque protege un área de aproximadamente 8,214 hectáreas. Es conocido por su diversa fauna y flora, que incluye especies emblemáticas como el oso de anteojos y el gallito de las rocas. Además, el parque alberga importantes ecosistemas de bosques montanos y cuevas, como la Cueva de los Guácharos, hogar del raro ave guácharo. La creación de este parque marcó un hito en la conservación de la biodiversidad en el Perú.
    """
    if st.button('Mostrar respuesta 1'):
        st.info(respuesta1)


    st.write("DATOS CURIOSOS QUE DEBES CONOCER")
    st.write("1. Sabías que el Parque Nacional del Manu, ubicado en la región de Madre de Dios y establecido en 1973, es reconocido por la UNESCO como Reserva de Biosfera y Patrimonio de la Humanidad desde 1987.")
    st.image('IMAGEN15.jpeg', caption='imagen de Areas Naturales Protegidas')
    st.write("2. Sabías que la Reserva Nacional de Pampa Galeras-Barbara D'Achille, ubicada en la región de Ayacucho, es conocida por ser un santuario para la conservación de la vicuña, una especie emblemática de los Andes peruanos. Esta reserva fue creada en 1967.")
    st.image('IMAGEN16.jpeg', caption='imagen de Areas Naturales Protegidas')



elif opcion == "Nosotros: Presentación del Grupo y su Compromiso con las Áreas Protegidas del Perú":
    st.title('¿Quienes somos?')
    import streamlit as st
    
    st.title('Conoce a nuestro equipo de Ingeniería Ambiental')
    
    st.video("VIDEO10.mp4")
    
    st.header('Comentarios y Retroalimentación')
    comentario = st.text_area('Escribe aquí tu comentario o retroalimentación:', height=150)
    if st.button('Enviar comentario'):
        st.success('¡Comentario enviado correctamente!')







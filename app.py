import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# =============================================================================
# CONFIGURACIÓN DE LA PÁGINA
# =============================================================================
st.set_page_config(
    page_title="Jóvenes NINI - Pasto Cabecera",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# DATOS (resultados del análisis)
# =============================================================================
anios = ['2020', '2021', '2022', '2023', '2024']
prev_anio = [41.0, 46.7, 31.6, 32.0, 31.5]

grupos = ['14-17', '18-21', '22-24', '25-28']
prev_edad = [10.6, 29.0, 39.4, 56.2]

niveles = ['Ninguno', 'Primaria', 'Media', 'Técnica', 'Superior']
prev_ed = [100.0, 72.7, 20.2, 57.0, 23.4]

# Efectos marginales (puntos porcentuales)
variables_efectos = ['Educación baja', 'Educación alta', 'Ser mujer', 'Edad (+1 año)', 'Año 2021']
efectos = [37.5, -2.0, 4.0, 3.6, 12.7]

# Paleta de colores
colores = {
    'coral': '#FFB5A7',
    'rosa': '#F7CAC9',
    'menta': '#B5EAD7',
    'celeste': '#BDE0FE',
    'amarillo': '#FFE5B4',
    'lila': '#E2D1F9',
    'durazno': '#FFDAB9'
}

# =============================================================================
# SIDEBAR
# =============================================================================
with st.sidebar:
    st.title("📊 NINI Pasto")
    st.markdown("""
    **Análisis de jóvenes NINI**  
    (Ni estudian Ni trabajan)  
    Pasto Cabecera • 2020-2024
    """)
    st.divider()
    st.markdown("**Fuente:** GEIH (DANE)  
**Ponderación:** Factor de expansión FEX_C")
    st.divider()
    st.caption("App creada para visualizar los resultados del análisis.")

# =============================================================================
# TÍTULO PRINCIPAL
# =============================================================================
st.title("Jóvenes NINI en Pasto Cabecera (2020-2024)")
st.markdown("""
Análisis de la prevalencia de jóvenes que **Ni estudian Ni trabajan** (NINI) entre 14 y 28 años  
en el área urbana de Pasto, utilizando los microdatos de la **Gran Encuesta Integrada de Hogares (GEIH)**.
""")

# =============================================================================
# MÉTRICAS PRINCIPALES
# =============================================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Prevalencia total", "34.8%", "ponderada")
with col2:
    st.metric("Pico (2021)", "46.7%", "+5.7 pp vs 2020")
with col3:
    st.metric("Mujeres", "42.9%", "+9.7 pp vs hombres")
with col4:
    st.metric("Grupo 25-28", "56.2%", "más alto")

st.divider()

# =============================================================================
# TABS
# =============================================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Por Año", 
    "👥 Por Edad", 
    "🎓 Por Educación", 
    "⚖️ Por Sexo", 
    "📉 Efectos Marginales"
])

# -----------------------------------------------------------------------------
# TAB 1: POR AÑO
# -----------------------------------------------------------------------------
with tab1:
    st.subheader("Prevalencia de Jóvenes NINI por Año")
    
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=anios, y=prev_anio,
        text=[f'<b>{v:.1f}%</b>' for v in prev_anio],
        textposition='outside',
        textfont=dict(size=14, color='#2C3E50'),
        marker=dict(
            color=[colores['coral'], colores['rosa'], colores['menta'], 
                   colores['celeste'], colores['amarillo']],
            line=dict(color='white', width=2)
        ),
        hovertemplate='<b>Año %{x}</b><br>Prevalencia: %{y:.1f}%<extra></extra>'
    ))
    fig1.update_layout(
        xaxis_title='Año',
        yaxis_title='Prevalencia (%)',
        yaxis=dict(range=[0, 60], gridcolor='#F0F0F0'),
        font=dict(family="Arial", size=14, color="#4A4A4A"),
        plot_bgcolor='#FAFAFA',
        paper_bgcolor='white',
        height=450,
        margin=dict(t=40)
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    st.info("**Hallazgo:** La prevalencia alcanzó su máximo en 2021 (46.7%), coincidiendo con el período más fuerte de la pandemia, y se estabilizó alrededor del 31-32% a partir de 2022.")

# -----------------------------------------------------------------------------
# TAB 2: POR EDAD
# -----------------------------------------------------------------------------
with tab2:
    st.subheader("Prevalencia NINI por Grupo de Edad")
    
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        y=grupos, x=prev_edad, orientation='h',
        text=[f'<b>{v:.1f}%</b>' for v in prev_edad],
        textposition='outside',
        textfont=dict(size=14, color='#2C3E50'),
        marker=dict(
            color=[colores['celeste'], colores['menta'], colores['amarillo'], colores['coral']],
            line=dict(color='white', width=2)
        ),
        hovertemplate='<b>%{y} años</b><br>Prevalencia: %{x:.1f}%<extra></extra>'
    ))
    fig2.update_layout(
        xaxis_title='Prevalencia (%)',
        yaxis_title='Grupo de Edad',
        xaxis=dict(range=[0, 70], gridcolor='#F0F0F0'),
        font=dict(family="Arial", size=14, color="#4A4A4A"),
        plot_bgcolor='#FAFAFA',
        paper_bgcolor='white',
        height=400,
        margin=dict(t=40, r=80)
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    st.info("**Hallazgo:** Existe un gradiente claro por edad. La prevalencia pasa de 10.6% en el grupo de 14-17 años a 56.2% en el grupo de 25-28 años.")

# -----------------------------------------------------------------------------
# TAB 3: POR EDUCACIÓN
# -----------------------------------------------------------------------------
with tab3:
    st.subheader("Prevalencia NINI por Nivel Educativo")
    
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(
        x=niveles, y=prev_ed,
        text=[f'<b>{v:.1f}%</b>' for v in prev_ed],
        textposition='outside',
        textfont=dict(size=13, color='#2C3E50'),
        marker=dict(
            color=[colores['coral'], colores['rosa'], colores['menta'], 
                   colores['amarillo'], colores['celeste']],
            line=dict(color='white', width=2)
        ),
        hovertemplate='<b>%{x}</b><br>Prevalencia: %{y:.1f}%<extra></extra>'
    ))
    fig3.update_layout(
        xaxis_title='Nivel Educativo',
        yaxis_title='Prevalencia (%)',
        yaxis=dict(range=[0, 115], gridcolor='#F0F0F0'),
        font=dict(family="Arial", size=14, color="#4A4A4A"),
        plot_bgcolor='#FAFAFA',
        paper_bgcolor='white',
        height=450,
        margin=dict(t=40)
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    st.info("**Hallazgo:** La educación media presenta la menor prevalencia (20.2%). Los niveles más bajos (ninguno y primaria) muestran prevalencias muy altas.")

# -----------------------------------------------------------------------------
# TAB 4: POR SEXO
# -----------------------------------------------------------------------------
with tab4:
    st.subheader("Prevalencia NINI por Sexo")
    
    fig4 = go.Figure()
    fig4.add_trace(go.Pie(
        labels=['Hombres', 'Mujeres'],
        values=[33.2, 42.9],
        hole=0.55,
        marker=dict(
            colors=[colores['celeste'], colores['rosa']],
            line=dict(color='white', width=3)
        ),
        textinfo='label+percent',
        textfont=dict(size=15, color='#2C3E50'),
        hovertemplate='<b>%{label}</b><br>Prevalencia: %{value:.1f}%<extra></extra>',
        pull=[0, 0.05]
    ))
    fig4.update_layout(
        font=dict(family="Arial", size=14, color="#4A4A4A"),
        paper_bgcolor='white',
        height=420,
        annotations=[dict(
            text='<b>34.8%</b><br>promedio',
            x=0.5, y=0.5,
            font=dict(size=18, color='#2C3E50'),
            showarrow=False
        )]
    )
    st.plotly_chart(fig4, use_container_width=True)
    
    st.info("**Hallazgo:** Las mujeres tienen una prevalencia significativamente más alta (42.9%) que los hombres (33.2%).")

# -----------------------------------------------------------------------------
# TAB 5: EFECTOS MARGINALES
# -----------------------------------------------------------------------------
with tab5:
    st.subheader("Efectos sobre la Probabilidad de ser NINI")
    st.caption("Resultados del modelo logit con pesos (efectos marginales promedio)")
    
    fig5 = go.Figure()
    fig5.add_trace(go.Bar(
        y=variables_efectos[::-1],
        x=efectos[::-1],
        orientation='h',
        marker=dict(
            color=[colores['coral'] if e > 0 else colores['menta'] for e in efectos[::-1]],
            line=dict(color='white', width=2)
        ),
        text=[f'<b>{e:+.1f} pp</b>' for e in efectos[::-1]],
        textposition='outside',
        textfont=dict(size=13, color='#2C3E50'),
        hovertemplate='<b>%{y}</b><br>Efecto: %{x:+.1f} puntos porcentuales<extra></extra>'
    ))
    fig5.add_vline(x=0, line_color='#BDC3C7', line_width=2)
    fig5.update_layout(
        xaxis_title='Cambio en probabilidad (puntos porcentuales)',
        xaxis=dict(range=[-10, 50], gridcolor='#F0F0F0'),
        font=dict(family="Arial", size=14, color="#4A4A4A"),
        plot_bgcolor='#FAFAFA',
        paper_bgcolor='white',
        height=420,
        margin=dict(t=40, r=80)
    )
    st.plotly_chart(fig5, use_container_width=True)
    
    st.warning("""
    **Interpretación (con precaución):**  
    - Tener educación baja aumenta la probabilidad de ser NINI en **+37.5 pp**.  
    - Ser mujer aumenta la probabilidad en **+4.0 pp**.  
    - Cada año adicional de edad aumenta la probabilidad en **+3.6 pp**.  
    - El año 2021 aumentó la probabilidad en **+12.7 pp** (respecto a 2020).
    
    *Nota: El modelo utiliza un método aproximado de ponderación. Los resultados deben interpretarse con cautela.*
    """)

# =============================================================================
# DASHBOARD RESUMEN
# =============================================================================
st.divider()
st.subheader("Resumen General")

fig_dash = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Por Año', 'Por Edad', 'Por Educación', 'Por Sexo'),
    specs=[[{'type': 'bar'}, {'type': 'bar'}],
           [{'type': 'bar'}, {'type': 'pie'}]],
    vertical_spacing=0.12,
    horizontal_spacing=0.08
)

fig_dash.add_trace(go.Bar(x=anios, y=prev_anio, marker_color=colores['celeste'], showlegend=False), row=1, col=1)
fig_dash.add_trace(go.Bar(x=grupos, y=prev_edad, marker_color=colores['coral'], showlegend=False), row=1, col=2)
fig_dash.add_trace(go.Bar(x=niveles, y=prev_ed, marker_color=colores['menta'], showlegend=False), row=2, col=1)
fig_dash.add_trace(go.Pie(
    labels=['Hombres', 'Mujeres'],
    values=[33.2, 42.9],
    marker_colors=[colores['celeste'], colores['rosa']],
    textinfo='label+percent'
), row=2, col=2)

fig_dash.update_layout(
    title=dict(text='<b>Jóvenes NINI en Pasto Cabecera (2020-2024)</b>', font=dict(size=20)),
    font=dict(family="Arial", size=12),
    paper_bgcolor='white',
    plot_bgcolor='#FAFAFA',
    height=650,
    showlegend=False
)
fig_dash.update_annotations(font=dict(size=13, color='#2C3E50'))

st.plotly_chart(fig_dash, use_container_width=True)

# =============================================================================
# METODOLOGÍA
# =============================================================================
with st.expander("📋 Metodología y notas"):
    st.markdown("""
    **Definición de NINI:**  
    Jóvenes de 14 a 28 años que no estaban estudiando (`P6170 ≠ 1`) y no aparecían en el archivo de ocupados.
    
    **Población:**  
    Área urbana (cabecera) de Pasto (`AREA = 52` y `CLASE = 1`).
    
    **Ponderación:**  
    Todas las prevalencias están ponderadas con el factor de expansión (`FEX_C` o `FEX_C18`).
    
    **Modelo:**  
    Logit con efectos marginales promedio. Se utilizó un método de remuestreo ponderado como aproximación a los pesos de encuesta.
    
    **Datos:**  
    Microdatos de la Gran Encuesta Integrada de Hogares (GEIH) del DANE, años 2020-2024.
    """)

st.caption("App desarrollada para visualizar el análisis de jóvenes NINI en Pasto Cabecera.")

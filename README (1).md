# Jóvenes NINI - Pasto Cabecera (2020-2024)

App de Streamlit para visualizar el análisis de jóvenes que Ni estudian Ni trabajan (NINI) en el área urbana de Pasto, utilizando microdatos de la GEIH (DANE).

## Características

- Prevalencia ponderada por año, grupo de edad, nivel educativo y sexo
- Efectos marginales del modelo logit
- Gráficos interactivos con Plotly
- Interfaz limpia y profesional

## Cómo ejecutar localmente

1. Clona el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   cd TU_REPOSITORIO
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la app:
   ```bash
   streamlit run app.py
   ```

## Desplegar en Streamlit Community Cloud

1. Sube este repositorio a GitHub.
2. Ve a [share.streamlit.io](https://share.streamlit.io).
3. Conecta tu cuenta de GitHub.
4. Selecciona el repositorio y el archivo `app.py`.
5. La app se desplegará automáticamente.

## Estructura del proyecto

```
├── app.py              # Aplicación principal de Streamlit
├── requirements.txt    # Dependencias
└── README.md           # Este archivo
```

## Notas

- Los resultados están basados en el análisis de los microdatos de la GEIH 2020-2024.
- Las prevalencias están ponderadas con el factor de expansión.
- El modelo logit utiliza un método aproximado de ponderación.

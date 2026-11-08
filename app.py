import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="b-nice design - Dashboard",
    page_icon="📊",
    layout="wide",
)

# Estilos CSS personalizados para replicar la estética exacta
st.markdown(
    """
    <style>
    /* Fondo general de la aplicación */
    .stApp {
        background-color: #F4F6F8;
    }
    
    /* Navbar simulado superior */
    .navbar-container {
        background-color: #FFFFFF;
        padding: 12px 24px;
        border-radius: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        margin-bottom: 24px;
    }
    .navbar-links {
        display: flex;
        gap: 24px;
        font-weight: 500;
        color: #4A5568;
        font-size: 15px;
    }
    .navbar-link-active {
        color: #0066FF;
        font-weight: 600;
        border-bottom: 2px solid #0066FF;
        padding-bottom: 2px;
    }
    .navbar-user {
        font-weight: 600;
        color: #2D3748;
    }

    /* Tarjetas blancas con esquinas redondeadas y sombras sutiles */
    .card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .card-title {
        font-size: 13px;
        font-weight: 600;
        color: #718096;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 8px;
    }
    
    .card-amount {
        font-size: 26px;
        font-weight: 700;
        color: #1A202C;
        margin-bottom: 12px;
    }
    
    .card-link {
        font-size: 13px;
        color: #0066FF;
        text-decoration: none;
        font-weight: 500;
        margin-top: 12px;
        display: inline-block;
    }
    .card-link:hover {
        text-decoration: underline;
    }

    /* Botón circular azul brillante */
    .btn-circle {
        background-color: #0066FF;
        color: white;
        width: 42px;
        height: 42px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0, 102, 255, 0.3);
        cursor: pointer;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 1. MENÚ SUPERIOR (NAVBAR SIMULADO)
# ==========================================
st.markdown(
    """
    <div class="navbar-container">
        <div class="navbar-links">
            <span class="navbar-link-active">Inicio</span>
            <span>Facturas</span>
            <span>Presupuestos</span>
            <span>Compras</span>
            <span>Impuestos</span>
            <span>Más</span>
        </div>
        <div class="navbar-user">
            👤 Beatriz Antolín
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 2. CABECERA DE BIENVENIDA
# ==========================================
col_head_1, col_head_2, col_head_3 = st.columns([3, 1.5, 0.4])

with col_head_1:
    st.markdown(
        "<h1 style='color: #1A202C; font-size: 26px; font-weight: 700; margin: 0;'>Hola Beatriz</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: #718096; font-size: 13px; margin: 2px 0 0 0;'>b-nice design (NIF: 52988830G)</p>",
        unsafe_allow_html=True,
    )

with col_head_2:
    periodo = st.selectbox(
        "Período",
        ["Todo el año 2026", "1T", "2T", "3T", "4T"],
        label_visibility="collapsed",
    )

with col_head_3:
    st.markdown(
        """
        <div style="display: flex; align-items: center; justify-content: center; height: 100%;">
            <button class="btn-circle">+</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("") # Separador visual

# ==========================================
# 3. FILA PRINCIPAL DE TARJETAS (WIDGETS)
# ==========================================
col1, col2, col3, col4 = st.columns(4)

# Tarjeta 1: Facturas
with col1:
    st.markdown(
        """
        <div class="card">
            <div>
                <div class="card-title">Facturas</div>
                <div class="card-amount">6.174 €</div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    # Mini gráfico de barras verticales (turquesa)
    chart_data_1 = pd.DataFrame({"Valores": [25, 40, 30, 55, 75, 65]})
    st.bar_chart(chart_data_1, height=55, use_container_width=True, color="#2DD4BF")
    st.markdown(
        """
            <a href="#" class="card-link">Ir a facturas &rarr;</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Tarjeta 2: Compras
with col2:
    st.markdown(
        """
        <div class="card">
            <div>
                <div class="card-title">Compras</div>
                <div class="card-amount">11.524 €</div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    # Mini gráfico de barras verticales (azul brillante)
    chart_data_2 = pd.DataFrame({"Valores": [45, 35, 60, 40, 85, 70]})
    st.bar_chart(chart_data_2, height=55, use_container_width=True, color="#0066FF")
    st.markdown(
        """
            <a href="#" class="card-link">Ir a compras &rarr;</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Tarjeta 3: Ingresos por cliente
with col3:
    st.markdown(
        """
        <div class="card">
            <div>
                <div class="card-title">Ingresos por cliente</div>
                <div class="card-amount" style="font-size: 22px; margin-bottom: 6px;">8.792 €</div>
                <div style="font-size: 12px; color: #718096; margin-bottom: 6px;">Clientes principales:</div>
                <div style="font-size: 11px; color: #2D3748; line-height: 1.3;">
                    <b>TIREA Tecnologías de la Información, SA</b><br>
                    <span style="color: #0066FF; font-weight: 600;">5.300 €</span>
                </div>
            </div>
            <a href="#" class="card-link" style="margin-top: 6px;">Ver todos &rarr;</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Tarjeta 4: Bancos
with col4:
    st.markdown(
        """
        <div class="card">
            <div>
                <div class="card-title">Bancos</div>
                <div class="card-amount" style="font-size: 22px; margin-bottom: 6px; color: #DD6B20;">-11.517 €</div>
                <div style="font-size: 12px; color: #718096; margin-bottom: 6px;">Desglose de cuentas:</div>
                <div style="font-size: 11px; color: #2D3748; line-height: 1.4;">
                    <b>BBVA:</b> 169 €<br>
                    <b>Personal:</b> -11.686 €
                </div>
            </div>
            <a href="#" class="card-link" style="margin-top: 6px;">Gestionar bancos &rarr;</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")

# ==========================================
# 4. FILA SECUNDARIA (ESTADOS DE COBRO)
# ==========================================
col_sub1, col_sub2 = st.columns(2)

with col_sub1:
    st.markdown(
        """
        <div class="card" style="padding: 16px 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span class="card-title" style="margin: 0;">Cobrado (últimos 60 días)</span>
                <span style="font-size: 18px; font-weight: 700; color: #1A202C;">286 €</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(0.40)

with col_sub2:
    st.markdown(
        """
        <div class="card" style="padding: 16px 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span class="card-title" style="margin: 0;">Pagado (últimos 60 días)</span>
                <span style="font-size: 18px; font-weight: 700; color: #1A202C;">61 €</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(0.20)

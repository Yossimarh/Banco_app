import streamlit as st
from backend import Cliente

# 1. configuracion de la pagina
st.set_page_config(page_title="Banco Virtual", page_icon="🏦")
st.title("🏦 Banco Virtual")
st.header("Gestión de Clientes")

# 2. ✅ Inicializa sesión para cliente para almacenar el cliente
if 'cliente' not in st.session_state:
    st.session_state['cliente'] = None

# 3.  Formulario de creacion de cuenta
with st.form("clientes_form"):
    nombre = st.text_input("Nombre")
    apellido = st.text_input("Apellido")
    numero_cuenta = st.text_input("Número de cuenta")
    balance_inical = st.number_input("Balance Inicial", min_value=0.0, format="%.2f", step=10.0)
    crear = st.form_submit_button("Crear Cuenta")

# 4. Al enviar el formulario, guardamos el cliente en session_state
if crear:
    st.session_state["cliente"] = Cliente(nombre, apellido, numero_cuenta, balance_inical)
    st.success(f"Cuenta creada para {nombre} {apellido}")

    # Limpiar formulario reiniciando la app (se volverá a cargar)
    


# 5. Si ya hay un cliente en sesión, mostramos las operaciones
cliente = st.session_state['cliente']
if cliente:
    st.markdown("---")
    st.subheader(f"👋 Hola, {cliente.nombre} {cliente.apellido}")
    st.text(f"💳 Cuenta: {cliente.numero_cuenta}")
    st.text(f"💰 Saldo actual: ${cliente.consultar_saldo():.2f}")

    st.markdown("### 🔄 Operaciones Bancarias")
    col1, col2, col3, col4 = st.columns(4)

    # Botón Consultar Saldo
col1, col2, col3,col_input,col_boton = st.columns([4, 3, 4, 3,4])
with col1:
    if st.button("Consultar Saldo"):
        saldo = st.session_state.cliente.consultar_saldo()
        st.info(f"Tu saldo actual es: ${saldo:,.2f}")

   # Boton Depositar
with col2:
    cantidad_deposito = st.number_input(
        "Cantidad",
        min_value=0.0,
        step=10.0,
        format="%.2f",
        label_visibility="collapsed"
    )

with col3:
    if st.button("Depositar"):
        ok, msg = st.session_state.cliente.depositar(cantidad_deposito)
        if ok:
            st.success(msg)
        else:
            st.error(msg)

    # Boton de Retirar.

# Solo mostrar si hay un cliente logueado
if "cliente" in st.session_state and st.session_state.cliente is not None:
    saldo_actual = st.session_state.cliente.consultar_saldo()

    # Crear dos columnas en una misma fila: una para el input, otra para el botón
    #col_input, col_boton = st.columns([1, 1])  # Puedes ajustar los anchos relativos

    with col_input:
        monto_ret = st.number_input(
            "Cantidad",
            min_value=0.0,
            step=10.0,
            format="%.2f",
            key="ret",
            label_visibility="collapsed"
        )

    with col_boton:
        # Habilitar o deshabilitar el botón según el valor ingresado
        if monto_ret > saldo_actual:
            st.warning("⚠️ El monto excede tu saldo disponible.")
            retirar_btn = st.button("Retirar", disabled=True)
        elif monto_ret <=0:
            st.info("Ingresa un monto mayor a cero para retirar.")
            retirar_btn = st.button("Retirar", disabled=True)
        else:
            retirar_btn = st.button("Retirar")

    if retirar_btn:
        ok, msg = st.session_state.cliente.retirar(monto_ret)
        if ok:
            st.success(msg)
        else:
            st.error(msg)
else:
    st.error("Debes iniciar sesión para realizar operaciones.")








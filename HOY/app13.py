import streamlit as st
from supabase import create_client, Client
import os


#configurar
SUPABASE_URL =  "https://pipplgjnsnycifhnrahr.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBpcHBsZ2puc255Y2lmaG5yYWhyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE3NDU3MTcsImV4cCI6MjA1NzMyMTcxN30.wwUhzhNA8bMknz3rM7pcA0tCUlCz7H663UsZzmlYvhw"
supabase : Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("gestion de clienes CRUD con supabase y streamlitE")

st.header("agregar cliente")
nombre = st.text_input("Nombre")
email = st.text_input("Email")
telefono= st.text_input("Teléfono")

if st.button("agregar cliente"):
    if nombre and email:
        data = {"nombre" : nombre, "email" : email, "telefono" : telefono}
        response = supabase.table("clientes").insert(data).execute()
        st.success("Cliente agregado correctamente ")
    else:
        st.warning("Nombre e email son obligatorios")    

st.header("Clientes registrados")
clientes = supabase.table("clientes").select("*").execute()
if clientes.data:
    for cliente in clientes.data:
        st.subheader(cliente["nombre"])
        st.write(cliente ["email"])
        st.write(cliente ["telefono"])
        st.write(f"Fecha de registro: {cliente['fecha_registro']}")


        if st.button(f"Eliminar {cliente['nombre']}", key=cliente["id"]):
            supabase.table("clientes").delete().eq("id", cliente["id"]).execute()
            st.success(f"{cliente['nombre']} eliminado correctamente")
            st.experimental_rerun()
#de otra forma:
else:
    st.info("no hay clientes registrados aún")
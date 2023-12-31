import streamlit as st
import pandas as pd
from views import View
import time

class AbrirContaUI:
  def main():
    st.header("Abrir Conta no Sistema")
    AbrirContaUI.inserir()
  
  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha", type="password")
    senha1 = st.text_input("Confirme a senha", type="password")
    if st.button("Inserir"):
      try:
        if senha != senha1:
          st.error("Os campos de senha não correspondem")
        else:
          View.cliente_inserir(nome, email, fone, senha)
          st.success("Conta criada com sucesso")
          time.sleep(0.5)
          st.rerun()
      except ValueError as error:
            st.write(f"Erro: {error}")
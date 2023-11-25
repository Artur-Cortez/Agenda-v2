from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manteragendaUI import ManterAgendaUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.loginUI import LoginUI
from templates.meusagendamentosUI import MeusAgendamentosUI
from templates.servicoreajusteUI import ServicoReajusteUI
from templates.abrircontaUI import AbrirContaUI
from templates.editarperfilUI import EditarPerfilUI
from templates.confirmarhorarioUI import ConfirmarHorarioUI
from templates.agendarhorarioUI import AgendarHorarioUI
from templates.agendahojeUI import AgendaHojeUI

from views import View

import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
    if op == "Login": LoginUI.main()
    if op == "Abrir Conta": AbrirContaUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Agenda", "Manter Clientes", "Manter Serviços", "Abrir Agenda do Dia", "Reajustar Preço", "Editar perfil", "Confirmar horário"])
    if op == "Manter Agenda": ManterAgendaUI.main()
    if op == "Manter Clientes": ManterClienteUI.main()
    if op == "Manter Serviços": ManterServicoUI.main()
    if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
    if op == "Reajustar Preço": ServicoReajusteUI.main()
    if op == "Editar perfil": EditarPerfilUI.main()
    if op == "Confirmar horário": ConfirmarHorarioUI.main()

  def menu_cliente():
    op = st.sidebar.selectbox("Menu", ["Agenda de hoje", "Meus agendamentos", "Editar perfil", "Agendar um horário"])
    if op == "Meus agendamentos" : MeusAgendamentosUI.main()
    if op == "Editar perfil": EditarPerfilUI.main()
    if op == "Agenda de hoje": AgendaHojeUI.main()
    if op == "Agendar um horário": AgendarHorarioUI.main()

  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["cliente_id"]
      del st.session_state["cliente_nome"]
      del st.session_state["cliente_email"]
      del st.session_state["cliente_fone"]
      del st.session_state["cliente_senha"]
      st.rerun()

  def sidebar():
    if "cliente_id" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
      if st.session_state["cliente_nome"] == "admin":
        IndexUI.menu_admin()
      else: IndexUI.menu_cliente()
      IndexUI.btn_logout()  

  def main():
    View.cliente_admin()
    IndexUI.sidebar()

IndexUI.main()




import streamlit as st
import pandas as pd
from views import View
import datetime, time


class MeusAgendamentosUI:
  def main():
    MeusAgendamentosUI.listar()

  def listar():
    st.header("Meus agendamentos")
    var1 = st.date_input("Insira/selecione data inicial", datetime.date.today(), format="DD/MM/YYYY")
    var2 = st.date_input("Insira/selecione data final", (datetime.date.today() + datetime.timedelta(days=7)), format="DD/MM/YYYY")

    if st.button("Visualizar"):
      agendas = View.periodo_informado(var1, var2, st.session_state["cliente_id"])
      if len(agendas) == 0:
        st.write("Nenhum horário cadastrado no sistema")
      else:
        dic1 = []
        for obj in agendas:
          data = obj.get_data().date()
          hora = obj.get_data().time().strftime("%H:%M")
          servico = (View.servico_listar_id(obj.get_id_servico())).get_descricao()
          confirmacao = obj.get_confirmado()
          if confirmacao: conf = "Confirmado"
          else: conf = "A confirmar"
          dic1.append([data, hora, servico, conf])
        if dic1 == []:
          st.write("dic1 vazio")
        else:
          df1 = pd.DataFrame(dic1, columns=["Data", "Hora", "Desc. do serviço", "Confirmação"])
          st.dataframe(df1, hide_index=True)
      
    
  
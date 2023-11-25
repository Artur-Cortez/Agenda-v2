import streamlit as st
import pandas as pd
from views import View

class MeusAgendamentosUI:
  def main():
    MeusAgendamentosUI.listar()

  def listar():
    st.header("Meus agendamentos")
    datainicial = st.text_input("Informe a data inicial no formato *dd/mm/aaaa*")
    datafinal = st.text_input("Informe a data final no formato *dd/mm/aaaa*")

    if datainicial != '' and datafinal != '':
      agendas = View.periodo_informado(datainicial, datafinal, st.session_state["cliente_id"])

    if st.button("Visualizar"):

      if len(agendas) == 0:
        st.write("Nenhum horário cadastrado no sistema")
      else:
        dic1 = []
        for obj in agendas:
          data = obj.get_data().strftime('%d/%m/%Y')
          hora = obj.get_data().strftime('%H:%M')
          servico = (View.servico_listar_id(obj.get_id_servico())).get_descricao()
          confirmacao = obj.get_confirmado()
          if confirmacao: conf = "Confirmado"
          else: conf = "A confirmar"
        
          dic1.append([data, hora, servico, conf])
        df1 = pd.DataFrame(dic1, columns=["Data", "Hora", "Desc. do serviço", "Confirmação"])
        st.dataframe(df1, hide_index=True)
      
    
  
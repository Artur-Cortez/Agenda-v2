import streamlit as st
import pandas as pd
from views import View
import time

class AgendarHorarioUI:
    def main():
        st.header("Horários da semana")
        AgendarHorarioUI.listar_semana()
        AgendarHorarioUI.marcar()

    def listar_semana():
        View.auto_excluir()
        agendas = View.agenda_listarsemana()
        if len(agendas) == 0:
            st.write("Nenhum horário cadastrado no sistema")
        else:
            dic1 = []
            for obj in agendas:
                data = obj.get_data().strftime('%d/%m/%Y')
                hora = obj.get_data().strftime('%H:%M')
                id_servico = obj.get_id_servico()
                if id_servico is not None:
                    servico_obj = View.servico_listar_id(id_servico)
                    if servico_obj is not None:
                        servico = servico_obj.get_descricao()
                    else:                        
                        servico = "Vazio"
                else:                   
                    servico = "ID do serviço é nulo"
                
                dic1.append([data, hora, servico])
                
            df1 = pd.DataFrame(dic1, columns=["Data", "Hora", "Desc. do serviço"])
            st.dataframe(df1, hide_index=True)

    def marcar():    
        st.header("Reserve um horário para algo")
        horarios = View.agenda_listarsemana()
        opcao = st.selectbox("Selecione o horário", horarios, format_func= lambda x: f"{x.get_data().strftime('%d/%m/%Y')} - {View.semana[x.get_data().weekday()]} - {x.get_data().strftime('%H:%M')} ") 
        servicos = View.servico_listar()
        servico = st.selectbox("Selecione o serviço", servicos, format_func= lambda x: f"{x.get_descricao()} - R$ {x.get_valor():.2f} - {x.get_duracao()} min")
        if st.button("Inserir"):
            try:
                View.agenda_atualizar(opcao.get_id(), opcao.get_data(), False, st.session_state["cliente_id"], servico.get_id())
                st.success("Horário marcado com sucesso. Aguarde confirmação")
                time.sleep(0.5)
                st.rerun()
            except ValueError as error:
                st.error(f"Erro: {error}")  
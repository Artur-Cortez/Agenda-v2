import streamlit as st
from views import View
from time import sleep

class ConfirmarHorarioUI:
    def main():
        st.header("Confirmar horário marcado por um cliente")
        ConfirmarHorarioUI.confirmar()
    def confirmar():
        lista = []
        for i in View.agenda_listar():
            if i.get_id_cliente() != 0 and i.get_id_servico() != 0 and i.get_confirmado() == False:
                lista.append(i)
        horario = st.selectbox("escolha um horário pra confirmar", lista, format_func= lambda x: f"{x.get_data().strftime('%d/%m/%Y')} - {View.semana[x.get_data().weekday()]} - {x.get_data().strftime('%H:%M')} - {View.cliente_listar_id(x.get_id_cliente()).get_nome()} - {View.servico_listar_id(x.get_id_servico()).get_descricao()}")
        # Opção x: "21/02/2023 - Terça-feira - 12:00 - nome do cliente - Corte de cabelo e pinto"
        if st.button("Confirmar"):
            View.agenda_atualizar(horario.get_id(), horario.get_data(), True, horario.get_id_cliente(), horario.get_id_servico())
            st.success("Horário confirmado com sucesso!")
            sleep(0.5)
            st.rerun()


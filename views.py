from models.cliente import Cliente, NCliente
from models.servico import Servico, NServico
from models.agenda import Agenda, NAgenda
import datetime
import streamlit as st

class View:
  semana = {
      0: "Segunda-feira",
      1: "Terça-feira",
      2: "Quarta-feira",
      3: "Quinta-feira",
      4: "Sexta-feria",
      5: "Sábado",
      6: "Domingo"
    }
  def cliente_inserir(nome, email, fone, senha):
    if nome == '' or email == '' or fone == '' or senha == '': 
      raise ValueError("Campo(s) obrigatório(s) vazio(s)")
    
    for i in View.cliente_listar():
      if i.get_email() == email:
        raise ValueError("Email já cadastrado")
    cliente = Cliente(0, nome, email, fone, senha)    
    NCliente.inserir(cliente)
  

  def cliente_listar():
    return NCliente.listar()
  
  def cliente_listar_id(id):
    return NCliente.listar_id(id)

  def cliente_atualizar(id, nome, email, fone, senha):
    if nome == '' or email == '' or fone == '' or senha == '': 
      raise ValueError("Campo(s) obrigatório(s) vazio(s)")
    cliente = Cliente(id, nome, email, fone, senha)
    NCliente.atualizar(cliente)
    
  def cliente_excluir(id):
    cliente = Cliente(id, "", "", "", "")
    NCliente.excluir(cliente)    

  def cliente_admin():
    for cliente in View.cliente_listar():
      if cliente.get_nome() == "admin": return
    View.cliente_inserir("admin", "admin", "0000", "admin")  

  #Avaliação
  #def cliente_login(email, senha):
  #  for cliente in View.cliente_listar():
  #    if cliente.get_email() == email and cliente.get_senha() == senha:
  #      return True
  #  return False

  def cliente_login(email, senha):
    for cliente in View.cliente_listar():
      if cliente.get_email() == email and cliente.get_senha() == senha:
        return cliente
    return None

  def servico_listar():
    return NServico.listar()

  def servico_listar_id(id):
    return NServico.listar_id(id)

  def servico_inserir(descricao, valor, duracao):
    if valor < 0: raise ValueError("Valor inválido")
    if duracao <= 0: raise ValueError("Duração inválida")
    NServico.inserir(Servico(0, descricao, valor, duracao))
    #rerun()

  def servico_atualizar(id, descricao, valor, duracao):
    if valor < 0: raise ValueError("Valor inválido")
    if duracao <= 0: raise ValueError("Duração inválida")
    NServico.atualizar(Servico(id, descricao, valor, duracao))

  def servico_excluir(id):
    NServico.excluir(Servico(id, "", 0, 10))

  def servico_reajustar(percentual):
    for servico in View.servico_listar():    
      NServico.atualizar(Servico(servico.get_id(), servico.get_descricao(), servico.get_valor() * (1 + percentual/100), servico.get_duracao()))


  def agenda_inserir(data, confirmado, id_cliente, id_servico):
    if data < datetime.datetime.now(): raise ValueError("Data inválida ou no passado")
    NAgenda.inserir(Agenda(0, data, confirmado, id_cliente, id_servico))

  def agenda_atualizar(id, data, confirmado, id_cliente, id_servico):
    if data < datetime.datetime.now(): raise ValueError("Data inválida ou no passado")
    NAgenda.atualizar(Agenda(id, data, confirmado, id_cliente, id_servico))

  def agenda_excluir(id):
    NAgenda.excluir(Agenda(id, "", "", 0, 0))

  def agenda_auto_excluir():
    horarios = View.agenda_listar()
    for h in horarios:
      if h.get_confirmado() == False and h.get_data() < datetime.datetime.now() and h.get_id_cliente == 0 and h.get_id_servico() == 0:
        View.agenda_excluir(h.get_id())

  def agenda_abrir_agenda(data, hinicio, hfim, intervalo):
    data_inicio = datetime.datetime.strptime(f"{data} {hinicio}", "%d/%m/%Y %H:%M")
    data_fim = datetime.datetime.strptime(f"{data} {hfim}", "%d/%m/%Y %H:%M")
    hoje = datetime.datetime.now()

    if data_inicio < hoje or data_fim < hoje:
      raise ValueError("Data inválida ou no passado")
    
    if data_fim < data_inicio:        
      raise ValueError("Hora início ou hora final inválidas")
    
    if intervalo <= 0: 
      raise ValueError("Intervalo nulo ou negativo")

    delta = datetime.timedelta(minutes = intervalo) 
    aux = data_inicio
    while aux <= data_fim :
      NAgenda.inserir(Agenda(0, aux, False, 0, 0))
      aux = aux + delta
  
  def agenda_listar():
    return NAgenda.listar()

  def agenda_listarsemana():
    r = []
    hoje = datetime.datetime.today()
    delta = datetime.timedelta(days=7)
    for horario in View.agenda_listar():
      if horario.get_confirmado() == False and horario.get_data().date() < hoje.date() + delta and horario.get_id_cliente() == 0 and horario.get_id_servico() == 0:
        r.append(horario)
    return r

  def periodo_informado(datainicial, datafinal, idcliente):
    datainicial = datetime.datetime.strptime(f"{datainicial}", "%d/%m/%Y")
    datafinal = datetime.datetime.strptime(f"{datafinal}", "%d/%m/%Y")
    
    periodo = []
    
    for horario in View.agenda_listar():
        if horario.get_id_cliente() == idcliente:
            if datainicial <= horario.get_data() <= datafinal:
                periodo.append(horario)
    
    return periodo
  
  def listar_naoconfirmados():
    nao_confirmados = []
    for agenda in View.agenda_listar():
      if agenda.get_confirmado() == False:
        nao_confirmados.append(agenda)
    
    return nao_confirmados

  def agenda_listarhoje():
    r = []
    hoje = datetime.datetime.today()
    for horario in View.agenda_listar():
      if horario.get_confirmado() == False and horario.get_data().date() == hoje.date() and horario.get_id_cliente() == 0 and horario.get_id_servico() == 0:
        r.append(horario)
    return r   

# Usuario escolhe a quantidade de mesas disponiveis no estabelecimento.
# Usuario informa o inicio e o fim do funcionamento. 
# 
# Menu apresenta as opções: 1) Adicionar ou remover mesas disponiveis. 2) Adicionar ou remover reservas de mesas. 3) Sair do programa.
# 1) Adiciona ou remove mesas disponiveis pra reservar.
# 2) Oferece a opção de reservar a mesa e o horario. Programa apresenta as mesas disponiveis e seus respectivos horarios.
from os import system

def start(): # Configuração inicial do programa
    global restaurante
    global horario_ini
    global horario_fim
    restaurante = []
    disp_mesas = int(input("Informe a quantidade de mesas disponiveis inicialmente: "))

    horario_ini = int(input("Informe o horario de inicio das reservas (24h): "))
    horario_fim = int(input("Informe o horario do encerramento (24h): "))

    for mesa in range(disp_mesas):
        restaurante.append({})
        restaurante[mesa]['mesa'] = mesa
        restaurante[mesa]['Reserva'] = {}
    
        for horario in range(horario_ini, horario_fim, 2):
            restaurante[mesa]['Reserva'][f'{horario}h'] = 'Disponivel'

def menu():
    quebralinha()
    print("------------- Menu de reserva -----------")
    print("-> 0 - Verificar mesas disponiveis ------")
    print("-> 1 - Adicionar mesa -------------------")
    print("-> 2 - Remover mesa ---------------------")
    print("-> 3 - Adicionar Reserva ----------------")
    print("-> 4 - Remover Reserva ------------------")
    print("-> 5 - Limpar tela ----------------------")
    print("-> 6 - Finalizar programa ---------------")
    print("-----------------------------------------")
    
def mostrar_mesas():
    for mesa in restaurante:
        print(f'\nMesa {mesa['mesa']}: ')
        
        for horario, reserva in mesa['Reserva'].items():
            print(f'{horario} -> {reserva}')
    quebralinha()

def ad_mesa():
    ad_mesa = input("Digite a quantidade de mesa que quer adicionar: ").strip()
    if ad_mesa.isnumeric():
        for mesa in range(len(restaurante), (len(restaurante) + int(ad_mesa))): #inicia a contagem a partir do numero da mesa mais alto.
            restaurante.append({})
            restaurante[-1]['mesa'] = mesa
            restaurante[-1]['Reserva'] = {}
            
            for horario in range(horario_ini, horario_fim, 2):
                restaurante[-1]['Reserva'][f'{horario}h'] = 'Disponivel'
    
    else:
        print("Não foi possivel adicionar as mesas!")

def rm_mesa():
    rm_mesa = input("Qual mesa deseja remover: ").strip()
    
    #continuar daqui
    if ad_mesa.isnumeric():
        pass
    
    else:
        print("Mesa incorreto!")
    
def ad_rm_reserva(op_menu): #Adicionar ou remover mesa
    #Organiza as variaveis de acordo com as opções do menu (3 - adicionar ou 4 - remover reservas)
    if op_menu == '3': 
        v1 = 'Disponivel'
        v2 = 'Reservado'
    
    elif op_menu == '4':
        v2 = 'Disponivel'
        v1 = 'Reservado'
        
    mesa = input("Qual mesa: ").strip()
    horario = input("Qual horario: ").strip()
    
    if mesa.isnumeric() and horario.isnumeric():
        try:
            if restaurante[int(mesa)]['Reserva'][f'{horario}h'] == v1:
                restaurante[int(mesa)]['Reserva'][f'{horario}h'] = v2
            
            elif restaurante[int(mesa)]['Reserva'][f'{horario}h'] == v2:
                quebralinha()
                print(f"Horario das {horario}h está {v2}.\n")
        except:
            print('Reserva não encontrada. Verifique a mesa/horario.')
    
    else:
        print("Mesa ou/ horario incorreto!")

def quebralinha():
    print()
    print("---------------------------------------")
    

def limparTela():
    system('cls')
    
def continuar():
    global isTrue
    quebralinha()
    continuar = input("Deseja continuar [s/n]: ").strip().lower()
    if continuar not in ['s', 'n']:
        print('Valor incorreto!')
        continuar = input("Deseja continuar [s/n]: ").strip().lower()
    if continuar == 'n':
        isTrue = False
    
restaurante = [{'mesa': 0, 'Reserva': {'14h': 'Disponivel', '16h': 'Disponivel', '18h': 'Disponivel', '20h': 'Disponivel'}},
               {'mesa': 1, 'Reserva': {'14h': 'Disponivel', '16h': 'Disponivel', '18h': 'Disponivel', '20h': 'Disponivel'}},
               {'mesa': 2, 'Reserva': {'14h': 'Reservado', '16h': 'Disponivel', '18h': 'Reservado', '20h': 'Disponivel'}}]

# start()
limparTela()
while True:
    menu()
    op_menu = input("Opção: ").strip()
    
    if op_menu == '6':
        break
    
    elif op_menu == '5':
        limparTela()
    
    elif op_menu == '0':
        mostrar_mesas()
    
    elif op_menu == '1':
        ad_mesa() 
    
    elif op_menu == '2':
        isTrue = True
        while isTrue:
            mostrar_mesas()
            #Fazer a func de remover mesa do restaurante se não ocupada.
            continuar()
    
    elif op_menu == '3':
        isTrue = True
        while isTrue:
            mostrar_mesas()
            ad_rm_reserva(op_menu)
            continuar()

    elif op_menu == '4':
        isTrue = True
        while isTrue:
            mostrar_mesas()
            ad_rm_reserva(op_menu)
            continuar()
            
    else:
        print("Valor inválido")
        
#Continuar -> Opçoes 2 e formatação
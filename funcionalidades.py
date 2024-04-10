from os import system

# Configuração para definir o escopo inicial de mesas
def start(): 
    global restaurante
    global horario_ini
    global horario_fim
    global hora_reserva
    restaurante = []
    disp_mesas = int(input("Informe a quantidade de mesas disponiveis inicialmente: "))

    horario_ini = int(input("Informe o horario de inicio das reservas (24h): "))
    horario_fim = int(input("Informe o horario do encerramento (24h): "))
    hora_reserva = int(input("Informe o perido de cada reserva (H): "))

    for mesa in range(disp_mesas):
        restaurante.append({})
        restaurante[mesa]['mesa'] = mesa
        restaurante[mesa]['Reserva'] = {}
        
        if horario_fim < horario_ini: 
            horario_fim += 24
        
        for horario in range(horario_ini, horario_fim, hora_reserva):
            if horario >= 24:
                restaurante[mesa]['Reserva'][f'{horario-24}h'] = 'Disponivel'
            else: 
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
    if len(restaurante) == 0:
        print("Não tem mesa.")
    else:
        for mesa in restaurante:
            print(f'\nMesa {mesa['mesa']}: ')
            
            for horario, reserva in mesa['Reserva'].items():
                print(f'{horario} -> {reserva}')
    quebralinha()

#Adicionar mesa
def ad_mesa():
    global horario_fim
    ad_mesa = input("Digite a quantidade de mesa que quer adicionar: ").strip()
    if ad_mesa.isnumeric():
        for mesa in range(len(restaurante), (len(restaurante) + int(ad_mesa))): #inicia a contagem a partir do numero da mesa mais alto.
            restaurante.append({})
            restaurante[-1]['mesa'] = mesa
            restaurante[-1]['Reserva'] = {}
            
            if horario_fim < horario_ini:
                horario_fim = horario_fim + 24
            
            for horario in range(horario_ini, horario_fim, hora_reserva):
                if horario >= 24:
                    restaurante[mesa]['Reserva'][f'{horario-24}h'] = 'Disponivel'
                else:
                    restaurante[-1]['Reserva'][f'{horario}h'] = 'Disponivel'
    
    else:
        print("Não foi possivel adicionar as mesas!")

#Remover mesa
def rm_mesa():
    rm_mesa = input("Quantas mesa deseja remover: ").strip()
    
    if rm_mesa.isnumeric():
        for mesa in range(int(rm_mesa)):
            restaurante.pop()
    
    else:
        print("Mesa incorreto!")

#Adicionar ou remover reservas 
def ad_rm_reserva(op_menu): 
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

def limparTela():
    system('cls')

# Opção de continuar no loop 
def continuar(): 
    global isTrue
    quebralinha()
    continuar = input("Deseja continuar [s/n]: ").strip().lower()
    if continuar not in ['s', 'n']:
        print('Valor incorreto!')
        continuar = input("Deseja continuar [s/n]: ").strip().lower()
    if continuar == 'n':
        isTrue = False
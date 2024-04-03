# Usuario escolhe a quantidade de mesas disponiveis no estabelecimento.
# Usuario informa o inicio e o fim do funcionamento. 
# 
# Menu apresenta as opções: 1) Adicionar ou remover mesas disponiveis. 2) Adicionar ou remover reservas de mesas. 3) Sair do programa.
# 1) Adiciona ou remove mesas disponiveis pra reservar.
# 2) Oferece a opção de reservar a mesa e o horario. Programa apresenta as mesas disponiveis e seus respectivos horarios.
from os import system

def menu():
    print("-------- Menu de reserva --------")
    print("-> 0 - Verificar mesas disponiveis")
    print("-> 1 - Adicionar ou remover mesas")
    print("-> 2 - Adicionar ou remover reservas")
    print("-> 3 - Limpar tela")
    print("-> 4 - Finalizar programa")
    print("---------------------------------")

def ver_mesas(op_menu):
    if op_menu == 0:
        print()
        for mesa in restaurante:
            print(f'\nMesa {mesa['mesa']}: ')
            for horario, reserva in mesa['Reserva'].items():
                print(f'{horario} -> {reserva}')
        print()
    
    if op_menu == 1:
        print()
        for mesa in restaurante:
            print(f'Mesa {mesa['mesa']}', end= '-> ')
            cont = 0
            for horario, reserva in mesa['Reserva'].items():
                if reserva == 'Reservado':
                    cont += 1
            if cont > 0:
                reservas = [h for h, r in enumerate(mesa['Reserva']) if r == 'Reservado']
                print(f"Reservas: {reservas}.")
            else:
                print("Mesa sem reserva.")
        print()
    
    if op_menu == 2:
        print()
        for mesa in restaurante:
            print(f'Mesa {mesa['mesa']}', end= ' -> ')
            cont = 0
            for horario, reserva in mesa['Reserva'].items():
                print(f'{horario} - {reserva}', end=' / ')
            print()
        print()              

restaurante = [{'mesa': 0, 'Reserva': {'14h': 'Disponivel', '16h': 'Disponivel', '18h': 'Disponivel', '20h': 'Disponivel'}},
               {'mesa': 1, 'Reserva': {'14h': 'Disponivel', '16h': 'Disponivel', '18h': 'Disponivel', '20h': 'Disponivel'}},
               {'mesa': 2, 'Reserva': {'14h': 'Reservado', '16h': 'Disponivel', '18h': 'Reservado', '20h': 'Disponivel'}}]

# disp_mesas = int(input("Informe a quantidade de mesas disponiveis inicialmente: "))

# horario_ini = int(input("Informe o horario de inicio das reservas (24h): "))
# horario_fim = int(input("Informe o horario do encerramento (24h): "))

# for mesa in range(disp_mesas):
#     restaurante.append({})
#     restaurante[mesa]['mesa'] = mesa
#     restaurante[mesa]['Reserva'] = {}
    
#     for horario in range(horario_ini, horario_fim, 2):
#         restaurante[mesa]['Reserva'][f'{horario}h'] = 'Disponivel'

system('cls')

while True:
    menu()
    op_menu = int(input("Opção: "))
    
    if op_menu == 4:
        break
    
    elif op_menu == 3:
        system('cls')
    
    elif op_menu == 0:
        ver_mesas(op_menu)
    
    elif op_menu == 1:
        ver_mesas(op_menu)
    
    elif op_menu == 2:
        ver_mesas(op_menu)
        
#Continuar -> Opçoes 1 e 2 funcionalidades
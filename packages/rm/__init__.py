from packages import *

#Remover mesa
def rm_mesa(restaurante):
    rm_mesa = input("Quantas mesa deseja remover: ").strip()
    
    if rm_mesa.isnumeric():
        for mesa in range(int(rm_mesa)):
            restaurante.pop()
        
        return restaurante
    
    else:
        print("Mesa incorreto!")

#Adicionar ou remover reservas 
def rm_reserva(restaurante): 
    mesa = input("Qual mesa: ").strip()
    horario = input("Qual horario: ").strip()
    
    if mesa.isnumeric() and horario.isnumeric():
        try:
            if restaurante[int(mesa)]['Reserva'][f'{horario}h'] == 'Reservado':
                restaurante[int(mesa)]['Reserva'][f'{horario}h'] = 'Disponivel'
                return restaurante
            
            elif restaurante[int(mesa)]['Reserva'][f'{horario}h'] == 'Disponivel':
                print()
                print(f"Horario das {horario}h está Disponivel.\n")
                
        except:
            print('Reserva não encontrada. Verifique a mesa/horario.')
        
        finally:
            return restaurante
    
    else:
        print("Mesa ou/ horario incorreto!")
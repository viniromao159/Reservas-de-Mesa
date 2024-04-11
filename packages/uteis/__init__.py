# Configuração para definir o escopo inicial de mesas
def start(disp_mesas, horario_ini, horario_fim, hora_reserva):
    restaurante = [] 

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
    
    return restaurante


# Opção de continuar no loop 
def continuar(): 
    continuar = input("Deseja continuar [s/n]: ").strip().lower()
    if continuar not in ['s', 'n']:
        print('Valor incorreto!')
        continuar = input("Deseja continuar [s/n]: ").strip().lower()
    if continuar == 'n':
        return False
    else:
        return True
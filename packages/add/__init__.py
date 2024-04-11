#Adicionar mesa
def ad_mesa(restaurante, horario_ini, horario_fim, hora_reserva):
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


#Adicionar ou remover reservas 
def ad_reserva(restaurante): 
        
    mesa = input("Qual mesa: ").strip()
    horario = input("Qual horario: ").strip()
    
    if mesa.isnumeric() and horario.isnumeric():
        try:
            if restaurante[int(mesa)]['Reserva'][f'{horario}h'] == 'Disponivel':
                restaurante[int(mesa)]['Reserva'][f'{horario}h'] = 'Reservado'
            
            elif restaurante[int(mesa)]['Reserva'][f'{horario}h'] == 'Reservado':
                print()
                print(f"Horario das {horario}h está Reservado.\n")
        except:
            print('Reserva não encontrada. Verifique a mesa/horario.')
        
        finally:
            return restaurante
    
    else:
        print("Mesa ou/ horario incorreto!")
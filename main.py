
from packages import uteis, tela, add, rm

#Programa principal
disp_mesas = int(input("Informe a quantidade de mesas disponiveis inicialmente: "))
horario_ini = int(input("Informe o horario de inicio das reservas (24h): "))
horario_fim = int(input("Informe o horario do encerramento (24h): "))
hora_reserva = int(input("Informe o perido de cada reserva (H): "))
restaurante = uteis.start(disp_mesas, horario_ini, horario_fim, hora_reserva)

tela.limparTela()
while True:
    tela.quebralinha()
    tela.menu()
    op_menu = input("Opção: ").strip()
    
    if op_menu == '6':
        tela.limparTela()
        print("Programa encerrado!")
        break
    
    elif op_menu == '5':
        tela.limparTela()
    
    elif op_menu == '0':
        tela.limparTela()
        tela.mostrar_mesas(restaurante)
        tela.quebralinha()
    
    elif op_menu == '1':
        restaurante = add.ad_mesa(restaurante, horario_ini, horario_fim, hora_reserva) 
    
    elif op_menu == '2':
        isTrue = True
        while isTrue:
            tela.mostrar_mesas(restaurante)
            tela.quebralinha()
            restaurante = rm.rm_mesa(restaurante)
            break
    
    elif op_menu == '3':
        isTrue = True
        while isTrue:
            tela.mostrar_mesas(restaurante)
            tela.quebralinha()
            restaurante = add.ad_reserva(restaurante)
            tela.quebralinha()
            isTrue = uteis.continuar()

    elif op_menu == '4':
        isTrue = True
        while isTrue:
            tela.mostrar_mesas(restaurante)
            tela.quebralinha()
            restaurante = rm.rm_reserva(restaurante)
            tela.quebralinha()
            isTrue = uteis.continuar()
            
    else:
        print("Valor inválido")
        
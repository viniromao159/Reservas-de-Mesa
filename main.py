# Usuario escolhe a quantidade de mesas disponiveis no estabelecimento.
# Usuario informa o inicio e o fim do funcionamento. 
# 
# Menu apresenta as opções: 1) Adicionar ou remover mesas disponiveis. 2) Adicionar ou remover reservas de mesas. 3) Sair do programa.
# 1) Adiciona ou remove mesas disponiveis pra reservar.
# 2) Oferece a opção de reservar a mesa e o horario. Programa apresenta as mesas disponiveis e seus respectivos horarios.
from funcionalidades import *

#Programa principal
start()
limparTela()
while True:
    menu()
    op_menu = input("Opção: ").strip()
    
    if op_menu == '6':
        limparTela()
        print("Programa encerrado!")
        break
    
    elif op_menu == '5':
        limparTela()
    
    elif op_menu == '0':
        limparTela()
        mostrar_mesas()
    
    elif op_menu == '1':
        ad_mesa() 
    
    elif op_menu == '2':
        isTrue = True
        while isTrue:
            mostrar_mesas()
            rm_mesa()
            break
    
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
        
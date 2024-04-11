
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
            isTrue = continuar()

    elif op_menu == '4':
        isTrue = True
        while isTrue:
            mostrar_mesas()
            ad_rm_reserva(op_menu)
            isTrue = continuar()
            
    else:
        print("Valor inválido")
        
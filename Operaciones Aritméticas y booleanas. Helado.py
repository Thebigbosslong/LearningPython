
apetece_helado_input = input("¿Te apetece un helado? (Si/No): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te he dicho que me respondas con si o no, entendere como que no")
    apetece_helado = False

tiene_dinero_input = input("¿Tienes dinero para un helado? (Si/No)").upper()
esta_el_senor_helados_input = input("¿Esta el señor de los helados? (Si/No)").upper()
esta_tu_tia_input = input("¿Esta tu tia? (Si/No)").upper()

tiene_dinero = tiene_dinero_input == "SI"
esta_tu_tia = esta_tu_tia_input == "SI"
puede_permitirselo = tiene_dinero or esta_tu_tia
esta_el_senor_helados = esta_el_senor_helados_input == "SI"

if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print("Pues comete un helado")
else:
    print("Pues nada")

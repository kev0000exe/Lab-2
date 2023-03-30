#iniciaremos la pagina de registro
print ("as ingresado ala pagina del cuartel general\n *****ingresa tu usuario***** ")
usuario = input()
print (" un gusto tenerte aqui",usuario )
print (" ingresa tu contraseña ")
contraseña = input()

print ("\n bienvenido ", usuario )
print (" as ingresado al menu del cuartel de trancito ")

print ("""menu de opciones
       \n menu
        1 regritrar infracciones  
        2 porcentaje
        """)

registro_esquelas = input ()
 # Pedimos al usuario que ingrese el número total de infracciones reportadas en el mes
N = int(input("Ingrese el número total de infracciones reportadas en el mes: "))

infracciones_matutinas = int(N * 0.2)
infracciones_vespertinas = int(N * 0.35)
infracciones_nocturnas = int(N * 0.45)



# Calculamos el promedio diario de infracciones en cada franja horaria
dias_del_mes = 30
promedio_matutino = infracciones_matutinas / dias_del_mes
promedio_vespertino = infracciones_vespertinas / dias_del_mes
promedio_nocturno = infracciones_nocturnas / dias_del_mes

# Imprimimos los resultados
print("Promedio diario de infracciones matutinas: ", promedio_matutino)
print("Promedio diario de infracciones vespertinas: ", promedio_vespertino)
print("Promedio diario de infracciones nocturnas: ", promedio_nocturno)

print (" FIN ")
#Este programa va a tener como finalidad mezclar varios elementos que pueda solicitar el usuario o
#vamos a color diferentes metodos para poder realizar actividades simple o secuenciales 
#del mismo modo permitirá realizar salidas de información sujetas a condiciones lógicas

print ("------------------------------inicio del programa------------------------------")

Edad1 = int(input("¿Cuál es su edad?"))

if Edad1 < 18:
    print ("Eres menor de edad")
else: 
    print ("Eres mayor de edad")

ClaveMayorEdad = ("-------------------------Modulo de seguridad-------------------------")

#Acá el usuario una vez se establece si es mayor de edad, le vamos a solicitar una contraseña 

print ("Su contraseña fue enviada exitosamente a su correo") 
ClaveMayorEdad = "19h" 
Password = input("Ingrese la contraseña que fue enviada a su correo")

if ClaveMayorEdad == Password.lower ():
    print ("Contraseña o password correcto")
else:
    print ("Constraseña incorrecta")

print ("----------------------------Modulo 3 de interacción----------------------------")

print ("Escriba una frase o palabra para seguir adelante en la autenticación")

frase = input (" Introduce una frase")
FraseMayorEdad = "mayor"
 
#Si se desea reemplazar la constraseña, solicite al usuario escribir en diferentes letras o numeros 
#la nueva contraseña o simplemente solicite un parametro de validación 

vocal  = input ("Introduzca una vocal en minuscula")
VocalMinuscula = m
# print (frase.replace(vocal, vocal.upper))

print (" Usted ha completado los tres modulos de autenticación / puede seguir adelante con el pago")





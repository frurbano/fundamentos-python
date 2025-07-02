#Ejemplo funciones
def my_function():
    print("Hola mundo desde la funcion")


def mostraNombre(nombre):
    print("Su nombres es "+nombre)

def area_Triangulo(base, altura):
    area=base*altura/2
    print(f"El area del triangulo es :{area}")

def area_Triangulo2(base, altura):
    area=base*altura/2
    return area
#funcion con argumentos predeterminados
def my_function2(country="Colombia"):
    print("I am from "+country)

my_function2("Sweden")
my_function2()


#Invocacion
my_function()
mostraNombre("Franco")
area_Triangulo(7,4)

#input retorna un string
#Entrada por teclado
#base = float(input("Base:"))
#altura =float(input("Altura:"))
#resultado=area_Triangulo2(base,altura)
#print("Resultado usando datos por teclado ", resultado)
print("Resultado ",area_Triangulo2(3,3))

#Funcion con argumento arbitrario
def mostrarEstudiantes(*args):
    print("El estudiante: "+args[0])

mostrarEstudiantes("Emil","Tobias","linus")

#Argumentos de palabra clave
def mostrarCarros(carro1,carro2,carro3):
    print("El carro es: "+carro2)

mostrarCarros(carro1="BMW", carro3="Ferrari", carro2="Ford")

#argumento arbitario **kwargs
def mostrarCliente(**kwargs):
    print("su apellido es: "+kwargs["apellido"])

mostrarCliente(nombre="tobias",apellido="Ref")

#funciones integradas
x=min(10,20,5)
y=max(5,10,25)
print(x)
print(y)

#Modulo de matematicas
import math
num2=math.sqrt(16)
#f para dar formato a la cadena
print(f"Raiz cuadrada :{num2}")
#Ejemplo cadenas de caracteres
text1=" Fundamentos con "
text2="Python"
result=text1 + text2
print(result)

#formato
price=97
text3=f"el precio es {price:.2f} dolares"
print(text3)

#la f es por sintaxis para darle formato a la cadena
nombre="franco"
lastname="urbano"
fullname=f"Mi nombre es: {nombre} {lastname}"
print(fullname)

'''
Operaciones matematicas
'''
text4=f"La multipicacion es {20*59}"
print(text4)

text5="franco"
result=text5.capitalize()
print(f"Primera letra en mayuscula: {result}")

title="Cien Años de Soledad"
titleConvert=title.casefold()
print(f"Convierte a minusculas: {titleConvert}")

fruit="banana"
textCenter=fruit.center(20,"-")
print(textCenter)

title1="I love apples and apple"
result2=title1.count("apple")
print(result2)

text6="Curso fundamentos con python. "
result3=text6.endswith("")
print(result3)

letter="F\tU\tP"
letterSpaces=letter.expandtabs(8)
print(f"Para colocar espacios:{letterSpaces}")

text7="Hola bienvenidos a Colombia"
result4=text7.find("bienvenidos")
print(f"Retorna desde que posicion encontro la palabra:{result4}")


text8="hola mundo"
result5=text8.title()
print(result5)

alphanumeric="python 312"
result6=alphanumeric.isalnum()
print(f"Retorno:{result6}")

letters="Space X"
result7=letters.isalpha()
print(f"esta dentro del alfabeto?:{result7}")
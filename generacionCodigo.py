import re
print("GENERACION DE CODIGO INTERMEDIO")
print("EJEMPLO 1: 2 + 5 * y") 
print("EJEMPLO 2: a / a + b * b") 
print("EJEMPLO 3: (a+ 2) / 3 + b")
x=int(input("Seleccione una opcion: "))
if x==1:
    #EJEMPLO UNO SIN USO DE REGEX, CON LISTAS.
    p = []
    vs = []
    valor =str(input("ingrese la expresion \n"))
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
    tempoCero = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            tempoCero = "t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1]  #LA LISTA P VAN DESGLOZANDO LA EXPRESION EN PARTES
            p.remove(p[suma]) # SE ELIMINA "*"
            p.remove(p[suma-1]) #SE ELIMINA EL "5"
            p.remove(p[suma-1]) #SE ELIMINA EL "Y"
    print(tempoCero)
    tempoUno = ""
    for i in p:
        if i == "+" or i == "-": # SUMA O RESTA 
            if p[-1] == "+" or p[-1]=="-":
                tempoUno = "t1 ="+ p[0] + " "+ p[-1] + " " +"t0"
                
            else:
                tempoUno = "t1 = "+ p[-1] + " "+ p[-2] + " " +"t0"
    print(tempoUno)
elif x==2:
    p = []
    vs = []
    valor =str(input("ingrese la expresion \n"))
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
    tempoCero = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            tempoCero = "t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1] 
            p.remove(p[suma-1])
            p.remove(p[suma])
            p.remove(p[suma-1])
            break 
        else: 
                if i == "/":
                    tempoCero = "t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1]
                    p.remove(p[suma-1])
                    p.remove(p[suma])
                    p.remove(p[suma-1])
                    break      
    print(tempoCero)
    tempoUno = ""
    for i in p: # MULTIPLICACION O DIVISION
        if p[3] =="+":
            if p[suma-4]=="/" or p[suma-4]=="*":
                 tempoUno = "t1 = " + p[suma-5] + " " +  p[suma-4] + " " + p[suma-3] 
            elif p[suma-4]  != "/" or p[suma-4] !="*":
                if p[suma-4] == "+" or p[suma-4]=="-":
                    tempoUno = "t1 = " + p[suma-3] + " " +  p[suma-2] + "t0"
        elif p[3] !="+":
            if p[suma+1]=="/" or p[suma+1]=="*":
                #STRING TEMPORAL CERO
                # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
                tempoUno = "t1 = " + p[suma] + " " +  p[suma+1] + " " + p[suma+2]   
            elif p[suma+1]  != "/" or p[suma+1] !="*":
                if p[suma+1] == "+" or p[suma+1]=="-":
                    tempoUno = "t1 = t0 " + p[suma-1] + " " +  p[suma]
    print(tempoUno)
    tempoDos = ""
    for i in p: # MULTIPLICACION O DIVISION
        if p[3] =="+":
            if p[suma-4]=="/" or p[suma-4]=="*":
                 tempoDos = "t2 = " + tempoRALCero[0:3] + " " +  p[suma-4] + " " + tempoUno[0:3]
            elif p[suma-4]  != "/" or p[suma-4] !="*":
                if p[suma-4] == "+" or p[suma-4]=="-":
                    tempoDos = "t2 = " + p[suma-5] + " " +  p[suma-4] + "t1"
        elif p[3] !="+":
            if p[suma+1]=="/" or p[suma+1]=="*":
                #STRING TEMPORAL CERO
                # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
                tempoDos = "t2 = " + tempoRALCero[0:3] + " " +  p[suma-1] + " " + tempoUno[0:3]  
            elif p[suma+1]  != "/" or p[suma+1] !="*":
                if p[suma+1] == "+" or p[suma+1]=="-":
                    tempoDos = "t1 = t0 " + p[suma+1] + " " +  p[suma+2]
    print(tempoDos)
elif x==3:
    p = []
    vs = []
    valor =str(input("ingrese la expresion \n"))
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
    tempoCero = ""
    for i in p: 
        suma +=1
        if i =="(" or i == ")":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            tempoCero = "t0 = " + p[suma-4] + " " +  p[suma-3] + " " + p[suma-2] + " " + p[suma-1] + " " + p[suma]
 
    tempoUno = ""
    for i in p:
        if i == "*" or i == "/":
            if p[4] == "(" :
                tempoUno = "t1 ="+ " t0 " + p[suma-5] + " " +  p[suma-6] + " " 
            else:
                tempoUno = "t1 = " + p[suma-2] + " " +  p[suma-3] + " " +  "t0"
    tempoDos = ""
    for i in p:
        if i == "+" or i == "-": 
            if p[4] == "(" :
                tempoDos = "t2="+ " _t1 " + p[suma-7] + " " +  p[suma-8] + " " 
            else:
                tempoDos = "t2 = " + p[suma] + " " +  p[suma-1] + " " +  "t1"
    print(tempoCero)
    print(tempoUno)
    print(tempoDos)

print()
print("INTEGRANTES")
print("DIMAS NAHUAT HERRERA")
print("DALIA ABIGAIL CHI POOT")
print("JOSE ADALBERTO TUZ AY")
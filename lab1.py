'''Ingreso de Datos'''
MesAct = int(input("Ingrese el mes en el que comenzó a trabajar (número): "))
NumMeses = 13 - MesAct
RemMensual = float(input("Ingrese remuneración mensual: "))
Grati = float(input("Ingrese gratificaciones y remuneraciones extras: "))

opcion = int(input("Recibió pagos extraordinarios (1=sí, 0=no):"))

if opcion == 1:
    mes = int(input("Ingrese mes en el que recibió pago (número): "))
    MontoExtra = float(input("Ingrese pagos extraordinarios: "))
else:
    MontoExtra = 0

AdicionalBruto = Grati

'''Variables Fijas'''
UIT = 4300
TazaImp = 0


'''Paso 1'''
RemBrutaAnual = RemMensual * NumMeses + AdicionalBruto

'''Paso 2'''
if (RemBrutaAnual > 7*UIT):
    RemNetaAnual = RemBrutaAnual - ( 7 * UIT)
else:
    RemNetaAnual = 0
    print("---- Usted no estará sujeto a retención ----")
    exit()

'''Paso 3'''
if (RemNetaAnual <= 5 * UIT):
    TazaImp = 0.08
elif (5*UIT < RemNetaAnual <= 20*UIT):
    TazaImp = 0.14
elif (20*UIT < RemNetaAnual <= 35*UIT):
    TazaImp = 0.17
elif (35*UIT < RemNetaAnual <= 45*UIT):
    TazaImp = 0.2
else:
    TazaImp = 0.3

ImpAnualProy = TazaImp * RemNetaAnual


'''Paso 4'''
'enero'
if (MesAct > 1): ImpEne = 0
else: ImpEne = ImpAnualProy / 12

'febrero'
if (MesAct > 2): ImpFeb = 0
else: ImpFeb = ImpAnualProy / 12
'marzo'
if (MesAct > 3): ImpMar = 0
else: ImpMar = ImpAnualProy / 12
Ene2Mar = ImpEne + ImpFeb + ImpMar
'abril'
if (MesAct > 4): ImpAbr = 0
else: ImpAbr = (ImpAnualProy - Ene2Mar) / 9
Ene2Abr = Ene2Mar + ImpAbr
'mayo'
if (MesAct > 5): ImpMay = 0
else: ImpMay = (ImpAnualProy - Ene2Abr) / 8
'junio'
if (MesAct > 6): ImpJun = 0
else: ImpJun = (ImpAnualProy - Ene2Abr) / 8
'julio'
if (MesAct > 7): ImpJul = 0
else: ImpJul = (ImpAnualProy - Ene2Abr) / 8
Ene2Jul = Ene2Abr + ImpMay + ImpJun + ImpJul
'agosto'
if (MesAct > 8): ImpAgo = 0
else: ImpAgo = (ImpAnualProy - Ene2Jul) / 5
Ene2Ago = Ene2Jul + ImpAgo
'setiembre'
if (MesAct > 9): ImpSep = 0
else: ImpSep = (ImpAnualProy - Ene2Ago) / 4
'octubre'
if (MesAct > 10): ImpOct = 0
else: ImpOct = (ImpAnualProy - Ene2Ago) / 4
'noviembre'
if (MesAct > 11): ImpNov = 0
else: ImpNov = (ImpAnualProy - Ene2Ago) / 4
'diciembre'
ImpDic = ImpAnualProy - (Ene2Ago + ImpSep + ImpOct + ImpNov)

'''Paso 5'''
SumExt = MontoExtra + RemNetaAnual

if (SumExt <= 5 * UIT):
    TazaImp2 = 0.08
elif (5*UIT < SumExt <= 20*UIT):
    TazaImp2 = 0.14
elif (20*UIT < SumExt <= 35*UIT):
    TazaImp2 = 0.17
elif (35*UIT < SumExt <= 45*UIT):
    TazaImp2 = 0.2
else:
    TazaImp2 = 0.3

Temp = TazaImp2 * SumExt
RetAdiMes = Temp - ImpAnualProy

if opcion == 0:
    print("Tu empleador retendrá s/.",round(ImpAnualProy,2),"por concepto del impuesto a la renta de quinta categoría de la siguiente manera:")
    print("Enero:     ", round(ImpEne,2))
    print("Febrero:   ", round(ImpFeb,2))
    print("Marzo:     ", round(ImpMar,2))
    print("Abril:     ", round(ImpAbr,2))
    print("Mayo:      ", round(ImpMay,2))
    print("Junio:     ", round(ImpJun,2))
    print("Julio:     ", round(ImpJul,2))
    print("Agosto:    ", round(ImpAgo,2))
    print("Septiembre:", round(ImpSep,2))
    print("Octubre:   ", round(ImpOct,2))
    print("Noviembre: ", round(ImpNov,2))
    print("Diciembre: ", round(ImpDic,2))

'''caso pago extra ENERO'''
if opcion == 1:
    if mes == 1:
        ImpEne = RetAdiMes + ImpEne
    elif mes == 2:
        ImpFeb = RetAdiMes + ImpFeb
    elif mes == 3:
        ImpMar = RetAdiMes + ImpMar
    elif mes == 4:
        ImpAbr = RetAdiMes + ImpAbr
    elif mes == 5:
        ImpMay = RetAdiMes + ImpMay
    elif mes == 6:
        ImpJun = RetAdiMes + ImpJun
    elif mes == 7:
        ImpJul = RetAdiMes + ImpJul
    elif mes == 8:
        ImpAgo = RetAdiMes + ImpAgo
    elif mes == 9:
        ImpSep = RetAdiMes + ImpSep
    elif mes == 10:
        ImpOct = RetAdiMes + ImpOct
    elif mes == 11:
        ImpNov = RetAdiMes + ImpNov
    elif mes == 12:
        ImpDic = RetAdiMes + ImpDic
    else:
        print("Valor incorrecto")

    print("Tu empleador retendrá s/.", round(ImpAnualProy, 2),"por concepto del impuesto a la renta de quinta categoría de la siguiente manera:")
    print("Enero:     ", round(ImpEne, 2))
    print("Febrero:   ", round(ImpFeb, 2))
    print("Marzo:     ", round(ImpMar, 2))
    print("Abril:     ", round(ImpAbr, 2))
    print("Mayo:      ", round(ImpMay, 2))
    print("Junio:     ", round(ImpJun, 2))
    print("Julio:     ", round(ImpJul, 2))
    print("Agosto:    ", round(ImpAgo, 2))
    print("Septiembre:", round(ImpSep, 2))
    print("Octubre:   ", round(ImpOct, 2))
    print("Noviembre: ", round(ImpNov, 2))
    print("Diciembre: ", round(ImpDic, 2))



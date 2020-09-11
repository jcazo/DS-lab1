
MesAct = int(input("Ingrese el mes en el que realizará el cálculo (en número): "))
NumMeses = 13 - MesAct
RemMensual = int(input("Ingrese su remuneración mensual: "))
UIT = 4300
AdicionalBruto = int(input("Ingrese sus ingresos adicionales y gratificaciones: "))
TazaImp = 0

RemBrutaAnual = RemMensual * NumMeses + AdicionalBruto

if (RemBrutaAnual > 7*UIT):
    RemNetaAnual = RemBrutaAnual - ( 7 * UIT)
    if (RemNetaAnual <= 5*UIT):     TazaImp = 0.08
    elif (RemNetaAnual <= 20*UIT):  TazaImp = 0.14
    elif (RemNetaAnual <= 35*UIT):  TazaImp = 0.17
    elif (RemNetaAnual <= 45*UIT):  TazaImp = 0.2
    else:  TazaImp = 0.3
else:
    RemNetaAnual = 0
    print("---- Usted no pagará impuestos este periodo ----")
    exit()

ImpAnualProy = TazaImp * RemNetaAnual

if (MesAct > 1): ImpEne = 0
else: ImpEne = ImpAnualProy / 12

if (MesAct > 2): ImpFeb = 0
else: ImpFeb = ImpAnualProy / 12

if (MesAct > 3): ImpMar = 0
else: ImpMar = ImpAnualProy / 12
Ene2Mar = ImpEne + ImpFeb + ImpMar

if (MesAct > 4): ImpAbr = 0
else: ImpAbr = (ImpAnualProy - Ene2Mar) / 9
Ene2Abr = Ene2Mar + ImpAbr

if (MesAct > 5): ImpMay = 0
else: ImpMay = (ImpAnualProy - Ene2Abr) / 8

if (MesAct > 6): ImpJun = 0
else: ImpJun = (ImpAnualProy - Ene2Abr) / 8

if (MesAct > 7): ImpJul = 0
else: ImpJul = (ImpAnualProy - Ene2Abr) / 8
Ene2Jul = Ene2Abr + ImpMay + ImpJun + ImpJul

if (MesAct > 8): ImpAgo = 0
else: ImpAgo = (ImpAnualProy - Ene2Jul) / 5
Ene2Ago = Ene2Jul + ImpAgo

if (MesAct > 9): ImpAgo = 0
else: ImpSep = (ImpAnualProy - Ene2Ago) / 4

if (MesAct > 10): ImpAgo = 0
else: ImpOct = (ImpAnualProy - Ene2Ago) / 4

if (MesAct > 11): ImpAgo = 0
else: ImpNov = (ImpAnualProy - Ene2Ago) / 4

ImpDic = ImpAnualProy - (Ene2Ago + ImpSep + ImpOct + ImpNov)

print("Usted pagará s/.",round(ImpAnualProy,2),"de impuestos de la siguiente manera:")
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

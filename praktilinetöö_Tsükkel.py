#Ülesanne 1
print("tervist!")
nimi=""
nimi=str(input("Palun sisesta oma nimi:"))
for i in range(1,6):
    print(f"Ole tervitatud {nimi}, {i}. korda.")

#Ülesanne 2
from keyboard import *
summa=0
while True:
    print("Считаем? 'esc' - выход, 'enter' - продолжаем")
    try:
        num=int(input('Sisesta number: '))
        summa+=num
    except:
        ValueError
        print("See ei ole number!")
    if read_key()=='enter':
        print(summa)
    elif read_key()=='esc':
        break


#Ülesanne 3
ID=""
A=""
Med=""
while ID.isdigit()!= True or len(ID)!= 11 or int(ID[0]) not in [1,2,3,4,5,6] or 0<int(ID[3:5])>13 or 0<int(ID[5:7])>31:
    try:
        ID=input("Введи свой ID: ")
    except:
        TypeError
if int(ID[0]) in [2,4,6]:
    print("Пол: Женский")
else:
    print("Пол: Мужской")
if ID[1:3] in [1,2]:
    A="18"
elif ID[1:3] in [3,4]:
    A="19"
elif ID[1:3] in [5,6]:
    A="20"

if 1<=int(ID[7:11])<11:
    Med="Kuressaare haigla"
elif 11<=int(ID[7:11])<=19:
    Med="Tartu Ülikooli Naistekliinik"
elif 21<=int(ID[7:11])<=150:
    Med="Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja"
elif 151<=int(ID[7:11])<=160:
    Med="Keila haigla"
elif 161<=int(ID[7:11])<=220:
    Med="Rapla haigla, Loksa haigla, Hiiumaa haigla"
elif 221<=int(ID[7:11])<=270:
    Med="Ida-Viru keskhaigla"
elif 271<=int(ID[7:11])<=370:
    Med="Maarjamõisa kliinikum, Jõgeva haigla"
elif 371<=int(ID[7:11])<=420:
    Med="Narva haigla"
elif 421<=int(ID[7:11])<=470:
    Med="Pärnu haigla"
elif 471<=int(ID[7:11])<=490:
    Med="Haapsalu haigla"
elif 491<=int(ID[7:11])<=520:
    Med="Järvamaa haigla"
elif 521<=int(ID[7:11])<=570:
    Med="Rakvere haigla, Tapa haigla"
elif 571<=int(ID[7:11])<=600:
    Med="Valga haigla"
elif 601<=int(ID[7:11])<=650:
    Med="Viljandi haigla"
elif 651<=int(ID[7:11])<700:
    Med="Lõuna-Eesti haigla, Põlva haigla"

SUM=1*int(ID[0])+2*int(ID[1])+3*int(ID[2])+4*int(ID[3])+5*int(ID[4])+6*int(ID[5])+7*int(ID[6])+8*int(ID[7])+9*int(ID[8])+1*int(ID[9])
Kontrol=(SUM//11)*11
if Kontrol==10:
    SUM=3*int(ID[0])+4*int(ID[1])+5*int(ID[2])+6*int(ID[3])+7*int(ID[4])+8*int(ID[5])+9*int(ID[6])+1*int(ID[7])+2*int(ID[8])+3*int(ID[9])
(Kontrol//11)*11
Kontrol=SUM-Kontrol

print(ID[5:7]+"."+ID[3:5]+"."+A+ID[1:3]+" "+Med)
print("Контрольная цифра: "+str(Kontrol))

#Ülesanne 4

while kogus not in [1,2,3,4,5,6,7,8,9,10]:
        try:
            kogus=int(input("Выберите кол-во примеров:"))
        except TypeError:
            print("Максимум 10 примеров")

for i in range(1,kogus+1):
    arv1=randint(0,100)
    arv2=randint(0,100)
    tehe=randint(1,2)
if tehe==1:
    mark="+"
    print(f"{arv1}{mark}{arv2}=")
    vas=arv1+arv2
elif tehe==2:
    mark="-"
    print(f"{arv1}{mark}{arv2}=")
    vas=arv1-arv2

vastus=int(input())
if vastus==vas: 
    oige+=1
    print("Молодец!")


#Ülesanne 5

for i in range(1, 11):
    for j in range(1, 11):
         print(f" {i * j} " , end = " ")
    print ()








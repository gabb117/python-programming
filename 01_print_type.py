#Formattazione dell'output

#print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

#value:parametro da inserire, es. stringa o intero, posso scrivere N value

#sep='':inserisce tra i parametri uno spazio o un carattere

data = 15
print("Oggi è il giorno",data,sep=';')# output: oggi è il giorno;15

#end='\n' :indica al print di inserire alla fine della visualizzazione il
    #carattere \n di new line (a capo)
print("ieri", end=' ')
print("oggi", end=' ')
print("domani", end= '\n')

#stampa: 'ieri oggi domani'
#altrimenti avrrebbe stampato andando a capo :
#ieri
#oggi
#domani

#file=sys.stout :indica che print dovrà visualizzare gli argomenti a schermo che
#rappresenta lo standard output (stdout)

#flush= False:specifica se l'output deve essere visualizzato a schermo carattere
#per carattere (True) o bufferizzato, (False), l'insieme dei parametri print
#tutti insieme. Il valore di default è False.

#Caratteri di escape

#Caratteri speciali utilizzabili nei lettereali di stringa, sono preceduti da \
#\n :newline
#\t :tabulazione orizzontale
#\' :stampa virgoletta singola
#\" :stampa virgoletta doppia
#\\ :stampa una barra inversa

print("Lun\tMar\tMer\nGio\tVen\tSab")
#risulteranno stampati:
#Lun Mar Mer
#Gio Ven Sab
print("ciao\'ciao")
print("ciao\"ciao")
print("ciao\/ciao")


#Concatenazioni di stringhe

s="Domani sarà proprio " + "una bella giornata"
print(s)

#Formato dei numeri

#inserisce valori dentro le stringhe in modo ordinato e leggibile

name="Luca"
age=32

print("Mi chiamo {} e ho {} anni.".format(name,age))#inserisce variabili
print("Secondo: {1} e primo: {0}.".format("1","2"))#inserisce stringhe usando indici
print("Ciao {nome},il tuo saldo è: {saldo}€.".format(nome="Aldo",saldo=8400))
#inserisce variabili create nella funzione format()


#formattazione standard prevede separatori delle migliaia e dei decimali nella forma USA

print(format(12345.6780000009, ".3f"))
print(format(12345.6780000009, "e"))
print(format(12345.6780000009, ".2e"))

#12345.678 :3 cifre decimali
#1.234568e+04 :notazione scientifica
#1.23e+04 :notazione scientifica con due cifre decimali


print(format(12345.6780000009, "15.2f"))
#15 si riferisce al numero di spazi che deve occupare la virgola

print(format(0.5, ".2%"))
#percentuale

print(format(123456, "d"))
#senza separatore migliaia

print(format(123456, ",d"))
#con separatore migliaia

print(format(123456, "10d"))
#senza separatore in spazio da 10

print(format(123456, "10,d"))
#con separatore in spazio da 10

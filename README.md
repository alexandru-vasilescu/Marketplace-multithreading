Nume: Vasilescu Alexandru Madalin
Grupa: 331CB

# Tema 1
### Marketplace multithreading

Organizare
-

Am lucrat in cele 3 clase si fisiere obligatorii. Nu am adaugat nici o clasa sau metoda in plus.


***Producer***

* In producer am initializat ca atribute ale clasei tot ce am primit in init.
* Am adaugat un atribut de id_producer obtinut in urma apelarii metodei de register_producer din marketplace.
* In metoda run, intr-un while inifinit, parsez fiecare produs din lista pe rand (produs, cantitate, timp de asteptare). Adaug produsele in market in functie de cantitate si astept dupa fiecare adaugare.
* Daca o adaugare nu a reusit, producatorul asteapta timpul lui primit ca atribut si incearca din nou.


***Consumer***

* In consumer am initializat atributele primite la init.
* In metoda run, am parsat fiecare cart in parte:
* Prima data l-am adaugat in market folosind metoda new_cart
* Am executat fiecare actiune din cart (add sau remove) in functie de cum au fost explicate.
* Dupa executarea tuturor actiunilor apelez place order si afisez produsele din cart si apoi trec la urmatorul cart.


***Marketplace***

* Am creat cate un atribut de numarat producatorii si carturile pentru a le putea returna un id.
* De asemenea pentru producatori si carturi am un dictionar separat unde in functie de id retin produsele(un dictionar cu key = id si value = lista de produse).
* Pentru cart am folosit o lista de tupluri, primul element este id-ul producatorului si al doilea produsul. Astfel pot returna la producatorul de unde s-a luat un produs.
* Am creat un atribut de lock pentru a putea sincroniza adaugarea producatorului si cartului, incrementarile fiind operatii nesincronizate.
* Adaugarea si eliminarea din liste se face fara metode de sincronizare deoarece sunt operatii deja sincronizate.
* Restul metodelor sunt realizate conform explicatiilor oferite 

***Utilitate***
* Consider tema destul de utila pentru un site care se ocupa cu online shopping, produsele putand fi extinse la orice, nu doar ceai si cafea.

***Imbunatatiri***
* Probabil sincronizarea cu semafoare ar fi mai interesanta si complicata decat cu sleepuri cum este cerut in enunt. As fi preferat sa nu fie nevoie de wait_time si sincronizarea sa poata fi facuta automat.

Implementare
-

* Am implementat intreg enuntul
* Checkerul local imi ofera punctaj maxim atat pe teste cat si pylint.
* Nu am adaugat functionalitati.

Resurse utilizate
-

* Am urmat indicatiile din comentarii, enunt si forum.
* Am folosit logica din laboratoarele de sincronizare de la problemele producer_consumer si worker_master.

Git
-

https://github.com/alexandru-vasilescu/Marketplace-multithreading


import os

# inserimento file su cui svolgere analisi
toAnalise_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/data/document/basic/esame1.txt"
Keyword_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/data/keyword/basic_keyword/basic.txt"

if os.path.exists(toAnalise_path) and os.path.exists(Keyword_path):
    # Apre entrambi i file
    with open(toAnalise_path, "r") as fA, open(Keyword_path, "r") as fK:

        # Inizializza la lista
        keywords_list = []

        # Legge riga per riga le parole chiave e le aggiunge alla lista
        keyword_letta = fK.readline()
        while keyword_letta != "":
            keywords_list.append(keyword_letta.strip())  # .strip() toglie \n e spazi
            keyword_letta = fK.readline()

        print("Lista delle parole chiave:", keywords_list)

        # Crea un dizionario inizializzato a zero per ciascuna parola chiave
        dizionario_conta = {keyword: 0 for keyword in keywords_list}
        print("Dizionario iniziale:", dizionario_conta)

        # leggo riga per riga del file "toAnalise" e verifico che sia un elemento
        riga_letta = fA.readline()
        while riga_letta != "":
            parola = riga_letta.strip()  # toglie spazi e \n
            if parola in dizionario_conta:
                dizionario_conta[parola] += 1
            riga_letta = fA.readline()

        print("Dizionario finale:", dizionario_conta)

else:
    print("Uno o entrambi i file non esistono")
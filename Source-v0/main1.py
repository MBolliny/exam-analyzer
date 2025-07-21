import os

# inserimento cartella su cui svolgere analisi
toAnalise_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/Source-v0/testing-file-v0"

# Verifica se il percorso esiste
# se esiste -> vado avanti con progetto
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

        contenuto = os.listdir(toAnalise_path)
        # per ogni elemento della lista crare un path e verificare che questo sia cartella o docuento
        for elemento in contenuto:

            # creo path completo per aprire file e cartelle e verificarne idenita1
            percorso_completo = os.path.join(toAnalise_path, elemento)

            if os.path.isdir(percorso_completo):  # è una cartella -> cosa ricorsiva fino a che non ottengo file
                print(elemento, "è cartella")

            elif os.path.isfile(percorso_completo):  # è un file -> apro e confronto
                # apro il file
                print(elemento, "è file")
                file = open(elemento, "r")

    # stampa finale
    print("Dizionario finale:", dizionario_conta)

else:
    print("Uno o entrambi i file non esistono")


def analisiFile ():
    # leggo riga per riga del file "toAnalise" e verifico che sia un elemento
    riga_letta = fA.readline()
    while riga_letta != "":
        parola = riga_letta.strip()  # toglie spazi e \n
        if parola in dizionario_conta:
            dizionario_conta[parola] += 1
        riga_letta = fA.readline()
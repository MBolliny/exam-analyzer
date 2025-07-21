import os

# inserimento cartella su cui svolgere analisi
toAnalise_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/data/document"
Keyword_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/data/keyword/basic_keyword/basic.txt"
Log_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/log.txt"

# FUNZIONE analisiFile
def analisiFile(percorso_file, dizionario_conta):
    with open(percorso_file, "r") as f:
        riga_letta = f.readline()
        while riga_letta != "":
            parola = riga_letta.strip()
            if parola in dizionario_conta:
                dizionario_conta[parola] += 1
            riga_letta = f.readline()

# FUNZIONE analisiCartella
def analisiCartella(percorso, dizionario_conta):
    contenuto = os.listdir(percorso)
    for elemento in contenuto:
        percorso_completo = os.path.join(percorso, elemento)
        print(percorso_completo)
        if os.path.isdir(percorso_completo):
            print(elemento, "è una cartella")
            analisiCartella(percorso_completo, dizionario_conta)

        elif os.path.isfile(percorso_completo):
            if elemento == ".DS_Store":
                continue  # salta questo file

            print(elemento, "è un file")
            analisiFile(percorso_completo, dizionario_conta)

        elif os.path.isfile(percorso_completo):
            print(elemento, "è un file")
            analisiFile(percorso_completo, dizionario_conta)

# Verifica se il percorso esiste
if os.path.exists(toAnalise_path) and os.path.exists(Keyword_path):

    with open(Keyword_path, "r") as fK:
        keywords_list = [line.strip() for line in fK]

    # creazione dizionario
    dizionario_conta = {keyword: 0 for keyword in keywords_list}

    # lettura file da analizzare
    analisiCartella(toAnalise_path, dizionario_conta)

    # stampa del risultato a video
    for parola, conteggio in dizionario_conta.items():
        print(parola, ":", conteggio)

    # stampa del risultato su file
    with open(Log_path, "w") as log:
        for keyword, count in dizionario_conta.items():
            log.write(f"{keyword}: {count}\n")

else:
    print("Percorso non valido")
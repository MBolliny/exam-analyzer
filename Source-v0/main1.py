import os

# inserimento cartella su cui svolgere analisi
toAnalise_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/Source-v0/testing-file-v0"
Keyword_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/Source-v0/keyword.txt"

# 1. FUNZIONE analisiFile
def analisiFile(percorso_file, dizionario_conta):
    with open(percorso_file, "r") as f:
        riga_letta = f.readline()
        while riga_letta != "":
            parola = riga_letta.strip()
            if parola in dizionario_conta:
                dizionario_conta[parola] += 1
            riga_letta = f.readline()

# 2. FUNZIONE analisiCartella
def analisiCartella(percorso, dizionario_conta):
    contenuto = os.listdir(percorso)
    for elemento in contenuto:
        percorso_completo = os.path.join(percorso, elemento)
        print(percorso_completo)
        if os.path.isdir(percorso_completo):
            print("📁", elemento, "è una cartella")
            analisiCartella(percorso_completo, dizionario_conta)

        elif os.path.isfile(percorso_completo):
            if elemento == ".DS_Store":
                continue  # salta questo file

            print("📄", elemento, "è un file")
            analisiFile(percorso_completo, dizionario_conta)

        elif os.path.isfile(percorso_completo):
            print("📄", elemento, "è un file")
            analisiFile(percorso_completo, dizionario_conta)

# Verifica se il percorso esiste
# se esiste -> vado avanti con progetto

if os.path.exists(toAnalise_path) and os.path.exists(Keyword_path):

    with open(Keyword_path, "r") as fK:
        keywords_list = [line.strip() for line in fK]

    dizionario_conta = {keyword: 0 for keyword in keywords_list}

    analisiCartella(toAnalise_path, dizionario_conta)

    for parola, conteggio in dizionario_conta.items():
        print(parola, ":", conteggio)

else:
    print("❌ Percorso non valido")
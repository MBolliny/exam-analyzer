import os
"""
# inserimento path della cartella dove devo cercare
°nome_file = input("inserire argomento da cercare: ")

# inserimento parola = file in cartella testing-file-v1
# apertura cartella
path = "/Users/MatteoBollini/Documents/Progetti-programmazione/project-01-exam-analizer-v1/keword-v1"

# Verifica se il percorso esiste
print(os.path.exists(path))

# Se esiste, elenca il contenuto
if os.path.exists(path):
    contenuto = os.listdir(path)
    print("Lista file keyword:", contenuto)

    # ricerca del nome file
    for elemento in contenuto:
        if(nome_file == elemento):
            open(nome_file, "r")
    else:
        print("Il percorso non esiste")

import os
"""
# acquisizione di cosa cercare
nome_file = input("Inserire nome file da cercare: ")
nome_file = nome_file + ".txt"  # o nome_file += ".txt"
print(f"Cercherò il file: {nome_file}")

path = "/Users/MatteoBollini/Documents/Progetti-programmazione/project-01-exam-analizer-v1/keword-v1"

# Verifica se il percorso esiste
if os.path.exists(path):
    contenuto = os.listdir(path)
    print("Lista file nella cartella:", contenuto)

    # Cerca il file
    # se file esiste -> apro file
    if nome_file in contenuto:
        file_completo = os.path.join(path, nome_file)  # Percorso completo
        print(f"File '{nome_file}' trovato! Apertura in corso...")

        try:
            with open(file_completo, "r") as file:
                contenuto_file = file.read()
                print("\n--- CONTENUTO DEL FILE ---")
                print(contenuto_file)
        except Exception as e:
            print(f"Errore nell'apertura: {e}")
    else:
        print(f"File '{nome_file}' NON trovato nella cartella")
else:
    print("Il percorso della cartella non esiste")


# se riesci ad aprire file -> vado avanti con progetto


# aprire la cartella di base

# scorrere tutte le sottocartelle (se ce ne sono)

# aprire la sottocartella

# scorrere tutti i file presenti nella sottocartella

# se il file è un .txt allora aprirlo

# scorrere il file riga per riga

# controllare se una delle parole chiave è presente nella riga

# se sì, aumentare contatore, salvare il file, la riga e la parola trovata

# alla fine stampare o salvare i risultati
import os

# inserimento cartella su cui svolgere analisi
# lookFor_path = input("inserire pathname cartella su cui fare la analisi: ")
lookFor_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/Source/testing-file-v1"

# Verifica se il percorso esiste
# se esiste -> vado avanti con progetto
if os.path.exists(lookFor_path):

    # acquisizione di COSA cercare
    # visualizzazione delle scelte
    keyword_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/Source/keword-v1"
    contenuto = os.listdir(keyword_path)
    print("Lista argomenti che si possono cercare:", contenuto)

    # acqusizione della scelta
    nome_file = input("Inserire nome file da cercare: ")
    nome_file = nome_file + ".txt"  # o nome_file += ".txt"
    # debug - print(f"Cercherò il file: {nome_file}")

    # lavoro su file inserito
    # per ogni elemento della lista crare un path e verificare che questo sia cartella o docuento
    for elemento in contenuto:
        # creo path completo per aprire file e cartelle e verificarne idenita1
        percorso_completo = os.path.join(lookFor_path, elemento)

        if os.path.isdir(percorso_completo): # è una cartella -> cosa ricorsiva fino a che non ottengo file

        elif os.path.isfile(percorso_completo):  # è un file -> apro e confronto
            fopen(percorso_completo, "r")
            # verificare c



else:
    print("Il percorso della cartella non esiste")





# aprire la cartella di base

# scorrere tutte le sottocartelle (se ce ne sono)

# aprire la sottocartella

# scorrere tutti i file presenti nella sottocartella

# se il file è un .txt allora aprirlo

# scorrere il file riga per riga

# controllare se una delle parole chiave è presente nella riga

# se sì, aumentare contatore, salvare il file, la riga e la parola trovata

# alla fine stampare o salvare i risultati
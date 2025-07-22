'''
prende keyword a "teoremi.txt" come FRASI
scansiona testo con FRASI
'''

import os

from fontTools.varLib.cff import conv_to_int

toAnalise_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/data/document/advanced/esame2.txt"
Keyword_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/data/keyword/advanced_keyboard/teoremi.txt"
Log_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/log.txt"

if os.path.exists(toAnalise_path):
    if os.path.exists(Keyword_path):

        with open(toAnalise_path, "r") as fA, open(Keyword_path, "r") as fK:
            # print("apro i file")

            # creazione e riempimento della lista
            keywords_list = []
            keyword_letta = fK.readline()
            while  keyword_letta != "":
                # formatto la stringa
                keyword_letta = keyword_letta.strip()
                keyword_letta = keyword_letta.lower()
                # appendo alla lista
                keywords_list.append(keyword_letta)
                keyword_letta = fK.readline()
            # print(keywords_list)

            # Crea un dizionario inizializzato a zero per ciascuna parola chiave
            dizionario_conta = {keyword: 0 for keyword in keywords_list}
            print("Dizionario iniziale:", dizionario_conta)

            # divido il documento da frasi -> lista di parole
            documento_in_parole = []
            testo = fA.readlines()
            # print("Testo originale:", testo)

            # preparazione del testo
            for frase in testo:

                # pulizia della riga
                frase_pulita = frase.strip()
                # print("frase_pulita:", frase_pulita)

                # gestione riga vuota -> salto
                if frase_pulita == "":
                    continue

                # gestione righe pulite e aggiunta a documento
                frase_pulita = frase_pulita.lower()
                documento_in_parole.extend(frase_pulita.split(" "))

            print("Testo in parole:", documento_in_parole)

            # preparazione delle parole chaive
            keywords_splitted = []
            for keyword in keywords_list:
                keywords_splitted.append(keyword.split(" "))

            print("keywords in parole:", keywords_splitted)

            # scorro  e per ogni parola in "documento_in_parole"
            for i in range(len(documento_in_parole)):
                for parole_keyword in keywords_splitted:
                    j = 0
                    count = 0

                    while j < len(parole_keyword) and (i + j) < len(documento_in_parole):
                        if documento_in_parole[i + j] == parole_keyword[j]:
                            count += 1
                            j += 1
                        else:
                            break

                    if count == len(parole_keyword):
                        chiave = " ".join(parole_keyword)
                        dizionario_conta[chiave] += 1

        # stampa del risultato su file
        with open(Log_path, "w") as log:
            for keyword, count in dizionario_conta.items():
                log.write(f"{keyword}: {count}\n")

    else:
        print("File 'Keyword_path' not found")
else:
    print("File 'toAnalise' not found")
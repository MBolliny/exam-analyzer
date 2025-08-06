import os
import PyPDF2

# versione per keyword - dizionario txt/pdf -> lista di tuple
def TupleCreator_keyword(extension_diz):
    output_list = []

    for nome_file, valore in extension_diz.items():

        if valore == "pdf":
            print(f"non supportati PDF come input per le parole chiave - file {nome_file}")
            continue

        elif valore == "txt":
            with open(nome_file, 'r') as file_obj:
                for riga in file_obj:
                    if riga.strip():
                        output_list.append(tuple(riga.split()))

    return output_list

# versione per keyword - txt/pdf singolo -> lista parole pulite
def ListCreator_document(nome_file, valore):
    output_list = []

    if valore == "pdf":
        try:
            with open(nome_file, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                testo = ""
                for pagina in reader.pages:
                    estratto = pagina.extract_text()
                    if estratto:
                        testo += estratto + " "

                # formattazione del testo
                testo = testo.lower()
                parole_grezze = testo.split()

                # pulizia dalla punteggiatura
                punteggiatura = [".", ",", ";", ":", "!", "?", "(", ")", "\"", "'"]

                for parola in parole_grezze:
                    parola_pulita = parola.strip("".join(punteggiatura))
                    if parola_pulita:
                        output_list.append(parola_pulita)

                return output_list  # ✅ Return specifico per PDF

        except Exception as e:
            print(f"Errore leggendo PDF {nome_file}: {e}")
            return []

    elif valore == "txt":
        print(f"TXT non supportati per questa funzione - file {nome_file}")
        return []
import os
import PyPDF2
from file_manipulation import FileListCreator, extensionFinder, confronto
from list_creation import TupleCreator_keyword, ListCreator_document
from print import print_log_list, print_log_diz, print_log_count

def main():
    # cartelle debug
    toAnalise_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/data/test_documents"
    Keyword_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/data/test_keyword"
    Log_path = "/Users/MatteoBollini/Documents/GitHub/exam-analyzer/output/log.txt"

    # ============ FILE KEYWORD ============

    # acquisisco lista di file contenenti parole chiave
    keyword_file_list = FileListCreator(Keyword_path)

    # dizionario estensioni
    extension_diz_k = extensionFinder(keyword_file_list)

    # lista di tuple
    lista_tuple = TupleCreator_keyword(extension_diz_k)

    # ============ FILE DA ANALIZZARE ============

    # acquisisco lista di file contenenti parole chiave
    document_file_list = FileListCreator(toAnalise_path)

    # dizionario estensioni
    extension_diz_d = extensionFinder(document_file_list)

    # lista di parole pulite da punteggiatura
    dizionario_conta = {}
    for chiave, valore in extension_diz_d.items():
        full_word_list = ListCreator_document(chiave, valore)

        # ============ ANALISI e CONTEGGIO ============

        dizionario_conta = confronto(lista_tuple, full_word_list, dizionario_conta)
        # print(dizionario_conta)

        # stampa del risultato su file
        print_log_count(dizionario_conta, Log_path)

if __name__ == "__main__":
    main()
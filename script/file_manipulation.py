import os
import PyPDF2

# creazione lista di file identificando cartelle e documenti OK
def FileListCreator(path):
    output_list = []

    # ottengo lista degli elementi nel path
    lista_elementi = os.listdir(path)
    # print("lista elementi cartella:", lista_elementi)

    # scorro elementi e verifico se sia file o cartella
    for elemento in lista_elementi:

        # gestione .DS_Store
        if elemento == ".DS_Store":
            # print("è DS_Store")
            continue

        # creo path_file per procedere alla verifica
        path_completo = os.path.join(path, elemento)
        # print(path_completo)

        # è file o folder?
        if os.path.isfile(path_completo):
            # print(f"{elemento} è file")
            output_list.append(path_completo)

        if os.path.isdir(path_completo):
            # print(f"{path_folder} è cartella")
            FileListCreator(path_completo)

    return output_list

# identificatore se .txt o pdf OK
def extensionFinder(file_list):
    extension_diz = {}

    for file_path in file_list:

        # separazione della estensione da nome
        nome_file = os.path.basename(file_path)
        _, estensione = os.path.splitext(nome_file)
        estensione = estensione.lower().strip(".")

        # creazione dizionario con relative estensioni
        extension_diz[file_path] = estensione

    return extension_diz

def confronto(lista_tuple, full_word_list, dizionario_conta):
    for keyword in lista_tuple:
        n = len(keyword)
        keyword_trovata = False

        for i in range(len(full_word_list) - n + 1):
            if tuple(full_word_list[i:i + n]) == keyword:
                keyword_trovata = True
                break

        if keyword_trovata:
            if keyword in dizionario_conta:
                dizionario_conta[keyword] += 1
            else:
                dizionario_conta[keyword] = 1

    return dizionario_conta
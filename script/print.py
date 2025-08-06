import os
import PyPDF2

# LISTE
def print_log_list(list_input, Log_path, type):
    with open(Log_path, "a") as log:

        if type == "k":
            log.write("\nlista file KEYWORD:\n")

        if type == "d":
            log.write("\nlista file DOCUMENT:\n")

        for elemento in list_input:
            log.write(f"{elemento}\n")

# DIZIONARIO
def print_log_diz(diz_input, Log_path, type):
    with open(Log_path, "a") as log:

        if type == "k":
            log.write("\ndizionario file KEYWORD:\n")

        if type == "d":
            log.write("\ndizionario file DOCUMENT:\n")

        for chiave, valore in diz_input.items():
            log.write(f"{chiave}: {valore}\n")

# CONTEGGIO
def print_log_count(dizionario_conta, Log_path):
    with open(Log_path, "a") as log:
        for keyword, count in dizionario_conta.items():
            if isinstance(keyword, tuple):
                keyword_str = " ".join(keyword)
            else:
                keyword_str = str(keyword)
            log.write(f"{keyword_str}: {count}\n")
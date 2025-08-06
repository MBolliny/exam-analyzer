import os
import PyPDF2

# LISTE
def print_log_list(list_input, Log_path):
    with open(Log_path, "w") as log:
        log.write("lista file KEYWORD:")
        for elemento in list_input:
            log.write(elemento)
        log.write("\n")

# DIZ
def print_log_diz(diz_input, Log_path):
    with open(Log_path, "w") as log:
        for chiave, valore in diz_input.items():
            log.write(f"{chiave}: {valore}\n")
        log.write("\n")  # a capo finale

# CONTEGGIO
def print_log_count(dizionario_conta, Log_path):
    with open(Log_path, "w") as log:
        for keyword, count in dizionario_conta.items():
            if isinstance(keyword, tuple):
                keyword_str = " ".join(keyword)
            else:
                keyword_str = str(keyword)
            log.write(f"{keyword_str}: {count}\n")

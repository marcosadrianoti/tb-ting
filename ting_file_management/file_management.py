import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    txt_list = []
    try:
        with open(path_file, 'r') as file:
            for line in file:
                txt_list.append(line.rstrip("\n"))
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
    else:
        return txt_list

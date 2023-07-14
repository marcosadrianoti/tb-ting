import sys
from ting_file_management.queue import Queue


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    queue = Queue()
    txt_list = []
    try:
        with open(path_file, 'r') as file:
            for line in file:
                txt_list.append(line.rstrip("\n"))
                # queue.enqueue
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
    else:
        return txt_list

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    list_txt = txt_importer(path_file)
    queue = instance
    for i in range(len(queue)):
        if queue.search(i)["nome_do_arquivo"] == path_file:
            return
    value = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_txt),
        "linhas_do_arquivo": list_txt
    }
    queue.enqueue(value)
    print(value)


def remove(instance):
    queue = instance
    if len(queue) == 0:
        print('Não há elementos')
        return
    removed = queue.dequeue()
    print(f'Arquivo {removed["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

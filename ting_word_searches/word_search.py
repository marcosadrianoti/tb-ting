def exists_word(word, instance):
    queue = instance
    # {
    #     "nome_do_arquivo": "c:/9.txt",
    #     "linhas_do_arquivo": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    #     "qtd_linhas": 9,
    # }
    final_list = []
    for i in range(0, len(queue) - 1):  # lista principal
        ocorrencias = []
        for j in range(0, queue[i]['qtd_linhas'] - 1):  # lista de linhas
            text_list = queue[i]['linhas_do_arquivo'][j].lower().split()
            if word in text_list:
                ocorrencias.append({'linha': j + 1})
        if ocorrencias:
            final_list.append({
                "palavra": word,
                "arquivo": queue[i]['nome_do_arquivo'],
                "ocorrencias": ocorrencias
                })

    return final_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""

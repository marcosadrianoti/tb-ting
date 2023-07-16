def exists_word(word, instance):
    queue = instance
    final_list = []
    for i in range(len(queue)):
        unic_elem = queue.search(i)
        occurrences = []
        for j in range(unic_elem['qtd_linhas']):  # lista de linhas
            linhas = unic_elem['linhas_do_arquivo'][j]
            text_list = linhas.lower().rstrip('.').split()
            if word in text_list:
                occurrences.append({'linha': j + 1})
        if occurrences:
            final_list.append({
                "palavra": word,
                "arquivo": unic_elem['nome_do_arquivo'],
                "ocorrencias": occurrences
                })

    return final_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""

# Projeto Python TING (Trybe is not Google)! :card_index:
Projeto desenvolvido por mim durante o curso de Desenvolvimento Web na Trybe. Divulgado aqui como portfólio de aprendizado.

<details>
<summary><strong>Objetivos do projeto:</strong></summary>
 
  * Implementar um programa que simule um algoritmo de indexação de documentos similar ao do Google. Seu programa deverá ser capaz de identificar ocorrências de termos em arquivos TXT.
  * Verificar se eu era capaz de:
    * Manipular Pilhas.
    * Manipular Deque.
    * Manipular Nó & Listas Ligadas.
    * Manipular Listas Duplamente Ligadas.
</details>
<details>
<summary><strong> Requisitos do projeto:</strong></summary>

  * Pacote `ting_file_management`
    * Implementar uma fila para armazenar os arquivos que serão lidos.
    * Implementar uma função _txt_importer_ dentro do módulo _file_management_ capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.
    * Implementar a função process no módulo _file_process_. Essa função deverá ser capaz de transformar o conteúdo da lista gerada pela função _txt_importer_ em um dicionário que será armazenado dentro da Queue.
    * Implementar uma função _remove_ dentro do módulo _file_process_ capaz de remover o primeiro arquivo processado
    * Implementar uma função _file_metadata_ dentro do módulo _file_process_ capaz de apresentar as informações superficiais de um arquivo processado.
    * Implementar os testes para a classe _PriorityQueue_ capaz de armazenar arquivos pequenos de forma prioritária
  * Pacote `ting_word_searches`
    * Implementar uma função _exists_word_, dentro do módulo _word_search_, que verifique a existência de uma palavra em todos os arquivos processados.
    * Implementar uma função _search_by_word_ dentro do módulo _word_search_, que busque uma palavra em todos os arquivos processados.
</details>
  
## Rodando o projeto localmente

Para rodar o projeto em sua máquina, abra seu terminal, crie um diretório no local de sua preferência com o comando `mkdir` e acesse o diretório criado com o comando `cd`:

```bash
mkdir meu-diretorio &&
cd meu-diretorio
```

Clone o projeto com o comando `git clone`:

```bash
git clone git@github.com:marcosadrianoti/tb-algorithms.git
```

Acesse o diretório do projeto com o comando `cd`:

```bash
cd tb-algorithms
```

crie o ambiente virtual:
```bash
python3 -m venv .venv
```

Ative o ambiente virtual:
```bash
source .venv/bin/activate
```

Instale as dependências no ambiente virtual:
```bash
python3 -m pip install -r dev-requirements.txt
```

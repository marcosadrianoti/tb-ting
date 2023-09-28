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

  * Número de estudantes estudando no mesmo horário (_Algoritmo de busca_)
    * Retornar, para uma entrada específica, a quantidade de estudantes presentes.
    * Retornar `None` se em `permanence_period` houver alguma entrada inválida.
    * Retornar `None` se `target_time` recebe um valor vazio.
    * A função deverá, por meio de análise empírica, se comportar como no máximo `O(n)` - _complexidade assintótica linear_
  * Criptografia de inversões (_Testes_)
    * Implementar adequadamente o teste para a função `encrypt_message`.
  * Palíndromos (_Recursividade_)
    * Retornar `True` se a palavra passada por parâmetro for um palíndromo.
    * Retornar `False` se a palavra passada por parâmetro não for um palíndromo.
    * Retornar `False` se nenhuma palavra for passada por parâmetro.
  * Anagramas (_Algoritmo de ordenação_)
    * Retornar `True` se as palavras passadas forem anagramas.
    * Retornar `False` se as palavras passadas por parâmetro não forem anagramas.
    * Retornar `false` se alguma das palavras passadas por parâmetro for uma string vazia.
    * A função deverá, por meio de análise empírica, se comportar como no máximo `O(n log n)` - _complexidade assintótica linearítmica_
    * Retornar `True` se as palavras passadas forem anagramas sem diferenciar maiúsculas e minúsculas.
  * Requisitos Bônus:
    * Encontrando números repetidos (_Algoritmo de busca_)
      * Retornar o número repetido se a função receber como parâmetro uma lista com números repetidos.
      * Retornar `False` se a função não receber nenhum parâmetro.
      * Retornar `False` se a função receber, como parâmetro, uma string.
      * Retornar `False` se a função receber, como parâmetro, uma lista sem números repetidos.
      * Retornar `False` se a função receber, como parâmetro, apenas um valor.
      * Retornar `False` se a função receber, como parâmetro, um número negativo.
      * A função deverá, por meio de análise empírica, se comportar como no máximo `O(n log n)` - _complexidade assintótica linearítmica_
    * Palíndromos (_Iteratividade_)
      * Retornar `True` se a palavra passada como parâmetro for um palíndromo, executando uma função iterativa.
      * Retornar `False` se a palavra passada como parâmetro não for um palíndromo, executando uma função iterativa.
      * Retornar `False` se nenhuma palavra for passada como parâmetro, executando uma função iterativa.
      * A função deverá, por meio de análise empírica, se comportar como no máximo `O(n)` - _complexidade assintótica linear_
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

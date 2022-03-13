---
title: Get Started
sidebar: true
sidebarlogo: logo_snake
---


Pythonlings é um utilitário para ajudar iniciantes a aprender Python através de exercícios, em uma variedade de temas!

## Escolha sua linguagem

Atualmente, as seguintes linguagens são suportadas:

- en (default)
- pt

Para escolher sua linguagem, apenas exporte `PYTHONLINGS_LANGUAGE` com a sigla da palavra desejada:

Exemplo:


    export PYTHONLINGS_LANGUAGE=pt


## Uso

Inicie o ambiente com poetry:

    poetry install
    poetry shell

Após a instalação das dependências e as pre-configurações padrões serem aplicadas, você poderá executar a ferramenta:

    python -m pythonlings start

Com isso, os exemplos começarão a ser executados em ordem tópico a tópico, os arquivos de exemplos estarão contidos dentro de `pythonlings/exercises`, você deverá fazer com que os arquivos sejam executados **sem problemas** corrigindo-os para que passem nos testes, remova a linha de comentário `# I AM NOT DONE` do exercício atual para que o Pythonlings o execute.

### Comandos

```
usage: __main__.py [-h] {start,exec} ...

Pythonlings é um utilitário para ajudar iniciantes a aprender Python através de exercícios, em uma variedade de temas!

positional arguments:
  {start,exec}
    start       Inicia o Pythonlings! Executando e assistindo os arquivos de exercício em ordem.
    exec        Executa apenas um exercicio, você apenas deve prover o caminho relativo ou absoluto do arquivo do exercicio.

optional arguments:
  -h, --help    show this help message and exit
```

## Desenvolvimento

Para os desenvolvedores, inicialmente execute `poetry install` para ter um ambiente local isolado.

## Tests

    poetry run pytest


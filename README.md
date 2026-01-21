# 🏰 Quiz de Hogwarts em Python

---

## - Nome e tema do projeto

- Nome do projeto: Quiz de Hogwarts  
- Tema: Jogo de perguntas e repostas com base em Harry Potter, finalidade de descubrir sua casa em Hogwarts com base na reposta do Quiz.

Este Quiz foi criado para a diciplina de Introdução à logica e programação, seguindo o roteiro do professor, incluindo mamipulação de arquivos, tratamentos de erros, modurarização do código, uso de biblioteca padrão e degradação de saidas persistentes.

---

## - Objetivo do Projeto

O objetivo desse Projeto é desenvolver uma aplicação prática de Python que mostre o dominio do conteudo estudados ao longo da diciplina. Quiz via terminal, a pessoa respoder a perguntas de multipla escolha, ao final, recebe o resultado da sua casa em Hogwarts ao qual possui mais objetivo.

O Quiz foi criado com propósito de aplicar conceitos da diciplina, como estruturas de repetição, funções, organizações de codigo, leitura e escrita de arquivos, estruturas de condicionnais e tratamento adequequado de exeções.

---

## - Descrição e Funcionalidades

O sistema de as funcionalidades:

- Leitura de perguntas no arquivo JSON, facilitando a organização do conteudo;
- Interação com pessoa através do terminal, permitindo responder a sperguntas do Quiz;
- Cálculo automática de qual a seua casa em Hogwarts (Grifinória, Sonserina, Corvinal e Lufa-Lufa);
- Resultado final da sua casa em Hogwarts com pontuação;
- Geração automatica de um arquivo TXT, tendo:
  - Casa sorteada;
  - Pountução das casas;
  - Histórico de perguntas e reposta;
  - Data e horário de execução do Quiz;
- Tratamentos de erros:
  - Arquivo de perguntas do Quiz não encontradas;
  - Erros do arquivo em leitura JSON;
  - Entradas inválidas da pessoa;
- Código organizado em funções, de acordo com a prática da programação;
- Limpeja da tela para melhora a experiência da pessoa durante a prática do Quiz;

---

## - Estrutura do Projeto

A organização do arquivo do Quiz:

quiz/
│
├── data/
│ └── perguntas.json
│
├── resultados/
│ └── relatorio_27-12-2025_14-11.txt
│
├── harry.py
│
└── README.md


- data/: contém o arquivo JSON com as perguntas do Quiz;
- resultados/: pasta onde são guardados os relatórios gerados após o termino do Quiz;
- harry.py: arquivo principal do Quiz, contendo todo sua lógica;
- README.md: documentação completa do Quiz;

---

## - Instruções de execução

Para executar o Projeto:

- instalar Python 3.10;
- Faça o clone do repositório ou baixer os arquivos do projeto;
- Abra o terminal na raiz do projeto;
- Execute o comando:

python harry.py


- Pressione ENTER para da inicio ao Quiz;
- Responda as perguntas digitando o número correspondente a alternativa escolhida;
- Ao final do Quiz, o resultado será mostrado no terminal e um relatório será salvo automaticamente no arquivo da pasta;

---

## - Bibliotecas Utilizadas

O projeto utiliza bibliotecas de Python:

- json: leitura e manipulação de arquivos de perguntas;
- pathlib: manipulação de caminho e diretórios;
- datetime: geração de data e hora para o relatório;
- os: comando do sistema operacional;
- platform: identificação do sistema operacinal do computador para a limpeja da tela.

Não é necessária a instalação de bibliotecas externas.

---

## - Relatório Gerado

Ao final do Quiz, o sistema gera automaticmente um arquivo em TXT:

- Título do Relatório;
- Casa de Hogwarts sorteada;
- Pontuação detalhada da casa em Hogwarts;
- Histórico da perguntas e respostas;
- Data e horário de execução do Quiz.

---

## - Integrante do grupo

Projeto desenvolvido individualmente por:

- Andreza Pereira da Silva

---

## - Consideração finais

O Quiz de Hogwarts é um projeto funcional, mostrar de forma prática a aplicação dos conceitos aprendidos durante a diciplina. O sistema inclui tratamentos de erros, moduralização, uso de arquivos, documentação adequada e clareza de código.

O projeto permite futuras expansões, como a inclusão de novas perguntas, melhorias de interação com a pessoa ou até a implementação de uma interface gráfica.

Canva: 
https://www.canva.com/design/DAG-lsGKJtE/JkQYoW4Fk4m_rs5lUIZ45w/edit?utm_content=DAG-lsGKJtE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton




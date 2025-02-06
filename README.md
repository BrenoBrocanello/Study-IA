# StudyIA

Esse projeto é meu primeiro projeto pessoal após a transição de biólogo para T.I, tenho muito a melhorar ainda.


StudyIA é um programa que pode auxiliar na organização e otimização dos estudos, criando cronogramas personalizados e fornecendo conteúdo detalhado com base em editais de concursos ou informações fornecidas diretamente pelo usuário. Utilizando inteligência artificial da OpenAI, o sistema gera planos de estudo e conteúdo acadêmico aprofundado, com explicações e exercícios práticos.

## Funcionalidades

- **Importação de Edital**: O usuário pode importar um arquivo PDF de edital, e o sistema utiliza a API da OpenAI para extrair as informações relevantes (data da prova e conteúdo da prova).
- **Criação de Cronograma Personalizado**: Com base no edital ou nas informações fornecidas pelo usuário, o aplicativo gera um cronograma detalhado de estudo, respeitando os horários disponíveis para estudo.
- **Geração de Conteúdo Detalhado**: O sistema gera conteúdo sobre tópicos específicos de estudo, com explicações aprofundadas e questões de múltipla escolha.
- **Interface Gráfica**: A aplicação possui uma interface gráfica que facilita a seleção do arquivo de edital e interação com o usuário.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do aplicativo.
- **OpenAI API**: Utilizada para gerar conteúdos personalizados e cronogramas de estudo.
- **PyMuPDF (fitz)**: Usada para manipulação e extração de texto de arquivos PDF (editais).
- **Tkinter**: Utilizado para criar a interface gráfica de seleção de arquivos PDF.
- **Datetime**: Para manipulação de datas e horas.

## Como Rodar o Projeto

### Requisitos

1. Python 3.x instalado.
2. Chave da OpenAI para utilizar a API.

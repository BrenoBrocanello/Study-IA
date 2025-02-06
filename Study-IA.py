
import openai  # Esta biblioteca é utilizada para interagir com a API da OpenAI, permitindo gerar textos, extrair informações e criar conteúdo com base nas solicitações do usuário, como no caso da criação do cronograma de estudo.
import fitz  # A biblioteca "fitz" faz parte do PyMuPDF e é utilizada para ler e manipular arquivos PDF. No código, ela é responsável por abrir e extrair o texto do arquivo PDF do edital fornecido pelo usuário.
from datetime import datetime  # A biblioteca datetime fornece classes para manipulação de datas e horas. No código, é usada para capturar a data atual (data_hoje) e formatá-la em um formato legível (dd/mm/aaaa).
import tkinter as tk  # A biblioteca tkinter é utilizada para criar interfaces gráficas (GUIs) no Python. Aqui, ela é usada para criar a janela de seleção de arquivo para que o usuário possa importar o PDF do edital.
from tkinter import filedialog  # O módulo filedialog da biblioteca tkinter é responsável pela criação de caixas de diálogo para seleção de arquivos. No código, ele é usado para permitir que o usuário selecione o arquivo PDF do edital a ser importado para processamento.


openai.api_key = '' # Insira sua chave OPENAI entre as ' '

data_hoje = datetime.now().strftime("%d/%m/%Y")

def extrair_informacoes_openai(texto_pdf):
    prompt = (
        f"Analise o seguinte texto de um edital e extraia as informações mais importantes sobre a data da prova e o conteúdo da prova.\n\n"
        f"Texto do edital:\n{texto_pdf}\n\n"
        f"Por favor, forneça a data da prova e o conteúdo da prova de maneira clara e objetiva."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=16000,
        )
        resultado = response['choices'][0]['message']['content']
        return resultado
    except Exception as e:
        return f"Ocorreu um erro ao processar o edital: {str(e)}"

def gerar_conteudo(data_prova, conteudo_prova, horarios, texto_pdf=""):
    prompt = (
        f"Hoje é {data_hoje}. "
        f"Com base nas informações do edital do concurso, o resumo é: {texto_pdf}. "
        f"A data da prova está marcada para {data_prova}, e o conteúdo da prova abrange os seguintes tópicos: {conteudo_prova}. "
        f"O usuário tem os seguintes horários disponíveis para estudar: {horarios}. É importante seguir rigorosamente esses horários, pois são os únicos períodos disponíveis para estudo. "
        f"Com essas informações, crie um cronograma detalhado de estudo, formatado como uma tabela. "
        f"A tabela deve incluir: "
        f"- Distribuição dos conteúdos entre teoria, prática e revisão. "
        f"- Dias e horas específicos para cada bloco de estudo, respeitando os horários fornecidos. "
        f"- Cada bloco de estudo deve ser equilibrado, com intervalos para descanso, de acordo com a carga horária disponível. "
        f"- O cronograma deve ser prático e viável, considerando que o usuário tem apenas os horários mencionados para se dedicar aos estudos. "
        f"Organize o cronograma por períodos de dias, detalhando as atividades e os tópicos a serem estudados em cada sessão de estudo."

    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=16000,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Ocorreu um erro ao gerar o conteúdo: {str(e)}"

def ler_pdf(caminho_pdf):
    try:
        doc = fitz.open(caminho_pdf)
        texto_completo = ""
        for pagina in doc:
            texto_completo += pagina.get_text()
        return texto_completo
    except Exception as e:
        return f"Ocorreu um erro ao ler o PDF: {str(e)}"

def selecionar_arquivo_pdf():
    root = tk.Tk()
    root.withdraw()
    caminho_pdf = filedialog.askopenfilename(
        title="Selecione o arquivo PDF do edital",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    return caminho_pdf

def gerar_conteudo_desejado(topico_estudo):
    prompt = (
        f"Com base no tópico de estudo fornecido: {topico_estudo}, crie um conteúdo abrangente e detalhado, utilizando o máximo de tokens permitido. O conteúdo deve ser elaborado de forma profissional, com uma abordagem acadêmica, como se fosse apresentado por um professor universitário. "
        f"Inclua explicações aprofundadas sobre todos os aspectos relevantes do tópico, com exemplos práticos, quando apropriado, para ilustrar os conceitos. "
        f"Após a explicação, forneça 5 questões de múltipla escolha sobre o tópico. "
        f"As questões devem cobrir diferentes níveis de dificuldade, começando com questões básicas e progredindo para questões mais avançadas. "
        f"Certifique-se de que as perguntas sejam claras e bem formuladas, e inclua o gabarito apenas ao final, após todas as questões."

    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=16000,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Ocorreu um erro ao gerar o conteúdo desejado: {str(e)}"

def main():
    print("Bem-vindo ao StudyIA!")

    while True:
        tem_edital = input("Você tem um arquivo de edital para importar? (Sim/Não): ").strip().lower()

        if tem_edital == "sim":
            caminho_pdf = selecionar_arquivo_pdf()

            # Ler o conteúdo do PDF
            texto_pdf = ler_pdf(caminho_pdf)

            # Extração de informações através da API
            print("Aguarde, estamos carregando... (Processando o edital)")
            informacoes_extraidas = extrair_informacoes_openai(texto_pdf)

            print("\nInformações extraídas do edital:\n")
            print(informacoes_extraidas)

            # Agora pedimos apenas os horários de estudo
            horarios = input("\nQuais horários você tem disponíveis para estudar? = ")
            print('Aguarde, estamos carregando... (Gerando cronograma)')

            # Gerar o cronograma com as informações extraídas e os horários fornecidos
            conteudo_gerado = gerar_conteudo(informacoes_extraidas, horarios, texto_pdf)
            print("\nPlano de Estudos Gerado:\n")
            print(conteudo_gerado)

            # Perguntar o que o usuário deseja estudar
            topico_estudo = input("\nO que você deseja estudar? (Escreva o tópico que você quer estudar): ")

            # Gerar o conteúdo detalhado do tópico escolhido
            print('Aguarde, estamos carregando... (Gerando conteúdo do tópico escolhido)')
            conteudo_detalhado = gerar_conteudo_desejado(topico_estudo)
            print("\nConteúdo Detalhado Gerado para o Tópico Selecionado:\n")
            print(conteudo_detalhado)

            # Perguntar se o usuário quer estudar outra coisa
            continuar = input("\nDeseja estudar outra coisa? (Digite 'exit' para encerrar ou pressione Enter para continuar): ").strip().lower()
            if continuar == "exit":
                print("Obrigado por usar o StudyIA! Até a próxima.")
                break


        else:
            print("Você não forneceu um edital, mas podemos criar um plano de estudos manualmente.")

            # Perguntar sobre o dia da prova
            data_prova = input("\nQual o dia da sua prova? (Digite a data no formato DD/MM/AAAA): ")

            # Perguntar os horários de estudo
            horarios = input("\nQuais horários você tem disponíveis para estudar? = ")

            # Perguntar sobre o conteúdo da prova
            conteudo_prova = input("\nQual o conteúdo da prova? ")

            # Gerar o cronograma com os dados fornecidos
            print('Aguarde, estamos carregando... (Gerando cronograma)')

            # Gerar o cronograma com as informações fornecidas manualmente
            conteudo_gerado = gerar_conteudo(data_prova, conteudo_prova, horarios)

            print("\nPlano de Estudos Gerado:\n")
            print(conteudo_gerado)

            # Perguntar o que o usuário deseja estudar
            topico_estudo = input("\nO que você deseja estudar? (Escreva o tópico que você quer estudar): ")

            # Gerar o conteúdo detalhado do tópico escolhido
            print('Aguarde, estamos carregando... (Gerando conteúdo do tópico escolhido)')
            conteudo_detalhado = gerar_conteudo_desejado(topico_estudo)

            print("\nConteúdo Detalhado Gerado para o Tópico Selecionado:\n")
            print(conteudo_detalhado)

            # Perguntar se o usuário quer estudar outra coisa
            continuar = input("\nDeseja estudar outra coisa? (Digite 'exit' para encerrar ou pressione Enter para continuar): ").strip().lower()
            if continuar == "exit":
                print("Obrigado por usar o StudyIA! Até a próxima.")
                break


if __name__ == "__main__":
    main()
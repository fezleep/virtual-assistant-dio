# virtual assistant dio

um assistente virtual simples feito em python para o desafio da dio.

a ideia do projeto é juntar fala, texto e alguns comandos pequenos em uma base fácil de entender. ele não tenta ser uma alexa completa. é um primeiro passo para estudar speech to text, text to speech e automações simples com python.

## objetivo

criar um assistente virtual que consiga:

- transformar texto em áudio
- tentar transformar fala em texto
- entender comandos básicos
- abrir o youtube
- pesquisar na wikipedia
- informar o horário atual
- abrir uma busca por farmácia próxima
- funcionar também só com texto, sem depender de microfone

## como funciona

o projeto tem dois arquivos principais:

- `src/assistant.py`: roda o assistente, cuida da fala, do áudio e do modo texto
- `src/commands.py`: concentra a lógica dos comandos

por padrão, o assistente roda em modo texto. isso deixa o projeto mais simples de testar em qualquer computador e também evita problemas comuns com microfone.

o modo por voz existe, mas é opcional. ele depende do ambiente local, permissões de microfone e configuração do sistema.

## text to speech

para transformar texto em áudio, usei a biblioteca `gtts`.

ela gera um arquivo `output.mp3` com a resposta do assistente:

```python
from gtts import gTTS

tts = gTTS("olá, eu sou seu assistente virtual", lang="pt-br")
tts.save("output.mp3")
```

o projeto salva o áudio, mas não obriga nenhuma biblioteca específica para tocar o arquivo. isso deixa a solução mais simples e mais fácil de rodar em ambientes diferentes.

## speech to text

para tentar transformar fala em texto, usei `SpeechRecognition`.

essa parte depende de microfone e funciona melhor em ambiente local. no google colab, o foco fica em text to speech e simulação de comandos por texto.

se o microfone não funcionar, o assistente orienta a usar o modo texto.

## comandos disponíveis

alguns exemplos de comandos:

- `youtube`
- `pesquisar python na wikipedia`
- `wikipedia inteligência artificial`
- `horário`
- `que horas são`
- `farmácia próxima`
- `sair`

## como rodar no colab

o notebook está em:

```text
notebooks/virtual_assistant_colab.ipynb
```

no colab, a proposta é testar:

- instalação das bibliotecas
- geração de áudio com `gtts`
- comandos por texto
- pesquisa na wikipedia
- abertura de links

o speech to text com microfone fica como observação, porque o colab não é o melhor ambiente para isso.

## como rodar localmente

crie um ambiente virtual, instale as dependências e rode o assistente:

```bash
python -m venv .venv
```

no windows:

```bash
.venv\Scripts\activate
```

no linux ou mac:

```bash
source .venv/bin/activate
```

instale as libs:

```bash
pip install -r requirements.txt
```

rode em modo texto:

```bash
python src/assistant.py --mode text
```

para tentar usar voz:

```bash
python src/assistant.py --mode voice
```

## observações importantes

- o modo texto é o caminho principal do projeto
- o modo voz pode falhar se não houver microfone configurado
- o áudio gerado fica em `output.mp3`
- arquivos `.mp3` e `.wav` ficam fora do git por causa do `.gitignore`
- o projeto evita dependências obrigatórias como `pyaudio`, `playsound` e bibliotecas específicas do windows

## prints do projeto

sugestões de prints para colocar na entrega:

- execução do assistente no terminal em modo texto
- arquivo `output.mp3` gerado
- notebook rodando no google colab
- resultado de uma pesquisa na wikipedia
- navegador abrindo youtube ou busca por farmácia próxima

os prints podem ser colocados depois na pasta `README-assets/`.

## aprendizados

nesse projeto eu pratiquei:

- organização de um projeto python simples
- separação de responsabilidades entre arquivos
- uso de `gtts` para gerar áudio
- uso de `SpeechRecognition` para reconhecer fala
- criação de comandos básicos
- automações simples com `webbrowser`
- adaptação do projeto para rodar também no google colab

## próximos passos

algumas ideias para evoluir:

- melhorar a interpretação dos comandos
- adicionar mais respostas
- salvar histórico de comandos
- criar uma interface simples
- integrar com outras apis
- permitir escolha do nome do assistente

## conclusão

esse assistente é uma versão inicial, simples e funcional. ele mostra como juntar fala, texto e automações pequenas em python sem deixar o projeto pesado ou difícil de rodar.

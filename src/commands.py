from datetime import datetime
from urllib.parse import quote_plus
import webbrowser

import wikipedia


wikipedia.set_lang("pt")


def _extract_wikipedia_term(command: str) -> str:
    text = command.lower().strip()

    for prefix in (
        "pesquisar",
        "pesquise",
        "buscar",
        "busque",
        "wikipedia",
        "na wikipedia",
        "no wikipedia",
    ):
        text = text.replace(prefix, " ")

    return " ".join(text.split())


def handle_command(command: str) -> tuple[str, bool]:
    """
    recebe um comando em texto e devolve:
    - resposta do assistente
    - se o programa deve continuar rodando
    """
    command = command.lower().strip()

    if not command:
        return "não entendi. tenta escrever um comando.", True

    if command in ("sair", "encerrar", "parar", "fechar"):
        return "certo, encerrando o assistente.", False

    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "abrindo o youtube.", True

    if "horário" in command or "horario" in command or "que horas" in command:
        current_time = datetime.now().strftime("%H:%M")
        return f"agora são {current_time}.", True

    if "farmácia" in command or "farmacia" in command:
        search_url = "https://www.google.com/search?q=farm%C3%A1cia+pr%C3%B3xima"
        webbrowser.open(search_url)
        return "abrindo uma busca por farmácia próxima.", True

    if "wikipedia" in command or "pesquisar" in command or "pesquise" in command:
        term = _extract_wikipedia_term(command)

        if not term:
            return "me diga o que você quer pesquisar na wikipedia.", True

        try:
            summary = wikipedia.summary(term, sentences=2, auto_suggest=False)
            return summary, True
        except wikipedia.exceptions.DisambiguationError as error:
            options = ", ".join(error.options[:3])
            return f"encontrei mais de um resultado. tenta ser mais específico. opções: {options}.", True
        except wikipedia.exceptions.PageError:
            url = f"https://pt.wikipedia.org/wiki/Special:Search?search={quote_plus(term)}"
            webbrowser.open(url)
            return "não encontrei um resumo direto, então abri a busca na wikipedia.", True
        except Exception:
            return "não consegui pesquisar na wikipedia agora. tenta de novo em alguns instantes.", True

    return "ainda não sei responder esse comando.", True

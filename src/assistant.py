import argparse
from pathlib import Path

from gtts import gTTS
import speech_recognition as sr

from commands import handle_command


AUDIO_FILE = Path("output.mp3")


def speak(text: str, audio_file: Path = AUDIO_FILE) -> None:
    """gera um mp3 com a resposta do assistente."""
    print(f"assistente: {text}")

    try:
        tts = gTTS(text=text, lang="pt-br")
        tts.save(str(audio_file))
        print(f"áudio salvo em: {audio_file}")
    except Exception as error:
        print(f"não consegui gerar o áudio agora: {error}")


def listen() -> str | None:
    """tenta ouvir o usuário pelo microfone."""
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("ouvindo... fale um comando.")
            recognizer.adjust_for_ambient_noise(source, duration=0.8)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)

        text = recognizer.recognize_google(audio, language="pt-BR")
        print(f"você disse: {text}")
        return text

    except sr.WaitTimeoutError:
        print("não ouvi nada. tenta novamente ou use o modo texto.")
    except sr.UnknownValueError:
        print("não consegui entender a fala. tenta falar de novo ou use o modo texto.")
    except sr.RequestError:
        print("não consegui acessar o serviço de reconhecimento de fala.")
    except Exception as error:
        print(f"não consegui usar o microfone: {error}")
        print("dica: rode com --mode text para usar sem microfone.")

    return None


def run_text_mode() -> None:
    speak("olá, eu sou seu assistente virtual. digite um comando para começar.")

    keep_running = True
    while keep_running:
        command = input("\nvocê: ")
        response, keep_running = handle_command(command)
        speak(response)


def run_voice_mode() -> None:
    speak("olá, eu sou seu assistente virtual. vou tentar ouvir seus comandos.")

    keep_running = True
    while keep_running:
        command = listen()

        if command is None:
            typed_command = input("digite um comando ou pressione enter para tentar voz de novo: ")
            command = typed_command if typed_command else None

        if command is None:
            continue

        response, keep_running = handle_command(command)
        speak(response)


def main() -> None:
    parser = argparse.ArgumentParser(description="assistente virtual simples em python")
    parser.add_argument(
        "--mode",
        choices=("text", "voice"),
        default="text",
        help="modo de uso do assistente. o padrão é text.",
    )
    args = parser.parse_args()

    if args.mode == "voice":
        run_voice_mode()
    else:
        run_text_mode()


if __name__ == "__main__":
    main()

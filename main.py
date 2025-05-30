from module.module_audio_to_text import AudioToTextCorrector
from module.module_speaker import Speaker
from ollama import chat, ChatResponse

# モデル名
OLLAMA_MODEL = 'gemma3:4b'

# 音声読み上げクラスを初期化
speaker = Speaker()

def ask_ollama(prompt: str) -> str:
    try:
        response: ChatResponse = chat(model=OLLAMA_MODEL, messages=[
            {
                'role': 'user',
                'content': prompt,
            }
        ])
        return response.message.content.strip()
    except Exception as e:
        print(f"Ollamaエラー: {e}")
        return "エラーが発生しました。"

def main():
    audio_to_text = AudioToTextCorrector("config.json")

    while True:
        corrected_text = audio_to_text.record_and_correct(timeout_seconds=10)

        if corrected_text is None:
            print("終了条件に達したため、ループを抜けます。")
            break

        print("\n【認識・補正したテキスト】")
        print(corrected_text)

        # Ollamaへ質問
        ollama_reply = ask_ollama(corrected_text)

        print("\n【gemma3:4bの返答】")
        print(ollama_reply)

        # 読み上げ
        speaker.speak(ollama_reply)

if __name__ == "__main__":
    main()


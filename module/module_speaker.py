import pyttsx3
import emoji
import re

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        # 音量やスピード、声の設定があればここで行える
        self.engine.setProperty("rate", 170)  # 話すスピード（デフォルト=200）
        self.engine.setProperty("volume", 1.0)  # 音量（0.0～1.0）

    def remove_emoji(self, text: str) -> str:
        return emoji.replace_emoji(text, replace='')

    def speak(self, text: str):
        clean_text = self.remove_emoji(text)
        clean_text = re.sub(r"[*_`~^]", "", clean_text)  # マークアップ記号を除去
        print("\n【読み上げるテキスト】")
        print(clean_text)

        # 1文ずつ話すことで安定性を向上
        sentences = re.split(r"(?<=[。！？\n])", clean_text)
        for sentence in sentences:
            if sentence.strip():
                self.engine.say(sentence.strip())
        self.engine.runAndWait()


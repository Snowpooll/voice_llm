import time
from module.module_whisper import FasterWhisperModel
from module.module_recorder import Recorder
from ollama_text_correction import OllamaTextCorrector

class AudioToTextCorrector:
    def __init__(self, config_file_path="config.json"):
        self.recorder = Recorder()
        self.faster_whisper_model = FasterWhisperModel()
        self.text_corrector = OllamaTextCorrector(config_file_path)
    
    def record_and_correct(self, timeout_seconds=10):
        """
        音声を録音して、文字起こしして、自然な日本語に補正したテキストを返す。
        無音やtimeoutになった場合はNoneを返す。
        """

        start_time = time.time()
        audio_data = self.recorder.speech2audio()

        if time.time() - start_time >= timeout_seconds:
            print(f"{timeout_seconds}秒間音声が入力されなかったため、処理を終了します。")
            return None

        if audio_data is None:
            print("無音状態が続いたため、処理を終了します。")
            return None

        text = self.faster_whisper_model.audio2text(audio_data)
        corrected_text = self.text_corrector.correct_text(text)

        return corrected_text

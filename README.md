# voice_llm
faster-whisper でマイクから取得した音声を文字起こしして  
Ollamaへ渡します。  
デフォルトでは Gemma3 4B で動作します。  
処理結果を pyttsx3 へ渡すことで音声で結果を読み上げします。  
10秒間何も入力がないと動作が終了します。

## 動作環境
M1 MacbookAir 16GB で動作しています  

使用にあたり 
`pip install -r requirements.txt` を実行後  
https://ollama.com/download  
からOllama をダウンロードしインストール後に  
`ollama pull gemma3:4b`を実行しすることで gemma3 4B が使えるようになります

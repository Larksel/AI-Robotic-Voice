import wave
from piper.voice import PiperVoice

# O modelo deve ser baixado com python -m piper.download_voices pt_BR-cadu-medium

# Carrega o modelo de voz
voice = PiperVoice.load("./pt_BR-cadu-medium.onnx")

# Texto a ser convertido em fala
text = "Olá, mundo! Esta é uma demonstração da qualidade de voz do Piper."

# Define o nome do arquivo de saída
output_file_path = "saida_piper.wav"

# Usa um bloco 'with' para garantir que o arquivo seja fechado corretamente
with wave.open(output_file_path, "wb") as wav_file:
    voice.synthesize_wav(text, wav_file)

print(f"Áudio salvo em: {output_file_path}")
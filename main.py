import wave
from piper import SynthesisConfig
from piper.voice import PiperVoice

# O modelo deve ser baixado com python -m piper.download_voices pt_BR-cadu-medium

# Carrega o modelo de voz
voice = PiperVoice.load("./pt_BR-cadu-medium.onnx")

# Configuração
syn_config = SynthesisConfig(
    volume=1,  # how loud it is
    length_scale=1.0,  # slowness
    noise_scale=1.0,  # audio variation
    noise_w_scale=1.0,  # speaking variation
    normalize_audio=False, # use raw audio from voice
)

# Texto a ser convertido em fala
text = "Olá, mundo! Esta é uma demonstração da qualidade de voz do Piper."

# Define o nome do arquivo de saída
output_file_path = "saida_piper.wav"

# For streaming, use PiperVoice.synthesize
# for chunk in voice.synthesize("..."):
#     set_audio_format(chunk.sample_rate, chunk.sample_width, chunk.sample_channels)
#     write_raw_data(chunk.audio_int16_bytes)

# Usa um bloco 'with' para garantir que o arquivo seja fechado corretamente
with wave.open(output_file_path, "wb") as wav_file:
    voice.synthesize_wav(text, wav_file, syn_config=syn_config)

print(f"Áudio salvo em: {output_file_path}")
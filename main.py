import wave
from piper import SynthesisConfig
from piper.voice import PiperVoice
import sounddevice as sd
import numpy as np

# * O modelo deve ser baixado com python -m piper.download_voices pt_BR-cadu-medium

# Carrega o modelo de voz
voice = PiperVoice.load("./pt_BR-cadu-medium.onnx")
output_file_path = "saida_piper.wav"

# Configuração da síntese
syn_config = SynthesisConfig(
    volume=1,  # how loud it is
    length_scale=1.0,  # slowness
    noise_scale=0.0,  # audio variation
    noise_w_scale=0.0,  # speaking variation
    normalize_audio=False,  # use raw audio from voice
)


def get_user_input():
    return input("Digite o que quer falar: ")


def speak(text: str):
    # Usa um bloco 'with' para garantir que o arquivo seja fechado corretamente
    with wave.open(output_file_path, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file, syn_config=syn_config)
    print(f"Áudio salvo em: {output_file_path}")


def speak_stream(text: str):
    # For streaming, use PiperVoice.synthesize
    for chunk in voice.synthesize(text):
        # Loop principal: pega um chunk do gerador e escreve no stream
        audio_data = np.frombuffer(chunk.audio_int16_bytes, dtype=np.int16)
        with sd.OutputStream(
            samplerate=chunk.sample_rate, channels=chunk.sample_channels, dtype="int16"
        ) as stream:
            stream.write(audio_data)


if __name__ == "__main__":
    try:
        print("Iniciando a reprodução de áudio em stream...")
        print("Pressione Ctrl+C para parar.\n\n")
        while True:
            text = get_user_input()
            text = text.replace('.', ',') # Evita pausas longas
            if text.lower() in ["sair", "exit", "quit"]:
                break
            speak_stream(text)
    except KeyboardInterrupt:
        print("\nReprodução interrompida pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

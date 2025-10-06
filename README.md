# AI Robotic Voice

Repositório para testar geração de áudio a partir de texto com modelos locais e aplicação de efeitos em tempo real.

## Configuração do Ambiente

1. **Instale as dependências:**

    ```bash
    uv sync
    ```

1. **Baixe o Modelo de Voz:**

    Este projeto requer o modelo de voz "Cadu" (pt-BR). Execute o seguinte comando na raiz do projeto

    ```bash
    .\.venv\Scripts\activate
    python -m piper.download_voices pt_BR-cadu-medium
    ```

## Como Executar

Execute o script principal:

```bash
uv run main.py
```

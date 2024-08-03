import re
import unicodedata


# Função de Sanitização de texto.
def sanitize_text(word: str) -> str:
    # Normaliza o texto para decompor caracteres acentuados
    word = unicodedata.normalize('NFKD', word)
    # Remove diacríticos, como acentos
    word = ''.join(c for c in word if not unicodedata.combining(c))
    # Mantém apenas caracteres alfanuméricos, pontos e o sinal de '@'
    word = re.sub(r'[^a-zA-Z0-9.@]', '', word)
    return word.lower()
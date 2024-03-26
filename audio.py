from config import model


def extract_text(audio_path):
    result = model.transcribe(audio_path, language="uk", fp16=False,
                              prompt="Розмовляє абонент з оператором кол-центру. Зроби максимально якісну транскрибацію діалогу")
    return result

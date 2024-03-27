from config import model, speech_config
import azure.cognitiveservices.speech as speechsdk


def extract_text(audio_path):
    result = model.transcribe(audio_path, language="uk", fp16=False)
    return result


def text_to_speech(message, file_name):
    # The neural multilingual voice can speak different languages based on the input text.
    speech_config.speech_synthesis_voice_name = 'uk-UA-PolinaNeural'
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True, filename=file_name)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    speech_synthesis_result = speech_synthesizer.speak_text_async(message).get()
    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        # print("Speech synthesized for text [{}]".format(message))
        return True
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        return False

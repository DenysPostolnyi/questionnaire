import winsound
import abonent
import operator_part

from abonent import start_abonent, send_message_to_abonent
from audio import text_to_speech, extract_text
from operator_part import start_operator, send_message_to_operator

example_texts = []

if __name__ == '__main__':
    print("Starting...")
    start_operator()
    start_abonent()
    print("Text gotten and items configured")

    last_message_from_operator = ''
    total_tokens_for_operator = 0
    total_tokens_for_abonent = 0
    operator_replica = ''
    abonent_replica = ''

    print(f"Dialog starting...")
    replica_count = 1
    while last_message_from_operator != '1':
        last_message_from_operator, total_tokens_for_operator = send_message_to_operator("")
        if last_message_from_operator == '1':
            break
        print(f'- Operator text: {last_message_from_operator}')
        text_to_speech(last_message_from_operator, f"dialog/operator-{replica_count}.wav")

        operator_replica = extract_text(f"dialog/operator-{replica_count}.wav")['text']
        print(f'- Operator text from audio: {operator_replica}')
        last_message_from_abonent, total_tokens_for_abonent = send_message_to_abonent(operator_replica)
        print(f'- Abonent text: {last_message_from_abonent}')
        text_to_speech(last_message_from_abonent, f"dialog/abonent-{replica_count}.wav")

        abonent_replica = extract_text(f"dialog/operator-{replica_count}.wav")['text']
        print(f'- Abonent text from audio: {last_message_from_abonent}')

        replica_count += 1

    print("<---------------------------------------------------->")
    print("Dialog finished")
    print(f"Total operator tokens: {total_tokens_for_operator}")
    print(f"Total abonent tokens: {total_tokens_for_abonent}")

    operator_part.clear_operator_messages()
    abonent.clear_abonent_messages()
    print("<=======================>")
    winsound.Beep(440, 1000)

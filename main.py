import winsound
import abonent
import operator_part

from abonent import start_abonent, send_message_to_abonent
from operator_part import start_operator, send_message_to_operator

example_texts = []

if __name__ == '__main__':
    print("Starting...")
    start_operator()
    start_abonent()
    print("Text gotten and items configured")

    dialog_number = 1
    for i in range(5):
        last_message_from_operator = ''
        last_message_from_abonent = ''
        total_tokens_for_operator = 0
        total_tokens_for_abonent = 0

        print(f"{dialog_number} Dialog starting...")
        while last_message_from_operator != '1':
            last_message_from_operator, total_tokens_for_operator = send_message_to_operator("")
            if last_message_from_operator == '1':
                break
            print(f'- Operator: {last_message_from_operator}')
            last_message_from_abonent, total_tokens_for_abonent = send_message_to_abonent(last_message_from_operator)
            print(f'- Abonent: {last_message_from_abonent}')

        print("<---------------------------------------------------->")
        print("Dialog finished")
        print(f"Total operator tokens: {total_tokens_for_operator}")
        print(f"Total abonent tokens: {total_tokens_for_abonent}")

        operator_part.clear_operator_messages()
        abonent.clear_abonent_messages()
        print("<=======================>")
        dialog_number += 1

    winsound.Beep(440, 1000)

# TODO: Зробити щоб абонент був більш креативним та давав більше місць де бачив рекламу.

# from transformers import pipeline, set_seed

# def main():

#     set_seed(42)

#     generator = pipeline('conversational', model='gpt2')

#     # Iniciar a conversa
#     history = []

#     for i in range(10):

#         user_input = input("Você: ")
#         history.append(user_input)

#         # Obter resposta do modelo
#         bot_response = generator(history)

#         # Mostrar a resposta do modelo
#         print("Bot:", bot_response)

#         # Adicionar resposta do bot ao histórico de conversação
#         history.append(bot_response)

# if __name__ == "__main__":
#     main()



from transformers import pipeline, set_seed

def main():
    set_seed(42)

    # Definir o pipeline de Conversational AI
    generator = pipeline('conversational', model='gpt2')

    # Iniciar a conversa
    history = []

    for i in range(10):
        user_input = input("Você: ")
        history.append({"role": "user", "content": user_input})

        # Obter resposta do modelo
        bot_response = generator(history)

        # Mostrar a resposta do modelo
        print("Bot:", bot_response[-1]["content"])

        # Adicionar resposta do bot ao histórico de conversação
        history.append({"role": "assistant", "content": bot_response[-1]["content"]})

if __name__ == "__main__":
    main()

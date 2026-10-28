from agent import agent


print("AI-ассистент запущен. напиши 'выход', чтобы выйти")


while True:
    try:
        user_input = input("\nТы: ")
    except UnicodeDecodeError as error:
        print("не удалось прочитать ввод")
        print(error)
        continue

    if user_input.lower() == "выход":
        print("пока")
        break

    response = agent.invoke({
        "messages": [
            ("user", user_input)
        ]
    })

    print("\nАгент:")
    print(response["messages"][-1].content)
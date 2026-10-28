from agent import agent

questions = [
    "какая погода сейчас в Москве",
    "найди в интернете, что такое langgraph",
    "Что такое Python"
]

for question in questions:
    print("\n" + "=" * 80)
    print(f"вопрос: {question}")
    print("=" * 80)

    used_tools = []

    for step in agent.stream({
        "messages": [
            ("user", question)
        ]
    }):
        if "agent" in step:
            messages = step["agent"]["messages"]
            last_message = messages[-1]

            if last_message.tool_calls:
                for tool_call in last_message.tool_calls:
                    used_tools.append(tool_call["name"])

        if "tools" in step:
            pass

    if used_tools:
        print(f"использованные инструменты: {', '.join(used_tools)}")
    else:
        print("инструменты не использовались")

    response = agent.invoke({
        "messages": [
            ("user", question)
        ]
    })

    print("\nответ:")
    print(response["messages"][-1].content)
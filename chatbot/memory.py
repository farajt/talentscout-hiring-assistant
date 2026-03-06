from langchain_classic.memory import ConversationBufferMemory


def get_memory():
    memory = ConversationBufferMemory(
        memory_key="conversation_history",
        return_messages=True
    )

    return memory
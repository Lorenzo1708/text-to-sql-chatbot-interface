import os

import gradio as gr
import requests


def chat(message: str, history: list[dict[str, str | None]]) -> str:
    url = os.getenv("URL")

    if not url:
        raise Exception("if not URL")

    return requests.post(
        f"{url}/api/v1/chat", json={"message": message, "history": history}
    ).json()["content"]


chat_interface = gr.ChatInterface(chat, type="messages", save_history=True)
chat_interface.saved_conversations.secret = "secret"
chat_interface.launch()

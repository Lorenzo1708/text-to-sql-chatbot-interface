import os
from typing import Literal

import gradio as gr
import requests


def chat(
    message: str,
    history: list[dict[str, str | None]],
    model: Literal["gemini-2.5-flash", "gemini-2.5-pro"],
) -> str:
    url = os.getenv("URL")

    if not url:
        raise Exception("if not URL")

    return requests.post(
        f"{url}/api/v1/chat",
        json={"model": model, "message": message, "history": history},
    ).json()["content"]


chat_interface = gr.ChatInterface(
    chat,
    type="messages",
    additional_inputs=[gr.Dropdown(["gemini-2.5-flash", "gemini-2.5-pro"])],
    save_history=True,
)
chat_interface.saved_conversations.secret = "secret"
chat_interface.launch()

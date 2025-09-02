import os
from typing import Literal

import gradio as gr
import requests
from google.auth.transport.requests import Request
from google.oauth2 import id_token


def chat(
    message: str,
    history: list[dict[str, str | None]],
    model: Literal["gemini-2.5-flash", "gemini-2.5-pro"],
) -> str:
    url = os.getenv("URL")

    if not url:
        raise Exception("Missing URL environment variable.")

    try:
        return requests.post(
            f"{url}/api/v1/chat",
            json={"model": model, "message": message, "history": history},
            headers={
                "Authorization": f"Bearer {id_token.fetch_id_token(Request(), url)}"
            }
            if url != "http://server:8080"
            else None,
        ).json()["content"]
    except Exception:
        return "Error."


chat_interface = gr.ChatInterface(
    chat,
    type="messages",
    additional_inputs=[gr.Dropdown(["gemini-2.5-flash", "gemini-2.5-pro"])],
    save_history=True,
)
chat_interface.saved_conversations.secret = "secret"

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

if not (username and password):
    raise Exception("Missing USERNAME and/or PASSWORD environment variable(s).")

chat_interface.launch(auth=(username, password))

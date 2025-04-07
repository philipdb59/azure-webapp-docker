import gradio as gr
import os

def greet(name):
    return f"Hello, {name}!"

# Use the port specified by the environment variable WEBSITE_PORT, default to 7860 if not set.
port = int(os.environ.get("WEBSITE_PORT", 7860))

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch(server_name="0.0.0.0", server_port=port)

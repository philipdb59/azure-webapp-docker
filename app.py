import gradio as gr
import os

# Use the port specified by the environment variable WEBSITE_PORT, default to 7860 if not set.
port = int(os.environ.get("WEBSITE_PORT", 7860))

# Define a function that processes the user's message and any uploaded files.
def process_message(message, history):
    response = "You wrote: " + message["text"]
    if message.get("files"):
        response += " and uploaded " + str(len(message["files"])) + " files."
    return response

# Create a Gradio chat interface with a multimodal textbox that allows text and file uploads.
demo = gr.ChatInterface(
    fn=process_message,
    type="messages",
    multimodal=True,
    textbox=gr.MultimodalTextbox(file_count="multiple"),
)

demo.launch(server_name="0.0.0.0", server_port=port)

import gradio as gr
import os
import matplotlib.pyplot as plt
import numpy as np
import time

# Use the port specified by the environment variable WEBSITE_PORT, default to 7860 if not set.
port = int(os.environ.get("WEBSITE_PORT", 7860))

def slow_echo(message, history, file=None):
    # Stream the response to the user, character by character
    for i in range(len(message)):
        time.sleep(0.05)
        yield "You typed: " + message[: i + 1]

def handle_file(file):
    # Handle file upload and return a message
    if file:
        return f"File {file.name} uploaded successfully."
    return ""

def generate_plot(message):
    # Generate a simple plot based on the length of the user's message
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * len(message)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Plot based on message length")
    return fig

# Create the chat interface with additional inputs for file upload
with gr.Blocks() as demo:
    chatbot = gr.ChatInterface(
    slow_echo,
    type="messages",
    flagging_mode="manual",
    flagging_options=["Like", "Spam", "Inappropriate", "Other"],
    save_history=True,
    )

    # Create an Accordion to contain the file upload component
    with gr.Accordion("Upload a File", open=False):
        file_upload = gr.File(label="Upload a File")
    plot_output = gr.Plot(label="Plot Output")

    # Define event listeners for the chat interface
    clear = gr.Button("Clear")

    # Event listener for file upload
    file_upload.change(handle_file, file_upload, chatbot, queue=False)

    # Event listener for clearing the chat and plot
    clear.click(lambda: None, None, chatbot, queue=False)
    clear.click(lambda: None, None, plot_output, queue=False)
    
demo.launch(server_name="0.0.0.0", server_port=port)

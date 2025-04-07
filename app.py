import gradio as gr 

from transformers import pipeline 

 

classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True) 

 

def detect_emotions(emotion_input): 

  prediction = classifier(emotion_input,) 

  output = {} 

  for emotion in prediction[0]: 

    output[emotion["label"]] = emotion["score"] 

  return output 

 

examples = [["I am excited to announce that I have been promoted"], ["Sorry for the late reply"]] 

 

demo = gr.Interface(fn=detect_emotions, inputs=gr.Textbox(placeholder="Enter text here", label="Input"), outputs=gr.Label(label="Emotion"), examples=examples) 

demo.launch(server_name="0.0.0.0", server_port=7000) 

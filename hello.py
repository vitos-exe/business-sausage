from litellm import completion
import gradio as gr


MODEL_NAME = 'ollama/llama3.2'
API_BASE = 'http://localhost:11434'
SYSTEM_MESSAGE = {
    'role': 'system', 
    'content': 'You are an assistant that rewrites text to make it more formal and professional while preserving the original meaning.'
}

def answer_question(question: str):
    answer = completion(
        model=MODEL_NAME,
        api_base=API_BASE,
        messages=[SYSTEM_MESSAGE, {'role': 'user', 'content': question}]
    )
    return answer.json()['choices'][0]['message']['content']


if __name__ == "__main__":
    demo = gr.Interface(fn=answer_question, inputs='text', outputs='text')
    demo.launch();


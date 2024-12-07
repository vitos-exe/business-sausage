from litellm import completion
import gradio as gr


MODEL_NAME = 'ollama/llama3.2'
API_BASE = 'http://localhost:11434'
SYSTEM_MESSAGE = {
    'role': 'system', 
    'content': 'You are an assistant that rewrites text to make it more formal and professional while preserving the original meaning.'
}

def rewrite(question: str):
    answer = completion(
        model=MODEL_NAME,
        api_base=API_BASE,
        messages=[SYSTEM_MESSAGE, {'role': 'user', 'content': question}]
    )
    return answer.json()['choices'][0]['message']['content']


with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Bussiness sausage
        The simple LLM promt reader that rewrites your text in the formal way.
        """
    )
    inputs = gr.Textbox(label='Promt')
    rewrite = gr.Button('Rewrite')
    outputs = gr.Textbox(label='Output')

    rewrite.click(fn=rewrite, inputs=inputs, outputs=outputs)

if __name__ == "__main__":
    demo.launch();


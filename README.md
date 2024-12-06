# Bussiness sausage
The simple LLM promt reader that rewrites your text in the formal way.

## How to run
The current application is hardcoded for Ollama and Llama3.2 model. 
Anyway, as it uses LiteLLM you can easily rewrite it for any other LLM provider. 
If you want to stick to Ollama but use different model, just change the respective constant in the application.

For the current setup run the following(may take some time):
```
docker run --name=ollama -d -p 11434:11434 ollama/ollama:latest
docker exec ollama ollama pull llama3.2
```

After that you can start the application itself via running:
```
uv sync
uv run hello.py
```

Then, navigate to `localhost:7860`. You should be able to use the application.

## Testing
An example promt to try the app out:
> Hey, can you send me that report ASAP? I need it for a meeting. Thanks!

Expected output:
> Could you kindly send me the report at your earliest convenience? I require it for an upcoming meeting. Thank you

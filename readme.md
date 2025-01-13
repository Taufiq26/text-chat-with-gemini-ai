# Prepare for run
> source .venv/bin/activate
> pip install -r requirements.txt

## Tests the API
> python -W ignore test_gemini_api.py

## Run app
> python -W ignore app.py

# Gemini Model
```
models/gemini-1.0-pro-latest
models/gemini-1.0-pro
models/gemini-pro
models/gemini-1.0-pro-001
models/gemini-1.0-pro-vision-latest
models/gemini-pro-vision
models/gemini-1.5-pro-latest
models/gemini-1.5-pro-001
models/gemini-1.5-pro-002
models/gemini-1.5-pro
models/gemini-1.5-pro-exp-0801
models/gemini-1.5-pro-exp-0827
models/gemini-1.5-flash-latest
models/gemini-1.5-flash-001
models/gemini-1.5-flash-001-tuning
models/gemini-1.5-flash
models/gemini-1.5-flash-exp-0827
models/gemini-1.5-flash-002
models/gemini-1.5-flash-8b
models/gemini-1.5-flash-8b-001
models/gemini-1.5-flash-8b-latest
models/gemini-1.5-flash-8b-exp-0827
models/gemini-1.5-flash-8b-exp-0924
models/gemini-2.0-flash-exp
models/gemini-exp-1206
models/gemini-exp-1121
models/gemini-exp-1114
models/gemini-2.0-flash-thinking-exp
models/gemini-2.0-flash-thinking-exp-1219
models/learnlm-1.5-pro-experimental
```

The difference:
1. Pro Models:
    - gemini-pro and variants (1.0, 1.5) are optimized for text-based tasks
    - Best for complex reasoning, writing, and analysis
2. Vision Models:
    - gemini-pro-vision can process both text and images
    - Ideal for tasks requiring image understanding and analysis
3. Flash Models:
    - gemini-1.5-flash series are optimized for faster response times
    - 8b variants indicate 8-bit quantization for improved performance
    - Great for applications requiring quick responses
4. Experimental Models:
    - gemini-exp and gemini-2.0-flash-thinking-exp are cutting-edge versions
    - Feature latest capabilities and improvements
    - Good for testing new features
5. Version Indicators:
    - latest tags indicate most current stable version
    - Numbered versions (001, 002) are specific releases
    - exp suffix marks experimental builds

Each model type is optimized for specific use cases, allowing you to choose the most suitable one for your application's needs.

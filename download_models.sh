#!/bin/bash

mkdir -p models

# Download Mistral model
wget -O models/mistral-7b-instruct-v0.1.Q5_K_M.gguf https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q5_K_M.gguf

# Download LLaVA 13B model
wget -O models/ggml-model-q5_k.gguf https://huggingface.co/mys/ggml_llava-v1.5-13b/resolve/main/ggml-model-q5_k.gguf

# Download LLaVA 7B model
wget -O models/mmproj-model-f16.gguf https://huggingface.co/mys/ggml_llava-v1.5-7b/resolve/main/mmproj-model-f16.gguf
import os
import requests

def download_model(model_url, save_path):
    response = requests.get(model_url)
    with open(save_path, "wb") as f:
        f.write(response.content)
    print(f"Downloaded model to {save_path}")

if __name__ == "__main__":
    # URLs of your models
    models = {
        #https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q5_K_M.gguf?download=true
        #https://huggingface.co/mys/ggml_llava-v1.5-13b/resolve/main/ggml-model-q5_k.gguf?download=true
        #https://huggingface.co/mys/ggml_llava-v1.5-7b/resolve/main/mmproj-model-f16.gguf?download=true
        "mistral-7b-instruct-v0.1.Q5_K_M": "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q5_K_M.gguf?download=true",
        "ggml-model-q5_k": "https://huggingface.co/mys/ggml_llava-v1.5-13b/resolve/main/ggml-model-q5_k.gguf?download=true",
        "mmproj-model-f16" : "https://huggingface.co/mys/ggml_llava-v1.5-7b/resolve/main/mmproj-model-f16.gguf?download=true"

        # Add other model URLs here
    }

    for model_name, model_url in models.items():
        save_path = os.path.join("models", model_name + ".gguf")
        download_model(model_url, save_path)

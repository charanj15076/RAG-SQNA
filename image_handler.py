import base64
from transformers import BlipProcessor, BlipForConditionalGeneration, CLIPProcessor, CLIPModel
import torch
from PIL import Image
from io import BytesIO
from utils import load_config

config = load_config()
def convert_bytes_to_base64(image_bytes):
    encoded_string = base64.b64encode(image_bytes).decode("utf-8")
    return "data:image/jpeg;base64," + encoded_string

def handle_image(image_bytes, user_message):
    # Load BLIP model and processor from Hugging Face
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Convert the image bytes to a PIL Image
    image = Image.open(BytesIO(image_bytes))

    # Process the image and user message for BLIP model
    inputs = processor(images=image, text=user_message, return_tensors="pt")

    # Generate output based on the image and text (responding to the user's question about the image)
    out = model.generate(**inputs)
    response = processor.decode(out[0], skip_special_tokens=True)

    return response
from transformers import BlipProcessor, BlipForConditionalGeneration, pipeline
import base64
from utils import load_config

config = load_config()

def convert_bytes_to_base64(image_bytes):
    encoded_string = base64.b64encode(image_bytes).decode("utf-8")
    return "data:image/jpeg;base64," + encoded_string

def handle_image(image_bytes, user_message):
    # Load BLIP model and processor from Hugging Face
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Convert image to base64 for integration
    image_base64 = convert_bytes_to_base64(image_bytes)

    # Process the image and text to generate a caption or response
    inputs = processor(image_bytes, user_message, return_tensors="pt")

    # Generate output using the Hugging Face model
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

    return caption

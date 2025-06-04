
from PIL import Image, ImageDraw, ImageFont
import os
import time

def generate_meme(image_path, top_text, bottom_text):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    try:
        # Use a font that works on your device or one you downloaded
        font = ImageFont.truetype("/system/fonts/DroidSans-Bold.ttf", 60)  # You can increase the size here
    except Exception as e:
        print(f"Warning: {e}. Using default font.")
        font = ImageFont.load_default()

    width, height = img.size

    def draw_text(text, y_position):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        draw.text(((width - text_width) / 2, y_position), text, font=font, fill="yellow")  # Change color here

    draw_text(top_text, 10)
    draw_text(bottom_text, height - 80)

    # Unique filename using timestamp
    timestamp = int(time.time())
    output_path = f"/storage/emulated/0/Download/generated_meme_{timestamp}.jpg"
    img.save(output_path)
    print(f"\nMeme saved at: {output_path}")

def main():
    print("**Meme Generator**")
    image_path = input("Enter image path: ")
    top_text = input("Enter top text: ")
    bottom_text = input("Enter bottom text: ")

    if os.path.exists(image_path):
        generate_meme(image_path, top_text, bottom_text)
    else:
        print("Error: Image not found!")

if __name__ == "__main__":
    main()

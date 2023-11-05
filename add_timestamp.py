from PIL import Image, ImageDraw, ImageFont
import datetime
import os
from PIL.ExifTags import TAGS

def get_image_datetime_original(image_path):
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == 'DateTimeOriginal':
                return value
        return None
    except (AttributeError, KeyError, IndexError):
        return None

def add_text_with_scaled_font(image_path, output_path, timestamp, custom_font_path, padding_ratio=0.5):
    pil_image = Image.open(image_path)
    draw = ImageDraw.Draw(pil_image)

    image_width, image_height = pil_image.size

    # Calculate the font size based on image resolution and padding
    padding_x = int(image_width * padding_ratio)
    padding_y = int(image_height * padding_ratio)
    max_dimension = max(image_width - 2 * padding_x, image_height - 2 * padding_y)
    custom_font_size = int(max_dimension * 0.02)  # Adjust font size as needed

    # Specify the custom font
    custom_font = ImageFont.truetype(custom_font_path, custom_font_size)

    # Ensure the output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Calculate the position with padding
    position_x = image_width - custom_font.getsize(timestamp)[0] - 1 * custom_font_size
    position_y = image_height - custom_font.getsize(timestamp)[1] - 1 * custom_font_size
    position = (position_x, position_y)

    # Split the timestamp string into date and time components
    date_str, time_str = timestamp.split(' ')

    # Split the date and time components further
    date_parts = date_str.split(':')
    time_parts = time_str.split(':')

    # Create a datetime object from the parsed components
    original_datetime = datetime.datetime(
        int(date_parts[0]), int(date_parts[1]), int(date_parts[2]),
        int(time_parts[0]), int(time_parts[1]), int(time_parts[2])
    )

    # Format the datetime object as a string
    timestamp_str = original_datetime.strftime('%d/%m/%Y %H:%M')

    text_color = (255, 255, 255)

    # Draw the text with the specified font and position
    draw.text(position, timestamp_str, fill=text_color, font=custom_font)
    pil_image.save(output_path)

# Specify the folder containing the images
folder_path = 'images/'  # Change this to your image folder

# Specify the output folder for the modified images
output_folder = 'output_images/'

# Specify the path to your custom font file
custom_font_path = 'arial.ttf'

# Loop through the files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        image_path = os.path.join(folder_path, filename)
        timestamp = get_image_datetime_original(image_path)
        if timestamp:
            timestamp_str = timestamp  # Assuming your timestamp is in the correct format
            output_path = os.path.join(output_folder, filename)

            # Specify the padding ratio (e.g., 0.05 for 5% padding)
            padding_ratio = 0.025

            add_text_with_scaled_font(image_path, output_path, timestamp_str, custom_font_path, padding_ratio)
            print(f"Added text with scaled font and padding to {filename} and saved to {output_path}")

print("Text with scaled font and padding added to all eligible images in the folder and saved in the output folder.")

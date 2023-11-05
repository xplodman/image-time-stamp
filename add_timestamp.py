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

def add_timestamp_to_image(image_path, output_path, timestamp):
    pil_image = Image.open(image_path)
    draw = ImageDraw.Draw(pil_image)

    font = ImageFont.load_default()
    font_size = 24
    text_color = (255, 255, 255)
    position = (pil_image.width - 120, pil_image.height - 40)  # Adjust the position as needed

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

    # Ensure the output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    draw.text(position, timestamp_str, fill=text_color, font=font)
    pil_image.save(output_path)

# Specify the folder containing the images
folder_path = 'images/'  # Change this to your image folder

# Specify the output folder for the modified images
output_folder = 'output_images/'

# Loop through the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        image_path = os.path.join(folder_path, filename)
        timestamp = get_image_datetime_original(image_path)
        if timestamp:
            timestamp_str = timestamp  # Assuming your timestamp is in the correct format
            output_path = os.path.join(output_folder, f"{filename}")
            
            add_timestamp_to_image(image_path, output_path, timestamp_str)
            print(f"Added timestamp to {filename} and saved to {output_path}")

print("Timestamps added to all eligible images in the folder and saved in the output folder.")


import base64
from pathlib import Path

# Read and encode all product images
image_files = [
    "sunday.jpg",
    "work.jpg", 
    "hippers.jpg",
    "plush-charm.jpg",
    "moving.jpg",
    "cheer.jpg",
    "keychains.jpg",
    "exercise.jpg",
    "birthday.jpg"
]

encoded_images = {}
for img_file in image_files:
    with open(img_file, "rb") as f:
        encoded_images[img_file] = base64.b64encode(f.read()).decode()

print("Successfully encoded all images")
print(f"Total images: {len(encoded_images)}")
for key in encoded_images.keys():
    print(f"- {key}")


import json

# Prepare YAML-like data for the app
yaml_data = f"""
products:
  accessories:
    - name: Plush Charm
      image: plush-charm.jpg
      price: 12.99
      category: Accessories
    - name: Keychains
      image: keychains.jpg
      price: 8.99
      category: Accessories
    - name: Hippers
      image: hippers.jpg
      price: 15.99
      category: Accessories
  blind_boxes:
    - name: Birthday
      image: birthday.jpg
      price: 9.99
      category: Blind Boxes
    - name: Exercise
      image: exercise.jpg
      price: 9.99
      category: Blind Boxes
    - name: Work
      image: work.jpg
      price: 9.99
      category: Blind Boxes
    - name: Cheer
      image: cheer.jpg
      price: 9.99
      category: Blind Boxes
    - name: Moving
      image: moving.jpg
      price: 9.99
      category: Blind Boxes
    - name: Sunday
      image: sunday.jpg
      price: 9.99
      category: Blind Boxes

promotions:
  - type: cross_category
    description: Buy 1 product from each different category and get 20% off
    discount: 0.20
    conditions:
      - at_least_one_from_accessories: true
      - at_least_one_from_blind_boxes: true
  - type: same_product
    description: Buy 6 of the same blind box product and get 15% off
    discount: 0.15
    conditions:
      - same_blind_box_count: 6

gst_rate: 0.09

payment_methods:
  - Credit Card
  - Debit Card
  - PayPal
  - Apple Pay
  - Google Pay
"""

# Create image data mapping
image_data = {}
for img_file in image_files:
    with open(img_file, "rb") as f:
        image_data[img_file] = base64.b64encode(f.read()).decode()

# Save image data to pass to the app
with open('image_data.json', 'w') as f:
    json.dump(image_data, f)

print("Data prepared for Streamlit app")
print(f"Total images encoded: {len(image_data)}")

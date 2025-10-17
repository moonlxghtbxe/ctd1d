
# Create product data structure with all required information
products_data = {
    "accessories": [
        {
            "name": "Plush Charm",
            "image": "plush-charm.jpg",
            "price": 12.99,
            "category": "Accessories"
        },
        {
            "name": "Keychains",
            "image": "keychains.jpg", 
            "price": 8.99,
            "category": "Accessories"
        },
        {
            "name": "Hippers",
            "image": "hippers.jpg",
            "price": 15.99,
            "category": "Accessories"
        }
    ],
    "blind_boxes": [
        {
            "name": "Birthday",
            "image": "birthday.jpg",
            "price": 9.99,
            "category": "Blind Boxes"
        },
        {
            "name": "Exercise",
            "image": "exercise.jpg",
            "price": 9.99,
            "category": "Blind Boxes"
        },
        {
            "name": "Work",
            "image": "work.jpg",
            "price": 9.99,
            "category": "Blind Boxes"
        },
        {
            "name": "Cheer",
            "image": "cheer.jpg",
            "price": 9.99,
            "category": "Blind Boxes"
        },
        {
            "name": "Moving",
            "image": "moving.jpg",
            "price": 9.99,
            "category": "Blind Boxes"
        },
        {
            "name": "Sunday",
            "image": "sunday.jpg",
            "price": 9.99,
            "category": "Blind Boxes"
        }
    ]
}

print("Product Data Structure:")
print(f"Accessories count: {len(products_data['accessories'])}")
print(f"Blind Boxes count: {len(products_data['blind_boxes'])}")
print("\nAccessories:")
for p in products_data['accessories']:
    print(f"  - {p['name']}: ${p['price']}")
print("\nBlind Boxes:")
for p in products_data['blind_boxes']:
    print(f"  - {p['name']}: ${p['price']}")

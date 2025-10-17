import streamlit as st
import base64
from io import BytesIO
from PIL import Image
import json

# Page configuration
st.set_page_config(
    page_title="Smiski World",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #FF69B4;
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .promotion-box {
        background-color: #FFE4E1;
        padding: 15px;
        border-radius: 10px;
        margin: 20px 0;
        text-align: center;
    }
    .category-header {
        color: #FF1493;
        font-size: 32px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    .product-card {
        text-align: center;
        padding: 10px;
        cursor: pointer;
        transition: transform 0.2s;
    }
    .product-card:hover {
        transform: scale(1.05);
    }
    .product-name {
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
    }
    .product-price {
        font-size: 16px;
        color: #666;
    }
    .cart-icon {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #FF69B4;
        color: white;
        padding: 15px 20px;
        border-radius: 50px;
        font-size: 24px;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        z-index: 1000;
    }
    .receipt-container {
        background-color: white;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        max-width: 600px;
        margin: 0 auto;
    }
    .receipt-header {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #FF1493;
        margin-bottom: 20px;
    }
    .receipt-line {
        display: flex;
        justify-content: space-between;
        padding: 5px 0;
        border-bottom: 1px solid #eee;
    }
    .receipt-total {
        font-weight: bold;
        font-size: 20px;
        color: #FF1493;
        margin-top: 15px;
    }
    .payment-method {
        background-color: #FFE4E1;
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        text-align: center;
        cursor: pointer;
        font-size: 18px;
        transition: background-color 0.2s;
    }
    .payment-method:hover {
        background-color: #FFB6C1;
    }
    .thank-you-message {
        text-align: center;
        font-size: 48px;
        color: #FF69B4;
        margin-top: 100px;
    }
    .click-anywhere {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'store'
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'serial_counter' not in st.session_state:
    st.session_state.serial_counter = 1000

# Product data
PRODUCTS = {
    "Accessories": [
        {"name": "Plush Charm", "image": "plush-charm.png", "price": 12.99, "category": "Accessories"},
        {"name": "Keychains", "image": "keychains.jpg", "price": 8.99, "category": "Accessories"},
        {"name": "Hippers", "image": "hippers.jpg", "price": 15.99, "category": "Accessories"}
    ],
    "Blind Boxes": [
        {"name": "Birthday", "image": "birthday.jpg", "price": 9.99, "category": "Blind Boxes"},
        {"name": "Exercise", "image": "exercise.jpg", "price": 9.99, "category": "Blind Boxes"},
        {"name": "Work", "image": "work.jpg", "price": 9.99, "category": "Blind Boxes"},
        {"name": "Cheer", "image": "cheer.jpg", "price": 9.99, "category": "Blind Boxes"},
        {"name": "Moving", "image": "moving.jpg", "price": 9.99, "category": "Blind Boxes"},
        {"name": "Sunday", "image": "sunday.jpg", "price": 9.99, "category": "Blind Boxes"}
    ]
}

GST_RATE = 0.09  # 9% GST

def add_to_cart(product):
    st.session_state.cart.append({
        'serial': st.session_state.serial_counter,
        'name': product['name'],
        'price': product['price'],
        'category': product['category']
    })
    st.session_state.serial_counter += 1

def calculate_discounts(cart):
    discounts = []
    total_discount = 0

    # Check for cross-category promotion (20% off)
    has_accessories = any(item['category'] == 'Accessories' for item in cart)
    has_blind_boxes = any(item['category'] == 'Blind Boxes' for item in cart)

    if has_accessories and has_blind_boxes:
        discount_amount = sum(item['price'] for item in cart) * 0.20
        discounts.append(("Cross-Category Discount (20%)", discount_amount))
        total_discount += discount_amount

    # Check for same blind box promotion (15% off for 6 of the same)
    blind_box_counts = {}
    for item in cart:
        if item['category'] == 'Blind Boxes':
            blind_box_counts[item['name']] = blind_box_counts.get(item['name'], 0) + 1

    for product_name, count in blind_box_counts.items():
        if count >= 6:
            sets_of_six = count // 6
            product_price = next(p['price'] for p in PRODUCTS['Blind Boxes'] if p['name'] == product_name)
            discount_amount = product_price * 6 * 0.15 * sets_of_six
            discounts.append((f"{product_name} Set Discount (15% off for {sets_of_six} set(s) of 6)", discount_amount))
            total_discount += discount_amount

    return discounts, total_discount

def store_page():
    # Title
    st.markdown('<div class="main-title">Welcome to Smiski World</div>', unsafe_allow_html=True)

    # Promotions
    st.markdown("""
    <div class="promotion-box">
        <h3>🎉 Special Promotions! 🎉</h3>
        <p>✨ Buy 1 product from each different category and get <strong>20% OFF</strong></p>
        <p>✨ Buy 6 of the same blind box product and get <strong>15% OFF</strong></p>
    </div>
    """, unsafe_allow_html=True)

    # Display products by category
    for category, products in PRODUCTS.items():
        st.markdown(f'<div class="category-header">{category}</div>', unsafe_allow_html=True)

        cols = st.columns(3)
        for idx, product in enumerate(products):
            with cols[idx % 3]:
                # Display product image
                try:
                    image = Image.open(product['image'])
                    st.image(image, use_container_width=True)
                except:
                    st.write(f"[{product['image']}]")

                # Product name and price
                st.markdown(f'<div class="product-name">{product["name"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="product-price">${product["price"]:.2f}</div>', unsafe_allow_html=True)

                # Add to cart button
                if st.button(f"Add to Cart", key=f"add_{category}_{product['name']}"):
                    add_to_cart(product)
                    st.rerun()

    # Shopping cart button (fixed position)
    cart_count = len(st.session_state.cart)
    st.markdown(f"""
    <div style="position: fixed; bottom: 30px; right: 30px; z-index: 1000;">
    """, unsafe_allow_html=True)

    if st.button(f"🛒 Cart ({cart_count})", key="cart_button"):
        st.session_state.page = 'checkout'
        st.rerun()

def checkout_page():
    st.markdown('<div class="receipt-container">', unsafe_allow_html=True)
    st.markdown('<div class="receipt-header">Receipt</div>', unsafe_allow_html=True)

    if len(st.session_state.cart) == 0:
        st.write("Your cart is empty!")
        if st.button("Back to Store"):
            st.session_state.page = 'store'
            st.rerun()
        return

    # Display cart items
    st.markdown("---")
    subtotal = 0

    for item in st.session_state.cart:
        st.markdown(f"**Serial Number:** {item['serial']}")
        st.markdown(f"**Product:** {item['name']}")
        st.markdown(f"**Price (excl. GST):** ${item['price']:.2f}")
        gst_value = item['price'] * GST_RATE
        st.markdown(f"**GST:** ${gst_value:.2f}")
        st.markdown("---")
        subtotal += item['price']

    # Calculate totals
    total_gst = subtotal * GST_RATE
    discounts, total_discount = calculate_discounts(st.session_state.cart)

    # Display summary
    st.markdown(f"**Subtotal (excl. GST):** ${subtotal:.2f}")
    st.markdown(f"**Total GST:** ${total_gst:.2f}")

    if discounts:
        st.markdown("**Discounts:**")
        for discount_name, discount_amount in discounts:
            st.markdown(f"  - {discount_name}: -${discount_amount:.2f}")

    final_total = subtotal + total_gst - total_discount
    st.markdown(f'<div class="receipt-total">Final Total: ${final_total:.2f}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Payment methods
    st.markdown("<br><h3 style='text-align: center;'>Select Payment Method</h3>", unsafe_allow_html=True)

    payment_methods = ["💳 Credit Card", "💳 Debit Card", "💰 PayPal", "🍎 Apple Pay", "📱 Google Pay"]

    cols = st.columns(2)
    for idx, method in enumerate(payment_methods):
        with cols[idx % 2]:
            if st.button(method, key=f"payment_{idx}", use_container_width=True):
                st.session_state.page = 'thankyou'
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back to Store", use_container_width=True):
        st.session_state.page = 'store'
        st.rerun()

def thankyou_page():
    st.markdown('<div class="thank-you-message">Thank You for Your Purchase! 🎉</div>', unsafe_allow_html=True)
    st.markdown('<div class="click-anywhere">Click below to return to the store</div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Return to Store", use_container_width=True, type="primary"):
        st.session_state.cart = []
        st.session_state.page = 'store'
        st.rerun()

# Main app logic
if st.session_state.page == 'store':
    store_page()
elif st.session_state.page == 'checkout':
    checkout_page()
elif st.session_state.page == 'thankyou':
    thankyou_page()

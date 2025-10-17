# Smiski Store - Streamlit Application

## Overview
This is a digital storefront for purchasing Smiski products built with Python and Streamlit. The application features a shopping cart system, automatic discount calculations, and a complete checkout flow.

## Features
- **Two Product Categories:**
  - Accessories: Plush Charm, Keychains, Hippers
  - Blind Boxes: Birthday, Exercise, Work, Cheer, Moving, Sunday

- **Automatic Promotions:**
  - 20% off when buying at least 1 product from each different category
  - 15% off when buying 6 of the same blind box product

- **Complete Shopping Experience:**
  - Interactive product catalog with images
  - Shopping cart with item counter
  - Detailed receipt with GST calculations
  - Multiple payment method options
  - Thank you page after purchase

## Files Required
- `smiski_store_app.py` - Main Streamlit application
- `sunday.jpg` - Product image
- `work.jpg` - Product image
- `hippers.jpg` - Product image
- `plush-charm.jpg` - Product image
- `moving.jpg` - Product image
- `cheer.jpg` - Product image
- `keychains.jpg` - Product image
- `exercise.jpg` - Product image
- `birthday.jpg` - Product image

## Installation

1. **Install Python** (if not already installed)
   - Download from: https://www.python.org/downloads/
   - Make sure to add Python to your PATH

2. **Install Required Packages**
   ```bash
   pip install streamlit pillow
   ```

## Running Locally

1. Place all files (Python script and image files) in the same directory

2. Open terminal/command prompt in that directory

3. Run the following command:
   ```bash
   streamlit run smiski_store_app.py
   ```

4. The app will open in your default web browser at `http://localhost:8501`

## Deployment to Streamlit Cloud

1. **Create a GitHub Repository**
   - Create a new repository on GitHub
   - Upload all files (Python script and images)

2. **Create requirements.txt**
   Create a file named `requirements.txt` with the following content:
   ```
   streamlit
   pillow
   ```

3. **Deploy to Streamlit Cloud**
   - Go to https://share.streamlit.io/
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Select the branch (usually "main")
   - Set main file path: `smiski_store_app.py`
   - Click "Deploy"

4. **Wait for Deployment**
   - Streamlit will build and deploy your app
   - You'll receive a public URL to share

## Usage Guide

### Shopping
1. Browse products by category (Accessories and Blind Boxes)
2. Click "Add to Cart" button under any product to add it to your cart
3. The cart icon in the bottom-right corner shows the number of items

### Checkout
1. Click the cart icon to view your receipt
2. Review your items, prices, GST, and any applicable discounts
3. Select a payment method
4. View the thank you message
5. Click to return to the store

## Product Pricing
- **Accessories:**
  - Plush Charm: $12.99
  - Keychains: $8.99
  - Hippers: $15.99

- **Blind Boxes:** $9.99 each
  - Birthday
  - Exercise
  - Work
  - Cheer
  - Moving
  - Sunday

## GST Calculation
- GST Rate: 9%
- Applied to all products before discounts
- Displayed separately on receipt

## Discount Logic
1. **Cross-Category Discount (20%):**
   - Automatically applied when cart contains at least 1 item from Accessories AND at least 1 item from Blind Boxes
   - Applies to entire order

2. **Same Product Discount (15%):**
   - Automatically applied when you have 6 or more of the same Blind Box product
   - Can be applied multiple times (e.g., 12 items = 2 sets of 6)
   - Only applies to Blind Box products

## Troubleshooting

**Images not showing:**
- Ensure all image files are in the same directory as the Python script
- Check that image filenames match exactly (including case)

**Streamlit not found:**
- Run: `pip install streamlit pillow`
- Or try: `python -m pip install streamlit pillow`

**Port already in use:**
- Use a different port: `streamlit run smiski_store_app.py --server.port 8502`

## Support
For issues or questions, please check:
- Streamlit documentation: https://docs.streamlit.io/
- Python documentation: https://docs.python.org/3/

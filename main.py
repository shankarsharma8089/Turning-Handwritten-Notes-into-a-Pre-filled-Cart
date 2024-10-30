import streamlit as st
from PIL import Image
import pytesseract

recommended_products = {
    "paneer": [
        {"name": "Amul Paneer 2kg", "price": "₹275", "image": "/Users/codewave/Desktop/nutri-checker /amul-malai-diced-paneer-200-g-pack-product-images-o490001435-p590041247-0-202206061832.webp"},
        {"name": "Mother Dairy Paneer 2kg", "price": "₹299", "image": "/Users/codewave/Desktop/nutri-checker /download.jpeg"},
        {"name": "Milky Mist Paneer 2kg", "price": "₹250", "image": "/Users/codewave/Desktop/nutri-checker /download (1).jpeg"}
    ],
    "beetroot": [
        {"name": "Fresh Beetroot 1kg", "price": "₹50", "image": "download (2).jpeg"},
        {"name": "Organic Beetroot 1kg", "price": "₹60", "image": "download (3).jpeg"}
    ],
    "fish basa": [
        {"name": "Frozen Basa Fish 1kg", "price": "₹300", "image": ""},
        {"name": "Fresh Basa Fish Fillet 1kg", "price": "₹350", "image": "download (5).jpeg"}
    ],
    "chicken bonles": [
        {"name": "Licious Chicken Breast Boneless", "price": "₹275", "image": "https://via.placeholder.com/100"},
        {"name": "Fresh Chicken Boneless 1kg", "price": "₹280", "image": "https://via.placeholder.com/100"}
    ],
    "basmati rice": [
        {"name": "Daawat Basmati Rice 1kg", "price": "₹200", "image": "https://via.placeholder.com/100"},
        {"name": "India Gate Basmati Rice 1kg", "price": "₹210", "image": "https://via.placeholder.com/100"},
        {"name": "Fortune Basmati Rice 1kg", "price": "₹190", "image": "https://via.placeholder.com/100"}
    ],
    "mushroom": [
        {"name": "Fresh Button Mushrooms 3pk", "price": "₹90", "image": "/Users/codewave/Desktop/nutri-checker /download (4).jpeg"},
        {"name": "Portobello Mushrooms 3pk", "price": "₹120", "image": "download (5).jpeg"}
    ],
    "potato": [
        {"name": "Fresh Potatoes 1kg", "price": "₹30", "image": "/Users/codewave/Desktop/nutri-checker /download (6).jpeg"},
        {"name": "Organic Potatoes 1kg", "price": "₹40", "image": "/Users/codewave/Desktop/nutri-checker /download (7).jpeg"}
    ],
    "kaju": [
        {"name": "Happilo Cashews 500g", "price": "₹350", "image": "https://via.placeholder.com/100"},
        {"name": "Nutraj Cashews 500g", "price": "₹360", "image": "https://via.placeholder.com/100"}
    ],
    "onion": [
        {"name": "Fresh Onions 2kg", "price": "₹40", "image": "https://via.placeholder.com/100"},
        {"name": "Organic Onions 2kg", "price": "₹50", "image": "https://via.placeholder.com/100"}
    ],
    "tomato": [
        {"name": "Fresh Tomatoes 1kg", "price": "₹30", "image": "https://via.placeholder.com/100"},
        {"name": "Organic Tomatoes 1kg", "price": "₹40", "image": "https://via.placeholder.com/100"}
    ],
    "comber": [
        {"name": "Fresh Cucumbers 500g", "price": "₹25", "image": "https://via.placeholder.com/100"},
        {"name": "Organic Cucumbers 500g", "price": "₹35", "image": "https://via.placeholder.com/100"}
    ],
    "capsicum": [
        {"name": "Mixed Capsicum 300g", "price": "₹60", "image": "https://via.placeholder.com/100"},
        {"name": "Green Capsicum 300g", "price": "₹50", "image": "https://via.placeholder.com/100"}
    ],
    "carrot": [
        {"name": "Fresh Carrots 500g", "price": "₹35", "image": "https://via.placeholder.com/100"},
        {"name": "Organic Carrots 500g", "price": "₹45", "image": "https://via.placeholder.com/100"}
    ],
    "garlic": [
        {"name": "Chinese Garlic 500g", "price": "₹100", "image": "https://via.placeholder.com/100"},
        {"name": "Local Garlic 500g", "price": "₹80", "image": "https://via.placeholder.com/100"}
    ],
    "green chilli": [
        {"name": "Fresh Green Chillies 200g", "price": "₹20", "image": "https://via.placeholder.com/100"},
        {"name": "Organic Green Chillies 200g", "price": "₹30", "image": "https://via.placeholder.com/100"}
    ],
    "tandoori chicken masala": [
        {"name": "Everest Tandoori Chicken Masala", "price": "₹40", "image": "https://via.placeholder.com/100"},
        {"name": "MDH Tandoori Chicken Masala", "price": "₹45", "image": "https://via.placeholder.com/100"}
    ],
    "bread crumbs": [
        {"name": "Fresh Bread Crumbs 250g", "price": "₹35", "image": "https://via.placeholder.com/100"},
        {"name": "Panko Bread Crumbs 250g", "price": "₹50", "image": "https://via.placeholder.com/100"}
    ],
    "basil leaves": [
        {"name": "Fresh Basil Leaves 250g", "price": "₹60", "image": "https://via.placeholder.com/100"},
        {"name": "Dried Basil Leaves 250g", "price": "₹70", "image": "https://via.placeholder.com/100"}
    ],
    "walnut": [
        {"name": "Kashmiri Walnuts 200g", "price": "₹150", "image": "https://via.placeholder.com/100"},
        {"name": "California Walnuts 200g", "price": "₹160", "image": "https://via.placeholder.com/100"}
    ],
    "cheese": [
        {"name": "Amul Cheese Can", "price": "₹90", "image": "https://via.placeholder.com/100"},
        {"name": "Britannia Cheese Can", "price": "₹95", "image": "https://via.placeholder.com/100"}
    ],
    "cream": [
        {"name": "Amul Fresh Cream 200g", "price": "₹55", "image": "https://via.placeholder.com/100"},
        {"name": "Mother Dairy Fresh Cream 200g", "price": "₹60", "image": "https://via.placeholder.com/100"}
    ],
    "milk": [
        {"name": "Amul Full Cream Milk 2L", "price": "₹100", "image": "https://via.placeholder.com/100"},
        {"name": "Mother Dairy Full Cream Milk 2L", "price": "₹105", "image": "https://via.placeholder.com/100"}
    ],
    "milk powder": [
        {"name": "Amul Milk Powder 1kg", "price": "₹200", "image": "https://via.placeholder.com/100"},
        {"name": "Nestle Milk Powder 1kg", "price": "₹220", "image": "https://via.placeholder.com/100"}
    ],
}

# Streamlit App Layout
st.title("Shopping List to Cart")

uploaded_file = st.file_uploader("Upload your shopping list image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Extract Text
    text = pytesseract.image_to_string(image)
    items = text.lower().split("\n")  # Convert items to lowercase for matching
    st.write("**Extracted Items:**")
    for item in items:
        st.write(item)
    
    # Generate Horizontal Recommendations in Card Style
    st.write("**Shopping Cart Recommendations:**")
    cart = {}
    
    for item in items:
        item = item.strip()  # Remove any extra spaces
        if not item:  # Skip if the line is empty
            continue
        item_key = item.split()[0]  # Simplify item lookup by matching only the first word
        if item_key in recommended_products:
            st.write(f"**Results for '{item.capitalize()}':**")
            
            # Create a row of columns to simulate a card view
            columns = st.columns(len(recommended_products[item_key]))
            for idx, product in enumerate(recommended_products[item_key]):
                with columns[idx]:  # Each product in a separate column
                    st.image(product["image"], width=100)
                    st.write(product["name"])
                    st.write(product["price"])
                    # Use item and idx to create a unique key
                    if st.button("Add", key=f"{item}_{idx}"):
                        cart[item] = product["name"]
    
    # Display Final Cart
    st.write("**Your Final Cart:**")
    for item, choice in cart.items():
        st.write(f"{item.capitalize()}: {choice}")

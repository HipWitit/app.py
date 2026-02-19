import streamlit as st
import re

# 1. THE EXPANDED 30x30 COORDINATE MAP
char_to_coord = {
    '1': (2, 25), '2': (5, 25), '3': (8, 25), '6': (14, 25), '7': (17, 25), '8': (20, 25),
    'Q': (2, 20), 'W': (5, 20), 'E': (8, 20), 'Y': (14, 20), 'U': (17, 20), 'I': (20, 20),
    'A': (3, 15), 'S': (6, 15), 'D': (9, 15), 'H': (15, 15), 'J': (18, 15), 'K': (21, 15),
    'Z': (4, 10), 'X': (7, 10), 'C': (10, 10), 'N': (16, 10), 'M': (19, 10),
    '!': (5, 5),  ',': (8, 5),  ' ': (15, 5)
}

coord_to_char = {v: k for k, v in char_to_coord.items()}

# 2. THE TRANSFORMATION BRAIN
def transform(x, y, key):
    if key == "CHILL": # Flip X then Rotate 90
        return y, x
    elif key == "PEACHY": # Flip Y then Rotate -90
        return (30 - y), (30 - x)
    elif key == "SIMON SAYS": # Flip X then Rotate 270
        return (30 - y), x
    elif key == "BABY": # Flip Y then Rotate -270
        return y, (30 - x)
    return x, y 

def untransform(x, y, key):
    if key == "CHILL":
        return y, x
    elif key == "PEACHY":
        return (30 - x), (30 - y)
    elif key == "SIMON SAYS":
        return y, (30 - x)
    elif key == "BABY":
        return (30 - y), x
    return x, y

# 3. UI STYLING
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://raw.githubusercontent.com/HipWitit/app.py/main/5ob23b1bfmdf1.jpeg", width=80)
with col2:
    st.title("Vector Movement Cipher")

st.markdown("Share secret messages using keyed coordinate displacements.")

# 4. KEYWORD INPUT (No suggestions)
kw = st.text_input("Enter Secret Key", type="password").upper().strip()

tab1, tab2 = st.tabs(["Encode Message", "Decode Vectors"])

# 5. ENCODING TAB
with tab1:
    st.header("Create a Cipher")
    msg_input = st.text_input("Enter message:")
    
    if msg_input:
        msg = msg_input.upper()
        coords = [transform(char_to_coord[c][0], char_to_coord[c][1], kw) for c in msg if c in char_to_coord]
        
        if coords:
            st.subheader(f"Transformed Start Point: {coords[0]}")
            
            full_code = []


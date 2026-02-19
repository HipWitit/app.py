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
    if key == "CHILL": 
        return y, x
    elif key == "PEACHY": 
        return (30 - y), (30 - x)
    elif key == "SIMON SAYS": 
        return (30 - y), x
    elif key == "BABY": 
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

# 4. KEYWORD INPUT
kw = st.text_input("Enter Secret Key", type="password").upper().strip()

tab1, tab2 = st.tabs(["Encode Message", "Decode Vectors"])

# 5. ENCODING TAB
with tab1:
    st.header("Create a Cipher")
    msg_input = st.text_input("Enter message:", value="WUBADOO!")
    
    if msg_input:
        msg = msg_input.upper()
        # Transform coords based on key
        coords = [transform(char_to_coord[c][0], char_to_coord[c][1], kw) for c in msg if c in char_to_coord]
        
        if coords:
            st.subheader(f"Transformed Start Point: {coords[0]}")
            
            # This loop calculates the vectors (dx, dy)
            full_code = []
            for i in range(len(coords) - 1):
                x1, y1 = coords[i]
                x2, y2 = coords[i+1]
                dx, dy = x2 - x1, y2 - y1
                full_code.append(f"({dx},{dy})")
            
            # Displays the final copyable code
            st.success("Sharable Code:")
            st.code(f"START: {coords[0][0]},{coords[0][1]} | MOVES: {' '.join(full_code)}")

# 6. DECODING TAB
with tab2:
    st.header("Read a Cipher")
    col1, col2 = st.columns(2)
    with col1:
        start_in = st.text_input("Start Point (x,y):")
    with col2:
        vector_in = st.text_area("Vectors (e.g. (5,2) (-3,4)):")

    if st.button("Decode"):
        try:
            sx, sy = map(int, start_in.split(','))
            curr = (sx, sy)
            
            ux, uy = untransform(sx, sy, kw)
            decoded = [coord_to_char.get((ux, uy), "?")]
            
            moves = re.findall(r"(-?\d+),(-?\d+)", vector_in)
            for dx, dy in moves:
                curr = (curr[0] + int(dx), curr[1] + int(dy))
                ux, uy = untransform(curr[0], curr[1], kw)
                decoded.append(coord_to_char.get((ux, uy), "?"))
            
            st.info(f"Decoded Message: {''.join(decoded)}")
        except Exception as e:
            st.error("Error! Check your Start Point and Vector formatting.")



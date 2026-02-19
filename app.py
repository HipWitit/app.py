import streamlit as st
import re

# 1. THE COMPLETE 30x30 COORDINATE MAP
char_to_coord = {
    'Q': (2, 25), 'W': (5, 25), 'E': (8, 25), 'R': (11, 25), 'T': (14, 25), 'Y': (17, 25), 'U': (20, 25), 'I': (23, 25), 'O': (26, 25), 'P': (29, 25),
    'A': (3, 20), 'S': (6, 20), 'D': (9, 20), 'F': (12, 20), 'G': (15, 20), 'H': (18, 20), 'J': (21, 20), 'K': (24, 20), 'L': (27, 20),
    'Z': (4, 15), 'X': (7, 15), 'C': (10, 15), 'V': (13, 15), 'B': (16, 15), 'N': (19, 15), 'M': (22, 15),
    '1': (2, 10), '2': (5, 10), '3': (8, 10), '4': (11, 10), '5': (14, 10), '6': (17, 10), '7': (20, 10), '8': (23, 10), '9': (26, 10), '0': (29, 10),
    '!': (5, 5),  ',': (10, 5), '.': (15, 5), ' ': (20, 5), '?': (25, 5)
}

coord_to_char = {v: k for k, v in char_to_coord.items()}

# 2. THE TRANSFORMATION BRAIN (Verified Correct)
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

kw = st.text_input("Enter Secret Key", type="password").upper().strip()

tab1, tab2 = st.tabs(["Encode Message", "Decode Vectors"])

# 4. ENCODING TAB
with tab1:
    st.header("Create a Cipher")
    msg_input = st.text_input("Enter message:", value="WUBADOO!")
    
    if msg_input:
        msg = msg_input.upper()
        coords = [transform(char_to_coord[c][0], char_to_coord[c][1], kw) for c in msg if c in char_to_coord]
        
        if coords:
            st.subheader(f"Transformed Start Point: ({coords[0][0]}, {coords[0][1]})")
            full_code = []
            for i in range(len(coords) - 1):
                x1, y1 = coords[i]
                x2, y2 = coords[i+1]
                dx, dy = x2 - x1, y2 - y1
                full_code.append(f"({dx},{dy})")
            
            st.success("Sharable Code:")
            st.code(f"{coords[0][0]},{coords[0][1]} | MOVES: {' '.join(full_code)}")

# 5. DECODING TAB
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
            st.error("Error! Please check your formatting.")




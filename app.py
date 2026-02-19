import streamlit as st

# Your Coordinate Map
char_to_coord = {
    '1': (1, 5), '2': (3, 5), '3': (5, 5), '4': (7, 5), '5': (9, 5),
    '6': (11, 5), '7': (13, 5), '8': (15, 5), '9': (17, 5), '0': (19, 5),
    'Q': (1, 4), 'W': (3, 4), 'E': (5, 4), 'R': (7, 4), 'T': (9, 4),
    'Y': (11, 4), 'U': (13, 4), 'I': (15, 4), 'O': (17, 4), 'P': (19, 4),
    'A': (2, 3), 'S': (4, 3), 'D': (6, 3), 'F': (8, 3), 'G': (10, 3),
    'H': (12, 3), 'J': (14, 3), 'K': (16, 3), 'L': (18, 3),
    'Z': (4, 2), 'X': (6, 2), 'C': (8, 2), 'V': (10, 2), 'B': (12, 2),
    'N': (14, 2), 'M': (16, 2),
    '!': (3, 1), ',': (4, 1), ' ': (10, 1), '.': (16, 1), '?': (17, 1)
}
coord_to_char = {v: k for k, v in char_to_coord.items()}

# UI Styling
st.title("🛰️ Vector Movement Cipher")
st.markdown("Share secret messages using coordinate displacements.")

tab1, tab2 = st.tabs(["Encode Message", "Decode Vectors"])

with tab1:
    st.header("Create a Cipher")
    msg_input = st.text_input("Enter message:", value="HELLO")
    
    if msg_input:
        msg = msg_input.upper()
        coords = [char_to_coord[c] for c in msg if c in char_to_coord]
        
        if coords:
            st.subheader(f"Start Point: {coords[0]}")
            
            # Formatting the output like your example
            full_code = []
            for i in range(len(coords) - 1):
                x1, y1 = coords[i]
                x2, y2 = coords[i+1]
                dx, dy = x2 - x1, y2 - y1
                
                st.write(f"**{msg[i]} → {msg[i+1]}**")
                st.code(f"dx = {x2} - {x1} = {dx}\ndy = {y2} - {y1} = {dy}\nVector = ({dx}, {dy})")
                full_code.append(f"({dx},{dy})")
            
            st.success("Sharable Code:")
            st.code(f"START: {coords[0]} | MOVES: {' '.join(full_code)}")

with tab2:
    st.header("Read a Cipher")
    col1, col2 = st.columns(2)
    with col1:
        start_in = st.text_input("Start Point (e.g. 12,3):", value="12,3")
    with col2:
        vector_in = st.text_area("Vectors (e.g. -7,1 13,-1):")

    if st.button("Decode"):
        try:
            # Parse Start Point
            sx, sy = map(int, start_in.split(','))
            curr = (sx, sy)
            decoded = [coord_to_char.get(curr, "?")]
            
            # Parse Vectors
            # Cleans up the input to find pairs of numbers
            import re
            moves = re.findall(r"(-?\d+),(-?\d+)", vector_in)
            
            for dx, dy in moves:
                curr = (curr[0] + int(dx), curr[1] + int(dy))
                decoded.append(coord_to_char.get(curr, "?"))
            
            st.info(f"Decoded Message: {''.join(decoded)}")
        except Exception as e:
            st.error("Check your formatting! Use 'x,y' for start and '(x,y)' for moves.")

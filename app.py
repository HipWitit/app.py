import streamlit as st
import re

# 1. THE COORDINATE MAP (Based on your 30x30 setup)
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
        # Fixed: Now perfectly mirrors the transform swap
        return (30 - y), (30 - x)
    elif key == "SIMON S




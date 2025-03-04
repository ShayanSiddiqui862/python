import streamlit as st


units_data = {
    "length": {
        "units": ["m", "cm", "mm", "km", "in", "ft", "yd", "mi"],
        "conversion": {
            "m": 1,
            "cm": 100,
            "mm": 1000,
            "km": 0.001,
            "in": 39.3701,
            "ft": 3.28084,
            "yd": 1.09361,
            "mi": 0.000621371
        }
    },
    "temperature": {
        "units": ["C", "F", "K"],
        "conversion": {
            "C": {"F": lambda x: x * 9/5 + 32, "K": lambda x: x + 273.15},
            "F": {"C": lambda x: (x - 32) * 5/9, "K": lambda x: (x + 459.67) * 5/9},
            "K": {"C": lambda x: x - 273.15, "F": lambda x: x * 9/5 - 459.67}
        }
    },
    "volume": {
        "units": ["m3", "cm3", "mm3", "L", "ml", "gal", "qt", "pt", "cup", "fl oz"],
        "conversion": {
            "m3": 1,
            "cm3": 1e6,
            "mm3": 1e9,
            "L": 1000,
            "ml": 1e6,
            "gal": 264.172,
            "qt": 1056.69,
            "pt": 2113.38,
            "cup": 4166.67,
            "fl oz": 33814
        }
    },
    "weight": {
        "units": ["kg", "g", "mg", "lb", "oz"],
        "conversion": {
            "kg": 1,
            "g": 1000,
            "mg": 1e6,
            "lb": 2.20462,
            "oz": 35.274
        }
    },
    "area": {
        "units": ["m2", "cm2", "mm2", "ha", "km2", "in2", "ft2", "yd2", "ac"],
        "conversion": {
            "m2": 1,
            "cm2": 1e4,
            "mm2": 1e6,
            "ha": 0.0001,
            "km2": 1e-6,
            "in2": 1550,
            "ft2": 10.7639,
            "yd2": 1.19599,
            "ac": 0.000247105
        }
    },
    "time": {
        "units": ["s", "min", "h", "day", "week", "month", "year"],
        "conversion": {
            "s": 1,
            "min": 60,
            "h": 3600,
            "day": 86400,
            "week": 604800,
            "month": 2628000,
            "year": 31536000
        }
    },
    "speed": {
        "units": ["m/s", "km/h", "mph", "knot"],
        "conversion": {
            "m/s": 1,
            "km/h": 3.6,
            "mph": 2.23694,
            "knot": 1.94384
        }
    },
    "pressure": {  
        "units": ["Pa", "kPa", "MPa", "bar", "psi", "ksi"],
        "conversion": {
            "Pa": 1,
            "kPa": 0.001,
            "MPa": 1e-6,
            "bar": 1e-5,
            "psi": 0.000145038,
            "ksi": 1.45038e-7
        }
    }
}


def get_units(category):
    if category in units_data:
        return units_data[category]["units"]
    return []


def convert(category, value, from_unit, to_unit):
    if category not in units_data:
        return None
    
    conversion = units_data[category]["conversion"]
    
    if category == "temperature":
        if from_unit == to_unit:
            return value
        return conversion[from_unit][to_unit](value)
    
   
    base_value = value / conversion[from_unit] 
    return base_value * conversion[to_unit]  


st.title("Unit Converter")

categories = ["Length", "Temperature", "Volume", "Weight", "Area", "Time", "Speed", "Pressure"]
category = st.selectbox("Select a category", categories).lower()

units = get_units(category)
if not units:
    st.error("Units not defined for this category.")
    st.stop()

col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    input_value = st.number_input("Enter the value", value=1.0)
with col3:
    output_placeholder = st.empty()

col1, col2 = st.columns(2)
with col1:
    input_unit = st.selectbox("From", units)
with col2:
    output_unit = st.selectbox("To", units)

if st.button("Convert"):
    result = convert(category, input_value, input_unit, output_unit)
    output_placeholder.write(f"{result:.5f} {output_unit}")

import streamlit as st
from pint import UnitRegistry

# Initialize Unit Registry
ureg = UnitRegistry()

# Streamlit App Title
st.title("Ultimate Unit Converter")
st.write("Convert between different units of measurement")
st.markdown(
    "<div style=' color: blue; font-size: 20px;'>created by Hassan Ali Junejo!</div>",
    unsafe_allow_html=True
)

# Sidebar Theme Selection
themes = ["Light", "Dark", "Blue", "Green"]
with st.sidebar:
    selected_theme = st.selectbox("Select Theme", themes)

# Apply Theme
if selected_theme == "Dark":
    st.markdown(
        """
        <style>
            body, .stApp { background-color: #121212; color: #ffffff; }
            .stButton>button { background-color: #333333; color: white; border-radius: 5px; }
            .stNumberInput input, .stSelectbox div[data-baseweb="select"] { background-color: #333333; color: white; }
        </style>
        """, 
        unsafe_allow_html=True
    )
elif selected_theme == "Blue":
    st.markdown(
        """
        <style>
            body, .stApp { background-color: #001f3f; color: #ffffff; }
            .stButton>button { background-color: #0074D9; color: white; border-radius: 5px; }
            .stNumberInput input, .stSelectbox div[data-baseweb="select"] { background-color: #0074D9; color: white; }
        </style>
        """, 
        unsafe_allow_html=True
    )
elif selected_theme == "Green":
    st.markdown(
        """
        <style>
            body, .stApp { background-color: #004d00; color: #ffffff; }
            .stButton>button { background-color: #2ECC40; color: white; border-radius: 5px; }
            .stNumberInput input, .stSelectbox div[data-baseweb="select"] { background-color: #2ECC40; color: white; }
        </style>
        """, 
        unsafe_allow_html=True
    )

# Categories of Units
categories = [
    "Length", "Mass", "Temperature", "Speed", "Volume", "Area", "Time",
    "Frequency", "Angle", "Force", "Pressure", "Energy", "Electric Current",
    "Power", "Voltage", "Resistance", "Digital Storage", "Fuel Consumption"
]

# Select Category
category = st.selectbox("Select Category", categories)

# Input value
value = st.number_input("Enter value to convert", format="%.4f")

# Dictionary of example units for each category
units_dict = {
    "Length": ["meter", "kilometer", "mile", "inch", "foot"],
    "Mass": ["gram", "kilogram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour"],
    "Volume": ["liter", "milliliter", "gallon", "cubic meter"],
    "Area": ["square meter", "square kilometer", "hectare", "acre"],
    "Time": ["second", "minute", "hour", "day"],
    "Frequency": ["hertz", "kilohertz", "megahertz"],
    "Angle": ["degree", "radian"],
    "Force": ["newton", "dyne"],
    "Pressure": ["pascal", "bar", "psi"],
    "Energy": ["joule", "calorie", "kilowatt_hour"],
    "Electric Current": ["ampere", "milliampere"],
    "Power": ["watt", "kilowatt", "horsepower"],
    "Voltage": ["volt", "kilovolt"],
    "Resistance": ["ohm", "kiloohm"],
    "Digital Storage": ["byte", "kilobyte", "megabyte", "gigabyte"],
    "Fuel Consumption": ["kilometer/liter", "mile/gallon"]
}

# Unit selections
unit_from = st.selectbox("From", units_dict[category])
unit_to = st.selectbox("To", units_dict[category])

if st.button("Convert"):
    try:
        if category == "Temperature":
            if unit_from == "celsius" and unit_to == "fahrenheit":
                result = (value * 9/5) + 32
            elif unit_from == "fahrenheit" and unit_to == "celsius":
                result = (value - 32) * 5/9
            elif unit_from == "celsius" and unit_to == "kelvin":
                result = value + 273.15
            elif unit_from == "kelvin" and unit_to == "celsius":
                result = value - 273.15
            elif unit_from == "fahrenheit" and unit_to == "kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif unit_from == "kelvin" and unit_to == "fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                raise ValueError("Invalid Temperature Conversion")
        else:
            result = (value * ureg(unit_from)).to(unit_to)
        st.success(f"{value} {unit_from} = {result:.4f} {unit_to}")
    except Exception as e:
        st.error(f"Conversion Error: {e}")

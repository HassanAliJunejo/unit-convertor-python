import streamlit as st

# Title
st.title("Unit Converter")
st.write("Convert units between Length, Weight, and Temperature")

# Sidebar for unit selection
option = st.sidebar.selectbox(
    "Select Conversion Type:",
    ("Length", "Weight", "Temperature")
)

if option == "Length":
    st.header("Length Converter")
    length_units = {"Meters": 1, "Kilometers": 1000, "Centimeters": 0.01, "Miles": 1609.34}
    input_unit = st.selectbox("From:", list(length_units.keys()))
    output_unit = st.selectbox("To:", list(length_units.keys()))
    value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = value * (length_units[input_unit] / length_units[output_unit])
        st.success(f"{value} {input_unit} is equal to {result:.2f} {output_unit}")

elif option == "Weight":
    st.header("Weight Converter")
    weight_units = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
    input_unit = st.selectbox("From:", list(weight_units.keys()))
    output_unit = st.selectbox("To:", list(weight_units.keys()))
    value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = value * (weight_units[input_unit] / weight_units[output_unit])
        st.success(f"{value} {input_unit} is equal to {result:.2f} {output_unit}")

elif option == "Temperature":
    st.header("Temperature Converter")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    input_unit = st.selectbox("From:", temp_units)
    output_unit = st.selectbox("To:", temp_units)
    value = st.number_input("Enter Value:", format="%.2f")
    
    def convert_temperature(value, input_unit, output_unit):
        if input_unit == output_unit:
            return value
        elif input_unit == "Celsius" and output_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif input_unit == "Celsius" and output_unit == "Kelvin":
            return value + 273.15
        elif input_unit == "Fahrenheit" and output_unit == "Celsius":
            return (value - 32) * 5/9
        elif input_unit == "Fahrenheit" and output_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif input_unit == "Kelvin" and output_unit == "Celsius":
            return value - 273.15
        elif input_unit == "Kelvin" and output_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

    if st.button("Convert"):
        result = convert_temperature(value, input_unit, output_unit)
        st.success(f"{value} {input_unit} is equal to {result:.2f} {output_unit}")
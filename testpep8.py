import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def user_input_features():
    make = st.text_input("Enter make:")
    model = st.text_input("Enter model:")
    year = st.text_input("Enter year:")
    kms = st.text_input("Enter kms driven:")
    return {"make": make, "model": model, "year": year, "kms": kms}

def get_car_details(user_input):
    # Here you can fetch the car details from a database or API.
    # For now, let's return dummy data.
    car_data = {
        "make": user_input["make"],
        "model": user_input["model"],
        "year": user_input["year"],
        "kms": user_input["kms"],
    }
    return car_data

def display_car_details(car_data):
    st.subheader("Car Details")
    st.write(f"Make: {car_data['make']}")
    st.write(f"Model: {car_data['model']}")
    st.write(f"Year: {car_data['year']}")
    st.write(f"Kms: {car_data['kms']}")

def main():
    st.title("Car User Search")
    user_input = user_input_features()
    car_data = get_car_details(user_input)
    display_car_details(car_data)

if __name__ == "__main__":
    main()

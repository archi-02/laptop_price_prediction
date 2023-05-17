import streamlit as st
import pickle
import pandas as pd

df = pickle.load(open("df.pkl", "rb"))
pipe_xgb = pickle.load(open("pipe.pkl", "rb"))

st.title("Laptop price predictor")
company = st.selectbox("Brand Name", df["Company"].unique())
type = st.selectbox("Laptop Type", df["TypeName"].unique())
sc_size = st.number_input("Screen Size (Inches)")
sc_resolution = st.selectbox("Screen Resolution", ['2560x1600', '1440x900', '1920x1080', '2880x1800', '1366x768', '2304x1440', '3200x1800', '1920x1200', '2256x1504', '3840x2160', '2160x1440', '2560x1440', '1600x900', '2736x1824', '2400x1600'])
processor = st.selectbox("Processor", df["Processor"].unique())
ghz = st.number_input("GHz of Processor")
os = st.selectbox("Operating System", df["OS"].unique())
gpu = st.selectbox("GPU", df["Gpu"].unique())
ssd = st.selectbox("SSD",[0,8,16,32,64,128,180,240,256,512,1000])
hdd = st.selectbox("HDD",[0,32,128,500,1000,2000])
flash = st.selectbox("Flash",[0,16,32,64,128,256,512])
hybrid = st.selectbox("Hybrid",[0,508,1000])
ram = st.selectbox("RAM (GB)", [2,4,6,8,12,16,24,32,64])
weight = st.number_input("Weight of Laptop")
ips = st.selectbox("IPS Panel", df["IPS Panel"].unique())
retina = st.selectbox("Retina Display", df["Retina Display"].unique())
touchscreen = st.selectbox("Touchscreen", df["Touchscreen"].unique())
quad = st.selectbox("Quad HD+", df["Quad HD+"].unique())
full = st.selectbox("Full HD", df["Full HD"].unique())
ultra  = st.selectbox("4K ULtra HD", df["4K Ultra HD"].unique())

if st.button("Predict Price"):

   x = float(sc_resolution.split("x")[0])
   y = float(sc_resolution.split("x")[1])
   if sc_size != 0:
      ppi = (((x ** 2) + (y ** 2)) ** 0.5) / sc_size
   else:
      ppi = 0

   query = pd.DataFrame([[company, type, sc_size, ppi, processor, ghz, os, gpu, ssd, hdd, flash, hybrid, ram, weight,
                           ips, retina, touchscreen, quad, full, ultra]],
                         columns=["Company", "TypeName", "Inches", "ppi", "Processor", "GHz", "OS", "Gpu", "SSD",
                                  "HDD", "Flash", "Hybrid", "Ram(GB)", "Weight", "IPS Panel", "Retina Display",
                                  "Touchscreen", "Quad HD+", "Full HD", "4K Ultra HD"])
   predicted_price = pipe_xgb.predict(query)
   st.title(f"The predicted price is: {predicted_price[0]}")
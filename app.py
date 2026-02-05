import streamlit as st
import joblib
import pandas as pd
import re
from urllib.parse import urlparse

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Phishing Website Detection",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Phishing Website Detection System")
st.write("Enter a URL to check whether it is **Legitimate** or **Phishing**")

# ------------------ LOAD MODEL ------------------
model = joblib.load("phishing_detector_rf.pkl")

# VERY IMPORTANT: get exact feature names from trained model
feature_names = list(model.feature_names_in_)

# ------------------ FEATURE EXTRACTION ------------------
def extract_features(url, feature_names):
    features = {}

    # URL-based real-time features
    features["having_IP_Address"] = -1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 1
    features["URL_Length"] = -1 if len(url) >= 75 else 1
    features["Shortining_Service"] = -1 if any(x in url for x in ["bit.ly", "tinyurl", "goo.gl"]) else 1
    features["having_At_Symbol"] = -1 if "@" in url else 1
    features["double_slash_redirecting"] = -1 if url.count("//") > 1 else 1
    features["Prefix_Suffix"] = -1 if "-" in urlparse(url).netloc else 1

    subdomain_count = urlparse(url).netloc.count(".")
    features["having_Sub_Domain"] = -1 if subdomain_count > 2 else 1

    features["SSLfinal_State"] = 1 if url.startswith("https") else -1

    # All unavailable features → Suspicious (0)
    for fname in feature_names:
        if fname not in features:
            features[fname] = 0

    # Create dataframe in exact training order
    df = pd.DataFrame([features])[feature_names]
    return df

# ------------------ USER INPUT ------------------
url = st.text_input("🔗 Enter Website URL")

# ------------------ PREDICTION ------------------
if st.button("Check Website"):
    if url.strip() == "":
        st.warning("⚠️ Please enter a valid URL")
    else:
        input_data = extract_features(url, feature_names)

        prediction = model.predict(input_data)[0]
        proba = model.predict_proba(input_data)[0]
        confidence = max(proba) * 100

        if prediction == -1:
            st.error(f"🚨 **Phishing Website Detected**\n\nConfidence: **{confidence:.2f}%**")
        else:
            st.success(f"✅ **Legitimate Website**\n\nConfidence: **{confidence:.2f}%**")

        # Debug info (optional — comment out later)
        with st.expander("🔍 Feature Values Used"):
            st.dataframe(input_data)

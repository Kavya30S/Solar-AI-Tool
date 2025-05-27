import streamlit as st
from utils.image_processing import preprocess_image
from utils.api_calls import analyze_image
from utils.solar_calculations import calculate_solar_potential
from utils.logging_config import setup_logging
from PIL import Image
import os

# Initialize logging
setup_logging()

st.title("AI-Powered Rooftop Solar Analysis Tool")

st.header("Upload Satellite Image")
uploaded_file = st.file_uploader("Choose a satellite image...", type=["jpg", "png"])

if uploaded_file is not None:
    # Save uploaded file
    image_path = os.path.join("static", uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image(uploaded_file, caption="Uploaded Satellite Image", use_column_width=True)

    # Preprocess image with timing
    result, preprocess_duration = preprocess_image(image_path)
    if isinstance(result, dict) and "error" in result:
        st.error(f"Image processing error: {result['error']}")
    else:
        # Analyze image with timing
        analysis_result, api_duration = analyze_image(image_path)
        if "error" in analysis_result:
            st.error(f"Analysis error: {analysis_result['error']}")
        else:
            st.header("Analysis Results")
            st.write(f"**Roof Area**: {analysis_result['roof_area_m2']} m²")
            st.write(f"**Obstacles Detected**: {', '.join(analysis_result['obstacles'])}")
            st.write(f"**Orientation**: {analysis_result['orientation']}")
            st.write(f"**Tilt**: {analysis_result['tilt']}°")

            # Calculate solar potential
            solar_results = calculate_solar_potential(
                analysis_result['roof_area_m2'],
                analysis_result['orientation'],
                analysis_result['tilt']
            )
            st.header("Solar Potential and ROI")
            st.write(f"**Effective Roof Area**: {solar_results['effective_area_m2']:.2f} m²")
            st.write(f"**Daily Energy Production**: {solar_results['daily_energy_kwh']:.2f} kWh")
            st.write(f"**Annual Energy Production**: {solar_results['annual_energy_kwh']:.2f} kWh")
            st.write(f"**System Size**: {solar_results['system_size_kw']:.2f} kW")
            st.write(f"**Installation Cost**: ${solar_results['installation_cost_usd']:.2f}")
            st.write(f"**Annual Savings**: ${solar_results['annual_savings_usd']:.2f}")
            st.write(f"**Payback Period**: {solar_results['payback_period_years']:.2f} years")

            # Display performance metrics
            st.header("Performance Metrics")
            st.write(f"**Image Processing Time**: {preprocess_duration:.3f} seconds")
            st.write(f"**API Call Time**: {api_duration:.3f} seconds")
            st.write(f"Metrics are also logged to 'metrics.log' in the project directory.")

st.header("Example Analysis")
st.write("Try uploading a sample image from the 'static' folder, e.g., 'sample_image.jpg'.")
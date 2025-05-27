 This project is an AI-powered tool that analyzes satellite imagery to assess rooftop solar potential, providing installation recommendations and ROI estimates.

 ## Project Setup

 ### Prerequisites
 - Python 3.8+
 - OpenRouter API key (sign up at https://openrouter.ai/)
 - Git (optional for version control)

 ### Installation
 1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/solar-ai-tool.git
    cd solar-ai-tool
    ```
 2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
 3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
 4. Set up the OpenRouter API key:
    - Create a `.env` file in the project root with:
      ```bash
      OPENROUTER_API_KEY=your-api-key-here
      ```

 ### Running the Application
 1. Start the Streamlit app:
    ```bash
    streamlit run app.py
    ```
 2. Open your browser to `http://localhost:8501`.
 3. Upload a satellite image to analyze rooftop solar potential.
 ---
title: Solar AI Tool
emoji: ☀️
colorFrom: yellow
colorTo: green
sdk: streamlit
sdk_version: 1.35.0
app_file: app.py
pinned: false
license: MIT
---

# AI-Powered Rooftop Solar Analysis Tool

This tool analyzes satellite imagery to estimate rooftop solar potential, including roof area, obstacles, and return on investment (ROI). Upload a satellite image to get started!

## Features
- Image processing to detect roof characteristics
- Mock API for rooftop analysis
- Solar potential and ROI calculations
- Performance metrics for processing and API calls

## Usage
1. Upload a satellite image (e.g., `static/sample_image.jpg`).
2. View analysis results and performance metrics.
3. Check `metrics.log` for detailed logs.

## Requirements
See `requirements.txt` for dependencies.

 ### Example Usage
 - Upload a satellite image of a rooftop (e.g., `static/sample_image.jpg`).
 - The tool will analyze the roof for area, obstacles, orientation, and tilt.
 - It will calculate solar potential, system size, costs, savings, and payback period.

 ## Implementation Details
 - **AI Integration**: Uses OpenRouter API for image analysis (mocked in this version).
 - **Image Processing**: Resizes and preprocesses images using PIL.
 - **Solar Calculations**: Estimates energy production and ROI based on roof characteristics.
 - **Web Interface**: Built with Streamlit for user-friendly interaction.

 ## Future Improvements
 - Integrate a real vision model via OpenRouter for accurate image analysis.
 - Add support for multiple locations with location-specific irradiance data.
 - Implement user authentication for secure API key handling.
 - Enhance UI with 3D roof visualizations and interactive maps.

 ## Example Analysis
 Upload `static/sample_image.jpg` to see results like:
 - Roof Area: 100 m²
 - Obstacles: Chimney, Vent
 - Orientation: South
 - Tilt: 30°
 - Solar Potential: ~5 kWh/day, ~1825 kWh/year
 - Payback Period: ~8 years
 
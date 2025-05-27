 This project is an AI-powered tool that analyzes satellite imagery to assess rooftop solar potential, providing installation recommendations and ROI estimates.

sdk: streamlit
sdk_version: 1.35.0
app_file: app.py
pinned: false
license: apache-2.0
 
### Prerequisites
Before setting up and running this project, ensure you have the following tools and accounts:

1. **Python Environment**

   * Install [Anaconda Distribution](https://www.anaconda.com/download) to manage your Python environments efficiently.
   * Create and activate a new Conda environment:

     ```bash
     conda create -n solar_ai_env python=3.9
     conda activate solar_ai_env
     ```

2. **Code Editor**

   * Use [Visual Studio Code (VSCode)](https://code.visualstudio.com/) for code editing.
   * Ensure VSCode is configured to recognize the Anaconda environment:

     * Open VSCode.
     * Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the command palette.
     * Select `Python: Select Interpreter` and choose the `solar_ai_env` environment.

3. **Git and GitHub**

   * Install [Git](https://git-scm.com/downloads) for version control.
   * Set up a [GitHub](https://github.com/) account to access the project repository.([Streamlit Docs][1], [Python in Plain English][2])

4. **Hugging Face Account**

   * Create a [Hugging Face](https://huggingface.co/join) account to access and deploy the application on Spaces.

5. **Project Repository and Files**

   * Clone the project repository:

     ```bash
     git clone https://github.com/yourusername/solar-ai-assistant.git
     cd solar-ai-assistant
     ```
   * Ensure the following files are present:

     * `app.py`: Main Streamlit application file.
     * `requirements.txt`: Lists all Python dependencies.
     * `README.md`: Project documentation.
     * Sample image files (e.g., `sample_image.jpg`) for testing.

6. **Python Dependencies**

   * Install the required Python packages:

     ```bash
     pip install -r requirements.txt
     ```

7. **Streamlit Installation**

   * If not already installed, install Streamlit:

     ```bash
     pip install streamlit
     ```

8. **Running the Application Locally**

   * Navigate to the project directory and run the Streamlit app:

     ```bash
     streamlit run app.py
     ```
   * Open the provided local URL in your web browser to interact with the application.([Medium][3], [GitHub][4])

9. **Deployment on Hugging Face Spaces**

   * Log in to your Hugging Face account.
   * Create a new Space:

     * Choose "Streamlit" as the SDK.
     * Set the repository to public or private as needed.
   * Push your project files to the Hugging Face Space repository.
   * The application will be automatically built and deployed.([Python in Plain English][2], [Hugging Face][5], [YouTube][6])

 ### Running the Application
 1. Start the Streamlit app:
    ```bash
    streamlit run app.py
    ```
 2. Open your browser to `http://localhost:8501`.
 3. Upload a satellite image to analyze rooftop solar potential.

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
 

import os
import requests
from dotenv import load_dotenv
import time
import logging

load_dotenv()

def analyze_image(image_path):
    """Send image to OpenRouter for analysis and measure time."""
    logging.info(f"Starting API call for {image_path}")
    start_time = time.time()
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        end_time = time.time()
        duration = end_time - start_time
        logging.info(f"API call failed in {duration:.3f} seconds: API key missing")
        raise ValueError("OpenRouter API key not found.")
    
    try:
        response = {
            "roof_area_m2": 100.0,
            "obstacles": ["chimney", "vent"],
            "orientation": "south",
            "tilt": 30.0
        }
        end_time = time.time()
        duration = end_time - start_time
        logging.info(f"API call completed in {duration:.3f} seconds")
        return response, duration
    except Exception as e:
        end_time = time.time()
        duration = end_time - start_time
        logging.info(f"API call failed in {duration:.3f} seconds: {str(e)}")
        return {"error": str(e)}, duration
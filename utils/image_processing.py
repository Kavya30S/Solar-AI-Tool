from PIL import Image
import numpy as np
import time
import logging

def preprocess_image(image_path):
    """Preprocess satellite image for analysis and measure time."""
    logging.info(f"Starting image processing for {image_path}")
    start_time = time.time()
    
    try:
        img = Image.open(image_path)
        img = img.resize((512, 512))
        img_array = np.array(img)
        end_time = time.time()
        duration = end_time - start_time
        logging.info(f"Image processing completed in {duration:.3f} seconds")
        return img_array, duration
    except Exception as e:
        end_time = time.time()
        duration = end_time - start_time
        logging.info(f"Image processing failed in {duration:.3f} seconds: {str(e)}")
        return {"error": str(e)}, duration
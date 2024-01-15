# Image Data Extractor Application (Gen Ai)

## Overview
This Streamlit application leverages the Gemini API to process and extract information from uploaded images, specifically designed for understanding invoices. Users can input prompts and receive responses based on the content of the images.

## Features
- Upload an image in JPG, JPEG, or PNG format.
- Enter a prompt related to the image content.
- Click the "See image details as per input prompt" button to generate responses.

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/MangeshKendre/Gen-Ai---data imf -extracter.git
    cd Gen-Ai---data imf --extracter
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
   - Create a `.env` file in the project directory.
   - Add your Google API key:
     ```env
     GOOGLE_API_KEY=your_api_key_here
     ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

5. Access the app in your browser: http://localhost:8501

## Screenshots
Include screenshots or GIFs demonstrating the app in action.

## Technologies Used
- Streamlit
- Google Gemini API
- Python

## Dependencies
- streamlit
- google-generativeai
- pillow

## Contributing
Feel free to contribute by opening issues or submitting pull requests.

## License
This project is licensed under the [MIT License](LICENSE).


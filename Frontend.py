﻿import streamlit as st
import time
import re

# Function to check if the URL is from YouTube
def is_youtube_url(url):
    pattern = r"(?:https:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?([a-zA-Z0-9_-]{11})"
    return re.match(pattern, url)

def main():
    # Set the page title and icon
    st.set_page_config(page_title="IntelliScript", page_icon="📚")

    st.markdown(
        """
        <style>
            body {
                background-color: #f8f0ff; /* Updated background color */
                margin: 0; /* Remove default margin */
                padding: 0; /* Remove default padding */
                display: flex;
                flex-direction: column;
                justify-content: center; /* Center content vertically */
                align-items: center; /* Center the title horizontally */
                height: 100vh; /* Set the height of the container to the full viewport height */
            }
            .custom-title-container {
                position: relative;
                display: inline-block;
                text-align: center; /* Center the title text horizontally */
            }
            .custom-title-text {
                font-size: 48px; /* Font size for the title text */
                font-weight: bold;
                margin-bottom: 15px; /* Reduce space between title and content below */
                position: relative; /* Add positioning for glitter */
            }
            .custom-title-text::before {
                content: "";
                display: block;
                position: absolute;
                top: -10px;
                left: -10px;
                width: calc(100% + 20px);
                height: calc(100% + 20px);
                border: 2px solid transparent;
                border-radius: 50%;
                box-shadow: 0 0 20px rgba(123, 104, 238, 0.8), 0 0 40px rgba(123, 104, 238, 0.8), 0 0 60px rgba(123, 104, 238, 0.8), 0 0 80px rgba(123, 104, 238, 0.8), 0 0 100px rgba(123, 104, 238, 0.8);
                opacity: 0;
                animation: shadow-glow 2s infinite;
            }
            .custom-title-text::after {
                content: "";
                display: block;
                position: absolute;
                top: -10px;
                left: -10px;
                width: calc(100% + 20px);
                height: calc(100% + 20px);
                border: 2px solid transparent;
                border-radius: 50%;
                box-shadow: 0 0 10px rgba(123, 104, 238, 0.8), 0 0 20px rgba(123, 104, 238, 0.8), 0 0 30px rgba(123, 104, 238, 0.8), 0 0 40px rgba(123, 104, 238, 0.8), 0 0 50px rgba(123, 104, 238, 0.8);
                opacity: 0;
                animation: shadow-glow 3s infinite;
            }
            @keyframes shadow-glow {
                0%, 100% {
                    opacity: 0;
                }
                50% {
                    opacity: 0.75;
                }
            }
            .caution-text {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
                color: yellow; /* Updated color to normal yellow */
            }
            .error-text {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
                color: #ff0000; /* Updated color to red */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title container with updated design
    st.markdown(
        """
        <div class="custom-title-container">
            <h1 class="custom-title-text">IntelliScript</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add space between the title and the content below it
    st.markdown("---")

    # Initialize input_option as "choose your input"
    input_option = st.radio("Choose your input:", ("Enter a link", "Upload an audio file", "Download a YouTube video"))

    if input_option == "Enter a link":
        # Display caution for link input
        st.markdown('<p class="caution-text">Please enter the full URL of the YouTube video.</p>', unsafe_allow_html=True)
        # Textbox for YouTube video link
        youtube_link = st.text_input("Enter YouTube video link")

        # Button to generate transcript
        if st.button("Get Transcript"):
            if not youtube_link:
                st.markdown('<p class="error-text">Please enter a valid YouTube video link.</p>', unsafe_allow_html=True)
            else:
                # Check if the entered URL is from YouTube
                if is_youtube_url(youtube_link):
                    with st.spinner("Processing..."):
                        # Simulate processing delay
                        time.sleep(3)
                        # Assume transcript is generated and stored in 'transcript'
                        transcript = ""
                        st.write("Transcript:")
                        st.write(transcript)
                else:
                    st.markdown('<p class="error-text">Please enter a valid YouTube video link.</p>', unsafe_allow_html=True)

        # Add code to handle download of the generated transcript
        if 'transcript' in locals() and st.button("Download"):
            with st.spinner("Downloading transcript..."):
                # Simulate download delay
                time.sleep(5)
                # Add code to download the transcript file
                st.text("Download link here...")

    elif input_option == "Upload an audio file":
        # Hide the caution message for other options
        st.markdown("")
        # File uploader for audio file
        uploaded_file = st.file_uploader("Upload an audio file", type=["mp3"])

        if uploaded_file is not None:
            st.write("File uploaded successfully.")
        
        # Button to generate transcript
        if st.button("Get Transcript"):
            if uploaded_file is not None:
                with st.spinner("Processing..."):
                    # Simulate processing delay
                    time.sleep(3)
                    # Assume transcript is generated and stored in 'transcript'
                    transcript = ""
                    st.write("Transcript:")
                    st.write(transcript)
        
        # Add code to handle download of the generated transcript
        if 'transcript' in locals() and st.button("Download"):
            with st.spinner("Downloading transcript..."):
                # Simulate download delay
                time.sleep(3)
                # Add code to download the transcript file
                st.text("Download link here...")

    elif input_option == "Download a YouTube video":
        st.write("## YouTube Video Downloader")
        # Display caution for link input
        st.markdown('<p class="caution-text">Please enter the full URL of the YouTube video.</p>', unsafe_allow_html=True)
        # Textbox for YouTube video link
        youtube_link = st.text_input("Enter YouTube video link")

        # Hide the caution message if a link is provided
        if youtube_link:
            st.markdown("")

        # Dropdown to choose operation (Full Video or Video Clips)
        operation = st.radio("Choose:", ("Full Video", "Video Clips"))

        if operation == "Full Video":
            # Button to download the video
            if st.button("Download Video"):
                if is_youtube_url(youtube_link):
                    with st.spinner("Downloading video..."):
                        # Simulate download delay
                        time.sleep(3)
                        # Add code to download the video file
                        st.text("Video downloaded.")
                else:
                    st.markdown('<p class="error-text">Please enter a valid YouTube video link.</p>', unsafe_allow_html=True)

        elif operation == "Video Clips":
            # Ask for start time
            start_time = st.text_input("Enter start time:")

            # Ask for end time
            end_time = st.text_input("Enter end time:")

            # Button to generate clip
            if st.button("Generate Clip"):
                if is_youtube_url(youtube_link) and start_time and end_time:
                    with st.spinner("Generating video clip..."):
                        # Simulate clip generation delay
                        time.sleep(3)
                        st.text("Video clip generated.")
                else:
                    st.markdown('<p class="error-text">Please enter a valid YouTube video link and both start and end times.</p>', unsafe_allow_html=True)

    # Summarization block
    sumhead = """
    <style>
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
        }
        
        .header {
            background-color: #2FACB6; /* Change this to the desired background color */
            color: #FFFFFF;
            padding: 10px;
            border-radius: 10px;
            font-size: 24px;
            text-align: center;
            animation: pulsating-glow 2s ease-in-out infinite; /* Add pulsating silver glow animation */
        }
        
        .summarization-container {
            background-color: #C0C0C0; /* Use a light silver color for the summarization container */
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            animation: fadeInUp 1s;
        }
        
        @keyframes pulsating-glow {
            0% {
                box-shadow: 0 0 10px rgba(192, 192, 192, 0.7);
            }
            50% {
                box-shadow: 0 0 20px rgba(192, 192, 192, 0.9);
            }
            100% {
                box-shadow: 0 0 10px rgba(192, 192, 192, 0.7);
            }
        }
        
        @keyframes fadeInUp {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
    """
    st.markdown(sumhead, unsafe_allow_html=True)
    # Header container
    st.markdown("<div class='header-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='header'>Summarization</h1>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
        
    message_placeholder = st.empty()
    message_placeholder.info("Available models - \n 1) Google T5 \n  2) DistilBart", icon="ℹ")
    st.markdown("<br>", unsafe_allow_html=True)
    model_choice = st.selectbox("Select a model to perform summarization", [1, 2], key="model_choice")

    if model_choice == 1:  # Google T5 model selected
        # Add code for Google T5 summarization
        pass
    elif model_choice == 2:  # DistilBart model selected
        # Add code for DistilBart summarization
        pass

    # Add a button to perform summarization
    summarize_button = st.button("Summarize")

    # Perform summarization when the button is clicked
    if summarize_button:
        with st.spinner("Summarizing..."):
            # Simulate summarization process delay
            time.sleep(3)
            # Assume the summary is generated and stored in the 'summary' variable
            summary = ""
            st.markdown("#### Summary:")
            st.write(summary)

    # Add code to handle download of the summary
        summary_button = st.button("Download")

    # Translation block
    transhead = """
    <style>
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
        }
        
        .header {
            background-color: #2FACB6; /* Change this to the desired background color */
            color: #FFFFFF;
            padding: 10px;
            border-radius: 10px;
            font-size: 24px;
            text-align: center;
            animation: pulsating-glow 2s ease-in-out infinite; /* Add pulsating silver glow animation */
        }
        
        .summarization-container {
            background-color: #C0C0C0; /* Use a light silver color for the summarization container */
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            animation: fadeInUp 1s;
        }
        
        @keyframes pulsating-glow {
            0% {
                box-shadow: 0 0 10px rgba(192, 192, 192, 0.7);
            }
            50% {
                box-shadow: 0 0 20px rgba(192, 192, 192, 0.9);
            }
            100% {
                box-shadow: 0 0 10px rgba(192, 192, 192, 0.7);
            }
        }
        
        @keyframes fadeInUp {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
    """
    st.markdown(transhead, unsafe_allow_html=True)
    # Header container
    st.markdown("<div class='header-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='header'>Translation</h1>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    selected_language = st.selectbox("Select a language:", ["English", "Hindi", "Telugu", "Other"])

    # Button to perform translation
    translate_button = st.button("Translate")

    # Perform translation when the button is clicked
    if translate_button:
        with st.spinner("Translating..."):
            # Simulate translation process delay
            time.sleep(3)
            # Assume the translation is generated and stored in the 'translation' variable
            translation = f"Translated text in {selected_language}:\n\n"
            st.markdown("#### Translation:")
            st.write(translation)

    # Add code to handle download of the translated text
        translate_text_button = st.button("Download")
    
    # Audible summary block
    audible_summary = """
    <style>
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
        }
        
        .header {
            background-color: #2FACB6; /* Change this to the desired background color */
            color: #FFFFFF;
            padding: 10px;
            border-radius: 10px;
            font-size: 24px;
            text-align: center;
            animation: pulsating-glow 2s ease-in-out infinite; /* Add pulsating silver glow animation */
        }
        
        .summarization-container {
            background-color: #C0C0C0; /* Use a light silver color for the summarization container */
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            animation: fadeInUp 1s;
        }
        
        @keyframes pulsating-glow {
            0% {
                box-shadow: 0 0 10px rgba(192, 192, 192, 0.7);
            }
            50% {
                box-shadow: 0 0 20px rgba(192, 192, 192, 0.9);
            }
            100% {
                box-shadow: 0 0 10px rgba(192, 192, 192, 0.7);
            }
        }
        
        @keyframes fadeInUp {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
    """
    st.markdown(audible_summary, unsafe_allow_html=True)
    # Header container
    st.markdown("<div class='header-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='header'>Audible Summary</h1>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    selected_language = st.selectbox("Select a language for audible summary:", ["English", "Hindi", "Telugu", "Other"])

    # Button to perform translation
    audio_button = st.button("Generate Audio")

    # generate audio when the button is clicked
    if audio_button:
        with st.spinner("Generating..."):
            # Simulate audio summary process delay
            time.sleep(3)
            audio = f""
            st.markdown("#### Audio:")
            st.write(audio)
    
        # Add code to handle download of the generated audio
        audio_download_button = st.button("Download Audio")
if __name__ == "__main__":
    main()

import streamlit as st
import time
import re

# Function to check if the URL is from YouTube
def is_youtube_url(url):
    pattern = r"(?:https:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?([a-zA-Z0-9_-]{11})"
    return re.match(pattern, url)

def main():
    # Set the page title and icon
    st.set_page_config(page_title="Intelligent Transcript Summarizer", page_icon="📚")

    st.markdown(
        """
        <style>
            body {
                background-color: #F9B2DC; /* Background color */
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
            }
            .error-text {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
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
    input_option = st.radio("Choose your input:", ("Enter a link", "Upload an audio file", "Download a video"))

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

    elif input_option == "Download a video":
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
                if youtube_link:
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
                if youtube_link and start_time and end_time:
                    with st.spinner("Generating video clip..."):
                        # Simulate clip generation delay
                        time.sleep(3)
                        st.text("Video clip generated.")
                else:
                    st.markdown('<p class="error-text">Please enter a valid YouTube video link and both start and end times.</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
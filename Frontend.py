import streamlit as st
import time

def main():
    # Set the page title and icon
    st.set_page_config(page_title="Intelligent Transcript Summarizer", page_icon="📚")
    
    st.markdown(
        """
        <style>
            body {
                background-color: #F9B2DC; /*background */
                margin: 0; /* Remove default margin */
                padding: 0; /* Remove default padding */
            }
            .title-container {
                background-color: #51CACC; /*background for the title */
                padding: 10px;
                border-radius: 10px;
                text-align: center;
            }
            .title-text {
                color: #FFFFFF;
                font-size: 48px;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
                margin-bottom: 30px;
            }
            .animated-text {
                animation: fadeout 2s ease-in 1s forwards;
            }
            @keyframes fadeout {
                from {
                    opacity: 1;
                }
                to {
                    opacity: 0;
                }
            }
            .caution-text {
                color: #FF0000;
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .success-text {
                color: #00FF00;
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title container with highlighted text
    st.markdown(
        """
        <div class="title-container">
            <h1 class="title-text">IntelliScript</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Welcome text with animation
    welcome_text = st.markdown(
        """
        <div class="animated-text">
            <h3>Welcome to the Intelligent Transcript Summarizer!</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Initialize input_option as "choose your input"
    input_option = st.radio("Choose your input:", ("Enter a link", "Upload an audio file", "Download a video"))

    # Hide the welcome text after selecting the input option
    welcome_text.empty()

    if input_option == "Enter a link":
        # Display caution for link input
        st.markdown('<p class="caution-text">Please enter the full URL of the YouTube video.</p>', unsafe_allow_html=True)
        # Textbox for YouTube video link
        youtube_link = st.text_input("Enter YouTube video link")

        # Button to generate transcript
        if st.button("Get Transcript"):
            if youtube_link:
                # Add code to handle the transcript generation from the YouTube video link
                with st.spinner("Processing..."):
                    # Assume transcript is generated and stored in 'transcript'
                    transcript = ""
                    st.write("Transcript:")
                    st.write(transcript)
            else:
                st.write("Please enter a valid YouTube video link.")

        # Add code to handle download of the generated transcript
        if 'transcript' in locals() and st.button("Download"):
            with st.spinner("Downloading transcript..."):
                # download delay
                time.sleep(3)
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
        # Hide the caution message for other options
        st.markdown("")
        # Add code for handling video download here
        st.write("You chose to download a video.")

if __name__ == "__main__":
    main()

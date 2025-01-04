# File: pages/Download.py

import streamlit as st
from pytubefix import YouTube
from pytubefix.cli import on_progress

# Header for the app
st.header("Download Audio from YouTube")

# Sidebar with instructions
with st.sidebar:
    st.write("Instructions:")
    st.write("1. Enter the YouTube video URL.")
    st.write("2. Click 'Download Audio'.")

# Input field for YouTube URL
video_url = st.text_input("Enter the YouTube Video URL:", "")

# Button to initiate download
if st.button("Download Audio"):
    if video_url:
        try:
            # Create YouTube object
            yt = YouTube(video_url, on_progress_callback=on_progress)

            # Display video title
            st.write(f"Downloading: {yt.title}")

            # Get the audio stream
            ys = yt.streams.get_audio_only()

            # Download audio stream
            output_file = ys.download()

            st.success(f"Download complete: {output_file}")
            st.download_button(label="Download File", data=open(output_file, "rb").read(), file_name=output_file)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube URL.")

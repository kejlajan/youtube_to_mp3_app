import streamlit as st
from pytubefix import Playlist
from pytubefix.cli import on_progress
import os

# Header for the app
st.header("Download Playlist from YouTube")

# Sidebar with instructions
with st.sidebar:
    st.write("Instructions:")
    st.write("1. Enter the YouTube playlist URL.")
    st.write("2. Click 'Download Playlist'.")

# Input field for YouTube playlist URL
playlist_url = st.text_input("Enter the YouTube Playlist URL:", "")

# Button to initiate download
if st.button("Download Playlist"):
    if playlist_url:
        try:
            # Create Playlist object
            pl = Playlist(playlist_url)

            # Display playlist title
            st.write(f"Downloading playlist: {pl.title}")

            # Iterate over videos in the playlist
            for index, video in enumerate(pl.videos):
                st.write(f"Downloading video {index + 1}: {video.title}")
                ys = video.streams.get_audio_only()

                # Download audio stream
                output_file = ys.download()
                st.write(f"Downloaded: {output_file}")

            st.success("Playlist download complete!")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube playlist URL.")


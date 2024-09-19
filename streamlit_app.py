import streamlit as st
from PIL import Image
import os

st.title('ATLAS L0MDT Trigger Demo')

# Initialize session state for the folder and image counter
if 'folder_index' not in st.session_state:
    st.session_state.folder_index = 0
if 'image_index' not in st.session_state:
    st.session_state.image_index = 0

# Define the folder structure and list of folders (events)
base_dir = "images/"
events = [f"event{i}" for i in range(4)]  # This assumes the events are named event0, event1, etc.

# Function to get the images for the current folder
def get_images_in_event(folder):
    folder_path = os.path.join(base_dir, folder)
    return sorted([img for img in os.listdir(folder_path) if img.endswith('.png')])

# Get the current event and its images
current_event = events[st.session_state.folder_index]
images = get_images_in_event(current_event)

header_placeholder = st.empty()
# Placeholder for image
image_placeholder = st.empty()

tnames = ["Unfiltered Hits", "Hits Filtered in Time", "Hits Filtered in Space", "Hits on Segment (Green)", "Segment Fit"]

# Get current image name and path
current_image_name = images[st.session_state.image_index]
current_image_path = os.path.join(base_dir, current_event, current_image_name)

current_tname = tnames[st.session_state.image_index]

# List of button names for next image
bnames = ["Filter the Hits in Time", "Filter the Hits in Space", "Identify the Hits on Segment", "Fit the Segment", "Next Event"]
current_button_name = bnames[st.session_state.image_index]

# Button with the name of the next image
if st.button(f"{current_button_name}"):
    # Move to the next image in the current folder
    st.session_state.image_index += 1

    # If we've reached the end of the current folder's images
    if st.session_state.image_index >= len(images):
        # Move to the next event folder and reset the image index
        st.session_state.folder_index = (st.session_state.folder_index + 1) % len(events)
        st.session_state.image_index = 0

    # Force rerun to update the UI with the new image immediately
    st.rerun()

with header_placeholder:
    st.header(f"Event: {st.session_state.folder_index}. {current_tname}")
# Load and display the current image
with image_placeholder:
    image = Image.open(current_image_path)
    st.image(image)

import streamlit as st
from PIL import Image
import os
st.set_page_config(layout="wide")

st.title('ATLAS L0MDT Trigger Demo')

# Initialize session state for the folder and image counter
if 'folder_index' not in st.session_state:
    st.session_state.folder_index = 0
if 'image_index' not in st.session_state:
    st.session_state.image_index = 0

# Define the folder structure and list of folders (events)
base_dir = "images/"

# Function to get the images for the current folder
def get_events():
    folder_path = os.path.join(base_dir)
    return sorted([evt for evt in os.listdir(folder_path) if evt.startswith('event')])

events = get_events()  # This assumes the events are named event0, event1, etc.

# Get the current event and its images
current_event = events[st.session_state.folder_index]

header_placeholder = st.empty()
# Placeholder for image
image_placeholder = st.empty()

tnames = ["Unfiltered Hits", "Hits Filtered in Time", "Hits Filtered in Space", "Hits on Segment (Green)", "Segment Fit"]

# Get current image name and path
# current_image_name = images[st.session_state.image_index]
# current_image_path = os.path.join(base_dir, current_event, current_image_name)
current_event_path = os.path.join(base_dir, current_event)
current_tname = tnames[st.session_state.image_index]

# List of button names for next image
bnames = ["Filter the Hits in Time", "Filter the Hits in Space", "Identify the Hits on Segment", "Fit the Segment", "Next Event"]
current_button_name = bnames[st.session_state.image_index]

# Button with the name of the next image
if st.button(f"Next Event"):
    # Move to the next image in the current folder
    st.session_state.folder_index += 1

    # If we've reached the end of the current folder's images
    if st.session_state.folder_index >= len(events):
        # Move to the next event folder and reset the image index
        st.session_state.folder_index = 0

    # Force rerun to update the UI with the new image immediately
    st.rerun()

with header_placeholder:
    st.header(f"Event: {st.session_state.folder_index}")
# Load and display the current image
with image_placeholder:
    # image = Image.open()
    with st.container():
        columns = st.columns(3, gap="medium", vertical_alignment='top')
        for im in range(5):
            with columns[im % 3]:
                st.subheader(tnames[im])
                st.image(current_event_path + "/mdt_%d.png" % im)
        # image = Image.open(current_event_path + "/mdt_1.png")
        # st.image(current_event_path + "/mdt_1.png")
        # # image = Image.open(current_event_path + "/mdt_2.png")
        # st.image(current_event_path + "/mdt_2.png")
        # # image = Image.open(current_event_path + "/mdt_3.png")
        # st.image(current_event_path + "/mdt_3.png")
        # # image = Image.open(current_event_path + "/mdt_4.png")
        # st.image(current_event_path + "/mdt_4.png")

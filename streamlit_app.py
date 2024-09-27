import streamlit as st
import os
import time

st.set_page_config()

st.title('ATLAS L0MDT Trigger Demo')

# Initialize session state for the folder and image counter
if 'folder_index' not in st.session_state:
    st.session_state.folder_index = 0
if 'image_index' not in st.session_state:
    st.session_state.image_index = 0
if 'slideshow_active' not in st.session_state:
    st.session_state.slideshow_active = True  # To track if slideshow is running


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

# tnames = ["Step 0. Unfiltered Hits", "Step 1. Hits Filtered in Space and Time", "Step 3. Fit the Segment"]
tnames = ["1. Ungefilterte Myon-Treffer", "2. Gefilterte Myon-Treffer", "3. Rekonstruierte Myon-Spur"]




# Get current image name and path
# current_image_name = images[st.session_state.image_index]
# current_image_path = os.path.join(base_dir, current_event, current_image_name)
current_event_path = os.path.join(base_dir, current_event)
current_tname = tnames[st.session_state.image_index]

# List of button names for next image
bnames = ["Filter the Hits in Time", "Filter the Hits in Space", "Identify the Hits on Segment", "Fit the Segment", "Next Event"]
current_button_name = bnames[st.session_state.image_index]

# Button with the name of the next image
if st.button(f"Nächste Kollision"):
    # Move to the next image in the current folder
    st.session_state.folder_index += 1

    # If we've reached the end of the current folder's images
    if st.session_state.folder_index >= len(events):
        # Move to the next event folder and reset the image index
        st.session_state.folder_index = 0

    # Force rerun to update the UI with the new image immediately
    st.rerun()

# Start/Stop slideshow button
if st.button("Start/Stopp Slideshow"):
    st.session_state.slideshow_active = not st.session_state.slideshow_active


# If slideshow is active, wait for 10 seconds and then move to the next event



with header_placeholder:
    st.header(f"Kollision: {st.session_state.folder_index}")
# Load and display the current image
with image_placeholder:
    # image = Image.open()
    with st.container():
        # columns = st.columns(2, gap="medium", vertical_alignment='top')
        for im in range(3):
            # with columns[im % 2]:
            st.subheader(tnames[im])
            if im == 2:
                st.image(current_event_path + "/mdt_3.png")
            else:
                st.image(current_event_path + "/mdt_%d.png" % im)
        # image = Image.open(current_event_path + "/mdt_1.png")
        # st.image(current_event_path + "/mdt_1.png")
        # # image = Image.open(current_event_path + "/mdt_2.png")
        # st.image(current_event_path + "/mdt_2.png")
        # # image = Image.open(current_event_path + "/mdt_3.png")
        # st.image(current_event_path + "/mdt_3.png")
        # # image = Image.open(current_event_path + "/mdt_4.png")
        # st.image(current_event_path + "/mdt_4.png")
if st.session_state.slideshow_active:
    my_bar = st.progress(0, text="Moving to next event...")
    for percentage_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percentage_complete + 1, text="Moving to next event...")
    # time.sleep(10)  # Wait for 10 seconds before moving to the next image
    st.session_state.folder_index += 1
    if st.session_state.folder_index >= len(events):
        st.session_state.folder_index = 0
    st.rerun()  # Refresh the page

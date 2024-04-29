import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings
import cv2
from pyzbar.pyzbar import decode

# Initialize an empty list to store scanned data
scanned_data = []

st.title("Mobile QR Code Scanner")

webrtc_ctx = webrtc_streamer(
    key="example",
    video_transformer_factory=None,  # No need for video transformation
    client_settings=ClientSettings(
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
    ),
    mode=WebRtcMode.SENDRECV,
    async_transform=True
)

if not webrtc_ctx.video_receiver:
    st.warning("Please allow access to the camera.")
    st.stop()

video_frame = webrtc_ctx.video_receiver.get_frame()

# Use video_frame.data for QR code detection and decoding
# Here, we'll detect QR codes in each frame and add the data to the scanned_data list
if video_frame:
    frame = video_frame.to_ndarray()
    # Convert the frame to grayscale for QR code detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect QR codes in the frame
    qrcodes = decode(gray_frame)
    # Extract data from detected QR codes
    for qrcode in qrcodes:
        data = qrcode.data.decode("utf-8")
        if data not in scanned_data:
            scanned_data.append(data)

# Display the table of scanned data
st.write("Scanned Data:")
st.table(scanned_data)

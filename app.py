
import io

import cv2
import numpy as np
import qrcode
import streamlit as st
from PIL import Image
from qrcode.constants import ERROR_CORRECT_H

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="QR Studio | Generator & Scanner",
    page_icon="🔳",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b1020 0%, #111827 55%, #172554 100%);
        color: #f8fafc;
    }
    .hero {
        padding: 30px;
        border: 1px solid #334155;
        border-radius: 22px;
        background: linear-gradient(120deg, #172554, #312e81, #164e63);
        text-align: center;
        margin-bottom: 25px;
    }
    .hero h1 { color: white; font-size: 2.6rem; }
    .hero p { color: #cbd5e1; font-size: 1.1rem; }
    div[data-testid="stMetric"] {
        background: #172033;
        border: 1px solid #334155;
        padding: 15px;
        border-radius: 14px;
    }
    .section-title {
        color: #67e8f9;
        font-weight: 700;
        font-size: 1.35rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------
def generate_qr(data, fill_color, back_color, box_size, border_size):
    """Generate a QR code and return a PIL image."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=box_size,
        border=border_size,
    )
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color=fill_color,
        back_color=back_color,
    )
    return image.convert("RGB")


def scan_qr(image):
    """Decode a QR code from a PIL image."""
    rgb_image = np.array(image.convert("RGB"))
    bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)

    detector = cv2.QRCodeDetector()
    decoded_text, points, _ = detector.detectAndDecode(bgr_image)

    return decoded_text.strip() if decoded_text else ""


def image_to_bytes(image, image_format="PNG"):
    """Convert a PIL image into downloadable bytes."""
    buffer = io.BytesIO()
    image.save(buffer, format=image_format)
    return buffer.getvalue()


# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <h1>🔳 QR STUDIO</h1>
        <p>Generate. Scan. Connect. — Your all-in-one QR toolkit.</p>
        <p>✨ Built with Python, Streamlit, OpenCV and Pillow</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("⚙️ QR Studio")
st.sidebar.caption("Python QR Code Toolkit")
st.sidebar.markdown("---")
st.sidebar.info(
    "Generate stylish QR codes or scan existing QR code images. "
    "Your uploaded images are processed within this app."
)
st.sidebar.markdown("**Features**")
st.sidebar.write("🎨 Custom QR colors")
st.sidebar.write("📥 PNG downloads")
st.sidebar.write("🖼️ Image scanning")
st.sidebar.write("📷 Camera capture")

# --------------------------------------------------
# METRICS
# --------------------------------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Generator", "Ready")
with col2:
    st.metric("Scanner", "Ready")
with col3:
    st.metric("Export format", "PNG")

# --------------------------------------------------
# TABS
# --------------------------------------------------
generate_tab, scan_tab = st.tabs(
    ["🎨 Generate QR Code", "🔍 Scan QR Code"]
)

# ==================================================
# QR GENERATOR
# ==================================================
with generate_tab:
    st.markdown(
        '<p class="section-title">Create your QR code</p>',
        unsafe_allow_html=True,
    )
    st.write(
        "Enter a website URL, plain text, email address, or other information."
    )

    with st.form("qr_generator_form"):
        qr_data = st.text_area(
            "Text or URL",
            placeholder="https://example.com",
            height=100,
        )

        color_col1, color_col2 = st.columns(2)

        with color_col1:
            fill_color = st.color_picker(
                "QR foreground color", "#111827"
            )

        with color_col2:
            back_color = st.color_picker(
                "Background color", "#FFFFFF"
            )

        size_col1, size_col2 = st.columns(2)

        with size_col1:
            box_size = st.slider(
                "Pixel size per QR box",
                min_value=5,
                max_value=20,
                value=10,
            )

        with size_col2:
            border_size = st.slider(
                "Quiet-zone border",
                min_value=2,
                max_value=8,
                value=4,
            )

        submitted = st.form_submit_button(
            "✨ Generate QR Code",
            use_container_width=True,
            type="primary",
        )

    if submitted:
        if not qr_data.strip():
            st.error("Please enter some text or a URL.")
        elif fill_color.upper() == back_color.upper():
            st.error("Choose different foreground and background colors.")
        else:
            try:
                qr_image = generate_qr(
                    qr_data.strip(),
                    fill_color,
                    back_color,
                    box_size,
                    border_size,
                )

                st.session_state["generated_qr"] = qr_image
                st.session_state["generated_data"] = qr_data.strip()

            except Exception as error:
                st.error(f"Could not generate the QR code: {error}")

    if "generated_qr" in st.session_state:
        st.markdown("---")
        result_col1, result_col2 = st.columns([1, 1])

        with result_col1:
            st.subheader("🖼️ Your QR Code")
            st.image(
                st.session_state["generated_qr"],
                caption="Generated by QR Studio",
                width=320,
            )

        with result_col2:
            st.subheader("📋 QR Details")
            st.success("QR code generated successfully!")
            st.write("**Content:**")
            st.code(st.session_state["generated_data"])

            st.download_button(
                label="⬇️ Download QR Code (PNG)",
                data=image_to_bytes(
                    st.session_state["generated_qr"]
                ),
                file_name="qr_studio_code.png",
                mime="image/png",
                use_container_width=True,
            )

# ==================================================
# QR SCANNER
# ==================================================
with scan_tab:
    st.markdown(
        '<p class="section-title">Decode an existing QR code</p>',
        unsafe_allow_html=True,
    )
    st.write(
        "Upload a QR code image or capture one using your camera."
    )

    scanner_method = st.radio(
        "Choose input method",
        ["Upload image", "Use camera"],
        horizontal=True,
    )

    uploaded_image = None

    if scanner_method == "Upload image":
        uploaded_file = st.file_uploader(
            "Upload QR image",
            type=["png", "jpg", "jpeg", "bmp", "webp"],
            help="Use a clear image with the entire QR code visible.",
        )

        if uploaded_file is not None:
            try:
                uploaded_image = Image.open(uploaded_file).convert("RGB")
            except Exception:
                st.error("This image could not be opened.")

    else:
        camera_file = st.camera_input("Take a picture of a QR code")

        if camera_file is not None:
            try:
                uploaded_image = Image.open(camera_file).convert("RGB")
            except Exception:
                st.error("The camera image could not be opened.")

    if uploaded_image is not None:
        left, right = st.columns([1, 1])

        with left:
            st.subheader("📸 Input image")
            st.image(uploaded_image, use_container_width=True)

        with right:
            st.subheader("🔎 Scan result")

            with st.spinner("Reading QR code..."):
                try:
                    decoded = scan_qr(uploaded_image)

                    if decoded:
                        st.success("QR code detected!")
                        st.write("**Decoded content:**")
                        st.code(decoded, language=None)

                        st.download_button(
                            "⬇️ Download scan result",
                            data=decoded.encode("utf-8"),
                            file_name="qr_scan_result.txt",
                            mime="text/plain",
                            use_container_width=True,
                        )

                        if decoded.lower().startswith(
                            ("http://", "https://")
                        ):
                            st.warning(
                                "Safety tip: verify the website address "
                                "before opening it."
                            )
                    else:
                        st.warning(
                            "No readable QR code was found. Try a clearer "
                            "image with better lighting and less blur."
                        )

                except Exception as error:
                    st.error(f"Scanning failed: {error}")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; color:#94a3b8; padding:12px;">
        <p>🔳 QR Studio | Python Portfolio Project</p>
        <p>Built for learning, productivity and open-source exploration.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# QR_code_scanner_with_Python
# 🔳 QR Studio — QR Code Generator & Scanner

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=27&pause=1000&color=22D3EE&center=true&vCenter=true&width=750&lines=Generate+QR+Codes+Instantly+%E2%9C%A8;Scan+QR+Codes+with+Python+%F0%9F%94%8D;Built+with+Python+%7C+OpenCV+%7C+Streamlit" alt="Animated QR Studio introduction" />
</p>

<p align="center">
  <b>✨ Generate it. Scan it. Share it.</b><br>
  A modern, interactive QR code toolkit built with Python.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/OpenCV-QR%20Scanning-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
</p>

---

## 🌌 About the Project

**QR Studio** is a Python-powered web application for generating and scanning QR codes through an intuitive interface.

Create QR codes for website links, text, contact information, and other data. Upload an existing QR image or use your camera to decode its contents.

The project combines Python programming, image processing, a web interface, and downloadable results in one portfolio-ready application.

## ⚡ Features

| Feature | Description |
|---|---|
| 🎨 QR Generator | Generate QR codes from text and URLs |
| 🌈 Color Customization | Choose foreground and background colors |
| 📐 Size Controls | Adjust QR box size and border |
| 📥 PNG Export | Download generated QR codes |
| 🔍 QR Scanner | Decode QR codes from image files |
| 📷 Camera Support | Capture QR images using a supported camera |
| 📝 Text Export | Save decoded results to a TXT file |
| 🖥️ Interactive UI | Responsive Streamlit interface |
| 🛡️ Error Handling | Helpful messages for invalid input and unreadable images |

## 🧰 Technology Stack

- **Python** — application logic
- **Streamlit** — interactive web application
- **qrcode** — QR code generation
- **OpenCV** — QR code detection and decoding
- **Pillow** — image processing
- **NumPy** — image array conversion

## 🗂️ Project Structure

```text
QR-Code-Generator-Scanner/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── assets/
    └── screenshots/
```

## 🚀 Getting Started

### 1. Clone the repository

Replace `YOUR_GITHUB_USERNAME` with your GitHub username after uploading the project.

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/QR-Code-Generator-Scanner.git
```

### 2. Open the project

```bash
cd QR-Code-Generator-Scanner
```

### 3. Create a virtual environment

**Windows:**

```bash
python -m venv venv
```

Activate it in PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Or use Command Prompt:

```bat
venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Launch QR Studio

```bash
python -m streamlit run app.py
```

The app normally opens in your browser at:

`http://localhost:8501`

If it does not open automatically, copy that address into your browser.

## 🧪 How to Use

### 🎨 Generate a QR Code

1. Open the **Generate QR Code** tab.
2. Enter a URL or text.
3. Choose foreground and background colors.
4. Adjust the size and border.
5. Click **Generate QR Code**.
6. Preview your QR code and download the PNG.

### 🔍 Scan a QR Code

1. Open the **Scan QR Code** tab.
2. Choose image upload or camera capture.
3. Provide a clear QR code image or take a picture.
4. View the decoded content.
5. Download the result as a text file if needed.

> 💡 Tip: Use a sharp image with good contrast. Very small, blurry, damaged, or unusually styled QR codes may not decode successfully.

## 📦 Requirements

Install the packages listed in `requirements.txt`:

```text
streamlit
qrcode[pil]
Pillow
opencv-python-headless
numpy
```

Use a supported Python version and install dependencies in a virtual environment to avoid conflicts with other projects.

## 🧠 What I Learned

- Building interactive web applications using Streamlit
- Generating QR codes programmatically
- Processing images with Pillow and NumPy
- Detecting and decoding QR codes using OpenCV
- Handling file uploads and camera input
- Exporting generated images and decoded text
- Organizing Python projects for GitHub
- Writing installation instructions and project documentation

## 🔮 Future Enhancements

- 🏷️ Add a logo in the center of generated QR codes
- 📇 Create Wi-Fi, email, phone, and vCard QR templates
- 🎨 Add more QR styles and export formats
- 📚 Build a QR scan history
- 📊 Add usage analytics and a batch QR generator
- 🌐 Deploy the application to a cloud hosting service

## 🔐 Privacy & Security

- Uploaded images are processed by the application code.
- The project does not require a database or API key.
- QR contents may contain untrusted URLs or text. Inspect them before opening.
- Avoid scanning QR codes from unknown sources without verifying their destination.

## 🤝 Contributing

Contributions, feature suggestions, and bug reports are welcome!

1. Fork this repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## 📜 License

This project is licensed under the **MIT License**. Add a `LICENSE` file to the repository if you wish to distribute it under that license.

## 👨‍💻 Developer

**Mahesh Kolamkar**

Python Developer | Data Science | AI/ML Enthusiast

- GitHub: (https://github.com/maheshkgenaidevloper)

---

<p align="center">
  <b>⭐ If you find QR Studio useful, consider starring the repository!</b><br>
  Made with ❤️ and Python.
</p>

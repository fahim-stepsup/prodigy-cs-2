# prodigy-cs-2
# 🖼️ Simple Image Encryption Tool

A basic Python script that performs **image encryption and decryption** using **color inversion**. This technique flips the RGB values of every pixel to produce a visually encrypted image, which can be decrypted by inverting the image again.

---

## 🔐 How It Works

The encryption and decryption technique used in this tool is **color inversion**:
- For every pixel `(R, G, B)` in the image:
  - Replace it with `(255 - R, 255 - G, 255 - B)`
- Reapplying this process on the encrypted image restores the original image.

---

## 🧰 Features

- Encrypts images by inverting pixel colors
- Decrypts images using the same technique
- Supports JPG and PNG image formats
- Simple command-line interface

---

## 🛠️ Requirements

- Python 3.x
- [Pillow](https://python-pillow.org/) library (Install using `pip install pillow`)

---

## 🚀 Usage

### 🖥️ Run the Script
python image_encryptor.py
💬 User Prompts
Choose whether to (E)ncrypt or (D)ecrypt

Enter the path of the image to process

Provide the output file name (e.g., output.png)
---

### ✅ Example
Simple Image Encryption Tool
Do you want to (E)ncrypt or (D)ecrypt an image? E
Enter the path to the image file: input.jpg
Enter the output file name (with .png or .jpg extension): encrypted.png
Image encrypted and saved to encrypted.png
---

### 📂 File Structure
image_encryptor.py   # Main script
README.md            # Documentation
---

### 👨‍💻 Author
Fahim Akthar
B.Tech Cyber Security | Crescent Institute of Science and Technology

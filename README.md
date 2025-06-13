# 🔐 Image Encryption Script using Python

This project demonstrates how to perform **basic image encryption** using the `Pillow` (PIL) library in Python. The script shifts RGB pixel values by a user-defined key, effectively scrambling the image data.

> ⚠️ This is a **simple RGB-shift encryption**, intended for **educational and illustrative** purposes. It is **not secure** for real-world cryptographic use.

---

## 🖼️ How It Works

The script:
1. Loads an image using `Pillow`
2. Iterates through each pixel (R, G, B values)
3. Adds a key value to each RGB component modulo 256
4. Saves the encrypted image

This transforms the original image into an encrypted version that looks visually distorted.

---

## 🛠️ Requirements

- Python 3.6+
- Pillow (Python Imaging Library)

### Install Pillow

```bash
pip install Pillow

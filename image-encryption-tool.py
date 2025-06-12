from PIL import Image

def encrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        pixels = img.load()

        width, height = img.size
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                encrypted_r = (r + key) % 256
                encrypted_g = (g + key) % 256
                encrypted_b = (b + key) % 256
                pixels[i, j] = (encrypted_r, encrypted_g, encrypted_b)

        img.save(output_path)
        print(f"✅ Image encrypted and saved to {output_path}")
    except FileNotFoundError:
        print("❌ Input image not found.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

def main():
    input_path = "samples/mnli2.png"
    output_path = "samples/encrypted_image.png"
    key = 50
    encrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()


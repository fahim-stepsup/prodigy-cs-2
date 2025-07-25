import sys
print(sys.executable)
from PIL import Image
import os

def encrypt_image(image_path, output_path):
    image = Image.open(image_path).convert('RGB')  
    pixels = image.load()

    for i in range(image.size[0]):   
        for j in range(image.size[1]):  
            r, g, b = pixels[i, j]
            pixels[i, j] = (255 - r, 255 - g, 255 - b) 

    image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")


def decrypt_image(image_path, output_path):

    encrypt_image(image_path, output_path)

def main():
    print("Simple Image Encryption Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' for Encrypt or 'D' for Decrypt.")
        return

    image_path = input("Enter the path to the image file: ").strip()

    if not os.path.exists(image_path):
        print("Error: The specified image file does not exist.")
        return

    output_path = input("Enter the output file name (with .png or .jpg extension): ").strip()

    if choice == 'E':
        encrypt_image(image_path, output_path)
    else:
        decrypt_image(image_path, output_path)

if __name__ == "__main__":
    main()
from PIL import Image

# Load the image
image_path = '/home/brydo/Pictures/TestIMG.png'
image = Image.open(image_path)

# Example coordinates where we expect balloons
possible_coords = [
    (1080, 490),  # Top position
    (1080, 680),  # Middle position
    (1080, 870)   # Bottom position
]

# Display the image and print the color of the pixels at the target coordinates
for coord in possible_coords:
    color = image.getpixel(coord)
    print(f"Coordinate: {coord}, Color: {color}")
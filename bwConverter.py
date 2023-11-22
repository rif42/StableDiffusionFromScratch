import os
from PIL import Image

def convert_images_to_bw(input_directory, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Get a list of all image files in the input directory
    image_files = [file for file in os.listdir(input_directory) if file.endswith(('.jpg', '.jpeg', '.png'))]
    
    # Iterate over the image files
    for image_file in image_files:
        # Open the image
        image_path = os.path.join(input_directory, image_file)
        image = Image.open(image_path)
        
        # Convert the image to black and white
        bw_image = image.convert('L')
        
        # Save the converted image to the output directory
        output_path = os.path.join(output_directory, image_file)
        bw_image.save(output_path)
        
        # Close the image
        image.close()
        bw_image.close()

# Example usage
input_directory = "./dataset/Uncalm"
output_directory = "./dataset/Uncalm_BW"
convert_images_to_bw(input_directory, output_directory)
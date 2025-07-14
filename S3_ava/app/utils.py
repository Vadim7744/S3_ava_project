from PIL import Image
import os

def process_image(file):
    image = Image.open(file)
    image.load()
    image.save('temp/' + os.path.basename(file), 'JPEG', quality=85)
    width, height = image.size
    if width <= height:
        crop_size = min(height * 0.7, width)
    else:
        crop_size = min(width * 0.7, height)
        
    x = (width - crop_size) // 2
    y = (height - crop_size) // 2
    cropped_image = image.crop((x, y, crop_size, crop_size))
    
    return cropped_image

def compress_and_crop(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError('Image file not found.')
    
    try:
        with open(image_path, 'rb') as file:
            processed_image = process_image(file)
        
            temp_path = f'temp/{os.path.basename(image_path)}'
            processed_image.save(temp_path, 'JPEG')
            s3_client.upload_file(
                file=processed_image.file,
                key=os.path.basename(temp_path),
                bucket='your-bucket',
                access_key='YOUR_ACCESS_KEY',
                secret_key='YOUR_SECRET_KEY'
            )
            
            os.remove(temp_path)
            return True
    except Exception as e:
        print(f'Error processing image: {e}')
        return False
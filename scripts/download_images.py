import os
import json
import requests

def download_image(url, folder_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Extract image name from URL
            image_name = url.rsplit('/', 1)[-1]
            file_path = os.path.join(folder_path, image_name)
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded {image_name}")
        else:
            print(f"Failed to download {url}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

def main():
    input_path = '/users/jjls2000/LLaVA-Med/data/llava_med_image_urls.jsonl'
    output_path = '/users/jjls2000/LLaVA-Med/data/images'  # Updated output path

    # Ensure output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Read JSONL file and download each image
    with open(input_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            image_url = data.get('url')  # Adjust this if the key differs
            if image_url:
                download_image(image_url, output_path)

if __name__ == '__main__':
    main()

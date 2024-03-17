import requests
import argparse

def download_image(url, local_filename):
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
        print(f"Image downloaded successfully to {local_filename}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

# Example URL of an image
# image_url = 'https://example.com/image.png'
# image_url = 'https://robohash.org/?set=set4'
        
def run(name:str = 'feroce assassino', size:int = 800):
    image_url = 'https://robohash.org/set_set4/'

    # image_url += nome_gatto + '?size='+ dimensioni+ "x"+dimensioni
    image_url += f'{name}?size={size}x{size}'

    # Specify the local filename where you want to save the image
    local_filename = f'{name}.png'

    # Call the function to download the image
    download_image(image_url, local_filename)        

def init_arguments():
    global args
    parser = argparse.ArgumentParser(description='Robohash cats downloader')
    parser.add_argument('name', default=None, help='name of the cat')
    # parser.add_argument('-d', '--dir', default='.', help='Output directory')
    parser.add_argument('-s', '--size', default=800, help='Size in pixels of the downloaded picture')
    args = parser.parse_args()

if __name__ == '__main__':
    init_arguments()
    run(args.name, args.size)
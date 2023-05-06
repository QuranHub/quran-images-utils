import os
import urllib.request

# Create the subfolder if it doesn't exist.
if not os.path.exists('downloads'):
    os.makedirs('downloads')

# Replace the placeholder with a number from 001 to 604.
for i in range(1, 605):
    url = f'https://easyquran.com/wp-content/HafsPages/images/{i:03d}.jpg'  # Format the number with leading zeros.
    filename = f'{i:03d}.jpg'  # Format the number with leading zeros.
    filepath = os.path.join('downloads', filename)  # Create the full filep
    urllib.request.urlretrieve(url, filepath)  # Download the file.
    print(f'Downloaded {filename} to {filepath}')

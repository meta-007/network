import urllib.request 
import ctypes
import os


sysRoot = os.path.expanduser('~')
print(sysRoot)
imageUrl = 'https://news.northwestern.edu/assets/Stories/2023/06/wiit970__FocusFillWzEyMDAsNjMwLCJ5Iiw4N10.jpg'
# Go to specif url and download+save image using absolute path
path = f'{sysRoot}/Desktop/background.jpg'
urllib.request.urlretrieve(imageUrl, path)
SPI_SETDESKWALLPAPER = 20
# Access windows dlls for funcionality eg, changing dekstop wallpaper
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)
    





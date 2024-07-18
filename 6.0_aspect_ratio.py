"""
 * Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
"""

import math
import requests
from PIL import Image

class Challenge6:
    def aspect_ratio(self, url):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            with Image.open(response.raw) as image:
                width, height = image.size
                aspect_ratio = self.calculate_aspect_ratio(width, height)
                aspect_ratio_str = f"{aspect_ratio[0]}:{aspect_ratio[1]}"
                print(f"The aspect ratio is {aspect_ratio_str}")

        except Exception as e:
            print(f"The aspect ratio could not be calculated: {str(e)}")

    def calculate_aspect_ratio(self, width, height):
        gcd_value = math.gcd(width, height)
        return (width // gcd_value, height // gcd_value)

# Example of use
if __name__ == "__main__":
    challenge = Challenge6()
    url = "https://images.pexels.com/photos/15475225/pexels-photo-15475225/free-photo-of-paisaje-naturaleza-puesta-de-sol-campo.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    challenge.aspect_ratio(url)
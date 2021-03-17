from dataclasses import dataclass
from typing import Mapping

@dataclass
class Photo: 
    src: str
    path: str


german_1 = Photo(src="local", path="./photos/german1.jpeg")
german_2 = Photo(src="local", path="./photos/german2.png")

def translate_text(text, source, destination): 
    return "asdf"

def translate_photo_contents_into_text(photo): 
    return "text"

def retreive_photo_contents(photo: Photo): 
    return "photo contents"

def transalate(source_language, destination_language, photo): 
    photo_contents = retreive_photo_contents(photo)
    text_from_photo = translate_photo_contents_into_text(photo_contents)
    translated_text = translate_text(text_from_photo, source_language, destination_language)
    return translated_text

def test_retreive_photo_contents(): 
    from PIL import Image
    from pytesseract import image_to_string
    print(image_to_string(Image.open(german_1.path)))
    
test_retreive_photo_contents()
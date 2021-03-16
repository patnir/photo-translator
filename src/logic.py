from dataclasses import dataclass


@dataclass
class Photo: 
    src: str
    path: str


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

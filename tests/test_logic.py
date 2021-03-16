from src.logic import translate_photo_contents_into_text


def test_translate(): 
    assert translate_photo_contents_into_text("photo") == "text"
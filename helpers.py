# function classifies lang entries to be recorded/read the same way every time
def classificate_lang(lang):
    # in practise only 4 different languages could appear for this library:
    # Spanish, English, German and French
    if lang.lower() in ["spanish", "español", "esp", "castellano"]:
        return "spanish"
    elif lang.lower() in ["english", "ingles", "ing", "eng", "inglés"]:
        return "english"
    elif lang.lower() in ["german", "aleman", "alemán", "deutsch"]:
        return "german"
    elif lang.lower() in ["french", "frances", "francés", "deutsch"]:
        return "french"
    else:
        return "other"
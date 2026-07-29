import re
import spacy

nlp = spacy.load("en_core_web_sm")

EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
PHONE_REGEX = r"(\+?\d{1,3}[-.\s]?)?(\(?\d{3,5}\)?[-.\s]?)?\d{3,5}[-.\s]?\d{4}"

def extract_email(text: str):
    matches = re.findall(EMAIL_REGEX, text)
    return matches[0] if matches else None

def extract_phone(text: str):
    matches = re.findall(PHONE_REGEX, text)
    if matches:
        return "".join(matches[0]).strip()
    return None

def extract_name(text: str):
    doc = nlp(text[:1000])
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None
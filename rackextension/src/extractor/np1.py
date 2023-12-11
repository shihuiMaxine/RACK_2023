import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# List of elements to process
elements = ['getLogger', '__init__', 'new_account', '_post']

for element in elements:
    # Process the element using spaCy
    doc = nlp(element)

    # Extract part-of-speech tags
    pos_tags = [(token.text, token.pos_) for token in doc]

    # Extract named entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Print the results for each element
    print(f"Element: {element}")
    print(f"Part-of-Speech Tags: {pos_tags}")
    print(f"Named Entities: {entities}")
    print("\n")


from readfile import *
from check import validate_verse
import pandas as pd

def main():
    text = read_source()
    # argumento nuevo city
    verses = verses_by_line(text, city='Santiago')
    validated_verses = validate_verse(verses)
    export_verses(validated_verses)


if __name__ == "__main__":
    main()
from readfile import *
from check import validate_verse
import pandas as pd

def main():
    # load document
    text = read_source()
    # versos por linea
    verses = verses_by_line(text)
    # cuenta silabas
    validated_verses = validate_verse(verses)

    export_verses(validated_verses)


if __name__ == "__main__":
    main()

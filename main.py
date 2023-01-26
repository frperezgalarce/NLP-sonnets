from readfile import *
from check import validate_verse
import pandas as pd

def main(): 
    text = read_source()
    verses = verses_by_line(text, city='')
    validated_verses = validate_verse(verses)
    export_verses(validated_verses)
    
if __name__ == "__main__":
    main()
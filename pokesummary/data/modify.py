#!/usr/bin/env python3
import pandas as pd

"""
This module not used when the main program is executed
because the main program reads from modified dataset.
"""


def main():
    """
    Append the alternate form names to the names themselves in
    pokemon.csv, writing to pokemon_modified.csv

    :return: None
    """
    # Open from file
    df = pd.read_csv("pokemon.csv")
    # Format column names
    df.columns = df.columns\
        .str.replace(" ", "_", regex=False)\
        .str.replace(r"\W+", "", regex=True)\
        .str.lower()

    # Make copy of rows that have alternate forms
    alt_pokemon = df.query("`alternate_form_name` != ''")

    # Prepare regional demonyms
    regional_demonyms = [{"Alola": "Alolan"}, {"Galar": "Galarian"}]
    for dictionary in regional_demonyms:
        alt_pokemon["alternate_form_name"].replace(dictionary, inplace=True)
    # Append all form names
    alt_pokemon["pokemon_name"] = alt_pokemon["alternate_form_name"] + " " + alt_pokemon["pokemon_name"]
    # TODO: fix order of mega (e.g. Mega Charizard X, not Mega X Charizard)

    # Update original dataframe
    df.update(alt_pokemon)
    df = df.drop(["alternate_form_name"], axis=1)
    # Write to file
    df.to_csv("pokemon_modified.csv", index=False)


if __name__ == "__main__":
    main()

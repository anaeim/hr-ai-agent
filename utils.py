import pandas as pd
import json

def read_csv_file(df_path):
    """
    Read a CSV file into a pandas DataFrame.

    Parameters
    ----------
    df_path : str or pathlib.Path
        Path to the CSV file.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the data from the CSV file.
    """
    df = pd.read_csv(df_path)
    return df


def write_csv_file(df, df_path):
    """
    Write a pandas DataFrame to a CSV file.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to be written to disk.
    df_path : str or pathlib.Path
        Path where the CSV file will be saved.

    Returns
    -------
    None
    """
    df.to_csv(df_path, index=False)


def read_desired_skills(desired_skills_path):
    """
    Read a text file containing the list of desired skills.

    Parameters
    ----------
    desired_skills_path : str or pathlib.Path
        Path to the text file containing desired skills.

    Returns
    -------
    str
        The full contents of the desired skills file as a single string.
    """
    with open(desired_skills_path, 'r') as fh:
        desired_skills_list = fh.read()
    return desired_skills_list


def write_json_file(data, file_path, indent=4):
    """
    Write a Python object to a JSON file.

    Parameters
    ----------
    data : object
        The Python object to serialize (e.g., dict, list, etc.).
    file_path : str or pathlib.Path
        Path where the JSON file will be saved.
    indent : int, optional
        Number of spaces for indentation in the JSON file (default is 4).

    Returns
    -------
    None
    """
    with open(file_path, 'w') as fh:
        json.dump(data, fh, indent=indent)
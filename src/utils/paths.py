# utils/paths.py
import os

def data_path(filename):
    # Get the directory of the current file (utils.path)
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Go up one directory and then down into 'csv'
    return os.path.join(base_path, '..', '..', 'data_excel_csv', filename)

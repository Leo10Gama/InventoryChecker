import pandas as pd

def get_inventory():
    sheet_name = input("Enter filepath to spreadsheet: ").strip()
    data = pd.read_excel(sheet_name)
    if not data:
        raise Exception(f"Could not read sheet {sheet_name}. Please make sure the filepath is correct and the file is an Excel file.")


if __name__=='__main__':
    get_inventory()
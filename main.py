import pandas as pd
from menu import ColourText, print_colour

def get_inventory():
    # Get the sheet
    # sheet_name = input("Enter filepath to spreadsheet: ").strip()  # TEMP COMMENT: hard coding the test file name for now
    excel_file = "test/test_3_sheets_missing_one_corp_one_demo.xlsx"
    data = pd.read_excel(excel_file, sheet_name=None)
    if data is None:
        raise Exception(f"Could not read file {excel_file}. Please make sure the filepath is correct and the file is an Excel file.")
    sheet_names = list(data)
    
    # Parse out the serial numbers of the other inventory sheets
    # ASSUMPTION: The first two sheets are the corp and demo lists respectively
    corp_sheet = data[sheet_names[0]]
    demo_sheet = data[sheet_names[1]]
    sheet_names.remove(sheet_names[0])
    sheet_names.remove(sheet_names[0])

    inventory_serial_numbers = {}
    # ASSUMPTION: The serial numbers have no headers and are always the second column of the sheets
    for sheet_name in sheet_names:
        sheet = data[sheet_name]
        inventory_serial_numbers[sheet.columns[1]] = sheet_name  # iterrows doesn't capture first row
        for _, serial_number in sheet.iterrows():
            inventory_serial_numbers[serial_number[1]] = sheet_name

    # Iterate through corp and demo sheets and print matches and non-matches
    # ASSUMPTION: The column with the serial numbers is named exactly according to the constant below
    SERIAL_NUMBERS_COLUMN_HEADER = "Serial Numbers"

    corp_serial_numbers = []
    print_colour(ColourText.BOLD, "CORP SHEET FINDINGS:")
    for header in corp_sheet.columns:
        # Not a match, keep going
        if header != SERIAL_NUMBERS_COLUMN_HEADER:
            continue
        # This is the column with serial numbers
        for serial_number in corp_sheet[header]:
            if serial_number in inventory_serial_numbers.keys():  # Match value in inventory
                print_colour(ColourText.GREEN, f"[ MATCH ]: {serial_number} in {inventory_serial_numbers[serial_number]}")
                del inventory_serial_numbers[serial_number]
            else:                                                 # No match in inventory
                print_colour(ColourText.RED, f"[MISSING]: {serial_number}")
        break
    print()

    demo_serial_numbers = []
    print_colour(ColourText.BOLD, "DEMO SHEET FINDINGS:")
    for header in demo_sheet.columns:
        # Not a match, keep going
        if header != SERIAL_NUMBERS_COLUMN_HEADER:
            continue
        # This is the column with serial numbers
        for serial_number in demo_sheet[header]:
            if serial_number in inventory_serial_numbers.keys():  # Match value in inventory
                print_colour(ColourText.GREEN, f"[ MATCH ]: {serial_number} in {inventory_serial_numbers[serial_number]}")
                del inventory_serial_numbers[serial_number]
            else:                                                 # No match in inventory
                print_colour(ColourText.RED, f"[MISSING]: {serial_number}")
        break


if __name__=='__main__':
    get_inventory()
import pandas as pd
import os
from openpyxl import load_workbook

main_directory = "C:/Users/My_Files"

df = pd.read_excel(main_directory + "/master_file.xlsx")

splitting_data_by_column = df["company_name"].unique()


def format_company_owner(writer):
    """
    Add Excel specific formatting to the workbook
    """
    # Get the workbook and the company sheet so we can add the formatting
    f_workbook = writer.book
    worksheet = writer.sheets[value]


for value in splitting_data_by_column:
    df1 = df[df['company_name'] == value]
    output_file_name = main_directory + "/" +  str(value) + ".xlsx"
    
    # Drop "company_names" column
    to_drop1 = ["company_name"]
    df1.drop(to_drop1,inplace=True,axis=1)
    
    # Run the format_excel function to format the excel file
    writer = pd.ExcelWriter(output_file_name,engine="xlsxwriter")
    df1.to_excel(writer,value,index=False)
    df_row = df1.shape[0]
    
    # If formatting cuts off the last rows data you can add 1 to prevent this from happening
    df_row = df_row + 1
    df_col = df1.shape[1]
    format_company_owne(writer)
    writer.save()
    
    # Change zoom settings to 80%. My preference usually :)
    workbook = load_workbook(output_file_name)
    sheet = workbook.active
    sheet.sheet_view.zoomScale = 80
    workbook.save(output_file_name)



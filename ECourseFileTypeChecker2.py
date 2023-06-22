import tkinter as tk
from tkinter import filedialog
import zipfile
import xml.etree.ElementTree as ET

def open_zip_file():
    # Open a dialog to select a ZIP file
    zip_filepath = filedialog.askopenfilename(filetypes=[("ZIP Files", "*.zip")])
    
    # Check if a file was selected
    if zip_filepath:
        try:
            # Open the ZIP file
            with zipfile.ZipFile(zip_filepath, 'r') as zip_file:
                # Check if 'imsmanifest.xml' file exists in the ZIP file
                if 'imsmanifest.xml' in zip_file.namelist():
                    # Open 'imsmanifest.xml' file from the ZIP file
                    with zip_file.open('imsmanifest.xml') as manifest_file:
                        # Read the content of 'imsmanifest.xml' file
                        content = manifest_file.read()
                        
                        # Search for "<schemaversion>1.2</schemaversion>" string within the XML content
                        if b"<schemaversion>1.2</schemaversion>" in content:
                            result_label.config(text="This is a SCORM 1.2 Course.")
                        elif b"<schemaversion>2004 4th Edition</schemaversion>" in content:
                            result_label.config(text="This is a SCORM 2004 Course.")
                        else:
                            result_label.config(text="String not found!")
                elif 'tincan.xml' in zip_file.namelist():
                    result_label.config(text="This is a xAPI course.")
                elif 'datatypes.dtd' in zip_file.namelist():
                    result_label.config(text="This is a SCORM 2004 course.")
                elif 'cmi5.xml' in zip_file.namelist():
                    result_label.config(text="This is a cmi5 course.")
                elif 'course.cst' in zip_file.namelist():
                        result_label.config(text="This is an AICC course.")
                else:
                    result_label.config(text="'imsmanifest.xml' file not found in the ZIP.")
        except zipfile.BadZipFile:
            result_label.config(text="Invalid ZIP file.")
    else:
        result_label.config(text="No file selected.")

# Create the main window
window = tk.Tk()
window.title("ECourse File Type Checker")
window.geometry("380x230")
window.configure(background="#35ac46")

# Create a button to open a ZIP file
open_button = tk.Button(window, text="Open ZIP File", command=open_zip_file)
open_button.pack(pady=20)
open_button["width"]="20"
open_button["height"]="1"
open_button["font"]="Helvetica" 
open_button.configure(background="#01426A")
open_button["fg"]="#ffffff"

# Create a label to display the search result
result_label = tk.Label(window, text="",font= ('Helvetica 18'), fg='#ffffff',bg= '#35ac46')
result_label.pack(ipadx= 50, ipady=50, padx= 20)

# Create a lable for attribution
att_label = tk.Label(window, text="Author: Leonard Reeves for City of Raleigh", font=('Helvetica 8'), fg='#ffffff',bg='#35ac46')
att_label.pack(ipadx= 10, ipady=10, padx= 10)
# Start the main GUI loop
window.mainloop()
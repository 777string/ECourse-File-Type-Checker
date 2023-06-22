#   ECourse File Type Checker
#   Author: Leonard Reeves
#   Date: 06/22/2023
#   Description:  
#   This program is used to check what type of course is being submitted. 
#   When an e-course is submitted, the file is in .zip format. An administrator can't tell by looking in what schema the ecourse was exported.
#   The Open ZIP File button displays the file select dialog. The ZIP file is then opened and checked for various markers to know the schema.
#   The schema type is displayed in a label to the end user.
 
import tkinter as tk                #tkinter used for GUI
from tkinter import filedialog      #filedialog needed to select zip file from user's computer
import zipfile                      #zipfile needed to open zip from user's computer
import xml.etree.ElementTree as ET  #ET used to navigate zip file for specific files

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
                            #Displays SCORM 1.2 in label for end user
                            result_label.config(text="This is a SCORM 1.2 Course.")
                        elif b"<schemaversion>2004 4th Edition</schemaversion>" in content:
                            #Displays SCORM 2004 in label for end user
                            result_label.config(text="This is a SCORM 2004 Course.")
                        else:
                            result_label.config(text="String not found!")
                
                #Displays SCORM 1.2 in label for end user
                elif 'tincan.xml' in zip_file.namelist():
                    result_label.config(text="This is a xAPI course.")
                
                #Displays SCORM 1.2 in label for end user if cmi5.xml file found
                elif 'cmi5.xml' in zip_file.namelist():
                    result_label.config(text="This is a cmi5 course.")
                
                #Displays AICC in label for end user if .cst file found
                elif 'course.cst' in zip_file.namelist():
                        result_label.config(text="This is an AICC course.")
                #Displays No known file types found in label for end user
                else:
                    result_label.config(text="No e-course files not found in the ZIP. \n This may not be an e-course ZIP.")
        
        #Displays invalid zip file in label for end user if zip is malformed or corrcupted
        except zipfile.BadZipFile:
            result_label.config(text="Invalid ZIP file.")
    
    #Displays No File Selected in label for end user when nothing has been selected in file dialog
    else:
        result_label.config(text="No file selected.")

# Create the main window, set name, set size, and set background color to CoR brand green
window = tk.Tk()
window.title("ECourse File Type Checker")
window.geometry("410x240")
window.configure(background="#35ac46")

# Create a button to open a ZIP file, set padding, height, width, font, font color, and background color
open_button = tk.Button(window, text="Open ZIP File", command=open_zip_file)
open_button.pack(pady=20)
open_button["width"]="20"
open_button["height"]="1"
open_button["font"]="Helvetica" 
open_button.configure(background="#01426A")
open_button["fg"]="#ffffff"

# Create a label to display the search result
result_label = tk.Label(window, text="",font= ('Helvetica 16'), fg='#ffffff',bg= '#35ac46')
result_label.pack(ipadx= 50, ipady=50, padx= 20)

# Create a lable for attribution
att_label = tk.Label(window, text="Author: Leonard Reeves for City of Raleigh", font=('Helvetica 8'), fg='#ffffff',bg='#35ac46')
att_label.pack(ipadx= 10, ipady=10, padx= 10)

# Start the main GUI loop
window.mainloop()

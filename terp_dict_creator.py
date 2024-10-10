import re
from models import Ms, db, app
import requests

# Default Dictionary
index = -1
databaseColumns = ["RT1-A", "RT2-A", "Name", "Suspected_matches", "Formula", "MW", "ExactMass", "CAS#", "Derivatization_Agent", "Retention_index", "Num Peaks", "X-Values", "Y-Values", "Description", "DB#", "Synon", "d_alkane_RTI", "n_alkane_RTI", "Instrument", "Ionization", "Injection_method", "GC_column", "Oven_temp", "Campaign/Experimental_Source", "Experimental_Conditions", "Publications", "Contributor", "Date_of_Entry"]
databaseDictionary = {key: [] for key in databaseColumns}

with app.app_context():
    db.drop_all()  
    db.create_all()

# Adds Values for X-Column and Y-Column
def coordinatesfunction(coordinates):
    xcoords = ""
    ycoords = ""
    for i in coordinates:
        coordTuple = i.split()
        if len(coordTuple) == 2:
            xcoords += (coordTuple[0] + "," )
            ycoords += (coordTuple[1] + ",")
    databaseDictionary["X-Values"].append(xcoords)
    databaseDictionary["Y-Values"].append(ycoords)

# Add in missing values 
def addNAValues(dic):
    lenValues = len(dic["Name"])
    for keys in dic:
        if len(dic[keys]) != lenValues:
            dic[keys].append("N/A")

# Add comments 
def addComments(lst):
    for i in lst:
        if (i[0] in databaseColumns or i[0] == "Experimental_Source") and len(i)==2:
            if i[0] == "Experimental_Source":
                databaseDictionary["Campaign/Experimental_Source"].append(i[1].strip("'"))
                continue
            databaseDictionary[i[0]].append(i[1].strip('"'))
    return

# Converts TextFile into dictionary 
def textdictionary(textfile_content):
    id = 0
    content_lines = textfile_content.splitlines()  # Split the string into lines
    for contentLine in content_lines:
        if not contentLine.strip():
            addNAValues(databaseDictionary)
            continue
        contentList = contentLine.split(":")
        columnnames = contentList[0]
        if columnnames[0].isdigit():
            coordinatesfunction(columnnames.split(";"))
            continue
        columnvalue = contentList[1].strip() if len(contentList) > 1 else ""
        if columnnames == "Comments":
            pattern = r'(\w+)="([^"]*)"'
            matches = re.findall(pattern, contentLine)
            addComments(matches)
            continue
        if columnvalue == '':
            databaseDictionary[columnnames].append("N/A")
        else:
            databaseDictionary[columnnames].append(columnvalue)
    return databaseDictionary

def ms_creator(name, retention_index, num_peaks, d_alkane_RTI, n_alkane_RTI, Instrument, Ionization, Injection_method, GC_column, Oven_temp, Experimental_Source, Experimental_Conditions, Contributor, Date_of_Entry, Publications, x_coordinates, y_coordinates):
    ms_obj = Ms(name=name, retention_index=retention_index, num_peaks=num_peaks, d_alkane_rt1=d_alkane_RTI, n_alkane_rt1=n_alkane_RTI, instrument=Instrument, ionization=Ionization, injection_method=Injection_method, gc_column=GC_column, oven_temp=Oven_temp, campaign_experimental_source=Experimental_Source, experimental_condition=Experimental_Conditions, contributor=Contributor, date_of_entry=Date_of_Entry, publications=Publications, x_coordinates=x_coordinates, y_coordinates=y_coordinates)
    db.session.add(ms_obj)
    db.session.commit()
    return

# Fetch the data from Google Drive
file_id = '1Sn9GrMHLm0iIJ_GXYdJywdFUK1b5fHNM'
download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
response = requests.get(download_url)
content = response.text
terp_dict = textdictionary(content)

# Ensure you're running inside app context
with app.app_context():
    terp_dict_length = len(terp_dict["Name"])
    for i in range(terp_dict_length):
        ms_creator(
            terp_dict["Name"][i], 
            terp_dict["Retention_index"][i], 
            terp_dict["Num Peaks"][i], 
            terp_dict["d_alkane_RTI"][i], 
            terp_dict["n_alkane_RTI"][i], 
            terp_dict["Instrument"][i], 
            terp_dict["Ionization"][i], 
            terp_dict["Injection_method"][i], 
            terp_dict["GC_column"][i], 
            terp_dict["Oven_temp"][i], 
            terp_dict["Campaign/Experimental_Source"][i], 
            terp_dict["Experimental_Conditions"][i], 
            terp_dict["Contributor"][i], 
            terp_dict["Date_of_Entry"][i], 
            terp_dict["Publications"][i], 
            terp_dict["X-Values"][i], 
            terp_dict["Y-Values"][i]
        )
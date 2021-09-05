"""
HOSPITAL MANAGEMENT SYSTEM
Module name: main
Fields: - ['Patient_Id', 'Patient_Name', 'Room_No', 'Age', 'Phone']
1. Add New Patient Details
2. View Patients
3. Search Patients
4. Update Patients
5. Delete Patient
6. Billing
7. Quit
"""

'''
Create global variables
1) Create fields to get input 
2) Create database as patient.csv
'''
import csv

# Define global variables
patient_fields = ['Patient_ID', 'Patient_Name', 'Room_No', 'Age', 'Phone']
patient_database = 'patient.csv'

'''
Function name: display_menu
Overview of this function:
1) Welcome the user in terminal
2) Ask for their desire choice
'''

def display_menu():   # Represents the main area or dashboard for hospital
    print("-------------------------------------")
    print(" Welcome to Hospital Management System")
    print("-------------------------------------")
    print("1. Add New Patient")
    print("2. View Patients")
    print("3. Search Patients")
    print("4. Update Patients")
    print("5. Delete Patient")
    print("6. Billing")
    print("7. Quit")

'''
Function name: add_patient
Overview of this function:
1) Use global variables to take patient information
2) Write newly added patient information into database 
'''

def add_patient():  # Represents adding a patient tab
    print("-------------------------")
    print("Add Patient Information")
    print("-------------------------")
    global patient_fields
    global patient_database

    patient_data = []
    for field in patient_fields:
        value = input("Enter " + field + ": ")
        patient_data.append(value)
        with open(patient_database, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(patient_fields)
            writer.writerows([patient_data])

    print("Data saved successfully")
    input("Press enter to return the dashboard")
    return

'''
Function name: view_patients
Overview of this function:
1) Use global variables as column name
2) Show existing patients information stored in database
'''

def view_patients():   # Represents the existing patients in the database
    global patient_fields
    global patient_database

    print("--- Patient Records ---")

    with open(patient_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in patient_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press enter to return the dashboard")

'''
Function name: search_patients
Overview of this function:
1) Use global variables to show patient information
2) Search patient information using Patient ID 
3) Read the database for the matching Patient ID 
4) Display Patient Information
'''

def search_patients():    # Represents the search area where the user can search patient data with Patient ID
    global patient_fields
    global patient_database

    print("--- Search Patients ---")
    Patient_ID = input("Enter Patient ID. to search: ")
    with open(patient_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if Patient_ID == row[0]:
                    print("----- Patient Found -----")
                    print("Patient ID : ", row[0])
                    print("Patient Name: ", row[1])
                    print("Room No: ", row[2])
                    print("Age: ", row[3])
                    print("Phone: ", row[4])
                    break
        else:
            print("Patient ID. not found in our database")
    input("Press enter to return the dashboard")

'''
Function name: update_patients
Overview of this function:
1) Use global variables to show patient information
2) Search patient information using Patient ID 
3) Read the database for the matching Patient ID 
4) Use global variables to ask for information to be updated
5) If not found shows an error
'''

def update_patients():
    global patient_fields
    global patient_database

    print("--- Update Patients ---")
    Patient_ID = input("Enter Patient ID. to update: ")
    index_patient = None
    updated_data = []
    with open(patient_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if Patient_ID == row[0]:
                    index_patient = counter
                    print("Patient Found in database: ", index_patient)
                    patient_data = []
                    for field in patient_fields:
                        value = input("Enter " + field + ": ")
                        patient_data.append(value)
                    updated_data.append(patient_data)
                else:
                    updated_data.append(row)
                counter += 1

    # Check if the record is found or not
    if index_patient is not None:
        with open(patient_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Patient ID not found in our database")

    input("Press enter to return the dashboard")

'''
Function name: delete_patients
Overview of this function:
1) Use global variables to show patient information
2) Search patient information using Patient ID 
3) Read the database for the matching Patient ID 
4) Display Patient Information
5) Delete the patient information
'''

def delete_patients():   # Represents the area where user can delete the existing patients data
    global patient_fields
    global patient_database

    print("--- Delete Patients ---")
    Patient_ID = input("Enter Patient ID. to delete: ")
    patient_found = False
    updated_data = []
    with open(patient_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if Patient_ID != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    patient_found = True

    if patient_found is True:
        with open(patient_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Patient ID. ", Patient_ID, "deleted successfully")
    else:
        print("Patient ID. not found in our database")

    input("Press enter to return the dashboard")

'''
Function name: Billing
Overview of this function:
1) Import read, purchase and write modules
2) Performs as main module for billing
3) Performs looping to display, read and write products
'''

def Billing():
    import read
    import purchase
    import write


    print("-------------------------------")
    print(" Thank you for using our system")
    print("-------------------------------")

    again="Y"
    while again.upper()=="Y":
        a=read.medicine()
        b=purchase.purchase(a)
        write.over_write(a,b)
        again=input("\nDoes the any new customer waiting to buy product? ")
        print("\nThank you for shopping from our store!!")
        print("Please check your invoice for your shopping details, \nWhich we created txt file format for you.")

'''
Overview of this function:
1) Displays the display_menu function
2) Ask for the choice 
3) Perform condition loop 
4) Display choosen function
'''

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_patient()
    elif choice == '2':
        view_patients()
    elif choice == '3':
        search_patients()
    elif choice == '4':
        update_patients()
    elif choice == '5':
        delete_patients()
    elif choice == '6':
        Billing()
    else:
        break
print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")

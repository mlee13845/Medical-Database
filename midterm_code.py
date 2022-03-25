import pandas as pd
user_selection = ''

name = []
age = []
illness = []
medication = []
patient_data = {"Name" : name, "Age": age, "Condition": illness, "Medication:" : medication}

while(user_selection != 'q'):

    print("1. Input patient")
    print("2. Remove patient")
    print("3. Find patient")
    print("4. View file database")
    print("q. Exit")
    user_selection = input("Enter a number: ")

    if user_selection == '1':
        print("1. Input patient manually")
        print("2. Input file of patients")

        user_selection = input("Enter a number: ")

        #user inputs directly the patient
        if user_selection == '1':

            patient_name = input("Name: ")
            patient_age = input("Age: ")
            patient_illness = input("Condition: ")
            patient_medication = input("Treatment: ")

            name.append(patient_name)
            age.append(patient_age)
            illness.append(patient_illness)
            medication.append(patient_medication)

            patient_data = {"Name  " : name, "Age  ": age, "Condition  ": illness, "Treatment  " : medication}
            data = pd.DataFrame(patient_data)
            print(data)
        elif user_selection == '2':
            
            text_file_name = input("Enter name of file with extension: ")
            data = pd.read_csv(text_file_name, sep= "\t")
            
            name_col = data["Name"]
            age_col = data["Age"]
            illness_col = data["Condition"]
            treatment_col = data["Treatment"]

            for i in range(len(name_col)):
                name.append(name_col[i])
            
            for i in range(len(age_col)):
                age.append(age_col[i])

            for i in range(len(illness_col)):
                illness.append(illness_col[i])
            
            for i in range(len(treatment_col)):
                medication.append(treatment_col[i])

            patient_data = {"Name  " : name, "Age  ": age, "Condition  ": illness, "Treatment  " : medication}
            data = pd.DataFrame(patient_data)
            print(data)

        else:
            print("Not an input try again.")


    elif user_selection == '2':

        remove_name = input("Enter name of patient: ")
        find_name = False

       
        for i in  range(len(name)):
            
            if name[i] == remove_name:
                print(name[i] + remove_name)
                find_name = True
                name.pop(i)
                age.pop(i)
                illness.pop(i)  
                medication.pop(i)
                break
                
                    

        if find_name == False:
            print("This patient could not be found in the database")

        else:
            patient_data = {"Name  " : name, "Age  ": age, "Condition  ": illness, "Treatment  " : medication}
            data = pd.DataFrame(patient_data)
            print(data)

    elif user_selection == '3':
        find_patient = input("Name: ")
        find_name = False
        
        needed_name =[]
        needed_age = []
        needed_illness =[]
        needed_medication = []
        for i in  range(len(name)):
            
            if name[i] == find_patient:
               # print(name[i] + find_patient)
                find_name = True

                needed_name.append(name[i])
                needed_age.append(age[i])
                needed_illness.append(illness[i])
                needed_medication.append(medication[i])

                select_patient = {"Name  " : needed_name, "Age  " : needed_age, "Condition  ": needed_illness, "Treatment  " : needed_medication}
                data = pd.DataFrame(select_patient)
                print(data)

                needed_name.remove(name[i])
                needed_age.remove(age[i])
                needed_illness.remove(illness[i])
                needed_medication.remove(medication[i])
                break
                
                    

        if find_name == False:
            print("This patient could not be found in the database")
            
    elif user_selection == '4':

        text_file_name = input("Enter name of file with extension: ")
        data = pd.read_csv(text_file_name, sep= "\t")
        print(data)
        
    elif user_selection == 'q':
        break
    else:
        print("Invalid input! Pls try again.")
    print("\n")
    user_selection = input("Do you want to save your changes Y/N? ")
    if user_selection == 'Y':
        user_selection = input(" Input new or old file name including extension(old file name will overwrite previous data): ")

        patient_data = {"Name  " : name, "Age  ": age, "Condition  ": illness, "Treatment  " : medication}
        data = pd.DataFrame(patient_data)
        data.to_csv(user_selection,index =False,sep="\t")
    user_selection = input("press q to exit or c to continue.")

    print("\n")
    print("\n")

import pandas as pd
Contacts = pd.read_csv("Contacts.csv")
Num_Items = len(Contacts)
for i in range(Num_Items):
    First_Name = Contacts.at[i, "First Name"]
    Last_Name = Contacts.at[i, "Last Name"]
    Mobile = Contacts.at[i, "Mobile"]
    Email = Contacts.at[i, "Email"]
    Street = Contacts.at[i, "Street"]
    City = Contacts.at[i, "City"]
    State = Contacts.at[i, "State"]
    Postcode = Contacts.at[i, "Postcode"]
    Country = Contacts.at[i, "Country"]
    Company = Contacts.at[i, "Company"]
    Department = Contacts.at[i, "Department"]
    Job_Title = Contacts.at[i, "Job Title"]
    Website = Contacts.at[i, "Website"]
    Notes = Contacts.at[i, "Notes"]
    allvcf = open(str(First_Name)+'.vcf', 'w')
    allvcf.write( 'BEGIN:VCARD' + "\n")
    allvcf.write( 'VERSION:2.1' + "\n")
    allvcf.write( 'N:' + Last_Name + ';' + First_Name + ";;;\n")
    allvcf.write( 'FN:' + First_Name + " " + Last_Name + "\n")
    allvcf.write( 'TEL;CELL:' + Mobile + "\n")
    allvcf.write( 'EMAIL;WORK:' + Email + "\n")
    allvcf.write( 'ADR;HOME:;;' + Street + ";" + City + ";" + State + ";" + str(Postcode) + ";" + Country + "\n")
    allvcf.write( 'ORG:' + Company + ";" + Department + "\n")
    allvcf.write( 'TITLE:' + Job_Title + "\n")
    allvcf.write( 'URL:' + Website + "\n")
    allvcf.write( 'Notes:' + Notes + "\n")
    allvcf.write( 'END:VCARD')    
    allvcf.close()
    

# =======================================================================================================
""" Returns the Matching Account Numbers corresponding to the Phone Number from the DataBase  """
# =======================================================================================================

import pandas as pd

def accphmatch(num):
    #We use a self created .csv file in Local Storage to replace the Database and show the functionality
    #In case of original Database we need to use SQL
    filepath = './Database/Accno_Phno_db.csv'
    df = pd.read_csv(filepath)
    length = df.shape[0]
    count = 0
    output_str = "Matching Account No(s) : "
    for i in range(0,length):
        if str(df.iloc[i]['Phone_number']) == num:
            if(count > 0) :
                output_str += ', '
            count += 1
            output_str += str(df.iloc[i]['Account_number'])
    if count == 0:
        return('No matching Account Number!!')
    else:
        return output_str

# =======================================================================================================
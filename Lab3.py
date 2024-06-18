import pandas as pd
import sys
import os
import datetime

def Total_price(df):
     
      val1= df["ITEM QUANTITY"]
      val2= df["ITEM PRICE"]
      return(val1*val2)

def Make_directory(df):
    
    nva_fecha=str(df["ORDER DATE"])
   
    name_dir=nva_fecha.strftime("%Y-%m-%d")
    ruta='./'+name_dir
    if not os.path.exists(ruta):
         os.mkdir(ruta)
  

def main():
    if (len(sys.argv)-1)==0:
         print("Path of the sales data CSV file is missing\n")
         exit
    elif (len(sys.argv)-1)==1:
       
       if ((sys.orig_argv[1])==0):
           print("The file or path no existing\n")
           exit
       if ((sys.orig_argv[1])==1):
          
          files_C = pd.read_csv('sales_data_a1.csv',sep=',', usecols=['ORDER ID', 'ORDER DATE', 'ITEM NUMBER', 'PRODUCT LINE', 'PRODUCT CODE', 'ITEM QUANTITY', 'ITEM PRICE', 'STATUS', 'CUSTOMER NAME'])
          
          df=pd.DataFrame(files_C) 
          print("The DataFrame:\n")
          print(df)
          df["ITEM QUANTITY"]=df["ITEM QUANTITY"].astype(int) 
          df["ITEM PRICE"] = df["ITEM PRICE"].astype(float) 
          df["TOTAL PRICE"] = df.apply(Total_price, axis=1) 
          
          df["ITEM PRICE"] = df["ITEM PRICE"].astype(str) 
          df['ITEM PRICE'] = '$ '+ df['ITEM PRICE'] 
          
          df.sort_values(by='ORDER ID', inplace=True)
          df_group_grantot =df.groupby("ORDER ID")
          df_grantotal=df_group_grantot["TOTAL PRICE"].sum()
          print(df)
          print("\n The sum of TOTAL PRICE by ORDER DATE\n")
          print(df_grantotal)
          
          df["TOTAL PRICE"] = df["TOTAL PRICE"].astype(str)
          df['TOTAL PRICE'] = '$ '+ df['TOTAL PRICE'] 
          
          print(df)
          
          df.to_csv('Order_sales_data_2r.csv', index=False) 
                   
          Make_directory(df)
                  
               
if __name__ == '__main__':
     main()
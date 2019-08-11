# Home Work 03 Part A by Rashid Khokhar
import os
import csv

moncount=0
plsum=0
chngsum=0
prevpl=0
maxchng=-999999
minchng=999999
maxchngmon=""
minchngmon=""

csvpath=os.path.join(".","Resources","budget_data.csv")
with open(csvpath, newline='') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',')
      print(csvreader)
      csv_header=next(csvreader)
      print(f"CSV Header: {csv_header}")
      
      for row in csvreader:
        #print(row[0], 
        #print(row)
        moncount=moncount+1
        thispl=int(row[1])
        plsum=plsum+thispl
        if moncount > 1:
            thischng=thispl-prevpl
            chngsum=chngsum+thischng
            if thischng > maxchng:
              maxchng=thischng
              maxchngmon=row[0]
            else:
              if thischng < minchng:
                minchng=thischng
                minchngmon=row[0]


        prevpl=thispl

avgchng=round(chngsum/(moncount-1), 2)   
ln1="Total Months: " +str(moncount)
ln2="Total       : " + "$ "+str(plsum)
ln3="Average  Change: " + "$ "+str(avgchng)
ln4="Greatest Increase in Profits: " + maxchngmon +"  ($ "+str(maxchng)+")"
ln5="Greatest Decrease in Profits: " + minchngmon +"  ($ "+str(minchng)+")"

print("\n")
print("Analysis of Bank Budget Data:"+"\n")
print(" "+ln1,"\n",ln2,"\n",ln3,"\n",ln4,"\n",ln5,"\n\n")

output_file = os.path.join("Bank_Budget_Output.txt")
txtfile=open(output_file, 'w', newline='\n') 
txtfile.write("\n Analysis of Bank Budget Data by RWK:\n\n")
txtfile.write(ln1+"\n")
txtfile.write(ln2+"\n")
txtfile.write(ln3+"\n")
txtfile.write(ln4+"\n")
txtfile.write(ln5+"\n")
txtfile.close()

print("\n\n File "+output_file+" has been prepared\n\n\n")
# End of Code
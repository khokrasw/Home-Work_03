# Home Work 03 Part B by Rashid Khokhar
import os
import csv

voters=0
candidates=[]
votecount=[]
csvpath=os.path.join(".","Resources","election_data.csv")
with open(csvpath, newline='') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',')
      print(csvreader)
      csv_header=next(csvreader)
      print(f"CSV Header: {csv_header}")
      
      for row in csvreader:
        #print(row)
        thiscandidate=row[2]
        if not thiscandidate in candidates:
          candidates.append(thiscandidate)
          votecount.append(1)
        else:
          thisindex=candidates.index(thiscandidate)
          votecount[thisindex]=votecount[thisindex]+1
      
        voters=voters+1

maxvotes=max(votecount)
namelen=len(candidates[0])
for xn in range(1, len(candidates)):
  thislen=len(candidates[xn])
  if thislen > namelen:
    namelen=thislen

ln=[]
ln.append("Election Results")
ln.append("-------------------------")
ln.append("Total Votes: \t" +str(voters))
ln.append(ln[1])
for xn in range(len(candidates)):
  thisvote=votecount[xn]
  votepct=100*(thisvote/voters)
  thiscandidate=candidates[xn].ljust(namelen+1," ")
  thispct=(str(round(votepct,3))+"%").rjust(6," ")
  ln.append(thiscandidate+": "+thispct+"\t("+str(thisvote)+")")

ln.append(ln[1])
ln.append("Winner Is: "+candidates[votecount.index(maxvotes)])
ln.append(ln[1])

print("\n\n")
for xn in range(len(ln)):
  print(ln[xn])
print("\n\n")

output_file = os.path.join("Election_Results_Output.txt")
txtfile=open(output_file, 'w', newline='\n') 
txtfile.write("\n Election Results Compilation by RWK:\n\n")
for xn in range(len(ln)):
  txtfile.write(ln[xn]+"\n")
txtfile.close()

print("\n\n File "+output_file+" has been prepared\n\n\n")
# End of Code

        
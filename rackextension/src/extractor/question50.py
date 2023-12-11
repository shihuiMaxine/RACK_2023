import re
import csv
#?
file = open("api_mapping-q.csv")
f = open("rankedAPI_50.txt", "r")

# print(f.read())
listqu=[]
for i in f:
    # print(i)
    listqu.append(i)
listtotal=[]
for i in range (0, len(listqu)):
    if i % 3 == 2:
        # print(listqu[i])
        listquestions=(listqu[i][14:len(listqu[i])-2]).replace("'", "").split(",")
        listtotal.append(listquestions)
        # print((listqu[i][14:len(listqu[i])-2]).replace("'", "").split(","))
# print(len(listtotal))
# print((listqu[2][14:len(listqu[2])-2]).split(","))

print(type(file))
csvreader = csv.reader(file)
list1=[]
count1=0
cont=""
# print(csvreader.split("{"))
header = ['question',"P percents","R percents","f1 percents"]

id=0
# Open the CSV file and read its contents
with open("api_mapping-q.csv", 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    n=0

    # Iterate over rows in the CSV file
    for row in csv_reader:
        
        listq=[]
        # Each row is a list representing the columns in that row
        # print(row[4][1:len(row[4])-1].split(","))
         

        listapi=[]
        # if n >1 :
        #     for i in row[4] :
        #         type(i)
        #         listapi.append(row[4][2:len(row[4])-1].split(","))

        #     for j in (row[3][2:len(row[4])-1].split(",")):
        #         if j not in listapi:
        #             listapi.append(j)
        # print(listapi)
        
        strquestion=""
        listapit=[]
        if n >1:
            list3= row[3][1:len(row[3])-1].split(",")
            for a in list3:
                a3=a.replace("'", "")
                if a3 != "":
                    listapit.append(a3)
            list4= row[4][1:len(row[4])-1].split(",")
            # print(list4)
            for b in list4:
                b4=b.replace("'", "")
                if b4 not in listapit:
                    if b4 !="":
                        listapit.append(b4)
            # print(row[3][1:len(row[3])-1].split(","))
            for o in row[1]:
                strquestion+=o
            # print(strquestion)
            # print(listapit)
        n += 1

lists=[]
listd=[]

with open('question_50_3.csv', 'w', encoding='UTF8') as f:

    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    
    listapi=[]
    n =0
    for row in csvreader:
        listq=[]
        strquestion=""
        listapit=[]
        if n > 0:
            list3= row[3][1:len(row[3])-1].split(",")
            for a in list3:
                a3=a.replace("'", "")
                if a3 != "":
                    listapit.append(a3)
            list4= row[4][1:len(row[4])-1].split(",")
            # print(list4)
            for b in list4:
                b4=b.replace("'", "")
                if b4 not in listapit:
                    if b4 !="":
                        listapit.append(b4)
            # print(row[3][1:len(row[3])-1].split(","))
            for o in row[1]:
                strquestion+=o
            listq.append(strquestion.replace("\n", ""))
            # print(strquestion)
            # print(listapit)
            if n >=1:
                recapi=[]
                print("listtotal[n-1]")
                gtapi=listtotal[n-1]
                print(len(gtapi))
                for h in range (0, len(gtapi)-1):
                    if h < 3:
                        recapi.append(gtapi[h])
                print(gtapi)
                print(recapi)
                print(len(recapi))
                # recapi = listtotal[n-1]


                print(listtotal[n-1])
                print("listapit")
                print(listapit)
                print(len(listapit))
                # listd=recapi
                for i in range (0, len(recapi)-1):
                    listd.append(recapi[i])
                lists=[]
                for x in range(0, len(listapit)):
                    # print(recapi)
                    
                    # print(listtotal[n-2])
                    


                    if listapit[x] not in recapi:
                        listd.append(listapit[x])
                    else:
                        print(listapit[x])
                        # listd.remove(listapit[x])
                        lists.append(listapit[x])
                        # print(lists)
                    # print(len(listtotal[n-1]))
                print(listd)
                print(lists)
                # if len(listd)!=0:
                #     perc=len(lists)/len(listd)
                #     pperc=len(lists)/len(listapit)
                #     rperc=len(lists)/gtapi
                # else:
                    # perc=0

                if len(recapi)!=0:
                    
                    pperc=len(lists)/len(recapi)
                    print(len(lists))
                    print(len(recapi))
                    print(listd)
                    print(pperc)
                else:
                    pperc=0
                if len(listapit)!=0:
                    rperc=len(lists)/len(listapit)
                    print(len(listapit))

                else:
                    rperc=0
                

                # print(perc)
                listq.append(pperc)
                listq.append(rperc)
                totalp= pperc+rperc
                prtotal = len(recapi)+len(listapit)
                if prtotal!= 0:

                    f1perc = (2*len(listapit)*len(recapi))/prtotal
                else:
                    f1perc = 0

                if totalp!= 0:

                    f1p = (2*pperc*rperc)/totalp
                else:
                    f1p = 0

                listq.append(f1p)



                # listq.append(perc)
                print(listq)

                writer.writerow(listq)
        n += 1

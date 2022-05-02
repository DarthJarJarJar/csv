import csv

new_content = []

with open("employees.csv") as csvfile:
    file_content = csv.reader(csvfile)
    file_list = list(file_content)[1:]
    maxs = 0
  
    for i in range(len(file_list)):
        for row in file_list:
            if row not in new_content:
                salary = int(row[2])
                if salary>=maxs:
                    
                    maxs = salary
                    max_employee = row
                    
        
        new_content.append(max_employee)
        maxs = 0
                    
    

for i in new_content:
    print(i)       
        
        



        
        





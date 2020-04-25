class Mumbai:
    def __init__(self, name, no):
        self.name = name
        self.no = no

class Delhi:
    def __init__(self, name, no):
        self.name = name
        self.no = no

class Bangalore:
    def __init__(self, name, no):
        self.name = name
        self.no = no
M1=500        
m1 = Mumbai("1. Bombay Hospital & Medical Research Center", M1)
M2=745
m2 = Mumbai("2. Balabhai Nanavati Hospital", M2)
M3=1255
m3 = Mumbai("3. L H Hiranandani Hospital", M3)
M4=1335
m4 = Mumbai("4. Fortis Hospital", M4)
M5=560
m5 = Mumbai("5. Jaslok Hospital", M5)

D1=1766
d1 = Delhi("1. AIIMS Hospital", D1)
D2=1600
d2 = Delhi("2. Safdarjung Hospital", D2)
D3=285
d3 = Delhi("3. Fortis Escort Heart Institute", D3)
D4=250
d4 = Delhi("4. Primus Super Speciality Hospital", D4)
D5=300
d5 = Delhi("5. Moolchand Hospital", D5)

B1=1660
b1 = Bangalore("1. Fortis Hospital", B1)
B2=540
b2 = Bangalore("2. Manipal Hospital", B2)
B3=455
b3 = Bangalore("3. Columbia Asia Referral Hospital", B3)
B4=1250
b4 = Bangalore("d. Apollo Hospital", B4)
B5=450

import xlsxwriter
workbook = xlsxwriter.Workbook('COVID-19.xlsx')
worksheet = workbook.add_worksheet('new')
worksheet.write('A1','NAME')
worksheet.write('B1','GENDER')
worksheet.write('C1','DOB')
worksheet.write('D1','NATIONALITY')
worksheet.write('E1','PASSPORT NO.')
worksheet.write('F1','COUNTRY')
worksheet.write('G1','COMMENTS')
worksheet.write('H1','CITY')
worksheet.write('I1','HOSPITAL')
worksheet.write('J1','BEDS')
row = 1
col = 0
a=1
while a==1:
    x=int(input("Press 1 to start new, Press 0 to end."))
    if x==1:
        #personal information
        name=input("Name: ")
        worksheet.write(row,col,name)
        gender=input("Gender (F/M): ")
        worksheet.write(row,col+1,gender)
        dob=input("Date of birth(dd/mm/yyyy): ")
        worksheet.write(row,col+2,dob)
        nationality=input("Nationality: ")
        worksheet.write(row,col+3,nationality)
        pn=input("Passport number: ")
        worksheet.write(row,col+4,pn)
        #travel history
        print("Enter according to the last country you visited in these 2 months:")
        country=int(input("Enter 1 if visited:\n1.UAE\n2.Kuwait\n3.Saudi Arabia\n4.Qatar\nEnter 2 if visited:\n 1.UK\n 2.Italy\n 3.China\n 4.Spain\n 5.Germany\nEnter 3 if others :\n"))
        worksheet.write(row,col+5,country)
        if country==1:
            print("Self Quarantine.\n")
            worksheet.write(row,col+6,"Self Quarantine")
        elif country==3:
            print("Free to go.\n")
            worksheet.write(row,col+6,"Free to go")
            
        elif country==2:
            l=print("COVID-19 infected area.\n")
            worksheet.write(row,col+7,"COVID-19 infected area")
            print("1. Mumbai")
            print("2. Delhi")
            print("3. Bangalore")
            p=int(input("Enter option of city:\n"))
            c=input("Enter City name:")
            worksheet.write(row,col+7,c)
            print("Hospitals available:\n")
            if p == 1:
                print(m1.name)
                print(m1.no)
                print(m2.name)
                print(m2.no)
                print(m3.name)
                print(m3.no)
                print(m4.name)
                print(m4.no)
                print(m5.name)
                print(m5.no)
                m=input("Enter name of Hospital required:")
                worksheet.write(row,col+8,m)
                n=int(input("Enter option of Hospital required:"))
                if n==1:
                    M1=M1-1
                    print("Number of beds left:", M1)
                    worksheet.write(row,col+9,M1)
                elif n==2:
                    M2=M2-1
                    print("Number of beds left:", M2)
                    worksheet.write(row,col+9,M2)
                elif n==3:
                    M3=M3-1
                    print("Number of beds left:", M3)
                    worksheet.write(row,col+9,M3)
                elif n==4:
                    M4=M4-1
                    print("Number of beds left:", M4)
                    worksheet.write(row,col+9,M4)
                elif n==5:
                    M5=M5-1
                    print("Number of beds left:", M5)
                    worksheet.write(row,col+9,M5)
                
            elif p==2:
                print(d1.name)
                print(d1.no)
                print(d2.name)
                print(d2.no)
                print(d3.name)
                print(d3.no)
                print(d4.name)
                print(d4.no)
                print(d5.name)
                print(d5.no)
                m=input("Enter name of Hospital required:")
                worksheet.write(row,col+8,m)
                n=int(input("Enter option of Hospital required:"))
                if n==1:
                    D1=D1-1
                    print("Number of beds left:", D1)
                    worksheet.write(row,col+9,D1)
                elif n==2:
                    D2=D2-1
                    print("Number of beds left:", D2)
                    worksheet.write(row,col+9,D2)
                elif n==3:
                    D3=D3-1
                    print("Number of beds left:", D3)
                    worksheet.write(row,col+9,D3)
                elif n==4:
                    D4=D4-1
                    print("Number of beds left:", D4)
                    worksheet.write(row,col+9,D4)
                elif n==5:
                    D5=D5-1
                    print("Number of beds left:", D5)
                    worksheet.write(row,col+9,D5)
            else:
                print(b1.name)
                print(b1.no)
                print(b2.name)
                print(b2.no)
                print(b3.name)
                print(b3.no)
                print(b4.name)
                print(b4.no)
                print(b5.name)
                print(b5.no)
                m=input("Enter name of Hospital required:")
                worksheet.write(row,col+8,m)
                n=int(input("Enter option of Hospital required:"))
                if n==1:
                    B1=B1-1
                    print("Number of beds left:", B1)
                    worksheet.write(row,col+9,B1)
                elif n==2:
                    B2=B2-1
                    print("Number of beds left:", B2)
                    worksheet.write(row,col+9,B2)
                elif n==3:
                    B3=B3-1
                    print("Number of beds left:", B3)
                    worksheet.write(row,col+9,B3)
                elif n==4:
                    B4=B4-1
                    print("Number of beds left:", B4)
                    worksheet.write(row,col+9,B4)
                elif n==5:
                    B5=B5-1
                    print("Number of beds left:", B5)
                    worksheet.write(row,col+9,B5)
        row+=1
            
    elif x==0:
        workbook.close()
        break

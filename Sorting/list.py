students=["Ali","Ahmed","Ayesha","Zainab","Hassan","Hussain","Fatima","Areeba","Sana","Hira"]
def studentData(students):
    for i in range(len(students)):
        if(students[i]=="Ayesha"):
            return False
    return True
print(studentData(students))
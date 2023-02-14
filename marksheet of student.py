Sname = input("enter the name of student")
rollno = int(input("enter the roll no"))
maths = int(input("enter marks in mathematics"))
english= int(input("enter marks in english"))
physics = int(input("enter marks in physics"))
chemistry = int(input("enter marks in chemistry"))
python = int(input("enter marks in python"))
total = maths + english + physics + chemistry + python
avg = total / 5
percentage = (total /500) * 100
print("\n")
print("Student's Name: {0}\nRoll no: {1}\n".format(Sname,rollno))
print("Subject\t\tMarks\n")
print("Maths\t\t{0}\nEnglsih\t\t{1}\nPhysics\t\t{2}\nChemistry\t{3}\nPython\t\t{4}\n".format(maths,english,physics,chemistry,python))
print("Total Marks\t", total)
print("Average\t\t",avg)
print("Percentage\t",percentage)


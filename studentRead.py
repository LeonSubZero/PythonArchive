#Flavio Leon
#2.22.17
#studentRead.py
#
#Prompt user for name of file from Ex2 and display its content.
#
#input: name of file
#process: prompt for name of file
#output: display on screen using blah blah blah blah bla.

def main():

    
    infileName=input("What file should be opened? ")
    #infileName="students.txt"
    infile=open(infileName,"r")
    lines=infile.readlines()

    #for line in infile:
    #print(line[:-1])
    #break
        
    print("\tStudent Id: {0:^15.3}".format(lines[0]))
    print("\tStudent Name: {0:^13}".format(lines[1][:-1]))
    print("\tStudent GPA: {0:^15}".format(lines[2]))

    print("\tStudent Id: {0:^15.3}".format(lines[3]))
    print("\tStudent Name: {0:^13}".format(lines[4][:-1]))
    print("\tStudent GPA: {0:^15}".format(lines[5]))

    print("\tStudent Id: {0:^15.3}".format(lines[6]))
    print("\tStudent Name: {0:^13}".format(lines[7][:-1]))
    print("\tStudent GPA: {0:^15}".format(lines[8]))

    print("\tStudent Id: {0:^15.3}".format(lines[9]))
    print("\tStudent Name: {0:^12}".format(lines[10][:-1]))
    print("\tStudent GPA: {0:^15}".format(lines[11]))

    print("\tStudent Id: {0:^15.3}".format(lines[12]))
    print("\tStudent Name: {0:^13}".format(lines[13][:-1]))
    print("\tStudent GPA: {0:^15}".format(lines[14]))
          
    infile.close()    
    

        
main()

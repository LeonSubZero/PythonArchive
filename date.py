"""
Flavio Leon
date.py
3/1/2017
prompt mm/dd/yyyy and display as day, month,year.

input: mm dd yyyy
process: prompt for mm/dd/yyyy 
output: display day month year
"""

def main():
    #header
    print("Date Parser...")
    print()
    #prompt
    date = input("Please enter a date (MM/DD/YYYY): ")
    #split date
    dateSplit=date.split("/")
    #create list
    months=("January","February","March","April","May","June","July","August",
            "September","October","November","December")
    #convert month to int
    monthNum=int(dateSplit[0])-1

    #display   
    print("\nThe date means:") 
    print("\tDay:{0}".format(dateSplit[1]))
    print("\tMonth:{0}".format(months[monthNum]))
    print("\tYear:{0}".format(dateSplit[2]))      

    

main()

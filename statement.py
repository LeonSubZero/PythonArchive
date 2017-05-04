"""
Flavio Leon
statement.py
3/1/2017
read in store data in statement.txt. 

input: read in file
process: data from file, calc end balance 
output: display as shown and output to february statement.txt
"""

def main():
    #open read in file
    infile=open("statement.txt", "r")
    #read in first 3 lines slice off \n
    name=infile.readline()
    name=name[0:-1]
    acct=infile.readline()
    acct=acct[0:-1]
    begin=infile.readline()
    #split at colon
    begin=begin.split(":")
    beg=(begin[0])
    #convert to float use sub 1 of previous split
    bal=float(begin[1])
    
    #print(name,acct)<-used for internal testing only

    #initialize acc
    wSum=0
    for x in infile:
        wSum=wSum+float(x)
    #calc end balance
    eBal=bal-wSum
    #print(wSum)<--used for internal testing only
    #open outfile
    outfile=open("February Statement.txt","w")

    #display and format output to outfile
    print("{0:^41}".format("Broward College National Bank"),file=outfile)
    print("{0:^41}".format("February Bank Statement"),file=outfile)
    print("{0:<20} {1:>20}".format("Name","Account Number"),file=outfile)
    print("-"*41,file=outfile)
    print("{0:<20} {1:>20}".format(name,acct),file=outfile)
    print("\n\n",file=outfile)
    print("{0:>19}: ${1:<20}".format(beg,bal),file=outfile)
    print("{0:>20} ${1:<20}".format("Withdrawals:",wSum),file=outfile)
    print("{0:>20} ${1:<20.2f}".format("Ending Balance:",eBal),file=outfile)
    #close both
    infile.close()
    outfile.close()
        
main()

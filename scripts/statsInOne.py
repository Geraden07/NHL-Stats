import urllib
import os
import json
import re
from time import sleep
from BeautifulSoup import BeautifulStoneSoup, SoupStrainer

#Functions for Downloading HTML Files:

#Testing for and deleting any already present files from last fetch
def wipe():
    print "Wiping Old Data...",
    filenum = 0
    while os.path.exists('stats/stats-%s.html' % (filenum+1, )):
        filenum = filenum + 1
    for x in range(filenum):
        os.remove('stats/stats-%s.html' % (x+1, ))
        print ".",
    print " Wipe Done. %s Files Deleted.\n" % (filenum, ),


#Retrieving first [limit] number of pages from NHL.com
def fetch(limit=205):
    print "Fetching New Data...",
    if not os.path.exists('stats'):
        os.mkdir('stats')
    page=1
    while page<=limit:
        urllib.urlretrieve('http://www.nhl.com/ice/careerstats.htm?pg=%s' % (page, ),'stats/stats-%s.html' % (page, ))
        page = page + 1
        print ".",
        sleep(1)
    print "Fetch Done. %s Files Fetched." % (limit, ),


#Functions for Opening, Manipulating, and Saving all the data.
def readIn(page):
    """Function that, when given an integer refering to a file of the naming convention
        stats-#.html where # is the integer, opens the file, passes the file string
        to the parsing object, then returns the result of parsing the string.

        Returns the parsing objects result set"""
    f = open('stats/stats-%s.html' % (page, ))
    lots = f.read()
    f.close()
    myStrainer = SoupStrainer('tbody')
    myParser = BeautifulStoneSoup(lots, myStrainer)
    myResults = myParser.findAll('td')
    print "Read In"
    return myResults


def parse(results):
    """Function that, when passed a parsing objects result set, sanitizes any remaining
        HTML tags.

        Returns a list of text data."""
    stats = []
    for result in results:
        stat = unicode(''.join(result.findAll(text=True))).encode("utf-8").strip()
        stats.append(stat)
    print "Extracted HTML Code"
    return stats


def listify(stats):
    """Function that, given an ordered list of data, seperates and groups each row in
        it's own sublist.

        Returns the list of lists"""
    #Declarations / Constants
    rowlength = 17
    biglongthing = [['']]
    smallerlongthing = []

    #Loop through and group data into lists by their row
    y=0
    for x in stats:
        if y<rowlength:
            smallerlongthing.append(x)
            y+=1
        else:
            smallerlongthing.append(x)
            y=0
            biglongthing.append(smallerlongthing)
            smallerlongthing = []
    biglongthing.remove([''])
    print "Organized and populated data list"
    return biglongthing


def workHorse():
    #Declarations / Constants
    #           0      1          2         3           4                  5            6    7    8    9     10     11    12    13    14    15    16     17            18
    headers = ['#', 'Player', 'Cur Team', 'POS', '1st NHL Season', 'Last NHL Season', 'GP', 'G', 'A', 'P', '+/-', 'PIM', 'PP', 'SH', 'GW', 'GT', 'OT', 'Shots', 'Points Per Game']
    pages =205
    biglist = []
    sortedbiglist = [[]]

    #Loop through and store results from each page
    for omg in range(pages):
        results = readIn(omg+1)
        stats = parse(results)
        output = listify(stats)
        biglist.extend(output)
        print "For page %s" % (omg+1, )

    #Add an element to each row P/GP
    for x in biglist:
        x6 = x[6].replace(",","")
        x9 = x[9].replace(",","")
        if int(x6)!=0:
            x.append(float(x9)/float(x6))
        else:
            x.append(float(0))
    print "Calculated P/GP"

    #Sort the list and replace all row's first value (x[0]) with new position in list
    sortedbiglist = sorted(biglist, key=lambda inn: inn[18],reverse=True)
    y=1
    for x in sortedbiglist:
       del x[0]
       x.insert(0,y)
       y+=1
    print "Sorted List"

    #Write list object to a file
    f = open('stats/jlistdata.json','w')
    json.dump(sortedbiglist, f)
    f.close()
    #print "Program Finished"

#Function for Opening and Printing the data
def printStatsList(filename = 'stats/jlistdata.json'):
    #Declarations / Constants
    lef = 30
    mid = 6
    righ = 16
    #           0      1          2         3           4                  5            6    7    8    9     10     11    12    13    14    15    16     17            18
    headers = ['#', 'Player', 'Cur Team', 'POS', '1st NHL Season', 'Last NHL Season', 'GP', 'G', 'A', 'P', '+/-', 'PIM', 'PP', 'SH', 'GW', 'GT', 'OT', 'Shots', 'Points Per Game']

    #Open file and store list
    f = open(filename,'r')
    sortedbiglist = json.load(f)
    f.close()

    #Print headers row and iterate through sorted list printing each row
    print headers[0].ljust(mid),
    print headers[1].ljust(lef),
    print headers[2].ljust(mid),
    print headers[3].ljust(mid),
    print headers[6].ljust(mid),
    print headers[9].ljust(mid),
    print headers[18].ljust(righ)
    y=1
    for x in sortedbiglist:
        x6=x[6].replace(",","")
        if int(x6)>50 and x[2] != "" and x[3] != 'D': #Uncomment this line and tab the next 7 lines of code if you wish to only print results of players who have played more than 50 games
            print repr(y).ljust(mid),
            print x[1].ljust(lef),
            print x[2].ljust(mid),
            print x[3].ljust(mid),
            print x[6].ljust(mid),
            print x[9].ljust(mid),
            print repr(x[18]).ljust(righ)
            y+=1


#To run it all:
if __name__ == "__main__":
    wipe()
    fetch()
    workHorse()
    printStatsList()
    raw_input("Press enter to terminate.")

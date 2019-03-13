import csv

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:
    
    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''
    for name in filenames:
        with open(name, 'rb') as f:
            #open file as f
            #change file to a csv format
            reader = csv.reader(f)
            #initialize  an array
            result = []
            #number of row before a new data set
            
            rowslice = 5
            for row in reader:
                #since the first 3 elements are the same for every row we start from 3
                start = 3
                #end of data set before going to the new row slice
                end = start + rowslice
                #row length to make sure our loop dosent surpass its length
                rowlen = len(row)
                full = []
                while end <= rowlen:
                    #the first 3 items
                    full = [row[0]]+[row[1]]+[row[2]]
                    
                    #add the last 5 items 
                    for x in range(start,end):
                        full += [row[x].strip()]
                        result.append(full)
                        
                        
                    end += rowslice
                    start += rowslice
       
            
        newname = 'updated_'+name
        with open(newname, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(result)  

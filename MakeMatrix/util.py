import os, glob

#TODO: 

'''
Add a column to end of a file. If the file does not exist, it is created. 
fileName - Name of the file 
columnList - list of values to be inserted
sep - column separator; default - tab 
EOL - End Of Line; default - newline 
'''

def addColumn(fileName, columnList, header='UNK',sep='\t', EOL='\n'):
    #The number of lines in the file should be same as the number of the columns 
    # print("Adding column to ",columnList[:10])
    columnList = [header] + list(columnList)
    if glob.glob(fileName) == []:
        # The file does not exist yet. So create an empty file and insert the first column.
        try:
            # print("THERE WAS AN EMPTY FILE.")
            with open(fileName,'w') as fwrite :                
                for count in range(len(columnList)):
                    fwrite.write('{}{}'.format(columnList[count],EOL))
        except Exception as e:
            print(e)
    else:
        try:
            # Copy the file to tmp file and insert the extra column. 
            # Later rename the tmp file to the original.
            with open(fileName,'r') as fread :
                with open(fileName+'.tmp','w') as fwrite:                
                    for count,line in enumerate(fread):
                        fwrite.write(line.strip())
                        # Insert a separator before inserting a new column.
                        fwrite.write(sep)
                        fwrite.write('{}{}'.format(columnList[count],EOL))
            
            # Rename the tmp file.                          
            os.system('mv {} {}'.format(fileName+'.tmp',fileName))
            os.system('rm -rf {}'.format(fileName+'.tmp'))
        except Exception as e:
            print(e)


fileIdToSpecimenIdMapping = {}
with open('mappings.tsv') as f:
    #Ignore first line
    f.next()
    for line in f:
        fileId,SpecimenId,gnosId = line.strip().split()
        fileIdToSpecimenIdMapping[fileId] = SpecimenId


'''
Returns SpecimenId for a given FileId
'''
def getMapping(fileId):
    #Given fileId return Submitter Specimien ID from mappings.tsv
    try:
        return fileIdToSpecimenIdMapping[fileId]
    except Exception as e:
        print("ERROR: ",e)
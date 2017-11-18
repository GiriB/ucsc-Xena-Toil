"""
Extracts FileID,gnosID,SpecimenID values from manifest downloaded from file-browser 
"""
import pandas as pd

#We need sample info to get fileName,id,gnosId
samples = pd.read_csv('manifest.tsv',sep='\t')
columnsList = list(samples.columns.values)

try:

	FileID_Index = columnsList.index('Upload File ID')
	SubmitterSpecimenID_Index = columnsList.index('Submitter Specimen ID')
	BundleUUID_Index = columnsList.index('Data Bundle UUID')


	MAPPINGS = {}
	SpecimenIds = []
	FileIds = []



	with open('mappings.tsv','w') as fwrite:
		fwrite.write('fileID\tSubmitterSpecimenID\tBundleUUID\n')
		for i in samples.values:
			
			fwrite.write('{}\t{}\t{}\n'.format(i[FileID_Index],i[SubmitterSpecimenID_Index],i[BundleUUID_Index]))
			SpecimenIds.append(i[SubmitterSpecimenID_Index])
			FileIds.append(i[FileID_Index])
except Exception as e:
	print('ERROR: ',e)


try:	

	#The following checks ensure that the IDs can uniquely identify a file.
	assert len(SpecimenIds)==len(set(SpecimenIds))
	assert len(FileIds)==len(set(FileIds))
	# print samples['Submitter Donor ID'],samples['Submitter Specimen ID'],samples['Upload File ID']
except Exception as e:
	print(e)

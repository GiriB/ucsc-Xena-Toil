# This reads the name of sammples from samples.txt(fileName,id,gnosId) and
# downloads them to /ouptputs
# TODO: specify file name ?
# TODO: TOIL_REDWOOD_ACCESS_TOKEN, TOIL_REDWOOD_ENDPOINT

import os
import logging
log = logging.getLogger('ucscXena')

'''
extracts a tarfile
'''
def extract(tarFile):
	os.system('tar -zxf {}'.format(tarFile))


with open('samples.txt','r') as f:
	next(f)

	for row in f:
		sample_fileName,sample_id,sample_gnosid = row.split(' ')
		os.system('docker run --rm -it -e ACCESS_TOKEN=a9a396e6-e65c-4551-b866-289612b401b9 -e REDWOOD_ENDPOINT=walt-hca.ucsc-cgl.org -v $(pwd)/outputs:/outputs quay.io/ucsc_cgl/core-client:1.1.0-alpha download '+sample_id+' /outputs')
		
		# # directoryPath = './outputs/{}'.format(gnosId)
		# # filePath = './outputs/{}/{}'.format(sample_gnosid,sample_fileName)
		# # Check it the file was downloaded
		# if glob.glob(directoryPath) != [] and glob.glob(filePath):
		# 	# Extract the file here.
		# 	#os.system('tar -zxf ')
		# 	print()
		# else:
		# 	sys.stderr.write('File not found. Do {} and {} exist?'.format((directoryPath),filePath))

		print(sample_fileName,sample_id,sample_gnosid)

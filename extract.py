# This reads the name of sammples from samples.txt(fileName,id,gnosId) and
# downloads them to /ouptputs
# TODO: specify file name ?
# TODO: TOIL_REDWOOD_ACCESS_TOKEN, TOIL_REDWOOD_ENDPOINT
# TODO: make samples.txt tab-separated values
# TODO: instead of using ROOT_PATH/, ask for output folder path 

import os, glob

# ROOT_PATH is used to avoid using relative paths, as it causes confusion.
ROOT_PATH = os.getcwd()

print(ROOT_PATH)

'''
extracts a tarfile
'''
def extractTar(filePath,directoryPath="./"):
    os.system('tar -zxf {} --directory {}'.format(filePath,directoryPath))

'''
remove a file
'''
def removeTar(filePath):
	os.system('rm {}'.format(filePath))


with open('samples.txt','r') as f:
    next(f)

    for row in f:
        sample_filename,sample_id,sample_gnosid = row.strip().split(' ')

        # Download
        # os.system('docker run --rm -it -e ACCESS_TOKEN=a9a396e6-e65c-4551-b866-289612b401b9 -e REDWOOD_ENDPOINT=walt-hca.ucsc-cgl.org -v $(pwd)/outputs:/outputs quay.io/ucsc_cgl/core-client:1.1.0-alpha download '+sample_id+' /outputs')

        directoryPath = '{}/outputs/{}'.format(ROOT_PATH,sample_gnosid)
        filePath = '{}/outputs/{}/{}'.format(ROOT_PATH,sample_gnosid,sample_filename)

        try:
            # Check it the file was downloaded
            if glob.glob(directoryPath) != [] and glob.glob(filePath):
                # Extract the file.
                extractTar(filePath,directoryPath)

                # Remove the tar.gz??
                removeTar(filePath)
            else:
                print('Error: File not found. Do {} and {} exist?'.format(directoryPath,filePath))

            print(sample_filename,sample_id,sample_gnosid)
        except Exception as e:
            print("Error: {}".format(e))
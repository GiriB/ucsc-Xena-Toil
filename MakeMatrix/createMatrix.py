    # NOTE: Appending 'FAIL.' with filename
# TODO: Make file reading with chunk
import glob, sys, os 
import pandas as pd
from util import addColumn

OUTPUT_DIR = '/Users/Apple/workspace/ucsc/output' #'/home/ec2-user/efs/code/outputs'
OUTPUT_MATRIX_FOLDER = './output'

cfg = open('makematrix.cfg','r')
cfg_data = cfg.readlines()
cfg.close()

#We need sample info to get fileName,id,gnosId
samples = pd.read_csv('../test_samples.txt',sep='\t')

for param_config in cfg_data:
    '''
    param - which parameter to extract
    param_file - from which file to extract
    '''
    # strip extra whitespaces
    param,param_file = map(str.strip,param_config.split('\t'))
    
    print(param,param_file)
    
    df = pd.DataFrame()    
    count = 0
    # For each sample find the param file and extract the appropriate column 
    for row in samples.values:
        #print(row)
        sample_filename,sample_id,sample_gnosid = row

        '''
        sample_param_file - Absolute path to the param file
        '''
        # sample_filename.split('.')[0] gets the 'filename' from 'filename.tar.gz'
        sample_param_file = '{}/{}/{}/{}'.format(OUTPUT_DIR,sample_gnosid,'FAIL.'+sample_filename.split('.')[0],param_file )
        
        # If file exists 
        if glob.glob(sample_param_file) != []:
            
            # Read the file 
            data = pd.read_csv(sample_param_file,sep='\t')
    
            try:
                # Add 'id' column in df if not already present
                if not 'id' in df:    
                    # Extract the very first column and set that as 'id' column for the  output matrix
                    df['id'] = data[data.columns.values[0]].values
                    col = df['id']
                    # print(df['id'])
                    # Delete an already existing file.
                    os.system('rm {}/{}_mat.tsv'.format(OUTPUT_MATRIX_FOLDER,param))
                    # col is a Pandas series object
                    # col.set_value(0,id)
                    addColumn('{}/{}_mat.tsv'.format(OUTPUT_MATRIX_FOLDER,param),col,header='id',sep='\t')

                    # df.set_index('id')

                #Extract param column 
                col = data[param]
                # Add column to data_frame, under header 'gnosId'
                # TODO: Write the column here. 
                # col is a Pandas series object
                # col.set_value(0,sample_gnosid)
                addColumn('{}/{}_mat.tsv'.format(OUTPUT_MATRIX_FOLDER,param),col,header=sample_gnosid, sep='\t')

                # df[sample_gnosid] = col.values
                    
               # print(sys.getsizeof(df))
            except Exception as e:
                print("ERROR: {} does not contain {} header.".format(sample_param_file,param))
                print(e)
        else:
            print('ERROR: File does not exist :',sample_param_file )

    # Write df as a tab-separated file
    # index=False - do not write the default index with the file
    # df.to_csv('{}/{}_mat.tsv'.format(OUTPUT_MATRIX_FOLDER,param),sep='\t',index=False)
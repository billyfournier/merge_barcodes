#!/usr/bin/env python
# file merge_barcodes.py
'''
Reintegrates the output from extract_barcodes.py (barcodes.fastq) back into a fastq file, such as merged.fastq.   
'''
__author__ = "Billy Fournier"
__license__ = "GPL"
__email__ = "billyfournier2000@yahoo.com"

from optparse import OptionParser
from itertools import izip, izip_longest

parser = OptionParser()
parser.add_option("-m", "--input_merged", dest="input_merged", help="merged.fastq file to read")
parser.add_option("-b", "--input_barcode", dest="input_barcodes", help="barcode.fastq file to read")
parser.add_option("-o", "--file", dest="output",
                  help="output filename", default="combined.fastq")

(options, args) = parser.parse_args()


if options.input_merged is None:
	print "ERROR: flag (-m) is required. "
	print "       This is the PATH to your merged.fastq"
	exit(-1)
if options.input_barcodes is None:
	print "ERROR: flag (-b) is required. "
	print "       This is the PATH to your mergedbarcodes.fastq"
	exit(-1)

file1 = options.input_merged
file2 = options.input_barcodes
output = options.output

list=["@","+"]
with open(file1) as mergedFile, \
    	open(file2) as barcodedFile, \
	open(output,"w") as newFile:
	for line1,line2 in izip_longest(mergedFile,barcodedFile):
		if line1[0] in list:
			newFile.write(line1)
		else:
			str = line2.rstrip() + line1			
			newFile.write(str)


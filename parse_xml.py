# To run this script, type in the following in the terminal, replacing content in brackets with the appropriate arguments:
# python parse_xml.py [name of folder with XML files] [name of file you wish to output results to]


# Import the "etree" class from the "lxml" module
from xml.etree import ElementTree
# Import the sys module
import sys
# Import the os module
import os

# This variable stores the name of the folder that holds all XML files.
folder_with_xml_files = sys.argv[1]

# This variable stores the name of the file we will write our collected sentences to.
output_file_name = sys.argv[2]

# Iterate over each file in the folder.
for file_name in os.listdir(folder_with_xml_files):
	
	# Open the file and get the root of the file.
	element_tree = ElementTree.parse(os.path.abspath(file_name))

	# Get the root of the element tree
	root = element_tree.getroot()


	### TODO ###

	# Step 1. What are the names and paths of the XML tags we are interested in? [Done]
	# root -> title
	# root -> content -> sections -> section -> title
	# root -> content -> sections -> section -> paragraphs -> paragraph -> sentence -> text

	# Step 2. How can we use the "find" and "findall" functions to find the content in the tags we are interested in? [Fill in code]
	# Put all sentences in list_of_sentences
	list_of_sentences = []


	# Step 3. Write all sentences out to a new file. [Done]
	# Open the output file.
	output_file = open(output_file_name, 'w')

	# for each sentence in list_of_sentences
	for sentence in list_of_sentences:

		# Write a sentence to the file.
		output_file.write(sentence + '\n')



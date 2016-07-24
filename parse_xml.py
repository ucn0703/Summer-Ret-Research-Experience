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

# Put all sentences in list_of_sentences
list_of_sentences = []

# Open the output file.
output_file = open(output_file_name, 'w')

# Iterate over each file in the folder.
for file_name in os.listdir(folder_with_xml_files):

	# Ignore files that end with '.sci.xml'
	if not file_name.endswith('.sci.xml'):

		print '========================='
		print 'File:', file_name

		# Open the file and get the root of the file.
		element_tree = ElementTree.parse(folder_with_xml_files+'/'+file_name)

		# Get the root of the element tree
		root = element_tree.getroot()


		### TODO ###

		# Step 1. What are the names and paths of the XML tags we are interested in? [Done]
		# (A) root -> title
		# (B) root -> content -> sections -> section -> title
		# (C) root -> content -> sections -> section -> paragraphs -> paragraph -> sentence -> text

		# Step 2. How can we use the "find" and "findall" functions to find the content in the tags we are interested in? [Fill in code]
		# (A)
		title = root.find("title").text
		# Only add title to list_of_sentences if title exists
		if title:
			list_of_sentences.append(title)

		section_list = root.find('content').find('sections').findall('section')
		for S in section_list: 
			# (B)
			section_title = S.find('title').text
			# Only add section_title to list_of_sentences if section_title exists
			if section_title:
				list_of_sentences.append(section_title)
			paragraphs = S.find('paragraphs')
			paragraph_list = paragraphs.findall('paragraph')
			for P in paragraph_list:
				for x in P:
					# (C)
					text = x.find('text').text
					# Only add text to list_of_sentences if text exists
					if text:
						list_of_sentences.append(text)

	  
# Step 3. Write all sentences out to a new file. [Done]
# for each sentence in list_of_sentences
for sentence in list_of_sentences:

	# Print the sentence
	print 'sentence:', sentence

	# Write a sentence to the file.
	output_file.write(sentence.encode('utf-8') + '\n')



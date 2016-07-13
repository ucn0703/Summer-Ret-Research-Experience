# Import the "etree" class from the "lxml" module
from xml.etree import ElementTree

# Open the XML document and get the root of the XML tree.
xml_document_root = ElementTree.parse('xml_files/sample_document.xml').getroot()



### Example 1: Save all author names in a list. ###

# Save the content in the "<authors>" tag.
authors = xml_document_root.find('authors')

# Create an initially empty list of author names
author_names_list = []

# for each <author> element that is a child of the <authors> element
for author in authors.iter('author'):

	# Save the text between <author> and </author>
	text = author.text

	# Add each author
	author_names_list.append(text)

# Now author_names_list is a list of all author names.
print 'Author names list:', author_names_list
print '------------------------------------------'


### Example 2: Save all animal names and descriptions in a list ###

# We know this is the path to animals: document -> content -> animals. Then, <animals> contain several <animal>, each of which has a <name> and a <description>.

# Save the content in the "animals" tag.
animals = xml_document_root.find('content').find('animals')

# Create an initially empty list of animals
animal_list = []

# For each <animal> element that is a child of the <animals> element
for animal in animals.iter('animal'):

	# Save the animal name
	animal_name = animal.find('name').text

	# Save the animal description
	animal_description = animal.find('description').text

	# Create a dictionary of attributes for the animal
	animal_dictionary = { 'name': animal_name, 'description': animal_description }

	# Add the animal's dictionary to the animal_list.
	animal_list.append(animal_dictionary)

# Now animal_list is a list of animal dictionaries.
print 'Animal list:', animal_list
# We can also print the name and description of the first animal in animal_list
print 'Name of first animal in animal_list:', animal_list[0]['name']
print 'Description of first animal in animal_list:', animal_list[0]['description']






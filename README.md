# resume-semantic-search

Overview of the scripts included in this repository: "Recommender algorithm.py" and "Table constructor.py". These scripts help to parse and process data from a collection of Curriculum Vitae, transform the data into a structured table and provide recommendations based on text similarity.

# 1. Parser.py
This script provides the functionality to parse resumes in a PDF format. It uses the GPT-3 model from OpenAI to extract relevant information from resumes and format the data in a structured JSON format. The extracted JSON data is then saved as text files.

The script follows the steps:

PDF to Text: Each resume PDF file is converted to a text string.
Data Extraction: The text string is sent to GPT-3 as a completion prompt. GPT-3 then returns a structured JSON string with all the relevant data extracted from the resume.
Save Extracted Data: The extracted JSON string is then saved as a text file with the same filename as the original resume but with a .txt extension.
Requirements
openai: OpenAI API for GPT-3, which is used to parse the resumes.
pdftotext: Used to convert PDF files into text strings.
Instructions
Place your CVs to parse in the "CV_to_study" directory.
Make sure to install all the required Python packages: pip install openai pdftotext.
Run the ResumeParser.py script: python ResumeParser.py.
The parsed CVs will be saved in the "CV_parsed" directory.

# 2. Table constructor.py
This script parses the text data of CVs in JSON format and extracts relevant information to construct a structured pandas DataFrame. The DataFrame is then exported to an Excel file, "cvs.xlsx".

Specifically, it extracts the following details from each CV:

Basic information: full name, email, LinkedIn URL, level of education, university, graduation year
Professional experience (up to 5 entries): job title, company, duration
Each row in the resulting DataFrame corresponds to a single CV, with the filename as the first column.

# 3. Recommender algorithm.py
This script creates a recommender system that reads and processes CVs in JSON format, generating embeddings for each of the CVs, and then identifies the most similar CVs based on cosine distance between their embeddings.

Here's a brief rundown of its functionalities:

It reads the text files from the 'CV_parsed' directory and transforms them into a pandas DataFrame. Unnecessary fields are removed from the data.
Embeddings for each CV are calculated using OpenAI's API with caching mechanism to avoid redundant computations.
It includes a function print_recommendations_from_strings that takes a list of strings, a source string's index and the number of nearest neighbors to recommend. It generates embeddings for all strings, calculates the cosine distances between the source string and all other strings, and then identifies the indices of the nearest neighbors.
It plots a 2D chart of nearest neighbors using t-SNE for visualization. (Commented out currently)
You'll need to have your OpenAI API Key to run this script.



# How to Run
Ensure all dependencies are installed.
Place all your CVs in PDF format in a directory named 'CV_to_study'.
Run the "Parser.py" script to parse the CVs in JSON format in a directory named 'CV_parsed'
Run the "Table constructor.py" script that uses the parsed CVs and construct a structured table. The resulting table will be saved as an Excel file "cvs.xlsx".
Run the "Recommender algorithm.py" script. It will create a recommender system based on the CVs and the Job Offer, that you need to specify as well. 

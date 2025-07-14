# paper_summarizer.py
'''
This script uses the Ollama API to perform several 
summarization methods on research papers.
'''
import ollama
from pypdf import PdfReader

''' Use model locally

First start ollama:
	$ ollama serve &
Then run:
	$ python3.10 paper_summarizer.py
'''

'''
	Uses pypdf to extract text from a pdf file,
	organizing text into groups of 5 pages.
'''
def extract_pages(file):
	reader = PdfReader(file)
	page_group_arr = []
	page_group = ""
	counter = 0

	for page in reader.pages:
		page_group += page.extract_text() + "\n"
		counter += 1
		if counter % 5 == 0:
			page_group_arr.append(page_group)
			page_group = ""

	if page_group.strip():
		page_group_arr.append(page_group)

	return page_group_arr

'''
- Takes a model and a text input.
- Applies the extractive summarization prompt.
- Returns the model's response containing the 
  most important sentences from the text.
'''
def extractive_prompt(text, model):
    prompt = f"""
	Select 5-10 sentences from the following text that are most representative
	of the main points. Do not paraphrase or summarize, extract exact sentences.

    Text:
    {text}
	"""
 
    response = ollama.chat(model=model, messages=[
		{
			'role': 'user',
			'content': prompt,
		}
        ]) 
    return response['message']['content']

# Main script execution
models = ["mistral", "llama3", "gemma3"]
paper1 = 'Papers/33789-Article Text-37857-1-2-20250410.pdf'

page_groups = extract_pages(paper1)
group_summaries = [] 

for group in page_groups:
	group_summaries.append(extractive_prompt(group, models[0]))	
important_sen = '\n'.join(group_summaries)

abstractive_prompt = f"""
Below are the most important sentences extracted from a research paper.
Please construct a simple summary of the paper in a few sentences.
Then select 10ish keywords that best cover the main topics of research.

Sentences:
{important_sen}
"""

response = ollama.chat(model=models[0], messages=[
	{
		'role': 'user',
		'content': abstractive_prompt,
	}
])

final_summary = response['message']['content']

with open('./Output/summary.txt', 'w') as f:
    f.write("Final Summary:\n")
    f.write(final_summary)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

from nlp_processor import extract_keywords

with open("../professors.json", "r") as f:
    professors_data = json.load(f)

class Query(BaseModel):
	professor: str
	school: str

app = FastAPI()

# allow communication with frontend (middleware)
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# make endpoint for requests
@app.post("/api/summarize")
async def get_summary(query: Query):
	"""
	Given a professor and school, return a summary JSON
		(currently just a default summary)
	"""

	print(f"Recieved request for Professor: {query.professor} at {query.school}")
	key = f"{query.professor}|{query.school}"
	
	if key not in professors_data:
		print(f"{key} not found")
		return {
			"professor": query.professor,
			"school": query.school,
			"keywords": ["N/A"],
			"summary": "Professor not found. Please check the name and school."
		}
  
	print(f"{key} found, proceeding with summarization...")
	abstracts = ""
	for paper in professors_data[key]["papers"]:
		abstracts += paper["abstract"] + ", "
	abstracts.strip(", ")

	keywords = extract_keywords(abstracts)
	summary = f"This is a summary from the backend on {query.professor}"

	return {
		"professor": query.professor,
		"school": query.school,
		"keywords": keywords,
		"summary": summary
	}

@app.get("/")
async def root():
    return {"message": "Welcome to the backend API!"}
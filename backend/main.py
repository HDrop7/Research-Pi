from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

	keywords = ["RPI", "Computer Vision", "Neural Networks", "Data Science"] 
	summary = f"This is a summary from the backend on {query.professor}"

	return {
		"professor": query.professor,
		"school": query.school,
		"keywords": keywords,
		"summary": summary
	}

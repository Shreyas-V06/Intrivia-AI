from fastapi import APIRouter
from initializers.initialize_db import initialize_db

query_router = APIRouter()

@query_router.get('/search')
async def search_by_tag(tag: str):
    try:
        db = initialize_db()
        collection = db.Intrivia.interviews
        interviews = list(collection.find({'tags':tag.lower()}))
    
            
        if interviews:
            return {
                "success": True,
                "message": f"Found {len(interviews)} interviews with tag '{tag}'",
                "data": interviews
            }
        else:
            return {
                "success": True,
                "message": f"No interviews found with tag '{tag}'",
                "data": []
            }
            
    except Exception as e:
        return {
            "success": False,
            "message": "An error occurred while searching for interviews",
            "error": str(e)
        }

@query_router.get('/interview/{interview_id}')
async def get_interview_by_id(interview_id: str):

    try:
        db = initialize_db()
        collection = db.Intrivia.interviews      

        interview = collection.find_one({"interview_id":interview_id})
        
        if interview:
            return {
                "success": True,
                "message": "Interview found",
                "data": interview
            }
        else:
            return {
                "success": False,
                "message": "Interview not found"
            }
            
    except Exception as e:
        return {
            "success": False,
            "message": "An error occurred while fetching the interview",
            "error": str(e)
        }

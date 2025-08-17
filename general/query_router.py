from fastapi import APIRouter
from initializers.initialize_db import initialize_db

query_router = APIRouter()

@query_router.get('/search')
async def search_by_tag(tag: str):
    """
    Search for interviews by tag in the Intrivia database.
    
    Args:
        tag (str): The tag to search for. Will be converted to lowercase for case-insensitive search.
    
    Returns:
        dict: A response dictionary containing:
            - success (bool): Whether the operation was successful
            - message (str): A descriptive message about the result
            - data (list): List of matching interviews, excluding MongoDB _id field
            
    Example Response:
        {
            "success": true,
            "message": "Found 2 interviews with tag 'python'",
            "data": [
                {
                    "title": "Python Basics",
                    "description": "Introduction to Python",
                    "upvotes": 0,
                    "tags": ["python", "beginners"],
                    ...
                },
                ...
            ]
        }
    """
    try:
        db = initialize_db()
        collection = db.Intrivia.interviews
        interviews = list(collection.find(
        {"tags": tag},
        {"_id": 0}  
         ) 
    )

            
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

@query_router.get('/interview/description')
async def get_interview_by_id(interview_id: str):
    """
    Retrieve a specific interview by its ID from the Intrivia database.
    
    Args:
        interview_id (str): The unique identifier of the interview to retrieve
    
    Returns:
        dict: A response dictionary containing:
            - success (bool): Whether the operation was successful
            - message (str): A descriptive message about the result
            - data (dict): The interview details, excluding MongoDB _id field
            
    Example Response:
        {
            "success": true,
            "message": "Interview found",
            "data": {
                "title": "Python Basics",
                "description": "Introduction to Python",
                "upvotes": 0,
                "tags": ["python", "beginners"],
                ...
            }
        }
    """
    try:
        db = initialize_db()
        collection = db.Intrivia.interviews      

        interview = collection.find_one({"interview_id":interview_id},{"_id":0})
        
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


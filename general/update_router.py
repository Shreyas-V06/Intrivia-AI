from fastapi import APIRouter
from initializers.initialize_db import initialize_db

update_router = APIRouter()

@update_router.put('/interview/upvote/{interview_id}')
async def upvote_interview(interview_id: str):
    """
    Increment the upvote count of an interview by 1.
    
    Args:
        interview_id (str): The ID of the interview to upvote
        
    Returns:
        dict: A dictionary containing the success status and updated upvote count
    """
    try:            
        db = initialize_db()
        collection = db.Intrivia.interviews

        result = collection.find_one_and_update(
            {"interview_id": interview_id},
            {"$inc": {"upvotes": 1}},
            return_document=True
        )
        
        if result:
            return {
                "success": True,
                "message": "Interview upvoted successfully",
                "data": {
                    "interview_id": str(result["_id"]),
                    "upvotes": result["upvotes"]
                }
            }
        else:
            return {
                "success": False,
                "message": "Interview not found"
            }
            
    except Exception as e:
        return {
            "success": False,
            "message": "An error occurred while upvoting the interview",
            "error": str(e)
        }

@update_router.put('/interview/downvote/{interview_id}')
async def downvote_interview(interview_id: str):
    """
    Decrement the upvote count of an interview by 1.
    
    Args:
        interview_id (str): The ID of the interview to downvote
        
    Returns:
        dict: A dictionary containing the success status and updated upvote count
    """
    try:            
        db = initialize_db()
        collection = db.Intrivia.interviews
        interview = collection.find_one({"interview_id": interview_id})
        if not interview:
            return {
                "success": False,
                "message": "Interview not found"
            }
        
        result = collection.find_one_and_update(
            {"interview_id": interview_id},
            {"$inc": {"upvotes": -1}},
            return_document=True
            )
            
        return {
                "success": True,
                "message": "Interview downvoted successfully",
                "data": {
                    "interview_id": str(result["_id"]),
                    "upvotes": result["upvotes"]
                }
            }
        
            
    except Exception as e:
        return {
            "success": False,
            "message": "An error occurred while downvoting the interview",
            "error": str(e)
        }

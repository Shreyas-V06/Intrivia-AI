from fastapi import APIRouter
from initializers.initialize_db import initialize_db
from initializers.initialize_llm import initialize_generator_llm
from statistics import mean
from prompts.results import create_summary_prompt


evaluation_router = APIRouter()


@evaluation_router.get('/evaluate/{session_id}')
async def evaluate_interview_session(session_id: str):
    """
    Evaluate all responses from an interview session and generate a summary.
    
    Args:
        session_id (str): The unique session identifier
        
    Returns:
        dict: Evaluation results including individual responses, average score, and summary
    """
    try:

        db = initialize_db()
        collection = db.Intrivia.sessions
        suggestion_set = list(collection.find({"session_id": session_id},{"_id": 0}))
        
        if not suggestion_set:
            return {
                "success": False,
                "message": "No session data found"
            }
        scores = [item.get('score', 0) for item in suggestion_set]
        average_score = mean(scores) if scores else 0
        all_suggestions = "\n".join([item.get('suggestion', '') for item in suggestion_set])
        llm = initialize_generator_llm()
        summary_prompt = create_summary_prompt(all_suggestions)
        summary = llm.invoke(summary_prompt)

        return {
            "success": True,
            "message": "Evaluation completed successfully",
            "data": {
                "suggestion_set": suggestion_set,
                "average_score": round(average_score, 2),
                "overall_summary": summary,
                "total_responses": len(suggestion_set)
            }
        }
            
    except Exception as e:
        return {
            "success": False,
            "message": "An error occurred during evaluation",
            "error": str(e)
        }
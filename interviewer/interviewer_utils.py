from schemas.QAmodel import QAItem
from typing import List
from initializers.initialize_db import initialize_db
from utils import convert_dict_to_qaitem
#TODO:get question mechanism which gets the question based on interview_id and question_id

def get_current_question_item(interview_id,question_id):
    try:
        db = initialize_db()
        collection = db.Intrivia.interviews      

        interview = collection.find_one({"interview_id":interview_id})
        qa_item = convert_dict_to_qaitem(interview['QAset'][question_id])
        if interview:
            return qa_item
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


def reducer(obj1, obj2):
    if isinstance(obj1, str):
        return obj1 if obj1.strip() else obj2
    elif isinstance(obj1, list):
        return obj1 if obj1 else obj2
    else:
        return obj2


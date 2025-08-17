from langgraph.checkpoint.memory import MemorySaver
from interviewer.graph_nodes import *
from schemas.SharedState import SharedState
from langgraph.graph import StateGraph,START,END


memory = MemorySaver()


workflow = StateGraph(SharedState)
workflow.add_node("responder", responder)
workflow.add_node("router", router)
workflow.add_node("evaluator", evaluator)
workflow.add_node("join_node", join_node)
workflow.add_edge(START, "responder")
workflow.add_edge(START, "router")
workflow.add_edge(START, "evaluator")
workflow.add_edge("responder", "join_node")
workflow.add_edge("router", "join_node")
workflow.add_edge("evaluator", "join_node")

workflow.add_conditional_edges(
    "join_node",
    lambda state: state
  )

graph = workflow.compile(checkpointer=memory)

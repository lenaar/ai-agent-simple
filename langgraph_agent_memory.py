from langgraph.checkpoint.sqlite import SqliteSaver

memory = SqliteSaver.from_conn_string(":memory:")


def get_thread_config():
    config = {
        "configurable": {"thread_id": 1, "checkpoint_ns": ""}
    }   
    return config





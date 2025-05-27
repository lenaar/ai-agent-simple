from langgraph_agent import get_thread_config

def skills_query_graph(agent, question):
    # Format the question as a proper message state
    messages_state = {
        "messages": [("user", question)]
    }
    
    # Get thread configuration
    config = get_thread_config()
    
    try:
        # Stream the response - the agent already has the checkpointer attached
        events = agent.stream(messages_state, config, stream_mode="values")
        
        # Process each event in the stream
        for event in events:
            if "messages" in event:
                latest_message = event["messages"][-1]
                latest_message.pretty_print()
        
        # Get the final state
        snapshot = agent.get_state(config)
        if snapshot:
            print("\nConversation state:", snapshot)
            
    except Exception as e:
        print(f"Error in stream processing: {str(e)}")
    
    return
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_interaction(session_id, query, response):
    logging.info({
        "session_id": session_id,
        "query": query,
        "response": response
    })

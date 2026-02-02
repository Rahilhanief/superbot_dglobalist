from dotenv import load_dotenv
load_dotenv()

from langfuse.langchain import CallbackHandler

langfuse_handler = CallbackHandler()

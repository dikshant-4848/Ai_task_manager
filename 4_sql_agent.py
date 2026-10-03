from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
import streamlit as st


DB=SQLDatabase.from_uri("sqlite:///my_tasktask.db")
DB.run("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT CHECK (status IN('pending','in_progress','completed')) DEFAULT  'pending',
        created_at TIMESTAMP default CURRENT_TIMESTAMP
    );
""")
## LLM ,AGENT,SYSTEM_PROMPT,MEMORY
model=ChatGroq(model="openai/gpt-oss-20b")
toolkit=SQLDatabaseToolkit(db=DB,llm=model)
tools=toolkit.get_tools()
# memory=InMemorySaver()


system_prompt="""
You are a task management assistant that interacts with sql database containing a 'tasks' table.

TASK RULE:
1. Limit SELECT queries to 10 result max with ORDER BY created_at DESC
2. After CREATE/UPDATE/DELETE with SELECT query
3. If the user requests a list of tasks, present the output in a structure table formate to ensure a clean and organized display in the browser.

CRUD OPERATIONS:
 CREATE: INSERT INTO tasks(title,description,status)
 READ:   SELECT * FROM tasks WHERE .... LIMIT 10
 UPDATE: UPDATE tasks SET status=? where id=? OR title=?
 DELETE: DELETE FROM task WHERE id=?, title=? OR status=?

Table schema: id,title,description,status(pending/progress/completed), created_at.

"""
@st.cache_resource
def get_agent():
    agent=create_agent(
        model=model,
        tools=tools,
        checkpointer=InMemorySaver(),
        system_prompt=system_prompt,
    )
    return agent
agent=get_agent()

st.subheader("TaskBot Manager")
if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

prompt=st.chat_input("Ask about your task!!")
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("AI"):
        with st.spinner("Processing..."):
            response=agent.invoke(
                {"messages":[{"role":"user","content":prompt}]},
                {"configurable":{"thread_id":"1"}}
            )
    result=response['messages'][-1].content
    st.markdown(result)
    st.session_state.messages.append({"role":"AI","content":result})


# print("Database TABLE tasks created")
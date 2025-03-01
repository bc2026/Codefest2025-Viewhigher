from openai import OpenAI

api_key = ""

client = OpenAI(api_key=api_key)


file  =  client.files.create(
    file=open("./*.pdf", 'rb'),
    purpose="assistants"
)

industry = ""
alumni = ""
user_school = ""


assistant = client.beta.assistants.create(
    name = "Job Application Agent",
    instructions = f"You will help me improve my job applicaiton to {industry} through {alumni} at {user_school}.",
    tools = [{"type":"file_search"}],
    model = "gpt-4o",
    file_ids = [file.id]
)

thread = client.beta.threads.create()
prompt = ""

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role=f"Job Seeker in {industry} at {user_school}",
  content=prompt
)
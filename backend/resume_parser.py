from openai import OpenAI

api_key = ""

client = OpenAI(api_key=api_key)


file  =  client.files.create(
    file=open("./*.pdf", 'rb'),
    purpose="assistants"

)


company = ""

assistant = client.beta.assistants.create(
    name = "Job Application Agent",
    instructions = "You will help me improve my job applicaiton to {company}",
    tools = [{"type":"file_search"}],
    model = "gpt-4o",
    file_ids = [file.id]
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="job seeker",
  content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)
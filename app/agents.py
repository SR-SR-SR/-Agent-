from app.llm import llm_call


class BaseAgent:
    def __init__(self, name, system_prompt):
        self.name = name
        self.system_prompt = system_prompt

    def run(self, task):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": task}
        ]
        return llm_call(messages)


class ManagerAgent(BaseAgent):
    def run(self, task):
        messages = [
            {"role": "system", "content": "你是任务拆解专家"},
            {"role": "user", "content": f"""
任务：
{task}

请拆解为 JSON：
[
  {{\"agent\": \"Research\", \"task\": \"...\"}},
  {{\"agent\": \"Content\", \"task\": \"...\"}},
  {{\"agent\": \"Review\", \"task\": \"...\"}}
]
"""}
        ]
        return llm_call(messages)


class ResearchAgent(BaseAgent):
    pass


class ContentAgent(BaseAgent):
    pass


class ReviewAgent(BaseAgent):
    pass

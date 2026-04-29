import json
from app.agents import (
    ManagerAgent,
    ResearchAgent,
    ContentAgent,
    ReviewAgent
)


class Orchestrator:
    def __init__(self):
        self.manager = ManagerAgent("manager", "")

        self.agent_map = {
            "Research": ResearchAgent("research", "你是调研专家"),
            "Content": ContentAgent("content", "你是内容创作者"),
            "Review": ReviewAgent("review", "你是审稿专家"),
        }

    def run(self, user_task):
        plan_text = self.manager.run(user_task)

        try:
            plan = json.loads(plan_text)
        except:
            return {"error": "任务拆解失败", "raw": plan_text}

        results = []

        for step in plan:
            agent_name = step["agent"]
            task = step["task"]

            agent = self.agent_map.get(agent_name)
            if not agent:
                continue

            result = agent.run(task)
            results.append({
                "agent": agent_name,
                "result": result
            })

        return {
            "plan": plan,
            "results": results
        }

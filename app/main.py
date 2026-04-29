from fastapi import FastAPI
from pydantic import BaseModel
from app.orchestrator import Orchestrator

app = FastAPI()
orch = Orchestrator()


class Task(BaseModel):
    content: str


@app.post("/run")
def run_task(task: Task):
    return orch.run(task.content)

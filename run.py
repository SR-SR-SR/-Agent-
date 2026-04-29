from app.orchestrator import Orchestrator

if __name__ == "__main__":
    orch = Orchestrator()

    while True:
        task = input("\n请输入任务: ")
        if task.lower() in ["exit", "quit"]:
            break

        result = orch.run(task)
        print("\n结果：\n", result)

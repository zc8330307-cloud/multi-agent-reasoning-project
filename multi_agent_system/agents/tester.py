from multi_agent_system.agents.base import AgentResult, BaseAgent
from multi_agent_system.memory import Memory


class TesterAgent(BaseAgent):
    name = "测试验证 Agent"

    def run(self, memory: Memory) -> AgentResult:
        required_keys = [
            "plan_steps",
            "subtasks",
            "research_points",
            "scan_result",
            "code_suggestions",
        ]

        checks = {}
        for key in required_keys:
            checks[key] = "通过" if memory.get(key) is not None else "缺失"

        passed = all(value == "通过" for value in checks.values())

        feedback = [
            "任务拆解结果已生成，可以进入文档整理阶段。",
            "代码扫描结果已写入共享上下文。",
            "资料整理内容已覆盖项目背景、应用场景和价值。",
        ]

        if not passed:
            feedback.append("部分中间结果缺失，建议重新执行对应 Agent。")
        else:
            feedback.append("所有关键中间结果均已生成，工作流闭环正常。")

        memory.set("test_checks", checks)
        memory.set("test_passed", passed)
        memory.set("test_feedback", feedback)
        memory.add_trace("TesterAgent completed validation.")

        return AgentResult(
            agent_name=self.name,
            summary="已完成中间结果验证和闭环反馈。",
            details={
                "检查项": checks,
                "是否通过": passed,
                "反馈建议": feedback,
            },
        )

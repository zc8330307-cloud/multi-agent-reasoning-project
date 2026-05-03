from multi_agent_system.agents.base import AgentResult, BaseAgent
from multi_agent_system.memory import Memory


class ReviewerAgent(BaseAgent):
    name = "结果审查 Agent"

    def run(self, memory: Memory) -> AgentResult:
        project_summary = memory.get("project_summary", "")
        test_passed = memory.get("test_passed", False)

        review_items = {
            "是否包含长链推理": "通过" if "需求理解" in project_summary and "反馈修正" in project_summary else "待完善",
            "是否包含多 Agent 协作": "通过" if memory.get("subtasks") else "待完善",
            "是否包含测试验证": "通过" if memory.get("test_checks") else "待完善",
            "是否包含文档输出": "通过" if project_summary else "待完善",
            "工作流是否闭环": "通过" if test_passed else "待完善",
        }

        final_advice = [
            "可以将 runs 文件夹中的 Markdown 日志截图作为 Agent 工作流证明。",
            "可以将 README.md 和 docs/workflow_design.md 一起上传 GitHub。",
            "后续可以接入真实大模型 API，使每个 Agent 具备更强的自然语言处理能力。",
        ]

        memory.set("review_items", review_items)
        memory.set("final_advice", final_advice)
        memory.add_trace("ReviewerAgent completed final review.")

        return AgentResult(
            agent_name=self.name,
            summary="已完成最终质量审查，项目具备上传 GitHub 和展示说明的基础。",
            details={
                "审查结果": review_items,
                "最终建议": final_advice,
            },
        )

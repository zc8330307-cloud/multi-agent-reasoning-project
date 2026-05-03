from multi_agent_system.agents.base import AgentResult, BaseAgent
from multi_agent_system.memory import Memory


class DocumentAgent(BaseAgent):
    name = "文档生成 Agent"

    def run(self, memory: Memory) -> AgentResult:
        plan_steps = memory.get("plan_steps", [])
        research_points = memory.get("research_points", [])
        code_suggestions = memory.get("code_suggestions", [])
        test_feedback = memory.get("test_feedback", [])

        project_summary = f"""
本项目是一个基于长链推理和多 Agent 协作的智能项目辅助系统。系统围绕用户任务目标，将复杂任务拆解为需求理解、资料整理、代码分析、测试验证、文档生成和结果审查等阶段。各 Agent 通过共享上下文协作完成任务，并将中间结果汇总为最终输出。

系统采用闭环工作流，不是一次性生成结果，而是按照“需求理解—任务拆解—分步执行—结果验证—反馈修正—最终输出”的方式推进。这样可以降低复杂任务中的遗漏风险，提高项目文档和代码分析结果的稳定性。
""".strip()

        workflow_doc = [
            "1. 用户输入任务目标",
            "2. 任务规划 Agent 进行需求理解和任务拆解",
            "3. 资料整理 Agent 提炼项目背景和应用价值",
            "4. 代码分析 Agent 扫描项目结构并给出优化建议",
            "5. 测试验证 Agent 检查关键中间结果是否完整",
            "6. 文档生成 Agent 输出项目说明",
            "7. 结果审查 Agent 完成最终质量检查",
        ]

        memory.set("project_summary", project_summary)
        memory.set("workflow_doc", workflow_doc)
        memory.add_trace("DocumentAgent completed final document draft.")

        return AgentResult(
            agent_name=self.name,
            summary="已完成项目说明文档和工作流说明生成。",
            details={
                "项目说明": project_summary,
                "工作流": workflow_doc,
                "长链步骤引用": plan_steps,
                "资料要点引用": research_points,
                "代码建议引用": code_suggestions,
                "测试反馈引用": test_feedback,
            },
        )

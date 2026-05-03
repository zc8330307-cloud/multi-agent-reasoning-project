from multi_agent_system.agents.base import AgentResult, BaseAgent
from multi_agent_system.memory import Memory


class PlannerAgent(BaseAgent):
    name = "任务规划 Agent"

    def run(self, memory: Memory) -> AgentResult:
        task = memory.task

        steps = [
            "理解用户目标与约束条件",
            "拆解任务为可执行子任务",
            "分配对应 Agent 处理不同环节",
            "汇总中间结果并建立上下文",
            "执行测试验证并形成反馈",
            "根据反馈修正输出",
            "生成最终文档与审查意见",
        ]

        subtasks = {
            "需求分析": "判断任务目标、输入材料、输出形式和质量要求",
            "代码分析": "扫描项目结构，检查代码逻辑、命名、复杂度和潜在风险",
            "资料整理": "提炼背景信息、功能说明和项目价值",
            "测试验证": "根据预期目标检查结果是否完整、合理、可运行",
            "文档生成": "整理 README、使用说明、项目总结和工作流说明",
            "结果审查": "检查最终结果的逻辑一致性、格式规范性和表达完整性",
        }

        memory.set("plan_steps", steps)
        memory.set("subtasks", subtasks)
        memory.add_trace("PlannerAgent completed task decomposition.")

        return AgentResult(
            agent_name=self.name,
            summary="已完成任务理解、长链流程设计和多 Agent 分工。",
            details={
                "原始任务": task,
                "长链推理步骤": steps,
                "子任务分配": subtasks,
            },
        )

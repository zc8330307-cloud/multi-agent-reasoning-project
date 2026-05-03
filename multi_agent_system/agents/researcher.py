from multi_agent_system.agents.base import AgentResult, BaseAgent
from multi_agent_system.memory import Memory


class ResearchAgent(BaseAgent):
    name = "资料整理 Agent"

    def run(self, memory: Memory) -> AgentResult:
        task = memory.task

        points = [
            "多 Agent 协作适合处理流程长、步骤多、需要反复验证的任务。",
            "长链推理可以把复杂目标拆解成多个中间步骤，降低一次性输出的遗漏风险。",
            "Token Plan 可以帮助不同阶段合理分配上下文资源，避免信息混乱。",
            "闭环验证可以通过测试和审查减少错误，提高最终输出稳定性。",
        ]

        use_cases = [
            "课程设计：快速生成项目结构、说明文档和测试思路",
            "代码开发：分析模块逻辑、定位报错、提出优化建议",
            "资料整理：提炼重点内容，形成报告或答辩材料",
            "项目复盘：自动生成运行日志、问题清单和改进方案",
        ]

        memory.set("research_points", points)
        memory.set("use_cases", use_cases)
        memory.add_trace("ResearchAgent completed background summary.")

        return AgentResult(
            agent_name=self.name,
            summary="已完成项目背景、应用价值和使用场景整理。",
            details={
                "背景要点": points,
                "应用场景": use_cases,
                "关联任务": task,
            },
        )

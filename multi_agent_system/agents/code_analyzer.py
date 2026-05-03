from pathlib import Path

from multi_agent_system.agents.base import AgentResult, BaseAgent
from multi_agent_system.memory import Memory
from multi_agent_system.tools.project_scanner import scan_project


class CodeAnalyzerAgent(BaseAgent):
    name = "代码分析 Agent"

    def run(self, memory: Memory) -> AgentResult:
        project_path = Path(memory.get("project_path", "."))
        scan_result = scan_project(project_path)

        suggestions = [
            "建议保持 Agent 基类统一接口，方便后续扩展真实 LLM Provider。",
            "建议将工作流编排逻辑与具体 Agent 逻辑分离，提高可维护性。",
            "建议保存每次运行的 Markdown 日志，便于复盘和截图证明。",
            "建议为关键模块补充单元测试，保证项目上传 GitHub 后可验证。",
        ]

        risk_checks = []
        if scan_result["python_files"] == 0:
            risk_checks.append("当前项目未发现 Python 文件，代码分析深度有限。")
        if scan_result["total_files"] > 80:
            risk_checks.append("项目文件数量较多，建议分模块逐步分析。")
        if not risk_checks:
            risk_checks.append("项目结构规模适中，适合作为多 Agent 工作流演示项目。")

        memory.set("scan_result", scan_result)
        memory.set("code_suggestions", suggestions)
        memory.set("risk_checks", risk_checks)
        memory.add_trace("CodeAnalyzerAgent completed project scan and suggestions.")

        return AgentResult(
            agent_name=self.name,
            summary="已完成项目结构扫描、代码风险判断和优化建议生成。",
            details={
                "扫描结果": scan_result,
                "优化建议": suggestions,
                "风险检查": risk_checks,
            },
        )

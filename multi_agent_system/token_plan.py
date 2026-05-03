from dataclasses import dataclass


@dataclass
class TokenPlan:
    total_budget: int
    planner: int
    researcher: int
    code_analyzer: int
    tester: int
    documenter: int
    reviewer: int

    def to_markdown(self) -> str:
        rows = [
            ("任务规划 Agent", self.planner),
            ("资料整理 Agent", self.researcher),
            ("代码分析 Agent", self.code_analyzer),
            ("测试验证 Agent", self.tester),
            ("文档生成 Agent", self.documenter),
            ("结果审查 Agent", self.reviewer),
        ]
        table = ["| Agent | Token Budget |", "|---|---:|"]
        table += [f"| {name} | {budget} |" for name, budget in rows]
        return "\n".join(table)


def build_token_plan(task: str, total_budget: int = 12000) -> TokenPlan:
    """Create a simple token allocation plan based on task complexity."""

    length_factor = min(max(len(task) / 100, 1), 3)

    planner = int(total_budget * 0.18)
    researcher = int(total_budget * 0.14 * length_factor / 2)
    code_analyzer = int(total_budget * 0.22)
    tester = int(total_budget * 0.16)
    documenter = int(total_budget * 0.20)
    reviewer = total_budget - planner - researcher - code_analyzer - tester - documenter

    return TokenPlan(
        total_budget=total_budget,
        planner=planner,
        researcher=researcher,
        code_analyzer=code_analyzer,
        tester=tester,
        documenter=documenter,
        reviewer=reviewer,
    )

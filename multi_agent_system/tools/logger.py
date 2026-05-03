from datetime import datetime
from pathlib import Path

from multi_agent_system.agents.base import AgentResult
from multi_agent_system.memory import Memory
from multi_agent_system.token_plan import TokenPlan


def save_run_log(
    memory: Memory,
    token_plan: TokenPlan,
    results: list[AgentResult],
    output_dir: str = "runs",
) -> Path:
    """Save a readable Markdown workflow log."""

    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = out_dir / f"run_{timestamp}.md"

    content = [
        "# Multi-Agent Workflow Run Log",
        "",
        f"- Run Time: {datetime.now().isoformat(timespec='seconds')}",
        f"- Task: {memory.task}",
        "",
        "## Token Plan",
        "",
        token_plan.to_markdown(),
        "",
        "## Long-Chain Trace",
        "",
    ]

    content.extend([f"{idx}. {msg}" for idx, msg in enumerate(memory.trace, start=1)])
    content.append("")

    for result in results:
        content.append(result.to_markdown())

    path.write_text("\n".join(content), encoding="utf-8")
    return path

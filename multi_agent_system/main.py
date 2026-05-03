import argparse

from multi_agent_system.workflow import MultiAgentWorkflow


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run a multi-agent long-chain reasoning workflow."
    )
    parser.add_argument(
        "--task",
        type=str,
        default="构建一个基于长链推理和多 Agent 协作的智能项目辅助系统",
        help="Task description for the workflow.",
    )
    parser.add_argument(
        "--project-path",
        type=str,
        default=".",
        help="Project directory to scan.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    workflow = MultiAgentWorkflow(project_path=args.project_path)
    result = workflow.run(args.task)

    print("=" * 70)
    print("Multi-Agent Workflow Finished")
    print("=" * 70)
    print(f"Task: {args.task}")
    print(f"Run log saved to: {result.log_path}")
    print()
    print("Token Plan:")
    print(result.token_plan.to_markdown())
    print()
    print("Final Review:")
    review = result.memory.get("review_items", {})
    for key, value in review.items():
        print(f"- {key}: {value}")


if __name__ == "__main__":
    main()

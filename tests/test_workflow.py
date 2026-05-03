from multi_agent_system.workflow import MultiAgentWorkflow


def test_workflow_runs():
    workflow = MultiAgentWorkflow(project_path=".")
    result = workflow.run("测试多 Agent 工作流是否可以正常运行")

    assert result.log_path.exists()
    assert result.memory.get("review_items") is not None
    assert len(result.agent_results) == 6

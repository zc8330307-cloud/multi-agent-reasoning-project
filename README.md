# Multi-Agent Long-Chain Reasoning Assistant

一个可直接上传 GitHub 的 Python 多 Agent 协作项目示例。项目实现了“任务规划 Agent、代码分析 Agent、资料整理 Agent、测试验证 Agent、文档生成 Agent、结果审查 Agent”的协作流程，并生成可保存的运行日志。

## 项目亮点

- 多 Agent 协作：不同 Agent 分工处理规划、分析、验证、文档与审查任务
- 长链任务流程：需求理解 → 任务拆解 → 分配 Agent → 汇总结果 → 测试验证 → 反馈修正 → 最终输出
- Token Plan：根据任务长度估算 Token 预算，并分配给不同 Agent
- 可运行日志：自动生成 `runs/run_xxx.md`，可作为 Agent 工作流截图材料
- 无需联网即可运行：默认使用本地规则引擎模拟 Agent 工作流
- 支持二次扩展：后续可以替换为真实大模型 API

## 项目结构

```text
multi_agent_system/
├── main.py                     # 命令行入口
├── workflow.py                 # 多 Agent 工作流编排
├── memory.py                   # 简单上下文记忆
├── token_plan.py               # Token 预算分配
├── agents/
│   ├── base.py                 # Agent 基类
│   ├── planner.py              # 任务规划 Agent
│   ├── code_analyzer.py        # 代码分析 Agent
│   ├── researcher.py           # 资料整理 Agent
│   ├── tester.py               # 测试验证 Agent
│   ├── documenter.py           # 文档生成 Agent
│   └── reviewer.py             # 结果审查 Agent
└── tools/
    ├── logger.py               # 运行日志生成工具
    └── project_scanner.py      # 项目文件扫描工具
examples/
├── sample_task.md              # 示例任务
docs/
├── workflow_design.md          # 工作流设计说明
tests/
├── test_workflow.py            # 简单测试
```

## 快速运行

```bash
python -m multi_agent_system.main --task "帮我分析一个 Python 项目，生成优化建议和项目说明文档"
```

运行后会在 `runs/` 文件夹生成 Markdown 格式的工作流日志。

## 情侣小游戏示例（骑士救援）

仓库中提供了一个可直接运行的命令行小游戏：程子阳控制骑士闯关，拯救陈晓凡。

```bash
python examples/couple_knight_game.py
```

玩法说明：
- 使用 `W/A/S/D` 控制移动
- `#` 是墙，`^` 是陷阱
- 第 3 关需要先拿到钥匙 `K` 才能救出陈晓凡 `P`

## 示例输出内容

系统会输出并保存以下内容：

1. 任务拆解结果
2. 多 Agent 执行过程
3. Token Plan 分配
4. 代码分析建议
5. 测试验证结果
6. 最终项目文档
7. 结果审查意见

## GitHub 上传建议

```bash
git init
git add .
git commit -m "init multi-agent long-chain reasoning project"
git branch -M main
git remote add origin 你的GitHub仓库地址
git push -u origin main
```

## 可用于申报/截图的说明

本项目实现了一个基于长链推理和多 Agent 协作的智能项目辅助系统。系统通过任务规划 Agent、代码分析 Agent、资料整理 Agent、测试验证 Agent、文档生成 Agent 和结果审查 Agent 协同完成复杂任务，并通过 Token Plan 对各阶段资源进行分配。工作流采用“需求理解—任务拆解—方案制定—分步执行—结果验证—反馈修正—最终输出”的闭环结构，可用于代码开发、文档生成、资料整理和问题排查等场景。

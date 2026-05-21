# GitHub Agent Setup Guide (多智能体系统开源与部署指南)

This guide details how to push this repository to GitHub and configure its specialized blueprints (`agents/sub_agents/`) and audio-visual playbooks (`references/`) as a fully collaborative multi-agent team inside popular Agent platforms (such as Custom GPTs, Coze, Dify, or OpenClaw).

---

## 1. Pushing the Repository to GitHub

To share this industrial-grade AIGC production skill with your friends, initialize git and push the codebase to your GitHub account:

```bash
# 1. Initialize git and add all files
git init
git add .

# 2. Commit the codebase
git commit -m "feat: upgrade to industrial-grade multi-agent system with audio-visual grammar bibles"

# 3. Create a new repository on GitHub and link it
git remote add origin https://github.com/您的用户名/aigc-film-production-master.git
git branch -M main

# 4. Push to main
git push -u origin main
```

---

## 2. Deploying as Custom GPTs (ChatGPT)

You and your friends can host this system as a set of specialized Custom GPTs on OpenAI's platform:

### Method A: The Master Producer GPT (Single Entry-Point)
1. Go to **ChatGPT -> Explore GPTs -> Create**.
2. **Name**: `AIGC Film Master Producer`.
3. **Instructions**: Copy the entire contents of [00_master_producer.md](file:///Users/wangpeng/Documents/Antigraviti/film%20production/agents/sub_agents/00_master_producer.md) as the GPT's instructions.
4. **Knowledge (Files)**: Upload the entire `references/` folder as knowledge, especially [aigc-audio-visual-grammar-bible.md](file:///Users/wangpeng/Documents/Antigraviti/film%20production/references/aigc-audio-visual-grammar-bible.md) and `references/genre-playbooks/`.
5. **Capabilities**: Enable Code Interpreter (allows parsing and updating the workspace files).

### Method B: The 6-Agent Swarm (Advanced GPTs Network)
Create 6 distinct Custom GPTs corresponding to each sub-agent file in `agents/sub_agents/`. Friends can mention them in a single ChatGPT conversation using the `@` symbol:
1. Start with `@AIGC Master Producer "我的剧本点子..."`
2. Hand off to `@AIGC Screenwriter` to lock Save the Cat beats.
3. Hand off to `@AIGC Director` to block focal lengths and the 180° axis.
4. Hand off to `@Asset Continuity Manager` to lock the character anchors.
5. Hand off to `@AIGC Prompt Factory` to bake the Image2 & Seedance 2.0 prompts.
6. Hand off to `@QA Risk Gatekeeper` to run the compliance checklist.

---

## 3. Deploying in Coze (扣子) / Dify

For a fully automated multi-agent workflow, you can build a graphical pipeline in Dify or Coze using the files in this repository:

### 3.1 Dify Setup (Recommended for Automation)
1. Go to **Dify Dashboard -> Studio -> Create New App -> Chatflow** (or Workflow).
2. Create **6 Agent Nodes** connected sequentially:
   - **Node 00 (Master Producer)**: Use `00_master_producer.md` as System Prompt.
   - **Node 01 (Upstream Writer)**: Use `01_upstream_writer.md` as System Prompt. Ingests output from Node 00.
   - **Node 02 (AIGC Director)**: Use `02_aigc_director.md` as System Prompt. Ingests output from Node 01.
   - **Node 03 (Continuity)**: Use `03_asset_continuity_manager.md` as System Prompt. Ingests output from Node 02.
   - **Node 04 (Factory)**: Use `04_prompt_factory.md` as System Prompt. Ingests outputs from Node 02 and Node 03.
   - **Node 05 (QA Gatekeeper)**: Use `05_qa_risk_gatekeeper.md` as System Prompt. Ingests output from Node 04.
3. **Knowledge Base**: Upload the `references/` folder as a shared vector knowledge base linked to all 6 nodes.
4. **Publish**: Publish the workflow. Dify will provide a single API endpoint. Your friends can type a film idea in the chat web app and receive the fully audited prompt file.

### 3.2 Coze Setup (扣子多智能体)
1. Create a **Multi-Agent App** (多智能体应用) in Coze.
2. Add **6 Agent Roles** inside the team. Copy the respective sub-agent markdown blueprint into each Agent's profile settings.
3. Bind the `references/` directory as a shared Text Knowledge Base.
4. Set up automatic transition rules or let the LLM route conversation turns dynamically.

---

## 4. Running locally with OpenClaw (Hermes)

If you are using OpenClaw or custom Python LLM orchestration frameworks, you can parse this repository dynamically:

```python
import os
from pathlib import Path

class AIGCFilmPipeline:
    def __init__(self, repo_path: str):
        self.repo = Path(repo_path)
        self.blueprints = self.load_blueprints()
        self.bible = (self.repo / "references" / "aigc-audio-visual-grammar-bible.md").read_text()

    def load_blueprints(self):
        blueprints = {}
        agents_dir = self.repo / "agents" / "sub_agents"
        for f in agents_dir.glob("*.md"):
            blueprints[f.stem[3:]] = f.read_text()
        return blueprints

    def execute_upstream_writer(self, source_packet: str, genre: str):
        system_prompt = self.blueprints["upstream_writer"] + "\n\n# BIBLE\n" + self.bible
        # Execute LLM call...
```

This makes your repository a highly versatile, open-source standard for anyone building autonomous AIGC video studios!

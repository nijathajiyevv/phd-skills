# phd-skills

Claude skills for PhD work.

## Skills

| Skill | Purpose |
|---|---|
| [`en-lv-thesis-summary`](en-lv-thesis-summary/SKILL.md) | Translate English academic dissertation material into Latvian at submission quality. Business, digital economy and similar studies only. |
| [`academic-article-writing`](academic-article-writing/SKILL.md) | Plan, audit, revise and submit journal and conference articles, tailored to the venue template and the author's own structure, style and citation format. Covers article types, novelty audit, section depth, reporting guidelines, citation styles, reviewer responses and AI disclosure. |
| [`academic-thesis-writing`](academic-thesis-writing/SKILL.md) | Plan, structure, audit and defend master's and PhD theses inside the structure the institution and candidate require (business, engineering, humanities, by publication and others). Covers originality, chapter depth, formatting, GenAI declarations and viva preparation. |

Both academic writing skills follow one rule: the user's or institution's structure decides the form, and the skill applies best practice inside it rather than imposing its own template.

## Install

Each skill is a folder. The folder holds one `SKILL.md` file and, in some cases, extra files. Always use the complete folder.

First, get the files:

```bash
git clone https://github.com/nijathajiyevv/phd-skills.git
```

### Claude Code

1. Make a skills folder: `mkdir -p ~/.claude/skills`
2. Copy the skill folders: `cp -r phd-skills/academic-* phd-skills/en-lv-thesis-summary ~/.claude/skills/`
3. Start Claude Code again.
4. Type `/skills` to make sure the skills show in the list.

To use the skills in one project only, copy the folders to `.claude/skills/` in that project.

### Claude.ai and Claude Desktop

1. Make a ZIP file of one skill folder. The folder must be at the top level of the ZIP.
2. Go to **Settings > Capabilities > Skills**.
3. Click **Upload skill** and select the ZIP file.
4. Set the skill to **On**.
5. Do steps 1 to 4 again for each skill.

### Other AI tools

Use these steps if the tool does not support skills.

1. Open the `SKILL.md` file of the skill you want.
2. Copy the text.
3. Paste the text into the custom instructions, project instructions or rules file of the tool.
4. Add extra files from the skill folder only if the instructions refer to them.

### Check

Ask: `Help me plan a journal article.` The AI tool must use `academic-article-writing`. If it does not, make sure the skill is **On** and start a new chat.

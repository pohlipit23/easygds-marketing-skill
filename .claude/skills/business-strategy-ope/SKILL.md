---
name: business-strategy-ope
description: "One-Page Endgame (OPE) business strategy framework by Wes Bush. Use when users want to: (1) Define business strategy, (2) Identify competitive moats, (3) Plan GTM approach, (4) Set business goals and milestones, (5) Create strategic alignment documents. Triggers: 'business strategy', 'competitive advantage', 'moat', 'go-to-market', 'business model canvas','OPE framework'."
---

# One-Page Endgame (OPE) Strategy Skill

Guide users through the OPE framework to create a complete business strategy canvas.

## Process Overview

**3 Phases:**
1. **Discovery** - Extract Ideal Customer Profile (ICP), problem, solution, channels (one question at a time)
2. **Moat Selection** - Analyze and select 3 competitive moats from 15 options
3. **Endgame Planning** - Define ultimate goal → yearly → quarterly → monthly milestones

**Final Output:** Completed OPE canvas (HTML) + markdown summary

## Formatting Guidelines

**Non-negotiable:**
- **Dates**: Always use DD/MM/YYYY format (e.g., 01/01/2026)
- **Numbers**: Use metric system only (km, kg, Celsius) - never imperial units
- **Currency**: Specify currency symbol (e.g., £1M, €500K, $2.5M)
- **Time format**: 24-hour format preferred (e.g., 14:30, not 2:30 PM)

## Phase 1: Discovery (Fundamentals)

Ask questions **one at a time** to populate these fields:

| Field | Question to Ask |
|-------|-----------------|
| **Obvious Choice** | "What specific market or niche do you want to dominate as THE obvious choice?" |
| **Ideal Customer** | "Describe your ideal customer - who loves your product as it exists today?" |
| **Core Problem** | "What meaningful problem do you solve for them?" |
| **Core Product** | "What is your core product/solution?" |
| **Primary Channels** | "What are your 2-3 primary marketing channels to reach this customer?" |
| **Geography** | "Which geography will you prioritize?" |

**Tips:**
- Offer multiple choice when context allows
- Suggest options based on industry knowledge
- Challenge vague answers - push for specificity
- "Obvious choice" means no-brainer, not just "good option"

## Phase 2: Moat Selection

Present all 15 moats with relevance scoring for user's context. Reference `references/moats.md` for definitions and examples.

**Process:**
1. Present moats in 3 groups (5 each) with brief descriptions
2. For each group, ask: "Which of these resonate most for your business?"
3. After all 3 groups, propose top 3 recommendations with rationale
4. Confirm or adjust based on user feedback

**Key principle:** User MUST select exactly 3 moats. No more, no less.

## Phase 3: Endgame Planning

### Step 1: Define Endgame
Ask: "What's your ultimate endgame? Examples: $1M ARR, 100K users, exit at $X valuation, team of 50 people"

### Step 2: Reverse-Engineer Milestones
For each timeframe, ask what success looks like:
- **1-Year Picture**: "What does progress look like in 12 months?"
- **Quarterly Picture**: "What must be true at end of this quarter?"
- **Monthly Picture**: "What's the focus for this month?"

### Step 3: Execution Requirements
- **Core Values**: "What values guide decision-making?"
- **Core Capabilities**: "What capabilities must you build or strengthen?"
- **Strategic Choices**: "What will you say NO to? What gets deprioritized?"

## Output Generation

After all phases complete, generate the OPE canvas:

1. **Read the HTML template**: `view assets/ope-canvas-template.html`
2. **Create filled canvas**: Replace placeholders with collected data
3. **Save to outputs**: `output/ope-canvas-[company]-[date].html` (in the current project directory)
4. **Create markdown summary**: Key decisions and action items in `output/ope-summary-[company]-[date].md`
5. **Present both files** to user

## Canvas Template Variables

Replace these placeholders in the HTML template:

```
{{COMPANY_NAME}}
{{DESIGNED_BY}}
{{DATE}}
{{OBVIOUS_CHOICE}}
{{IDEAL_CUSTOMER}}
{{CORE_PROBLEM}}
{{CORE_PRODUCT}}
{{PRIMARY_CHANNELS}}
{{GEOGRAPHY}}
{{MOAT_1}}
{{MOAT_2}}
{{MOAT_3}}
{{ENDGAME}}
{{YEAR_PICTURE}}
{{QUARTERLY_PICTURE}}
{{MONTHLY_PICTURE}}
{{CORE_VALUES}}
{{CORE_CAPABILITIES}}
{{STRATEGIC_CHOICES}}
```

## Key Principles

- **One question at a time** - Never overwhelm with multiple questions
- **Multiple choice preferred** - Easier to answer than open-ended
- **Push for specificity** - Vague answers = vague strategy
- **Challenge assumptions** - Play devil's advocate on moat selections
- **Force prioritization** - Exactly 3 moats, not 4 or 5
- **Action-oriented** - End with "What can you do TODAY?"

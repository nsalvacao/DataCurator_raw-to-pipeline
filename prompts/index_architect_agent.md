<role>You are an expert execution roadmap architect and strategic program planner specializing in creating comprehensive delivery plans that integrate multiple work streams, optimize for team velocity, and provide executive-level visibility into complex technical initiatives.</role>

<task>Create a master execution roadmap file (ROADMAP.md) for the analysis/ directory that serves as the definitive delivery plan, integrating all category roadmaps into a cohesive, resource-optimized, dependency-aware program execution strategy.</task>

<context>
This ROADMAP.md file will be the central command center for the entire improvement initiative. It must provide:
1. **Executive Dashboard**: High-level status, timelines, risks, and resource allocation
2. **Cross-Category Coordination**: Dependencies, sequencing, and integration points
3. **Resource Management**: Team allocation, capacity, and bottleneck identification
4. **Progress Tracking**: Milestones, KPIs, and completion metrics
5. **Decision Support**: Priority trade-offs, risk management, and strategic guidance

The analysis/ directory contains multiple curated category roadmaps. Each represents a distinct execution stream with prioritized problems, solutions, and timelines.

Your role: Synthesize these into a master plan that optimizes delivery speed, manages resource constraints, and provides stakeholder visibility.
</context>

<critical_constraints>
- MUST NOT modify or alter content in existing curated category files
- MUST maintain this as a strategic coordination tool, NOT detailed implementation documentation
- MUST provide actionable sequencing that accounts for ALL cross-category dependencies
- MUST surface risks, blockers, and resource conflicts proactively
- MUST enable executive decision-making with clear trade-off analysis
</critical_constraints>

<mandatory_components>

The ROADMAP.md file MUST include ALL of the following sections in this order:

## 1. EXECUTIVE DASHBOARD

**Purpose**: One-page status view for leadership

**Contents**:
- Overall program status (ON_TRACK | AT_RISK | BLOCKED)
- Total problems across all categories
- Completion percentage
- Timeline (start date, current phase, projected completion)
- Resource utilization summary
- Top 5 risks
- Top 5 wins this period
- Budget status (if effort translates to cost)

## 2. PROGRAM OVERVIEW

**Purpose**: Strategic context and objectives

**Contents**:
- Initiative goals (why we're doing this)
- Success criteria (how we measure victory)
- Scope (what's included, what's not)
- Assumptions and constraints
- Key stakeholders and decision-makers
- Communication plan cadence

## 3. CATEGORY PORTFOLIO

**Purpose**: Complete inventory of execution streams

**For each category, provide**:
- Category name with link to detailed roadmap
- Status (NOT_STARTED | IN_PROGRESS | BLOCKED | COMPLETED)
- Problems: Total count and severity breakdown
- Effort: Estimated duration
- Owner: Primary team
- Current phase
- Completion percentage
- RAG status (Red/Amber/Green)
- Brief description (2 sentences)

## 4. MASTER TIMELINE (GANTT VIEW)

**Purpose**: Visual representation of all work streams over time

**Contents**:
- Timeline visualization (ASCII art or table format)
- Category execution periods
- Critical path highlighted
- Phase boundaries marked
- Dependency indicators
- Resource allocation by period
- Milestone markers

## 5. INTEGRATED DEPENDENCY MAP

**Purpose**: Cross-category prerequisite and blocking relationships

**Contents**:
- Visual dependency graph (ASCII art)
- Critical path analysis (longest dependency chain)
- Blocking chains (what blocks what)
- Parallel execution opportunities
- Coordination requirements
- External dependencies (vendor, third-party)

## 6. RESOURCE ALLOCATION PLAN

**Purpose**: Team capacity, utilization, and constraint management

**Contents**:
- Team-by-team breakdown
  - Allocated categories
  - Total effort committed
  - Capacity vs demand
  - Utilization percentage
  - Over/under allocation
- Resource conflicts (same team, multiple categories)
- Hiring/contractor needs
- Skill gap analysis
- Cross-team coordination requirements

## 7. PHASED EXECUTION STRATEGY

**Purpose**: Logical grouping of work into manageable phases

**For each phase**:
- Phase name and objective
- Duration and timeline
- Categories included
- Problems being solved (high-level)
- Entry criteria (what must be done first)
- Exit criteria (definition of phase complete)
- Success metrics
- Resources required
- Dependencies
- Risks

## 8. PRIORITY FRAMEWORK & TRADE-OFFS

**Purpose**: Decision support for conflicting priorities

**Contents**:
- P0 Criticality: All blockers across categories
- Quick Win Portfolio: All high-ROI items
- Strategic Priorities: Long-term foundational work
- Deferred Items: Explicitly postponed work with rationale
- Trade-off analysis: If we prioritize X, we defer Y
- Decision matrix: Effort vs Impact quadrant

## 9. RISK & DEPENDENCY REGISTER

**Purpose**: Proactive identification and mitigation of program risks

**Contents**:
- Consolidated risks from all categories
- Cross-category risks (coordination failures)
- Resource risks (key person dependency, capacity)
- Technical risks (integration, architecture)
- External risks (vendor, third-party)
- Risk scoring: Probability × Impact
- Mitigation strategies
- Risk owners
- Status tracking

## 10. QUICK WIN EXECUTION PLAN

**Purpose**: Fast-track high-value, low-effort items for early momentum

**Contents**:
- All quick wins from all categories
- Sorted by ROI (impact / effort)
- Recommended execution batch
- Team assignments
- Effort total
- Expected outcomes
- Timeline (typically 1-2 sprints)

## 11. CRITICAL PATH ANALYSIS

**Purpose**: Identify longest dependency chain that determines minimum timeline

**Contents**:
- Critical path definition (sequential dependencies)
- Timeline impact (minimum program duration)
- Bottleneck identification (limiting resources)
- Acceleration options (how to compress timeline)
- Risk to critical path (what could extend it)
- Mitigation strategies

## 12. PROGRESS TRACKING & KPIS

**Purpose**: Measurable success criteria and progress monitoring

**Contents**:
- Program-level KPIs with baseline and targets
- Category completion tracking
- Velocity metrics (problems solved per sprint)
- Quality metrics (defect rate, rework percentage)
- Resource efficiency (actual vs estimated effort)
- Timeline adherence (on-time delivery percentage)
- Business impact metrics (user satisfaction, performance)

## 13. COMMUNICATION & GOVERNANCE

**Purpose**: Stakeholder engagement and decision-making process

**Contents**:
- Status reporting cadence (weekly, bi-weekly)
- Stakeholder meeting schedule
- Escalation process
- Decision-making authority
- Change management process
- Documentation requirements
- Success celebration milestones

## 14. RECOMMENDED EXECUTION SEQUENCES

**Purpose**: Multiple execution path options based on different constraints

**Provide at least 3 paths**:

**Path 1: Fastest Delivery** (Minimize time)
- Maximize parallelization
- Resource assumptions (optimal staffing)
- Timeline: [X weeks]
- Tradeoffs: High coordination overhead, resource intensive

**Path 2: Resource-Constrained** (Limited team size)
- Sequential execution where necessary
- Realistic staffing levels
- Timeline: [Y weeks, longer than Path 1]
- Tradeoffs: Slower but sustainable

**Path 3: Risk-Minimized** (Safest approach)
- Conservative sequencing
- Extra validation phases
- Timeline: [Z weeks, longest]
- Tradeoffs: Slowest but most reliable

**Path 4: Quick Wins First** (Early momentum)
- Front-load high-ROI items
- Build team confidence
- Timeline: Phased with early deliverables
- Tradeoffs: May not address blockers first

## 15. COORDINATION REQUIREMENTS

**Purpose**: Identify necessary cross-team interactions

**Contents**:
- Categories requiring joint effort
- Integration points (where work streams merge)
- Shared deliverables
- Review/approval requirements
- Communication channels
- Conflict resolution process

</mandatory_components>

<formatting_specifications>
- Use Markdown syntax throughout
- Apply consistent heading hierarchy (# for title, ## for major sections, ### for subsections)
- Use tables extensively for structured data (category portfolios, resource allocation, KPIs)
- Use bullet points (-) for lists
- Use numbered lists (1., 2., 3.) for sequential execution steps
- Apply **bold** for critical items (blockers, risks, high-priority)
- Use color indicators: 🔴 (blocked/critical), 🟡 (at risk), 🟢 (on track), ⚪ (not started), ✅ (complete)
- Include horizontal rules (---) between major sections
- Use code blocks for ASCII diagrams (```text ... ```)
- Proper spacing: blank line before/after headings and between sections
- Use relative links to category roadmaps: [Category Name](./analysis/curated/category.md)
</formatting_specifications>

<style_guidelines>
- Write for executive audience (concise, strategic, decision-oriented)
- Use present tense for status, future tense for plans
- Quantify everything (numbers, percentages, dates)
- Highlight risks and blockers prominently
- Provide actionable recommendations, not just observations
- Use consistent terminology across sections
- Avoid technical jargon in executive sections (save for detailed sections)
- Include visual elements (tables, diagrams) for scannability
</style_guidelines>

<quality_validation>

Before finalizing, verify:

✓ **Completeness**:
  - All categories from curated roadmaps included
  - All 15 mandatory sections present
  - All cross-category dependencies documented

✓ **Accuracy**:
  - Timeline math is correct (effort sums match)
  - Resource allocation adds up (no double-counting)
  - Dependency chains are valid (no circular dependencies)
  - KPIs have baseline and target values

✓ **Actionability**:
  - Each phase has clear entry/exit criteria
  - Execution paths are specific (not vague guidance)
  - Resource conflicts are identified with resolution options
  - Decisions needed are explicitly called out

✓ **Executive Readiness**:
  - Executive dashboard fits on one screen
  - Risks are prioritized (not just listed)
  - Trade-offs are clearly articulated
  - Recommendations are specific and justified

✓ **Coordination Support**:
  - Cross-category dependencies explicit
  - Integration points identified
  - Team coordination requirements documented
  - Conflict resolution process defined

✓ **Progress Tracking**:
  - Milestones are measurable
  - KPIs are quantified
  - Status template is practical
  - Success criteria are clear

</quality_validation>

<success_criteria>

The roadmap succeeds when:

1. **Executive can make decisions** using dashboard and trade-off analysis
2. **PM/TL can coordinate work** using phased execution strategy and timeline
3. **Teams know dependencies** from integrated dependency map
4. **Resource managers can staff** from allocation plan
5. **Everyone understands progress** from KPIs and milestones
6. **Risks are managed** proactively via register
7. **Quick wins are visible** and scheduled for early delivery
8. **Critical path is understood** and actively managed

**The document answers these strategic questions:**
- What's the overall status? (Dashboard)
- When will we be done? (Timeline + Critical Path)
- Are we on track? (KPIs + Progress Tracking)
- What are the biggest risks? (Risk Register)
- Where are we stuck? (Blockers + Dependencies)
- How should we sequence work? (Execution Paths)
- Where should we focus? (Priority Framework)
- Who's working on what? (Resource Allocation)
- What decisions do we need to make? (Trade-offs)

</success_criteria>

<execution_instructions>

**Workflow for creating ROADMAP.md**:

1. **Data Collection** (15%)
	- Read all curated category roadmaps
	- Extract key data: effort, timeline, dependencies, resources, risks
	- Build master problem inventory across all categories

2. **Dependency Analysis** (20%)
	- Map all cross-category dependencies
	- Identify critical path (longest dependency chain)
	- Find parallelization opportunities
	- Note coordination requirements

3. **Resource Planning** (15%)
	- Calculate total effort per team
	- Compare against capacity
	- Identify over/under allocation
	- Flag resource conflicts (same team, overlapping timeline)

4. **Phasing Strategy** (15%)
	- Group categories into logical phases
	- Define phase objectives and exit criteria
	- Sequence phases based on dependencies
	- Estimate phase durations

5. **Timeline Construction** (10%)
	- Create master timeline (Gantt-style)
	- Show category execution periods
	- Highlight critical path
	- Mark milestones

6. **Risk Consolidation** (10%)
	- Aggregate risks from all categories
	- Add cross-category coordination risks
	- Add program-level risks
	- Prioritize by probability × impact
	- Define mitigation strategies

7. **Quick Win Extraction** (5%)
	- Collect all quick wins across categories
	- Rank by ROI
	- Create dedicated execution plan
	- Schedule for early delivery

8. **Execution Path Design** (10%)
	- Design 3-4 execution path options
	- Optimize for different constraints (time, resources, risk)
	- Document tradeoffs for each
	- Recommend preferred path

9. **Documentation Assembly** (10%)
	- Create all 15 mandatory sections
	- Apply formatting and styling
	- Add visual elements (tables, diagrams)
	- Validate completeness and accuracy

</execution_instructions>

<output_format_example>

```markdown
# Program Execution Roadmap

**Last Updated**: [Date]  
**Program Status**: 🟢 ON TRACK  
**Completion**: 34% (45 of 132 problems resolved)  
**Timeline**: Week 12 of 35 (on schedule)

---

## Executive Dashboard

| Metric | Value | Status | Notes |
|--------|-------|--------|-------|
| **Overall Status** | 🟢 ON TRACK | Green | All phases proceeding as planned |
| **Total Problems** | 132 | - | Across 11 categories |
| **Completed** | 45 (34%) | 🟢 | Above target (30% at Week 12) |
| **In Progress** | 28 (21%) | 🟢 | Aligned with plan |
| **Blocked** | 3 (2%) | 🟡 | Escalated (see Risks) |
| **Timeline** | Week 12 of 35 | 🟢 | On schedule for Q3 completion |
| **Budget** | 85% allocated | 🟢 | $425K of $500K committed |
| **Resource Utilization** | 92% | 🟢 | Optimal (80-100% target) |

**Top 5 Risks**:
1. 🔴 CAT-004 blocked by external dependency (API vendor delay)
2. 🟡 Backend team at 110% capacity (Phase 3 may slip)
3. 🟡 Database migration complexity higher than estimated
4. 🟢 Key engineer on PTO Week 15 (coverage arranged)
5. 🟢 Integration testing requires 2 extra days (buffer available)

**Top 5 Wins This Period**:
1. ✅ Authentication refactor complete (2 days early)
2. ✅ Quick Win Sprint delivered 12 high-impact fixes
3. ✅ Database indexing improved p95 latency by 70%
4. ✅ 15 critical production bugs resolved
5. ✅ Test coverage increased from 42% to 78%

---

## Program Overview

### Initiative Goals

This program addresses [X] problems across [Y] categories to achieve:

**Primary Objectives**:
1. **Eliminate Blockers**: Resolve all CRITICAL issues blocking development
2. **Improve Performance**: Reduce API latency to <500ms (current: 3.2s)
3. **Reduce Tech Debt**: Increase test coverage to 80%+ (current: 42%)
4. **Enable Features**: Unblock 15 features waiting on infrastructure

**Success Criteria**:
- Zero P0/P1 production issues for 30 days
- All KPIs meet targets (see section 12)
- 90%+ stakeholder satisfaction score
- Timeline variance <10% (within 3-4 weeks of plan)

[Continue with all sections...]
```

</output_format_example>

<completion_protocol>

When roadmap is complete, end with:

---

## Document Control

**Version**: 1.0  
**Created**: [Date]  
**Author**: [Agent name]  
**Status**: READY FOR REVIEW  

**Distribution**:
- Executive Leadership (for approval)
- Engineering Managers (for resource planning)
- Product Management (for prioritization input)
- Program Management (for tracking)

**Review Cycle**:
- Weekly updates every [Day]
- Monthly review with leadership
- Ad-hoc updates for significant changes

**Change Log**:
| Date | Version | Changes | Author |
|------|---------|---------|--------|
| [Date] | 1.0 | Initial roadmap | [Name] |

---

**Next Actions**:
1. [ ] Leadership review and approval (by [date])
2. [ ] Resource commitment confirmation (by [date])
3. [ ] Kick-off meeting scheduled (date: [X])
4. [ ] Category leads assigned
5. [ ] Weekly status reporting initiated

---

**ROADMAP COMPLETE - READY FOR PROGRAM EXECUTION**

</completion_protocol>

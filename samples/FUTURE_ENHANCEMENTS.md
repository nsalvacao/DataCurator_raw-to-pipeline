# Future Enhancements - Nexo Spec Kit (Phase 0 + Spec-Driven Development)

**Document Purpose**: Track enhancements identified during ideation but deferred for post-PoC.  
**Audience**: Maintainers and contributors to the fork.  
**Scope**: Enhancements that remain compatible with upstream, unless explicitly noted.  

---

## How to Use This Document

- Treat each enhancement as an independent track with its own scope, effort, and acceptance criteria.
- Keep items optional or profile-based unless explicitly designated as a core change.
- Before implementing, validate dependencies and confirm impact on upstream compatibility.
- Update this file when an item is shipped, split, or superseded.

**Status Legend** (default for all items): `Planned` unless otherwise noted.

---

## Category A — Core Workflow & State

### Enhancement #1: Full Stateful Mode

**Priority**: P2 (after PoC validation)  
**Estimated Effort**: +3-4 days  
**Origin**: Ideation Session Q7 (2026-01-12)  
**Status**: Planned  
**Dependencies**: None (internal)  
**Risks**: State migration compatibility, UX drift  

#### Current State (PoC - Lightweight)
- Minimal state.yaml (~15 lines)
- Dependency validation only
- No auxiliary commands
- No timestamps/history

#### Proposed Enhancement (Full Stateful)

##### Rich State Schema
```yaml
# .spec-kit/state.yaml (Full version)
workflow_version: "1.0"
session_id: "20260112-141300"
started_at: "2026-01-12T14:13:00Z"
current_phase: structure
profile: ai-system

phases:
  ideate:
    status: completed
    started_at: "2026-01-12T14:15:00Z"
    completed_at: "2026-01-12T14:45:00Z"
    duration_min: 30
    framework: "SCAMPER + HMW (full)"
    artifacts:
      - .spec-kit/ideas_backlog.md
    stats:
      seed_ideas: 3
      generated_ideas: 10
      total_ideas: 13
  
  select:
    status: completed
    started_at: "2026-01-12T14:46:00Z"
    completed_at: "2026-01-12T15:26:00Z"
    duration_min: 40
    framework: "AI-RICE (6 dimensions)"
    artifacts:
      - .spec-kit/idea_selection.md
    stats:
      ideas_scored: 13
      winner: "RAG Knowledge Base (score 127.5)"
  
  structure:
    status: in_progress
    started_at: "2026-01-12T15:30:00Z"
    framework: "Integrated Canvas (JTBD+Lean+AI)"
    progress_pct: 60
  
  validate:
    status: pending

gates:
  G0:
    status: pending
    criteria_count: 20

decisions_log:
  - timestamp: "2026-01-12T14:13:37Z"
    question: "Q1: Timeline dogfooding"
    answer: "B+ (1-3 weeks, multiple ideas)"
  - timestamp: "2026-01-12T14:22:11Z"
    question: "Q6: Gate G0 rigor"
    answer: "C (Rigorous, 20 criteria, waivers)"
```

##### Auxiliary Commands

**1. `/speckit.status` - Progress Dashboard**
```
╔═══════════════════════════════════════════════════════════╗
║  AI System Ideation Workflow - Status                    ║
╚═══════════════════════════════════════════════════════════╝

Session: 20260112-141300
Started: 2026-01-12 14:13:00 (1h 17min ago)
Profile: ai-system

Progress: ████████████░░░░░░░░ 50% (2/4 phases)

✅ IDEATE   [Completed] 30 min
   Framework: SCAMPER + HMW (full)
   Output: 13 ideas generated

✅ SELECT   [Completed] 40 min
   Framework: AI-RICE (6D scoring)
   Winner: RAG Knowledge Base (score 127.5)

⏳ STRUCTURE [In Progress] 60% complete
   Framework: Integrated Canvas (JTBD+Lean+AI)
   Started: 15:30 (10 min ago)

⏸️  VALIDATE [Pending]
   Gate G0: 20 criteria (rigorous)

Next Action: Complete STRUCTURE phase
Command: /speckit.structure --resume
```

**2. `/speckit.resume` - Continue Workflow**
- Detects current_phase from state.yaml
- Continues from last checkpoint
- Loads context from previous phases

**3. `/speckit.reset` - Clear State**
```
Warning: This will clear all progress and delete artifacts.
Phases completed: IDEATE, SELECT (2/4)
Are you sure? Type 'reset workflow' to confirm:
```

**4. `/speckit.history` - Decisions Log**
```
╔═══════════════════════════════════════════════════════════╗
║  Decisions Log                                            ║
╚═══════════════════════════════════════════════════════════╝

Q1 [14:13:37] Timeline: B+ (1-3 weeks, multiple ideas)
Q2 [14:13:37] Workflow: A (Full 4-phase workflow)
Q3 [13:56:02] IDEATE role: B (Co-creator, SCAMPER+HMW full)
Q4 [14:05:15] SELECT framework: C (AI-RICE 6D)
Q5 [14:13:37] STRUCTURE: B (Integrated Canvas)
Q6 [14:22:11] Gate G0: C (Rigorous, 20 criteria, waivers)

Frameworks Applied:
  • IDEATE: SCAMPER (7 lenses) + HMW questions
  • SELECT: AI-RICE (Reach, Impact, Confidence, Data, Effort, Risk)
  • STRUCTURE: JTBD + Lean Startup + AI Canvas (integrated)
  • VALIDATE: Gate G0 (20 criteria: automated + manual + AI-specific)
```

#### Benefits
- Rich UX (status dashboard, progress tracking)
- Resumability (clear next step, resume command)
- Auditability (timestamps, decisions log, duration tracking)
- History (frameworks applied, decisions visible)
- Stats tracking (ideas count, scores, duration)
- Professional polish (production-ready feel)

#### Implementation Breakdown
- Rich state schema design: 0.5 days
- State read/write/update logic: 1 day
- `/speckit.status` command + formatting: 1 day
- `/speckit.resume` command: 0.5 days
- `/speckit.reset` command: 0.5 days
- `/speckit.history` command: 0.5 days
- Testing + documentation: 0.5 days

**Total**: 4.5 days (rounded to 4-5 days)

#### Acceptance Criteria
- [ ] State.yaml tracks timestamps, duration, stats
- [ ] `/speckit.status` shows formatted progress dashboard
- [ ] `/speckit.resume` continues from current phase
- [ ] `/speckit.reset` clears state with confirmation
- [ ] `/speckit.history` shows decisions log + frameworks
- [ ] Backwards compatible (lightweight state upgrades gracefully)

---

### Enhancement #2: Multi-Idea Parallel Tracking

**Priority**: P3  
**Effort**: 2-3 days  
**Status**: Planned  
**Dependencies**: Enhancement #1 (preferred)  
**Risks**: Increased state complexity  

Allow tracking multiple ideas in parallel (not just sequential workflow).
- state.yaml supports multiple sessions
- Switch between ideas: `/speckit.switch --idea=2`

---

## Category B — Visualization & Export

### Enhancement #3: Export to Different Formats

**Priority**: P3  
**Effort**: 1-2 days  
**Status**: Planned  
**Dependencies**: None  
**Risks**: Format drift, maintenance overhead  

Export vision_brief.md to different formats:
- PDF (professional presentation)
- Notion/Confluence (team collaboration)
- Markdown slides (pitch deck)

---

### Enhancement #4: AI-RICE Scoring Visualization

**Priority**: P3  
**Effort**: 1 day  
**Status**: Planned  
**Dependencies**: AI-RICE outputs  
**Risks**: Charting library choice  

Generate visual scoring comparison:
- Radar chart (6 dimensions per idea)
- Ranking table with highlighting
- Export to image/PDF

---

## Category C — Multi-Profile Phase 0

### Enhancement #5: Multi-Profile Phase 0 (Non-AI + AI Variants)

**Priority**: P2  
**Effort**: 5-8 days  
**Goal**: Add Phase 0 profile variants with tailored Gate G0 templates and guidance (Level 2 only).  
**Status**: Planned  
**Dependencies**: None (templates + docs)  
**Risks**: Fragmentation, doc sprawl  

#### Proposed Profiles (Concrete List)

1) **ai-system**  
   - Scope: LLM apps, RAG, agents, MCP servers, fine-tuning  
   - Standards: NIST AI RMF, model eval, safety, data readiness, cost  

2) **web-saas**  
   - Scope: B2B/B2C web products  
   - Standards: GDPR, SOC2/ISO27001, OWASP, SLOs  

3) **mobile-app**  
   - Scope: iOS/Android apps  
   - Standards: App Store/Play compliance, privacy, offline/perf  

4) **desktop-app**  
   - Scope: Windows/macOS/Linux desktop  
   - Standards: update/signing, local storage, security  

5) **api-service**  
   - Scope: APIs, integrations, backend services  
   - Standards: OpenAPI, versioning, auth, rate limits, SLA  

6) **data-platform**  
   - Scope: pipelines, analytics infra, ETL  
   - Standards: data governance, lineage, retention, PII  

7) **devtools-sdk**  
   - Scope: CLI tools, SDKs, dev tooling  
   - Standards: SemVer, DX, backwards compatibility  

8) **infra-platform**  
   - Scope: infra tooling, orchestration, platforms  
   - Standards: SRE/SLO, security hardening, compliance  

9) **self-hosted-web**  
   - Scope: local web apps, Dockerized deployments  
   - Standards: install UX, upgrade paths, secure defaults  

10) **automation-agent**  
    - Scope: workflow bots, automation agents  
    - Standards: audit logging, permissions, rollback  

#### How This Fits the Framework (Level 2)
- Keep the same 4 phases (IDEATE → SELECT → STRUCTURE → VALIDATE)  
- Provide **profile-specific templates** for:
  - Gate G0 report (manual checks)  
  - Vision brief guidance  
- Use **profile checklists** in docs, not code (avoid complex conditional scripts)

#### AI-Specific Extensions (inside ai-system)
- MCP servers, fine-tuning, observability tracked as **ai-system sub-criteria**  
- Add optional criteria for:
  - Data governance + eval harness  
  - Model drift monitoring  
  - Safety/abuse testing  
  - Runtime observability & audit logs  

---

## Category D — Fork Professionalization & Distribution

### Enhancement #6: Fork Professionalization & Distribution Track

**Priority**: P2  
**Effort**: 6-10 days  
**Goal**: Make the fork distribution-ready and contribution-friendly.  
**Status**: Planned  
**Dependencies**: None  
**Risks**: Release workflow complexity  

#### Professionalization Checklist
- README rewrite with:
  - Clear fork value proposition  
  - Differences vs upstream  
  - Compatibility guarantees  
  - Not affiliated with GitHub disclaimer  
- Dedicated docs:
  - `docs/upstream-sync.md` (sync strategy)  
  - `docs/distribution.md` (install paths + `SPECIFY_TEMPLATE_REPO`)  
  - `docs/release.md` (fork release process)  
  - `docs/compatibility.md` (supported upstream versions)  
- Contribution UX:
  - Update CONTRIBUTING.md for fork workflow  
  - Issue + PR templates aligned with fork scope  
- Compliance:
  - License compatibility confirmation  
  - Trademark usage review  
  - SECURITY.md / SUPPORT.md fork ownership clarity  

#### Distribution Strategy
- Publish fork releases with assets  
- Versioning scheme: `0.0.xx-fork.N`  
- Validate `specify init` with override repo  

---

## Category E — Web Presence

### Enhancement #7: GitHub Pages Site

**Priority**: P3  
**Effort**: 3-5 days  
**Goal**: Create a public landing site for fork adoption.  
**Status**: Planned  
**Dependencies**: None  
**Risks**: Content duplication if docs not unified  

#### Options / Frameworks
- MkDocs Material (fast, docs-first)  
- Docusaurus (feature-rich docs site)  
- Astro/Starlight (marketing + docs)  

#### Recommended Site Structure
- Landing page (value proposition + diffs vs upstream)  
- Install / Quickstart  
- Phase 0 ideation workflow  
- Fork compatibility + sync guide  
- Releases + changelog  
- Governance / compliance (license, security)  

#### Deployment
- GitHub Pages workflow (main → gh-pages)  
- README badge linking to site  

---

## Category F — Standards & Quality Packs

### Enhancement #9: Standards-Backed Spec Extensions (Quality Packs)

**Priority**: P3  
**Effort**: 4-6 days  
**Goal**: Add optional standards-based templates/checklists that can be attached to specs when needed.  
**Status**: Planned  
**Dependencies**: None  
**Risks**: Template bloat if all packs are enabled by default  

#### Proposed Add-ons (standards)
1) **EARS requirements syntax**  
   - Lightweight template for precise requirement sentences  
   - Link: https://alistairmavin.com/ears/

2) **Gherkin acceptance criteria**  
   - BDD-style scenarios for executable specs  
   - Link: https://cucumber.io/docs/gherkin/reference

3) **API contract templates (sync + async)**  
   - OpenAPI + AsyncAPI spec skeletons  
   - Links: https://spec.openapis.org/oas/latest.html, https://www.asyncapi.com/docs/reference/specification/latest

4) **STRIDE threat modeling checklist**  
   - Security threat categories for early review  
   - Link: https://learn.microsoft.com/en-us/windows-hardware/drivers/driversecurity/threat-modeling-for-drivers

5) **LINDDUN privacy threat modeling**  
   - Privacy threat categories for early review  
   - Link: https://www.nist.gov/privacy-framework/linddun-privacy-threat-modeling-framework

6) **SRE error-budget policy template**  
   - Reliability guardrails for post-spec delivery  
   - Link: https://sre.google/workbook/error-budget-policy/

7) **Accessibility compliance checklist**  
   - WCAG 2.2 criteria summary  
   - Link: https://www.w3.org/TR/WCAG22/

8) **Supply-chain security pack**  
   - SPDX SBOM + SLSA provenance guidance  
   - Links: https://spdx.dev/specifications/, https://slsa.dev/

9) **Architecture diagramming (C4 model)**  
   - Consistent, readable architecture views  
   - Link: https://c4model.com/

10) **DPIA starter kit (GDPR Art. 35)**  
    - Privacy impact assessment template  
    - Link: https://eur-lex.europa.eu/eli/reg/2016/679/oj

---

## Category G — Post-Spec Integrations & Automations

### Enhancement #10: Post-Spec Kit Integrations & Automations

**Priority**: P3  
**Effort**: 6-12 days  
**Goal**: Provide downstream integrations and automations after the spec is produced.  
**Status**: Planned  
**Dependencies**: None  
**Risks**: External API churn, credential handling  

#### Proposed Integrations (post-spec)

**Planning & Delivery**
1) **Spec → Issues (GitHub Issues API)**  
   - Auto-create backlog items from specs  
   - Link: https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28

2) **Spec → Roadmap/Projects (GitHub Projects)**  
   - Populate project boards and roadmaps  
   - Link: https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects

3) **Spec → CI workflows (GitHub Actions)**  
   - Generate baseline pipelines  
   - Link: https://docs.github.com/en/actions/using-workflows

4) **Spec → Release automation (release-please)**  
   - Conventional commits to release PRs  
   - Link: https://github.com/googleapis/release-please

**Infrastructure & Delivery**
5) **Spec → GitOps CD (Argo CD)**  
   - Deployment automation from declared state  
   - Link: https://argo-cd.readthedocs.io/en/stable/

6) **Spec → IaC scaffolding (Terraform)**  
   - Infra baseline from spec outputs  
   - Link: https://developer.hashicorp.com/terraform/intro

7) **Spec → Container registry release (GHCR)**  
   - Publish images + artifacts  
   - Link: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry

**Operations & Reliability**
8) **Spec → Observability baseline (OpenTelemetry)**  
   - Standardized telemetry plan  
   - Link: https://opentelemetry.io/docs/

9) **Spec → Incident management (PagerDuty)**  
   - On-call and incident routing  
   - Link: https://support.pagerduty.com/main/lang-ja/docs/api-access-keys

10) **Spec → Secrets management (Vault)**  
    - Policy + secret placeholders  
    - Link: https://developer.hashicorp.com/vault/docs

11) **Spec → Feature flags (LaunchDarkly)**  
    - Flag registry + rollout plan  
    - Link: https://launchdarkly.com/docs/api/feature-flags

**Knowledge & Collaboration**
12) **Spec → Service catalog entry (Backstage)**  
    - `catalog-info.yaml` + ownership  
    - Link: https://backstage.io/docs/features/software-catalog/descriptor-format

13) **Spec → Knowledge base publishing (Confluence)**  
    - Publish docs to team workspace  
    - Link: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/

14) **Spec → ChatOps notifications (Slack)**  
    - Spec status and release alerts  
    - Link: https://api.slack.com/apis

**Security & Maintenance**
15) **Spec → Dependency updates (Dependabot)**  
    - Automated update PRs  
    - Link: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates

---

## Category H — External Fork Intelligence (Backlog)

### Enhancement #8: Fork Intelligence Scan (External Fork Insights)

**Priority**: P3  
**Effort**: 4-7 days  
**Goal**: Extract best ideas from external forks and integrate as optional extensions.  
**Status**: Planned  
**Dependencies**: None  
**Risks**: Divergence from upstream scope  

#### Sources Scanned (public forks)
- spec-kit-plus (panaversity): multi-agent stacks + MCP/Dapr/Ray focus
- spec-kit-improved (SpecifyX): Jinja2 templating + TOML config + CLI UX
- spec-kit-roo: agent-specific onboarding (Roo Code)
- research-kit: research-first workflow with citations and rigor
- pmf-kit: product/market validation workflow
- agentic-sdlc-spec-kit: governance/12-factors + knowledge packets
- GitYCC/spec-kit: localization (zh-TW)

#### Proposed Improvements (Backlog)
1) **Advanced templating + config**  
   - Jinja2 templates with variables/loops  
   - `specify.toml` for defaults (agents, template repo, paths, profiles)

2) **Multi-agent production profile**  
   - Optional profile for MCP/Dapr/Ray/K8s stacks  
   - Dedicated checks and guidance for agentic systems

3) **Research gate (pre-Phase 0)**  
   - Lightweight research workflow with citations and evidence logging  
   - Structured inputs to Gate G0

4) **PMF validation kit**  
   - Hypothesis → evidence → decision loop  
   - Optional templates and artifacts

5) **Governance + knowledge packets**  
   - “Org directives” layer (team standards)  
   - Knowledge packets / level-up summaries per phase

6) **Agent-specific onboarding guides**  
   - Dedicated guides for Codex, Claude, Copilot, Roo, etc.  
   - Common pitfalls + best practices

7) **Localization pack**  
   - Multi-language docs/templates (PT-PT, EN, zh-TW)

#### Notes
- All items should remain optional or profile-based to avoid breaking upstream compatibility.  
- Track prerequisites and dependency graph in a follow-up roadmap before implementation.

---

## Category I — Implementation Gap Closure

### Enhancement #11: Phase 0 Scripted Automation & Runtime Setup Parity

**Priority**: P2  
**Effort**: 3-6 days  
**Goal**: Close gaps between the original blueprint and the current prompt-driven implementation.  
**Status**: Planned  
**Dependencies**: None  
**Risks**: Cross-platform parity (bash/PowerShell), CLI UX consistency  

#### Missing Items to Implement
1) **Phase 0 command scripts (bash)**  
   - `scripts/bash/ideate.sh` (create `.spec-kit/ideas_backlog.md`)  
   - `scripts/bash/select.sh` (interactive AI‑RICE scoring + ranking)  
   - `scripts/bash/structure.sh` (canvas creation + brief generation)  

2) **Phase 0 command scripts (PowerShell)**  
   - `scripts/powershell/ideate.ps1`  
   - `scripts/powershell/select.ps1`  
   - `scripts/powershell/structure.ps1`  

3) **Canvas → Brief transform logic**  
   - Structured extraction/formatting from `ai_vision_canvas.md` into `vision_brief.md`  

4) **AI‑RICE scoring automation**  
   - Compute score, sort, pick top idea  
   - Capture runner‑ups + rationale stubs  

5) **Runtime directory auto‑setup**  
   - Create `.spec-kit/approvals/` automatically  
   - Add `.spec-kit/.gitignore` template (artifacts ignored by default)  

6) **Edge‑case tests**  
   - IDEATE with 1 seed and 10+ seeds  
   - State skip/re‑run protection scenarios  

---

### Enhancement #12: Dogfooding + Final Review Gate

**Priority**: P2  
**Effort**: 2-4 days  
**Goal**: Validate real‑world usability and close feedback loop before release.  
**Status**: Planned  
**Dependencies**: Enhancement #11 (preferred), but can run partially  
**Risks**: Scope creep if feedback is not triaged  

#### Proposed Activities
1) Run full workflow on a real AI system idea  
2) Collect friction points and confusion spots  
3) Iterate on templates/scripts based on feedback  
4) Perform test coverage review and gap analysis  
5) Decide whether to prepare an upstream PR (optional)

---

## Category J — Lifecycle Expansion (Post‑Spec)

### Enhancement #13: Phases 6–8 (Verification → Release → Operation)

**Priority**: P3  
**Effort**: 4-6 weeks  
**Goal**: Extend the workflow beyond spec delivery into verification, release, and operations.  
**Status**: Planned  
**Dependencies**: Stable Phase 0 + Spec core  
**Risks**: Increased surface area, heavier maintenance  

#### Phase 6: Verification (QA/NFR/Security)
- QA and NFR checklists
- Security gates (OWASP/Threat modeling pack)
- Test strategy + coverage mapping

#### Phase 7: Release
- Packaging checklist
- Deployment plan + rollback
- SBOM + provenance (SLSA/SPDX)

#### Phase 8: Operation
- Observability plan (metrics/logs/traces)
- Runbooks + incident playbooks
- Iteration loop + post‑mortems

---

**Document Maintained By**: Ideation session outcomes  
**Last Updated**: 2026-01-14

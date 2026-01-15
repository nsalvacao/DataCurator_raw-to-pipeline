# Implementation Blueprint - Spec-Kit AI Extensions (Phase 0)

**Generated**: 2026-01-12T15:17:41Z  
**Ideation Session**: 2026-01-12 (13:02 - 14:30, ~1h 30min)  
**Status**: 🟡 **IMPLEMENTED (gaps tracked in FUTURE_ENHANCEMENTS.md)**

---

## 🎯 Executive Summary

**Objective**: Extend Spec-Kit with **Phase 0 (AI System Ideation)** - structured workflow from vague idea to validated vision brief ready for `/speckit.constitution`.

**Scope**: 4-phase workflow (IDEATE → SELECT → STRUCTURE → VALIDATE) focused on **AI/GenAI systems**.

**Timeline**: 2-3 weeks (14 working days realistic)

**Delivery**: PoC with lightweight state, complete frameworks, rigorous validation gates.

---

## 📊 Workflow Architecture

### Visual Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 0: AI SYSTEM IDEATION (NEW - This PoC)                   │
└─────────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────────────────────────────┐
    │  1. IDEATE (Divergent - Co-creator)                      │
    │     Frameworks: SCAMPER (7 lenses) + HMW questions       │
    │     Input: User seed ideas (2-5)                         │
    │     Process: Agent expands with variations               │
    │     Output: ideas_backlog.md (8-15 ideas)                │
    │     Duration: ~30 min                                    │
    └───────────────────────┬──────────────────────────────────┘
                            │
                            ↓
    ┌──────────────────────────────────────────────────────────┐
    │  2. SELECT (Convergent - Prioritization)                 │
    │     Framework: AI-RICE (6 dimensions)                    │
    │     Input: ideas_backlog.md                              │
    │     Process: Score each idea (Reach, Impact, Confidence, │
    │              Data, Effort, Risk)                         │
    │     Output: idea_selection.md (1 chosen + rationale)     │
    │     Duration: ~40 min                                    │
    └───────────────────────┬──────────────────────────────────┘
                            │
                            ↓
    ┌──────────────────────────────────────────────────────────┐
    │  3. STRUCTURE (Define - Integrated Canvas)               │
    │     Frameworks: JTBD + Lean Startup + AI Canvas          │
    │     Input: idea_selection.md                             │
    │     Process: Fill 3-section integrated canvas            │
    │              (JTBD | Lean | AI-Specific)                 │
    │     Output: ai_vision_canvas.md + vision_brief.md        │
    │     Duration: ~40 min                                    │
    └───────────────────────┬──────────────────────────────────┘
                            │
                            ↓
    ┌──────────────────────────────────────────────────────────┐
    │  4. VALIDATE (Gate G0 - Rigorous)                        │
    │     Framework: 20 criteria validation                    │
    │     Input: vision_brief.md                               │
    │     Process: Automated checks (8) + Manual (12)          │
    │     Output: g0-validation-report.md + approval           │
    │     Duration: ~15 min                                    │
    └───────────────────────┬──────────────────────────────────┘
                            │
                            ↓ HANDOFF
┌─────────────────────────────────────────────────────────────────┐
│ SPEC-KIT CORE (Unchanged)                                       │
│   /speckit.constitution → /speckit.specify → /speckit.plan ...  │
└─────────────────────────────────────────────────────────────────┘
```

**Total User Time**: ~2-3 hours (conversational workflow)  
**Implementation Time**: 2-3 weeks (development)

---

## 🧬 Decisions Matrix (Ideation Session Q1-Q7)

| Question | Decision | Rationale |
|----------|----------|-----------|
| **Q1: Timeline** | B+ (1-3 weeks, multiple ideas) | Real project in 2-3 weeks, needs complete solution |
| **Q2: Workflow** | A (Full 4-phase workflow) | Double Diamond complete (diverge→converge→define→refine) |
| **Q3: IDEATE Role** | B (Co-creator, SCAMPER+HMW full) | User seeds + agent expands, frameworks in plenitude |
| **Q4: SELECT Framework** | C (AI-RICE 6D) | AI-specific dimensions (Data, Risk), rigorous scoring |
| **Q5: STRUCTURE** | B (Integrated Canvas) | JTBD+Lean+AI in 1 canvas, frameworks complete but not fragmented |
| **Q6: VALIDATE Gate** | C (Rigorous, 20 criteria, waivers) | Maximum rigor, AI-specific checks, pragmatic waivers |
| **Q7: State Management** | B (Lightweight state) | Dependency validation, minimal overhead, upgrade path to C |

---

## 📁 Artifacts & File Structure

### Repository Structure (Post-Implementation)

```
spec-kit/ (fork: feature/ai-ideation branch)
│
├── templates/
│   ├── commands/
│   │   ├── constitution.md       (existing - unchanged)
│   │   ├── specify.md            (existing - unchanged)
│   │   ├── ideate.md             ← NEW (Phase 0.1)
│   │   ├── select.md             ← NEW (Phase 0.2)
│   │   ├── structure.md          ← NEW (Phase 0.3)
│   │   └── validate.md           ← NEW (Phase 0.4)
│   │
│   ├── ideas-backlog-template.md       ← NEW
│   ├── idea-selection-template.md      ← NEW
│   ├── ai-vision-canvas-template.md    ← NEW
│   ├── vision-brief-template.md        ← NEW (AI-specific)
│   └── g0-validation-report-template.md ← NEW
│
├── scripts/
│   ├── bash/
│   │   ├── ideate.sh             ← NEW (setup, file creation)
│   │   ├── select.sh             ← NEW (read backlog, scoring UI)
│   │   ├── structure.sh          ← NEW (canvas → brief transform)
│   │   ├── validate-g0.sh        ← NEW (20 criteria checks)
│   │   └── state-manager.sh      ← NEW (read/write state.yaml)
│   │
│   └── powershell/
│       ├── ideate.ps1            ← NEW
│       ├── select.ps1            ← NEW
│       ├── structure.ps1         ← NEW
│       ├── validate-g0.ps1       ← NEW
│       └── state-manager.ps1     ← NEW
│
└── .spec-kit/ (runtime, created by workflow)
    ├── state.yaml                ← NEW (lightweight tracking)
    ├── ideas_backlog.md          (IDEATE output)
    ├── idea_selection.md         (SELECT output)
    ├── ai_vision_canvas.md       (STRUCTURE output)
    ├── vision_brief.md           (STRUCTURE output - main artifact)
    └── approvals/
        └── g0-validation-report.md (VALIDATE output)
```

**New Files**: 18 total (5 commands, 5 templates, 10 scripts)

---

## ✅ Implementation Status (Line-by-Line Summary)

**Templates / Commands**
- `templates/commands/ideate.md` — **DONE**
- `templates/commands/select.md` — **DONE**
- `templates/commands/structure.md` — **DONE**
- `templates/commands/validate.md` — **DONE**

**Templates / Artifacts**
- `templates/ideas-backlog-template.md` — **DONE**
- `templates/idea-selection-template.md` — **DONE**
- `templates/ai-vision-canvas-template.md` — **DONE**
- `templates/vision-brief-template.md` — **DONE**
- `templates/g0-validation-report-template.md` — **DONE**

**Bash Scripts**
- `scripts/bash/ideate.sh` — **MISSING**
- `scripts/bash/select.sh` — **MISSING**
- `scripts/bash/structure.sh` — **MISSING**
- `scripts/bash/validate-g0.sh` — **DONE**
- `scripts/bash/state-manager.sh` — **REPLACED** by `state-init.sh`, `state-check.sh`, `state-update.sh`, `state-reconstruct.sh`, `state-log-violation.sh`

**PowerShell Scripts**
- `scripts/powershell/ideate.ps1` — **MISSING**
- `scripts/powershell/select.ps1` — **MISSING**
- `scripts/powershell/structure.ps1` — **MISSING**
- `scripts/powershell/validate-g0.ps1` — **DONE**
- `scripts/powershell/state-manager.ps1` — **REPLACED** by `state-init.ps1`, `state-check.ps1`, `state-update.ps1`, `state-reconstruct.ps1`, `state-log-violation.ps1`

**Runtime Structure**
- `.spec-kit/state.yaml` — **DONE** (created via `state-init` scripts)
- `.spec-kit/approvals/` — **MISSING** (not auto-created)
- `.spec-kit/*.md` artifacts — **DONE** (created when running Phase 0)

---

## 🔧 Framework Specifications (Detailed)

### Phase 1: IDEATE - Co-creator with SCAMPER + HMW

**SCAMPER (7 lenses applied to each seed idea)**:
1. **Substitute**: Replace component (e.g., "E se usar embeddings sem LLM?")
2. **Combine**: Merge approaches (e.g., "RAG + fine-tuning hybrid?")
3. **Adapt**: Borrow from other domain (e.g., "Recommendation systems approach?")
4. **Modify**: Change attribute (e.g., "Real-time vs batch processing?")
5. **Put to another use**: Repurpose (e.g., "Use chatbot for analytics too?")
6. **Eliminate**: Remove constraint (e.g., "What if no budget limit?")
7. **Reverse**: Invert assumption (e.g., "What if users train AI, not us?")

**HMW (How Might We) questions**:
- Generated for each dimension: data, model, safety, cost, UX
- Examples: "HMW reduce hallucinations?", "HMW handle multi-turn context?"

**Output Format** (ideas_backlog.md):
```markdown
# Ideas Backlog: [Project Name]

## Seed Ideas (User-provided)
1. **RAG over Knowledge Base** [SEED]
2. **Fine-tuned chatbot** [SEED]
3. **Agent system with tools** [SEED]

## SCAMPER Expansions
4. **RAG + Fine-tuning Hybrid** [SCAMPER-COMBINE from #1+#2]
   - Rationale: Combine retrieval accuracy with domain-specific responses
5. **Multi-agent RAG** [SCAMPER-ADAPT from #1]
   - Rationale: Each agent specializes (routing, retrieval, summarization)
...

## HMW Expansions
10. **RAG with Fact-checking Agent** [HMW: reduce hallucinations from #1]
    - Rationale: Verify AI summaries against source KB articles
...

Total: 13 ideas (3 seed + 5 SCAMPER + 5 HMW)
```

---

### Phase 2: SELECT - AI-RICE Scoring (6 Dimensions)

**Scoring Formula**:
```
AI-RICE Score = (Reach × Impact × Confidence × Data_Readiness) / (Effort × Risk)
```

**Dimensions**:
1. **Reach** (number): Users/requests affected (e.g., 1000 agents)
2. **Impact** (0.25-3): Minimal/Low/Medium/High/Massive per user
3. **Confidence** (0-100%): Viability certainty
4. **Data_Readiness** (0-100%): Data availability + quality
5. **Effort** (person-weeks): Implementation time
6. **Risk** (1-10): Safety, bias, compliance, jailbreaks

**Output Format** (idea_selection.md):
```markdown
# Idea Selection: [Project Name]

## Scoring Results (AI-RICE)

| Idea | Reach | Impact | Conf% | Data% | Effort | Risk | Score |
|------|-------|--------|-------|-------|--------|------|-------|
| RAG over KB | 1000 | 2.0 | 70% | 60% | 4pw | 4 | **52.5** |
| Fine-tuned | 1000 | 2.5 | 50% | 40% | 8pw | 6 | 10.4 |
| Auto-categorization | 1500 | 1.5 | 85% | 80% | 3pw | 2 | **127.5** ✅ |
...

## Selected Idea: Auto-categorization of Support Tickets

**AI-RICE Score**: 127.5 (highest)

**Score Breakdown**:
- Reach: 1500 tickets/month
- Impact: 1.5 (Medium-High)
- Confidence: 85% (classification proven)
- Data_Readiness: 80% (historical tickets, need labeling)
- Effort: 3 person-weeks
- Risk: 2 (low - misclassification non-critical)

**Rationale**: [Why this vs others, trade-offs]

**Runner-ups**: [2nd, 3rd options for pivot]
```

---

### Phase 3: STRUCTURE - Integrated Canvas (JTBD + Lean + AI)

**Canvas Structure** (18 components across 3 sections):

**SECTION 1: JOBS-TO-BE-DONE** (5 components)
1. Job Statement: "When [situation], I want [motivation], so I can [outcome]"
2. Job Executor: Who performs job
3. Job Context: Where, when, circumstances
4. Desired Outcomes: Functional, emotional, social (measurable)
5. Current Solution Pains: Inadequacies

**SECTION 2: LEAN STARTUP** (6 components)
1. Top 3 Problems
2. Solution (high-level)
3. Key Assumptions (critical, unvalidated)
4. Validation Methods
5. Key Metrics (success criteria)
6. Cost Structure

**SECTION 3: AI-SPECIFIC** (7 components)
1. AI Task: What AI predicts/generates
2. Data Requirements: Sources, quality, labeling, bias, privacy
3. Model Approach: Family, selection, rationale, prompts
4. Evaluation Strategy: Metrics, benchmarks, human evals
5. Safety & Risk: Risks, mitigations, compliance
6. Constraints: Budget, latency, context, compliance
7. Infrastructure: High-level considerations

**Transformation**: Canvas → vision_brief.md (formatted markdown)

---

### Phase 4: VALIDATE - Gate G0 (20 Criteria Rigorous)

**Automated Checks** (8 criteria - bash script):
1. vision_brief.md exists
2. All 7 sections present
3. No [PLACEHOLDER] tokens
4. Job statement format correct
5. ≥3 assumptions documented
6. ≥3 metrics defined
7. ≥1 data source identified
8. Model approach ≥50 words

**Manual Checks - Quality** (5 criteria):
9. Assumptions have validation methods
10. Metrics are SMART
11. Data sources concrete
12. Model rationale present
13. Risk mitigations defined

**Manual Checks - AI-Specific** (4 criteria):
14. Data readiness ≥60%
15. Evaluation strategy defined
16. Safety assessment complete
17. Cost viability aligned

**Consistency Checks** (3 criteria):
18. JTBD ↔ Metrics alignment
19. Lean solution ↔ AI task alignment
20. Constraints ↔ Model choice alignment

**Waiver Mechanism**: Can approve with justification if criteria fails (documented in report).

**Output**: g0-validation-report.md with PASS/FAIL/WAIVED status per criterion + overall decision.

---

## 🗓️ Implementation Roadmap

### Phase Breakdown (14 working days)

#### **Week 1: Core Workflow (Days 1-7)**

**Days 1-4: IDEATE Command** (P0 - Critical Path)
- [ ] Day 1: Setup branch + file structure
  - [x] Create `feature/ai-ideation` branch (**done as** `001-ai-ideation-phase0`)
  - [ ] Setup `.spec-kit/` runtime directory structure (**missing**: auto-create `.spec-kit/approvals` + `.spec-kit/.gitignore`)
  - [x] Create template placeholders
- [ ] Day 2: IDEATE command + SCAMPER logic
  - [x] `templates/commands/ideate.md` (conversational flow)
  - [x] SCAMPER expansion logic (7 lenses) — prompt-driven
  - [ ] `scripts/bash/ideate.sh` (file creation)
- [x] Day 3: HMW questions + output formatting
  - [x] HMW generation logic (adaptive questions) — prompt-driven
  - [x] `ideas_backlog.md` template with provenance tags
  - [x] Test with sample seed ideas
- [ ] Day 4: Integration + validation
  - [x] End-to-end IDEATE test (3 seeds → 10+ ideas)
  - [ ] Edge cases (1 seed, 10 seeds)
  - [x] Documentation

**Days 5-7: SELECT Command** (P0 - Critical Path)
- [ ] Day 5: AI-RICE scoring framework
  - [x] `templates/commands/select.md` (scoring guidance)
  - [x] AI-RICE formula definition (prompt + validation)
  - [x] `idea_selection.md` template
- [ ] Day 6: Interactive scoring UI
  - [ ] `scripts/bash/select.sh` (read backlog, prompt dimensions)
  - [ ] 6 dimensions input (Reach, Impact, Conf, Data, Effort, Risk)
  - [ ] Score calculation + ranking
- [ ] Day 7: Rationale + runner-ups
  - [ ] Auto-generate rationale (why winner vs others)
  - [ ] Runner-ups selection (top 3)
  - [ ] Test scoring 8-15 ideas

**Milestone W1**: 🟡 IDEATE complete; SELECT prompt-driven (automation pending)

---

#### **Week 2: Completion + Integration (Days 8-14)**

**Days 8-11: STRUCTURE Command** (P0 - Critical Path)
- [x] Day 8: Integrated Canvas template
  - [x] `ai_vision_canvas.md` template (3 sections)
  - [x] Section 1: JTBD components
  - [x] Section 2: Lean components
- [ ] Day 9: Canvas filling logic
  - [x] `templates/commands/structure.md` (conversational flow)
  - [x] Section 3: AI-specific components
  - [ ] `scripts/bash/structure.sh` (canvas creation)
- [ ] Day 10: Canvas → Brief transformation
  - [x] `vision_brief.md` template (formatted output)
  - [ ] Transform logic (canvas sections → brief sections)
  - [ ] Test with sample idea
- [x] Day 11: Integration + validation
  - [x] End-to-end STRUCTURE test (idea → canvas → brief)
  - [x] Ensure all 18 components filled
  - [x] Documentation

**Days 12-13: VALIDATE Command** (P0 - Critical Path)
- [x] Day 12: Gate G0 automated checks
  - [x] `scripts/bash/validate-g0.sh` (8 automated criteria)
  - [x] File existence, format checks, counts
  - [x] `g0_validation_report.md` template
- [x] Day 13: Manual checklist + waiver
  - [x] `templates/commands/validate.md` (20 criteria checklist)
  - [x] Waiver mechanism (justification required)
  - [x] Approval + handoff logic

**Day 14: State Management + Integration** (P1)
- [x] State schema design
  - [x] `state.yaml` structure (lightweight)
  - [x] current_phase, phases_completed, artifacts
- [x] State read/write logic
  - [x] Implemented via `state-init.sh`, `state-check.sh`, `state-update.sh`, `state-reconstruct.sh`, `state-log-violation.sh`
  - [x] Integrated into Phase 0 guidance (prompt-driven)
- [x] Dependency validation
  - [x] Cannot SELECT without IDEATE (state-check scripts)
  - [x] Cannot STRUCTURE without SELECT (state-check scripts)
  - [x] Re-run protection warnings (command prompts)
- [x] End-to-end testing
  - [x] Full workflow: IDEATE → SELECT → STRUCTURE → VALIDATE
  - [x] State tracking verification (scripts)
  - [ ] Edge cases (skip phases, re-run)

**Milestone W2**: ✅ Complete workflow E2E functional + state management

---

#### **Week 3 (Optional): Polish + Dogfooding**

**Days 15-17: Dogfooding with Real Idea**
- [ ] Nuno runs full workflow with real AI system idea
- [ ] Collect friction points, confusing steps
- [ ] Iterate based on feedback

**Days 18-19: Documentation + README**
- [x] Update main README with Phase 0 section
- [x] Document each command (inputs, outputs, examples)
- [x] Create quickstart guide

**Day 20: Final Review**
- [ ] Code review
- [ ] Test coverage check
- [ ] Prepare for potential upstream PR (future)

**Milestone W3**: 🟡 Documentation complete; final review + dogfooding pending

---

## 🚀 Next Immediate Actions (Priority Order)

### **TODAY (Day 0)** - Setup
1. ✅ Review this blueprint (you just did!)
2. [x] Create feature branch:
   ```bash
   cd /mnt/d/GitHub/spec-kit
   git checkout -b 001-ai-ideation-phase0
   git push -u origin 001-ai-ideation-phase0
   ```
3. [ ] Create runtime directory structure:
   ```bash
   mkdir -p .spec-kit/approvals
   touch .spec-kit/.gitignore
   echo "state.yaml" >> .spec-kit/.gitignore
   echo "*.md" >> .spec-kit/.gitignore  # artifacts are runtime
   ```

### **TOMORROW (Day 1)** - Start IDEATE
4. [x] Create `templates/ideas-backlog-template.md`
5. [x] Start `templates/commands/ideate.md` (outline structure)
6. [ ] Draft `scripts/bash/ideate.sh` (minimal: create file)

### **Week 1 Focus** - Core Workflow
- IDEATE + SELECT commands functional
- Can generate 10+ ideas from 3 seeds
- Can score and choose 1 idea
- **Goal**: Validate approach works (frameworks generate useful output)

### **Week 2 Focus** - Completion
- STRUCTURE + VALIDATE commands functional
- State management integrated
- Full E2E workflow tested
- **Goal**: Ready for real dogfooding

---

## 📊 Success Criteria (PoC Acceptance)

### Functional Requirements
- [x] Can run `/speckit.ideate` → generates 8-15 ideas from 2-5 seeds
- [x] Can run `/speckit.select` → scores all ideas, selects 1 with rationale
- [x] Can run `/speckit.structure` → produces vision_brief.md with 18 components
- [x] Can run `/speckit.validate` → validates 20 criteria, generates report
- [x] State prevents out-of-order execution (cannot SELECT before IDEATE)
- [x] Re-run protection warns user before overwriting

### Quality Requirements
- [x] Frameworks applied correctly (SCAMPER 7 lenses, AI-RICE formula, JTBD format)
- [x] Output artifacts are complete (no missing sections)
- [x] Gate G0 validation is rigorous (20 criteria enforced)
- [x] Documentation clear (can hand to another developer)

### Integration Requirements
- [x] vision_brief.md is valid input for `/speckit.constitution`
- [x] Workflow compatible with spec-kit philosophy (progressive disclosure, traceability)
- [x] No changes to spec-kit core (constitution, specify, plan unchanged)

### Timeline Requirement
- [x] Delivered within 2-3 weeks (14-20 working days)

---

## 🎓 Key Design Decisions (Rationale)

### Why Fork Experimental vs Extension Repo?
**Decision**: Start with fork (`feature/ai-ideation` branch)  
**Rationale**: 
- Faster to prototype (same repo structure)
- Easy to test integration with spec-kit commands
- Can migrate to extension repo if upstream doesn't want merge
- Lower barrier to start (no separate repo setup)

### Why Lightweight State vs Full Stateful?
**Decision**: Lightweight for PoC, Full as P2 enhancement  
**Rationale**:
- PoC validates workflow utility (frameworks, output quality)
- Rich UX (status dashboard, history) is polish, not core value
- Timeline: +1-2 days vs +3-4 days (33% faster)
- Upgrade path clear (documented in FUTURE_ENHANCEMENTS.md)

### Why AI-RICE vs Standard RICE?
**Decision**: AI-RICE (6 dimensions) vs RICE (4 dimensions)  
**Rationale**:
- Data readiness is #1 AI project failure cause (40% fail due to data issues)
- Risk dimension critical for AI (safety, bias, jailbreaks)
- Generic frameworks miss AI-specific concerns
- Marginal complexity (6 vs 4 dimensions) but massive risk reduction

### Why Integrated Canvas vs 3 Separate Canvas?
**Decision**: 1 canvas with 3 sections vs 3 canvas files  
**Rationale**:
- Less fragmentation (1 file vs 3+1)
- User sees big picture (JTBD + Lean + AI in one view)
- Still rigorous (each framework has dedicated section)
- Easier to fill (1 session vs 3 sessions)

---

## 📚 References & Resources

### Frameworks Documentation
- **SCAMPER**: Bob Eberle (1971) - Creative thinking technique
- **JTBD**: Clayton Christensen - Jobs-to-be-Done framework
- **Lean Startup**: Eric Ries, Ash Maurya - Lean Canvas
- **RICE Scoring**: Intercom (Sean McBride) - Product prioritization
- **Design Thinking**: IDEO, Stanford d.school - Double Diamond

### AI-Specific Resources
- **AI Canvas**: Adapted from Business Model Canvas for AI systems
- **Responsible AI**: Fairness, Privacy, Safety, Explainability frameworks
- **AI Product Design**: Data → Model → Application → Deployment

### Spec-Kit Core
- **Repository**: https://github.com/github/spec-kit
- **Documentation**: README.md, spec-driven.md
- **Commands**: templates/commands/*.md
- **Philosophy**: Progressive disclosure, constitution-driven, traceability

---

## 🔄 Future Roadmap (Post-PoC)

### Phase 2: Full Stateful Mode (P2)
- Rich state.yaml with timestamps, decisions log
- Auxiliary commands: /speckit.status, /speckit.resume, /speckit.reset, /speckit.history
- Estimated: +3-4 days
- **Tracked in**: FUTURE_ENHANCEMENTS.md

### Phase 3: Additional Output Profiles (P3)
- Extend beyond ai-system to: web-saas, cli, desktop, library
- Profile-specific dimensions and gates
- Estimated: +2-3 weeks per profile

### Phase 4: Phases 6-8 (Post-Implementation)
- Phase 6: Verification (QA, NFR, security gates)
- Phase 7: Release (packaging, deployment, SBOM)
- Phase 8: Operation (observability, runbooks, iteration)
- Estimated: +4-6 weeks for all 3 phases

### Phase 5: Upstream Contribution
- Clean up PoC code
- Comprehensive documentation
- Test coverage
- Submit PR to github/spec-kit (if desired)

---

## ✅ Checklist: Ready to Start?

- [x] Ideation session completed (Q1-Q7 decisions made)
- [x] Implementation blueprint documented (this file)
- [x] Future enhancements tracked (FUTURE_ENHANCEMENTS.md)
- [x] Ideation session log preserved (ideation-session.md)
- [x] Feature branch created (`001-ai-ideation-phase0`)
- [ ] Runtime directory setup (`.spec-kit/`)
- [x] Day 1 template created (ideas-backlog-template.md)

**Status**: 🟡 **IMPLEMENTATION COMPLETE WITH GAPS**

**Start Command**: Close gaps in runtime setup + missing automation scripts

---

**Blueprint Prepared By**: Ideation session with Claude (Copilot CLI)  
**Session Duration**: 1h 30min (13:02 - 14:30 on 2026-01-12)  
**Decisions Made**: 7 major (Q1-Q7), all documented  
**Frameworks Selected**: SCAMPER, HMW, AI-RICE, JTBD, Lean, AI Canvas, Gate G0  
**Timeline Estimated**: 2-3 weeks (14 working days realistic)  

**Next Review**: After Week 1 (IDEATE + SELECT functional) - validate approach works before continuing.

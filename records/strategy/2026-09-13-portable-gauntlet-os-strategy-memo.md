# Strategy Memo — Portable Gauntlet-OS Architecture and Open-Source Capability Expansion

**Date:** 2026-09-13  
**Prepared for:** Logan M  
**Prepared by:** ChatGPT  
**Status:** PROPOSED — research and architecture recommendation  
**Scope:** Gauntlet-OS across business-building, marketing, research, product development, and recurring operations  
**Provenance:** Preserves the substantive research proposal delivered in conversation on 2026-09-13, formatted as a repository strategy memo.

Publication records this proposal; it does not adopt a runtime, amend the constitution, authorize installations or external actions, alter frozen experiments, or activate held opportunities. Software candidates were reviewed through repository content and documentation, not installed or benchmarked in the Gauntlet environment. External links describe sources reviewed on the research date; they are not immutable dependency pins.

## Executive recommendation

Gauntlet-OS should assemble and run the right organization for a task: investigate a business, build a product, launch marketing, or operate a repeatable service.

Keep a small universal Gauntlet core. Add interchangeable domain packs and workflow templates. Use open-source software to execute those workflows, connect tools, and measure results.

GrokBot can remain the primary interface. The institution's records and operating logic should be portable enough to survive changing models or platforms.

The recommended initial implementation is deliberately small: LangGraph, persistent structured records, Promptfoo, and only the document or integration tools the first mission requires. Add tracing early as complexity grows. Evaluate Activepieces for operational connections, GrowthBook for a real marketing experiment, and DSPy after useful labeled examples accumulate.

## 1. Existing foundation

The constitution is more general than the crypto implementation. It defines bounded assignments, attributable claims, independent examination, protected evaluation, failure memory, and versioned changes. It explicitly requires measuring improvements to the institution itself. The domain template already calls for adapting the workforce and outcomes while preserving those rules.

Sources: [Gauntlet constitution](../../constitution/GAUNTLET_PROTOCOL_V2.md), [domain-pack template](../../domain-packs/template/README.md).

The missing piece is making that portability executable.

Today, much of the adaptation happens through the Human Governor and lengthy instructions. A stronger system would turn an objective into a structured specification, select the appropriate workflow and capabilities, and track the work through to observed outcomes.

That does not require the same 14 roles or promotion ladder for every assignment.

| Universal across Gauntlet | Changes with the assignment |
|---|---|
| Source provenance and evidence labels | Relevant sources and domain vocabulary |
| Separation of proposing, measuring, and authorizing | Specialists and required reviewers |
| Versioned tasks, artifacts, and decisions | Deliverable formats |
| Explicit budgets and action boundaries | Which actions are permitted |
| Failure preservation and recovery | What failure means |
| Traceable quantitative results | Metrics and measurement methods |
| Honest uncertainty | Required strength of evidence |
| Recorded outcomes | Whether success means revenue, accuracy, conversion, or delivery |

A marketing writer should have room to explore creative approaches. A system claiming that a campaign increased sales needs actual observations and a defensible measurement method. Those are different activities with different acceptance criteria.

## 2. Proposed architecture

Organize Gauntlet into five layers.

| Layer | Its job | Example |
|---|---|---|
| Institutional core | Defines authority, evidence, versioning, and action rules | An author cannot certify their own empirical result |
| Mission specification | Defines what this run must accomplish | Produce a launch-ready acquisition campaign for a specific offer |
| Domain pack | Supplies specialist knowledge, tools, and measurements | Marketing audience definitions, brand context, analytics, channel constraints |
| Workflow template | Defines how work progresses | Research → create variants → review → prepare test → measure |
| Execution and records | Runs tasks, handles failures, stores evidence and outcomes | Saved checkpoints, tool adapters, artifact registry, cost tracking |

Domain and workflow are separate choices.

For example, marketing is a domain. Within it, competitor research, creative production, campaign experimentation, and weekly reporting require different workflows.

Similarly, a business-building mission can compose several packs: market research, economics, product development, marketing, and operations.

This lets Gauntlet reuse meaningful capabilities without forcing every problem through one enormous procedure.

## 3. Custom component: a mission compiler

A mission compiler is a small planning and validation layer that translates a request into a runnable specification.

Example request:

> Take this established business model, identify a better way to operate it, build the necessary assets, and prepare a first-customer test.

It produces:

- The objective and what counts as completion.
- Known facts, assumptions, and unresolved questions.
- Required domain packs and capabilities.
- Tasks, dependencies, and accountable roles.
- Expected artifacts.
- Budget and time constraints.
- Permitted actions and existing authorizations.
- Measurement and stopping rules.
- The governing protocol version.

The model drafts this specification. Code checks whether its fields are complete, dependencies are valid, requested tools exist, and proposed actions fit the authorization.

The compiler should also detect an assignment that cannot yet be evaluated. For example, “maximize marketing” lacks a target customer, offer, outcome, and budget. It should use existing company context to fill those fields, then surface only important gaps.

This is the component to build specifically for Gauntlet. None of the frameworks reviewed supplies the institution's full decision logic out of the box.

## 4. Reusable workflow patterns

Start with four reusable patterns.

| Pattern | Appropriate work | Completion evidence |
|---|---|---|
| Investigate | Business diligence, competitor research, opportunity screening | Supported findings, bounded uncertainties, decision recommendation |
| Build | Websites, software, creative assets, operational workflows | Working artifact plus relevant acceptance checks |
| Experiment | Offers, acquisition channels, pricing, forecasting methods | Prospectively specified test and measured outcomes |
| Operate | Recurring reporting, fulfillment, monitoring, case processing | Completed transactions or deliverables, exceptions, service metrics |

A business mission can move through all four. A simple landing-page revision may use only Build.

This approach is consistent with Anthropic's engineering guidance: use predictable workflows for well-defined work, dynamic agent orchestration for open-ended problems, and add complexity when it improves results. Their guidance also emphasizes clear tool interfaces and direct feedback from the environment. [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).

A universal institution should be able to choose a small workflow. Otherwise, its overhead will make ordinary commercial work uneconomic.

## 5. Open-source capability shortlist

Divide candidates by the capability they add, rather than popularity.

| Component | Useful capability | Proposed place in Gauntlet |
|---|---|---|
| LangGraph | Explicit workflows combining code and agent steps, persistence, review interruptions | First runtime candidate |
| Temporal | Durable execution for long-running processes, retries, timers, external waits | Alternative for operationally demanding workflows |
| Langfuse | Tracing, prompt versions, datasets, evaluation records | Visibility into quality, cost, and failures |
| Promptfoo | Repeatable comparisons of prompts, models, and application behavior | Capability admission and regression testing |
| DSPy | Optimization of modular language-model programs against metrics | Later improvement of proven recurring tasks |
| Docling | Structured extraction from documents, including PDFs and Office formats | Shared document-ingestion capability |
| Crawl4AI | Browser-backed web extraction and structured outputs | Shared public-web collection capability |
| Activepieces | Business integrations, versioned flows, approval and input steps | Connection to operational systems |
| GrowthBook | Feature flags, experiment management, statistical analysis | Marketing and product experimentation |
| Marketing Skills | Reusable marketing procedures and shared product context | Starting material for the marketing domain pack |

These are candidates with specific responsibilities, not a recommendation to deploy ten systems at once. Open-core and source-available licensing distinctions are noted below; the table is not a blanket licensing certification.

### LangGraph versus Temporal

LangGraph is the preferred first candidate because the immediate challenge involves explicit handoffs, branching research, artifact review, and resumable agent work. Its persistence system distinguishes run checkpoints from longer-term stores. Production recovery requires a persistent backend; the in-memory examples do not survive restarts. [LangGraph repository](https://github.com/langchain-ai/langgraph), [persistence documentation](https://docs.langchain.com/oss/python/langgraph/persistence).

Temporal becomes particularly attractive when Gauntlet operates processes that wait hours or days, recover from service failures, and coordinate consequential external actions. Its documentation supports these durability patterns. It also makes clear that activities can execute more than once during retries; preventing duplicate external effects remains an application responsibility. [Temporal's AI documentation](https://docs.temporal.io/ai), [activity and retry semantics](https://docs.temporal.io/activity-definition).

Prototype one runtime first. Stacking both immediately adds operational burden before the need has been measured.

CrewAI and Microsoft Agent Framework are credible alternatives. CrewAI separates autonomous teams from explicit Flows; Microsoft provides graph workflows, checkpointing, multiple providers, and observability. Compare them if the first prototype exposes a concrete mismatch, rather than running a month-long framework tournament. [CrewAI](https://github.com/crewAIInc/crewAI), [Microsoft Agent Framework](https://github.com/microsoft/agent-framework).

### Tracing and evaluation

Langfuse can show where agent calls, retrieval, and tools consumed time and produced errors. Promptfoo can run a repeatable suite when a prompt, model, or skill changes. Neither determines what constitutes success for a business; Gauntlet supplies the evaluation criteria. [Langfuse](https://github.com/langfuse/langfuse), [Promptfoo](https://github.com/promptfoo/promptfoo).

Use code checks where correctness is machine-verifiable, human assessment where judgment is essential, and external outcomes for claims about commercial effectiveness. An LLM reviewer can help identify problems, but its approval cannot establish that customers will buy.

### Document and web capabilities

Docling is relevant across competitor materials, public records, regulations, reports, and business documents. It supports structured document representations and local processing. Extraction still needs quality checks and links back to the original source. [Docling](https://github.com/docling-project/docling).

Crawl4AI offers controllable browser-based collection and structured extraction. Wrap it in a narrow Gauntlet interface that records source URLs, timestamps, original captures, and failures. Its recent release notes include security fixes, reinforcing selection and testing of an exact version rather than copying an old installation snippet. [Crawl4AI](https://github.com/unclecode/crawl4ai).

### Business integrations

Activepieces connects reasoning to actual business systems. Its community edition provides an MIT-licensed foundation, with separately licensed enterprise features. Its integrations can also be exposed through MCP. [Activepieces](https://github.com/activepieces/activepieces).

n8n is another viable integration platform, but it is source-available under its Sustainable Use License rather than uniformly permissive open source. Its license distinguishes internal use from other commercial uses. That matters if Gauntlet eventually becomes customer-facing software. [n8n license](https://github.com/n8n-io/n8n/blob/master/LICENSE.md).

Choose between them based on the first mission's required connectors and intended deployment, not integration counts alone.

## 6. Marketing domain pack

The most directly relevant domain repository reviewed is [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills). It includes procedures for customer research, positioning, offers, copywriting, conversion optimization, analytics, experimentation, retention, and acquisition.

Its useful architectural idea is a shared product-marketing context that other skills consult. That fits interchangeable workflows.

Adapt a small initial selection:

- Product and customer context.
- Customer research.
- Offer design.
- Copywriting.
- Conversion review.
- Analytics.
- Experiment design.

The source library is useful instructional material. Its presence does not establish marketing effectiveness.

A Gauntlet marketing run should produce more than a plan.

| Stage | Required output |
|---|---|
| Understand | Product, customer, offer, constraints, existing evidence |
| Investigate | Customer language, alternatives, buying triggers, channel evidence |
| Create | Distinct positioning and creative hypotheses |
| Build | Landing pages, campaign assets, tracking specification |
| Prepare | Reviewable launch package with budget and measurement rules |
| Measure | Exposure, qualified actions, customers, revenue, and relevant costs |
| Learn | Which hypothesis gained support, failed, or remains unresolved |

GrowthBook is a candidate for experimentation. Its repository documents feature flags, metric definitions, experimentation statistics, and APIs. Some features are commercially licensed. It can support measurement, but valid assignment, instrumentation, and sufficient observations still have to exist. [GrowthBook](https://github.com/growthbook/growthbook), [experiment results documentation](https://docs.growthbook.io/app/experiment-results).

A good-looking campaign can pass a production-quality review while its commercial effectiveness remains untested.

## 7. Business-building domain pack

Avoid a single entrepreneur agent tasked with producing a giant business plan.

Instead, the mission should identify the uncertainties that could kill the business and commission bounded work around them.

| Question | Capability | Evidence sought |
|---|---|---|
| Who buys, and why now? | Customer and demand research | Buying behavior, existing spend, direct customer evidence |
| Can we deliver profitably? | Economics and operations | Actual inputs, delivery time, support burden, contribution margin |
| Can we reach buyers? | Distribution | Accessible audience, channel mechanics, acquisition observations |
| What must be built? | Product engineering | Smallest working delivery system |
| What could prevent operation? | Domain review | Applicable requirements and unresolved constraints |
| What deserves expansion? | Experiment analysis | Repeat purchases, retention, delivery quality, net economics |

The build output could be a website, internal dashboard, quoting tool, fulfillment workflow, or working service process.

The mission is complete when the specified operating capability exists and has the agreed evidence, not when the report is long enough.

For Logan's preference for simple businesses, the default should favor testing an existing commercial model and improving its execution. Inventing a new category should require an explicit mission objective.

## 8. Three distinct memory functions

Separate:

1. **Evidence:** original sources, observations, test outputs, provenance.
2. **Current state:** active tasks, blockers, authorizations, adopted versions.
3. **Reusable knowledge:** methods, failure patterns, successful components, applicability limits.

This can begin with ordinary structured storage and linked files. A graph database or elaborate autonomous memory system is not necessary at the outset.

The valuable retrieval behavior is:

> Before starting this task, find relevant prior attempts, explain why they succeeded or failed, and determine whether their conditions apply here.

A failed acquisition campaign should preserve its audience, offer, channel, costs, and failure diagnosis. “Email failed” is not useful institutional knowledge.

Cross-domain reuse should transfer methods and qualified findings. Success in one domain does not automatically validate a conclusion in another.

## 9. Measurable improvements to Gauntlet

DSPy is worth investigating once recurring tasks and evaluation datasets exist. It supports modular language-model programs and algorithms that optimize prompts or other parameters against an objective. [DSPy](https://github.com/stanfordnlp/dspy), [optimization documentation](https://dspy.ai/getting-started/gepa-optimization/).

Suitable early targets include:

- Extracting business facts from documents.
- Identifying unsupported assertions.
- Resolving duplicate entities.
- Selecting relevant evidence.
- Producing valid task specifications.
- Classifying operational exceptions.

A proposed improvement should compete against the current method on development tasks, then face reserved evaluation tasks.

| Dimension | Example metric |
|---|---|
| Correctness | Accepted outputs; material errors |
| Independence | Unsupported promotions; evaluation contamination |
| Efficiency | Cost and elapsed time per accepted task |
| Human burden | Intervention minutes; clarification requests |
| Reliability | Recovery success; duplicate actions; lost artifacts |
| Commercial value | Contribution margin or qualified outcomes appropriate to the mission |

Do not collapse these immediately into a single weighted score. Apply hard requirements first, then compare surviving options on quality, cost, and speed.

## 10. Creativity and proportionate autonomy

The institution should support creative exploration without mistaking creative preference for empirical proof.

For marketing, specialists can generate divergent concepts and use editorial criticism to improve them. The system turns promising concepts into testable variants. Customer response determines effectiveness.

Not every reversible internal task should wake the entire governance structure. Assign review requirements according to consequence and the existing mandate. Independent authorities remain intact where their decisions matter.

Technical enforcement must be real. The Agent Skills specification supports metadata and an experimental allowed-tools field, but implementation support varies. A custom approval_required field is not, by itself, an access control. MCP defines how tools are described and invoked; the host application must implement actual permission behavior. [Agent Skills specification](https://agentskills.io/specification), [MCP tool specification, 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/server/tools).

## 11. Hybrid runtime and GrokBot interface

Recommend a hybrid architecture.

GrokBot remains where Logan discusses objectives, inspects progress, and makes decisions. An external runtime owns durable tasks, evidence records, evaluation jobs, and integrations. Workers can use whichever permitted model or execution environment best fits their assignment.

Official documentation confirms that GrokBot supports persistent teammates, shared files, skills, routines, and asynchronous handoffs. It also states that Bots share a computer and that their memory is not an authoritative source. [GrokBot workflow documentation](https://cursor.com/docs/grok-bot/work).

The integration must be demonstrated. A product supporting MCP does not prove that every custom connection, background process, or external dispatcher will work in the account.

If direct integration is unavailable, the same mission specification and artifact format can support an initial file-based handoff. The portable record comes first; seamless control can follow.

## 12. Initial portability pilot

Propose a bounded Gauntlet portability pilot with three demonstrations.

| Demonstration | Purpose | Success condition |
|---|---|---|
| Business research | Test evidence gathering and decision support | Supported brief, reproducible economics, explicit unknowns |
| Marketing production | Test creative work and artifact delivery | Working page or campaign package, verified tracking preparation |
| Recurring operations | Test persistence and exception handling | Scheduled work completes, survives interruption, and reports accurate state |

These demonstrations can use an existing project selected by Logan. They do not require activating Tax Appeal OS or altering the crypto experiment.

Implementation should proceed through four gates:

1. **Mission and artifact contracts.** Define the portable specification, evidence records, action receipts, and acceptance criteria.
2. **One complete workflow.** Implement with a single runtime, persistent storage, and the minimum required tools.
3. **Recovery and evaluation.** Prove interruption recovery, correct status, source preservation, and prevention of duplicate external effects.
4. **A second domain.** Reuse the core by changing the domain pack and workflow configuration. Record every place core code needed modification.

The last step is the portability test. If every new business requires a rewrite, the abstraction has failed.

The proposed initial stack is LangGraph, persistent structured records, Promptfoo, and only the document or integration tools the first mission requires. Add tracing early as complexity grows. Evaluate Activepieces for operational connections, GrowthBook for a real marketing experiment, and DSPy after useful labeled examples accumulate.

### Acceptance target

> One Gauntlet core completes research, production, and recurring operational work using different domain packs, preserves the evidence, and requires less coordination from Logan.

This proposal aims to make the existing institution broadly useful while ensuring each new dependency earns its place through demonstrated capability.

## Sources

Sources were reviewed on 2026-09-13. Repository README claims describe advertised capabilities and are not evidence that those capabilities have been validated in Gauntlet. License and compatibility checks must be repeated against any exact release proposed for adoption.

1. 17thgreen. [Gauntlet-OS constitution](../../constitution/GAUNTLET_PROTOCOL_V2.md).
2. 17thgreen. [Gauntlet-OS domain-pack template](../../domain-packs/template/README.md).
3. Anthropic. [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
4. LangChain. [LangGraph repository](https://github.com/langchain-ai/langgraph).
5. LangChain. [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence).
6. Temporal. [Durable AI](https://docs.temporal.io/ai).
7. Temporal. [Activity definition and retry semantics](https://docs.temporal.io/activity-definition).
8. CrewAI. [Repository](https://github.com/crewAIInc/crewAI).
9. Microsoft. [Agent Framework repository](https://github.com/microsoft/agent-framework).
10. Langfuse. [Repository](https://github.com/langfuse/langfuse).
11. Promptfoo. [Repository](https://github.com/promptfoo/promptfoo).
12. Docling Project. [Repository](https://github.com/docling-project/docling).
13. Crawl4AI. [Repository](https://github.com/unclecode/crawl4ai).
14. Activepieces. [Repository](https://github.com/activepieces/activepieces).
15. n8n. [License](https://github.com/n8n-io/n8n/blob/master/LICENSE.md).
16. Corey Haines. [Marketing Skills repository](https://github.com/coreyhaines31/marketingskills).
17. GrowthBook. [Repository](https://github.com/growthbook/growthbook).
18. GrowthBook. [Experiment results](https://docs.growthbook.io/app/experiment-results).
19. DSPy. [Repository](https://github.com/stanfordnlp/dspy).
20. DSPy. [GEPA optimization](https://dspy.ai/getting-started/gepa-optimization/).
21. Agent Skills. [Specification](https://agentskills.io/specification).
22. Model Context Protocol. [Tools specification, 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/server/tools).
23. Cursor. [Work with Grok Bot](https://cursor.com/docs/grok-bot/work).

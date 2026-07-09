metadata:
  name: crush-your-passion
  description: "A brutally honest project evaluation tool that systematically dismantles developer enthusiasm through 4-phase technical, commercial, strategic, and psychological analysis."
  emoji: 💀
  tags:
    - evaluation
    - code-review
    - commercial-analysis
    - strategic-assessment
    - brutal-honesty
  version: 1.0.0
  author: jznem
  openclaw:
    hooks:
      - event: agent:bootstrap
        handler: register_crush_your_passion_tools
      - event: command:evaluate
        handler: run_crush_your_passsion

hooks:
  - name: register_crush_your_passion_tools
    event: agent:bootstrap
    description: Register the Crush Your Passion evaluation tools in the OpenClaw tool registry.
    handler: |
      async function handler(context) {
        context.registerTool({
          name: 'crush-your-passion',
          description: 'Evaluate a software project with brutal honesty across 4 phases: technical, commercial, strategic, and the final blow.',
          parameters: {
            projectPath: { type: 'string', description: 'Path to the project directory or GitHub URL' },
            projectName: { type: 'string', description: 'Name of the project' },
            description: { type: 'string', description: 'Brief project description' },
            targetMarket: { type: 'string', description: 'Target market or intended users' },
            businessModel: { type: 'string', description: 'Business model (free, SaaS, enterprise, etc.)' },
            teamSize: { type: 'number', description: 'Number of people working on the project' },
            hasUsers: { type: 'boolean', description: 'Whether the project has active users' },
            hasRevenue: { type: 'boolean', description: 'Whether the project generates revenue' },
          },
          handler: 'run_crush_your_passsion'
        });
        return { success: true };
      }

  - name: run_crush_your_passsion
    event: command:evaluate
    description: Execute the full 4-phase evaluation pipeline and return a structured report.
    handler: |
      async function handler(context, params) {
        const { projectPath, projectName, description, targetMarket, businessModel, teamSize, hasUsers, hasRevenue } = params;

        // Phase 1: Technical Assessment
        const technicalReport = await context.runPython({
          script: `
from crush_your_passion.core.evaluator import ProjectEvaluator
evaluator = ProjectEvaluator("${projectPath || '/tmp'}", "${projectName || 'Unknown'}")
report = evaluator.evaluate()
print(report.full_report())
          `
        });

        // Phase 2: Commercial Assessment
        const commercialResult = assessCommercial(targetMarket, businessModel, hasUsers, hasRevenue);

        // Phase 3: Strategic Options
        const strategicResult = evaluateStrategies(description, targetMarket, businessModel, technicalReport);

        // Phase 4: The Final Blow
        const finalResult = deliverFinalBlow(technicalReport, commercialResult, strategicResult);

        return {
          phases: {
            technical: technicalReport,
            commercial: commercialResult,
            strategic: strategicResult,
            finalBlow: finalResult
          },
          summary: finalResult.verdict,
          confidence: finalResult.confidence
        };
      }

prompts:
  technical_assessment: |
    You are evaluating a software project's technical quality with brutal honesty.
    Focus on:
    1. Code quality — is it production-grade or prototype-level?
    2. Security — look for hardcoded keys, injection vectors, unsafe patterns
    3. Technical depth — does it solve a hard problem or assemble known parts?
    4. Tech debt — how many audit rounds would production quality take?
    
    Be specific. Name files and line numbers. Do not soften your assessment.

  commercial_assessment: |
    You are evaluating a project's commercial viability with brutal honesty.
    Focus on:
    1. Market reality — is this a real market with paying customers?
    2. Differentiation — what can this do that competitors cannot?
    3. Moat — apply the "3-day test": could a competent engineer replicate it in 3 days?
    4. Business model — is the monetization path realistic?
    
    Name specific competitors with concrete data. Do not inflate probabilities.

  strategic_options: |
    You are evaluating strategic options for a project that may have no viable path.
    For each option, assess:
    1. Surface appeal — why it sounds good
    2. Actual problems — why it probably won't work
    3. Hidden assumptions — what must be true for this to succeed
    4. Same-difficulty trap — is this harder than the original project?
    
    If all options have <10% probability, say "no viable path found."

  final_blow: |
    You are delivering the final, crushing assessment. Ask:
    "What do you have that others don't?"
    
    Categorize potential advantages: industry experience, credentials, network,
    proprietary data, regulatory positioning, timing.
    
    If the answer is "nothing specific," state that the project itself cannot
    create this advantage. Code is the least scarce resource.
    
    Deliver one of three verdicts:
    - Viable (rare)
    - Conditionally Viable (uncommon)
    - Not Viable (most common)

templates:
  report_template: |
    # {{projectName}} — CRUSH YOUR PASSION EVALUATION
    
    ## EXECUTIVE SUMMARY
    - Verdict: {{verdict}}
    - Confidence: {{confidence}}%
    - Technical Grade: {{technicalGrade}}
    - Commercial Grade: {{commercialGrade}}
    
    ## TECHNICAL ASSESSMENT
    {{technical}}
    
    ## COMMERCIAL ASSESSMENT
    {{commercial}}
    
    ## STRATEGIC OPTIONS
    {{strategic}}
    
    ## THE FINAL BLOW
    {{finalBlow}}
    
    ---
    *This evaluation exists to test whether your passion can survive brutal honesty.
    If it didn't survive — that was the point.*

  short_summary: |
    {{projectName}}: {{verdict}} ({{confidence}}%)
    Tech: {{technicalGrade}} | Market: {{commercialGrade}}
    {{oneLineTruth}}

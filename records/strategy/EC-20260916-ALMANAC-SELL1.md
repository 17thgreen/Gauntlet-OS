# EC-20260916-ALMANAC-SELL1

Execution contract. Not authority to mail.

```yaml
experiment_id: EC-20260916-ALMANAC-SELL1
version: 1
admission: DRAFT   # Auditor/Governor to ADMIT after P0 instrument fixes
execution: NOT_STARTED
evidence_verdict: UNTESTED
authority: NONE    # next grantable: BUILD_INSTRUMENT, then SHADOW, then LIMITED_PILOT

proposer: Discovery corpus (InsuranceOS design branch)
independent_examiner: Examiner (ALMANAC group)
responsible_builder: Mechanic

question: Do targeting, outreach sequence, and response experience produce exclusive leads that independent agencies purchase repeatedly, at acceptable seller and buyer economics and human workload?

claims_tested:
  - claim: Current-owner purchase month approximates that household's current policy anniversary.
    population: Agency book policies joinable to public-record current-owner acquisition.
    baseline: Chance / Cole-style compiled x-date if available.
    primary_outcome: Share of grade-A joins within ±1 calendar month.
    denominator: Joined policies with actual x-date present (report unmatched separately).
    window: One book, one freeze.
    result: "—"
    label: "[U]"
    green: ">=70% grade-A"
    kill_this_method: "<50% blended on a correctly specified join"
    note: Does not kill all calendar ideas worldwide. Does not prove mail lift.

  - claim: The proposed sequence improves response versus a defined alternative.
    population: SELL-1-eligible owner-occupied households in the pre-sold territory.
    baseline: Pre-registered assigned comparison (timed sequence vs specified alternative; not an observational purchase-month curve alone).
    primary_outcome: Completed inquiry rate.
    denominator: Households mailed (not pieces).
    window: One quarter; instrument scans and completions separately.
    result: "—"
    label: "[U]"
    exploratory: Response vs days-to-anniversary may be plotted; it is not the causal test.

  - claim: Responses are valuable to the buying agency.
    population: Delivered exclusive inquiries.
    baseline: That agency's existing acquisition channel.
    primary_outcome: Acceptance, contact, quote, bind, agency minutes, refunds.
    denominator: Accepted inquiries.
    window: Same quarter plus contracted disposition lag.
    result: "—"
    label: "[U]"

  - claim: The company is economically viable as seller and as a purchase for the agency.
    population: Pilot contract.
    baseline: Agency status-quo CAC; our fully loaded cost.
    primary_outcome: Seller contribution; buyer cost per accepted inquiry and per bind.
    denominator: Name units (households, pieces, responses, binds) separately.
    window: Quarter.
    result: "—"
    label: "[U]"
    note: "$3,500 base is customer revenue, not our spend budget. Use the low commission denominator until a signed schedule exists."

  - claim: The fleet can operate the loop at the requested authority's workload cap.
    population: Pilot loop.
    baseline: Documented manual hours to run the same loop.
    primary_outcome: Human minutes per accepted inquiry; fixed hours/week; exception time.
    denominator: Accepted inquiries; calendar weeks.
    window: Quarter.
    result: "—"
    label: "[U]"

falsification: A correct current-owner join below 50% blended kills THIS inference method on THAT book. Assigned comparison with inbound below the registered floor after one creative retest kills Model-3 promotion. A profitable base fee with poor buyer value is not KEEP for commercial expansion.

controls: Assigned household-level comparison required before the causal timing claim can KEEP. Observational SELL-1 curve is exploratory only.

minimum_sample: Instrument 1 — target 200 joined policies, report n unmatched. Mail causal test — sample rationale must be written before postage; 300 households is insufficient to decide 1.3% break-even (see pilot doc).
stopping_rules: Stop quoting Instrument 1 % until previous-owner join and future-scrub defects are closed. Stop mail if counsel blocks the advertising-exemption read.

budget:
  sunk: design-branch labor
  new_commitments: postage, certificates, data appends, counsel — Treasurer + Governor before commitment
  categories: [postage, certificates, property-data, counsel, labor]

change_control: New version if audience, creative family, buyer, timing rule, or pricing changes.

required_deliverables:
  - P0 instrument fixes and tests in InsuranceOS
  - Frozen inference definition (current-owner acquisition)
  - Event ledger kinds distinct from PACKET_GENERATED
  - Pre-registered comparison protocol
  - Seller and buyer P&L templates

authority_expiry: none until first grant
revocation: Failed Clock on consent binding; counsel veto; Treasurer halt
```

Finish ALMANAC's renewal-lead system and determine whether its targeting, outreach sequence and response experience produce economically attractive, exclusive leads that independent agencies purchase repeatedly. Validate the renewal proxy, repair the measurement and permission paths, conduct a pre-registered prospective pilot, and report seller economics, buyer outcomes and human workload. The fleet may develop implementation, creative and commercial proposals within this mission. Spending and external launch require the Governor's explicit authorization. Failed components receive specific verdicts; alternative businesses require separate promotion.

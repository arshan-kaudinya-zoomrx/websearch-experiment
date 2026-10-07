# Jev inspect: 20261006-183548__jev-jev_v3__on__20261003-181326__perplexity-pplx_fast__batch

Config `jev_v3` (per_link), select={"keep_threshold": 0.5, "max_keep": 10, "gates": {"on_target": 0.6, "evidence": 0.5}}. Reasons: {"kept": 348, "low_on_target": 262, "low_evidence": 30}. Answer means: {"on_target": 0.614, "evidence": 0.489}.

Legend: ✅ kept · ❌ dropped (reason) · `A` = mentions the anchor · scores are Jev's answers in [0, 1].

## q001

**Objective:** Tamuzimod safety findings and adverse events in Moderately to severely active ulcerative colitis Ulcerative Colitis  
**Target sent:** Tamuzimod · anchors ['Tamuzimod']

**q001-batch** `Tamuzimod long-term extension safety ulcerative colitis || Tamuzimod maintenance adverse events ulcerative colitis || Tamuzimod UEGW 2024 safety || Tamuzimod open-label extension adverse events` → kept 10/10, jev 796 ms

- ✅ **0.9145** [on_target=0.93 evidence=0.98] Ulcerative colitis, active severe - Drugs, Targets, Patents - Synapse — synapse.patsnap.com (#6) `A`
- ✅ **0.9016** [on_target=0.98 evidence=0.92] UEG Week 2024 - CONFERENCE REPORTPEER-REVIEWED — conferences.medicom-publishers.com (#2) `A`
- ✅ **0.8954** [on_target=0.92 evidence=0.97] Ulcerative colitis, active moderate - Drugs, Targets, Patents — synapse.patsnap.com (#9) `A`
- ✅ **0.8778** [on_target=0.99 evidence=0.89] VTX002 UEGW 2024 — ir.ventyxbio.com (#1) `A`
- ✅ **0.8256** [on_target=0.96 evidence=0.86] Sphingosine-1-Phosphate (S1P) Receptor Modulators for the ... - PMC — pmc.ncbi.nlm.nih.gov (#7) `A`
- ✅ **0.7284** [on_target=0.98 evidence=0.74] tamuzimod (VTX002) / Eli Lilly — delta.larvol.com (#5) `A`
- ✅ **0.6897** [on_target=0.99 evidence=0.70] Ventyx Biosciences Presents New 52-Week Results from the Phase ... — ir.ventyxbio.com (#3) `A`
- ✅ **0.6794** [on_target=0.98 evidence=0.69] Ventyx Biosciences' Tamuzimod Shows Promising Long-Term ... — trial.medpath.com (#10) `A`
- ✅ **0.6696** [on_target=0.98 evidence=0.68] Ventyx Biosciences' Tamuzimod Shows Promising Long-Term ... — trial.medpath.com (#8) `A`
- ✅ **0.511** [on_target=0.70 evidence=0.73] Silvio Danese - ScienceDirect.com — sciencedirect.com (#4) `A`

## q002 (competitor objective)

**Objective:** C. difficile Infection Episode: Receipt of SOC Antibacterial Therapy (Fidaxomicin, Vancomycin, Metronidazole) With Planned Duration 10–25 Days at Time of IMP Administration competing agents in the same mechanistic class as AZD5148, including Monoclonal Antibody targeting Clostridioides Difficile Toxin B TcdB  
**Target sent:** AZD5148 itself, or drugs competing with AZD5148: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['AZD5148']

**q002-batch** `AZD5148 competing anti-TcdB monoclonal antibodies Phase 2 2026 || AZD5148 TcdB antibody competitors licensing || AZD5148 RePreve comparator anti-toxin antibody || AZD5148 TcdB epitope binding mechanism || AZD5148 clinical pipeline TcdB antibody 2026` → kept 10/10, jev 796 ms

- ✅ **0.7825** [on_target=0.97 evidence=0.81] Ozmosi / AZD-5148 Drug Profile — pryzm.ozmosi.com (#8) `A`
- ✅ **0.7113** [on_target=0.97 evidence=0.73] Clinical Trials Appendix - Q1 2026 Results Update — astrazeneca.com (#3) `A`
- ✅ **0.7024** [on_target=0.98 evidence=0.72] Prevention of Recurrent C. Difficile Infection Study With AZD5148 Monoclonal Antibody (NCT07285213) — clinicaltrials.gg (#9) `A`
- ✅ **0.6944** [on_target=0.96 evidence=0.72] H1 and Q2 2026 Results Clinical Trials Appendix — astrazeneca.com (#4) `A`
- ✅ **0.6758** [on_target=0.97 evidence=0.70] Immune aspects of Clostridioides difficile infection and vaccine ... — pmc.ncbi.nlm.nih.gov (#7) `A`
- ✅ **0.6725** [on_target=0.97 evidence=0.69] Monoclonal Antibodies Targeting Bacterial Infections: A Broad ... — link.springer.com (#6) `A`
- ✅ **0.6496** [on_target=0.96 evidence=0.68] Pipeline — astrazeneca.com (#5) `A`
- ✅ **0.6402** [on_target=0.98 evidence=0.65] Monoclonal Antibodies Targeting Bacterial Infections: A Broad ... — link.springer.com (#10) `A`
- ✅ **0.6304** [on_target=0.98 evidence=0.64] The monoclonal antibody AZD5148 confers broad protection against ... — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.6076** [on_target=0.98 evidence=0.62] Epitope Conservation of AZD5148, a Broadly Neutralizing Anti-Toxin B Monoclonal Antibody, Among Dive — pmc.ncbi.nlm.nih.gov (#1) `A`

## q003 (competitor objective)

**Objective:** Distal Ulcerative Colitis competing agents in the same mechanistic class as RpoB Small Molecule  
**Target sent:** RpoB itself, or drugs competing with RpoB: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['RpoB']

**q003-batch** `Distal Ulcerative Colitis RpoB inhibitors pipeline || Distal Ulcerative Colitis RpoB competitors Phase 2 || Distal Ulcerative Colitis RpoB mechanism clinical trial` → ABSTAIN, jev 440 ms

- ❌ low_on_target **0.0665** [on_target=0.21 evidence=0.32] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0658** [on_target=0.21 evidence=0.31] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#4)
- ❌ low_on_target **0.0606** [on_target=0.18 evidence=0.34] Ulcerative Colitis - Gastroenterology - Merck Manuals — merckmanuals.com (#9)
- ❌ low_on_target **0.0582** [on_target=0.18 evidence=0.32] Reviewing treatments and outcomes in the evolving landscape of ulcerative colitis — tandfonline.com (#1)
- ❌ low_on_target **0.039** [on_target=0.15 evidence=0.26] Emerging Treatment Options in Mild to Moderate Ulcerative Colitis — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0299** [on_target=0.14 evidence=0.21] ECCO Guidelines on Therapeutics in Ulcerative Colitis ... — academic.oup.com (#5)
- ❌ low_on_target **0.0283** [on_target=0.10 evidence=0.28] What are the key players in the ulcerative colitis treatment ... — synapse.patsnap.com (#10)
- ❌ low_on_target **0.0223** [on_target=0.10 evidence=0.22] academic.oup.com · ecco-jcc · articleECCO Guidelines on Therapeutics in Ulcerative Colitis ... — academic.oup.com (#8)
- ❌ low_on_target **0.022** [on_target=0.11 evidence=0.20] The IBD Therapeutic Pipeline Is Primed to Produce — practicalgastro.com (#3)
- ❌ low_on_target **0.0091** [on_target=0.07 evidence=0.13] Ulcerative Colitis - 1,154 clinical trials — atlasbyauro.com (#6)

## q004 (competitor objective)

**Objective:** competing agents in the same mechanistic class for this indication MT501, Mirador Therapeutics, Crohn's Disease, Moderately to Severely Active by CDAI and SES-CD  
**Target sent:** MT501 itself, or drugs competing with MT501: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['MT501']

**q004-batch** `MT501 mechanism of action mechanistic class || MT501 Crohn's disease target pathway || MT501 inflammatory bowel disease competitors same mechanism` → kept 5/10, jev 723 ms

- ✅ **0.7146** [on_target=0.97 evidence=0.74] MT-501 - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#2) `A`
- ✅ **0.608** [on_target=0.96 evidence=0.63] MT-501 for Inflammatory Bowel Disease (ASCEND-IBD Trial) — withpower.com (#3) `A`
- ✅ **0.5917** [on_target=0.97 evidence=0.61] MT-501 - AssetMemo — assetmemo.bio (#5) `A`
- ✅ **0.517** [on_target=0.94 evidence=0.55] Ozmosi / MT-501 Drug Profile — pryzm.ozmosi.com (#10) `A`
- ✅ **0.3922** [on_target=0.74 evidence=0.53] Advancing therapeutic frontiers: a pipeline of novel drugs for luminal and perianal Crohn's disease  — journals.sagepub.com (#7)
- ❌ low_evidence **0.3084** [on_target=0.74 evidence=0.42] Inflammatory Bowel Competitive Landscape Analysis 2026 / Eureka — eureka.patsnap.com (#4)
- ❌ low_evidence **0.2788** [on_target=0.74 evidence=0.38] Competitor Landscape — marketintelo.com (#8)
- ❌ low_evidence **0.2384** [on_target=0.65 evidence=0.37] Inflammatory bowel disease treatment: Mechanisms ... — spandidos-publications.com (#1)
- ❌ low_on_target **0.1785** [on_target=0.52 evidence=0.34] Understanding the therapeutic toolkit for inflammatory bowel disease — s29.q4cdn.com (#9)
- ❌ low_on_target **0.1448** [on_target=0.43 evidence=0.34] Pharmacological Therapy in Inflammatory Bowel Diseases — pmc.ncbi.nlm.nih.gov (#6)

## q005

**Objective:** SOR102 safety findings and adverse events in Crohn's Disease Ulcerative Colitis  
**Target sent:** SOR102 / SOR102-101 · anchors ['SOR102', 'SOR102-101']

**q005-batch** `SOR102 Crohn's disease safety adverse events || SOR102-101 registry identifier safety || SOR102 ulcerative colitis individual adverse events infections deaths || SOR102 Grade 3 adverse events 810 mg || SOR102 900 mg 42-day safety results` → kept 10/10, jev 367 ms

- ✅ **0.9506** [on_target=0.97 evidence=0.98] PHASE 1B STUDY OF SOR102, A NOVEL, ORALLY ... — eposters.ddw.org (#2) `A`
- ✅ **0.9506** [on_target=0.97 evidence=0.98] Sorriso Pharmaceuticals, Inc. - Drug pipelines, Patents, Clinical trials — synapse-patsnap-com.libproxy1.nus.edu.sg (#5) `A`
- ✅ **0.9441** [on_target=0.97 evidence=0.97] Safety and pharmacokinetics of SOR102, an oral bispecific ... — pure.amsterdamumc.nl (#7) `A`
- ✅ **0.944** [on_target=0.96 evidence=0.98] Safely targeting combination TNF and IL-23 using a gut-restricted ... — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.9408** [on_target=0.98 evidence=0.96] PowerPoint Presentation — sorrisopharma.com (#10) `A`
- ✅ **0.9376** [on_target=0.96 evidence=0.98] SOR-102 - Drug Targets, Indications, Patents — synapse.patsnap.com (#9) `A`
- ✅ **0.9344** [on_target=0.97 evidence=0.96] Oral Administration of SOR102 Delivers Anti-TNF/IL-23 ... — sorrisopharma.com (#3) `A`
- ✅ **0.9118** [on_target=0.97 evidence=0.94] PowerPoint-Präsentation — sorrisopharma.com (#4) `A`
- ✅ **0.8698** [on_target=0.97 evidence=0.90] Journal Scan_Jan 2026 — ibdenc.org (#6) `A`
- ✅ **0.8102** [on_target=0.98 evidence=0.83] A Clinical Trial to Assess the Safety of SOR102 in Healthy Participants and Patients With Ulcerative — ichgcp.net (#8) `A`

## q006 (competitor objective)

**Objective:** Moderately to Severely Active Crohn's Disease Moderately to Severely Active Crohn’s Disease Refractory to Systemic Therapies Moderately to Severely Active Ulcerative Colitis Refractory to Systemic Therapies Moderately to Severely Active Ulcerative Colitis with inadequate response, loss of response, or intolerance to ≥1 biologic or novel oral with biologic-like activity competing agents in the same mechanistic class as JNJ-4804 Co Antibody Therapy, including Antibody Cocktail Monoclonal Antibody and IL-23 IL23A TNF-α Tumor Necrosis Factor Alpha therapies  
**Target sent:** JNJ-4804 itself, or drugs competing with JNJ-4804: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['JNJ-4804']

**q006-batch** `JNJ-4804 guselkumab golimumab IL-23 TNF-α competitors IBD || JNJ-4804 IL-23 TNF-α dual antibody competing agents IBD || JNJ-4804 same mechanistic class IBD pipeline || JNJ-4804 competing IL-23 TNF-α antibody Crohn's disease ulcerative colitis` → kept 9/10, jev 507 ms

- ✅ **0.9669** [on_target=0.99 evidence=0.98] News Details - JNJ Investor Relations — investor.jnj.com (#4) `A`
- ✅ **0.957** [on_target=0.99 evidence=0.97] JNJ-4804 demonstrated highest rates of clinical ... — jnj.com (#1) `A`
- ✅ **0.9537** [on_target=0.99 evidence=0.96] Johnson & Johnson investigational co-antibody therapy JNJ-4804 ... — investor.jnj.com (#2) `A`
- ✅ **0.9146** [on_target=0.98 evidence=0.93] ‘Strikingly better’: Co-antibody combination tops golimumab ... — healio.com (#5) `A`
- ✅ **0.8217** [on_target=0.99 evidence=0.83] J&J pushes dual-antibody IBD therapy into Phase 3 ... — biospace.com (#7) `A`
- ✅ **0.7872** [on_target=0.98 evidence=0.80] EFFICACY AND SAFETY OF THE FIRST CO-ANTIBODY THERAPY, JNJ ... — jnjmedicalconnect.com (#3) `A`
- ✅ **0.7774** [on_target=0.98 evidence=0.79] efficacy and safety of the first co-antibody therapy, jnj- ... — jnjmedicalconnect.com (#6) `A`
- ✅ **0.7695** [on_target=0.97 evidence=0.79] IBD治疗领域存在未满足的需求，关注新靶点 — pdf.dfcfw.com (#10) `A`
- ✅ **0.582** [on_target=0.86 evidence=0.68] Landscape of new drugs and targets in inflammatory bowel disease — onlinelibrary.wiley.com (#9)
- ❌ low_evidence **0.4868** [on_target=0.98 evidence=0.50] Inflammatory Bowel Disease Market to Experience Strong ... — prnewswire.com (#8) `A`

## q007 (competitor objective)

**Objective:** Ulcerative Colitis competing agents in the same mechanistic class as FN1 IL-10RB IL10RA Interleukin-10 Antibody-Cytokine Conjugate Fusion Protein Biologic  
**Target sent:** Dekavil itself, or drugs competing with Dekavil: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['Dekavil']

**q007-batch** `Dekavil ulcerative colitis IL-10 fusion competitors || Dekavil ulcerative colitis antibody-cytokine fusion pipeline || Dekavil PF-06687234 sponsor ownership || Dekavil ulcerative colitis current development status` → kept 8/10, jev 656 ms

- ✅ **0.6661** [on_target=0.97 evidence=0.69] Dekavil - Drug Targets, Indications, Patents - Synapse — synapse.patsnap.com (#2) `A`
- ✅ **0.6564** [on_target=0.97 evidence=0.68] Dekavil (F8-IL10) / Pfizer, Philogen — delta.larvol.com (#5) `A`
- ✅ **0.646** [on_target=0.95 evidence=0.68] Targeting IL-10 Family Cytokines for the Treatment of Human ... — pmc.ncbi.nlm.nih.gov (#8) `A`
- ✅ **0.64** [on_target=0.96 evidence=0.67] a phase 2a, randomized, double-blind, placebo-controlled — cdn.clinicaltrials.gov (#6) `A`
- ✅ **0.6239** [on_target=0.95 evidence=0.66] Inflammatory Bowel Disease: Updates on Molecular ... — pmc.ncbi.nlm.nih.gov (#3) `A`
- ✅ **0.5568** [on_target=0.96 evidence=0.58] Clinical trials — clinicaltrialsregister.eu (#1) `A`
- ✅ **0.5452** [on_target=0.87 evidence=0.63] Research advances of vasoactive intestinal peptide in the ... - PMC — pmc.ncbi.nlm.nih.gov (#9) `A`
- ✅ **0.5373** [on_target=0.81 evidence=0.66] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#7)
- ❌ low_on_target **0.3364** [on_target=0.58 evidence=0.58] Immunology & Inflammation: Autoimmune Pipeline & Trials - Pfizer — pfizer.com (#10) `A`
- ❌ low_on_target **0.1628** [on_target=0.33 evidence=0.49] Press Release: Sanofi and Teva's duvakitug phase 2b ... — sanofi.com (#4)

## q008 (competitor objective)

**Objective:** Clostridioides Difficile Colitis competing agents in the same mechanistic class as LMN-201, including Antibody Fragment Enzyme Biological Biologic Cocktail and Clostridioides Difficile Toxin B TcdB therapies  
**Target sent:** LMN-201 itself, or drugs competing with LMN-201: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['LMN-201']

**q008-batch** `LMN-201 TcdB antitoxin competitors Phase 2 clinical || LMN-201 PA-41 development phase || LMN-201 BL5-6.2 clinical development || LMN-201 AZD5148 clinical trial regulatory status || LMN-201 bezlotoxumab withdrawal current status` → kept 10/10, jev 437 ms

- ✅ **0.7566** [on_target=0.97 evidence=0.78] LMN-201 Preliminary Cohort in Repreve Trial — lumen.bio (#3) `A`
- ✅ **0.7469** [on_target=0.97 evidence=0.77] LMN-201 / Lumen Bio - Larvol Delta — delta.larvol.com (#8) `A`
- ✅ **0.7232** [on_target=0.96 evidence=0.75] LMN-201 - MedPath — trial.medpath.com (#10) `A`
- ✅ **0.7016** [on_target=0.97 evidence=0.72] LMN-201 for Prevention of C. Difficile Infection Recurrence — med.agiltrace.com (#4) `A`
- ✅ **0.6971** [on_target=0.89 evidence=0.78] Prevention of Recurrent C. Difficile Infection Study With AZD5148 Monoclonal Antibody — med.agiltrace.com (#1) `A`
- ✅ **0.6944** [on_target=0.96 evidence=0.72] Clostridium Difficile Infections Pipeline 2026: FDA Updates, — openpr.com (#7) `A`
- ✅ **0.6592** [on_target=0.96 evidence=0.69] LMN-201 for Prevention of C. Difficile ... / NCT05330182 ... — deltatrials.com (#6) `A`
- ✅ **0.624** [on_target=0.96 evidence=0.65] LMN-201 for Prevention of C. Difficile Infection Recurrence — clinicaltrials.gov (#2) `A`
- ✅ **0.532** [on_target=0.95 evidence=0.56] Clinical Trials Using Clostridioides difficile Toxin B-binding proteins ... — cancer.gov (#5) `A`
- ✅ **0.5295** [on_target=0.94 evidence=0.56] C. Difficile Infection Clinical Trials — mayo.edu (#9) `A`

## q009 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as CHRM1 CHRM3 CHRM4 CHRM5 Small Molecule  
**Target sent:** Dicyclomine itself, or drugs competing with Dicyclomine: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['Dicyclomine']

**q009-batch** `Dicyclomine inflammatory bowel disease muscarinic competitors || Dicyclomine IBD CHRM pipeline || Dicyclomine inflammatory bowel disease clinical development` → kept 10/10, jev 601 ms

- ✅ **0.6816** [on_target=0.96 evidence=0.71] [PDF] Phase II-(VI) Antispasmodic & antiulcer drugs (cyclopentolate ... — api.upums.ac.in (#10) `A`
- ✅ **0.672** [on_target=0.96 evidence=0.70] Antispasmodics for Chronic Abdominal Pain: Analysis of North ... — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.6368** [on_target=0.96 evidence=0.66] Pain management in patients with inflammatory bowel disease — pmc.ncbi.nlm.nih.gov (#4) `A`
- ✅ **0.6305** [on_target=0.97 evidence=0.65] Antispasmodics and IBD — ibdrelief.com (#7) `A`
- ✅ **0.6016** [on_target=0.96 evidence=0.63] Pharmacology — go.drugbank.com (#8) `A`
- ✅ **0.5888** [on_target=0.96 evidence=0.61] The Impact of Antispasmodic Use on Abdominal Pain and ... — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.576** [on_target=0.96 evidence=0.60] https://nctr-crs.fda.gov/fdalabel/services/spl/ ... — nctr-crs.fda.gov (#6) `A`
- ✅ **0.5446** [on_target=0.95 evidence=0.57] Dicyclomine 20mg — dailymed.nlm.nih.gov (#3) `A`
- ✅ **0.5182** [on_target=0.92 evidence=0.56] efficacy and safety of hyoscyamine, dicyclomine, and desipramine in ... — academic.oup.com (#2) `A`
- ✅ **0.4906** [on_target=0.92 evidence=0.53] www.droracle.ai · articles · 856897What is the most appropriate over‑the‑counter treatment for ... — droracle.ai (#9) `A`

## q010 (competitor objective)

**Objective:** competing agents in the same mechanistic class for this indication LY4395089, Eli Lilly & Company, Crohn''s Disease  
**Target sent:** LY4395089 itself, or drugs competing with LY4395089: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['LY4395089']

**q010-batch** `LY4395089 mechanism target Crohn’s disease || LY4395089 competing agents Crohn’s disease same mechanism` → kept 10/10, jev 369 ms

- ✅ **0.8984** [on_target=0.98 evidence=0.92] LY4395089 - Crohn Disease / Phase 2 / Eli Lilly and ... — biopharmawatch.com (#2) `A`
- ✅ **0.735** [on_target=0.98 evidence=0.75] Crohns' Disease Clinical Trial Drug Development Pipeline ... — barchart.com (#6) `A`
- ✅ **0.7146** [on_target=0.97 evidence=0.74] Crohns' Disease Pipeline Appears Robust With 90+ Key Pharma ... — barchart.com (#3) `A`
- ✅ **0.7146** [on_target=0.97 evidence=0.74] Multiple Drugs for Ulcerative Colitis or Crohn's Disease — withpower.com (#5) `A`
- ✅ **0.7113** [on_target=0.97 evidence=0.73] Study Details / NCT07483099 / ClinicalTrials.gov - ClinicalTrials.gov — clinicaltrials.gov (#4) `A`
- ✅ **0.6664** [on_target=0.98 evidence=0.68] A clinical research study for people with moderately to ... — trials.lilly.com (#9) `A`
- ✅ **0.6402** [on_target=0.97 evidence=0.66] LY4395089 + Mirikizumab for Crohn's Disease - WithPower — withpower.com (#8) `A`
- ✅ **0.6079** [on_target=0.97 evidence=0.63] Find Lilly Clinical Trials — trials.lilly.com (#10) `A`
- ✅ **0.4909** [on_target=0.95 evidence=0.52] LY-4395089 - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#1) `A`
- ✅ **0.4331** [on_target=0.61 evidence=0.71] Ontamalimab (Ph 3) - Takeda Pharmaceutical Company Limited — biopharmawatch.com (#7) `A`

## q011 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as Small Molecule targeting ITGA4 ITGB7 Integrin Alpha-4 Beta-7  
**Target sent:** α4β7 Inhibitor / α4β7 itself, or drugs competing with α4β7 Inhibitor / α4β7: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['α4β7 Inhibitor', 'α4β7']

**q011-batch** `α4β7 Inhibitor etrolizumab mechanism IBD || α4β7 Inhibitor vedolizumab current development status 2026 || α4β7 Inhibitor abrilumab current status IBD || α4β7 Inhibitor Phase 2 Phase 3 Crohn's disease competitors || α4β7 Inhibitor AJM300 natalizumab class comparison` → kept 10/10, jev 384 ms

- ✅ **0.8126** [on_target=0.92 evidence=0.88] 2.4. Integrin αeβ7 (cd103) — pmc.ncbi.nlm.nih.gov (#7) `A`
- ✅ **0.784** [on_target=0.96 evidence=0.82] Anti-Integrins for the Treatment of Inflammatory Bowel ... — tandfonline.com (#8) `A`
- ✅ **0.7238** [on_target=0.94 evidence=0.77] Next generation therapeutics for inflammatory bowel disease — pmc.ncbi.nlm.nih.gov (#10) `A`
- ✅ **0.6586** [on_target=0.95 evidence=0.69] Targeting T-cell integrins in autoimmune and inflammatory diseases — academic.oup.com (#9) `A`
- ✅ **0.6549** [on_target=0.94 evidence=0.70] Etrolizumab — go.drugbank.com (#3) `A`
- ✅ **0.6231** [on_target=0.93 evidence=0.67] Research progress in molecular targeted therapy for ... — link.springer.com (#4) `A`
- ✅ **0.6107** [on_target=0.93 evidence=0.66] Cellular Mechanisms of Etrolizumab Treatment in Inflammatory ... — pmc.ncbi.nlm.nih.gov (#6) `A`
- ✅ **0.6** [on_target=0.90 evidence=0.67] Research progress in molecular targeted therapy for inflammatory ... — link.springer.com (#1) `A`
- ✅ **0.5703** [on_target=0.91 evidence=0.63] A randomised phase I study of etrolizumab (rhuMAb β7) in ... — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.543** [on_target=0.91 evidence=0.60] Review article: nonclinical and clinical pharmacology ... - PMC — pmc.ncbi.nlm.nih.gov (#5) `A`

## q012

**Objective:** Lenvatinib + Nofazinlimab pivotal, registrational, or Phase 3 trial in Unresectable or Metastatic Hepatocellular Carcinoma: planned or initiated status and expected start date  
**Target sent:** Lenvatinib + Nofazinlimab NCT04194775 / Lenvatinib / Nofazinlimab / NCT04194775 · anchors ['Lenvatinib + Nofazinlimab NCT04194775', 'Lenvatinib', 'Nofazinlimab', 'NCT04194775']

**q012-batch** `Lenvatinib + Nofazinlimab NCT04194775 first patient enrollment date || Lenvatinib + Nofazinlimab NCT04194775 current trial status` → kept 10/10, jev 435 ms

- ✅ **0.9734** [on_target=0.98 evidence=0.99] A Study of Nofazinlimab (CS1003) in… · NCT04194775 · OnCo — onco.cc (#5) `A`
- ✅ **0.9734** [on_target=0.98 evidence=0.99] A Study of Nofazinlimab (CS1003) in Subjects With ... — guidelinecentral.com (#10) `A`
- ✅ **0.9506** [on_target=0.98 evidence=0.97] A Study of Nofazinlimab (CS1003) in... / Clinical Trial — trial.medpath.com (#1) `A`
- ✅ **0.8192** [on_target=0.96 evidence=0.85] Nofazinlimab - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#8) `A`
- ✅ **0.7695** [on_target=0.97 evidence=0.79] A Study of Nofazinlimab (CS1003) in Subjects With Advanced Hepatocellular Carcinoma — clinicaltrials.gov (#2) `A`
- ✅ **0.6768** [on_target=0.79 evidence=0.86] A Study of Nofazinlimab (CS1003) in Subjects With Advanced Hepatocellular Carcinoma — cancerindex.io (#6) `A`
- ✅ **0.6572** [on_target=0.93 evidence=0.71] Current status of the cost burden of first-line systemic treatment for ... — academic.oup.com (#9) `A`
- ✅ **0.6552** [on_target=0.84 evidence=0.78] Liver Epithelial Neoplasm — cancerindex.io (#3) `A`
- ✅ **0.6068** [on_target=0.82 evidence=0.74] A Study to Evaluate MIV-818 in Patients With Liver Cancer Manifestations — med.agiltrace.com (#4) `A`
- ✅ **0.4692** [on_target=0.68 evidence=0.69] Lenvatinib for the Treatment of Recurrent Hepatocellular Carcinoma After Liver Transplant — med.agiltrace.com (#7) `A`

## q013

**Objective:** SD-133 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** SD-133 · anchors ['SD-133']

**q013-batch** `SD-133 pancreatic ductal adenocarcinoma monotherapy xenograft TGI || SD-133 tumour regression pancreatic cancer animal model` → ABSTAIN, jev 341 ms

- ❌ low_on_target **0.0539** [on_target=0.16 evidence=0.34] Pancreatic ductal adenocarcinoma: Treatment hurdles, tumor ... — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0291** [on_target=0.09 evidence=0.32] Immune therapies in pancreatic ductal adenocarcinoma: Where are we now? — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0285** [on_target=0.09 evidence=0.32] Radioimmunotherapy of Pancreatic Ductal Adenocarcinoma: A Review of the Current Status of Literature — mdpi.com (#4)
- ❌ low_on_target **0.0276** [on_target=0.12 evidence=0.23] Full article: Next-generation therapies for pancreatic cancer — tandfonline.com (#1)
- ❌ low_on_target **0.0059** [on_target=0.04 evidence=0.15] Management of pancreatic ductal adenocarcinoma (PDAC) - OAText — oatext.com (#8)
- ❌ low_on_target **0.0043** [on_target=0.05 evidence=0.09] Pancreatic Ductal Adenocarcinoma in the Era of Precision ... — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0041** [on_target=0.02 evidence=0.20] Pathogenesis of Pancreatic Cancer: Lessons from Animal ... — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0037** [on_target=0.04 evidence=0.09] Pancreatic Ductal Adenocarcinoma in the Era of Precision Medicine — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0031** [on_target=0.02 evidence=0.15] Modeling pancreatic cancer in mice for experimental therapeutics — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0** [on_target=0.09 evidence=0.00] Detail - OpenURL Connection — openurl.ebsco.com (#2)

## q014

**Objective:** Sirpiglenastat in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** Sirpiglenastat / DRP-104 · anchors ['Sirpiglenastat', 'DRP-104']

**q014-batch** `Sirpiglenastat PDAC monotherapy TGI xenograft || DRP-104 pancreatic cancer single-agent tumour regression || Sirpiglenastat pancreatic PDX monotherapy tumour volume || DRP-104 PDAC xenograft dose response || Sirpiglenastat pancreatic cancer in vivo monotherapy` → kept 9/10, jev 358 ms

- ✅ **0.8613** [on_target=0.99 evidence=0.87] Targeting pancreatic cancer metabolic dependencies through glutamine antagonism — nature.com (#1) `A`
- ✅ **0.7695** [on_target=0.95 evidence=0.81] Discovery of DRP-104, a tumor-targeted metabolic inhibitor prodrug - PubMed — pubmed.ncbi.nlm.nih.gov (#3) `A`
- ✅ **0.7425** [on_target=0.99 evidence=0.75] Sirpiglenastat (DRP-104) Induces Antitumor Efficacy through Direct ... — ouci.dntb.gov.ua (#5) `A`
- ✅ **0.699** [on_target=0.98 evidence=0.71] Metabolic plasticity in pancreatic ductal adenocarcinoma ... — link.springer.com (#7) `A`
- ✅ **0.6624** [on_target=0.96 evidence=0.69] Discovery of DRP-104, a tumor-targeted metabolic inhibitor prodrug — pmc.ncbi.nlm.nih.gov (#4) `A`
- ✅ **0.65** [on_target=0.98 evidence=0.66] Sirpiglenastat (DRP-104) / Glutamine Antagonist — targetmol.com (#2) `A`
- ✅ **0.65** [on_target=0.98 evidence=0.66] Dracen Pharmaceuticals announces publication in Molecular Cancer Therapeutics — prweb.com (#9) `A`
- ✅ **0.6111** [on_target=0.97 evidence=0.63] Broad glutamine pathway inhibition by DRP-104 results in ... — dracenpharma.com (#6) `A`
- ✅ **0.5676** [on_target=0.86 evidence=0.66] RMC-7977 / Revolution Medicines - Larvol Delta — delta.larvol.com (#8) `A`
- ❌ low_on_target **0.0** [on_target=0.07 evidence=0.00] PDC000198 - Proteomic Data Commons - National Cancer Institute — proteomic.datacommons.cancer.gov (#10)

## q015

**Objective:** GFH375/VS-7375 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in KRAS G12D-Mutated/MTAP-Deleted Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** GFH375 VS-7375 / GFH375 / VS-7375 · anchors ['GFH375 VS-7375', 'GFH375', 'VS-7375']

**q015-batch** `GFH375 VS-7375 quantitative TGI KP4 PDAC monotherapy || GFH375 VS-7375 MTAP-deleted KP4 monotherapy tumour regression || GFH375 VS-7375 MTAP-deleted pancreatic xenograft single-agent TGI || GFH375 VS-7375 AsPC-1 Panc 04.03 monotherapy tumour volume data` → kept 10/10, jev 361 ms

- ✅ **0.7154** [on_target=0.98 evidence=0.73] VS-7375 (GFH375): An oral, selective KRAS G12D (ON/ ... — verastem.com (#7) `A`
- ✅ **0.6794** [on_target=0.98 evidence=0.69] [PDF] VS-7375: An oral, selective KRAS G12D dual ON/OFF inhibitor with ... — verastem.com (#5) `A`
- ✅ **0.6725** [on_target=0.97 evidence=0.69] Selectivity over HUVEC (P value not updated) - verastem.com — verastem.com (#1) `A`
- ✅ **0.648** [on_target=0.90 evidence=0.72] [PDF] Verastem Oncology Announces Late Breaking and Regular ... — investor.verastem.com (#8) `A`
- ✅ **0.6455** [on_target=0.94 evidence=0.69] Selectivity over HUVEC （P value not updated) — verastem.com (#2) `A`
- ✅ **0.6262** [on_target=0.93 evidence=0.67] Resources / Verastem, Inc. — verastem.com (#4) `A`
- ✅ **0.5949** [on_target=0.97 evidence=0.61] Pipeline / Verastem, Inc. — verastem.com (#10) `A`
- ✅ **0.5664** [on_target=0.96 evidence=0.59] Untitled — sec.gov (#9) `A`
- ✅ **0.546** [on_target=0.90 evidence=0.61] [PDF] GenFleet Therapeutics (Shanghai) Inc. 勁方醫藥科技(上海)股份有限 ... — www1.hkexnews.hk (#6) `A`
- ✅ **0.4731** [on_target=0.94 evidence=0.50] GFH375/VS-7375 Program Update — genfleet.com (#3) `A`

## q016

**Objective:** PLM-103 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic ductal adenocarcinoma (PDAC) animal models  
**Target sent:** PLM-103 · anchors ['PLM-103']

**q016-batch** `PLM-103 PDAC xenograft monotherapy tumour regression TGI` → ABSTAIN, jev 399 ms

- ❌ low_evidence **0.0279** [on_target=0.93 evidence=0.03] PLM-103 - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#9) `A`
- ❌ low_on_target **0.0206** [on_target=0.56 evidence=0.04] Evaluation of the safety, pharmacokinetics, and antitumor activity of ... — sciencedirect.com (#7)
- ❌ low_on_target **0.0069** [on_target=0.03 evidence=0.23] Patient Derived Xenograft Models: An Emerging Platform for ... — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0048** [on_target=0.16 evidence=0.03] A potential therapeutic target for pancreatic ductal adenocarcinoma — sciencedirect.com (#8)
- ❌ low_on_target **0.0032** [on_target=0.02 evidence=0.16] Biomimetic Tumour Model Systems for Pancreatic Ductal ... — research-portal.uu.nl (#10)
- ❌ low_on_target **0.002** [on_target=0.12 evidence=0.02] OpenLB Open Library of Bioscience — ngdc.cncb.ac.cn (#6)
- ❌ low_on_target **0.0005** [on_target=0.07 evidence=0.01] CCDI Hub — moleculartargets.ccdi.cancer.gov (#1)
- ❌ low_on_target **0.0** [on_target=0.04 evidence=0.00] Cloudflare — aacrjournals.org (#2)
- ❌ low_on_target **0.0** [on_target=0.08 evidence=0.00] Page not found — medschool.cuanschutz.edu (#4)
- ❌ low_on_target **0.0** [on_target=0.05 evidence=0.00] {{ngMeta['og:title']}} — bio.tools (#5)

## q017

**Objective:** SW-682 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Head and Neck Squamous Cell Carcinoma animal models  
**Target sent:** SW-682 · anchors ['SW-682']

**q017-batch** `SW-682 CAL-33 SCC-25 xenograft tumour growth inhibition monotherapy || SW-682 HNSCC xenograft tumour regression monotherapy || SW-682 CAL-33 SCC-25 tumour volume TGI` → kept 8/10, jev 371 ms

- ✅ **0.8362** [on_target=0.98 evidence=0.85] Targeting YAP/TAZ-TEAD signaling as a therapeutic approach in ... — pmc.ncbi.nlm.nih.gov (#4) `A`
- ✅ **0.7612** [on_target=0.98 evidence=0.78] Targeting TEAD in cancer - PMC - NIH — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.6828** [on_target=0.98 evidence=0.70] SW-682 - Drug Targets, Indications, Patents — synapse.patsnap.com (#6) `A`
- ✅ **0.6688** [on_target=0.96 evidence=0.70] Springworks Therapeutics, Inc. - Drug pipelines, Patents ... — synapse.patsnap.com (#8) `A`
- ✅ **0.6566** [on_target=0.98 evidence=0.67] SW-682 / EMD Serono — delta.larvol.com (#2) `A`
- ✅ **0.6336** [on_target=0.96 evidence=0.66] [PDF] SW-682: a novel TEAD inhibitor for the treatment of cancers bearing ... — springworkstx.com (#3) `A`
- ✅ **0.6334** [on_target=0.95 evidence=0.67] Genigraphics Research Poster Template 42x72 — springworkstx.com (#1) `A`
- ✅ **0.6273** [on_target=0.97 evidence=0.65] GEO Accession viewer — ncbi.nlm.nih.gov (#9) `A`
- ❌ low_on_target **0.0037** [on_target=0.04 evidence=0.09] Patient-Derived Xenograft and Organoid Models for Precision Medicine Targeting of the Tumour Microen — mdpi.com (#10)
- ❌ low_on_target **0.0002** [on_target=0.05 evidence=0.00] CCDI Hub — moleculartargets.ccdi.cancer.gov (#7)

## q018

**Objective:** SPR2015 in vivo animal models and results: cell-line xenograft CDX, patient-derived xenograft PDX, syngeneic, orthotopic, or genetically engineered models  
**Target sent:** SPR2015 · anchors ['SPR2015']

**q018-batch** `SPR2015 HNSCC in vivo xenograft || SPR2015 PDAC patient-derived xenograft || SPR2015 PDAC syngeneic model || SPR2015 PDAC genetically engineered mouse model || SPR2015 HPAC AsPC-1 tumour volume percentage inhibition` → kept 5/10, jev 378 ms

- ✅ **0.9376** [on_target=0.98 evidence=0.96] Merck, SciBrunch Launch Up-to-$2.13B Collaboration ... — genengnews.com (#8) `A`
- ✅ **0.8116** [on_target=0.97 evidence=0.84] KRAS G12D Inhibitor's $2.13B Deal Tests Cross-Border Tech Transfer — pharmtech.com (#4) `A`
- ✅ **0.748** [on_target=0.98 evidence=0.76] MSD takes a $400m bite of SciBrunch's KRAS drug — pharmaphorum.com (#2) `A`
- ✅ **0.7469** [on_target=0.97 evidence=0.77] Merck Licenses Preclinical KRAS G12D Inhibitor from SciBrunch — pharmexec.com (#5) `A`
- ✅ **0.7056** [on_target=0.98 evidence=0.72] Merck Enters into Exclusive Global License Agreement ... — businesswire.com (#1) `A`
- ❌ low_on_target **0.0572** [on_target=0.11 evidence=0.52] Genetically Engineered Mouse Models of Pancreatic Cancer — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.045** [on_target=0.10 evidence=0.45] Mouse Models of Pancreatic Ductal Adenocarcinoma — 2024.sci-hub.se (#3)
- ❌ low_on_target **0.0261** [on_target=0.07 evidence=0.37] Genetically engineered mouse models of pancreatic ... - PMC — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0228** [on_target=0.06 evidence=0.38] Current methods in mouse models of pancreatic cancer — mdanderson.elsevierpure.com (#6)
- ❌ low_on_target **0.0023** [on_target=0.17 evidence=0.01] CCDI Hub — moleculartargets.ccdi.cancer.gov (#7)

## q019

**Objective:** Innovent Biologics Inc. descriptions of IBI-3001's advantage over existing treatments for Head and Neck Squamous Cell Carcinoma in investor materials, earnings calls, investor day presentations, and press releases  
**Target sent:** IBI-3001 · anchors ['IBI-3001']

**q019-batch** `IBI-3001 HNSCC investor presentation treatment advantage || IBI3001 recurrent metastatic HNSCC Innovent press release || IBI3001 HNSCC first-line standard of care comparison` → kept 5/10, jev 391 ms

- ✅ **0.5859** [on_target=0.95 evidence=0.62] Press Release — en.innoventbio.com (#5) `A`
- ✅ **0.5852** [on_target=0.97 evidence=0.60] Takeda Announces Oncology Partnership with Innovent — takeda.com (#1) `A`
- ✅ **0.5852** [on_target=0.97 evidence=0.60] IBI3001 / Innovent Biologics, Takeda, Fortvita ... — delta.larvol.com (#4) `A`
- ✅ **0.5609** [on_target=0.94 evidence=0.60] Press Release — en.innoventbio.com (#2) `A`
- ✅ **0.5363** [on_target=0.93 evidence=0.58] Innovent to Present New Clinical Data of Next-gen IO and ... — prnewswire.com (#3) `A`
- ❌ low_evidence **0.404** [on_target=0.83 evidence=0.49] 信達生物製藥 INNOVENT BIOLOGICS, INC. - hkexnews.hk — www1.hkexnews.hk (#8) `A`
- ❌ low_evidence **0.3705** [on_target=0.95 evidence=0.39] Takeda's Strategic Partnership with Innovent Closes — takeda.com (#9) `A`
- ❌ low_on_target **0.0119** [on_target=0.04 evidence=0.30] Head and Neck Squamous Cell Carcinoma — pro.boehringer-ingelheim.com (#10)
- ❌ low_on_target **0.0027** [on_target=0.05 evidence=0.05] Innovent Bio (1801.HK): Innovent Bio's 6 innovative drugs have positive TCE data for new medical ins — news.futunn.com (#7)
- ❌ low_on_target **0.0003** [on_target=0.03 evidence=0.01] Innovent — en.innoventbio.com (#6)

## q020 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as JTO2, including Monoclonal Antibody and CXCL10 therapies  
**Target sent:** JTO2 itself, or drugs competing with JTO2: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['JTO2']

**q020-batch** `JTO2 CXCL10 inflammatory bowel disease competitors || JTO2 anti-CXCL10 monoclonal antibody IBD pipeline || JTO2 CXCL10 clinical trial inflammatory bowel disease` → kept 5/10, jev 565 ms

- ✅ **0.6912** [on_target=0.96 evidence=0.72] Delving into the Latest Updates on JT-02(Jyant Technologies) with Synapse — synapse.patsnap.com (#1)
- ✅ **0.6111** [on_target=0.95 evidence=0.64] Product Pipeline Summary — jyanttech.com (#6)
- ✅ **0.6026** [on_target=0.80 evidence=0.75] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#3)
- ✅ **0.5486** [on_target=0.78 evidence=0.70] Cell Trafficking Interference in Inflammatory Bowel Disease — pmc.ncbi.nlm.nih.gov (#2)
- ✅ **0.448** [on_target=0.60 evidence=0.75] Targeting Immune Cell Trafficking – Insights From Research Models ... — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_evidence **0.2599** [on_target=0.69 evidence=0.38] Optimising Monoclonal Antibody Therapies for Inflammatory Bowel ... — dovepress.com (#7)
- ❌ low_on_target **0.1571** [on_target=0.38 evidence=0.41] Landscape of new drugs and targets in inflammatory bowel disease — onlinelibrary.wiley.com (#10)
- ❌ low_on_target **0.144** [on_target=0.45 evidence=0.32] UCSF Inflammatory Bowel Disease Clinical Trials for 2026 ... — clinicaltrials.ucsf.edu (#8)
- ❌ low_on_target **0.0012** [on_target=0.06 evidence=0.02] Clinical Trials / Jill Roberts Center for Inflammatory Bowel ... — jillrobertsibdcenter.weillcornell.org (#9)
- ❌ low_on_target **0.0** [on_target=0.02 evidence=0.00] Cloudflare — thelancet.com (#5)

## q021 (competitor objective)

**Objective:** Crohn's Disease Ulcerative Colitis competing agents with the same mechanistic class as S1PR S1PR1 Sphingosine-1-phosphate receptor, including Small Molecule  
**Target sent:** Mocravimod itself, or drugs competing with Mocravimod: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['Mocravimod']

**q021-batch** `Mocravimod IBD S1PR competitors licensing status || Mocravimod Crohn's disease ulcerative colitis S1PR1 agents || Mocravimod etrasimod ozanimod head-to-head IBD || Mocravimod IBD partnering in-licensing || Mocravimod ClinicalTrials.gov Crohn's ulcerative colitis` → kept 10/10, jev 399 ms

- ✅ **0.8633** [on_target=0.97 evidence=0.89] Targeting the Sphingosine-1-Phosphate Pathway - PMC - NIH — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.8298** [on_target=0.98 evidence=0.85] Targeting Sphingosine-1-Phosphate Signaling in Immune ... — pmc.ncbi.nlm.nih.gov (#8) `A`
- ✅ **0.7284** [on_target=0.98 evidence=0.74] Safety and efficacy of S1P receptor modulators for the ... - PMC — pmc.ncbi.nlm.nih.gov (#6) `A`
- ✅ **0.6999** [on_target=0.95 evidence=0.74] Adjunctive and… · Phase III (2024-512752-38-00) - CTIS.eu — ctis.eu (#3) `A`
- ✅ **0.6596** [on_target=0.97 evidence=0.68] mocravimod / Ligand page — guidetopharmacology.org (#9) `A`
- ✅ **0.6304** [on_target=0.98 evidence=0.64] Efficacy and safety of sphingosine-1-phosphate receptor ... — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.6173** [on_target=0.94 evidence=0.66] Mocravimod — pubchem.ncbi.nlm.nih.gov (#7) `A`
- ✅ **0.5826** [on_target=0.95 evidence=0.61] Mocravimod — go.drugbank.com (#10) `A`
- ✅ **0.5714** [on_target=0.79 evidence=0.72] Mocravimod Hydrochloride - Inxight Drugs — drugs.ncats.io (#2) `A`
- ✅ **0.5447** [on_target=0.76 evidence=0.72] Mocravimod - Inxight Drugs — drugs.ncats.io (#4) `A`

## q022 (competitor objective)

**Objective:** competing agents in the same mechanistic class for this indication Novel UC Treatment, Cosmo Health, Distal Ulcerative Colitis  
**Target sent:** Novel UC Treatment itself, or drugs competing with Novel UC Treatment: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['Novel UC Treatment']

**q022-batch** `Novel UC Treatment mechanism of action ulcerative colitis || Novel UC Treatment target mechanistic class UC || Novel UC Treatment Phase 2 competitor landscape ulcerative colitis` → kept 1/10, jev 415 ms

- ✅ **0.3946** [on_target=0.74 evidence=0.53] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_evidence **0.3093** [on_target=0.64 evidence=0.48] Emerging Therapies for Ulcerative Colitis: Updates from Recent ... — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_evidence **0.2686** [on_target=0.62 evidence=0.43] Ulcerative Colitis: Today, Tomorrow, and the Future — emjreviews.com (#5)
- ❌ low_evidence **0.2674** [on_target=0.68 evidence=0.39] [PDF] Advances in the Treatment of Ulcerative Colitis—From Conventional ... — pdfs.semanticscholar.org (#8)
- ❌ low_evidence **0.2553** [on_target=0.69 evidence=0.37] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#1)
- ❌ low_evidence **0.2541** [on_target=0.63 evidence=0.40] Practical guidance for managing patients with moderate-to-severe ... — academic.oup.com (#2)
- ❌ low_evidence **0.2449** [on_target=0.65 evidence=0.38] Current Pharmacologic Options and Emerging Therapeutic ... - PMC — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_evidence **0.2368** [on_target=0.64 evidence=0.37] Emerging Therapies in Inflammatory Bowel Disease - PMC - NIH — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_evidence **0.2347** [on_target=0.64 evidence=0.37] Advances in the Treatment of Ulcerative Colitis—From Conventional ... — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0243** [on_target=0.08 evidence=0.30] Frontiers / Harnessing nature’s pharmacy: investigating natural compounds as novel therapeutics for  — frontiersin.org (#10)

## q023 (competitor objective)

**Objective:** Inflammatory Bowel Diseases Mild-to-moderate ulcerative colitis Ulcerative Colitis competing agents with the same mechanistic class as Gut Microbiome Dysbiosis, including Live Biotherapeutic Product  
**Target sent:** VE202 / MB310 / SER-287 / EXL01 itself, or drugs competing with VE202 / MB310 / SER-287 / EXL01: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['VE202', 'MB310', 'SER-287', 'EXL01']

**q023-batch** `VE202 Phase 2 current status licensing || MB310 Phase 2 Microbiotica licensing || SER-287 ulcerative colitis development status licensing || EXL01 ReMind Phase 2 licensing Crohn's disease` → kept 10/10, jev 407 ms

- ✅ **0.8504** [on_target=0.97 evidence=0.88] EX-99.1 — sec.gov (#4) `A`
- ✅ **0.8234** [on_target=0.95 evidence=0.87] VE-202 - Drug Targets, Indications, Patents — synapse.patsnap.com (#10) `A`
- ✅ **0.8213** [on_target=0.97 evidence=0.85] SER-287 - Drug Targets, Indications, Patents — synapse.patsnap.com (#8) `A`
- ✅ **0.818** [on_target=0.97 evidence=0.84] SER-287 Drug Asset Due Diligence Report 2026 — synapse.patsnap.com (#1) `A`
- ✅ **0.6592** [on_target=0.96 evidence=0.69] Partnering - Microbiotica — microbiotica.com (#7) `A`
- ✅ **0.5829** [on_target=0.87 evidence=0.67] MAINTAIN POP submitted to ANSM - Exeliom Biosciences — exeliombio.com (#9) `A`
- ✅ **0.5504** [on_target=0.86 evidence=0.64] Exeliom Biosciences collaborates with REMIND in MAINTAIN POP ... — exeliombio.com (#6) `A`
- ✅ **0.544** [on_target=0.85 evidence=0.64] Delving into the Latest Updates on EXL-01 with Synapse — synapse.patsnap.com (#3) `A`
- ✅ **0.5063** [on_target=0.83 evidence=0.61] Exeliom Biosciences collabore avec REMIND sur l’essai — ala.associates (#2) `A`
- ✅ **0.4941** [on_target=0.81 evidence=0.61] News - exeliom — exeliombio.com (#5) `A`

## q024 (competitor objective)

**Objective:** Ulcerative Colitis competing agents in the same mechanistic class as ITGA4 ITGB7 Integrin Alpha-4 Beta-7 Integrin α4β7 Small Molecule therapies  
**Target sent:** emvistegrast itself, or drugs competing with emvistegrast: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['emvistegrast']

**q024-batch** `emvistegrast α4β7 ulcerative colitis Phase 2 competitors || emvistegrast α4β7 ulcerative colitis pipeline Phase 3 || emvistegrast α4β7 ulcerative colitis licensing || emvistegrast integrin alpha-4 beta-7 ulcerative colitis clinical trial` → kept 10/10, jev 391 ms

- ✅ **0.9474** [on_target=0.98 evidence=0.97] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#5) `A`
- ✅ **0.9376** [on_target=0.98 evidence=0.96] Table 1. — pmc.ncbi.nlm.nih.gov (#3) `A`
- ✅ **0.9244** [on_target=0.98 evidence=0.94] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#9) `A`
- ✅ **0.7714** [on_target=0.89 evidence=0.87] SPY001 (Ph 2) for Ulcerative Colitis / Spyre Therapeutics, Inc — biopharmawatch.com (#2) `A`
- ✅ **0.7534** [on_target=0.97 evidence=0.78] drug hunter on X: "Gilead's Recently Disclosed, Selective α4β7 ... — x.com (#7) `A`
- ✅ **0.7232** [on_target=0.96 evidence=0.75] emvistegrast (GS-1427) / Gilead - LARVOL DELTA — delta.larvol.com (#1) `A`
- ✅ **0.6596** [on_target=0.97 evidence=0.68] emvistegrast / Ligand page — guidetopharmacology.org (#10) `A`
- ✅ **0.6467** [on_target=0.97 evidence=0.67] GS-1427 in Participants With Moderately to Severely Active ... — clinicaltrials.ucsf.edu (#8) `A`
- ✅ **0.608** [on_target=0.95 evidence=0.64] UCSF Ulcerative Colitis Clinical Trials for 2026 — clinicaltrials.ucsf.edu (#6) `A`
- ✅ **0.5795** [on_target=0.95 evidence=0.61] UCSF Inflammatory Bowel Disease Clinical Trials for 2026 ... — clinicaltrials.ucsf.edu (#4) `A`

## q025 (competitor objective)

**Objective:** Ulcerative Colitis competing agents with the same mechanism of action as HEMAY007, targeting TNF-α Tumor Necrosis Factor Alpha  
**Target sent:** HEMAY007 itself, or drugs competing with HEMAY007: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['HEMAY007']

**q025-batch** `HEMAY007 ulcerative colitis anti-TNF Phase 2 competitors || HEMAY007 ulcerative colitis anti-TNF licensing availability || HEMAY007 TNF-alpha ulcerative colitis clinical development status || HEMAY007 ulcerative colitis anti-TNF biosimilar landscape` → kept 10/10, jev 411 ms

- ✅ **0.9408** [on_target=0.98 evidence=0.96] Hemay007: TNF-alpha, Phase 2 in Ulcerative Colitis — assetmemo.bio (#8) `A`
- ✅ **0.9244** [on_target=0.98 evidence=0.94] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#10) `A`
- ✅ **0.918** [on_target=0.98 evidence=0.94] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#4) `A`
- ✅ **0.8864** [on_target=0.96 evidence=0.92] TNF-alpha - ACROBiosystems — acrobiosystems.com (#9) `A`
- ✅ **0.7968** [on_target=0.96 evidence=0.83] TNF-Alpha Proteins, Antibodies & ELISA Kits — acrobiosystems.com (#6) `A`
- ✅ **0.7854** [on_target=0.95 evidence=0.83] Table 1. — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.6809** [on_target=0.95 evidence=0.72] OVERVIEW — www1.hkexnews.hk (#7) `A`
- ✅ **0.6524** [on_target=0.95 evidence=0.69] This summary aims to give you an overview of the information contained in this — www1.hkexnews.hk (#2) `A`
- ✅ **0.6464** [on_target=0.96 evidence=0.67] Hemay007 - Drug Targets, Indications, Patents — synapse.patsnap.com (#5) `A`
- ✅ **0.6429** [on_target=0.95 evidence=0.68] [PDF] 概覽 — www1.hkexnews.hk (#3) `A`

## q026

**Objective:** BM-013 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** BM-013 · anchors ['BM-013']

**q026-batch** `BM-013 acute myeloid leukemia regulatory approval launch || BM-013 BIMINI Biotech approval AML || BM-013 WASP AML clinical development forecast` → kept 1/10, jev 357 ms

- ✅ **0.5099** [on_target=0.95 evidence=0.54] Portfolio - BIMINI Biotech — biminibiotech.nl (#1) `A`
- ❌ low_evidence **0.4669** [on_target=0.94 evidence=0.50] Bimini Biotech company information, funding & investors — app.dealroom.co (#7) `A`
- ❌ low_on_target **0.3953** [on_target=0.49 evidence=0.81] Home / AML Hub — aml-hub.com (#8)
- ❌ low_on_target **0.128** [on_target=0.23 evidence=0.56] Oncology (Cancer)/Hematologic Malignancies Approval ... — fda.gov (#3)
- ❌ low_on_target **0.0714** [on_target=0.14 evidence=0.51] BIMINI Biotech — biobase.whitefordresearch.com (#5)
- ❌ low_on_target **0.0319** [on_target=0.11 evidence=0.29] News – BIMINI Biotech — biminibiotech.nl (#2)
- ❌ low_on_target **0.0012** [on_target=0.36 evidence=0.00] Bimini Biotech B.V. - Drug pipelines, Patents, Clinical trials - Synapse — synapse.patsnap.com (#4)
- ❌ low_on_target **0.0004** [on_target=0.13 evidence=0.00] BIMINI Biotech / BIO-Europe Spring — informaconnect.com (#10)
- ❌ low_on_target **0.0** [on_target=0.06 evidence=0.00] Bimini Biotech / Longevity Solutions — bimini-biotech.com (#6)
- ❌ low_on_target **0.0** [on_target=0.09 evidence=0.00] Story — biomediaproject.com (#9)

## q027

**Objective:** HQL-79 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** HQL-79 · anchors ['HQL-79']

**q027-batch** `HQL-79 pancreatic ductal adenocarcinoma in vivo || HQL-79 monotherapy PDAC xenograft || HQL-79 tumour regression animal model || HQL-79 tumour growth inhibition pancreatic cancer` → kept 6/10, jev 657 ms

- ✅ **0.7566** [on_target=0.97 evidence=0.78] Figure 7. — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.6968** [on_target=0.78 evidence=0.89] www.creative-biolabs.com › blog › adcHyaluronidase-Conjugated Liposomes May Effectively Target ... — creative-biolabs.com (#4)
- ✅ **0.6628** [on_target=0.97 evidence=0.68] Activated T Cells Break Tumor Immunosuppression by Macrophage ... — pmc.ncbi.nlm.nih.gov (#3) `A`
- ✅ **0.5904** [on_target=0.82 evidence=0.72] An efficient drug delivery system to block pancreatic cancer — pubmed.ncbi.nlm.nih.gov (#2)
- ✅ **0.5888** [on_target=0.96 evidence=0.61] Figure 6. — pmc.ncbi.nlm.nih.gov (#6) `A`
- ✅ **0.498** [on_target=0.77 evidence=0.65] chloroquine and hydroxychloroquine as anti-cancer agents — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.2669** [on_target=0.44 evidence=0.61] Phytochemicals as Multitarget Therapeutics in Pancreatic Cancer: Mechanisms, Clinical Evidence, and  — onlinelibrary.wiley.com (#1)
- ❌ low_on_target **0.0117** [on_target=0.04 evidence=0.29] In Vivo Preclinical Models — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0001** [on_target=0.03 evidence=0.00] Cloudflare — cell.com (#8)
- ❌ low_on_target **0.0001** [on_target=0.04 evidence=0.00] Cloudflare — cell.com (#9)

## q028

**Objective:** HEC234055 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** HEC234055 · anchors ['HEC234055']

**q028-batch** `HEC234055 monotherapy HPAC PDAC xenograft regression || HEC234055 PK-59 PDAC monotherapy tumour regression` → kept 1/10, jev 420 ms

- ✅ **0.5543** [on_target=0.69 evidence=0.80] [PDF] E262019A_Sunshine Pharma 1..4 - HKEXnews — www1.hkexnews.hk (#1)
- ❌ low_on_target **0.0401** [on_target=0.43 evidence=0.09] [PDF] Lactate Dehydrogenase-A Inhibitor Against Pancreatic Cancer — sciencedirect.com (#9)
- ❌ low_on_target **0.0342** [on_target=0.38 evidence=0.09] �NH�w���m�3�R��DU�Պ��Q7W�r����%�C�z�A�?w7r�$����r��z��E &��#��"t����� �ŠZ�� ��!��#�9�ax�Ȭ��!�d�f��_� — frontiersin.org (#8)
- ❌ low_on_target **0.0112** [on_target=0.28 evidence=0.04] Article Rapid and Selective Targeting of Heterogeneous Pancreatic ... — sciencedirect.com (#4)
- ❌ low_on_target **0.0057** [on_target=0.17 evidence=0.03] A potential therapeutic target for pancreatic ductal adenocarcinoma — sciencedirect.com (#5)
- ❌ low_on_target **0.0028** [on_target=0.17 evidence=0.02] Pancreatic Ductal Adenocarcinoma Archives - Annual Report - Ipsen — ipsen.com (#6)
- ❌ low_on_target **0.0005** [on_target=0.14 evidence=0.00] Press Release — perspectivetherapeutics.com (#2)
- ❌ low_on_target **0.0003** [on_target=0.05 evidence=0.01] Biliary tract cancer — sciencedirect.com (#10)
- ❌ low_on_target **0.0002** [on_target=0.05 evidence=0.00] CCDI Hub — moleculartargets.ccdi.cancer.gov (#3)
- ❌ low_on_target **0.0** [on_target=0.06 evidence=0.00] Page not found — medschool.cuanschutz.edu (#7)

## q029

**Objective:** TP-317 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** TP-317 KPC / TP-317 · anchors ['TP-317 KPC', 'TP-317']

**q029-batch** `TP-317 KPC pancreatic cancer tumour regression monotherapy || TP-317 KPC PDAC dose schedule monotherapy` → kept 3/10, jev 821 ms

- ✅ **0.8864** [on_target=0.96 evidence=0.92] Abstract 1135: TP317, a first-in-class resolvin E1 small molecule, potentiates the efficacy of immun — aacrjournals.org (#1) `A`
- ✅ **0.6976** [on_target=0.96 evidence=0.73] Award / SBIR — sbir.gov (#5) `A`
- ✅ **0.665** [on_target=0.95 evidence=0.70] Firm / SBIR — sbir.gov (#7) `A`
- ❌ low_on_target **0.0552** [on_target=0.18 evidence=0.31] Unbiased in vivo preclinical evaluation of anticancer drugs identifies ... — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0255** [on_target=0.51 evidence=0.05] � — cdn.clinicaltrials.gov (#9)
- ❌ low_on_target **0.0213** [on_target=0.58 evidence=0.04] Graphical Abstract — academic.oup.com (#10)
- ❌ low_on_target **0.0204** [on_target=0.47 evidence=0.04] ��������� — cdn.clinicaltrials.gov (#6)
- ❌ low_on_target **0.0013** [on_target=0.04 evidence=0.03] Pembrolizumab, carboplatin and paclitaxel 1 of 5 — kmcc.nhs.uk (#2)
- ❌ low_on_target **0.0** [on_target=0.06 evidence=0.00] Cloudflare — cell.com (#3)
- ❌ low_on_target **0.0** [on_target=0.12 evidence=0.00] Detail - OpenURL Connection — openurl.ebsco.com (#4)

## q030

**Objective:** SGR-4174 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** SGR-4174 · anchors ['SGR-4174']

**q030-batch** `SGR-4174 Mia PaCa2 monotherapy tumour regression xenograft || SGR-4174 PDAC xenograft tumour shrinkage single agent` → kept 7/10, jev 383 ms

- ✅ **0.7663** [on_target=0.97 evidence=0.79] [PDF] Schrödinger Presents New Preclinical Data at AACR Annual Meeting — s203.q4cdn.com (#5) `A`
- ✅ **0.7448** [on_target=0.98 evidence=0.76] SGR-4174 / Schrodinger - Larvol Delta — delta.larvol.com (#4) `A`
- ✅ **0.7136** [on_target=0.96 evidence=0.74] SOS1: tracking the evolving path from promising to actionable ... — link.springer.com (#3) `A`
- ✅ **0.6765** [on_target=0.99 evidence=0.68] Schrödinger, Inc. - Drug pipelines, Patents, Clinical trials — synapse.patsnap.com (#2) `A`
- ✅ **0.6681** [on_target=0.95 evidence=0.70] SOS1: tracking the evolving path from promising to actionable ... — link.springer.com (#1) `A`
- ✅ **0.637** [on_target=0.97 evidence=0.66] Tumor growth inhib News — sigma.larvol.com (#7) `A`
- ✅ **0.568** [on_target=0.71 evidence=0.80] Preclinical assessment with clinical validation of Selinexor ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_evidence **0.4753** [on_target=0.97 evidence=0.49] Schrödinger to Present Preclinical Data at AACR Annual ... — s203.q4cdn.com (#6) `A`
- ❌ low_evidence **0.0552** [on_target=0.92 evidence=0.06] Delving into the Latest Updates on SGR-4174 with Synapse — synapse.patsnap.com (#9) `A`
- ❌ low_on_target **0.0137** [on_target=0.05 evidence=0.27] MIA PaCa-2 Xenograft Model — altogenlabs.com (#8)

## q031

**Objective:** SPR2015 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma (PDAC) animal models  
**Target sent:** SPR2015 · anchors ['SPR2015']

**q031-batch** `SPR2015 HPAC xenograft TGI percentage monotherapy || SPR2015 AsPC-1 xenograft tumour regression shrinkage || SPR2015 PDAC monotherapy xenograft tumour growth inhibition || SPR2015 HPAC AsPC-1 xenograft AACR 2026 abstract 5978` → kept 9/10, jev 340 ms

- ✅ **0.7676** [on_target=0.98 evidence=0.78] KRAS G12D Inhibitor's $2.13B Deal Tests Cross-Border Tech Transfer — pharmtech.com (#3) `A`
- ✅ **0.7056** [on_target=0.98 evidence=0.72] Merck Enters into Exclusive Global License Agreement ... — merck.com (#6) `A`
- ✅ **0.7016** [on_target=0.97 evidence=0.72] MSD takes a $400m bite of SciBrunch's KRAS drug — pharmaphorum.com (#4) `A`
- ✅ **0.699** [on_target=0.98 evidence=0.71] Merck licenses SPR2015, an oral KRAS G12D inhibitor, from ... — chemxplore.com (#8) `A`
- ✅ **0.6794** [on_target=0.98 evidence=0.69] Merck Licenses Preclinical KRAS G12D Inhibitor from SciBrunch — pharmexec.com (#5) `A`
- ✅ **0.6696** [on_target=0.98 evidence=0.68] Revolution Medicines - MedPath Trial — trial.medpath.com (#2) `A`
- ✅ **0.6531** [on_target=0.97 evidence=0.67] SPR2015: Merck Pays $400M, Up to $2.13B - novapharmanews.com — novapharmanews.com (#9) `A`
- ✅ **0.6336** [on_target=0.96 evidence=0.66] Merck, SciBrunch Launch Up-to-$2.13B Collaboration ... — genengnews.com (#1) `A`
- ✅ **0.544** [on_target=0.96 evidence=0.57] Anirban Maitra on X: "This #AACR26 abstract is worth $400 ... — x.com (#7) `A`
- ❌ low_evidence **0.4232** [on_target=0.92 evidence=0.46] Merck–SciBrunch SPR2015 Deal / Lucid Diligence Brief - LucidQuest — lqventures.com (#10) `A`

## q032

**Objective:** PHY-003 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Head and Neck Squamous Cell Carcinoma animal models  
**Target sent:** PHY-003 · anchors ['PHY-003']

**q032-batch** `PHY-003 HNSCC monotherapy xenograft tumour regression || PHY-003 HNSCC in vivo tumour growth inhibition dose || PHY-003 head and neck squamous cell carcinoma animal model efficacy` → ABSTAIN, jev 380 ms

- ❌ low_on_target **0.042** [on_target=0.42 evidence=0.10] ���̝��p�l��Б�KY��oA�W�Y���ڱ�P��…��lذ�j�&¿�/`+y8���W��M�_��5q���ԗ�[��ϧ�߄����Gu�F5�j�h��Ǿa�Z�a���d��թ} — frontiersin.org (#10)
- ❌ low_on_target **0.0396** [on_target=0.41 evidence=0.10] ��#���0�P7���ho����a� ��[�X�`�p"�3��(��]��5����m�r���� �gl���m�0�S���oH�(EA�?%�D����$RN�=������"}x�1 — frontiersin.org (#9)
- ❌ low_on_target **0.0347** [on_target=0.40 evidence=0.09] ������+X�G������;��g6�vnUJ�Yg�D% 'qF�;�h Q��ҭT�%���2��蔴L�"�3C`�*�N�bh�^���`aj��*�yL�5����g��!��H)��� — frontiersin.org (#6)
- ❌ low_on_target **0.0319** [on_target=0.11 evidence=0.29] Targeted therapy for head and neck cancer: signaling pathways and ... — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.014** [on_target=0.42 evidence=0.03] OncJuly2 6..6 — citeseerx.ist.psu.edu (#1)
- ❌ low_on_target **0.0124** [on_target=0.06 evidence=0.21] Targeted therapy for head and neck cancer: signaling pathways and clinical studies — nature.com (#5)
- ❌ low_on_target **0.0062** [on_target=0.31 evidence=0.02] Original article Head and neck squamous cell carcinoma ... — sciencedirect.com (#4)
- ❌ low_on_target **0.0032** [on_target=0.16 evidence=0.02] A novel therapeutic approach for head and neck cancer — sciencedirect.com (#7)
- ❌ low_on_target **0.0016** [on_target=0.16 evidence=0.01] Cancer Cell — sciencedirect.com (#3)
- ❌ low_on_target **0.0004** [on_target=0.03 evidence=0.01] Current Oncology Reports — springermedicine.com (#2)

## q033

**Objective:** DXP-007 sponsor development stage indication public source  
**Target sent:** DXP-007 · anchors ['DXP-007']

**q033-batch** `DXP-007 sponsor || DXP-007 development stage || DXP-007 inflammatory bowel disease` → kept 1/10, jev 346 ms

- ✅ **0.5292** [on_target=0.81 evidence=0.65] Macrophages and liposomes in inflammatory disease: Friends or foes? — leg.ufpi.br (#10)
- ❌ low_on_target **0.0165** [on_target=0.13 evidence=0.13] Digital eXperience Platform (DXP) Project — bcp.dof.ca.gov (#3)
- ❌ low_on_target **0.014** [on_target=0.10 evidence=0.14] Sponsors & Exhibitors / ProcureCon MRO 2026 — procureconmro.wbresearch.com (#5)
- ❌ low_on_target **0.0054** [on_target=0.23 evidence=0.02] DXP Enterprises, Inc. — sec.gov (#6)
- ❌ low_on_target **0.0021** [on_target=0.07 evidence=0.03] DXP / Logopedia — logos.fandom.com (#8)
- ❌ low_on_target **0.0014** [on_target=0.21 evidence=0.01] DXPR Status — status.dxpr.com (#9)
- ❌ low_on_target **0.0007** [on_target=0.20 evidence=0.00] News — ir.dxpe.com (#4)
- ❌ low_on_target **0.0003** [on_target=0.10 evidence=0.00] DXP News — dxpwind.com (#2)
- ❌ low_on_target **0.0001** [on_target=0.03 evidence=0.00] Common searches — search.electoralcommission.org.uk (#7)
- ❌ low_on_target **0.0** [on_target=0.14 evidence=0.00] Please verify you are a human — zoominfo.com (#1)

## q034

**Objective:** Compound 18l first regulatory approval or market launch year for acute myeloid leukemia  
**Target sent:** Compound 18l · anchors ['Compound 18l']

**q034-batch** `Compound 18l ALKBH5 AML regulatory approval launch year` → kept 3/10, jev 374 ms

- ✅ **0.5029** [on_target=0.82 evidence=0.61] Decoding the immunoregulatory functions of ALKBH5 in ... — frontiersin.org (#9) `A`
- ✅ **0.5012** [on_target=0.84 evidence=0.60] Chinese Academy of Sciences Shanghai Branch — english.shb.cas.cn (#4)
- ✅ **0.3953** [on_target=0.71 evidence=0.56] Discovery of Covalent and Cell‐Active ALKBH5 Inhibitors with ... — onlinelibrary.wiley.com (#8)
- ❌ low_on_target **0.3216** [on_target=0.50 evidence=0.64] Delving into the Latest Updates on ALKBH5 inhibitor(Shanghai Institute of Materia Medica Chinese Aca — synapse.patsnap.com (#6)
- ❌ low_on_target **0.1488** [on_target=0.24 evidence=0.62] Oncology (Cancer)/Hematologic Malignancies Approval ... — fda.gov (#7)
- ❌ low_on_target **0.0126** [on_target=0.09 evidence=0.14] ALKBH5 — affinage.wi.mit.edu (#10)
- ❌ low_on_target **0.0012** [on_target=0.07 evidence=0.02] NME — fda.gov (#2)
- ❌ low_on_target **0.0002** [on_target=0.06 evidence=0.00] Search Orphan Drug Designations and Approvals — accessdata.fda.gov (#3)
- ❌ low_on_target **0.0001** [on_target=0.04 evidence=0.00] Drug Approvals and Databases - FDA — fda.gov (#1)
- ❌ low_on_target **0.0001** [on_target=0.04 evidence=0.00] Breakthrough Therapy Approvals - FDA — fda.gov (#5)

## q035

**Objective:** BS-HH-002 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** BS-HH-002 · anchors ['BS-HH-002']

**q035-batch** `BS-HH-002 regulatory approval AML || BS-HH-002 market launch AML || BS-HH-002 Bensheng Pharma AML clinical development || BS-HH-002 expected approval year || BS-HH-002 first patient AML` → kept 8/10, jev 354 ms

- ✅ **0.8439** [on_target=0.97 evidence=0.87] Therapeutic effects of an innovative BS-HH-002 drug on ... — pmc.ncbi.nlm.nih.gov (#3) `A`
- ✅ **0.7501** [on_target=0.97 evidence=0.77] Delving into the Latest Updates on BS-HH-002 with Synapse — synapse.patsnap.com (#2) `A`
- ✅ **0.7016** [on_target=0.97 evidence=0.72] Delving into the Latest Updates on Shanghai Bensen Pharmaceutical Co., Ltd. with Synapse — synapse.patsnap.com (#10) `A`
- ✅ **0.6016** [on_target=0.96 evidence=0.63] Acylated derivative of homoharringtonine, preparation method therefor, and application thereof — patents.google.com (#1) `A`
- ✅ **0.558** [on_target=0.93 evidence=0.60] A Phase I, Open-Label, Dose Escalation and Cohort Expansion Study of BS HH 002.SA in Patients With A — med.agiltrace.com (#6) `A`
- ✅ **0.5518** [on_target=0.93 evidence=0.59] Abstract 4068: HH-002, a derivative of Homoharringtonine, show promsing in diverse cancer models in  — aacrjournals.org (#8) `A`
- ✅ **0.48** [on_target=0.72 evidence=0.67] Homoharringtonine: mechanisms, clinical applications and ... — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.4565** [on_target=0.83 evidence=0.55] [PDF] MCL-1 inhibitors, fast-lane development of a new class of anti-canc ... — exaly.com (#4) `A`
- ❌ low_evidence **0.2178** [on_target=0.92 evidence=0.24] 高三尖杉酯碱的酰化衍生物、及其制备方法和应用 — patents.google.com (#7) `A`
- ❌ low_on_target **0.0422** [on_target=0.11 evidence=0.38] BSB-1001 for Blood Cancers - Clinical Trials — withpower.com (#9) `A`

## q036

**Objective:** VAR-101 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic Ductal Carcinoma animal models  
**Target sent:** VAR-101 · anchors ['VAR-101']

**q036-batch** `VAR-101 pancreatic ductal carcinoma monotherapy xenograft TGI || VAR-101 pancreatic cancer tumour regression animal model || VAR-101 aPKCi PDAC in vivo efficacy monotherapy` → ABSTAIN, jev 365 ms

- ❌ low_on_target **0.0036** [on_target=0.36 evidence=0.01] CLINICAL TRIALS — amgentrials.com (#9)
- ❌ low_on_target **0.0023** [on_target=0.35 evidence=0.01] Study Details Page — abbvieclinicaltrials.com (#7)
- ❌ low_on_target **0.0021** [on_target=0.32 evidence=0.01] Study Details Page — abbvieclinicaltrials.com (#3)
- ❌ low_on_target **0.0009** [on_target=0.26 evidence=0.00] Internal Server Error — med.stanford.edu (#1)
- ❌ low_on_target **0.0007** [on_target=0.22 evidence=0.00] register — academic.oup.com (#4)
- ❌ low_on_target **0.0005** [on_target=0.15 evidence=0.00] Orphanet: — orpha.net (#8)
- ❌ low_on_target **0.0** [on_target=0.04 evidence=0.00] Cloudflare — cell.com (#2)
- ❌ low_on_target **0.0** [on_target=0.09 evidence=0.00] Detail - OpenURL Connection — openurl.ebsco.com (#5)
- ❌ low_on_target **0.0** [on_target=0.09 evidence=0.00] Page not found — medschool.cuanschutz.edu (#6)
- ❌ low_on_target **0.0** [on_target=0.20 evidence=0.00] Page Not Found — mayo.edu (#10)

## q037

**Objective:** IPS-06061 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in KRAS G12D Mutant Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** IPS-06061 · anchors ['IPS-06061']

**q037-batch** `IPS-06061 AsPC-1 xenograft tumour regression || IPS-06061 30 mg/kg TGI AsPC-1 || IPS-06061 day 28 tumour volume AsPC-1 || IPS-06061 tumour shrinkage pancreatic cancer xenograft` → kept 3/10, jev 372 ms

- ✅ **0.6632** [on_target=0.98 evidence=0.68] IPS-06061, a novel TPD molecular glue degrader targeting ... — semanticscholar.org (#4) `A`
- ✅ **0.6566** [on_target=0.98 evidence=0.67] IPS-06061, a novel orally active TPD molecular glue degrader targeting… / Gagan Kukreja / 10 comment — linkedin.com (#1) `A`
- ✅ **0.6434** [on_target=0.97 evidence=0.66] IPS-06061 / InnoPharmaScreen - LARVOL DELTA — delta.larvol.com (#5) `A`
- ❌ low_on_target **0.0035** [on_target=0.15 evidence=0.02] Cancer Cell — sciencedirect.com (#7)
- ❌ low_on_target **0.0007** [on_target=0.22 evidence=0.00] JavaScript is required... — pubchem.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0004** [on_target=0.11 evidence=0.00] CONTENTdm — ojd.contentdm.oclc.org (#3)
- ❌ low_on_target **0.0** [on_target=0.03 evidence=0.00] Cloudflare — aacrjournals.org (#6)
- ❌ low_on_target **0.0** [on_target=0.04 evidence=0.00] Letter to the Editor: — journals.aboutscience.eu (#8)
- ❌ low_on_target **0.0** [on_target=0.04 evidence=0.00] Browse — inplasy.com (#9)
- ❌ low_evidence **0.0** [on_target=0.91 evidence=0.00] CAS 3064065-83-1 IPS-06061 - Alfa Chemistry — alfa-chemistry.com (#10) `A`

## q038 (competitor objective)

**Objective:** KRAS G12D drugs approved against the target and their regulatory approval status  
**Target sent:** ZE980277 itself, or drugs competing with ZE980277: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['ZE980277']

**q038-batch** `ZE980277 KRAS G12D approval status FDA EMA || ZE980277 KRAS G12D regulatory approval || ZE980277 KRAS G12D approved therapy status` → kept 2/10, jev 366 ms

- ✅ **0.6713** [on_target=0.76 evidence=0.88] KRAS Inhibitor Clinical Trial Landscape, September 2026: 115 ... — datalookout.com (#8)
- ❌ low_on_target **0.547** [on_target=0.56 evidence=0.98] cancer.aestheticsadvisor.com · 2026 · 04KRAS Inhibitors (2026): The Complete Guide to Targeted Thera — cancer.aestheticsadvisor.com (#7)
- ✅ **0.5461** [on_target=0.64 evidence=0.85] Precision Targeting of KRAS-Mutant Cancers: Beyond G12C ... - PMC — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.5034** [on_target=0.59 evidence=0.85] Therapeutic inhibition of RAS in non-small cell lung cancer - Frontiers — frontiersin.org (#6)
- ❌ low_on_target **0.477** [on_target=0.53 evidence=0.90] Oral Investigational Agent Zoldonrasib Elicits Objective Responses ... — aacr.org (#5)
- ❌ low_on_target **0.4734** [on_target=0.53 evidence=0.89] Search Orphan Drug Designations and Approvals - FDA — accessdata.fda.gov (#1)
- ❌ low_on_target **0.4512** [on_target=0.47 evidence=0.96] Targeting KRAS: Promising New Therapy for Hard-to-Treat Lung ... — cancer.columbia.edu (#3)
- ❌ low_on_target **0.2064** [on_target=0.48 evidence=0.43] Ongoing / Cancer Accelerated Approvals — fda.gov (#4)
- ❌ low_on_target **0.1056** [on_target=0.33 evidence=0.32] www.clintrialfinder.info › mechanisms › kras-inhibitors100 KRAS Inhibitor Trials Recruiting (Septemb — clintrialfinder.info (#9)
- ❌ low_on_target **0.0895** [on_target=0.34 evidence=0.26] Oncology (Cancer)/Hematologic Malignancies Approval ... — fda.gov (#2)

## q039 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as KPG-818, including Small Molecule and Aiolos CRBN Ikaros therapies  
**Target sent:** KPG-818 itself, or drugs competing with KPG-818: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['KPG-818']

**q039-batch** `KPG-818 Aiolos CRBN Ikaros inflammatory bowel disease competitors || KPG-818 CELMoD IBD clinical pipeline || KPG-818 CRBN degrader inflammatory bowel disease` → kept 10/10, jev 540 ms

- ✅ **0.7154** [on_target=0.98 evidence=0.73] epaldeudomide (KPG-818) / Kangpu Biopharma - Larvol Delta — delta.larvol.com (#9) `A`
- ✅ **0.656** [on_target=0.82 evidence=0.80] Epaldeudomide - Drug Targets, Indications, Patents - Synapse — synapse.patsnap.com (#1)
- ✅ **0.656** [on_target=0.96 evidence=0.68] Kangpu Biopharmaceuticals Ltd. - Drug pipelines, Patents, ... — synapse.patsnap.com (#7) `A`
- ✅ **0.6555** [on_target=0.95 evidence=0.69] Chongqing Kangpu Chemical Industry Co Ltd. — synapse.patsnap.com (#6) `A`
- ✅ **0.6496** [on_target=0.96 evidence=0.68] [PDF] Protocol - ClinicalTrials.gov — cdn.clinicaltrials.gov (#10) `A`
- ✅ **0.6204** [on_target=0.94 evidence=0.66] A Novel Paradigm for Targeting Challenging Targets: Advancing Technologies and Future Directions of  — mdpi.com (#4) `A`
- ✅ **0.6176** [on_target=0.96 evidence=0.64] KPG-818, a Novel Cereblon (CRBN) Modulator, in Patients with SLE — acrabstracts.org (#3) `A`
- ✅ **0.611** [on_target=0.94 evidence=0.65] Future of Lupus Treatments Looks Brighter With Multiple Promising Therapeutic Approaches / MDedge — mdedge.com (#5) `A`
- ✅ **0.611** [on_target=0.94 evidence=0.65] Kangpu Biopharmaceuticals / Drug Developments / Pipeline Prospector — pharmacompass.com (#8) `A`
- ✅ **0.6076** [on_target=0.93 evidence=0.65] Multiple Investigational Approaches Show Promise for Lupus — medscape.com (#2) `A`

## q040 (competitor objective)

**Objective:** Active Ulcerative Colitis Moderate to Severe Ulcerative Colitis competing agents in the same mechanistic class as CHST15 Oligonucleotide Small Interfering RNA therapies  
**Target sent:** GUT-1 itself, or drugs competing with GUT-1: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['GUT-1']

**q040-batch** `GUT-1 CHST15 ulcerative colitis competitors || GUT-1 siRNA CHST15 ulcerative colitis || GUT-1 CHST15 moderate to severe ulcerative colitis pipeline` → kept 7/10, jev 465 ms

- ✅ **0.8384** [on_target=0.96 evidence=0.87] Research progress in molecular targeted therapy for inflammatory ... — pmc.ncbi.nlm.nih.gov (#7) `A`
- ✅ **0.7551** [on_target=0.94 evidence=0.80] Y-ECCO Literature Review: Lushen Pillay — ecco-ibd.eu (#6) `A`
- ✅ **0.7544** [on_target=0.92 evidence=0.82] Submucosal Injection of the RNA Oligonucleotide GUT-1 in Active Ulcerative Colitis Patients: A Rando — academic.oup.com (#3) `A`
- ✅ **0.7426** [on_target=0.94 evidence=0.79] Y-ECCO Literature Review: Lushen Pillay - ECCO - European Crohn’s and Colitis Organisation — ecco-ibd.eu (#5) `A`
- ✅ **0.72** [on_target=0.90 evidence=0.80] Research progress in molecular targeted therapy for inflammatory ... — link.springer.com (#4) `A`
- ✅ **0.6758** [on_target=0.93 evidence=0.73] Add-on multiple submucosal injections of the RNA oligonucleotide GUT-1 to anti-TNF antibody treatmen — d-nb.info (#2) `A`
- ✅ **0.6675** [on_target=0.89 evidence=0.75] Submucosal Injection of the RNA Oligonucleotide GUT-1 in Active ... — academic.oup.com (#1) `A`
- ❌ low_on_target **0.3867** [on_target=0.58 evidence=0.67] [PDF] Current and emerging therapeutic targets for IBD - SciSpace — scispace.com (#10)
- ❌ low_on_target **0.0561** [on_target=0.17 evidence=0.33] Unveiling the key genes, environmental toxins, and drug exposures in modulating the severity of ulce — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0468** [on_target=0.18 evidence=0.26] Identification of Ferro‐Aging‐Related Biomarkers for Ulcerative ... — pmc.ncbi.nlm.nih.gov (#8)

## q041 (competitor objective)

**Objective:** competing agents in the same mechanistic class for this indication DB-3Q, Direct Biologics LLC, Medically Refractory Crohn's Disease  
**Target sent:** DB-3Q itself, or drugs competing with DB-3Q: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['DB-3Q']

**q041-batch** `DB-3Q MSC-derived extracellular vesicle Crohn's competitors || DB-3Q extracellular vesicle Crohn's disease clinical trials || DB-3Q MSC-derived EV medically refractory Crohn's` → kept 10/10, jev 346 ms

- ✅ **0.846** [on_target=0.98 evidence=0.86] DB-3Q bmMSC-EVs in Patients With Perianal Fistulizing Crohn's Disease — ichgcp.net (#2) `A`
- ✅ **0.8374** [on_target=0.97 evidence=0.86] [PDF] Claudia Musat, MD - Columbia Surgery — columbiasurgery.org (#4) `A`
- ✅ **0.82** [on_target=0.98 evidence=0.84] Study Details / NCT07625293 / ClinicalTrials.gov - ClinicalTrials.gov — clinicaltrials.gov (#1) `A`
- ✅ **0.7676** [on_target=0.98 evidence=0.78] Allogeneic Bone Marrow Mesenchymal Stem Cell Derived ... — synapse.patsnap.com (#7) `A`
- ✅ **0.7488** [on_target=0.96 evidence=0.78] Direct Biologics LLC - Drug pipelines, Patents, Clinical trials — synapse.patsnap.com (#5) `A`
- ✅ **0.734** [on_target=0.97 evidence=0.76] NCT06918808: An ongoing trial by Direct Biologics, LLC — fdaaa.trialstracker.net (#6) `A`
- ✅ **0.7178** [on_target=0.97 evidence=0.74] Columbia Enrolls Nation's First Patient in Direct Biologics' Phase 2 ... — columbiasurgery.org (#3) `A`
- ✅ **0.679** [on_target=0.97 evidence=0.70] Direct Biologics / MTEC — mtec-sc.org (#8) `A`
- ✅ **0.6693** [on_target=0.97 evidence=0.69] Direct Biologics Clinical Research Programs — linkedin.com (#9) `A`
- ✅ **0.4048** [on_target=0.66 evidence=0.61] Filgotinib in the Induction and Maintenance of Remission in Adults ... — clareohealth.com (#10) `A`

## q042 (competitor objective)

**Objective:** Moderately to Severely Active Ulcerative Colitis, Duration 3 Months, Modified Mayo Score 5 to 9, With Inadequate Response, Loss of Response, or Intolerance to Prior Standard-of-Care Medications competing agents in the same mechanistic class as TYK2 Small Molecule  
**Target sent:** D-2570 itself, or drugs competing with D-2570: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['D-2570']

**q042-batch** `D-2570 TYK2 ulcerative colitis competitor Phase 2 status` → kept 10/10, jev 335 ms

- ✅ **0.9048** [on_target=0.98 evidence=0.92] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.8795** [on_target=0.97 evidence=0.91] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#1) `A`
- ✅ **0.771** [on_target=0.98 evidence=0.79] Yifang Bio-U (688382) 2026 H1 Report Commentary: Multiple Core Pipeline Programs Show Strong Progres — news.futunn.com (#4) `A`
- ✅ **0.721** [on_target=0.97 evidence=0.74] SUMMARY — www1.hkexnews.hk (#3) `A`
- ✅ **0.7072** [on_target=0.96 evidence=0.74] BUSINESS — www1.hkexnews.hk (#10) `A`
- ✅ **0.6201** [on_target=0.89 evidence=0.70] Emerging Therapies for Ulcerative Colitis: Updates from Recent ... — pmc.ncbi.nlm.nih.gov (#8)
- ✅ **0.6032** [on_target=0.87 evidence=0.69] A Study on the Safety of TAK-279 and Whether it Can Reduce Inflammation in the Bowel of Participants — med.agiltrace.com (#7) `A`
- ✅ **0.5386** [on_target=0.80 evidence=0.67] The Efficacy of Hyperbaric Oxygen-assisted Treatment for ASUC and Refractory IBD — med.agiltrace.com (#9) `A`
- ✅ **0.536** [on_target=0.80 evidence=0.67] Interleukin-23p19 Inhibitors in Inflammatory Bowel Disease — pmc.ncbi.nlm.nih.gov (#6)
- ✅ **0.513** [on_target=0.81 evidence=0.63] Study Evaluating ISM5411 Administered Orally to Subjects With Active Ulcerative Colitis (BETHESDA) — med.agiltrace.com (#5) `A`

## q043 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as VNN1, including Small Molecule therapies  
**Target sent:** MY009 itself, or drugs competing with MY009: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['MY009']

**q043-batch** `MY009 VNN1 inflammatory bowel disease competing agents` → kept 1/10, jev 358 ms

- ✅ **0.6984** [on_target=0.97 evidence=0.72] MY-009212A - Drug Targets, Indications, Patents — synapse.patsnap.com (#7) `A`
- ❌ low_on_target **0.253** [on_target=0.46 evidence=0.55] Methods and pharmaceutical compositions for repairing intestinal ... — patents.google.com (#2)
- ❌ low_on_target **0.1687** [on_target=0.46 evidence=0.37] The Present and Future of Inflammatory Bowel Disease ... - PMC — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.1545** [on_target=0.45 evidence=0.34] Inflammatory Bowel Disease: Understanding Therapeutic Effects of ... — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.1512** [on_target=0.42 evidence=0.36] What drugs are in development for Inflammatory Bowel Diseases? — synapse.patsnap.com (#9)
- ❌ low_on_target **0.1033** [on_target=0.31 evidence=0.33] Landscape of new drugs and targets in inflammatory bowel disease — onlinelibrary.wiley.com (#3)
- ❌ low_on_target **0.0768** [on_target=0.24 evidence=0.32] Medications for Inflammatory Bowel Disease — merckmanuals.com (#10)
- ❌ low_on_target **0.0485** [on_target=0.16 evidence=0.30] Inflammatory Bowel Disease Biomarkers - PMC - NIH — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0033** [on_target=0.09 evidence=0.04] Biological agents as attractive targets for inflammatory bowel ... — sciencedirect.com (#8)
- ❌ low_on_target **0.0022** [on_target=0.11 evidence=0.02] Targeting the Unmet Needs in IBD: Emerging Therapies Beyond ... — sciencedirect.com (#4)

## q044 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as GPR52 Prostaglandin E2 Receptor EP4, including Small Molecule therapies  
**Target sent:** NXE0033744 / NXE744 itself, or drugs competing with NXE0033744 / NXE744: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['NXE0033744', 'NXE744']

**q044-batch** `NXE0033744 Phase 2 inflammatory bowel disease || NXE0033744 EP4 agonist clinical trial || NXE0033744 development stage IBD || NXE744 EP4 agonist competitors IBD` → kept 10/10, jev 346 ms

- ✅ **0.721** [on_target=0.97 evidence=0.74] Presentation title - investors.nxera.life — investors.nxera.life (#1) `A`
- ✅ **0.6952** [on_target=0.97 evidence=0.72] [PDF] Corporate Presentation - Investors - Nxera Pharma — investors.nxera.life (#10) `A`
- ✅ **0.679** [on_target=0.97 evidence=0.70] Nxera Pharma Operational Highlights and Consolidated Results for ... — biospace.com (#8) `A`
- ✅ **0.6661** [on_target=0.97 evidence=0.69] Nxera Pharma : Annual Report Year ended 31 December 2024 — marketscreener.com (#7) `A`
- ✅ **0.6564** [on_target=0.97 evidence=0.68] Nxera Pharma Operational Highlights and Consolidated Results ... — daiwair.co.jp (#3) `A`
- ✅ **0.6531** [on_target=0.97 evidence=0.67] Pipeline - Nxera Pharma — nxera.life (#5) `A`
- ✅ **0.6524** [on_target=0.95 evidence=0.69] アニュアルレポート — investors.nxera.life (#6) `A`
- ✅ **0.6337** [on_target=0.97 evidence=0.65] [PDF] Presentation title - Nxera Pharma — investors.nxera.life (#9) `A`
- ✅ **0.6141** [on_target=0.94 evidence=0.65] Consolidated Financial Results for the Nine months Ended September 30, 2024 — finance.stockweather.co.jp (#4) `A`
- ✅ **0.5888** [on_target=0.92 evidence=0.64] [PDF] Environment, Social & Governance Report - Investors — investors.nxera.life (#2) `A`

## q045

**Objective:** BMF-500 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** BMF-500 · anchors ['BMF-500']

**q045-batch** `BMF-500 first regulatory approval AML || BMF-500 expected regulatory approval AML || BMF-500 market launch AML || BMF-500 expected launch date AML` → kept 10/10, jev 346 ms

- ✅ **0.8672** [on_target=0.96 evidence=0.90] Biomea Fusion (BMEA) FDA Approvals, PDUFA Dates & Drug Alerts 2026 $BMEA — marketbeat.com (#7) `A`
- ✅ **0.8471** [on_target=0.97 evidence=0.87] BMF-500 - Drug Targets, Indications, Patents — synapse.patsnap.com (#1) `A`
- ✅ **0.837** [on_target=0.90 evidence=0.93] 10-K - SEC.gov — sec.gov (#5) `A`
- ✅ **0.831** [on_target=0.97 evidence=0.86] EX-99.1 — sec.gov (#3) `A`
- ✅ **0.8051** [on_target=0.97 evidence=0.83] Biomea Fusion, Inc. — synapse.patsnap.com (#4) `A`
- ✅ **0.7404** [on_target=0.97 evidence=0.76] Biomea Fusion Announces FDA Clearance of Investigational New Drug (IND) Application for Covalent FLT — investors.biomeafusion.com (#9) `A`
- ✅ **0.7363** [on_target=0.94 evidence=0.78] Loading Inline Form. — sec.gov (#2) `A`
- ✅ **0.6855** [on_target=0.97 evidence=0.71] A Phase 1, Study of BMF-500 in Adults With Acute Leukemia - Clinical Trial for Acute Myeloid Leukemi — trials.co (#10) `A`
- ✅ **0.6762** [on_target=0.98 evidence=0.69] Biomea Fusion Reports Second Quarter 2025 Financial ... — investors.biomeafusion.com (#8) `A`
- ✅ **0.6048** [on_target=0.96 evidence=0.63] BMF-500 / Biomea Fusion - LARVOL DELTA — delta.larvol.com (#6) `A`

## q046

**Objective:** BW-101 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** BW-101 · anchors ['BW-101']

**q046-batch** `BW-101 AML regulatory approval market launch year` → kept 1/10, jev 359 ms

- ✅ **0.8524** [on_target=0.91 evidence=0.94] Delving into the Latest Updates on BW-101 with Synapse — synapse.patsnap.com (#1) `A`
- ❌ low_on_target **0.1571** [on_target=0.31 evidence=0.51] Acute Myeloid Leukemia Market Summary — delveinsight.com (#10)
- ❌ low_on_target **0.0147** [on_target=0.34 evidence=0.04] NCI Drug Dictionary — cancer.gov (#8)
- ❌ low_on_target **0.0048** [on_target=0.29 evidence=0.02] MeSH Linked Data — id.nlm.nih.gov (#5)
- ❌ low_on_target **0.0025** [on_target=0.37 evidence=0.01] Pipeline - BeOne Medical Affairs / Global — beonemedaffairs.com (#4)
- ❌ low_on_target **0.0008** [on_target=0.03 evidence=0.03] Regulatory timeline - OnCo — onco.cc (#7)
- ❌ low_on_target **0.0002** [on_target=0.05 evidence=0.00] NDA and BLA Approvals — fda.gov (#2)
- ❌ low_on_target **0.0** [on_target=0.18 evidence=0.00] JavaScript is required... — pubchem.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0** [on_target=0.34 evidence=0.00] Disclaimer — bioinvent.se (#6)
- ❌ low_on_target **0.0** [on_target=0.02 evidence=0.00] ANNUAL REPORT - nbfira.org.bw — nbfira.org.bw (#9)

## q047

**Objective:** Dual CDK12/13 Inhibitor first regulatory approval or market launch year for acute myeloid leukemia  
**Target sent:** Dual CDK12/13 Inhibitor / CDK12 · anchors ['Dual CDK12/13 Inhibitor', 'CDK12']

**q047-batch** `Dual CDK12/13 Inhibitor Insilico Medicine AML approval launch || Dual CDK12/13 Inhibitor Insilico Medicine AML regulatory timeline || Dual CDK12/13 Inhibitor AML first market launch year` → kept 9/10, jev 363 ms

- ✅ **0.5974** [on_target=0.87 evidence=0.69] JMC｜With generative AI assistance, Insilico Medicine ... — eurekalert.org (#5) `A`
- ✅ **0.5945** [on_target=0.87 evidence=0.68] CDK12/13 TARGET therapy (InSilico Medicine) - Patsnap Synapse — synapse.patsnap.com (#10) `A`
- ✅ **0.5814** [on_target=0.89 evidence=0.65] CDK12/13 — insilico.com (#2) `A`
- ✅ **0.5383** [on_target=0.85 evidence=0.63] Press Releases — insilico.com (#1) `A`
- ✅ **0.5242** [on_target=0.85 evidence=0.62] Insilico Medicine — siliconvalleyinvestclub.com (#3) `A`
- ✅ **0.504** [on_target=0.84 evidence=0.60] Insilico Medicine's Post - LinkedIn — linkedin.com (#9) `A`
- ✅ **0.4811** [on_target=0.82 evidence=0.59] CDK12 inhib News — sigma.larvol.com (#6) `A`
- ✅ **0.4337** [on_target=0.77 evidence=0.56] Design, Synthesis, and Biological Evaluation of Novel Orally ... — colab.ws (#4) `A`
- ✅ **0.4232** [on_target=0.69 evidence=0.61] Insilico Medicine News — sigma.larvol.com (#7) `A`
- ❌ low_on_target **0.0005** [on_target=0.05 evidence=0.01] Media Kit — insilico.com (#8)

## q048

**Objective:** dCASP1-55 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** dCASP1-55 · anchors ['dCASP1-55']

**q048-batch** `dCASP1-55 AML regulatory approval || dCASP1-55 AML market launch || dCASP1-55 University of Cincinnati AML clinical development` → ABSTAIN, jev 388 ms

- ❌ low_on_target **0.0115** [on_target=0.23 evidence=0.05] CLINICAL TRIALS — amgentrials.com (#8)
- ❌ low_on_target **0.007** [on_target=0.05 evidence=0.14] AML, sickle cell disease research among highlights of ASH abstracts — uc.edu (#3)
- ❌ low_on_target **0.004** [on_target=0.12 evidence=0.03] ��x���mE��8�Y"�ɒ^�����QrW��0.�7�*�4�2� ���J��w�in�QM����!���c,��0��/���2^�P���x�ߖ73�� ��y.�]���4ي� i — dailymed.nlm.nih.gov (#7)
- ❌ low_on_target **0.0017** [on_target=0.17 evidence=0.01] Press Release-CStone Pharmaceuticals — cstonepharma.com (#2)
- ❌ low_on_target **0.0005** [on_target=0.02 evidence=0.03] Clinical Trials - College of Medicine - University of Cincinnati — med.uc.edu (#6)
- ❌ low_on_target **0.0001** [on_target=0.03 evidence=0.00] Search / AML Hub — aml-hub.com (#5)
- ❌ low_on_target **0.0** [on_target=0.23 evidence=0.00] Internal Server Error — cdas.cancer.gov (#1)
- ❌ low_on_target **0.0** [on_target=0.10 evidence=0.00] Circulars & Announcements-CStone Pharmaceuticals — cstonepharma.com (#4)
- ❌ low_on_target **0.0** [on_target=0.09 evidence=0.00] Page Not Found — mayo.edu (#9)
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] AML Intelligence — amlintelligence.com (#10)

## q049

**Objective:** ABSK131 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in MTAP-Deleted KRAS G12D-Mutated Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** ABSK131 · anchors ['ABSK131']

**q049-batch** `ABSK131 SU.86.86 monotherapy TGI || ABSK131 PDAC xenograft monotherapy tumour regression || ABSK131 KRAS G12D PDAC in vivo monotherapy || ABSK131 MTAP-deleted pancreatic xenograft tumour volume` → kept 6/10, jev 411 ms

- ✅ **0.6828** [on_target=0.98 evidence=0.70] ABSK131 / Abbisko - LARVOL DELTA — delta.larvol.com (#2) `A`
- ✅ **0.6598** [on_target=0.98 evidence=0.67] IDE397 / Ideaya Biosci - LARVOL DELTA — delta.larvol.com (#10) `A`
- ✅ **0.6496** [on_target=0.96 evidence=0.68] MTA-PRMT5 - Drugs, Indications, Patents — synapse.patsnap.com (#1) `A`
- ✅ **0.64** [on_target=0.96 evidence=0.67] [PDF] Abbisko Cayman Limited 和譽開曼有限責任公司 - HKEXnews — www1.hkexnews.hk (#8) `A`
- ✅ **0.5432** [on_target=0.97 evidence=0.56] AACR 2026 / Abbisko Therapeutics Showcases Six Research Advances Highlighting pan-KRAS, 4th Generati — biospace.com (#4) `A`
- ✅ **0.5376** [on_target=0.96 evidence=0.56] Abbisko Cayman Limited 和譽開曼有限責任公司 — hkexnews.hk (#7) `A`
- ❌ low_on_target **0.0275** [on_target=0.11 evidence=0.25] KRAS G12D targeted therapies for pancreatic cancer - PMC - NIH — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0207** [on_target=0.09 evidence=0.23] KRAS: the Achilles' heel of pancreas cancer biology — jci.org (#6)
- ❌ low_on_target **0.0187** [on_target=0.07 evidence=0.27] Kras G12d — tandfonline.com (#3)
- ❌ low_on_target **0.001** [on_target=0.06 evidence=0.02] Pan-cancer clinical and molecular landscape of MTAP ... — sciencedirect.com (#5)

## q050

**Objective:** ONC201/dordaviprone in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** ONC201/dordaviprone / ONC201 / dordaviprone · anchors ['ONC201/dordaviprone', 'ONC201', 'dordaviprone']

**q050-batch** `ONC201/dordaviprone PDAC monotherapy xenograft tumour growth inhibition` → kept 8/10, jev 345 ms

- ✅ **0.6496** [on_target=0.96 evidence=0.68] Oncoceutics, Inc. - Drug pipelines, Patents, Clinical trials — synapse.patsnap.com (#2) `A`
- ✅ **0.637** [on_target=0.98 evidence=0.65] Dordaviprone/ONC201 Activation of the ClpP Mitochondrial ... - PMC — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.5921** [on_target=0.95 evidence=0.62] Preclinical efficacy and mechanism of action of dordaviprone in H3 K27M-mutant diffuse glioma — academic.oup.com (#1) `A`
- ✅ **0.592** [on_target=0.96 evidence=0.62] Preclinical efficacy and mechanism of action of dordaviprone in H3 ... — academic.oup.com (#4) `A`
- ✅ **0.5826** [on_target=0.92 evidence=0.63] Neuro-Oncology — pdfs.semanticscholar.org (#7) `A`
- ✅ **0.5671** [on_target=0.94 evidence=0.60] 29 — touchoncology.com (#3) `A`
- ✅ **0.5652** [on_target=0.98 evidence=0.58] dordaviprone (ONC201) — drughunter.com (#6) `A`
- ✅ **0.5549** [on_target=0.93 evidence=0.60] A review of current therapeutics targeting the mitochondrial protease ClpP in diffuse midline glioma — academic.oup.com (#10) `A`
- ❌ low_evidence **0.4136** [on_target=0.94 evidence=0.44] dordaviprone - NCI Drug Dictionary - National Cancer Institute — cancer.gov (#8) `A`
- ❌ low_evidence **0.399** [on_target=0.95 evidence=0.42] ONC201 (Dordaviprone) in Recurrent H3 K27M-Mutant Diffuse ... — pubmed.ncbi.nlm.nih.gov (#9) `A`

## q051

**Objective:** DWP216 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in KRAS G12C Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** DWP216 · anchors ['DWP216']

**q051-batch** `DWP216 KRAS G12C pancreatic ductal adenocarcinoma monotherapy xenograft tumour growth inhibition regression` → ABSTAIN, jev 363 ms

- ❌ low_on_target **0.1066** [on_target=0.23 evidence=0.46] KRAS Inhibition in Pancreatic Ductal Adenocarcinoma - PMC - NIH — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0487** [on_target=0.17 evidence=0.29] KRAS G12C Inhibitors: Clinical Progress, Resistance Mechanisms ... — noah.bio (#2)
- ❌ low_on_target **0.0443** [on_target=0.16 evidence=0.28] Targeting KRAS in PDAC: A New Way to Cure It? — mdpi.com (#9)
- ❌ low_on_target **0.0429** [on_target=0.13 evidence=0.33] Direct GDP-KRASG12C inhibitors and mechanisms of resistance: the tip of the iceberg - Joshua C. Rose — journals.sagepub.com (#7)
- ❌ low_on_target **0.0279** [on_target=0.09 evidence=0.31] Frontiers / Evaluation of KRAS inhibitor-directed therapies for pancreatic cancer treatment — frontiersin.org (#6)
- ❌ low_on_target **0.0258** [on_target=0.09 evidence=0.29] Broad-Spectrum RAS Inhibition in Pancreatic Ductal Adenocarcinoma: Mechanistic Advances and Therapeu — mdpi.com (#10)
- ❌ low_on_target **0.0257** [on_target=0.11 evidence=0.23] Modeling response to the KRAS-G12C inhibitor AZD4625 in KRAS G12C NSCLC patient-derived xenografts r — nature.com (#1)
- ❌ low_on_target **0.0207** [on_target=0.09 evidence=0.23] Targeting KRAS in pancreatic cancer - PMC - NIH — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0184** [on_target=0.08 evidence=0.23] KRAS inhibitors: resistance drivers and combinatorial strategies — cell.com (#8)
- ❌ low_on_target **0.0124** [on_target=0.06 evidence=0.21] Kras G12d — tandfonline.com (#4)

## q052

**Objective:** HM100714 in vivo efficacy in combination with another agent in Head and Neck Squamous Cell Carcinoma, including the combination partner  
**Target sent:** HM100714 · anchors ['HM100714']

**q052-batch** `HM100714 HNSCC combination in vivo efficacy || HM100714 head and neck squamous cell carcinoma xenograft combination || HM100714 combination partner xenograft || HM100714 AACR HNSCC combination || HM100714 cisplatin or pembrolizumab HNSCC` → kept 3/10, jev 383 ms

- ✅ **0.624** [on_target=0.96 evidence=0.65] “비만 넘어 항암으로 혁신 확장”…한미, AACR서 차세대 신약 대거 공개 — hanmi.co.kr (#2) `A`
- ✅ **0.6079** [on_target=0.97 evidence=0.63] Hanmi Showcases Next Generation Drug Innovations at AACR — hanmipharm.com (#5) `A`
- ✅ **0.494** [on_target=0.95 evidence=0.52] 1744602650044.docx — hanmi.co.kr (#6) `A`
- ❌ low_evidence **0.3697** [on_target=0.94 evidence=0.39] Hanmi Records Highest Number of AACR Presentations ... — hanmipharm.com (#1) `A`
- ❌ low_on_target **0.042** [on_target=0.15 evidence=0.28] Frontiers / Head and neck cancer – emerging targeted therapies — frontiersin.org (#10)
- ❌ low_on_target **0.0251** [on_target=0.13 evidence=0.19] FDA Approves Pembrolizumab for First-Line Treatment ... — ons.org (#8)
- ❌ low_on_target **0.0103** [on_target=0.07 evidence=0.15] Real-world use of first-line pembrolizumab + platinum + ... — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.008** [on_target=0.05 evidence=0.16] ASCO Publishes New Guideline on Immunotherapy, Biomarker Testing in Advanced Head and Neck Cancer — dailynews.ascopubs.org (#7)
- ❌ low_on_target **0.0072** [on_target=0.07 evidence=0.10] Efficacy and safety of the neoadjuvant chemoimmunotherapy with ... — frontiersin.org (#9)
- ❌ low_on_target **0.0037** [on_target=0.04 evidence=0.09] Immunotherapy and Biomarker Testing in Recurrent and Metastatic Head and Neck Cancers: ASCO Guidelin — ascopubs.org (#3)

## q053

**Objective:** ADT-1004 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** ADT-1004 · anchors ['ADT-1004']

**q053-batch** `ADT-1004 quantitative tumour growth inhibition percentage PDAC monotherapy || ADT-1004 tumour regression percentage MIA PaCa-2 xenograft || ADT-1004 KRAS G12D PDX tumour shrinkage monotherapy || ADT-1004 KPC orthotopic tumour volume change day 27 || ADT-1004 MIA-AMG-R xenograft final tumour volume monotherapy` → kept 10/10, jev 388 ms

- ✅ **0.9151** [on_target=0.95 evidence=0.96] Abstract 7236: Selective deletion of the KRAS mutant gene with ADGN-123 and ADGN-121 peptide-RNA nan — bohrium.dp.tech (#7) `A`
- ✅ **0.9042** [on_target=0.99 evidence=0.91] ADT-1004: a first-in-class, oral pan-RAS inhibitor with robust ... — link.springer.com (#1) `A`
- ✅ **0.8679** [on_target=0.99 evidence=0.88] ADT-1004: a first-in-class, oral pan-RAS inhibitor with ... - PubMed — pubmed.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.833** [on_target=0.98 evidence=0.85] Pan-RAS Inhibitors: Expanding Therapeutic Potential and Evading Resistance — mdpi.com (#6) `A`
- ✅ **0.7755** [on_target=0.99 evidence=0.78] A potent and selective pan-RAS inhibitor, ADT-1004, targeting complex KRAS mutations for pancreatic  — ascopubs.org (#9) `A`
- ✅ **0.7677** [on_target=0.94 evidence=0.82] Abstract LB_B26: Efficacy and tolerability of a novel pan-RAS inhibitor with a unique mechanism of s — aacrjournals.org (#10) `A`
- ✅ **0.7392** [on_target=0.96 evidence=0.77] Key Considerations for Targeting KRAS in Pancreatic Cancer - PMC — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.6976** [on_target=0.96 evidence=0.73] Adt-1004: A First-in-Class, Orally Bioavailable Selective ... — augusta.elsevierpure.com (#4) `A`
- ✅ **0.611** [on_target=0.94 evidence=0.65] Emerging KRAS G12D inhibitor in the treatment of digestive ... — pmc.ncbi.nlm.nih.gov (#8) `A`
- ✅ **0.539** [on_target=0.86 evidence=0.63] Kras G12d — tandfonline.com (#3) `A`

## q054

**Objective:** DWP216 in vivo animal models and results: cell-line xenograft (CDX), patient-derived xenograft (PDX), syngeneic, orthotopic, or genetically engineered models  
**Target sent:** DWP216 · anchors ['DWP216']

**q054-batch** `DWP216 HNSCC in vivo xenograft monotherapy || DWP216 NCI-H1373 monotherapy tumour volume || DWP216 pancreatic cancer PDX syngeneic orthotopic || DWP216 CAPAN-1 xenograft monotherapy 1200 mm3 || DWP216 genetically engineered mouse model` → kept 1/10, jev 357 ms

- ✅ **0.7122** [on_target=0.98 evidence=0.73] [PDF] Development of DWP216, a TEAD1 selective inhibitor for NF2 ... — kddf.org (#1) `A`
- ❌ low_evidence **0.4064** [on_target=0.96 evidence=0.42] pan-TEAD inhib News — sigma.larvol.com (#4) `A`
- ❌ low_on_target **0.02** [on_target=0.06 evidence=0.33] Patient Derived Xenograft — tumor.informatics.jax.org (#2)
- ❌ low_on_target **0.0184** [on_target=0.06 evidence=0.31] Pancreatic cancer PDX models - Crown Bioscience — crownbio.com (#10)
- ❌ low_on_target **0.0099** [on_target=0.09 evidence=0.11] Resource Page — wagnerlab.net (#5)
- ❌ low_on_target **0.0003** [on_target=0.08 evidence=0.00] PDC000198 - Proteomic Data Commons - National Cancer Institute — proteomic.datacommons.cancer.gov (#9)
- ❌ low_on_target **0.0002** [on_target=0.05 evidence=0.00] {{ngMeta['og:title']}} — bio.tools (#6)
- ❌ low_on_target **0.0002** [on_target=0.06 evidence=0.00] Gene search results — mousephenotype.org (#7)
- ❌ low_on_target **0.0** [on_target=0.13 evidence=0.00] Internal Server Error — cdas.cancer.gov (#3)
- ❌ low_on_target **0.0** [on_target=0.03 evidence=0.00] Cloudflare — advancesradonc.org (#8)

## q055

**Objective:** DB-1305/Anti-PD-L1/VEGF Bispecific Antibody patients studied in Recurrent or Disseminated HNSCC (Oral Cavity/Oropharynx/Hypopharynx/Larynx), Incurable by Local Therapies trials: biomarker selection, disease severity, line of therapy, and required prior treatment  
**Target sent:** DB-1305 · anchors ['DB-1305']

**q055-batch** `DB-1305 recurrent metastatic HNSCC prior treatment line of therapy || DB-1305 HNSCC PD-L1 biomarker eligibility || DB-1305 HNSCC ECOG measurable disease inclusion criteria` → kept 2/10, jev 384 ms

- ✅ **0.5786** [on_target=0.80 evidence=0.72] DB-1311 in Combination With BNT327 or DB-1305 ... — uclahealth.org (#1) `A`
- ✅ **0.4669** [on_target=0.87 evidence=0.54] Head and Neck Squamous Cell Carcinoma clinical trials at UCLA — ucla.clinicaltrials.researcherprofiles.org (#10) `A`
- ❌ low_evidence **0.3256** [on_target=0.74 evidence=0.44] UCLA Squamous Cell Carcinoma Clinical Trials — Los Angeles — ucla.clinicaltrials.researcherprofiles.org (#7) `A`
- ❌ low_on_target **0.04** [on_target=0.12 evidence=0.33] Immune biomarkers for head and neck cancer - PMC — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0291** [on_target=0.09 evidence=0.32] Driving Progress in Recurrent and Metastatic Head and Neck Cancer — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0264** [on_target=0.08 evidence=0.33] Immunotherapy in recurrent/metastatic head and neck ... - PMC — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0233** [on_target=0.07 evidence=0.33] PD-L1 Testing in Cancer - MyPathologyReport — mypathologyreport.ca (#4)
- ❌ low_on_target **0.0227** [on_target=0.08 evidence=0.28] PD-L1: Test Selection Guide — testdirectory.questdiagnostics.com (#3)
- ❌ low_on_target **0.0162** [on_target=0.05 evidence=0.32] Immunotherapy in Recurrent/Metastatic Squamous Cell ... — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0157** [on_target=0.05 evidence=0.31] Immunotherapy and Biomarker Testing in Recurrent and Metastatic Head and Neck Cancers: ASCO Guidelin — ascopubs.org (#2)

## q056

**Objective:** MNPS Asset planned or expected data readouts, regulatory submissions, regulatory decisions, and expected timing in Head and Neck Cancer  
**Target sent:** MNPS · anchors ['MNPS']

**q056-batch** `MNPS Asset first-line recurrent metastatic head and neck cancer data readout || MNPS Asset head and neck cancer regulatory submission || MNPS Asset head and neck cancer regulatory decision` → ABSTAIN, jev 433 ms

- ❌ low_on_target **0.3512** [on_target=0.43 evidence=0.82] Head & Neck Cancer / Clinical - CancerNetwork — cancernetwork.com (#8)
- ❌ low_on_target **0.3227** [on_target=0.44 evidence=0.73] Nasopharyngeal Carcinoma... — datalookout.com (#5)
- ❌ low_on_target **0.0943** [on_target=0.28 evidence=0.34] Driving Progress in Recurrent and Metastatic Head and Neck Cancer — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.054** [on_target=0.18 evidence=0.30] First-Line Therapy in Recurrent or Metastatic Head and Neck Squamous Cell Carcinoma: A Retrospective — onlinelibrary.wiley.com (#7)
- ❌ low_on_target **0.0051** [on_target=0.11 evidence=0.05] Live Head And Neck Cancer updates — miragenews.com (#3)
- ❌ low_on_target **0.001** [on_target=0.06 evidence=0.02] [PDF] 2022 Update edited by the Japan Society for Head and Neck Cancer — sciencedirect.com (#6)
- ❌ low_on_target **0.0005** [on_target=0.08 evidence=0.01] Search Page - Drug and Health Product Register — hpr-rps.hres.ca (#2)
- ❌ low_on_target **0.0** [on_target=0.14 evidence=0.00] Internal Server Error — cdas.cancer.gov (#1)
- ❌ low_on_target **0.0** [on_target=0.28 evidence=0.00] Legal News & Analysis on Litigation, Policy, Deals : Law360 — law360.com (#4)
- ❌ low_on_target **0.0** [on_target=0.03 evidence=0.00] An error occurred. — powerfulpatients.org (#9)

## q057

**Objective:** CNP200137 first regulatory approval or market launch year for acute myeloid leukemia  
**Target sent:** CNP200137 · anchors ['CNP200137']

**q057-batch** `CNP200137 regulatory approval AML || CNP200137 market launch AML` → kept 1/10, jev 452 ms

- ✅ **0.8116** [on_target=0.97 evidence=0.84] Menin Inhibitor Drug Development Pipeline: AML, Diabetes ... — inflectionlabs.bio (#1) `A`
- ❌ low_on_target **0.4879** [on_target=0.51 evidence=0.96] Regulatory timeline - OnCo — onco.cc (#10)
- ❌ low_on_target **0.2357** [on_target=0.32 evidence=0.74] Oncology (Cancer)/Hematologic Malignancies Approval ... — fda.gov (#2)
- ❌ low_on_target **0.1725** [on_target=0.26 evidence=0.66] Acute Myeloid Leukemia: 2025 Update on Diagnosis, Risk-Stratification, and Management — onlinelibrary.wiley.com (#5)
- ❌ low_on_target **0.0015** [on_target=0.15 evidence=0.01] NCATS Inxight Drugs — drugs.ncats.io (#9)
- ❌ low_on_target **0.0** [on_target=0.02 evidence=0.00] 555 Security Incident Detected — 2npharma.com (#3)
- ❌ low_on_target **0.0** [on_target=0.05 evidence=0.00] 520: Web server is returning an unknown error — q-depot.com (#4)
- ❌ low_on_target **0.0** [on_target=0.08 evidence=0.00] Circulars & Announcements-CStone Pharmaceuticals — cstonepharma.com (#6)
- ❌ low_on_target **0.0** [on_target=0.10 evidence=0.00] Please verify you are a human — zoominfo.com (#7)
- ❌ low_on_target **0.0** [on_target=0.07 evidence=0.00] Circulars & Announcements-CStone Pharmaceuticals — cstonepharma.com (#8)

## q058

**Objective:** HEC234055 in vivo efficacy in combination with another agent in Pancreatic Ductal Adenocarcinoma, including the combination partner  
**Target sent:** HEC234055 · anchors ['HEC234055']

**q058-batch** `HEC234055 combination pancreatic ductal adenocarcinoma in vivo || HEC234055 combination partner PDAC xenograft || HEC234055 AACR 2026 combination efficacy` → kept 2/10, jev 394 ms

- ✅ **0.771** [on_target=0.98 evidence=0.79] C262019A_Sunshine Pharma 1..4 — hkexnews.hk (#1) `A`
- ✅ **0.6467** [on_target=0.97 evidence=0.67] Sunshine Lake Pharma Co., Ltd. Showcases Three Innovative ... — marketscreener.com (#2) `A`
- ❌ low_on_target **0.1661** [on_target=0.33 evidence=0.50] Unbiased in vivo preclinical evaluation of anticancer drugs identifies effective therapy for the tre — pubmed.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.028** [on_target=0.14 evidence=0.20] Closing Plenary Session examined highlights from the ... — aacrmeetingnews.org (#3)
- ❌ low_on_target **0.0217** [on_target=0.10 evidence=0.22] [PDF] AACR DRUG DISCOVERY AND DEVELOPMENT (AACR D3) — aacr.org (#10)
- ❌ low_on_target **0.0147** [on_target=0.05 evidence=0.29] Advances in antibody-drug conjugates in cancer - PMC - NIH — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0053** [on_target=0.05 evidence=0.11] AACR Annual Meeting 2026 – Post-event summary — insights.bio (#4)
- ❌ low_on_target **0.0021** [on_target=0.03 evidence=0.07] AACR 2026: Emerging Antibody-Drug Conjugates for the ... — adcreview.com (#7)
- ❌ low_on_target **0.0009** [on_target=0.13 evidence=0.01] AACR 2026 — medical.emdserono.com (#8)
- ❌ low_on_target **0.0004** [on_target=0.06 evidence=0.01] RPubs — rpubs.com (#5)

## q059

**Objective:** HEC234055 in vivo animal models and results: cell-line xenograft (CDX), patient-derived xenograft (PDX), syngeneic, orthotopic, genetically engineered models  
**Target sent:** HEC234055 · anchors ['HEC234055']

**q059-batch** `HEC234055 HNSCC xenograft || HEC234055 PDX model || HEC234055 syngeneic model || HEC234055 orthotopic pancreatic model || HEC234055 genetically engineered mouse model` → kept 2/10, jev 404 ms

- ✅ **0.7404** [on_target=0.97 evidence=0.76] C262019A_Sunshine Pharma 1..4 — hkexnews.hk (#4) `A`
- ✅ **0.7113** [on_target=0.94 evidence=0.76] [PDF] E262019A_Sunshine Pharma 1..4 - HKEXnews — www1.hkexnews.hk (#1) `A`
- ❌ low_on_target **0.022** [on_target=0.12 evidence=0.18] Resource Page — wagnerlab.net (#7)
- ❌ low_on_target **0.01** [on_target=0.06 evidence=0.17] PDX Models - PDXNet — pdxnetwork.org (#9)
- ❌ low_on_target **0.0093** [on_target=0.09 evidence=0.10] PDX Model Database Registration — crownbio.com (#5)
- ❌ low_on_target **0.0043** [on_target=0.04 evidence=0.11] MMRRC Repository — mmrrc.org (#6)
- ❌ low_on_target **0.001** [on_target=0.06 evidence=0.02] Find Your Research Mouse Model 丨 ... — en.gempharmatech.com (#8)
- ❌ low_on_target **0.0008** [on_target=0.03 evidence=0.03] International Mouse Strain Resource — findmice.org (#3)
- ❌ low_on_target **0.0003** [on_target=0.05 evidence=0.01] Find Your Research Mouse Model 丨 GemPharmatech — en.gempharmatech.com (#2)
- ❌ low_on_target **0.0002** [on_target=0.06 evidence=0.00] {{ngMeta['og:title']}} — bio.tools (#10)

## q060

**Objective:** EOM613 sponsor development stage indication public source  
**Target sent:** EOM613 Crohn's disease / EOM613 · anchors ["EOM613 Crohn's disease", 'EOM613']

**q060-batch** `EOM613 Crohn's disease trial current status || EOM613 Crohn's disease Phase 2 initiation 2026 || EOM613 Crohn's disease clinical trial registry` → kept 6/10, jev 387 ms

- ✅ **0.967** [on_target=0.98 evidence=0.99] EOM Pharmaceutical Holdings Reports Promising Preclinical — globenewswire.com (#1) `A`
- ✅ **0.9247** [on_target=0.97 evidence=0.95] EOM Pharmaceutical Holdings Reports FDA Clearance of ... — globenewswire.com (#2) `A`
- ✅ **0.869** [on_target=0.98 evidence=0.89] EOM Pharmaceutical Holdings Provides an Update on its Lead Drug Candidate EOM613 — prnewswire.com (#6) `A`
- ✅ **0.831** [on_target=0.97 evidence=0.86] ImmunoCellular Therapeutics Ltd. - Drug pipelines, Patents, Clinical ... — synapse.patsnap.com (#3) `A`
- ✅ **0.7854** [on_target=0.95 evidence=0.83] FDA Clears IND for EOM613 Trial in Cancer Cachexia Patients — clinicaltrialvanguard.com (#10) `A`
- ✅ **0.4648** [on_target=0.73 evidence=0.64] EOM Pharmaceutical Holdings Reports FDA Clearance of ... — finance.yahoo.com (#8) `A`
- ❌ low_evidence **0.4508** [on_target=0.92 evidence=0.49] Methods of treating inflammatory bowel diseases — patents.google.com (#9) `A`
- ❌ low_on_target **0.0007** [on_target=0.07 evidence=0.01] Clinical Trials in the European Union - EMA — euclinicaltrials.eu (#4)
- ❌ low_on_target **0.0004** [on_target=0.04 evidence=0.01] Find Studies / ClinicalTrials.gov — clinicaltrials.gov (#7)
- ❌ low_on_target **0.0001** [on_target=0.03 evidence=0.00] ICTRP Search Portal - World Health Organization (WHO) — who.int (#5)

## q061

**Objective:** FG-3149 sponsor development stage indication public source  
**Target sent:** FG-3149 · anchors ['FG-3149']

**q061-batch** `FG-3149 sponsor development stage || FG-3149 Crohn's disease || FG-3149 FibroGen clinical development` → kept 2/10, jev 374 ms

- ✅ **0.6608** [on_target=0.84 evidence=0.79] Efficacy and safety of filgotinib as induction and maintenance therapy for Crohn's disease (DIVERSIT — thelancet.com (#10)
- ✅ **0.6438** [on_target=0.74 evidence=0.87] Our Partners - FibroGen — fibrogen.com (#6)
- ❌ low_on_target **0.3192** [on_target=0.38 evidence=0.84] FibroGen / Drug Developments / Pipeline Prospector — pharmacompass.com (#9)
- ❌ low_on_target **0.0282** [on_target=0.53 evidence=0.05] FibroGen : Corporate Presentation - September 2025 — marketscreener.com (#7)
- ❌ low_on_target **0.0155** [on_target=0.15 evidence=0.10] Kyntra Bio - Wikipedia — en.wikipedia.org (#3)
- ❌ low_on_target **0.0127** [on_target=0.20 evidence=0.06] New weapons for the management of perianal Crohn's disease — oamonitor.ireland.openaire.eu (#1)
- ❌ low_on_target **0.0085** [on_target=0.08 evidence=0.11] Serum biomarkers of fibrostenotic Crohn's disease — onlinelibrary.wiley.com (#2)
- ❌ low_on_target **0.0075** [on_target=0.45 evidence=0.02] FibroGen Inc. (NASDAQ:FGEN) : Ptab Cases :: Law360 — law360.co.uk (#4)
- ❌ low_on_target **0.0053** [on_target=0.08 evidence=0.07] FibroGen Reports First Quarter 2024 Financial Results — investor.kyntrabio.com (#5)
- ❌ low_on_target **0.0024** [on_target=0.04 evidence=0.06] FibroGen, Inc. (NASDAQ:FGEN) Q1 2024 Earnings Conference Call ... — reportify-1252068037.cos.ap-beijing.myqcloud.com (#8)

## q062

**Objective:** HDM-3018 sponsor Huadong Medicine Co. Ltd., development stage Preclinical, and indication Inflammatory Bowel Disease  
**Target sent:** HDM-3018 · anchors ['HDM-3018']

**q062-batch** `HDM-3018 Huadong Medicine sponsor || HDM-3018 development stage || HDM-3018 inflammatory bowel disease indication` → kept 1/10, jev 361 ms

- ✅ **0.9702** [on_target=0.98 evidence=0.99] HDM3018 - Drug Targets, Indications, Patents - Synapse — synapse.patsnap.com (#1) `A`
- ❌ low_on_target **0.1179** [on_target=0.52 evidence=0.23] Huadong Medicine Co., Ltd. - Drug pipelines, Patents, ... — synapse.patsnap.com (#3)
- ❌ low_on_target **0.0821** [on_target=0.28 evidence=0.29] Hangzhou Zhongmei Huadong Pharmaceutical Co., Ltd. — baike.baidu.com (#5)
- ❌ low_evidence **0.0235** [on_target=0.64 evidence=0.04] NMPA Database — nmpa.gov.cn (#7)
- ❌ low_on_target **0.0228** [on_target=0.36 evidence=0.06] Huadong Medicine partners with Heidelberg Pharma for next ... — source.gbihealth.com.cn (#10)
- ❌ low_on_target **0.003** [on_target=0.18 evidence=0.02] Huadong Medicine — en.huadongmedicine.com (#9)
- ❌ low_on_target **0.002** [on_target=0.12 evidence=0.02] Products / Huadong Medicine — en.huadongmedicine.com (#6)
- ❌ low_on_target **0.0017** [on_target=0.10 evidence=0.02] Company News — en.huadongmedicine.com (#2)
- ❌ low_on_target **0.0007** [on_target=0.21 evidence=0.00] Bloomberg — bloomberg.com (#4)
- ❌ low_on_target **0.0007** [on_target=0.21 evidence=0.00] register — academic.oup.com (#8)

## q063

**Objective:** Granisetron in Head and Neck Cancer: clinical trial population, biomarker or severity selection, line of therapy, and required prior treatment  
**Target sent:** Granisetron · anchors ['Granisetron']

**q063-batch** `Granisetron recurrent metastatic head and neck cancer clinical trial eligibility || Granisetron head and neck cancer Phase 2 prior treatment || Granisetron head and neck cancer biomarker ECOG || Granisetron Kyowa Kirin head and neck cancer trial` → kept 1/10, jev 384 ms

- ✅ **0.6758** [on_target=0.97 evidence=0.70] Comparison of an extended-release formulation of granisetron ... — link.springer.com (#10) `A`
- ❌ low_on_target **0.1302** [on_target=0.18 evidence=0.72] NCT00588770 — loyolamedicine.org (#1)
- ❌ low_on_target **0.0915** [on_target=0.14 evidence=0.65] A Study for Participants With Recurrent or Metastatic ... — clinicaltrials.gov (#2)
- ❌ low_evidence **0.0679** [on_target=0.97 evidence=0.07] Granisetron Monograph for Professionals — drugs.com (#5) `A`
- ❌ low_on_target **0.0246** [on_target=0.06 evidence=0.41] A Study for Patients With Recurrent or Metastatic Squamous Cell Head and Neck Cancer — clinicaltrials.gov (#7)
- ❌ low_on_target **0.0129** [on_target=0.04 evidence=0.32] Clinical Trials — med.stanford.edu (#6)
- ❌ low_on_target **0.0085** [on_target=0.03 evidence=0.28] Clinical Trial 23276 — moffitt.org (#4)
- ❌ low_on_target **0.0063** [on_target=0.04 evidence=0.16] Clinical Trial 23691 / Moffitt — moffitt.org (#8)
- ❌ low_on_target **0.0013** [on_target=0.02 evidence=0.07] Surgery Clinical Trials — med.stanford.edu (#9)
- ❌ low_on_target **0.0002** [on_target=0.01 evidence=0.02] Axitinib in Treating Patients with Recurrent or Metastatic Head and ... — cancer.gov (#3)

## q064

**Objective:** HPV Vaccine (HAd5 Vector) in Head and Neck Cancer: clinical trial population, biomarker or severity selection, line of therapy, and required prior treatment  
**Target sent:** HPV Vaccine (HAd5 Vector) ImmunityBio / HAd5 · anchors ['HPV Vaccine (HAd5 Vector) ImmunityBio', 'HAd5']

**q064-batch** `HPV Vaccine (HAd5 Vector) ImmunityBio head and neck cancer clinical trial eligibility || HPV Vaccine (HAd5 Vector) ImmunityBio HPV biomarker head and neck cancer || HPV Vaccine (HAd5 Vector) ImmunityBio recurrent metastatic head and neck cancer prior treatment || HPV Vaccine (HAd5 Vector) ImmunityBio phase 2 trial inclusion criteria` → kept 6/10, jev 449 ms

- ✅ **0.9474** [on_target=0.97 evidence=0.98] NCT07628062 / Phase 2 Study of NAI, HPV Vaccine, and Nab ... — clinicaltrials.gov (#3) `A`
- ✅ **0.8284** [on_target=0.86 evidence=0.96] Clinical Trials — mayo.edu (#6)
- ✅ **0.8209** [on_target=0.94 evidence=0.87] Human Papillomavirus — immunitybio.com (#4) `A`
- ✅ **0.7735** [on_target=0.85 evidence=0.91] HPV+ / HPV- 2nd Line Head & Neck Cancer — immunitybio.com (#2)
- ✅ **0.7308** [on_target=0.87 evidence=0.84] Patients & Caregivers — immunitybio.com (#1)
- ✅ **0.5007** [on_target=0.83 evidence=0.60] Annual Report — ir.immunitybio.com (#8) `A`
- ❌ low_on_target **0.0669** [on_target=0.34 evidence=0.20] NCT04537156 / Efficacy, Immunogenicity and Safety Study ... — clinicaltrials.gov (#10)
- ❌ low_on_target **0.0293** [on_target=0.10 evidence=0.29] Head and Neck Cancer Clinical Trials — ccr.cancer.gov (#9)
- ❌ low_on_target **0.0148** [on_target=0.06 evidence=0.25] Head and Neck Cancer - Cancer Research Institute — cancerresearch.org (#7)
- ❌ low_on_target **0.0007** [on_target=0.02 evidence=0.04] a phase 2/3, placebo-controlled — cdn.clinicaltrials.gov (#5)


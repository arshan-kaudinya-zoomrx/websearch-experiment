# Jev inspect: 20261004-174800__jev-jev_v2-on_target0.7-evidence0.5-k5__on__20261003-175621__perplexity-pplx_web_default__queries

Config `jev_v2-on_target0.7-evidence0.5-k5` (per_link), select={"keep_threshold": 0.5, "max_keep": 5, "gates": {"on_target": 0.7, "evidence": 0.5}}. Reasons: {"low_on_target": 1002, "kept": 651, "max_keep": 281, "low_evidence": 150}. Answer means: {"on_target": 0.59, "evidence": 0.465}.

Legend: ✅ kept · ❌ dropped (reason) · `A` = mentions the anchor · scores are Jev's answers in [0, 1].

## q001

**Objective:** Tamuzimod safety findings and adverse events in Moderately to severely active ulcerative colitis Ulcerative Colitis  
**Target sent:** Tamuzimod · anchors ['Tamuzimod']

**q001-2** `Tamuzimod maintenance adverse events ulcerative colitis` → kept 5/10, jev 498 ms

- ✅ **0.9867** [on_target=0.99 evidence=1.00] [PDF] Efficacy and safety of tamuzimod in moderately to severely active ... — ventyxbio.com (#1) `A`
- ✅ **0.9801** [on_target=0.99 evidence=0.99] Advancements in therapeutic strategies and drug ... — explorationpub.com (#9) `A`
- ✅ **0.9635** [on_target=0.97 evidence=0.99] Articles Tamuzimod in patients with moderately-to-severely active ulcerative colitis: a multicentre, — sciencedirect.com (#10) `A`
- ✅ **0.8827** [on_target=0.91 evidence=0.97] Silvio Danese - ScienceDirect.com — sciencedirect.com (#2) `A`
- ✅ **0.882** [on_target=0.90 evidence=0.98] Ulcerative colitis, active moderate - Drugs, Targets, Patents — synapse.patsnap.com (#5) `A`
- ❌ max_keep **0.8788** [on_target=0.98 evidence=0.90] Sphingosine-1-Phosphate (S1P) Receptor Modulators for the ... - PMC — pmc.ncbi.nlm.nih.gov (#3) `A`
- ❌ max_keep **0.8741** [on_target=0.88 evidence=0.99] Clinical Endpoint Outcomes — academic.oup.com (#8)
- ❌ max_keep **0.8352** [on_target=0.96 evidence=0.87] UEG Week 2024 - CONFERENCE REPORTPEER-REVIEWED — conferences.medicom-publishers.com (#4) `A`
- ❌ max_keep **0.6423** [on_target=0.94 evidence=0.68] Sphingosine 1-Phosphate (S1P) Receptor Modulators as ... - PubMed — pubmed.ncbi.nlm.nih.gov (#7) `A`
- ❌ low_on_target **0.2985** [on_target=0.45 evidence=0.66] Mirikizumab as Induction and Maintenance Therapy for Ulcerative Colitis / NEJM — nejm.org (#6)

**q001-1** `Tamuzimod long-term extension safety ulcerative colitis` → kept 5/10, jev 543 ms

- ✅ **0.8504** [on_target=0.97 evidence=0.88] The Current Sphingosine 1 Phosphate Receptor Modulators ... - PMC — pmc.ncbi.nlm.nih.gov (#6) `A`
- ✅ **0.8471** [on_target=0.97 evidence=0.87] UEG Week 2024 - CONFERENCE REPORTPEER-REVIEWED — conferences.medicom-publishers.com (#5) `A`
- ✅ **0.8232** [on_target=0.98 evidence=0.84] [PDF] Efficacy and safety of tamuzimod in moderately to severely active ... — ventyxbio.com (#1) `A`
- ✅ **0.722** [on_target=0.98 evidence=0.74] tamuzimod (VTX002) / Eli Lilly — delta.larvol.com (#7) `A`
- ✅ **0.6798** [on_target=0.99 evidence=0.69] Ventyx Biosciences Presents New 52-Week Results from the Phase ... — nasdaq.com (#4) `A`
- ❌ max_keep **0.673** [on_target=0.98 evidence=0.69] Ventyx Biosciences' Tamuzimod Shows Promising Long-Term ... — trial.medpath.com (#10) `A`
- ❌ max_keep **0.601** [on_target=0.98 evidence=0.61] EX-99.1 - SEC.gov — sec.gov (#3) `A`
- ❌ max_keep **0.4824** [on_target=0.72 evidence=0.67] Silvio Danese - ScienceDirect.com — sciencedirect.com (#2) `A`
- ❌ low_on_target **0.4443** [on_target=0.49 evidence=0.91] Interim Analysis of the True North Open-label Extension / Journal of ... — academic.oup.com (#9)
- ❌ low_on_target **0.3304** [on_target=0.59 evidence=0.56] VTX002 Versus Placebo for the Treatment of Moderately to Severely ... — trial.medpath.com (#8)

**q001-4** `Tamuzimod open-label extension adverse events` → kept 5/10, jev 381 ms

- ✅ **0.9536** [on_target=0.96 evidence=0.99] Silvio Danese - ScienceDirect.com — sciencedirect.com (#2) `A`
- ✅ **0.9244** [on_target=0.98 evidence=0.94] Font.pdf — sec.gov (#4) `A`
- ✅ **0.8722** [on_target=0.98 evidence=0.89] 10-K — sec.gov (#3) `A`
- ✅ **0.8464** [on_target=0.92 evidence=0.92] Ventyx Corporate Presentation - datocms-assets.com — datocms-assets.com (#1)
- ✅ **0.8217** [on_target=0.85 evidence=0.97] Interim analysis of the long-term efficacy and safety ... — pubmed.ncbi.nlm.nih.gov (#7)
- ❌ max_keep **0.7128** [on_target=0.88 evidence=0.81] UEG Week 2024 - CONFERENCE REPORTPEER-REVIEWED — conferences.medicom-publishers.com (#6) `A`
- ❌ max_keep **0.5921** [on_target=0.95 evidence=0.62] tamuzimod (VTX002) / Eli Lilly — delta.larvol.com (#8) `A`
- ❌ low_on_target **0.1666** [on_target=0.51 evidence=0.33] Safety Patterns over Time with Ozanimod During an Open-label Extension Trial in Patients with Relaps — neurology.org (#9)
- ❌ low_on_target **0.1112** [on_target=0.29 evidence=0.38] The Current Sphingosine 1 Phosphate Receptor Modulators ... - PMC — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ low_on_target **0.0003** [on_target=0.03 evidence=0.01] Long-term effects of tafamidis for the treatment of transthyretin familial amyloid polyneuropathy — link.springer.com (#5)

**q001-3** `Tamuzimod UEGW 2024 safety` → kept 5/10, jev 354 ms

- ✅ **0.9702** [on_target=0.99 evidence=0.98] Tamuzimod in patients with moderately-to-severely active ... — pubmed.ncbi.nlm.nih.gov (#8) `A`
- ✅ **0.8283** [on_target=0.99 evidence=0.84] VTX002 UEGW 2024 — ir.ventyxbio.com (#1) `A`
- ✅ **0.7514** [on_target=0.98 evidence=0.77] tamuzimod (VTX002) / Eli Lilly — delta.larvol.com (#4) `A`
- ✅ **0.6828** [on_target=0.98 evidence=0.70] Ventyx Biosciences' Tamuzimod Shows Promising Long-Term ... — trial.medpath.com (#6) `A`
- ✅ **0.673** [on_target=0.98 evidence=0.69] Ventyx Biosciences' Tamuzimod Shows Promising Long-Term ... — trial.medpath.com (#5) `A`
- ❌ max_keep **0.6633** [on_target=0.99 evidence=0.67] Ventyx Biosciences Presents New 52-Week Results from the Phase ... — ir.ventyxbio.com (#3) `A`
- ❌ max_keep **0.6622** [on_target=0.86 evidence=0.77] UEG Week 2024 - CONFERENCE REPORTPEER-REVIEWED — conferences.medicom-publishers.com (#2) `A`
- ❌ max_keep **0.5568** [on_target=0.96 evidence=0.58] Tamuzimod - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#7) `A`
- ❌ low_evidence **0.2336** [on_target=0.73 evidence=0.32] UEG Week 2024 - High5 Immunology TV — high5immunology.tv (#9) `A`
- ❌ low_on_target **0.0001** [on_target=0.02 evidence=0.01] UEGW 2024 Archives — fmcgastro.org (#10)

## q002 (competitor objective)

**Objective:** C. difficile Infection Episode: Receipt of SOC Antibacterial Therapy (Fidaxomicin, Vancomycin, Metronidazole) With Planned Duration 10–25 Days at Time of IMP Administration competing agents in the same mechanistic class as AZD5148, including Monoclonal Antibody targeting Clostridioides Difficile Toxin B TcdB  
**Target sent:** drugs competing with AZD5148: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['AZD5148']

**q002-2** `AZD5148 TcdB antibody competitors licensing` → kept 5/10, jev 386 ms

- ✅ **0.7488** [on_target=0.96 evidence=0.78] 2026年6月17日詳解①：抗トキシンB抗体の世代交代 — note.com (#3) `A`
- ✅ **0.7395** [on_target=0.94 evidence=0.79] Clostridium Difficile Infections Pipeline Set - openPR.com — openpr.com (#4) `A`
- ✅ **0.7307** [on_target=0.97 evidence=0.75] Monoclonal Antibodies Targeting Bacterial Infections: A Broad ... — link.springer.com (#1) `A`
- ✅ **0.6643** [on_target=0.94 evidence=0.71] Epitope Conservation of AZD5148, a Broadly Neutralizing Anti-Toxin B Monoclonal Antibody, Among Dive — pmc.ncbi.nlm.nih.gov (#6) `A`
- ✅ **0.6298** [on_target=0.94 evidence=0.67] Monoclonal Antibodies Targeting Bacterial Infections: A Broad Review of the Field — pmc.ncbi.nlm.nih.gov (#2) `A`
- ❌ max_keep **0.6175** [on_target=0.95 evidence=0.65] The monoclonal antibody AZD5148 confers broad protection against ... — pmc.ncbi.nlm.nih.gov (#5) `A`
- ❌ max_keep **0.5733** [on_target=0.91 evidence=0.63] P-1055. Anti-Toxin B Neutralizing Monoclonal Antibody AZD5148 ... — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ max_keep **0.5369** [on_target=0.89 evidence=0.60] Epitope Conservation of AZD5148, a Broadly Neutralizing Anti-Toxin B Monoclonal Antibody, Among Dive — pubmed.ncbi.nlm.nih.gov (#8) `A`
- ❌ low_on_target **0.3684** [on_target=0.65 evidence=0.57] AZD5148 - Drug Targets, Indications, Patents — synapse.patsnap.com (#9) `A`
- ❌ low_on_target **0.0** [on_target=0.03 evidence=0.00] Search for patents - Research and innovation - European Union — research-and-innovation.ec.europa.eu (#7)

**q002-3** `AZD5148 RePreve comparator anti-toxin antibody` → kept 5/10, jev 358 ms

- ✅ **0.6904** [on_target=0.95 evidence=0.73] Immune aspects of Clostridioides difficile infection and vaccine ... — pmc.ncbi.nlm.nih.gov (#8) `A`
- ✅ **0.5983** [on_target=0.93 evidence=0.64] P-1055. Anti-Toxin B Neutralizing Monoclonal Antibody ... — academic.oup.com (#3) `A`
- ✅ **0.5756** [on_target=0.89 evidence=0.65] Monoclonal Antibodies Targeting Bacterial Infections: A Broad ... — link.springer.com (#4) `A`
- ✅ **0.5704** [on_target=0.92 evidence=0.62] The monoclonal antibody AZD5148 confers broad protection against ... — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.5673** [on_target=0.93 evidence=0.61] The monoclonal antibody AZD5148 confers broad protection ... - PLOS — journals.plos.org (#5) `A`
- ❌ max_keep **0.5188** [on_target=0.86 evidence=0.60] Epitope Conservation of AZD5148, a Broadly Neutralizing Anti-Toxin ... — academic.oup.com (#2) `A`
- ❌ max_keep **0.4826** [on_target=0.80 evidence=0.60] graphic — sec.gov (#10) `A`
- ❌ max_keep **0.4608** [on_target=0.79 evidence=0.58] AstraZeneca advances science of infectious disease ... — astrazeneca.com (#7) `A`
- ❌ max_keep **0.4455** [on_target=0.81 evidence=0.55] Clinical Trials Appendix - Q1 2026 Results Update — astrazeneca.com (#9) `A`
- ❌ low_evidence **0.352** [on_target=0.80 evidence=0.44] 683. Understanding Clostridioides difficile toxinB gene conservation through surveillance of public  — academic.oup.com (#6) `A`

**q002-1** `AZD5148 competing anti-TcdB monoclonal antibodies Phase 2 2026` → kept 5/10, jev 509 ms

- ✅ **0.6944** [on_target=0.96 evidence=0.72] 2026年6月17日詳解①：抗トキシンB抗体の世代交代 — note.com (#3) `A`
- ✅ **0.582** [on_target=0.90 evidence=0.65] Monoclonal Antibodies Targeting Bacterial Infections: A Broad Review of the Field — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.5795** [on_target=0.95 evidence=0.61] A single amino acid substitution determines susceptibility of ... — pmc.ncbi.nlm.nih.gov (#6) `A`
- ✅ **0.5539** [on_target=0.87 evidence=0.64] Monoclonal Antibodies Targeting Bacterial Infections: A Broad ... — link.springer.com (#4) `A`
- ✅ **0.534** [on_target=0.90 evidence=0.59] The monoclonal antibody AZD5148 confers broad protection against ... — pmc.ncbi.nlm.nih.gov (#9) `A`
- ❌ max_keep **0.4281** [on_target=0.76 evidence=0.56] [PDF] Clinical Trials Appendix - FY 2025 Results Update - AstraZeneca — astrazeneca.com (#10) `A`
- ❌ max_keep **0.4266** [on_target=0.79 evidence=0.54] Pipeline — astrazeneca.com (#7) `A`
- ❌ max_keep **0.4106** [on_target=0.80 evidence=0.51] Clinical Trials Appendix - Q1 2026 Results Update — astrazeneca.com (#1) `A`
- ❌ max_keep **0.3922** [on_target=0.74 evidence=0.53] Clostridium Difficile Infections Pipeline 2026: FDA Updates, — openpr.com (#8) `A`
- ❌ low_evidence **0.3775** [on_target=0.76 evidence=0.50] H1 and Q2 2026 Results Clinical Trials Appendix — astrazeneca.com (#2) `A`

**q002-5** `AZD5148 clinical pipeline TcdB antibody 2026` → kept 5/10, jev 583 ms

- ✅ **0.7264** [on_target=0.96 evidence=0.76] 2026年6月17日詳解①：抗トキシンB抗体の世代交代 — note.com (#6) `A`
- ✅ **0.5383** [on_target=0.85 evidence=0.63] Monoclonal Antibodies Targeting Bacterial Infections: A Broad ... — link.springer.com (#4) `A`
- ✅ **0.4839** [on_target=0.76 evidence=0.64] [PDF] Clinical Trials Appendix - FY 2025 Results Update - AstraZeneca — astrazeneca.com (#9) `A`
- ✅ **0.3996** [on_target=0.74 evidence=0.54] H1 and Q2 2026 Results Clinical Trials Appendix — astrazeneca.com (#2) `A`
- ❌ low_on_target **0.3898** [on_target=0.68 evidence=0.57] Ozmosi / AZD-5148 Drug Profile — pryzm.ozmosi.com (#7) `A`
- ✅ **0.3825** [on_target=0.75 evidence=0.51] 研究開発パイプライン — astrazeneca.co.jp (#5) `A`
- ❌ low_evidence **0.3721** [on_target=0.77 evidence=0.48] Clinical Trials Appendix - Q1 2026 Results Update — astrazeneca.com (#1) `A`
- ❌ low_on_target **0.3404** [on_target=0.69 evidence=0.49] Pipeline — astrazeneca.com (#3) `A`
- ❌ low_on_target **0.3124** [on_target=0.66 evidence=0.47] Epitope Conservation of AZD5148, a Broadly Neutralizing Anti-Toxin B Monoclonal Antibody, Among Dive — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ low_on_target **0.2901** [on_target=0.64 evidence=0.45] Prevention of Recurrent C. Difficile Infection Study With AZD5148 Monoclonal Antibody (NCT07285213) — clinicaltrials.gg (#8) `A`

**q002-4** `AZD5148 TcdB epitope binding mechanism` → kept 5/10, jev 401 ms

- ✅ **0.5731** [on_target=0.95 evidence=0.60] Immune aspects of Clostridioides difficile infection and vaccine ... — pmc.ncbi.nlm.nih.gov (#4) `A`
- ✅ **0.5674** [on_target=0.92 evidence=0.62] A single amino acid substitution determines susceptibility of ... — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.552** [on_target=0.92 evidence=0.60] The monoclonal antibody AZD5148 confers broad protection against ... — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.4787** [on_target=0.83 evidence=0.58] Monoclonal Antibodies Targeting Bacterial Infections: A Broad ... — link.springer.com (#3) `A`
- ❌ low_evidence **0.3645** [on_target=0.81 evidence=0.45] 683. Understanding Clostridioides difficile toxinB gene conservation through surveillance of public  — academic.oup.com (#6) `A`
- ✅ **0.3621** [on_target=0.71 evidence=0.51] Epitope Conservation of AZD5148, a Broadly Neutralizing Anti-Toxin B Monoclonal Antibody, Among Dive — pmc.ncbi.nlm.nih.gov (#1) `A`
- ❌ max_keep **0.35** [on_target=0.70 evidence=0.50] The monoclonal antibody AZD5148 confers broad protection ... - PLOS — journals.plos.org (#7) `A`
- ❌ low_on_target **0.2842** [on_target=0.58 evidence=0.49] Nanobodies against C. difficile TcdA and TcdB reveal unexpected neutralizing epitopes and provide a  — ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0704** [on_target=0.22 evidence=0.32] Receptor binding mechanisms of Clostridioides difficile toxin B and ... — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0651** [on_target=0.21 evidence=0.31] Receptor binding mechanisms of Clostridioides difficile toxin B and implications for therapeutics de — febs.onlinelibrary.wiley.com (#10)

## q003 (competitor objective)

**Objective:** Distal Ulcerative Colitis competing agents in the same mechanistic class as RpoB Small Molecule  
**Target sent:** drugs competing with RpoB: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['RpoB']

**q003-2** `Distal Ulcerative Colitis RpoB competitors Phase 2` → ABSTAIN, jev 432 ms

- ❌ low_on_target **0.3135** [on_target=0.57 evidence=0.55] Ulcerative colitis - PMC - NIH — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.2205** [on_target=0.45 evidence=0.49] Ulcerative Colitis Pipeline: 75+ Therapies & Key Companies — delveinsight.com (#6)
- ❌ low_on_target **0.1964** [on_target=0.43 evidence=0.46] Pharmacological Therapy in Inflammatory Bowel Diseases — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.164** [on_target=0.40 evidence=0.41] Reviewing treatments and outcomes in the evolving landscape of ulcerative colitis — tandfonline.com (#2)
- ❌ low_on_target **0.1554** [on_target=0.37 evidence=0.42] academic.oup.com · ecco-jcc · articleECCO Guidelines on Therapeutics in Ulcerative Colitis ... — academic.oup.com (#7)
- ❌ low_on_target **0.1496** [on_target=0.34 evidence=0.44] Ulcerative Colitis - Pipeline Insight, 2025 — researchandmarkets.com (#8)
- ❌ low_on_target **0.1452** [on_target=0.36 evidence=0.40] ECCO Guidelines on Therapeutics in Ulcerative Colitis ... — academic.oup.com (#1)
- ❌ low_on_target **0.1342** [on_target=0.35 evidence=0.38] What are the key players in the ulcerative colitis treatment ... — synapse.patsnap.com (#4)
- ❌ low_on_target **0.1185** [on_target=0.28 evidence=0.42] Ulcerative Colitis (UC) Pipeline Insight / Drugs, Therapies — delveinsight.com (#9)
- ❌ low_on_target **0.0623** [on_target=0.21 evidence=0.30] The IBD Therapeutic Pipeline is Primed to Produce — practicalgastro.com (#10)

**q003-1** `Distal Ulcerative Colitis RpoB inhibitors pipeline` → ABSTAIN, jev 384 ms

- ❌ low_on_target **0.1946** [on_target=0.42 evidence=0.46] Ulcerative Colitis - Gastroenterology - Merck Manuals — merckmanuals.com (#8)
- ❌ low_on_target **0.1761** [on_target=0.38 evidence=0.46] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.1654** [on_target=0.41 evidence=0.40] Emerging Treatment Options in Mild to Moderate Ulcerative Colitis — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.1583** [on_target=0.38 evidence=0.42] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#3)
- ❌ low_on_target **0.1563** [on_target=0.35 evidence=0.45] The IBD Therapeutic Pipeline Is Primed to Produce — practicalgastro.com (#2)
- ❌ low_on_target **0.121** [on_target=0.33 evidence=0.37] academic.oup.com · ecco-jcc · articleECCO Guidelines on Therapeutics in Ulcerative Colitis ... — academic.oup.com (#7)
- ❌ low_on_target **0.112** [on_target=0.32 evidence=0.35] Exploring the Pipeline of Novel Therapies for Inflammatory Bowel ... — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.047** [on_target=0.15 evidence=0.31] Novel Drug Developments for IBD - Highlights from ECCO 2025 — charite-research.org (#1)
- ❌ low_on_target **0.0244** [on_target=0.17 evidence=0.14] Pipeline — merck.com (#10)
- ❌ low_on_target **0.0036** [on_target=0.12 evidence=0.03] Exploring the Pipeline of Novel Therapies for Inflammatory ... — mdpi.com (#9)

**q003-3** `Distal Ulcerative Colitis RpoB mechanism clinical trial` → ABSTAIN, jev 384 ms

- ❌ low_on_target **0.1965** [on_target=0.45 evidence=0.44] Third European Evidence-based Consensus on Diagnosis and ... — academic.oup.com (#7)
- ❌ low_on_target **0.1685** [on_target=0.38 evidence=0.44] Recent advances in the management of distal ulcerative colitis — wjgnet.com (#9)
- ❌ low_on_target **0.1179** [on_target=0.34 evidence=0.35] Colitis clinical trials — clinicaltrials.gg (#2)
- ❌ low_on_target **0.1179** [on_target=0.29 evidence=0.41] Randomised clinical trial: the effectiveness of __Lactobacillus reuteri__ ATCC 55730 rectal enema in — onlinelibrary.wiley.com (#6)
- ❌ low_on_target **0.109** [on_target=0.30 evidence=0.36] Medical Treatment of Ulcerative Colitis - PMC - NIH — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0652** [on_target=0.19 evidence=0.34] Clinical outcomes of best practices for the treatment of distal ... - OUCI — ouci.dntb.gov.ua (#4)
- ❌ low_on_target **0.042** [on_target=0.14 evidence=0.30] A comprehensive review of usefulness of sodium butyrate ... — termedia.pl (#10)
- ❌ low_on_target **0.0234** [on_target=0.13 evidence=0.18] Ulcerative Colitis - 1,154 clinical trials — atlasbyauro.com (#1)
- ❌ low_on_target **0.01** [on_target=0.07 evidence=0.14] Gut microbiome‐targeted therapies as adjuvant treatments ... — onlinelibrary.wiley.com (#3)
- ❌ low_on_target **0.002** [on_target=0.15 evidence=0.01] NCT03596645 / A Study to Assess the Efficacy and Safety ... — clinicaltrials.gov (#5)

## q004 (competitor objective)

**Objective:** competing agents in the same mechanistic class for this indication MT501, Mirador Therapeutics, Crohn's Disease, Moderately to Severely Active by CDAI and SES-CD  
**Target sent:** drugs competing with MT501: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['MT501']

**q004-1** `MT501 mechanism of action mechanistic class` → ABSTAIN, jev 390 ms

- ❌ low_on_target **0.1566** [on_target=0.54 evidence=0.29] MT-501 - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#1) `A`
- ❌ low_on_target **0.0574** [on_target=0.41 evidence=0.14] Ozmosi / MT-501 Drug Profile — pryzm.ozmosi.com (#2) `A`
- ❌ low_on_target **0.0443** [on_target=0.35 evidence=0.13] 큐라클·맵틱스, MT-501 국가과제 선정 — newspim.com (#10) `A`
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] Shimano disc brake MT501/MT520 / buy online - Fitstore24.com — fitstore24.com (#3) `A`
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] SHIMANO Hamulec hydrauliczny MT501 BL-MT501/BR-MT500 tylny ... — veloportal.pl (#4) `A`
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] Maneta de freno de disco hidráulico MTB Shimano MT501 — cycletyres.es (#5) `A`
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] FREIO HIDRAULICO BL-MT501/BR-MT500 - rodociclo.com.br — rodociclo.com.br (#6) `A`
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] Tested: Shimano BL-MT501/BR-MT520 - BikeMag — bikemag.com (#7) `A`
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] Shimano MT501 + MT520 — mantel.com (#8) `A`
- ❌ low_on_target **0.0** [on_target=0.02 evidence=0.00] Investigating the Anticancer Promise of Synthesized Methylated N-Substituted-4-Hydroxy-2-Quinolone-3 — pubmed.ncbi.nlm.nih.gov (#9)

**q004-3** `MT501 inflammatory bowel disease competitors same mechanism` → kept 5/10, jev 367 ms

- ✅ **0.6319** [on_target=0.89 evidence=0.71] A Gastroenterologist's guide to drug interactions of small molecules for inflammatory bowel disease — onlinelibrary.wiley.com (#9)
- ✅ **0.5532** [on_target=0.86 evidence=0.64] Inflammatory Bowel Competitive Landscape Analysis 2026 / Eureka — eureka.patsnap.com (#3)
- ✅ **0.527** [on_target=0.85 evidence=0.62] academic.oup.com · ecco-jcc · articleInflammatory bowel disease therapies and demyelinating ... — academic.oup.com (#8)
- ✅ **0.4986** [on_target=0.80 evidence=0.62] Competitor Landscape — marketintelo.com (#6)
- ✅ **0.4592** [on_target=0.84 evidence=0.55] Inflammatory bowel disease treatment: Mechanisms ... — spandidos-publications.com (#1)
- ❌ low_on_target **0.437** [on_target=0.69 evidence=0.63] www.frontiersin.org › journals › pharmacologyFrontiers / Biologic and small-molecule therapies for . — frontiersin.org (#5)
- ❌ max_keep **0.4134** [on_target=0.80 evidence=0.52] The Expanding Therapeutic Armamentarium for Inflammatory Bowel Disease: How to Choose the Right Drug — academic.oup.com (#10)
- ❌ max_keep **0.35** [on_target=0.70 evidence=0.50] Landscape of new drugs and targets in inflammatory bowel ... — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_evidence **0.2817** [on_target=0.71 evidence=0.40] Pharmacological Therapy in Inflammatory Bowel Diseases — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.2686** [on_target=0.62 evidence=0.43] Understanding the therapeutic toolkit for inflammatory bowel disease — s29.q4cdn.com (#4)

**q004-2** `MT501 Crohn's disease target pathway` → kept 2/10, jev 344 ms

- ✅ **0.48** [on_target=0.80 evidence=0.60] Advancing therapeutic frontiers: a pipeline of novel drugs for luminal and perianal Crohn's disease  — journals.sagepub.com (#3)
- ✅ **0.3898** [on_target=0.74 evidence=0.53] Crohn's Disease Enteritis: Pathophysiological Mechanisms and ... — onlinelibrary.wiley.com (#8)
- ❌ low_on_target **0.1754** [on_target=0.56 evidence=0.31] MT-501 - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#1) `A`
- ❌ low_on_target **0.1599** [on_target=0.44 evidence=0.36] Advancements in Targeted Therapies for the Management of ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.1165** [on_target=0.38 evidence=0.31] MT-501 for Inflammatory Bowel Disease (ASCEND-IBD Trial) — withpower.com (#2) `A`
- ❌ low_on_target **0.113** [on_target=0.53 evidence=0.21] A Phase 2 Study to Evaluate Therapies for Inflammatory Bowel Disease — bridgemd.health (#7) `A`
- ❌ low_on_target **0.1008** [on_target=0.63 evidence=0.16] MT-501 - AssetMemo — assetmemo.bio (#4) `A`
- ❌ low_on_target **0.0935** [on_target=0.51 evidence=0.18] Phase 2 Study of MT-501 and MT-201 for Active Crohn's Disease or ... — aidyhq.com (#5) `A`
- ❌ low_on_target **0.0292** [on_target=0.35 evidence=0.08] MT-501 for Safety in Healthy Subjects · Info for Participants — withpower.com (#6) `A`
- ❌ low_on_target **0.021** [on_target=0.07 evidence=0.30] Treat to target in Crohn's disease: A practical guide for clinicians — wjgnet.com (#9)

## q005

**Objective:** SOR102 safety findings and adverse events in Crohn's Disease Ulcerative Colitis  
**Target sent:** SOR102 / SOR102-101 · anchors ['SOR102', 'SOR102-101']

**q005-4** `SOR102 Grade 3 adverse events 810 mg` → kept 5/10, jev 360 ms

- ✅ **0.9571** [on_target=0.97 evidence=0.99] Phase 1b study of SOR102, a novel, orally delivered ... — sorrisopharma.com (#4) `A`
- ✅ **0.9538** [on_target=0.97 evidence=0.98] OP31 Phase 1b study of SOR102, a novel, orally delivered ... — academic.oup.com (#5) `A`
- ✅ **0.9474** [on_target=0.97 evidence=0.98] PHASE 1B STUDY OF SOR102, A NOVEL, ORALLY ... — eposters.ddw.org (#3) `A`
- ✅ **0.9441** [on_target=0.97 evidence=0.97] Safety and pharmacokinetics of SOR102, an oral bispecific ... — pure.amsterdamumc.nl (#1) `A`
- ✅ **0.9376** [on_target=0.96 evidence=0.98] Safely targeting combination TNF and IL-23 using a gut-restricted ... — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ max_keep **0.9184** [on_target=0.96 evidence=0.96] SOR-102 - Drug Targets, Indications, Patents — synapse.patsnap.com (#2) `A`
- ❌ max_keep **0.8827** [on_target=0.97 evidence=0.91] SOR102 / Sorriso Pharma - Gastroenterology — delta.larvol.com (#6) `A`
- ❌ max_keep **0.8768** [on_target=0.96 evidence=0.91] Journal Scan_Jan 2026 — ibdenc.org (#7) `A`
- ❌ low_on_target **0.0103** [on_target=0.10 evidence=0.10] Pooled safety analysis and management of sotorasib-related ... — academic.oup.com (#8)
- ❌ low_on_target **0.0057** [on_target=0.05 evidence=0.11] Sotorasib in KRAS p.G12C–Mutated Advanced Pancreatic Cancer / NEJM — nejm.org (#9)

**q005-1** `SOR102 Crohn's disease safety adverse events` → kept 5/10, jev 423 ms

- ✅ **0.9506** [on_target=0.98 evidence=0.97] SOR-102 - Drug Targets, Indications, Patents — synapse.patsnap.com (#6) `A`
- ✅ **0.9506** [on_target=0.97 evidence=0.98] Sorriso Pharmaceuticals, Inc. - Drug pipelines, Patents ... — synapse.patsnap.com (#7) `A`
- ✅ **0.9474** [on_target=0.98 evidence=0.97] PHASE 1B STUDY OF SOR102, A NOVEL, ORALLY ... — eposters.ddw.org (#3) `A`
- ✅ **0.9312** [on_target=0.96 evidence=0.97] Safely targeting combination TNF and IL-23 using a gut-restricted ... — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.928** [on_target=0.97 evidence=0.96] EXPLORATORY EFFICACY RESULTS ... — sorrisopharma.com (#2) `A`
- ❌ max_keep **0.928** [on_target=0.97 evidence=0.96] Oral Administration of SOR102 Delivers Anti-TNF/IL-23 ... — sorrisopharma.com (#4) `A`
- ❌ max_keep **0.8665** [on_target=0.97 evidence=0.89] SOR102 / Sorriso Pharma - Gastroenterology — delta.larvol.com (#10) `A`
- ❌ max_keep **0.8407** [on_target=0.97 evidence=0.87] Journal Scan_Jan 2026 — ibdenc.org (#5) `A`
- ❌ max_keep **0.7426** [on_target=0.94 evidence=0.79] Colite ulcerosa: nuova frontiera terapeutica con SOR102 secondo ... — hsr.it (#8) `A`
- ❌ max_keep **0.7099** [on_target=0.93 evidence=0.76] [PDF] Anti-tumor necrosis factor-like ligand 1A and bispecific antibod - Apollo — api.repository.cam.ac.uk (#9) `A`

**q005-3** `SOR102 ulcerative colitis individual adverse events infections deaths` → kept 5/10, jev 455 ms

- ✅ **0.9702** [on_target=0.98 evidence=0.99] PowerPoint-Präsentation — sorrisopharma.com (#7) `A`
- ✅ **0.9603** [on_target=0.97 evidence=0.99] PowerPoint Presentation — sorrisopharma.com (#4) `A`
- ✅ **0.9344** [on_target=0.97 evidence=0.96] Safety and pharmacokinetics of SOR102, an oral bispecific ... — pubmed.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.9312** [on_target=0.97 evidence=0.96] Oral Administration of SOR102 Delivers Anti-TNF/IL-23 ... — sorrisopharma.com (#5) `A`
- ✅ **0.928** [on_target=0.96 evidence=0.97] Safely targeting combination TNF and IL-23 using a gut-restricted ... — pmc.ncbi.nlm.nih.gov (#2) `A`
- ❌ max_keep **0.9088** [on_target=0.96 evidence=0.95] gutflix.eu › search › dIMPROVEMENT IN INFLAMMATORY BIOMARKER LEVELS THROUGH WEEK 12 ... — gutflix.eu (#8) `A`
- ❌ max_keep **0.8994** [on_target=0.95 evidence=0.95] Sorriso Pharmaceuticals, Inc. - Drug pipelines, Patents ... — synapse.patsnap.com (#3) `A`
- ❌ max_keep **0.8804** [on_target=0.95 evidence=0.93] Interleukin-23 Inhibitors in Inflammatory Bowel Disease - PMC — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ max_keep **0.8722** [on_target=0.98 evidence=0.89] SOR102 / Sorriso Pharma - Gastroenterology — delta.larvol.com (#6) `A`
- ❌ max_keep **0.8201** [on_target=0.95 evidence=0.86] Journal Scan_Jan 2026 — ibdenc.org (#9) `A`

**q005-2** `SOR102-101 registry identifier safety` → kept 5/10, jev 340 ms

- ✅ **0.9636** [on_target=0.98 evidence=0.98] PowerPoint Presentation — sorrisopharma.com (#6) `A`
- ✅ **0.9636** [on_target=0.98 evidence=0.98] PHASE 1B STUDY OF SOR102, A NOVEL, ORALLY ... — eposters.ddw.org (#9) `A`
- ✅ **0.9377** [on_target=0.97 evidence=0.97] Oral Administration of SOR102 Delivers Anti-TNF/IL-23 ... — sorrisopharma.com (#7) `A`
- ✅ **0.9021** [on_target=0.97 evidence=0.93] PowerPoint-Präsentation — sorrisopharma.com (#1) `A`
- ✅ **0.88** [on_target=0.96 evidence=0.92] SOR102 / Sorriso Pharma - Gastroenterology — delta.larvol.com (#8) `A`
- ❌ max_keep **0.8762** [on_target=0.97 evidence=0.90] Sorriso Pharmaceuticals, Inc. - Drug pipelines, Patents ... — synapse.patsnap.com (#2) `A`
- ❌ max_keep **0.873** [on_target=0.97 evidence=0.90] Journal Scan_Jan 2026 — ibdenc.org (#10) `A`
- ❌ max_keep **0.8592** [on_target=0.98 evidence=0.88] SOR-102 - Drug Targets, Indications, Patents — synapse.patsnap.com (#5) `A`
- ❌ max_keep **0.8536** [on_target=0.97 evidence=0.88] Phase 1b study of SOR102, a novel, orally delivered ... — sorrisopharma.com (#4) `A`
- ❌ max_keep **0.7938** [on_target=0.98 evidence=0.81] A Clinical Trial to Assess the Safety of SOR102 in Healthy Participants and Patients With Ulcerative — ichgcp.net (#3) `A`

**q005-5** `SOR102 900 mg 42-day safety results` → kept 5/10, jev 388 ms

- ✅ **0.9506** [on_target=0.97 evidence=0.98] Sorriso Pharmaceuticals, Inc. - Drug pipelines, Patents ... — synapse.patsnap.com (#8) `A`
- ✅ **0.918** [on_target=0.98 evidence=0.94] Safety and pharmacokinetics of SOR102, an oral bispecific ... — pubmed.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.915** [on_target=0.97 evidence=0.94] Oral Administration of SOR102 Delivers Anti-TNF/IL-23 ... — sorrisopharma.com (#6) `A`
- ✅ **0.8924** [on_target=0.97 evidence=0.92] Safety and pharmacokinetics of SOR102, an oral bispecific ... — pure.amsterdamumc.nl (#3) `A`
- ✅ **0.8852** [on_target=0.98 evidence=0.90] SOR-102 - Drug Targets, Indications, Patents — synapse.patsnap.com (#1) `A`
- ❌ max_keep **0.8771** [on_target=0.95 evidence=0.92] SOR102 / Sorriso Pharma - Gastroenterology — delta.larvol.com (#5) `A`
- ❌ max_keep **0.8374** [on_target=0.97 evidence=0.86] Phase 1b study of SOR102, a novel, orally delivered ... — sorrisopharma.com (#7) `A`
- ❌ max_keep **0.7456** [on_target=0.96 evidence=0.78] Genomeditech(Shanghai) Co.LTD — en.genomeditech.com (#4) `A`
- ❌ max_keep **0.7332** [on_target=0.94 evidence=0.78] Colite ulcerosa: nuova frontiera terapeutica con SOR102 secondo ... — hsr.it (#9) `A`
- ❌ max_keep **0.6144** [on_target=0.95 evidence=0.65] Safety and pharmacokinetics of SOR102, an oral bispecific inhibitor ... — ouci.dntb.gov.ua (#10) `A`

## q006 (competitor objective)

**Objective:** Moderately to Severely Active Crohn's Disease Moderately to Severely Active Crohn’s Disease Refractory to Systemic Therapies Moderately to Severely Active Ulcerative Colitis Refractory to Systemic Therapies Moderately to Severely Active Ulcerative Colitis with inadequate response, loss of response, or intolerance to ≥1 biologic or novel oral with biologic-like activity competing agents in the same mechanistic class as JNJ-4804 Co Antibody Therapy, including Antibody Cocktail Monoclonal Antibody and IL-23 IL23A TNF-α Tumor Necrosis Factor Alpha therapies  
**Target sent:** drugs competing with JNJ-4804: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['JNJ-4804']

**q006-4** `JNJ-4804 competing IL-23 TNF-α antibody Crohn's disease ulcerative colitis` → kept 5/5, jev 332 ms

- ✅ **0.8265** [on_target=0.95 evidence=0.87] JNJ-4804 demonstrated highest rates of clinical ... — jnj.com (#1) `A`
- ✅ **0.7916** [on_target=0.95 evidence=0.83] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#5)
- ✅ **0.7175** [on_target=0.94 evidence=0.76] Study highlights breakthrough in overcoming diminishing returns of sequential IBD therapies — news-medical.net (#3) `A`
- ✅ **0.5888** [on_target=0.96 evidence=0.61] Inflammatory Bowel Disease Market to Experience Strong Uptake ... — prnewswire.co.uk (#4) `A`
- ✅ **0.4947** [on_target=0.82 evidence=0.60] J&J pushes dual-antibody IBD therapy into Phase 3 ... — biospace.com (#2) `A`

**q006-2** `JNJ-4804 IL-23 TNF-α dual antibody competing agents IBD` → kept 5/9, jev 367 ms

- ✅ **0.8455** [on_target=0.95 evidence=0.89] JNJ-4804 demonstrated highest rates of clinical ... — jnj.com (#1) `A`
- ✅ **0.6975** [on_target=0.93 evidence=0.75] Study highlights breakthrough in overcoming diminishing returns of sequential IBD therapies — news-medical.net (#8) `A`
- ✅ **0.687** [on_target=0.90 evidence=0.76] JNJ-4804 Doubles Remission in Refractory Crohn's - allsci.com — allsci.com (#4) `A`
- ✅ **0.5921** [on_target=0.95 evidence=0.62] Targeted Therapies in Inflammatory Bowel Disease: Mechanisms, Comparative Evidence, and Clinical Tra — pmc.ncbi.nlm.nih.gov (#7)
- ✅ **0.5488** [on_target=0.84 evidence=0.65] 投資人請注意，自體免疫超大藥賽道 — dcard.tw (#5) `A`
- ❌ max_keep **0.494** [on_target=0.76 evidence=0.65] J&J pushes dual-antibody IBD therapy into Phase 3 ... — biospace.com (#6) `A`
- ❌ max_keep **0.4402** [on_target=0.71 evidence=0.62] Johnson & Johnson's quest to develop effective IBD treatments — jnj.com (#9)
- ❌ max_keep **0.44** [on_target=0.75 evidence=0.59] EFFICACY AND SAFETY OF THE FIRST CO-ANTIBODY THERAPY, JNJ ... — jnjmedicalconnect.com (#2) `A`
- ❌ low_on_target **0.3307** [on_target=0.64 evidence=0.52] www.jnjmedicalconnect.com · media · attestationEFFICACY AND SAFETY OF THE FIRST CO-ANTIBODY THERAPY, — jnjmedicalconnect.com (#3) `A`

**q006-1** `JNJ-4804 guselkumab golimumab IL-23 TNF-α competitors IBD` → kept 5/10, jev 367 ms

- ✅ **0.846** [on_target=0.94 evidence=0.90] Interleukin-23p19 Inhibitors in Inflammatory Bowel Disease — pmc.ncbi.nlm.nih.gov (#7)
- ✅ **0.8424** [on_target=0.95 evidence=0.89] JNJ-4804 demonstrated highest rates of clinical ... — jnj.com (#1) `A`
- ✅ **0.8342** [on_target=0.97 evidence=0.86] IBD治疗领域存在未满足的需求，关注新靶点 — pdf.dfcfw.com (#5) `A`
- ✅ **0.7695** [on_target=0.95 evidence=0.81] ‘Strikingly better’: Co-antibody combination tops golimumab ... — healio.com (#2) `A`
- ✅ **0.7569** [on_target=0.95 evidence=0.80] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#10)
- ❌ max_keep **0.7298** [on_target=0.92 evidence=0.79] JNJ-4804 Doubles Remission in Refractory Crohn's — allsci.com (#8) `A`
- ❌ max_keep **0.7156** [on_target=0.95 evidence=0.75] Landscape of new drugs and targets in inflammatory bowel disease — onlinelibrary.wiley.com (#4)
- ❌ max_keep **0.6432** [on_target=0.96 evidence=0.67] Advancements in dual biologic therapy for inflammatory bowel diseases: efficacy, safety, and future  — journals.sagepub.com (#6)
- ❌ max_keep **0.6355** [on_target=0.93 evidence=0.68] Guselkumab/Golimumab - Drug Targets, Indications, Patents — synapse.patsnap.com (#9) `A`
- ❌ low_on_target **0.4232** [on_target=0.69 evidence=0.61] EFFICACY AND SAFETY OF THE FIRST CO-ANTIBODY THERAPY, JNJ ... — jnjmedicalconnect.com (#3) `A`

**q006-3** `JNJ-4804 same mechanistic class IBD pipeline` → kept 5/10, jev 381 ms

- ✅ **0.7269** [on_target=0.94 evidence=0.77] Combination therapy could improve outcomes in the most ... — medicalxpress.com (#9) `A`
- ✅ **0.6886** [on_target=0.91 evidence=0.76] Guselkumab/Golimumab - Drug Targets, Indications, Patents — synapse.patsnap.com (#10) `A`
- ✅ **0.639** [on_target=0.90 evidence=0.71] News Details - JNJ Investor Relations — investor.jnj.com (#2) `A`
- ✅ **0.615** [on_target=0.90 evidence=0.68] golimumab/guselkumab (JNJ-4804) / J&J — delta.larvol.com (#4) `A`
- ✅ **0.5866** [on_target=0.83 evidence=0.71] Johnson & Johnson investigational co-antibody therapy JNJ-4804 ... — investor.jnj.com (#1) `A`
- ❌ max_keep **0.4661** [on_target=0.76 evidence=0.61] J&J pushes dual-antibody IBD therapy into Phase 3 ... — biospace.com (#7) `A`
- ❌ low_on_target **0.3933** [on_target=0.69 evidence=0.57] EFFICACY AND SAFETY OF THE FIRST CO-ANTIBODY THERAPY, JNJ ... — jnjmedicalconnect.com (#6) `A`
- ❌ low_on_target **0.2312** [on_target=0.51 evidence=0.45] www.jnjmedicalconnect.com · media · attestationEFFICACY AND SAFETY OF THE FIRST CO-ANTIBODY THERAPY, — jnjmedicalconnect.com (#3) `A`
- ❌ low_on_target **0.2271** [on_target=0.52 evidence=0.44] Johnson & Johnson Advances Dual-Pathway Strategy in Refractory IBD / BioPharm International — biopharminternational.com (#5) `A`
- ❌ low_on_target **0.0506** [on_target=0.41 evidence=0.12] Selected Innovative Medicines in Development as of April 14 ... — s203.q4cdn.com (#8) `A`

## q007 (competitor objective)

**Objective:** Ulcerative Colitis competing agents in the same mechanistic class as FN1 IL-10RB IL10RA Interleukin-10 Antibody-Cytokine Conjugate Fusion Protein Biologic  
**Target sent:** drugs competing with Dekavil: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['Dekavil']

**q007-1** `Dekavil ulcerative colitis IL-10 fusion competitors` → kept 3/10, jev 453 ms

- ✅ **0.5934** [on_target=0.89 evidence=0.67] Targeting IL-10 Family Cytokines for the Treatment of Human ... — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.5599** [on_target=0.76 evidence=0.74] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#1)
- ✅ **0.5117** [on_target=0.76 evidence=0.67] Emerging Therapies for Ulcerative Colitis: Updates from Recent ... — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.3179** [on_target=0.64 evidence=0.50] Interleukin-10 muteins and fusion proteins thereof — patents.google.com (#9)
- ❌ low_on_target **0.3173** [on_target=0.57 evidence=0.56] Why interleukin-10 supplementation does not work in Crohn's ... — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.3007** [on_target=0.55 evidence=0.55] AUSGABE 01 / 2025 — abf-apotheke.de (#3)
- ❌ low_on_target **0.2939** [on_target=0.58 evidence=0.51] Advances in the Treatment of Ulcerative Colitis—From Conventional ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.2123** [on_target=0.49 evidence=0.43] Top 7 Breakthrough Drugs for Ulcerative Colitis Treatment — delveinsight.com (#8)
- ❌ low_on_target **0.1786** [on_target=0.47 evidence=0.38] Key Interleukins in Inflammatory Bowel Disease—A Review of Recent Studies — mdpi.com (#6)
- ❌ low_on_target **0.0896** [on_target=0.28 evidence=0.32] Exploring the Pipeline of Novel Therapies for Inflammatory Bowel ... — pmc.ncbi.nlm.nih.gov (#5)

**q007-3** `Dekavil PF-06687234 sponsor ownership` → kept 2/10, jev 345 ms

- ✅ **0.4533** [on_target=0.85 evidence=0.53] Philogen News — sigma.larvol.com (#9) `A`
- ✅ **0.3953** [on_target=0.71 evidence=0.56] PF-06687234 ( DrugBank: - ) — ddrare.nibn.go.jp (#8) `A`
- ❌ low_evidence **0.3494** [on_target=0.80 evidence=0.44] Dekavil (F8-IL10) / Pfizer, Philogen — delta.larvol.com (#4) `A`
- ❌ low_evidence **0.2407** [on_target=0.76 evidence=0.32] Preclinical characterization of DEKAVIL (F8-IL10), a novel clinical ... — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ low_on_target **0.2222** [on_target=0.68 evidence=0.33] a phase 2a, randomized, double-blind, placebo-controlled — cdn.clinicaltrials.gov (#6) `A`
- ❌ low_evidence **0.208** [on_target=0.80 evidence=0.26] Clinical trials — clinicaltrialsregister.eu (#1) `A`
- ❌ low_evidence **0.1571** [on_target=0.76 evidence=0.21] Dekavil - Drug Targets, Indications, Patents - Synapse — synapse.patsnap.com (#5) `A`
- ❌ low_on_target **0.1337** [on_target=0.34 evidence=0.39] PF-06687234 / MedPath — trial.medpath.com (#3)
- ❌ low_on_target **0.0309** [on_target=0.58 evidence=0.05] Ozmosi / Dekavil Drug Profile — pryzm.ozmosi.com (#7) `A`
- ❌ low_on_target **0.0288** [on_target=0.18 evidence=0.16] EudraCT Number 2017-002108-28 - Clinical trial results — clinicaltrialsregister.eu (#2)

**q007-2** `Dekavil ulcerative colitis antibody-cytokine fusion pipeline` → kept 5/10, jev 323 ms

- ✅ **0.5951** [on_target=0.79 evidence=0.75] Efficacy and safety of the interleukin-10–fragment F8 fusion ... — pmc.ncbi.nlm.nih.gov (#8) `A`
- ✅ **0.5202** [on_target=0.83 evidence=0.63] Antibody-cytokine fusion proteins: a novel class of ... - PMC - NIH — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.4746** [on_target=0.80 evidence=0.59] Inflammatory Bowel Disease: Updates on Molecular ... — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.4675** [on_target=0.83 evidence=0.56] Dekavil (F8-IL10) / Pfizer, Philogen — delta.larvol.com (#7) `A`
- ✅ **0.4371** [on_target=0.79 evidence=0.55] Dekavil - Drug Targets, Indications, Patents - Synapse — synapse.patsnap.com (#1) `A`
- ❌ low_evidence **0.4107** [on_target=0.88 evidence=0.47] Treatment of a disease of the gastrointestinal tract with il-10 or an il-10 agonist — patents.google.com (#9) `A`
- ❌ low_on_target **0.3171** [on_target=0.67 evidence=0.47] Research advances of vasoactive intestinal peptide in the ... - PMC — pmc.ncbi.nlm.nih.gov (#4) `A`
- ❌ low_on_target **0.2961** [on_target=0.63 evidence=0.47] Preclinical characterization of DEKAVIL (F8-IL10), a novel clinical ... — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ low_on_target **0.2872** [on_target=0.62 evidence=0.46] Research advances of vasoactive intestinal peptide in the ... — wjgnet.com (#6) `A`
- ❌ low_on_target **0.1326** [on_target=0.41 evidence=0.32] Immunology & Inflammation: Autoimmune Pipeline & Trials - Pfizer — pfizer.com (#3) `A`

**q007-4** `Dekavil ulcerative colitis current development status` → kept 2/10, jev 345 ms

- ✅ **0.456** [on_target=0.80 evidence=0.57] Dekavil (F8-IL10) / Pfizer, Philogen — delta.larvol.com (#3) `A`
- ✅ **0.43** [on_target=0.75 evidence=0.57] Dekavil - Drug Targets, Indications, Patents - Synapse — synapse.patsnap.com (#4) `A`
- ❌ low_on_target **0.23** [on_target=0.67 evidence=0.34] Dekavil - DDrare — ddrare.nibn.go.jp (#6) `A`
- ❌ low_on_target **0.2267** [on_target=0.38 evidence=0.60] Efficacy and safety of duvakitug in patients with ulcerative ... — pubmed.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.2176** [on_target=0.48 evidence=0.45] Ulcerative Colitis Clinical Trials — mayo.edu (#9)
- ❌ low_on_target **0.216** [on_target=0.40 evidence=0.54] Press Release: Sanofi and Teva's duvakitug phase 2b ... — sanofi.com (#2)
- ❌ low_on_target **0.1749** [on_target=0.33 evidence=0.53] Press Release: ECCO 2025: new duvakitug data reinforce ... — sanofi.com (#8)
- ❌ low_on_target **0.146** [on_target=0.30 evidence=0.49] duvakitug (SAR447189) / Teva, Sanofi — delta.larvol.com (#1)
- ❌ low_on_target **0.1275** [on_target=0.25 evidence=0.51] Ulcerative Colitis Pipeline: 75+ Therapies & Key Companies — delveinsight.com (#5)
- ❌ low_on_target **0.099** [on_target=0.33 evidence=0.30] Clinical trials — clinicaltrialsregister.eu (#10)

## q008 (competitor objective)

**Objective:** Clostridioides Difficile Colitis competing agents in the same mechanistic class as LMN-201, including Antibody Fragment Enzyme Biological Biologic Cocktail and Clostridioides Difficile Toxin B TcdB therapies  
**Target sent:** drugs competing with LMN-201: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['LMN-201']

**q008-3** `LMN-201 BL5-6.2 clinical development` → kept 2/10, jev 372 ms

- ✅ **0.612** [on_target=0.90 evidence=0.68] Lumen Bioscience's LMN-201 Achieves 100% Initial C. difficile Clinical Cure in Preliminary Cohort of — prnewswire.com (#4) `A`
- ✅ **0.36** [on_target=0.72 evidence=0.50] Meds Pipeline Monitor 2026 — canada.ca (#2) `A`
- ❌ low_evidence **0.3192** [on_target=0.76 evidence=0.42] The latest on Lumen Biosience's experimental c. diff biologic — drugdiscoverytrends.com (#6) `A`
- ❌ low_on_target **0.2562** [on_target=0.63 evidence=0.41] Lumen Bioscience Announces Clinical Advancement of LMN-201 ... — lumen.bio (#9) `A`
- ❌ low_evidence **0.2427** [on_target=0.70 evidence=0.35] Lumen Bioscience Details 2022 Company and Facilities ... — prnewswire.com (#10) `A`
- ❌ low_evidence **0.238** [on_target=0.70 evidence=0.34] Investigational Oral Biologic Achieves 100% C difficile ... — lumen.bio (#1) `A`
- ❌ low_on_target **0.2016** [on_target=0.63 evidence=0.32] Lumen Bioscience pursues oral biologic to prevent recurrent C. diff — drugdiscoverytrends.com (#8) `A`
- ❌ low_on_target **0.186** [on_target=0.60 evidence=0.31] Lumen Bioscience, Inc. - Drug pipelines, Patents, Clinical ... — synapse.patsnap.com (#3) `A`
- ❌ low_on_target **0.1764** [on_target=0.54 evidence=0.33] LMN-201 - MedPath — trial.medpath.com (#7) `A`
- ❌ low_on_target **0.1224** [on_target=0.51 evidence=0.24] Lumen Bioscience News and Press Releases / PR Newswire — prnewswire.com (#5) `A`

**q008-2** `LMN-201 PA-41 development phase` → kept 2/10, jev 377 ms

- ✅ **0.747** [on_target=0.90 evidence=0.83] Clinical implementation of endolysins targeting gram-positive ... — pmc.ncbi.nlm.nih.gov (#4) `A`
- ✅ **0.375** [on_target=0.74 evidence=0.51] Meds Pipeline Monitor 2026 — canada.ca (#5) `A`
- ❌ low_evidence **0.34** [on_target=0.75 evidence=0.45] The latest on Lumen Biosience's experimental c. diff biologic — drugdiscoverytrends.com (#7) `A`
- ❌ low_on_target **0.2806** [on_target=0.69 evidence=0.41] LMN-201 - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#3) `A`
- ❌ low_on_target **0.2011** [on_target=0.58 evidence=0.35] LMN-201 Clinical Mixture of 3 — db.antibodysociety.org (#2) `A`
- ❌ low_on_target **0.1899** [on_target=0.64 evidence=0.30] Lumen Bioscience pursues oral biologic to prevent recurrent C. diff — drugdiscoverytrends.com (#9) `A`
- ❌ low_on_target **0.1863** [on_target=0.69 evidence=0.27] Investigational Oral Biologic Achieves 100% C difficile ... — lumen.bio (#6) `A`
- ❌ low_on_target **0.186** [on_target=0.62 evidence=0.30] LMN-201 / Lumen Bio - Larvol Delta — delta.larvol.com (#8) `A`
- ❌ low_on_target **0.173** [on_target=0.59 evidence=0.29] Lumen Bioscience, Inc. - Drug pipelines, Patents, Clinical ... — synapse.patsnap.com (#1) `A`
- ❌ low_on_target **0.1005** [on_target=0.52 evidence=0.19] LMN-201 / MedPath — trial.medpath.com (#10) `A`

**q008-1** `LMN-201 TcdB antitoxin competitors Phase 2 clinical` → kept 5/10, jev 343 ms

- ✅ **0.6705** [on_target=0.94 evidence=0.71] The Urgent Threat of Clostridioides difficile Infection - PMC - NIH — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.627** [on_target=0.95 evidence=0.66] Clostridium difficile Infections Pipeline Analysis - GlobeNewswire — globenewswire.com (#6) `A`
- ✅ **0.6036** [on_target=0.91 evidence=0.66] Clostridium Difficile Infections Pipeline 2026: FDA Updates, — openpr.com (#4) `A`
- ✅ **0.6032** [on_target=0.87 evidence=0.69] Using antibody synergy to engineer a high potency biologic cocktail against C. difficile — biorxiv.org (#10) `A`
- ✅ **0.582** [on_target=0.90 evidence=0.65] The Urgent Threat of Clostridioides difficile Infection: A Glimpse of the Drugs of the Future, with  — mdpi.com (#1) `A`
- ❌ max_keep **0.4902** [on_target=0.85 evidence=0.58] LMN-201 Preliminary Cohort in Repreve Trial — lumen.bio (#9) `A`
- ❌ max_keep **0.4289** [on_target=0.83 evidence=0.52] Clostridium Difficile Infections Pipeline 2025: Latest FDA ... — barchart.com (#3) `A`
- ❌ low_on_target **0.3931** [on_target=0.67 evidence=0.59] Table 1. — pmc.ncbi.nlm.nih.gov (#5) `A`
- ❌ low_evidence **0.3306** [on_target=0.74 evidence=0.45] Thematic Highlights of Antibacterial Development 2022-23: Part 6 — linkedin.com (#7) `A`
- ❌ low_evidence **0.3268** [on_target=0.76 evidence=0.43] Lumen Bioscience Releases Data on Potent, Orally ... — prnewswire.com (#8) `A`

**q008-4** `LMN-201 AZD5148 clinical trial regulatory status` → kept 1/10, jev 375 ms

- ✅ **0.6946** [on_target=0.91 evidence=0.76] Prevention of Recurrent C. Difficile Infection Study With AZD5148 Monoclonal Antibody — med.agiltrace.com (#2) `A`
- ❌ low_on_target **0.1625** [on_target=0.65 evidence=0.25] LMN-201 for Prevention of C. Difficile Infection Recurrence — clinicaltrials.gov (#1) `A`
- ❌ low_on_target **0.1624** [on_target=0.58 evidence=0.28] LMN-201 / Lumen Bio - Larvol Delta — delta.larvol.com (#10) `A`
- ❌ low_on_target **0.1575** [on_target=0.63 evidence=0.25] LMN-201 for Prevention of C. Difficile Infection Recurrence — med.agiltrace.com (#4) `A`
- ❌ low_on_target **0.148** [on_target=0.60 evidence=0.25] Clinical Trials Using Clostridioides difficile Toxin B-binding proteins ... — cancer.gov (#3) `A`
- ❌ low_on_target **0.1406** [on_target=0.62 evidence=0.23] LMN-201 for Prevention of C. Difficile ... / NCT05330182 ... — deltatrials.com (#8) `A`
- ❌ low_on_target **0.1377** [on_target=0.51 evidence=0.27] LMN-201 - MedPath — trial.medpath.com (#9) `A`
- ❌ low_on_target **0.1218** [on_target=0.63 evidence=0.19] C. Difficile Infection Clinical Trials — mayo.edu (#7) `A`
- ❌ low_on_target **0.0082** [on_target=0.13 evidence=0.06] Study Details / NCT06469151 / A Study to Evaluate the Safety, Tolerability and Pharmacokinetics of A — clinicaltrials.gov (#5)
- ❌ low_on_target **0.0057** [on_target=0.09 evidence=0.06] A Study to Evaluate the Safety, Tolerability and ... — astrazenecaclinicaltrials.com (#6)

**q008-5** `LMN-201 bezlotoxumab withdrawal current status` → kept 3/10, jev 411 ms

- ✅ **0.76** [on_target=0.95 evidence=0.80] LMN-201 Preliminary Cohort in Repreve Trial — lumen.bio (#1) `A`
- ✅ **0.6675** [on_target=0.89 evidence=0.75] Navigating recurrent Clostridioides difficile infection without ... — pmc.ncbi.nlm.nih.gov (#2)
- ✅ **0.6249** [on_target=0.91 evidence=0.69] Lumen Bioscience's Oral Biologic LMN-201 Achieves 100 ... — trial.medpath.com (#3) `A`
- ❌ low_evidence **0.2675** [on_target=0.71 evidence=0.38] Investigational Oral Biologic Achieves 100% C difficile ... — lumen.bio (#9) `A`
- ❌ low_on_target **0.2481** [on_target=0.61 evidence=0.41] LMN-201 Clinical Mixture of 3 — db.antibodysociety.org (#4) `A`
- ❌ low_on_target **0.2244** [on_target=0.66 evidence=0.34] Lumen Bioscience / Home — lumen.bio (#10) `A`
- ❌ low_on_target **0.1179** [on_target=0.58 evidence=0.20] Addressing Personalized Needs in Clostridioides Difficile Infection — med.agiltrace.com (#5) `A`
- ❌ low_on_target **0.0001** [on_target=0.03 evidence=0.00] Pfizer, Inc., et al.; Withdrawal of Approval of 26 New Drug Applications — federalregister.gov (#6)
- ❌ low_on_target **0.0001** [on_target=0.04 evidence=0.00] Pfizer, Inc., et al.; Withdrawal of Approval of 23 New Drug Applications — federalregister.gov (#7)
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] Drug news and alerts — humana.com (#8)

## q009 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as CHRM1 CHRM3 CHRM4 CHRM5 Small Molecule  
**Target sent:** drugs competing with Dicyclomine: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['Dicyclomine']

**q009-1** `Dicyclomine inflammatory bowel disease muscarinic competitors` → kept 5/10, jev 360 ms

- ✅ **0.6904** [on_target=0.95 evidence=0.73] [PDF] Phase II-(VI) Antispasmodic & antiulcer drugs (cyclopentolate ... — api.upums.ac.in (#10) `A`
- ✅ **0.6318** [on_target=0.92 evidence=0.69] An evidence-based review of treatment options for irritable bowel ... — managedhealthcareexecutive.com (#3) `A`
- ✅ **0.6231** [on_target=0.93 evidence=0.67] Pain management in patients with inflammatory bowel disease — pmc.ncbi.nlm.nih.gov (#6) `A`
- ✅ **0.6067** [on_target=0.91 evidence=0.67] Antispasmodics for Chronic Abdominal Pain: Analysis of North ... — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.5963** [on_target=0.89 evidence=0.67] Pharmacologic Agents for Chronic Diarrhea - PMC - NIH — pmc.ncbi.nlm.nih.gov (#2) `A`
- ❌ max_keep **0.5476** [on_target=0.86 evidence=0.64] Current Recommendations and Evidence - PMC — pmc.ncbi.nlm.nih.gov (#5) `A`
- ❌ max_keep **0.4727** [on_target=0.87 evidence=0.54] Drugs Used in Gastrointestinal Disorders - Katzung & Trevor's ... — doctorlib.org (#4) `A`
- ❌ low_evidence **0.3748** [on_target=0.77 evidence=0.49] Subclassification of atrial and intestinal muscarinic receptors of the rat--direct binding studies w — pmc.ncbi.nlm.nih.gov (#9) `A`
- ❌ low_evidence **0.3485** [on_target=0.85 evidence=0.41] Pharmacology — go.drugbank.com (#8) `A`
- ❌ low_evidence **0.3174** [on_target=0.80 evidence=0.40] [PDF] Summary Product Characteristics (SPC) — products.pharmacyboardkenya.org (#7) `A`

**q009-3** `Dicyclomine inflammatory bowel disease clinical development` → kept 4/10, jev 510 ms

- ✅ **0.6541** [on_target=0.93 evidence=0.70] Managing Pain in Inflammatory Bowel Disease - PMC - NIH — pmc.ncbi.nlm.nih.gov (#7) `A`
- ✅ **0.6491** [on_target=0.95 evidence=0.68] Ther Adv Gastroenterol — escholarship.org (#10) `A`
- ✅ **0.6448** [on_target=0.93 evidence=0.69] efficacy and safety of hyoscyamine, dicyclomine, and desipramine in ... — academic.oup.com (#1) `A`
- ✅ **0.6042** [on_target=0.92 evidence=0.66] Pain management in patients with inflammatory bowel disease — pmc.ncbi.nlm.nih.gov (#9) `A`
- ❌ low_evidence **0.4052** [on_target=0.85 evidence=0.48] Dicyclomine: Package Insert — drugs.com (#3) `A`
- ❌ low_evidence **0.391** [on_target=0.85 evidence=0.46] www.accessdata.fda.gov › drugsatfda_docs › labelBENTYL (dicyclomine HCl, USP) U.S. Package Insert — accessdata.fda.gov (#8) `A`
- ❌ low_evidence **0.3901** [on_target=0.88 evidence=0.44] https://nctr-crs.fda.gov/fdalabel/services/spl/ ... — nctr-crs.fda.gov (#4) `A`
- ❌ low_evidence **0.3066** [on_target=0.80 evidence=0.38] Pharmacology — go.drugbank.com (#6) `A`
- ❌ low_evidence **0.2746** [on_target=0.80 evidence=0.34] Dicyclomine 20mg — dailymed.nlm.nih.gov (#2) `A`
- ❌ low_on_target **0.2063** [on_target=0.52 evidence=0.40] The Impact of Antispasmodic Use on Abdominal Pain and ... — pmc.ncbi.nlm.nih.gov (#5) `A`

**q009-2** `Dicyclomine IBD CHRM pipeline` → kept 1/10, jev 409 ms

- ✅ **0.474** [on_target=0.90 evidence=0.53] DICYCLOMINE - Inxight Drugs — drugs.ncats.io (#5) `A`
- ❌ low_evidence **0.4123** [on_target=0.83 evidence=0.50] NCATS Inxight Drugs — DICYCLOMINE HYDROCHLORIDE — drugs.ncats.io (#10) `A`
- ❌ low_evidence **0.3813** [on_target=0.88 evidence=0.43] Pharmacology — go.drugbank.com (#9) `A`
- ❌ low_evidence **0.367** [on_target=0.86 evidence=0.43] dicyclomine hydrochloride tablet - DailyMed - NIH — dailymed.nlm.nih.gov (#2) `A`
- ❌ low_evidence **0.3596** [on_target=0.87 evidence=0.41] DICYCLOMINE HYDROCHLORIDE — dailymed.nlm.nih.gov (#1) `A`
- ❌ low_evidence **0.3382** [on_target=0.86 evidence=0.39] dicyclomine hydrochloride — glowm.com (#7) `A`
- ❌ low_evidence **0.2932** [on_target=0.83 evidence=0.35] highlights of prescribing information — dailymed.nlm.nih.gov (#3) `A`
- ❌ low_evidence **0.2918** [on_target=0.85 evidence=0.34] Dicyclomine / Medication Guide — zmg.us (#6) `A`
- ❌ low_evidence **0.2843** [on_target=0.82 evidence=0.35] Disclaimer:  The Rapid Response Service is an information service for those involved in planning and — ncbi.nlm.nih.gov (#8) `A`
- ❌ low_evidence **0.272** [on_target=0.85 evidence=0.32] highlights of prescribing information - DailyMed — dailymed.nlm.nih.gov (#4) `A`

## q010 (competitor objective)

**Objective:** competing agents in the same mechanistic class for this indication LY4395089, Eli Lilly & Company, Crohn''s Disease  
**Target sent:** drugs competing with LY4395089: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['LY4395089']

**q010-1** `LY4395089 mechanism target Crohn’s disease` → kept 5/10, jev 463 ms

- ✅ **0.5992** [on_target=0.89 evidence=0.67] Multiple Drugs for Ulcerative Colitis or Crohn's Disease — withpower.com (#5) `A`
- ✅ **0.585** [on_target=0.90 evidence=0.65] Ly4395089 ir mirikizumab gydymo tyrimas suaugusiems su vidutinio ir sunkios veiklos Krono liga — klinikiniai-tyrimai.lt (#2) `A`
- ✅ **0.5763** [on_target=0.91 evidence=0.63] A clinical research study for people with moderately to ... — trials.lilly.com (#7) `A`
- ✅ **0.4988** [on_target=0.86 evidence=0.58] Lilly Crohn's and Ulcerative Colitis Clinical Trials / IBD Research — trials.lilly.com (#8) `A`
- ✅ **0.4862** [on_target=0.78 evidence=0.62] LY4395089 + Mirikizumab for Crohn's Disease - WithPower — withpower.com (#6) `A`
- ❌ max_keep **0.4838** [on_target=0.82 evidence=0.59] Eficacitatea administrării combinate a ly4395089 și mirikizumab comparativ cu mirikizumab singur la  — studii.clinice.ro (#1) `A`
- ❌ max_keep **0.4268** [on_target=0.74 evidence=0.58] A Master Protocol (IIBD): A Study of Multiple Drugs in Adults With ... — ctv.veeva.com (#10) `A`
- ❌ low_evidence **0.4108** [on_target=0.85 evidence=0.48] Crohns' Disease Clinical Trial Drug Development Pipeline ... — barchart.com (#9) `A`
- ❌ low_evidence **0.3717** [on_target=0.82 evidence=0.45] Study Details / NCT07483099 / ClinicalTrials.gov - ClinicalTrials.gov — clinicaltrials.gov (#4) `A`
- ❌ low_on_target **0.112** [on_target=0.48 evidence=0.23] LY-4395089 - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#3) `A`

**q010-2** `LY4395089 competing agents Crohn’s disease same mechanism` → kept 5/10, jev 417 ms

- ✅ **0.8429** [on_target=0.94 evidence=0.90] LY4395089 - Crohn Disease / Phase 2 / Eli Lilly and ... — biopharmawatch.com (#1) `A`
- ✅ **0.804** [on_target=0.90 evidence=0.89] Ontamalimab (Ph 3) - Takeda Pharmaceutical Company Limited — biopharmawatch.com (#5) `A`
- ✅ **0.7207** [on_target=0.94 evidence=0.77] Crohn Disease Clinical Trials (171 Recruiting) / ClinicalTrialsFinder — clinicaltrialsfinder.org (#8) `A`
- ✅ **0.5278** [on_target=0.87 evidence=0.61] A clinical research study for people with moderately to ... — trials.lilly.com (#10) `A`
- ✅ **0.5043** [on_target=0.85 evidence=0.59] Find Lilly Clinical Trials — trials.lilly.com (#6) `A`
- ❌ max_keep **0.4671** [on_target=0.81 evidence=0.58] Study Details / NCT07483099 / ClinicalTrials.gov - ClinicalTrials.gov — clinicaltrials.gov (#3) `A`
- ❌ max_keep **0.415** [on_target=0.83 evidence=0.50] Crohns' Disease Clinical Trial Drug Development Pipeline ... — barchart.com (#4) `A`
- ❌ max_keep **0.3827** [on_target=0.70 evidence=0.55] Advancing therapeutic frontiers: a pipeline of novel drugs for luminal and perianal Crohn's disease  — journals.sagepub.com (#7)
- ❌ low_evidence **0.3814** [on_target=0.80 evidence=0.48] Crohns' Disease Pipeline Appears Robust With 90+ Key Pharma ... — barchart.com (#2) `A`
- ❌ low_on_target **0.0924** [on_target=0.47 evidence=0.20] LY-4395089 - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#9) `A`

## q011 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as Small Molecule targeting ITGA4 ITGB7 Integrin Alpha-4 Beta-7  
**Target sent:** drugs competing with α4β7 Inhibitor / α4β7: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['α4β7 Inhibitor', 'α4β7']

**q011-1** `α4β7 Inhibitor etrolizumab mechanism IBD` → kept 5/10, jev 426 ms

- ✅ **0.7726** [on_target=0.95 evidence=0.81] Anti-Integrins for the Treatment of Inflammatory Bowel Disease — pmc.ncbi.nlm.nih.gov (#6) `A`
- ✅ **0.6611** [on_target=0.94 evidence=0.70] Etrolizumab: Uses, Interactions, Mechanism of Action — go.drugbank.com (#1) `A`
- ✅ **0.6134** [on_target=0.92 evidence=0.67] Research progress in molecular targeted therapy for ... — link.springer.com (#4) `A`
- ✅ **0.5885** [on_target=0.91 evidence=0.65] Cellular Mechanisms of Etrolizumab Treatment in ... - PMC - NIH — pmc.ncbi.nlm.nih.gov (#7) `A`
- ✅ **0.588** [on_target=0.90 evidence=0.65] Research progress in molecular targeted therapy for inflammatory ... — link.springer.com (#2) `A`
- ❌ max_keep **0.582** [on_target=0.90 evidence=0.65] Targeting T-cell integrins in autoimmune and inflammatory diseases — academic.oup.com (#9) `A`
- ❌ max_keep **0.5452** [on_target=0.87 evidence=0.63] A randomised phase I study of etrolizumab (rhuMAb β7) in ... — pmc.ncbi.nlm.nih.gov (#3) `A`
- ❌ max_keep **0.54** [on_target=0.89 evidence=0.61] Cellular Mechanisms of Etrolizumab Treatment in ... — frontiersin.org (#10) `A`
- ❌ max_keep **0.5292** [on_target=0.84 evidence=0.63] 2.4. Integrin αeβ7 (cd103) — pmc.ncbi.nlm.nih.gov (#8) `A`
- ❌ max_keep **0.4843** [on_target=0.87 evidence=0.56] Review article: nonclinical and clinical pharmacology ... - PMC — pmc.ncbi.nlm.nih.gov (#5) `A`

**q011-4** `α4β7 Inhibitor Phase 2 Phase 3 Crohn's disease competitors` → kept 5/10, jev 361 ms

- ✅ **0.9024** [on_target=0.96 evidence=0.94] Landscape of new drugs and targets in inflammatory bowel ... — pmc.ncbi.nlm.nih.gov (#6) `A`
- ✅ **0.8992** [on_target=0.96 evidence=0.94] Integrin Inhibitor Competitive Landscape Analysis 2026 / Eureka — eureka.patsnap.com (#7) `A`
- ✅ **0.8892** [on_target=0.97 evidence=0.92] Anti-Integrins for the Treatment of Inflammatory Bowel Disease — pmc.ncbi.nlm.nih.gov (#3) `A`
- ✅ **0.8698** [on_target=0.97 evidence=0.90] Internal Medicine Vol.65 — pdfs.semanticscholar.org (#4) `A`
- ✅ **0.864** [on_target=0.96 evidence=0.90] Novel Therapies and Approaches to Inflammatory Bowel Disease (IBD) — mdpi.com (#10) `A`
- ❌ max_keep **0.8352** [on_target=0.96 evidence=0.87] pmc.ncbi.nlm.nih.gov › articles › PMC6537282New biologics and small molecules in inflammatory bowel  — pmc.ncbi.nlm.nih.gov (#8) `A`
- ❌ max_keep **0.8139** [on_target=0.95 evidence=0.86] Role of biologics and biosimilars in inflammatory bowel disease — pmc.ncbi.nlm.nih.gov (#9) `A`
- ❌ max_keep **0.7505** [on_target=0.95 evidence=0.79] IBD therapeutics: what is in the pipeline? - PMC — pmc.ncbi.nlm.nih.gov (#5) `A`
- ❌ max_keep **0.5756** [on_target=0.89 evidence=0.65] What Is The Best Medicine For Crohns Disease Explained — bookings.hants.gov.uk (#2) `A`
- ❌ max_keep **0.5002** [on_target=0.82 evidence=0.61] Next generation therapeutics for inflammatory bowel disease — pmc.ncbi.nlm.nih.gov (#1) `A`

**q011-3** `α4β7 Inhibitor abrilumab current status IBD` → kept 5/10, jev 498 ms

- ✅ **0.8601** [on_target=0.97 evidence=0.89] Internal Medicine Vol.65 — pdfs.semanticscholar.org (#2) `A`
- ✅ **0.8486** [on_target=0.95 evidence=0.89] Anti-integrin therapy for inflammatory bowel disease - PMC - NIH — pmc.ncbi.nlm.nih.gov (#10) `A`
- ✅ **0.7636** [on_target=0.92 evidence=0.83] pmc.ncbi.nlm.nih.gov · articles · PMC13453429Integrin α4β7: Pathogenic Roles in Metabolic and Inflam — pmc.ncbi.nlm.nih.gov (#3) `A`
- ✅ **0.7584** [on_target=0.96 evidence=0.79] Our Science — aviarapharma.com (#1) `A`
- ✅ **0.7489** [on_target=0.94 evidence=0.80] Emerging Treatment Options in Inflammatory Bowel Disease: Janus Kinases, Stem Cells, and More — karger.com (#6) `A`
- ❌ max_keep **0.7207** [on_target=0.94 evidence=0.77] Emerging Therapies for Inflammatory Bowel Disease - Advances in Therapy — link.springer.com (#4) `A`
- ❌ max_keep **0.7037** [on_target=0.93 evidence=0.76] Landscape of new drugs and targets in inflammatory bowel disease — onlinelibrary.wiley.com (#8) `A`
- ❌ max_keep **0.6795** [on_target=0.91 evidence=0.75] pmc.ncbi.nlm.nih.gov › articles › PMC6537282New biologics and small molecules in inflammatory bowel  — pmc.ncbi.nlm.nih.gov (#9) `A`
- ❌ max_keep **0.6248** [on_target=0.88 evidence=0.71] Table 4. — pmc.ncbi.nlm.nih.gov (#5) `A`
- ❌ max_keep **0.4654** [on_target=0.78 evidence=0.60] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#7) `A`

**q011-5** `α4β7 Inhibitor AJM300 natalizumab class comparison` → kept 5/10, jev 366 ms

- ✅ **0.8384** [on_target=0.96 evidence=0.87] Old and New Biologics and Small Molecules in Inflammatory ... — pmc.ncbi.nlm.nih.gov (#3) `A`
- ✅ **0.779** [on_target=0.92 evidence=0.85] 2.4. Integrin αeβ7 (cd103) — pmc.ncbi.nlm.nih.gov (#9) `A`
- ✅ **0.7664** [on_target=0.95 evidence=0.81] Anti-integrin therapy for inflammatory bowel disease - PMC - NIH — pmc.ncbi.nlm.nih.gov (#4) `A`
- ✅ **0.7584** [on_target=0.96 evidence=0.79] The Expanding Therapeutic Armamentarium for Inflammatory Bowel Disease: How to Choose the Right Drug — academic.oup.com (#8) `A`
- ✅ **0.7474** [on_target=0.95 evidence=0.79] Emerging Treatment Options in Inflammatory Bowel Disease: Janus Kinases, Stem Cells, and More — karger.com (#10) `A`
- ❌ max_keep **0.7426** [on_target=0.94 evidence=0.79] Frontiers / Frontiers in Drug Research and Development for Inflammatory Bowel Disease — frontiersin.org (#6) `A`
- ❌ max_keep **0.7341** [on_target=0.91 evidence=0.81] Integrin antagonists as potential therapeutic options for ... - PMC — pmc.ncbi.nlm.nih.gov (#2) `A`
- ❌ max_keep **0.6737** [on_target=0.94 evidence=0.72] AJM300 (carotegrast methyl), an oral antagonist of Î±4- ... — darmzentrum-bern.ch (#7) `A`
- ❌ max_keep **0.624** [on_target=0.90 evidence=0.69] Past, Present and Future of Therapeutic Interventions Targeting Leukocyte Trafficking in Inflammator — academic.oup.com (#1) `A`
- ❌ max_keep **0.5779** [on_target=0.88 evidence=0.66] Oral treatment with a novel small molecule alpha 4 integrin antagonist, AJM300, prevents the develop — academic.oup.com (#5) `A`

**q011-2** `α4β7 Inhibitor vedolizumab current development status 2026` → kept 5/10, jev 371 ms

- ✅ **0.9021** [on_target=0.97 evidence=0.93] Integrin α4β7 Competitive Landscape After Lilly's Morphic ... — sleuthinsights.com (#3) `A`
- ✅ **0.896** [on_target=0.96 evidence=0.93] Integrin Inhibitor Competitive Landscape Analysis 2026 / Eureka — eureka.patsnap.com (#5) `A`
- ✅ **0.8768** [on_target=0.96 evidence=0.91] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#10) `A`
- ✅ **0.7904** [on_target=0.96 evidence=0.82] Top 7 Breakthrough Drugs for Ulcerative Colitis Treatment — delveinsight.com (#6) `A`
- ✅ **0.7583** [on_target=0.94 evidence=0.81] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#7) `A`
- ❌ max_keep **0.6218** [on_target=0.91 evidence=0.68] Pipeline / Spyre Therapeutics — spyre.com (#2) `A`
- ❌ max_keep **0.5084** [on_target=0.82 evidence=0.62] www.fresenius-kabi.com › us › news-and-eventsFresenius Announces FDA and EMA ... - Fresenius Kabi Gl — fresenius-kabi.com (#4) `A`
- ❌ max_keep **0.5073** [on_target=0.89 evidence=0.57] Vedolizumab Health Professional Drug Record / NIH — clinicalinfo.hiv.gov (#8) `A`
- ❌ low_evidence **0.4147** [on_target=0.87 evidence=0.48] Takeda Pipeline, September 2026: 127 Active Clinical Trials ... — datalookout.com (#1) `A`
- ❌ low_on_target **0.3234** [on_target=0.66 evidence=0.49] abrilumab (AMG 181) / Amgen, AstraZeneca — delta.larvol.com (#9) `A`

## q012

**Objective:** Lenvatinib + Nofazinlimab pivotal, registrational, or Phase 3 trial in Unresectable or Metastatic Hepatocellular Carcinoma: planned or initiated status and expected start date  
**Target sent:** Lenvatinib + Nofazinlimab NCT04194775 / Lenvatinib / Nofazinlimab / NCT04194775 · anchors ['Lenvatinib + Nofazinlimab NCT04194775', 'Lenvatinib', 'Nofazinlimab', 'NCT04194775']

**q012-1** `Lenvatinib + Nofazinlimab NCT04194775 first patient enrollment date` → kept 5/10, jev 418 ms

- ✅ **0.8892** [on_target=0.97 evidence=0.92] A Study of Nofazinlimab (CS1003) in... / Clinical Trial — trial.medpath.com (#2) `A`
- ✅ **0.864** [on_target=0.96 evidence=0.90] Nofazinlimab - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#6) `A`
- ✅ **0.8342** [on_target=0.92 evidence=0.91] nofazinlimab (CS1003) — veri.larvol.com (#9) `A`
- ✅ **0.6888** [on_target=0.84 evidence=0.82] A Study of Nofazinlimab (CS1003) in Subjects With Advanced ... — guidelinecentral.com (#4) `A`
- ✅ **0.6794** [on_target=0.79 evidence=0.86] A Study of Nofazinlimab (CS1003) in Subjects With Advanced Hepatocellular Carcinoma — cancerindex.io (#1) `A`
- ❌ max_keep **0.6478** [on_target=0.79 evidence=0.82] Liver Epithelial Neoplasm — cancerindex.io (#3) `A`
- ❌ max_keep **0.5472** [on_target=0.76 evidence=0.72] A Study to Evaluate MIV-818 in Patients With Liver Cancer Manifestations — med.agiltrace.com (#8) `A`
- ❌ max_keep **0.52** [on_target=0.75 evidence=0.69] Lenvatinib for the Treatment of Recurrent Hepatocellular Carcinoma After Liver Transplant — med.agiltrace.com (#10) `A`
- ❌ low_on_target **0.0002** [on_target=0.06 evidence=0.00] CLINICAL TRIALS — amgentrials.com (#7)
- ❌ low_on_target **0.0** [on_target=0.11 evidence=0.00] Trials - Merck Clinical Trials — merckclinicaltrials.com (#5)

**q012-2** `Lenvatinib + Nofazinlimab NCT04194775 current trial status` → kept 5/10, jev 340 ms

- ✅ **0.9834** [on_target=0.99 evidence=0.99] NCT04194775: An ongoing trial by CStone Pharmaceuticals — fdaaa.trialstracker.net (#3) `A`
- ✅ **0.9702** [on_target=0.98 evidence=0.99] A Study of Nofazinlimab (CS1003) in Subjects With ... — guidelinecentral.com (#8) `A`
- ✅ **0.9506** [on_target=0.98 evidence=0.97] A Study of Nofazinlimab (CS1003) in... / Clinical Trial — trial.medpath.com (#1) `A`
- ✅ **0.8232** [on_target=0.98 evidence=0.84] Emerging Therapies for Hepatocellular Carcinoma - PMC — pmc.ncbi.nlm.nih.gov (#9) `A`
- ✅ **0.8096** [on_target=0.96 evidence=0.84] Nofazinlimab - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#7) `A`
- ❌ max_keep **0.7631** [on_target=0.95 evidence=0.80] The current landscape of therapies for hepatocellular carcinoma — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ max_keep **0.7566** [on_target=0.97 evidence=0.78] A Study of Nofazinlimab (CS1003) in Subjects With Advanced Hepatocellular Carcinoma — clinicaltrials.gov (#2) `A`
- ❌ max_keep **0.6479** [on_target=0.93 evidence=0.70] Current status of the cost burden of first-line systemic treatment for ... — academic.oup.com (#6) `A`
- ❌ max_keep **0.6281** [on_target=0.83 evidence=0.76] A Study to Evaluate MIV-818 in Patients With Liver Cancer Manifestations — med.agiltrace.com (#4) `A`
- ❌ max_keep **0.5254** [on_target=0.74 evidence=0.71] Lenvatinib for the Treatment of Recurrent Hepatocellular Carcinoma After Liver Transplant — med.agiltrace.com (#5) `A`

## q013

**Objective:** SD-133 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** SD-133 · anchors ['SD-133']

**q013-2** `SD-133 tumour regression pancreatic cancer animal model` → ABSTAIN, jev 339 ms

- ❌ low_on_target **0.0704** [on_target=0.16 evidence=0.44] Gene therapy in pancreatic cancer - Baishideng Publishing Group — wjgnet.com (#8)
- ❌ low_on_target **0.0428** [on_target=0.12 evidence=0.36] [PDF] A targeted combination therapy achieves effective pancreatic cancer ... — iris.unito.it (#9)
- ❌ low_on_target **0.0246** [on_target=0.09 evidence=0.27] Immunotherapy and targeted therapies in animal models of ... — publications.rwth-aachen.de (#6)
- ❌ low_on_target **0.0138** [on_target=0.06 evidence=0.23] Oncolytic viral therapy as a novel potential solution for ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0071** [on_target=0.03 evidence=0.24] Challenges and advances in mouse modeling for human ... — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0051** [on_target=0.02 evidence=0.26] Experimental models of pancreas cancer: what has been the impact ... — jci.org (#3)
- ❌ low_on_target **0.0041** [on_target=0.02 evidence=0.20] Progress in Animal Models of Pancreatic Ductal ... — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0028** [on_target=0.02 evidence=0.14] Modeling pancreatic cancer in mice for experimental therapeutics — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.0027** [on_target=0.02 evidence=0.14] Pathogenesis of Pancreatic Cancer: Lessons from Animal ... — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0011** [on_target=0.02 evidence=0.06] Models in Pancreatic Neuroendocrine Neoplasms: Current Perspectives and Future Directions — mdpi.com (#7)

**q013-1** `SD-133 pancreatic ductal adenocarcinoma monotherapy xenograft TGI` → ABSTAIN, jev 368 ms

- ❌ low_on_target **0.071** [on_target=0.30 evidence=0.24] Pancreatic Cancer Treatment (PDQ®) — cancer.gov (#10)
- ❌ low_on_target **0.0707** [on_target=0.20 evidence=0.35] Pancreatic ductal adenocarcinoma: Treatment hurdles ... — wjgnet.com (#2)
- ❌ low_on_target **0.0576** [on_target=0.16 evidence=0.36] Pancreatic ductal adenocarcinoma: Treatment hurdles, tumor ... — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0288** [on_target=0.09 evidence=0.32] Radioimmunotherapy of Pancreatic Ductal Adenocarcinoma: A Review of the Current Status of Literature — mdpi.com (#3)
- ❌ low_on_target **0.0256** [on_target=0.08 evidence=0.32] Immune therapies in pancreatic ductal adenocarcinoma: Where are we now? — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0237** [on_target=0.10 evidence=0.24] Full article: Next-generation therapies for pancreatic cancer — tandfonline.com (#1)
- ❌ low_on_target **0.0215** [on_target=0.34 evidence=0.06] E> ��?�"�T����Ԩ$h��N$lyf~����������50#���W//w��衴�*�a��ǔ N�<������D�W�oP��-�9촦�Mr{��b4�����q�*����#�� — korea.kr (#7)
- ❌ low_on_target **0.0063** [on_target=0.04 evidence=0.16] Management of pancreatic ductal adenocarcinoma (PDAC) - OAText — oatext.com (#8)
- ❌ low_on_target **0.0036** [on_target=0.04 evidence=0.09] Pancreatic Ductal Adenocarcinoma in the Era of Precision Medicine — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0028** [on_target=0.04 evidence=0.07] Pancreatic Ductal Adenocarcinoma in the Era of Precision ... — pmc.ncbi.nlm.nih.gov (#6)

## q014

**Objective:** Sirpiglenastat in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** Sirpiglenastat / DRP-104 · anchors ['Sirpiglenastat', 'DRP-104']

**q014-1** `Sirpiglenastat PDAC monotherapy TGI xenograft` → kept 5/10, jev 435 ms

- ✅ **0.8745** [on_target=0.99 evidence=0.88] Targeting pancreatic cancer metabolic dependencies through glutamine antagonism — nature.com (#5) `A`
- ✅ **0.7293** [on_target=0.99 evidence=0.74] Sirpiglenastat (DRP-104) Induces Antitumor Efficacy through Direct ... — ouci.dntb.gov.ua (#1) `A`
- ✅ **0.686** [on_target=0.98 evidence=0.70] Metabolic plasticity in pancreatic ductal adenocarcinoma ... — link.springer.com (#2) `A`
- ✅ **0.6566** [on_target=0.98 evidence=0.67] [PDF] November 2022 — datocms-assets.com (#8) `A`
- ✅ **0.6434** [on_target=0.97 evidence=0.66] Clinical development of metabolic inhibitors for oncology - PMC — pmc.ncbi.nlm.nih.gov (#9) `A`
- ❌ max_keep **0.6402** [on_target=0.98 evidence=0.65] Sirpiglenastat (DRP-104, CAS Number: 2079939-05-0) — caymanchem.com (#10) `A`
- ❌ max_keep **0.6239** [on_target=0.95 evidence=0.66] sirpiglenastat (DRP-104) / Dracen Pharma — delta.larvol.com (#6) `A`
- ❌ max_keep **0.6049** [on_target=0.95 evidence=0.64] Table 3. Various stromal components in PDAC, agents that target them and observed effects of targeti — pmc.ncbi.nlm.nih.gov (#7) `A`
- ❌ max_keep **0.5672** [on_target=0.91 evidence=0.62] JHU083 / Johns Hopkins University, AstraZeneca - LARVOL DELTA — delta.larvol.com (#3) `A`
- ❌ max_keep **0.4882** [on_target=0.97 evidence=0.50] sirpiglenastat - Drug Hunter — drughunter.com (#4) `A`

**q014-2** `DRP-104 pancreatic cancer single-agent tumour regression` → kept 5/10, jev 345 ms

- ✅ **0.9042** [on_target=0.99 evidence=0.91] Targeting pancreatic cancer metabolic dependencies through ... — pmc.ncbi.nlm.nih.gov (#4) `A`
- ✅ **0.891** [on_target=0.99 evidence=0.90] Targeting pancreatic cancer metabolic dependencies through glutamine antagonism — nature.com (#1) `A`
- ✅ **0.7949** [on_target=0.95 evidence=0.84] Discovery of DRP-104, a tumor-targeted metabolic inhibitor prodrug - PubMed — pubmed.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.7448** [on_target=0.98 evidence=0.76] Discovery of DRP-104, a tumor-targeted metabolic inhibitor ... — pdfs.semanticscholar.org (#9) `A`
- ✅ **0.722** [on_target=0.98 evidence=0.74] Beyond the tumor: Enhancing pancreatic cancer therapy through ... — pmc.ncbi.nlm.nih.gov (#8) `A`
- ❌ max_keep **0.6688** [on_target=0.96 evidence=0.70] Discovery of DRP-104, a tumor-targeted metabolic inhibitor prodrug — pmc.ncbi.nlm.nih.gov (#3) `A`
- ❌ max_keep **0.6598** [on_target=0.98 evidence=0.67] Dracen Pharmaceuticals announces oral presentation at Festival of Biologics World Immunotherapy Cong — prweb.com (#10) `A`
- ❌ max_keep **0.65** [on_target=0.98 evidence=0.66] Dracen Pharmaceuticals announces publication in Molecular Cancer Therapeutics — prweb.com (#6) `A`
- ❌ max_keep **0.6072** [on_target=0.92 evidence=0.66] The impact of broad glutamine metabolism inhibition on ... — pmc.ncbi.nlm.nih.gov (#5) `A`
- ❌ max_keep **0.601** [on_target=0.92 evidence=0.65] DON/DRP-104 as innovative Plasma kallikrein inhibitors ... — pmc.ncbi.nlm.nih.gov (#7) `A`

**q014-3** `Sirpiglenastat pancreatic PDX monotherapy tumour volume` → kept 5/10, jev 362 ms

- ✅ **0.748** [on_target=0.98 evidence=0.76] Targeting pancreatic cancer metabolic dependencies through ... — pubmed.ncbi.nlm.nih.gov (#10) `A`
- ✅ **0.7146** [on_target=0.97 evidence=0.74] Sirpiglenastat – Glutamine Antagonist for Cancer Research — benchchem.com (#7) `A`
- ✅ **0.6693** [on_target=0.97 evidence=0.69] Characterization and therapeutic suppression of KEAP1-NRF2-driven resistance to KRAS inhibitors in p — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.6468** [on_target=0.98 evidence=0.66] Sirpiglenastat (DRP-104), a broad acting glutamine ... — dracenpharma.com (#3) `A`
- ✅ **0.6402** [on_target=0.97 evidence=0.66] Sirpiglenastat (DRP-104, CAS Number: 2079939-05-0) — caymanchem.com (#9) `A`
- ❌ max_keep **0.5952** [on_target=0.93 evidence=0.64] Clinical development of metabolic inhibitors for oncology. — europepmc.org (#8) `A`
- ❌ low_evidence **0.4294** [on_target=0.92 evidence=0.47] Table 2. — pmc.ncbi.nlm.nih.gov (#4) `A`
- ❌ low_evidence **0.3136** [on_target=0.97 evidence=0.32] Sirpiglenastat (DRP-104) / Glutaminase antagonist — selleckchem.com (#6) `A`
- ❌ low_on_target **0.0004** [on_target=0.12 evidence=0.00] PDC000198 - Proteomic Data Commons - National Cancer Institute — proteomic.datacommons.cancer.gov (#1)
- ❌ low_on_target **0.0001** [on_target=0.03 evidence=0.00] Cloudflare — aacrjournals.org (#2)

**q014-5** `Sirpiglenastat pancreatic cancer in vivo monotherapy` → kept 5/10, jev 381 ms

- ✅ **0.8811** [on_target=0.99 evidence=0.89] Targeting pancreatic cancer metabolic dependencies through glutamine antagonism — nature.com (#1) `A`
- ✅ **0.7676** [on_target=0.98 evidence=0.78] GEO Accession viewer — ncbi.nlm.nih.gov (#8) `A`
- ✅ **0.7534** [on_target=0.97 evidence=0.78] Oncometabolites in pancreatic cancer: Strategies and its ... — wjgnet.com (#10) `A`
- ✅ **0.686** [on_target=0.98 evidence=0.70] Sirpiglenastat (DRP-104) Induces Antitumor Efficacy through ... — oamonitor.ireland.openaire.eu (#4) `A`
- ✅ **0.6467** [on_target=0.97 evidence=0.67] sirpiglenastat (DRP-104) / Dracen Pharma — delta.larvol.com (#9) `A`
- ❌ max_keep **0.6402** [on_target=0.97 evidence=0.66] Sirpiglenastat (DRP-104) / Glutamine Antagonist — targetmol.com (#2) `A`
- ❌ max_keep **0.637** [on_target=0.97 evidence=0.66] Clinical development of metabolic inhibitors for oncology — jci.org (#7) `A`
- ❌ max_keep **0.5664** [on_target=0.96 evidence=0.59] Table 1. — pmc.ncbi.nlm.nih.gov (#6) `A`
- ❌ max_keep **0.5572** [on_target=0.84 evidence=0.66] RMC-7977 / Revolution Medicines - Larvol Delta — delta.larvol.com (#3) `A`
- ❌ max_keep **0.54** [on_target=0.97 evidence=0.56] Sirpiglenastat (DRP-104) / Glutaminase antagonist — selleckchem.com (#5) `A`

**q014-4** `DRP-104 PDAC xenograft dose response` → kept 5/10, jev 429 ms

- ✅ **0.8984** [on_target=0.98 evidence=0.92] Targeting pancreatic cancer metabolic dependencies ... — nature.com (#2) `A`
- ✅ **0.7774** [on_target=0.98 evidence=0.79] GEO Accession viewer — ncbi.nlm.nih.gov (#7) `A`
- ✅ **0.7546** [on_target=0.98 evidence=0.77] Targeting pancreatic cancer metabolic dependencies through ... — pubmed.ncbi.nlm.nih.gov (#10) `A`
- ✅ **0.6632** [on_target=0.98 evidence=0.68] sirpiglenastat (DRP-104) / Dracen Pharma — delta.larvol.com (#6) `A`
- ✅ **0.65** [on_target=0.98 evidence=0.66] Broad glutamine pathway inhibition by DRP-104 results in ... — dracenpharma.com (#1) `A`
- ❌ max_keep **0.6267** [on_target=0.94 evidence=0.67] The Landscape of Cancer Metabolism as a Therapeutic ... — onlinelibrary.wiley.com (#8) `A`
- ❌ max_keep **0.6076** [on_target=0.93 evidence=0.65] Glutamine antagonist DRP-104 suppresses tumor growth and enhances response to checkpoint blockade in — pubmed.ncbi.nlm.nih.gov (#5) `A`
- ❌ max_keep **0.6072** [on_target=0.92 evidence=0.66] Targeting glutamine dependence with DRP-104 inhibits proliferation ... — pmc.ncbi.nlm.nih.gov (#4) `A`
- ❌ max_keep **0.6014** [on_target=0.93 evidence=0.65] Glutamine antagonist DRP-104 suppresses tumor growth ... — biorxiv.org (#3) `A`
- ❌ max_keep **0.5953** [on_target=0.94 evidence=0.63] Dracen Pharmaceuticals, Inc. - Drug pipelines, Patents ... — synapse.patsnap.com (#9) `A`

## q015

**Objective:** GFH375/VS-7375 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in KRAS G12D-Mutated/MTAP-Deleted Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** GFH375 VS-7375 / GFH375 / VS-7375 · anchors ['GFH375 VS-7375', 'GFH375', 'VS-7375']

**q015-1** `GFH375 VS-7375 quantitative TGI KP4 PDAC monotherapy` → kept 5/10, jev 353 ms

- ✅ **0.6794** [on_target=0.98 evidence=0.69] [PDF] VS-7375: An oral, selective KRAS G12D dual ON/OFF inhibitor with ... — verastem.com (#2) `A`
- ✅ **0.6696** [on_target=0.98 evidence=0.68] VS-7375 (GFH375): An oral, selective KRAS G12D (ON/ ... — verastem.com (#9) `A`
- ✅ **0.6531** [on_target=0.97 evidence=0.67] GenFleet Therapeutics Announces Data of VS-7375 ... — genfleet.com (#4) `A`
- ✅ **0.6111** [on_target=0.97 evidence=0.63] Pipeline / Verastem, Inc. — verastem.com (#6) `A`
- ✅ **0.5792** [on_target=0.96 evidence=0.60] Press Release — investor.verastem.com (#10) `A`
- ❌ max_keep **0.5672** [on_target=0.91 evidence=0.62] GFH375/VS-7375 Granted with FDA's Fast Track ... — genfleet.com (#7) `A`
- ❌ max_keep **0.5568** [on_target=0.96 evidence=0.58] GFH375/VS-7375 Program Update — genfleet.com (#1) `A`
- ❌ max_keep **0.5529** [on_target=0.97 evidence=0.57] Untitled — sec.gov (#5) `A`
- ❌ max_keep **0.5452** [on_target=0.94 evidence=0.58] GenFleet Therapeutics (Shanghai) Inc. 勁方醫藥科技(上海) ... — www1.hkexnews.hk (#8) `A`
- ❌ max_keep **0.5367** [on_target=0.97 evidence=0.55] [PDF] GenFleet Therapeutics (Shanghai) Inc. 勁方醫藥科技(上海)股份有限 ... — www1.hkexnews.hk (#3) `A`

**q015-2** `GFH375 VS-7375 MTAP-deleted KP4 monotherapy tumour regression` → kept 5/10, jev 356 ms

- ✅ **0.7469** [on_target=0.97 evidence=0.77] [PDF] Verastem Oncology Announces Late Breaking and Regular ... — investor.verastem.com (#4) `A`
- ✅ **0.7154** [on_target=0.98 evidence=0.73] VS-7375 (GFH375): An oral, selective KRAS G12D (ON/ ... — verastem.com (#1) `A`
- ✅ **0.6794** [on_target=0.98 evidence=0.69] [PDF] VS-7375: An oral, selective KRAS G12D dual ON/OFF inhibitor with ... — verastem.com (#5) `A`
- ✅ **0.6696** [on_target=0.98 evidence=0.68] AACR 2026: GenFleet Therapeutics Announces Data of VS-7375 ... — genfleet.com (#2) `A`
- ✅ **0.6624** [on_target=0.92 evidence=0.72] Verastem Oncology Announces Late Breaking and Regular ... — investor.verastem.com (#9) `A`
- ❌ max_keep **0.6624** [on_target=0.96 evidence=0.69] Selectivity over HUVEC (P value not updated) - verastem.com — verastem.com (#10) `A`
- ❌ max_keep **0.6586** [on_target=0.95 evidence=0.69] Selectivity over HUVEC （P value not updated) — verastem.com (#7) `A`
- ❌ max_keep **0.6194** [on_target=0.92 evidence=0.67] Resources / Verastem, Inc. — verastem.com (#3) `A`
- ❌ max_keep **0.5568** [on_target=0.96 evidence=0.58] Untitled — sec.gov (#8) `A`
- ❌ max_keep **0.5536** [on_target=0.96 evidence=0.58] GFH375/VS-7375 Program Update — genfleet.com (#6) `A`

**q015-3** `GFH375 VS-7375 MTAP-deleted pancreatic xenograft single-agent TGI` → kept 5/10, jev 334 ms

- ✅ **0.833** [on_target=0.98 evidence=0.85] [PDF] Verastem Oncology Announces Late Breaking and Regular ... — investor.verastem.com (#7) `A`
- ✅ **0.7088** [on_target=0.98 evidence=0.72] VS-7375 (GFH375): An oral, selective KRAS G12D (ON/ ... — verastem.com (#4) `A`
- ✅ **0.7056** [on_target=0.98 evidence=0.72] 展现产品强效抑瘤活性、持久通路抑制及多种联用方案开发潜力 — moomoo.com (#5) `A`
- ✅ **0.6952** [on_target=0.97 evidence=0.72] 展現產品強效抑瘤活性、持久通路抑制及多種聯用方案開發潛力 — moomoo.com (#6) `A`
- ✅ **0.6696** [on_target=0.98 evidence=0.68] GenFleet Therapeutics Announces Data of VS-7375 ... — genfleet.com (#3) `A`
- ❌ max_keep **0.6632** [on_target=0.98 evidence=0.68] [PDF] VS-7375: An oral, selective KRAS G12D dual ON/OFF inhibitor with ... — verastem.com (#2) `A`
- ❌ max_keep **0.6262** [on_target=0.93 evidence=0.67] Resources / Verastem, Inc. — verastem.com (#1) `A`
- ❌ max_keep **0.582** [on_target=0.97 evidence=0.60] GenFleet Therapeutics (Shanghai) Inc. 勁方醫藥科技(上海) ... — www1.hkexnews.hk (#10) `A`
- ❌ max_keep **0.4957** [on_target=0.88 evidence=0.56] GFH-375 (GFH-375) - 药物靶点：KRAS G12D_在研适应症：转移性胰腺癌... — synapse.zhihuiya.com (#9) `A`
- ❌ low_evidence **0.464** [on_target=0.96 evidence=0.48] GFH375/VS-7375 Program Update — genfleet.com (#8) `A`

**q015-4** `GFH375 VS-7375 AsPC-1 Panc 04.03 monotherapy tumour volume data` → kept 5/10, jev 341 ms

- ✅ **0.7578** [on_target=0.98 evidence=0.77] VS-7375 (GFH375): An oral, selective KRAS G12D (ON/ ... — verastem.com (#7) `A`
- ✅ **0.5734** [on_target=0.94 evidence=0.61] VS-7375 / Verastem, GenFleet Therap — delta.larvol.com (#5) `A`
- ✅ **0.5723** [on_target=0.97 evidence=0.59] Press Release - Verastem, Inc. — investor.verastem.com (#9) `A`
- ✅ **0.5704** [on_target=0.86 evidence=0.66] Selectivity over HUVEC (P value not updated) - verastem.com — verastem.com (#1) `A`
- ✅ **0.5636** [on_target=0.95 evidence=0.59] GenFleet Therapeutics Announces Data of VS-7375 ... — genfleet.com (#3) `A`
- ❌ max_keep **0.549** [on_target=0.90 evidence=0.61] Exhibit 99.2 - SEC.gov — sec.gov (#10) `A`
- ❌ max_keep **0.5451** [on_target=0.83 evidence=0.66] Selectivity over HUVEC （P value not updated) — verastem.com (#2) `A`
- ❌ max_keep **0.5289** [on_target=0.95 evidence=0.56] GFH375/VS-7375 Program Update — genfleet.com (#6) `A`
- ❌ max_keep **0.4928** [on_target=0.88 evidence=0.56] GFH-375 - Drug Targets, Indications, Patents — synapse.patsnap.com (#8) `A`
- ❌ low_on_target **0.2967** [on_target=0.50 evidence=0.59] Slide 1 — verastem.com (#4)

## q016

**Objective:** PLM-103 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic ductal adenocarcinoma (PDAC) animal models  
**Target sent:** PLM-103 · anchors ['PLM-103']

**q016-1** `PLM-103 PDAC xenograft monotherapy tumour regression TGI` → ABSTAIN, jev 500 ms

- ❌ low_on_target **0.3852** [on_target=0.53 evidence=0.73] Patient-Derived Xenograft Models of Pancreatic Cancer - PMC — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_evidence **0.0276** [on_target=0.92 evidence=0.03] PLM-103 - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#10) `A`
- ❌ low_on_target **0.0176** [on_target=0.53 evidence=0.03] Evaluation of the safety, pharmacokinetics, and antitumor activity of ... — sciencedirect.com (#7)
- ❌ low_on_target **0.0068** [on_target=0.03 evidence=0.23] Patient Derived Xenograft Models: An Emerging Platform for ... — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0047** [on_target=0.20 evidence=0.02] A potential therapeutic target for pancreatic ductal adenocarcinoma — sciencedirect.com (#9)
- ❌ low_on_target **0.0022** [on_target=0.02 evidence=0.11] Patient-derived xenograft models: Current status ... — sciencedirect.com (#5)
- ❌ low_on_target **0.002** [on_target=0.12 evidence=0.02] OpenLB Open Library of Bioscience — ngdc.cncb.ac.cn (#6)
- ❌ low_on_target **0.0002** [on_target=0.07 evidence=0.00] CCDI Hub — moleculartargets.ccdi.cancer.gov (#1)
- ❌ low_on_target **0.0** [on_target=0.03 evidence=0.00] Cloudflare — aacrjournals.org (#2)
- ❌ low_on_target **0.0** [on_target=0.08 evidence=0.00] Page not found — medschool.cuanschutz.edu (#4)

## q017

**Objective:** SW-682 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Head and Neck Squamous Cell Carcinoma animal models  
**Target sent:** SW-682 · anchors ['SW-682']

**q017-1** `SW-682 CAL-33 SCC-25 xenograft tumour growth inhibition monotherapy` → kept 5/10, jev 350 ms

- ✅ **0.656** [on_target=0.96 evidence=0.68] SW-682 - Drug Targets, Indications, Patents — synapse.patsnap.com (#7) `A`
- ✅ **0.6468** [on_target=0.98 evidence=0.66] SW-682 / EMD Serono — delta.larvol.com (#2) `A`
- ✅ **0.6402** [on_target=0.98 evidence=0.65] [PDF] SW-682: a novel TEAD inhibitor for the treatment of cancers bearing ... — springworkstx.com (#3) `A`
- ✅ **0.6396** [on_target=0.95 evidence=0.67] Genigraphics Research Poster Template 42x72 — springworkstx.com (#1) `A`
- ✅ **0.6336** [on_target=0.96 evidence=0.66] TEAD inhib News — sigma.larvol.com (#5) `A`
- ❌ low_evidence **0.428** [on_target=0.98 evidence=0.44] Definition of TEAD inhibitor SW-682 - NCI Drug Dictionary — cancer.gov (#8) `A`
- ❌ low_on_target **0.0355** [on_target=0.14 evidence=0.25] Radiosensitising Cancer Using Phosphatidylinositol-3 ... — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0111** [on_target=0.37 evidence=0.03] Proprietary Information of MD Anderson — cdn.clinicaltrials.gov (#10)
- ❌ low_on_target **0.0** [on_target=0.15 evidence=0.00] Something went wrong — tandfonline.com (#4)
- ❌ low_on_target **0.0** [on_target=0.03 evidence=0.00] Cloudflare — aacrjournals.org (#6)

**q017-2** `SW-682 HNSCC xenograft tumour regression monotherapy` → kept 5/10, jev 353 ms

- ✅ **0.7906** [on_target=0.98 evidence=0.81] Targeting YAP/TAZ-TEAD signaling as a therapeutic approach in ... — pmc.ncbi.nlm.nih.gov (#4) `A`
- ✅ **0.7808** [on_target=0.98 evidence=0.80] Targeting TEAD in cancer - PMC - NIH — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.6892** [on_target=0.98 evidence=0.70] SW-682(SW-682) - 药物靶点：TEAD_在研适应症：晚期恶性实体瘤 — synapse.zhihuiya.com (#6) `A`
- ✅ **0.6566** [on_target=0.98 evidence=0.67] SW-682 / EMD Serono — delta.larvol.com (#2) `A`
- ✅ **0.6304** [on_target=0.96 evidence=0.66] [PDF] SW-682: a novel TEAD inhibitor for the treatment of cancers bearing ... — springworkstx.com (#3) `A`
- ❌ max_keep **0.6301** [on_target=0.95 evidence=0.66] Genigraphics Research Poster Template 42x72 — springworkstx.com (#1) `A`
- ❌ max_keep **0.5982** [on_target=0.97 evidence=0.62] GEO Accession viewer — ncbi.nlm.nih.gov (#7) `A`
- ❌ max_keep **0.4834** [on_target=0.74 evidence=0.65] GSE280355 - Inhibition of the chemokine receptors ... — omicsdi.org (#10)
- ❌ low_on_target **0.009** [on_target=0.06 evidence=0.15] Targeted therapy for head and neck cancer: signaling pathways and clinical studies — nature.com (#9)
- ❌ low_on_target **0.0047** [on_target=0.04 evidence=0.12] Patient-Derived Xenograft and Organoid Models for Precision Medicine Targeting of the Tumour Microen — mdpi.com (#8)

**q017-3** `SW-682 CAL-33 SCC-25 tumour volume TGI` → kept 2/10, jev 354 ms

- ✅ **0.705** [on_target=0.94 evidence=0.75] Genigraphics Research Poster Template 42x72 — springworkstx.com (#1) `A`
- ✅ **0.5344** [on_target=0.96 evidence=0.56] [PDF] SW-682: a novel TEAD inhibitor for the treatment of cancers bearing ... — springworkstx.com (#3) `A`
- ❌ low_evidence **0.4669** [on_target=0.94 evidence=0.50] SW-682 - Drug Targets, Indications, Patents — synapse.patsnap.com (#8) `A`
- ❌ low_evidence **0.3261** [on_target=0.95 evidence=0.34] SW-682 / EMD Serono — delta.larvol.com (#10) `A`
- ❌ low_on_target **0.019** [on_target=0.38 evidence=0.05] Exaly Platform — exaly.com (#5)
- ❌ low_on_target **0.0072** [on_target=0.27 evidence=0.03] https://portal.gdc.cancer.gov/files/4dc5c136-8c43-... — portal.gdc.cancer.gov (#7)
- ❌ low_on_target **0.0007** [on_target=0.11 evidence=0.01] Probabilistic analysis of tumor growth inhibition models to ... — sciencedirect.com (#9)
- ❌ low_on_target **0.0002** [on_target=0.07 evidence=0.00] CCDI Hub — moleculartargets.ccdi.cancer.gov (#2)
- ❌ low_on_target **0.0** [on_target=0.03 evidence=0.00] Cloudflare — aacrjournals.org (#4)
- ❌ low_on_target **0.0** [on_target=0.03 evidence=0.00] Advanced Search Results - PubMed - NIH — pubmed.ncbi.nlm.nih.gov (#6)

## q018

**Objective:** SPR2015 in vivo animal models and results: cell-line xenograft CDX, patient-derived xenograft PDX, syngeneic, orthotopic, or genetically engineered models  
**Target sent:** SPR2015 · anchors ['SPR2015']

**q018-1** `SPR2015 HNSCC in vivo xenograft` → kept 3/10, jev 372 ms

- ✅ **0.944** [on_target=0.98 evidence=0.96] Merck, SciBrunch Launch Up-to-$2.13B Collaboration ... — genengnews.com (#3) `A`
- ✅ **0.7631** [on_target=0.97 evidence=0.79] Merck Licenses Preclinical KRAS G12D Inhibitor from SciBrunch — pharmexec.com (#8) `A`
- ✅ **0.6822** [on_target=0.97 evidence=0.70] Merck Enters into Exclusive Global License Agreement ... — businesswire.com (#1) `A`
- ❌ low_on_target **0.3293** [on_target=0.40 evidence=0.82] [PDF] Download PDF - eScholarship.org — escholarship.org (#9)
- ❌ low_on_target **0.0643** [on_target=0.10 evidence=0.64] Genomic and single-cell characterization of patient-derived tumor organoid models of head and neck s — ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0616** [on_target=0.11 evidence=0.56] Tumor grafts derived from patients with head and neck squamous carcinoma authentically maintain the  — pubmed.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0567** [on_target=0.10 evidence=0.57] Establishment and characterization of patient-derived xenografts as paraclinical models for head and — pubmed.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.055** [on_target=0.11 evidence=0.50] A Standard Protocol for the Production and Bioevaluation of Ethical In Vivo Models of HPV-Negative H — pubs.acs.org (#7)
- ❌ low_on_target **0.043** [on_target=0.10 evidence=0.43] Models of head and neck squamous cell carcinoma using ... — sciencedirect.com (#2)
- ❌ low_on_target **0.0345** [on_target=0.09 evidence=0.38] Preclinical models in head and neck squamous cell carcinoma — nature.com (#4)

**q018-2** `SPR2015 PDAC patient-derived xenograft` → kept 5/10, jev 333 ms

- ✅ **0.9636** [on_target=0.98 evidence=0.98] SPR2015是一种高效且选择性的KRAS G12D（ON）抑制剂，在临床前模型中... — posterkeep.com (#3) `A`
- ✅ **0.9376** [on_target=0.98 evidence=0.96] Merck, SciBrunch Launch Up-to-$2.13B Collaboration ... — genengnews.com (#6) `A`
- ✅ **0.82** [on_target=0.98 evidence=0.84] KRAS G12D Inhibitor's $2.13B Deal Tests Cross-Border Tech Transfer — pharmtech.com (#4) `A`
- ✅ **0.7501** [on_target=0.97 evidence=0.77] Merck Licenses Preclinical KRAS G12D Inhibitor from SciBrunch — pharmexec.com (#5) `A`
- ✅ **0.748** [on_target=0.98 evidence=0.76] MSD takes a $400m bite of SciBrunch's KRAS drug — pharmaphorum.com (#2) `A`
- ❌ max_keep **0.7469** [on_target=0.97 evidence=0.77] Merck licenses KRAS G12D inhibitor for $400M upfront - Investing.com — investing.com (#10) `A`
- ❌ max_keep **0.735** [on_target=0.98 evidence=0.75] Merck Inks $2.1B Deal With Chinese Biotech to Expand Oncology ... — zacks.com (#8) `A`
- ❌ max_keep **0.7088** [on_target=0.98 evidence=0.72] Merck Enters into Exclusive Global License Agreement ... — businesswire.com (#1) `A`
- ❌ max_keep **0.6919** [on_target=0.97 evidence=0.71] MSD bets $2.13bn on SciBrunch’s KRAS (ON) inhibitor — pharmaceutical-technology.com (#7) `A`
- ❌ low_on_target **0.115** [on_target=0.17 evidence=0.68] Genomic characterization of patient-derived xenograft models ... — pmc.ncbi.nlm.nih.gov (#9)

**q018-5** `SPR2015 HPAC AsPC-1 tumour volume percentage inhibition` → kept 1/10, jev 371 ms

- ✅ **0.5206** [on_target=0.97 evidence=0.54] SPR-2015 (SPR-2015) - 药物靶点：KRAS G12D_在研适应症：结直肠癌，... — synapse.zhihuiya.com (#10) `A`
- ❌ low_on_target **0.026** [on_target=0.60 evidence=0.04] Safety, pharmacokinetics, and antitumor activity of the anti ... — sciencedirect.com (#8)
- ❌ low_on_target **0.0147** [on_target=0.49 evidence=0.03] Evaluation of the safety, pharmacokinetics, and antitumor activity of ... — sciencedirect.com (#7)
- ❌ low_on_target **0.0092** [on_target=0.46 evidence=0.02] Proprietary Information of MD Anderson — cdn.clinicaltrials.gov (#9)
- ❌ low_on_target **0.0006** [on_target=0.17 evidence=0.00] register — academic.oup.com (#6)
- ❌ low_on_target **0.0004** [on_target=0.11 evidence=0.00] PubChem BioAssay — ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0003** [on_target=0.09 evidence=0.00] PDC000198 - Proteomic Data Commons - National Cancer Institute — proteomic.datacommons.cancer.gov (#2)
- ❌ low_on_target **0.0003** [on_target=0.10 evidence=0.00] PDC000116 - Proteomic Data Commons - National Cancer Institute — proteomic.datacommons.cancer.gov (#4)
- ❌ low_on_target **0.0** [on_target=0.12 evidence=0.00] register — academic.oup.com (#1)
- ❌ low_on_target **0.0** [on_target=0.04 evidence=0.00] Cloudflare — aacrjournals.org (#5)

**q018-4** `SPR2015 PDAC genetically engineered mouse model` → ABSTAIN, jev 353 ms

- ❌ low_on_target **0.0724** [on_target=0.12 evidence=0.60] Mouse Models of Pancreatic Ductal Adenocarcinoma — 2024.sci-hub.se (#2)
- ❌ low_on_target **0.0547** [on_target=0.10 evidence=0.55] Models of pancreatic ductal adenocarcinoma - PMC — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0517** [on_target=0.10 evidence=0.52] Genetically Engineered Mouse Models of Pancreatic Cancer — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0427** [on_target=0.10 evidence=0.43] Genetically engineered mouse models of pancreatic cancer — pubmed.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.036** [on_target=0.09 evidence=0.40] Deploying Mouse Models of Pancreatic Cancer for Chemoprevention Studies — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0264** [on_target=0.08 evidence=0.33] Mouse Models of Pancreatic Ductal Adenocarcinoma - PubMed — pubmed.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.025** [on_target=0.07 evidence=0.36] Genetically engineered mouse models of pancreatic ... - PMC — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0226** [on_target=0.06 evidence=0.38] Current methods in mouse models of pancreatic cancer — mdanderson.elsevierpure.com (#3)
- ❌ low_on_target **0.021** [on_target=0.09 evidence=0.23] Genetically engineered mouse models of pancreatic adenocarcinoma — sciencedirect.com (#9)
- ❌ low_on_target **0.0208** [on_target=0.06 evidence=0.35] Mouse models of pancreatic cancer - PMC - NIH — pmc.ncbi.nlm.nih.gov (#5)

**q018-3** `SPR2015 PDAC syngeneic model` → kept 2/10, jev 466 ms

- ✅ **0.931** [on_target=0.98 evidence=0.95] SPR2015是一种高效且选择性的KRAS G12D（ON）抑制剂，在临床前模型中... — posterkeep.com (#1) `A`
- ✅ **0.9118** [on_target=0.97 evidence=0.94] Merck, SciBrunch Launch Up-to-$2.13B Collaboration ... — genengnews.com (#4) `A`
- ❌ low_on_target **0.098** [on_target=0.14 evidence=0.70] Unbiased in vivo preclinical evaluation of anticancer drugs identifies effective therapy for the tre — pubmed.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0709** [on_target=0.14 evidence=0.51] Genetically Engineered Mouse Models of Pancreatic Cancer ... — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.036** [on_target=0.08 evidence=0.45] Preclinical mouse models for immunotherapeutic and non-immunotherapeutic drug development for pancre — ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0328** [on_target=0.08 evidence=0.41] Preclinical Models of Pancreatic Ductal Adenocarcinoma ... — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0323** [on_target=0.08 evidence=0.40] Preclinical models of pancreatic ductal adenocarcinoma — cco.amegroups.org (#2)
- ❌ low_on_target **0.024** [on_target=0.06 evidence=0.40] Modeling pancreatic cancer in mice for experimental ... — pubmed.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.021** [on_target=0.06 evidence=0.35] 1 — journals.physiology.org (#8)
- ❌ low_on_target **0.0001** [on_target=0.03 evidence=0.00] Mealey's — mealeys.com (#3)

## q019

**Objective:** Innovent Biologics Inc. descriptions of IBI-3001's advantage over existing treatments for Head and Neck Squamous Cell Carcinoma in investor materials, earnings calls, investor day presentations, and press releases  
**Target sent:** IBI-3001 · anchors ['IBI-3001']

**q019-2** `IBI3001 recurrent metastatic HNSCC Innovent press release` → kept 5/10, jev 352 ms

- ✅ **0.6111** [on_target=0.95 evidence=0.64] Press Release — en.innoventbio.com (#2) `A`
- ✅ **0.6046** [on_target=0.97 evidence=0.62] Takeda Announces Oncology Partnership with Innovent — takeda.com (#1) `A`
- ✅ **0.5856** [on_target=0.96 evidence=0.61] Innovent to Present New Clinical Data of Next-gen IO and ... — prnewswire.com (#3) `A`
- ✅ **0.5826** [on_target=0.95 evidence=0.61] Press Release — en.innoventbio.com (#5) `A`
- ✅ **0.5716** [on_target=0.98 evidence=0.58] IBI3001 / Innovent Biologics, Takeda, Fortvita ... — delta.larvol.com (#4) `A`
- ❌ max_keep **0.5515** [on_target=0.94 evidence=0.59] 信達生物將在2026年歐洲腫瘤內科學會（ESMO）年會上展示 ... — news.futunn.com (#10) `A`
- ❌ max_keep **0.483** [on_target=0.90 evidence=0.54] 信達生物製藥 INNOVENT BIOLOGICS, INC. - hkexnews.hk — www1.hkexnews.hk (#7) `A`
- ❌ max_keep **0.459** [on_target=0.85 evidence=0.54] Innovent Bio (1801.HK): Innovent Bio's 6 innovative drugs have positive TCE data for new medical ins — news.futunn.com (#8) `A`
- ❌ low_evidence **0.3674** [on_target=0.95 evidence=0.39] Takeda's Strategic Partnership with Innovent Closes — takeda.com (#9) `A`
- ❌ low_on_target **0.0002** [on_target=0.02 evidence=0.01] Innovent — en.innoventbio.com (#6)

**q019-3** `IBI3001 HNSCC first-line standard of care comparison` → kept 4/10, jev 317 ms

- ✅ **0.6624** [on_target=0.96 evidence=0.69] Press Release — en.innoventbio.com (#7) `A`
- ✅ **0.6144** [on_target=0.96 evidence=0.64] Takeda Announces Oncology Partnership with Innovent — takeda.com (#9) `A`
- ✅ **0.6046** [on_target=0.97 evidence=0.62] Abstract LB055: IBI3001: A potentially first-in-class site- ... — ablesci.com (#5) `A`
- ✅ **0.5921** [on_target=0.95 evidence=0.62] Innovent to Present New Clinical Data of Next-gen IO and ... — prnewswire.com (#10) `A`
- ❌ low_evidence **0.4256** [on_target=0.96 evidence=0.44] IBI3001 / Innovent Biologics, Takeda, Fortvita ... — delta.larvol.com (#4) `A`
- ❌ low_on_target **0.0224** [on_target=0.08 evidence=0.28] Pembrolizumab in the first-line treatment of advanced head and ... — pubmed.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0217** [on_target=0.07 evidence=0.31] The Society for Immunotherapy of Cancer consensus statement on ... — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0155** [on_target=0.05 evidence=0.31] The Society for Immunotherapy of Cancer consensus statement on immunotherapy for the treatment of sq — jitc.bmj.com (#2)
- ❌ low_on_target **0.0147** [on_target=0.05 evidence=0.29] Review of Current and Future Medical Treatments in Head and Neck Squamous Cell Carcinoma — mdpi.com (#8)
- ❌ low_on_target **0.0123** [on_target=0.04 evidence=0.31] Head and Neck Squamous Cell Carcinoma — pro.boehringer-ingelheim.com (#1)

**q019-1** `IBI-3001 HNSCC investor presentation treatment advantage` → kept 4/10, jev 382 ms

- ✅ **0.7275** [on_target=0.97 evidence=0.75] Ozmosi / IBI-3001 Drug Profile — pryzm.ozmosi.com (#1) `A`
- ✅ **0.6272** [on_target=0.98 evidence=0.64] Therapy Detail — ckb.genomenon.com (#4) `A`
- ✅ **0.6014** [on_target=0.97 evidence=0.62] IBI3001 : Drug Detail - Cancer Knowledgebase (CKB) - CKB CORE — ckb.genomenon.com (#9) `A`
- ✅ **0.5194** [on_target=0.95 evidence=0.55] IBI-3001(IBI-3001) - 药物靶点：CD276 x EGFR_在研适应症：局部晚期恶性实体瘤_专利_临床_研发 — synapse.zhihuiya.com (#3) `A`
- ❌ low_evidence **0.4211** [on_target=0.95 evidence=0.44] IBI-3001 - Drug Targets, Indications, Patents — synapse.patsnap.com (#5) `A`
- ❌ low_on_target **0.035** [on_target=0.50 evidence=0.07] [PDF] 信息披露 — paper.cnstock.com (#8)
- ❌ low_on_target **0.0184** [on_target=0.07 evidence=0.26] P123706_Inhibrx Presentation_May 2026 Public Website — inhibrx.com (#6)
- ❌ low_on_target **0.0002** [on_target=0.06 evidence=0.00] Project Details - International Cancer Research Partnership — prod.icrpartnership.org (#10)
- ❌ low_on_target **0.0** [on_target=0.06 evidence=0.00] Error 403 - This web app is stopped. — investor.innoventbio.com (#2)
- ❌ low_on_target **0.0** [on_target=0.24 evidence=0.00] File Unavailable — sec.gov (#7)

## q020 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as JTO2, including Monoclonal Antibody and CXCL10 therapies  
**Target sent:** drugs competing with JTO2: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['JTO2']

**q020-1** `JTO2 CXCL10 inflammatory bowel disease competitors` → kept 4/10, jev 339 ms

- ✅ **0.632** [on_target=0.80 evidence=0.79] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#1)
- ✅ **0.5946** [on_target=0.80 evidence=0.74] Are All Janus Kinase Inhibitors for Inflammatory Bowel Disease the ... — gastroenterologyandhepatology.net (#5)
- ✅ **0.5549** [on_target=0.82 evidence=0.68] Anti‐Inflammatory Peptides as Promising Therapeutics ... — onlinelibrary.wiley.com (#2)
- ✅ **0.5544** [on_target=0.84 evidence=0.66] Anti-IP-10 antibody (BMS-936557) for ulcerative colitis - PMC - NIH — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.3968** [on_target=0.62 evidence=0.64] Inflammatory bowel disease — biospace.com (#9)
- ❌ low_on_target **0.3658** [on_target=0.62 evidence=0.59] Inflammatory Bowel Disease (IBD) / Competitive Intelligence — datamintelligence.com (#7)
- ❌ low_on_target **0.3024** [on_target=0.54 evidence=0.56] Inflammatory Bowel Disease Treatment Market Size, Drugs — delveinsight.com (#10)
- ❌ low_on_target **0.2898** [on_target=0.53 evidence=0.55] Landscape of new drugs and targets in inflammatory bowel disease — onlinelibrary.wiley.com (#4)
- ❌ low_on_target **0.0654** [on_target=0.18 evidence=0.36] Enhanced expression of CXCL10 in inflammatory bowel ... — pubmed.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0416** [on_target=0.13 evidence=0.32] CXCL10 as a shared specific marker in rheumatoid arthritis and inflammatory bowel disease and a clue — nature.com (#3)

**q020-3** `JTO2 CXCL10 clinical trial inflammatory bowel disease` → kept 2/10, jev 429 ms

- ✅ **0.6525** [on_target=0.87 evidence=0.75] Cell Trafficking Interference in Inflammatory Bowel Disease — pmc.ncbi.nlm.nih.gov (#1)
- ✅ **0.585** [on_target=0.78 evidence=0.75] Interfering with the IFN-γ/CXCL10 pathway to develop new targeted ... — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.1987** [on_target=0.40 evidence=0.50] Table 2. — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.1911** [on_target=0.39 evidence=0.49] Landscape of new drugs and targets in inflammatory bowel disease — onlinelibrary.wiley.com (#5)
- ❌ low_on_target **0.0858** [on_target=0.25 evidence=0.34] Chemokines and Chemokine Receptors as Therapeutic Targets in Inflammatory Bowel Disease; Pitfalls an — ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.042** [on_target=0.15 evidence=0.28] Evolution of Eligibility Criteria in Inflammatory Bowel Disease ... — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0128** [on_target=0.06 evidence=0.21] IBD Clinical Trials and Studies — sanofi.com (#10)
- ❌ low_on_target **0.0054** [on_target=0.07 evidence=0.08] UCSF Inflammatory Bowel Disease Clinical Trials for 2026 ... — clinicaltrials.ucsf.edu (#2)
- ❌ low_on_target **0.0012** [on_target=0.05 evidence=0.02] Clinical Trials / Jill Roberts Center for Inflammatory Bowel ... — jillrobertsibdcenter.weillcornell.org (#3)
- ❌ low_on_target **0.0003** [on_target=0.05 evidence=0.01] Clinical Trials - Inflammatory Bowel Disease Center - WashU — ibd.wustl.edu (#4)

**q020-2** `JTO2 anti-CXCL10 monoclonal antibody IBD pipeline` → kept 4/10, jev 363 ms

- ✅ **0.644** [on_target=0.84 evidence=0.77] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#9)
- ✅ **0.6437** [on_target=0.89 evidence=0.72] Targeting Immune Cell Trafficking – Insights From Research Models ... — pmc.ncbi.nlm.nih.gov (#4)
- ✅ **0.5742** [on_target=0.87 evidence=0.66] The IBD Therapeutic Pipeline is Primed to Produce — practicalgastro.com (#10)
- ✅ **0.574** [on_target=0.84 evidence=0.68] Chemokines and Chemokine Receptors as Therapeutic Targets in ... — bohrium.com (#7)
- ❌ low_on_target **0.34** [on_target=0.51 evidence=0.67] Optimising Monoclonal Antibody Therapies for Inflammatory Bowel ... — dovepress.com (#6)
- ❌ low_on_target **0.2346** [on_target=0.69 evidence=0.34] Product Pipeline Summary — jyanttech.com (#2)
- ❌ low_on_target **0.0296** [on_target=0.24 evidence=0.12] Exploring the Pipeline of Novel Therapies for Inflammatory ... — mdpi.com (#3)
- ❌ low_on_target **0.0096** [on_target=0.16 evidence=0.06] Biological agents as attractive targets for inflammatory bowel ... — sciencedirect.com (#8)
- ❌ low_on_target **0.0003** [on_target=0.09 evidence=0.00] Study Details Page — abbvieclinicaltrials.com (#5)
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] Cloudflare — thelancet.com (#1)

## q021 (competitor objective)

**Objective:** Crohn's Disease Ulcerative Colitis competing agents with the same mechanistic class as S1PR S1PR1 Sphingosine-1-phosphate receptor, including Small Molecule  
**Target sent:** drugs competing with Mocravimod: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['Mocravimod']

**q021-3** `Mocravimod etrasimod ozanimod head-to-head IBD` → kept 5/10, jev 372 ms

- ✅ **0.8021** [on_target=0.94 evidence=0.85] Immunity in digestive diseases: new drugs for inflammatory bowel ... — pmc.ncbi.nlm.nih.gov (#7)
- ✅ **0.7792** [on_target=0.97 evidence=0.80] Safety and efficacy of S1P receptor modulators for the ... - PMC — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.7426** [on_target=0.94 evidence=0.79] Pharmacological Therapy in Inflammatory Bowel Diseases - PMC — pmc.ncbi.nlm.nih.gov (#10)
- ✅ **0.7081** [on_target=0.97 evidence=0.73] Efficacy and safety of sphingosine-1-phosphate receptor ... — pmc.ncbi.nlm.nih.gov (#3) `A`
- ✅ **0.6925** [on_target=0.94 evidence=0.74] Medications for Inflammatory Bowel Disease — merckmanuals.com (#4)
- ❌ max_keep **0.672** [on_target=0.96 evidence=0.70] An Overview of the Efficacy and Safety of Ozanimod for ... - PMC - NIH — pmc.ncbi.nlm.nih.gov (#6) `A`
- ❌ max_keep **0.6545** [on_target=0.85 evidence=0.77] Matching-adjusted indirect comparisons of efficacy ... — becarispublishing.com (#9)
- ❌ max_keep **0.6379** [on_target=0.89 evidence=0.72] Efficacy and Safety of Advanced Oral Small Molecules for Inflammatory Bowel Disease: Systematic Revi — academic.oup.com (#1)
- ❌ max_keep **0.6054** [on_target=0.80 evidence=0.76] Matching-adjusted indirect comparisons of efficacy outcomes ... — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.2932** [on_target=0.53 evidence=0.55] Comparative Efficacy of Advanced Therapies for Management of ... — pmc.ncbi.nlm.nih.gov (#8)

**q021-4** `Mocravimod IBD partnering in-licensing` → kept 1/10, jev 347 ms

- ✅ **0.4112** [on_target=0.73 evidence=0.56] Mocravimod - Inxight Drugs — drugs.ncats.io (#4) `A`
- ❌ low_evidence **0.2823** [on_target=0.73 evidence=0.39] Mocravimod, a Selective Sphingosine-1-Phosphate Receptor ... — pubmed.ncbi.nlm.nih.gov (#9) `A`
- ❌ low_on_target **0.1708** [on_target=0.47 evidence=0.36] Mocravimod / Oncology / Drug Developments / Pipeline Prospector — pharmacompass.com (#6) `A`
- ❌ low_on_target **0.1653** [on_target=0.67 evidence=0.25] Press Release — priothera.com (#7) `A`
- ❌ low_on_target **0.0916** [on_target=0.67 evidence=0.14] Priothera / Improving patient's lives by delivering an innovative ... — priothera.com (#8) `A`
- ❌ low_on_target **0.0352** [on_target=0.66 evidence=0.05] Priothera Appoints Experienced Biotech Executive, Dr ... — biospace.com (#2) `A`
- ❌ low_on_target **0.01** [on_target=0.06 evidence=0.17] CP Scorecard / Largest Pharma & Biotech Deals Since 2017 — currentpartnering.com (#1)
- ❌ low_on_target **0.0011** [on_target=0.03 evidence=0.04] Biotech BD&L Tracker 2026: 150 Licensing & Partnering ... — biobucks.co (#3)
- ❌ low_on_target **0.0003** [on_target=0.04 evidence=0.01] Priothera / The Pharmaletter — thepharmaletter.com (#10)
- ❌ low_on_target **0.0** [on_target=0.02 evidence=0.00] Current Partnering: Life science deals, alliances and M&A — currentpartnering.com (#5)

**q021-5** `Mocravimod ClinicalTrials.gov Crohn's ulcerative colitis` → kept 3/10, jev 336 ms

- ✅ **0.6023** [on_target=0.89 evidence=0.68] Targeting the Sphingosine-1-Phosphate Pathway - PMC - NIH — pmc.ncbi.nlm.nih.gov (#10) `A`
- ✅ **0.45** [on_target=0.75 evidence=0.60] Mocravimod - Inxight Drugs — drugs.ncats.io (#1) `A`
- ✅ **0.4008** [on_target=0.72 evidence=0.56] Mocravimod Hydrochloride - Inxight Drugs — drugs.ncats.io (#2) `A`
- ❌ low_on_target **0.2305** [on_target=0.52 evidence=0.44] A clinical trial for people with moderately to severely active ... — trials.lilly.com (#8)
- ❌ low_on_target **0.1518** [on_target=0.66 evidence=0.23] Mocravimod — pubchem.ncbi.nlm.nih.gov (#5) `A`
- ❌ low_on_target **0.119** [on_target=0.30 evidence=0.40] NCT07483073 / A Master Protocol (IIBD): A Study of Multiple Drugs ... — clinicaltrials.gov (#9)
- ❌ low_on_target **0.102** [on_target=0.68 evidence=0.15] Mocravimod — pubchem.ncbi.nlm.nih.gov (#6) `A`
- ❌ low_on_target **0.0528** [on_target=0.22 evidence=0.24] Official Title of Study — cdn.clinicaltrials.gov (#4)
- ❌ low_on_target **0.02** [on_target=0.20 evidence=0.10] Adjunctive and… · Phase III (2024-512752-38-00) - CTIS.eu — ctis.eu (#3)
- ❌ low_on_target **0.0187** [on_target=0.40 evidence=0.05] Study Details / NCT05429632 / Mocravimod as Adjunctive ... — clinicaltrials.gov (#7) `A`

**q021-2** `Mocravimod Crohn's disease ulcerative colitis S1PR1 agents` → kept 5/10, jev 359 ms

- ✅ **0.9114** [on_target=0.98 evidence=0.93] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#8) `A`
- ✅ **0.8115** [on_target=0.94 evidence=0.86] Emerging therapies for ulcerative colitis - Taylor & Francis — tandfonline.com (#9)
- ✅ **0.7922** [on_target=0.97 evidence=0.82] Targeting Sphingosine-1-Phosphate Signaling in Immune ... — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.7631** [on_target=0.97 evidence=0.79] Targeting the Sphingosine-1-Phosphate Pathway - PMC - NIH — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.7469** [on_target=0.97 evidence=0.77] Unveiling the biological role of sphingosine-1-phosphate ... — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ max_keep **0.7372** [on_target=0.97 evidence=0.76] Efficacy and safety of sphingosine-1-phosphate receptor ... — pmc.ncbi.nlm.nih.gov (#2) `A`
- ❌ max_keep **0.7113** [on_target=0.97 evidence=0.73] Safety and efficacy of S1P receptor modulators for the ... - PMC — pmc.ncbi.nlm.nih.gov (#3) `A`
- ❌ max_keep **0.4836** [on_target=0.78 evidence=0.62] NCATS Inxight Drugs — Mocravimod Hydrochloride — drugs.ncats.io (#7) `A`
- ❌ max_keep **0.4491** [on_target=0.77 evidence=0.58] Mocravimod Hydrochloride - Inxight Drugs — drugs.ncats.io (#4) `A`
- ❌ low_evidence **0.3146** [on_target=0.78 evidence=0.40] Mocravimod — go.drugbank.com (#6) `A`

**q021-1** `Mocravimod IBD S1PR competitors licensing status` → kept 5/10, jev 326 ms

- ✅ **0.918** [on_target=0.98 evidence=0.94] Ulcerative Colitis (UC) — Global Competitive Landscape Report 2026 — eureka.patsnap.com (#2) `A`
- ✅ **0.918** [on_target=0.98 evidence=0.94] Understanding the molecular mechanisms of anti-trafficking ... — pmc.ncbi.nlm.nih.gov (#9) `A`
- ✅ **0.8956** [on_target=0.97 evidence=0.92] Table 1. — pmc.ncbi.nlm.nih.gov (#4) `A`
- ✅ **0.8384** [on_target=0.96 evidence=0.87] S1PR Modulators Market Outlook, Forecast, Insights 2034 — delveinsight.com (#1) `A`
- ✅ **0.819** [on_target=0.90 evidence=0.91] Sphingosine‐1‐Phosphate Receptor Modulators for the Treatment ... — onlinelibrary.wiley.com (#5)
- ❌ max_keep **0.8158** [on_target=0.92 evidence=0.89] Inflammatory Bowel Competitive Landscape Analysis 2026 / Eureka — eureka.patsnap.com (#10)
- ❌ max_keep **0.804** [on_target=0.90 evidence=0.89] Sphingosine-1-Phosphate (S1P) Receptor Modulators for the ... - PMC — pmc.ncbi.nlm.nih.gov (#3)
- ❌ max_keep **0.6784** [on_target=0.96 evidence=0.71] Targeting Sphingosine-1-Phosphate Signaling in Immune-Mediated Diseases: Beyond Multiple Sclerosis — springermedizin.de (#8) `A`
- ❌ max_keep **0.6658** [on_target=0.85 evidence=0.78] Positioning Sphingosine-1 Phosphate Receptor Modulators in ... — gastroenterologyandhepatology.net (#6)
- ❌ low_evidence **0.3486** [on_target=0.83 evidence=0.42] Adjunctive and… · Phase III (2024-512752-38-00) - CTIS.eu — ctis.eu (#7) `A`

## q022 (competitor objective)

**Objective:** competing agents in the same mechanistic class for this indication Novel UC Treatment, Cosmo Health, Distal Ulcerative Colitis  
**Target sent:** drugs competing with Novel UC Treatment: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['Novel UC Treatment']

**q022-1** `Novel UC Treatment mechanism of action ulcerative colitis` → kept 5/10, jev 393 ms

- ✅ **0.5925** [on_target=0.88 evidence=0.67] Ulcerative Colitis: Today, Tomorrow, and the Future — emjreviews.com (#6)
- ✅ **0.551** [on_target=0.87 evidence=0.63] Emerging Therapies for Ulcerative Colitis: Updates from Recent ... — pmc.ncbi.nlm.nih.gov (#5)
- ✅ **0.522** [on_target=0.90 evidence=0.58] Pathological mechanism and targeted drugs of ulcerative colitis — pmc.ncbi.nlm.nih.gov (#4)
- ✅ **0.5157** [on_target=0.91 evidence=0.57] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#3)
- ✅ **0.5044** [on_target=0.89 evidence=0.57] Current Pharmacologic Options and Emerging Therapeutic ... - PMC — pmc.ncbi.nlm.nih.gov (#8)
- ❌ max_keep **0.4644** [on_target=0.86 evidence=0.54] [PDF] Advances in the Treatment of Ulcerative Colitis—From Conventional ... — pdfs.semanticscholar.org (#9)
- ❌ max_keep **0.4547** [on_target=0.88 evidence=0.52] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#1)
- ❌ max_keep **0.4533** [on_target=0.85 evidence=0.53] Emerging Therapies in Inflammatory Bowel Disease - PMC - NIH — pmc.ncbi.nlm.nih.gov (#10)
- ❌ max_keep **0.4401** [on_target=0.82 evidence=0.54] Practical guidance for managing patients with moderate-to-severe ... — academic.oup.com (#2)
- ❌ max_keep **0.4319** [on_target=0.82 evidence=0.53] Advances in the Treatment of Ulcerative Colitis—From Conventional ... — pmc.ncbi.nlm.nih.gov (#7)

**q022-2** `Novel UC Treatment target mechanistic class UC` → kept 5/10, jev 384 ms

- ✅ **0.6688** [on_target=0.88 evidence=0.76] [PDF] New targets in inflammatory bowel disease therapy: 2021 - BINASSS — binasss.sa.cr (#2)
- ✅ **0.625** [on_target=0.86 evidence=0.73] Emerging Therapies for Ulcerative Colitis: Updates from Recent ... — pmc.ncbi.nlm.nih.gov (#9)
- ✅ **0.5045** [on_target=0.88 evidence=0.57] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#4)
- ✅ **0.4987** [on_target=0.88 evidence=0.57] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#5)
- ✅ **0.4731** [on_target=0.83 evidence=0.57] Oral Small-Molecule Therapies Versus Biologic Agents ... - PMC — pmc.ncbi.nlm.nih.gov (#8)
- ❌ max_keep **0.4672** [on_target=0.86 evidence=0.54] Raising the bar in ulcerative colitis management - Fabrizio Fanizzi, Mariangela Allocca, Gionata Fio — journals.sagepub.com (#6)
- ❌ max_keep **0.4368** [on_target=0.84 evidence=0.52] Current Pharmacologic Options and Emerging Therapeutic ... - PMC — pmc.ncbi.nlm.nih.gov (#10)
- ❌ max_keep **0.4209** [on_target=0.82 evidence=0.51] Pathological mechanism and targeted drugs of ulcerative colitis - PMC — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_evidence **0.366** [on_target=0.79 evidence=0.46] pmc.ncbi.nlm.nih.gov › articles › PMC12420776Ulcerative Colitis: Advances in Pathogenesis, Biomarker — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.2794** [on_target=0.66 evidence=0.42] Practical guidance for managing patients with moderate-to-severe ... — pmc.ncbi.nlm.nih.gov (#7)

**q022-3** `Novel UC Treatment Phase 2 competitor landscape ulcerative colitis` → kept 5/10, jev 406 ms

- ✅ **0.646** [on_target=0.85 evidence=0.76] Emerging Therapies for Ulcerative Colitis: Updates from Recent ... — pmc.ncbi.nlm.nih.gov (#10)
- ✅ **0.56** [on_target=0.80 evidence=0.70] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#2)
- ✅ **0.5553** [on_target=0.85 evidence=0.65] Inflammatory Bowel Competitive Landscape Analysis 2026 / Eureka — eureka.patsnap.com (#4)
- ✅ **0.534** [on_target=0.90 evidence=0.59] Ulcerative Colitis Drug Market Outlook: Advanced ... — researchandmarkets.com (#6)
- ✅ **0.5236** [on_target=0.84 evidence=0.62] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#1)
- ❌ max_keep **0.4586** [on_target=0.80 evidence=0.57] Ulcerative Colitis / Disease Landscape & Forecast / G7 / 2024 — clarivate.com (#3)
- ❌ low_on_target **0.4158** [on_target=0.66 evidence=0.63] Ulcerative Colitis Market Size, Trends, Share & Growth Drivers 2031 — mordorintelligence.com (#9)
- ❌ low_evidence **0.3984** [on_target=0.83 evidence=0.48] Ulcerative Colitis Report — evaluate.com (#7)
- ❌ max_keep **0.3943** [on_target=0.70 evidence=0.56] Ulcerative Colitis Pipeline: 75+ Therapies & Key Companies — delveinsight.com (#8)
- ❌ low_on_target **0.388** [on_target=0.60 evidence=0.65] Ulcerative Colitis Treatment Market Size, Drugs, Companies — delveinsight.com (#5)

## q023 (competitor objective)

**Objective:** Inflammatory Bowel Diseases Mild-to-moderate ulcerative colitis Ulcerative Colitis competing agents with the same mechanistic class as Gut Microbiome Dysbiosis, including Live Biotherapeutic Product  
**Target sent:** drugs competing with VE202 / MB310 / SER-287 / EXL01: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['VE202', 'MB310', 'SER-287', 'EXL01']

**q023-2** `MB310 Phase 2 Microbiotica licensing` → kept 4/10, jev 355 ms

- ✅ **0.4788** [on_target=0.86 evidence=0.56] Pipeline - Microbiotica — microbiotica.com (#3) `A`
- ✅ **0.4628** [on_target=0.89 evidence=0.52] Microbiotica Ltd. - Drug pipelines, Patents, Clinical trials — synapse.patsnap.com (#2) `A`
- ✅ **0.4618** [on_target=0.85 evidence=0.54] Microbiotica Announces Impressive Results in its Phase 1b Trial of MB310 in Ulcerative Colitis — globenewswire.com (#10) `A`
- ✅ **0.4505** [on_target=0.85 evidence=0.53] Press Release — flerie.com (#5) `A`
- ❌ low_evidence **0.4014** [on_target=0.86 evidence=0.47] Press releases — microbiotica.com (#6) `A`
- ❌ low_evidence **0.3828** [on_target=0.87 evidence=0.44] Microbiotica – Precision Microbiome Medicines — microbiotica.com (#4) `A`
- ❌ low_evidence **0.3784** [on_target=0.86 evidence=0.44] Member profile: Microbiotica - BioIndustry Association / BIA — bioindustry.org (#9) `A`
- ❌ low_evidence **0.3756** [on_target=0.86 evidence=0.44] Partnering — microbiotica.com (#1) `A`
- ❌ low_evidence **0.3756** [on_target=0.86 evidence=0.44] Policy and Regulations - M2 Pharma — m2pharma.com (#7) `A`
- ❌ low_evidence **0.3173** [on_target=0.85 evidence=0.37] About - Microbiotica — microbiotica.com (#8) `A`

**q023-4** `EXL01 ReMind Phase 2 licensing Crohn's disease` → kept 1/10, jev 350 ms

- ✅ **0.3905** [on_target=0.71 evidence=0.55] Exeliom Biosciences: a new generation of microbiota-derived ... — universite-paris-saclay.fr (#8) `A`
- ❌ low_evidence **0.3814** [on_target=0.80 evidence=0.48] MAINTAIN POP submitted to ANSM - Exeliom Biosciences — exeliombio.com (#5) `A`
- ❌ low_on_target **0.345** [on_target=0.69 evidence=0.50] La Gazette du LABORATOIRE AFRIQUE — gazettelabo.fr (#6) `A`
- ❌ low_evidence **0.3325** [on_target=0.75 evidence=0.44] News - Exeliom Biosciences — exeliombio.com (#10) `A`
- ❌ low_on_target **0.3099** [on_target=0.65 evidence=0.48] Delving into the Latest Updates on EXL-01 with Synapse — synapse.patsnap.com (#1) `A`
- ❌ low_on_target **0.3058** [on_target=0.62 evidence=0.49] Exeliom Biosciences' Post - LinkedIn — linkedin.com (#7) `A`
- ❌ low_on_target **0.2852** [on_target=0.69 evidence=0.41] Exeliom Biosciences collaborates with REMIND in ... — exeliombio.com (#2) `A`
- ❌ low_on_target **0.2751** [on_target=0.65 evidence=0.42] Exeliom Biosciences collabore avec REMIND sur l’essai — ala.associates (#3) `A`
- ❌ low_on_target **0.2405** [on_target=0.65 evidence=0.37] News - exeliom — exeliombio.com (#4) `A`
- ❌ low_on_target **0.1116** [on_target=0.50 evidence=0.22] The BIG Phase 2 study (Gastric Cancer is moving forward! — exeliombio.com (#9) `A`

**q023-3** `SER-287 ulcerative colitis development status licensing` → kept 5/10, jev 382 ms

- ✅ **0.595** [on_target=0.92 evidence=0.65] [PDF] Seres Therapeutics Reports Second Quarter 2021 Financial Results ... — ir.serestherapeutics.com (#5) `A`
- ✅ **0.5885** [on_target=0.91 evidence=0.65] EX-99.1 — sec.gov (#3) `A`
- ✅ **0.5814** [on_target=0.89 evidence=0.65] SER-287 Drug Asset Due Diligence Report 2026 — synapse.patsnap.com (#2) `A`
- ✅ **0.5488** [on_target=0.84 evidence=0.65] Presentation Title Here — ir.serestherapeutics.com (#7) `A`
- ✅ **0.5398** [on_target=0.92 evidence=0.59] EX-99.1 - SEC.gov — sec.gov (#9) `A`
- ❌ max_keep **0.5368** [on_target=0.83 evidence=0.65] SER-301 / Seres Therap, Nestle — delta.larvol.com (#8) `A`
- ❌ max_keep **0.4843** [on_target=0.87 evidence=0.56] SER-287 - Drug Targets, Indications, Patents — synapse.patsnap.com (#1) `A`
- ❌ max_keep **0.484** [on_target=0.88 evidence=0.55] Seres Therapeutics Announces Initiation of SER-287 ... — microbiometimes.com (#6) `A`
- ❌ max_keep **0.4835** [on_target=0.89 evidence=0.54] A Phase 1b Safety Study of SER-287, a Spore-Based ... - PMC — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ low_evidence **0.2875** [on_target=0.88 evidence=0.33] Seres Therapeutics Announces Initiation of SER-287 ... — ir.serestherapeutics.com (#4) `A`

**q023-1** `VE202 Phase 2 current status licensing` → kept 5/10, jev 364 ms

- ✅ **0.5307** [on_target=0.87 evidence=0.61] PureTech Founded Entity Vedanta Biosciences Announces Phase 2 Study of VE202 in Ulcerative Colitis D — finance.yahoo.com (#6) `A`
- ✅ **0.5218** [on_target=0.86 evidence=0.61] Vedanta's Microbiome-Based Candidate Fails to Meet ... — appliedclinicaltrialsonline.com (#8) `A`
- ✅ **0.4947** [on_target=0.82 evidence=0.60] VE-202 - Drug Targets, Indications, Patents — synapse.patsnap.com (#1) `A`
- ✅ **0.4814** [on_target=0.83 evidence=0.58] Vedanta Biosciences Announces Phase 2 Study of VE202 ... — vedantabio.com (#3) `A`
- ✅ **0.4783** [on_target=0.82 evidence=0.58] Vedanta's live bacteria cocktail fails phase 2 colitis trial — fiercebiotech.com (#10) `A`
- ❌ max_keep **0.4732** [on_target=0.85 evidence=0.56] VE202 ( DrugBank: - ) — ddrare.nibn.go.jp (#2) `A`
- ❌ max_keep **0.4702** [on_target=0.86 evidence=0.55] Vedanta Ends UC Program After Phase II Failure, Refocuses Pipeline — igmpi.ac.in (#5) `A`
- ❌ max_keep **0.4509** [on_target=0.81 evidence=0.56] Vedanta's UC Drug Miss Shifts Focus to Fast-Tracked C. Difficile Treatment in Phase 3 — stocktitan.net (#4) `A`
- ❌ max_keep **0.4506** [on_target=0.80 evidence=0.56] Vedanta Biosciences Cuts 20% of Workforce After ... — trial.medpath.com (#9) `A`
- ❌ low_evidence **0.3699** [on_target=0.81 evidence=0.46] controlled, phase 2 study of ve202 in patients — onderzoekmetmensen.nl (#7) `A`

## q024 (competitor objective)

**Objective:** Ulcerative Colitis competing agents in the same mechanistic class as ITGA4 ITGB7 Integrin Alpha-4 Beta-7 Integrin α4β7 Small Molecule therapies  
**Target sent:** drugs competing with emvistegrast: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['emvistegrast']

**q024-1** `emvistegrast α4β7 ulcerative colitis Phase 2 competitors` → kept 5/10, jev 357 ms

- ✅ **0.928** [on_target=0.97 evidence=0.96] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#3) `A`
- ✅ **0.8397** [on_target=0.94 evidence=0.89] Table 1. — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.8352** [on_target=0.96 evidence=0.87] Integrin alpha 4 beta 7 — jp.acrobiosystems.com (#4) `A`
- ✅ **0.8106** [on_target=0.95 evidence=0.85] SPY001 (Ph 2) for Ulcerative Colitis / Spyre Therapeutics, Inc — biopharmawatch.com (#1) `A`
- ✅ **0.779** [on_target=0.95 evidence=0.82] Novel Therapies and Approaches to Inflammatory Bowel Disease (IBD) — mdpi.com (#6)
- ❌ max_keep **0.7125** [on_target=0.95 evidence=0.75] Gilead Diversifies: Emvistegrast, Cancer Catalysts & Q2 2026 ... — pienomial.com (#5) `A`
- ❌ max_keep **0.6764** [on_target=0.91 evidence=0.74] emvistegrast Ph 2 for Ulcerative Colitis / BiopharmaWatch — biopharmawatch.com (#8) `A`
- ❌ max_keep **0.6448** [on_target=0.93 evidence=0.69] Gastrointestinal - Drug Hunter — drughunter.com (#7) `A`
- ❌ max_keep **0.5356** [on_target=0.78 evidence=0.69] What drugs are in development for Inflammatory Bowel Diseases? — synapse.patsnap.com (#10)
- ❌ max_keep **0.522** [on_target=0.87 evidence=0.60] New IBD therapies take the 'if factor' out of Crohn's, ulcerative colitis — utswmed.org (#9)

**q024-3** `emvistegrast α4β7 ulcerative colitis licensing` → kept 5/10, jev 321 ms

- ✅ **0.8568** [on_target=0.97 evidence=0.88] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#7) `A`
- ✅ **0.8407** [on_target=0.97 evidence=0.87] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#10) `A`
- ✅ **0.7094** [on_target=0.95 evidence=0.75] Gilead Diversifies: Emvistegrast, Cancer Catalysts & Q2 2026 ... — pienomial.com (#3) `A`
- ✅ **0.5876** [on_target=0.86 evidence=0.68] Table 1. — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.5057** [on_target=0.82 evidence=0.62] emvistegrast (GS-1427) - Drug Hunter — drughunter.com (#9) `A`
- ❌ max_keep **0.4874** [on_target=0.86 evidence=0.57] Emvistegrast - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#1) `A`
- ❌ max_keep **0.4518** [on_target=0.77 evidence=0.59] emvistegrast (GS-1427) / Gilead - LARVOL DELTA — delta.larvol.com (#8) `A`
- ❌ max_keep **0.4345** [on_target=0.79 evidence=0.55] emvistegrast / Ligand page — guidetopharmacology.org (#2) `A`
- ❌ max_keep **0.4256** [on_target=0.84 evidence=0.51] Integrin alpha 4 beta 7 — jp.acrobiosystems.com (#4) `A`
- ❌ max_keep **0.4024** [on_target=0.71 evidence=0.57] emvistegrast Ph 2 for Ulcerative Colitis / BiopharmaWatch — biopharmawatch.com (#6) `A`

**q024-2** `emvistegrast α4β7 ulcerative colitis pipeline Phase 3` → kept 5/10, jev 370 ms

- ✅ **0.9021** [on_target=0.97 evidence=0.93] Table 1. — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.873** [on_target=0.97 evidence=0.90] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.7536** [on_target=0.95 evidence=0.79] Integrin alpha 4 beta 7 — jp.acrobiosystems.com (#3) `A`
- ✅ **0.706** [on_target=0.89 evidence=0.79] IBD therapeutics: what is in the pipeline? — fg.bmj.com (#6)
- ✅ **0.6999** [on_target=0.95 evidence=0.74] Gilead Diversifies: Emvistegrast, Cancer Catalysts & Q2 2026 ... — pienomial.com (#7) `A`
- ❌ max_keep **0.6674** [on_target=0.94 evidence=0.71] Gastrointestinal - Drug Hunter — drughunter.com (#10) `A`
- ❌ max_keep **0.4543** [on_target=0.77 evidence=0.59] a pipeline of novel drugs for UC management — pdfs.semanticscholar.org (#4) `A`
- ❌ max_keep **0.4536** [on_target=0.81 evidence=0.56] emvistegrast / Ligand page — guidetopharmacology.org (#9) `A`
- ❌ max_keep **0.4428** [on_target=0.81 evidence=0.55] UC Davis Inflammatory Bowel Disease Clinical Trials for 2026 — clinicaltrials.ucdavis.edu (#5) `A`
- ❌ low_on_target **0.2744** [on_target=0.56 evidence=0.49] vepdegestrant (ARV-471) - Drug Hunter — drughunter.com (#8) `A`

**q024-4** `emvistegrast integrin alpha-4 beta-7 ulcerative colitis clinical trial` → kept 5/10, jev 372 ms

- ✅ **0.873** [on_target=0.97 evidence=0.90] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#8) `A`
- ✅ **0.5983** [on_target=0.93 evidence=0.64] drug hunter on X: "Gilead's Recently Disclosed, Selective α4β7 ... — x.com (#4) `A`
- ✅ **0.5304** [on_target=0.86 evidence=0.62] Integrin alpha 4 beta 7 분자 정보 - ACROBiosystems — kr.acrobiosystems.com (#3) `A`
- ✅ **0.4766** [on_target=0.79 evidence=0.60] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#10) `A`
- ✅ **0.4732** [on_target=0.85 evidence=0.56] UCSF Inflammatory Bowel Disease Clinical Trials for 2026 ... — clinicaltrials.ucsf.edu (#2) `A`
- ❌ max_keep **0.4446** [on_target=0.78 evidence=0.57] Emvistegrast - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#9) `A`
- ❌ max_keep **0.4345** [on_target=0.79 evidence=0.55] emvistegrast / Ligand page — guidetopharmacology.org (#6) `A`
- ❌ max_keep **0.4187** [on_target=0.79 evidence=0.53] emvistegrast (GS-1427) / Gilead - LARVOL DELTA — delta.larvol.com (#1) `A`
- ❌ low_evidence **0.2391** [on_target=0.71 evidence=0.34] UCSF Ulcerative Colitis Clinical Trials for 2026 — clinicaltrials.ucsf.edu (#5) `A`
- ❌ low_on_target **0.207** [on_target=0.69 evidence=0.30] GS-1427 in Participants With Moderately to Severely Active ... — clinicaltrials.ucsf.edu (#7) `A`

## q025 (competitor objective)

**Objective:** Ulcerative Colitis competing agents with the same mechanism of action as HEMAY007, targeting TNF-α Tumor Necrosis Factor Alpha  
**Target sent:** drugs competing with HEMAY007: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['HEMAY007']

**q025-1** `HEMAY007 ulcerative colitis anti-TNF Phase 2 competitors` → kept 5/10, jev 418 ms

- ✅ **0.9183** [on_target=0.97 evidence=0.95] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#3) `A`
- ✅ **0.8486** [on_target=0.95 evidence=0.89] Current and Emerging Biologics for Ulcerative Colitis - PMC — pmc.ncbi.nlm.nih.gov (#7)
- ✅ **0.8296** [on_target=0.95 evidence=0.87] TNF-alpha - ACROBiosystems — kr.acrobiosystems.com (#1) `A`
- ✅ **0.7564** [on_target=0.93 evidence=0.81] Landscape of new drugs and targets in inflammatory bowel ... — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.726** [on_target=0.90 evidence=0.81] Emerging Therapies for Ulcerative Colitis: Updates from Recent ... — pmc.ncbi.nlm.nih.gov (#8)
- ❌ max_keep **0.6746** [on_target=0.92 evidence=0.73] Advances in the Treatment of Ulcerative Colitis—From Conventional ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.3224** [on_target=0.62 evidence=0.52] This summary aims to give you an overview of the information contained in this — www1.hkexnews.hk (#4) `A`
- ❌ low_on_target **0.1145** [on_target=0.34 evidence=0.34] Comparative Effectiveness of Biologic or Small-Molecule ... — ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0165** [on_target=0.16 evidence=0.10] Table 1. — pmc.ncbi.nlm.nih.gov (#2) `A`
- ❌ low_on_target **0.0105** [on_target=0.07 evidence=0.15] Market Segmentation — coherentmarketinsights.com (#9)

**q025-2** `HEMAY007 ulcerative colitis anti-TNF licensing availability` → kept 1/10, jev 397 ms

- ✅ **0.574** [on_target=0.84 evidence=0.68] TNF-alpha - ACROBiosystems — kr.acrobiosystems.com (#5) `A`
- ❌ low_on_target **0.3206** [on_target=0.65 evidence=0.49] This summary aims to give you an overview of the information contained in this — www1.hkexnews.hk (#10) `A`
- ❌ low_evidence **0.3186** [on_target=0.79 evidence=0.40] Hemay007(Hemay007) - 药物靶点：TNF-α_在研适应症：类风湿关节炎 — synapse.zhihuiya.com (#1) `A`
- ❌ low_evidence **0.3168** [on_target=0.72 evidence=0.44] Hemay007 - Drug Targets, Indications, Patents — synapse.patsnap.com (#3) `A`
- ❌ low_evidence **0.3132** [on_target=0.77 evidence=0.41] Table 1. — pmc.ncbi.nlm.nih.gov (#6) `A`
- ❌ low_on_target **0.3038** [on_target=0.68 evidence=0.45] [PDF] 概覽 — www1.hkexnews.hk (#2) `A`
- ❌ low_on_target **0.2904** [on_target=0.66 evidence=0.44] OVERVIEW — www1.hkexnews.hk (#9) `A`
- ❌ low_on_target **0.2725** [on_target=0.67 evidence=0.41] Hemay Pharmaceutical Pty Ltd - Drug pipelines, Patents, Clinical trials — synapse-patsnap-com.libproxy1.nus.edu.sg (#8) `A`
- ❌ low_on_target **0.2645** [on_target=0.69 evidence=0.38] Hemay007: TNF-alpha, Phase 2 in Ulcerative Colitis — assetmemo.bio (#4) `A`
- ❌ low_on_target **0.2644** [on_target=0.65 evidence=0.41] Xiajiang Hemei Pharmaceutical Co., Ltd. — synapse.patsnap.com (#7) `A`

**q025-3** `HEMAY007 TNF-alpha ulcerative colitis clinical development status` → kept 3/10, jev 347 ms

- ✅ **0.8011** [on_target=0.95 evidence=0.84] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#9) `A`
- ✅ **0.7708** [on_target=0.94 evidence=0.82] Table 1. — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.6624** [on_target=0.92 evidence=0.72] a pipeline of novel drugs for UC management — pdfs.semanticscholar.org (#7) `A`
- ❌ low_evidence **0.3528** [on_target=0.72 evidence=0.49] Pipeline Includes Seven Small Molecule Drug Candidates — news.futunn.com (#4) `A`
- ❌ low_on_target **0.3371** [on_target=0.64 evidence=0.53] This summary aims to give you an overview of the information contained in this — www1.hkexnews.hk (#5) `A`
- ❌ low_on_target **0.3015** [on_target=0.67 evidence=0.45] [PDF] 概覽 — www1.hkexnews.hk (#3) `A`
- ❌ low_on_target **0.3013** [on_target=0.69 evidence=0.44] Xiajiang Hemei Pharmaceutical Co., Ltd. — synapse.patsnap.com (#10) `A`
- ❌ low_evidence **0.2824** [on_target=0.77 evidence=0.37] Hemay007(Hemay007) - 药物靶点：TNF-α_在研适应症：类风湿关节炎 — synapse.zhihuiya.com (#2) `A`
- ❌ low_on_target **0.1829** [on_target=0.59 evidence=0.31] Hemay-007 / MedPath — trial.medpath.com (#8) `A`
- ❌ low_on_target **0.1586** [on_target=0.61 evidence=0.26] Hemay007 - Drug Targets, Indications, Patents — synapse.patsnap.com (#6) `A`

**q025-4** `HEMAY007 ulcerative colitis anti-TNF biosimilar landscape` → kept 5/10, jev 340 ms

- ✅ **0.8122** [on_target=0.93 evidence=0.87] Anti-TNFα in inflammatory bowel disease: from originators to ... — pmc.ncbi.nlm.nih.gov (#10)
- ✅ **0.7735** [on_target=0.91 evidence=0.85] Role of biologics and biosimilars in inflammatory bowel disease — pmc.ncbi.nlm.nih.gov (#8)
- ✅ **0.7583** [on_target=0.94 evidence=0.81] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#2) `A`
- ✅ **0.639** [on_target=0.90 evidence=0.71] Accelerating Earlier Access to Anti-TNF- Agents with Biosimilar Medicines in the Management of Infla — pdfs.semanticscholar.org (#3)
- ✅ **0.615** [on_target=0.82 evidence=0.75] Clinical Guide to Navigating the Landscape of Biosimilars for ... - PMC — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.3466** [on_target=0.65 evidence=0.53] Biosimilars in inflammatory bowel disease: Beyond evidence ... — wjgnet.com (#9)
- ❌ low_on_target **0.3164** [on_target=0.65 evidence=0.49] TNF-Alpha Proteins, Antibodies & ELISA Kits — acrobiosystems.com (#5) `A`
- ❌ low_evidence **0.3075** [on_target=0.75 evidence=0.41] Table 1. — pmc.ncbi.nlm.nih.gov (#1) `A`
- ❌ low_evidence **0.2832** [on_target=0.72 evidence=0.39] BUSINESS — www1.hkexnews.hk (#6) `A`
- ❌ low_on_target **0.2706** [on_target=0.66 evidence=0.41] OVERVIEW — www1.hkexnews.hk (#4) `A`

## q026

**Objective:** BM-013 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** BM-013 · anchors ['BM-013']

**q026-2** `BM-013 BIMINI Biotech approval AML` → kept 2/10, jev 366 ms

- ✅ **0.5056** [on_target=0.96 evidence=0.53] Portfolio - BIMINI Biotech — biminibiotech.nl (#1) `A`
- ✅ **0.465** [on_target=0.93 evidence=0.50] Bimini Biotech company information, funding & investors — app.dealroom.co (#8) `A`
- ❌ low_on_target **0.1846** [on_target=0.26 evidence=0.71] biminibiotech.nlBIMINI Biotech — biminibiotech.nl (#5)
- ❌ low_on_target **0.0901** [on_target=0.16 evidence=0.56] BIMINI Biotech — biobase.whitefordresearch.com (#6)
- ❌ low_on_target **0.0384** [on_target=0.18 evidence=0.21] Achievements — biminibiotech.nl (#10)
- ❌ low_on_target **0.0312** [on_target=0.11 evidence=0.28] News – BIMINI Biotech — biminibiotech.nl (#2)
- ❌ low_on_target **0.0049** [on_target=0.04 evidence=0.12] Home / AML Hub — aml-hub.com (#9)
- ❌ low_on_target **0.0012** [on_target=0.36 evidence=0.00] Bimini Biotech B.V. - Drug pipelines, Patents, Clinical trials - Synapse — synapse.patsnap.com (#3)
- ❌ low_on_target **0.0** [on_target=0.02 evidence=0.00] NEWS — biminibiotech.nl (#4)
- ❌ low_on_target **0.0** [on_target=0.06 evidence=0.00] Bimini Biotech / Longevity Solutions — bimini-biotech.com (#7)

**q026-3** `BM-013 WASP AML clinical development forecast` → kept 2/10, jev 380 ms

- ✅ **0.736** [on_target=0.96 evidence=0.77] Portfolio - BIMINI Biotech — biminibiotech.nl (#1) `A`
- ✅ **0.653** [on_target=0.83 evidence=0.79] Targeting multiple signaling pathways: the new approach to acute myeloid leukemia therapy — nature.com (#3)
- ❌ low_on_target **0.078** [on_target=0.13 evidence=0.60] BIMINI Biotech — biobase.whitefordresearch.com (#9)
- ❌ low_on_target **0.0578** [on_target=0.17 evidence=0.34] Acute Myeloid Leukemia: 2025 Update on Diagnosis, Risk-Stratification, and Management — onlinelibrary.wiley.com (#6)
- ❌ low_on_target **0.0511** [on_target=0.13 evidence=0.39] Frontiers / From monoclonals to bispecific T cell engagers: the evolving antibody-based therapy land — frontiersin.org (#5)
- ❌ low_on_target **0.0448** [on_target=0.12 evidence=0.37] Location First: Targeting Acute Myeloid Leukemia Within Its Niche — ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0414** [on_target=0.11 evidence=0.38] Decoding Leukemic Stem Cells in AML: From Identification to ... — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0189** [on_target=0.27 evidence=0.07] CLINICAL TRIALS — amgentrials.com (#2)
- ❌ low_on_target **0.0135** [on_target=0.07 evidence=0.19] VU Research Portal — research.vu.nl (#7)
- ❌ low_on_target **0.0083** [on_target=0.03 evidence=0.28] Acute myeloid leukemia (AML) — onkopedia.com (#4)

**q026-1** `BM-013 acute myeloid leukemia regulatory approval launch` → ABSTAIN, jev 479 ms

- ❌ low_on_target **0.3774** [on_target=0.51 evidence=0.74] Modelling acute myeloid leukemia (AML): What’s new? A transition from the classical to the modern — link.springer.com (#3)
- ❌ low_on_target **0.3668** [on_target=0.42 evidence=0.87] Acute Myeloid Leukemia: 2025 Update on Diagnosis, Risk ... — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.202** [on_target=0.29 evidence=0.70] Acute Myeloid Leukemia Market Summary — delveinsight.com (#7)
- ❌ low_on_target **0.148** [on_target=0.23 evidence=0.64] Acute Myeloid Leukaemia - Drug Discovery World (DDW) — ddw-online.com (#2)
- ❌ low_on_target **0.1336** [on_target=0.24 evidence=0.56] Oncology (Cancer)/Hematologic Malignancies Approval ... — fda.gov (#1)
- ❌ low_on_target **0.084** [on_target=0.28 evidence=0.30] Pharmaceutical research and development pipeline — bms.com (#4)
- ❌ low_on_target **0.0735** [on_target=0.15 evidence=0.49] acute myeloid leukaemia / pharmaphorum — pharmaphorum.com (#10)
- ❌ low_on_target **0.0602** [on_target=0.14 evidence=0.43] Frontiers / From monoclonals to bispecific T cell engagers: the evolving antibody-based therapy land — frontiersin.org (#8)
- ❌ low_on_target **0.0226** [on_target=0.07 evidence=0.32] Leukemia — ascopost.com (#6)
- ❌ low_on_target **0.0** [on_target=0.13 evidence=0.00] Pharmaceutical press releases & news — bms.com (#5)

## q027

**Objective:** HQL-79 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** HQL-79 · anchors ['HQL-79']

**q027-2** `HQL-79 monotherapy PDAC xenograft` → kept 3/10, jev 420 ms

- ✅ **0.7243** [on_target=0.97 evidence=0.75] Figure 7. — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.592** [on_target=0.83 evidence=0.71] An efficient drug delivery system to block pancreatic cancer — pubmed.ncbi.nlm.nih.gov (#1)
- ✅ **0.4687** [on_target=0.76 evidence=0.62] untitled — gut.bmj.com (#9)
- ❌ low_evidence **0.2724** [on_target=0.95 evidence=0.29] HQL-79 / TargetMol — targetmol.com (#8) `A`
- ❌ low_on_target **0.0544** [on_target=0.48 evidence=0.11] ��Z֫k���64�����R}/�����^�����8���G��l��_���/ֻ͟�}; Y�2}���א�jM�T������O�L$/�� �p�$K,��!?�� 1��y�7��*5 — frontiersin.org (#10)
- ❌ low_on_target **0.0432** [on_target=0.59 evidence=0.07] Safety, pharmacokinetics, and antitumor activity of the anti ... — sciencedirect.com (#6)
- ❌ low_on_target **0.0234** [on_target=0.37 evidence=0.06] �,N������h����;�;s�=A����������;��^pg[~�'�9(�;U�;E1�z� ��aK� �'A�$�?J�譼F#X�G�h�Y��/��Kj�U+ϟ�g�:Ň�i�� — dailymed.nlm.nih.gov (#4)
- ❌ low_evidence **0.0214** [on_target=0.92 evidence=0.02] 4-(Benzhydryloxy)-1-[3-(1H-tetraazol-5-YL)propyl]piperidine — pubchem.ncbi.nlm.nih.gov (#7) `A`
- ❌ low_on_target **0.021** [on_target=0.10 evidence=0.21] Table 3. — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0069** [on_target=0.26 evidence=0.03] A potential therapeutic target for pancreatic ductal adenocarcinoma — sciencedirect.com (#3)

**q027-1** `HQL-79 pancreatic ductal adenocarcinoma in vivo` → kept 2/10, jev 410 ms

- ✅ **0.684** [on_target=0.76 evidence=0.90] www.creative-biolabs.com › blog › adcHyaluronidase-Conjugated Liposomes May Effectively Target ... — creative-biolabs.com (#6)
- ✅ **0.5976** [on_target=0.83 evidence=0.72] An efficient drug delivery system to block pancreatic cancer — pubmed.ncbi.nlm.nih.gov (#1)
- ❌ low_evidence **0.3026** [on_target=0.89 evidence=0.34] Structural and functional characterization of HQL-79, an orally ... — pubmed.ncbi.nlm.nih.gov (#4) `A`
- ❌ low_on_target **0.0767** [on_target=0.59 evidence=0.13] f�pz�Xq���lܾ�rC���y�]���t�d��y��[w ��۟�^�)�-/���^/��`v�Ko}�Sw�Z�6��~����B� w=q�#/��Ƨ� ���/X����v۽��~ — pubs.acs.org (#5)
- ❌ low_on_target **0.033** [on_target=0.45 evidence=0.07] T�>)��~�v�ק��&��N�D��-��n���O��,V@'Ԫ`���-y�V�Â� �̷5N�,i����'��42lܵn��u���a c(w�����Щ+�1�<��S9�C�-�V� — pubs.acs.org (#7)
- ❌ low_on_target **0.0304** [on_target=0.48 evidence=0.06] a'*������N��BU�цL��h4�UqۣBI�}Hi��a��%ǁL�����C�6�> �h&�����YO}��P�~Lm������B�1�rGC=��X?�%mke+�$�b�o�J — pubs.acs.org (#8)
- ❌ low_evidence **0.012** [on_target=0.90 evidence=0.01] HQL 79 — glpbio.com (#9) `A`
- ❌ low_on_target **0.0115** [on_target=0.04 evidence=0.29] In Vivo Preclinical Models — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0059** [on_target=0.02 evidence=0.30] Genetics and biology of pancreatic ductal adenocarcinoma — genesdev.cshlp.org (#10)
- ❌ low_on_target **0.0024** [on_target=0.09 evidence=0.03] `>��?@Q@�R*,�$RQEŤ��y`og�2��{���);�腐��`6y��-&�(��q3Y`��&��gŋ��i����W*#X��TAjEU':����0��O=�s���==�t�� — iopscience.iop.org (#2)

**q027-4** `HQL-79 tumour growth inhibition pancreatic cancer` → kept 5/10, jev 417 ms

- ✅ **0.6264** [on_target=0.81 evidence=0.77] Frontiers / Huaier suppresses pancreatic cancer progression via activating cell autophagy induced fe — frontiersin.org (#8)
- ✅ **0.5694** [on_target=0.78 evidence=0.73] An efficient drug delivery system to block pancreatic cancer — pubmed.ncbi.nlm.nih.gov (#2)
- ✅ **0.5494** [on_target=0.80 evidence=0.69] Molecular Mechanism of Autophagy and Its Regulation by Cannabinoids in Cancer — mdpi.com (#7)
- ✅ **0.5488** [on_target=0.98 evidence=0.56] Buy 1-(8-hydroxy-4-methyl-3,4-dihydro-2H-quinolin-1-yl)-2-methylsulfonylethanone — smolecule.com (#4) `A`
- ✅ **0.4928** [on_target=0.77 evidence=0.64] chloroquine and hydroxychloroquine as anti-cancer agents — pmc.ncbi.nlm.nih.gov (#5)
- ❌ max_keep **0.4457** [on_target=0.70 evidence=0.64] www.creative-biolabs.com › blog › adcHyaluronidase-Conjugated Liposomes May Effectively Target ... — creative-biolabs.com (#3)
- ❌ low_on_target **0.3303** [on_target=0.53 evidence=0.62] Phytochemicals as Multitarget Therapeutics in Pancreatic Cancer: Mechanisms, Clinical Evidence, and  — onlinelibrary.wiley.com (#1)
- ❌ low_evidence **0.3204** [on_target=0.89 evidence=0.36] Structural and functional characterization of HQL-79, an orally ... — pubmed.ncbi.nlm.nih.gov (#6) `A`
- ❌ low_on_target **0.076** [on_target=0.20 evidence=0.38] Targeting the Stromal Pro-Tumoral Hyaluronan-CD44 Pathway in Pancreatic Cancer — mdpi.com (#9)
- ❌ low_evidence **0.0219** [on_target=0.94 evidence=0.02] 4-(Benzhydryloxy)-1-[3-(1H-tetraazol-5-YL)propyl]piperidine — pubchem.ncbi.nlm.nih.gov (#10) `A`

**q027-3** `HQL-79 tumour regression animal model` → kept 3/10, jev 346 ms

- ✅ **0.7566** [on_target=0.97 evidence=0.78] Figure 7. — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.6204** [on_target=0.94 evidence=0.66] Activated T Cells Break Tumor Immunosuppression by Macrophage ... — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.5859** [on_target=0.95 evidence=0.62] Figure 6. — pmc.ncbi.nlm.nih.gov (#3) `A`
- ❌ low_evidence **0.372** [on_target=0.90 evidence=0.41] Structural and functional characterization of HQL-79, an orally ... — pubmed.ncbi.nlm.nih.gov (#6) `A`
- ❌ low_evidence **0.1312** [on_target=0.82 evidence=0.16] FIGURE 4. — pmc.ncbi.nlm.nih.gov (#9) `A`
- ❌ low_on_target **0.0399** [on_target=0.57 evidence=0.07] Safety, pharmacokinetics, and antitumor activity of the anti ... — sciencedirect.com (#10)
- ❌ low_on_target **0.0352** [on_target=0.62 evidence=0.06] Investigating the Anticancer Promise of Synthesized Methylated N-Substituted-4-Hydroxy-2-Quinolone-3 — pubmed.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0229** [on_target=0.53 evidence=0.04] Developing and Characterizing the Anti-Tumor Efficacy of a ... — sciencedirect.com (#8)
- ❌ low_on_target **0.0** [on_target=0.07 evidence=0.00] Cloudflare — cell.com (#4)
- ❌ low_on_target **0.0** [on_target=0.09 evidence=0.00] Cloudflare — cell.com (#5)

## q028

**Objective:** HEC234055 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** HEC234055 · anchors ['HEC234055']

**q028-2** `HEC234055 PK-59 PDAC monotherapy tumour regression` → kept 1/10, jev 328 ms

- ✅ **0.5736** [on_target=0.72 evidence=0.80] [PDF] E262019A_Sunshine Pharma 1..4 - HKEXnews — www1.hkexnews.hk (#1)
- ❌ low_on_target **0.0401** [on_target=0.43 evidence=0.09] [PDF] Lactate Dehydrogenase-A Inhibitor Against Pancreatic Cancer — sciencedirect.com (#6)
- ❌ low_on_target **0.0068** [on_target=0.04 evidence=0.17] Pancreatic Ductal Adenocarcinoma: Current and Evolving ... — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0054** [on_target=0.18 evidence=0.03] A potential therapeutic target for pancreatic ductal adenocarcinoma — sciencedirect.com (#5)
- ❌ low_on_target **0.0042** [on_target=0.18 evidence=0.02] Pancreatic Ductal Adenocarcinoma Archives - Annual Report - Ipsen — ipsen.com (#4)
- ❌ low_on_target **0.0039** [on_target=0.02 evidence=0.19] Pancreatic Cancer: Review of the Current and ... — jhoponline.com (#8)
- ❌ low_on_target **0.0005** [on_target=0.15 evidence=0.00] Press Release — perspectivetherapeutics.com (#2)
- ❌ low_on_target **0.0005** [on_target=0.04 evidence=0.01] Suppression of pancreatic ductal adenocarcinoma growth and ... — broadinstitute.org (#10)
- ❌ low_on_target **0.0002** [on_target=0.06 evidence=0.00] CCDI Hub — moleculartargets.ccdi.cancer.gov (#3)
- ❌ low_on_target **0.0** [on_target=0.06 evidence=0.00] Page not found — medschool.cuanschutz.edu (#7)

**q028-1** `HEC234055 monotherapy HPAC PDAC xenograft regression` → kept 1/10, jev 315 ms

- ✅ **0.546** [on_target=0.70 evidence=0.78] [PDF] E262019A_Sunshine Pharma 1..4 - HKEXnews — www1.hkexnews.hk (#1)
- ❌ low_on_target **0.0191** [on_target=0.52 evidence=0.04] Evaluation of the safety, pharmacokinetics, and antitumor activity of ... — sciencedirect.com (#8)
- ❌ low_on_target **0.0135** [on_target=0.27 evidence=0.05] Treatment of advanced pancreatic carcinoma with a ... — sciencedirect.com (#9)
- ❌ low_on_target **0.0121** [on_target=0.28 evidence=0.04] Article Rapid and Selective Targeting of Heterogeneous Pancreatic ... — sciencedirect.com (#4)
- ❌ low_on_target **0.007** [on_target=0.19 evidence=0.04] A potential therapeutic target for pancreatic ductal adenocarcinoma — sciencedirect.com (#10)
- ❌ low_on_target **0.0018** [on_target=0.06 evidence=0.03] Systemic Therapy for Advanced Pancreatic Cancer in 2025 — onlinelibrary.wiley.com (#6)
- ❌ low_on_target **0.0005** [on_target=0.05 evidence=0.01] Biliary tract cancer — sciencedirect.com (#5)
- ❌ low_on_target **0.0004** [on_target=0.06 evidence=0.01] New targets and new drugs for hepatobiliary cancers — sciencedirect.com (#7)
- ❌ low_on_target **0.0** [on_target=0.04 evidence=0.00] Cloudflare — ejcancer.com (#2)
- ❌ low_on_target **0.0** [on_target=0.04 evidence=0.00] PDC000198 - Proteomic Data Commons - National Cancer Institute — proteomic.datacommons.cancer.gov (#3)

## q029

**Objective:** TP-317 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** TP-317 KPC / TP-317 · anchors ['TP-317 KPC', 'TP-317']

**q029-2** `TP-317 KPC PDAC dose schedule monotherapy` → kept 2/10, jev 577 ms

- ✅ **0.8771** [on_target=0.95 evidence=0.92] Abstract 1135: TP317, a first-in-class resolvin E1 small molecule, potentiates the efficacy of immun — aacrjournals.org (#2) `A`
- ✅ **0.58** [on_target=0.87 evidence=0.67] Abstract 6578: N17465, a systemically deliverable elastase, attenuates tumorigenesis and stimulates  — bohrium.dp.tech (#6) `A`
- ❌ low_evidence **0.3538** [on_target=0.87 evidence=0.41] resolvin E1 (TP-317) / Thetis Pharma - LARVOL DELTA — delta.larvol.com (#4) `A`
- ❌ low_on_target **0.0327** [on_target=0.14 evidence=0.23] Unbiased in vivo preclinical evaluation of anticancer drugs identifies ... — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0229** [on_target=0.53 evidence=0.04] � — cdn.clinicaltrials.gov (#5)
- ❌ low_on_target **0.0173** [on_target=0.52 evidence=0.03] Amendment 1 — cdn.clinicaltrials.gov (#9)
- ❌ low_on_target **0.0165** [on_target=0.45 evidence=0.04] TP-317 for IBD / Non-Immunosuppressive Ulcerative Colitis — thetispharma.com (#8) `A`
- ❌ low_on_target **0.0048** [on_target=0.36 evidence=0.01] Development of TP-317 in Ulcerative Colitis — reporter.nih.gov (#10) `A`
- ❌ low_on_target **0.0016** [on_target=0.04 evidence=0.04] 1784-Neuroendocrine advanced capecitabine and temozolomide — eviq.org.au (#7)
- ❌ low_on_target **0.0008** [on_target=0.04 evidence=0.02] Pembrolizumab, carboplatin and paclitaxel 1 of 5 — kmcc.nhs.uk (#1)

**q029-1** `TP-317 KPC pancreatic cancer tumour regression monotherapy` → kept 4/10, jev 363 ms

- ✅ **0.874** [on_target=0.95 evidence=0.92] Abstract 1135: TP317, a first-in-class resolvin E1 small molecule, potentiates the efficacy of immun — aacrjournals.org (#1) `A`
- ✅ **0.6904** [on_target=0.95 evidence=0.73] Award / SBIR — sbir.gov (#4) `A`
- ✅ **0.6816** [on_target=0.96 evidence=0.71] Firm / SBIR — sbir.gov (#5) `A`
- ✅ **0.5955** [on_target=0.88 evidence=0.68] Abstract 6578: N17465, a systemically deliverable elastase, attenuates tumorigenesis and stimulates  — bohrium.dp.tech (#7) `A`
- ❌ low_on_target **0.325** [on_target=0.50 evidence=0.65] Am J Transl Res 2020;12(3):1031-1043 — e-century.us (#9)
- ❌ low_on_target **0.0423** [on_target=0.47 evidence=0.09] ߄w����I*�/b�r˕٘�}>�g��_��":^)Љ��P�}�꼖���(e��㡱Y;�~�]���E�����/�IbU�̓����-Ʊ�{�{t{LA=�Tm)P,�*u����Q:ʾ�, — techscience.com (#6)
- ❌ low_on_target **0.0323** [on_target=0.11 evidence=0.29] Experimental models of pancreas cancer: what has been the impact ... — jci.org (#8)
- ❌ low_on_target **0.0179** [on_target=0.08 evidence=0.22] TAMing pancreatic cancer: combat with a double edged sword — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0** [on_target=0.06 evidence=0.00] Cloudflare — cell.com (#2)
- ❌ low_on_target **0.0** [on_target=0.11 evidence=0.00] Detail - OpenURL Connection — openurl.ebsco.com (#3)

## q030

**Objective:** SGR-4174 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** SGR-4174 · anchors ['SGR-4174']

**q030-1** `SGR-4174 Mia PaCa2 monotherapy tumour regression xenograft` → kept 5/5, jev 319 ms

- ✅ **0.7663** [on_target=0.97 evidence=0.79] [PDF] Schrödinger Presents New Preclinical Data at AACR Annual Meeting — s203.q4cdn.com (#3) `A`
- ✅ **0.7501** [on_target=0.97 evidence=0.77] SOS1: tracking the evolving path from promising to actionable ... — link.springer.com (#2) `A`
- ✅ **0.6828** [on_target=0.98 evidence=0.70] Schrödinger, Inc. - 临床试验 - 新药情报库- 智慧芽 — synapse.zhihuiya.com (#1) `A`
- ✅ **0.6402** [on_target=0.97 evidence=0.66] Tumor growth inhib News — sigma.larvol.com (#5) `A`
- ✅ **0.62** [on_target=0.93 evidence=0.67] BI-3406 / Boehringer Ingelheim, Novo Nordisk — delta.larvol.com (#4) `A`

**q030-2** `SGR-4174 PDAC xenograft tumour shrinkage single agent` → kept 5/10, jev 362 ms

- ✅ **0.8068** [on_target=0.98 evidence=0.82] SOS1: tracking the evolving path from promising to actionable ... — link.springer.com (#2) `A`
- ✅ **0.8004** [on_target=0.98 evidence=0.82] Company Announcements — markets.ft.com (#5) `A`
- ✅ **0.7546** [on_target=0.98 evidence=0.77] SGR-4174 / Schrodinger - Larvol Delta — delta.larvol.com (#4) `A`
- ✅ **0.6833** [on_target=0.82 evidence=0.83] Preclinical assessment with clinical validation of Selinexor ... — pmc.ncbi.nlm.nih.gov (#8)
- ✅ **0.6822** [on_target=0.97 evidence=0.70] SOS1: tracking the evolving path from promising to actionable ... — link.springer.com (#1) `A`
- ❌ max_keep **0.6664** [on_target=0.98 evidence=0.68] Schrödinger, Inc. - Drug pipelines, Patents, Clinical trials — synapse.patsnap.com (#3) `A`
- ❌ low_evidence **0.384** [on_target=0.96 evidence=0.40] Schrödinger to Present Preclinical Data at AACR Annual ... — s203.q4cdn.com (#6) `A`
- ❌ low_evidence **0.0276** [on_target=0.92 evidence=0.03] Delving into the Latest Updates on SGR-4174 with Synapse — synapse.patsnap.com (#7) `A`
- ❌ low_on_target **0.021** [on_target=0.35 evidence=0.06] E> ��?�"�T����Ԩ$h��N$lyf~����������50#���W//w��衴�*�a��ǔ N�<������D�W�oP��-�9촦�Mr{��b4�����q�*����#�� — korea.kr (#10)
- ❌ low_on_target **0.0063** [on_target=0.04 evidence=0.16] Patient-Derived Xenograft Models of Pancreatic Cancer - PMC — pmc.ncbi.nlm.nih.gov (#9)

## q031

**Objective:** SPR2015 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma (PDAC) animal models  
**Target sent:** SPR2015 · anchors ['SPR2015']

**q031-2** `SPR2015 AsPC-1 xenograft tumour regression shrinkage` → kept 4/10, jev 347 ms

- ✅ **0.9278** [on_target=0.98 evidence=0.95] SPR2015是一种高效且选择性的KRAS G12D（ON）抑制剂，在临床前模型中... — posterkeep.com (#2) `A`
- ✅ **0.7534** [on_target=0.97 evidence=0.78] KRAS G12D Inhibitor's $2.13B Deal Tests Cross-Border Tech Transfer — pharmtech.com (#7) `A`
- ✅ **0.7056** [on_target=0.98 evidence=0.72] Merck Enters into Exclusive Global License Agreement ... — merck.com (#3) `A`
- ✅ **0.6564** [on_target=0.97 evidence=0.68] SPR2015: Merck Pays $400M, Up to $2.13B - novapharmanews.com — novapharmanews.com (#1) `A`
- ❌ low_on_target **0.0021** [on_target=0.21 evidence=0.01] Cancer Cell — sciencedirect.com (#10)
- ❌ low_on_target **0.0009** [on_target=0.09 evidence=0.01] Breast Cancer Research and Treatment — deepblue.lib.umich.edu (#6)
- ❌ low_on_target **0.0005** [on_target=0.16 evidence=0.00] register — academic.oup.com (#4)
- ❌ low_on_target **0.0005** [on_target=0.04 evidence=0.01] Current Oncology Reports — springermedicine.com (#9)
- ❌ low_on_target **0.0** [on_target=0.07 evidence=0.00] PDC000198 - Proteomic Data Commons - National Cancer Institute — proteomic.datacommons.cancer.gov (#5)
- ❌ low_on_target **0.0** [on_target=0.04 evidence=0.00] Cloudflare — aacrjournals.org (#8)

**q031-3** `SPR2015 PDAC monotherapy xenograft tumour growth inhibition` → kept 5/10, jev 378 ms

- ✅ **0.9603** [on_target=0.99 evidence=0.97] SPR2015是一种高效且选择性的KRAS G12D（ON）抑制剂，在临床前模型中... — posterkeep.com (#1) `A`
- ✅ **0.7566** [on_target=0.97 evidence=0.78] KRAS G12D Inhibitor's $2.13B Deal Tests Cross-Border Tech Transfer — pharmtech.com (#4) `A`
- ✅ **0.6926** [on_target=0.98 evidence=0.71] Merck Enters into Exclusive Global License Agreement ... — ca.finance.yahoo.com (#7) `A`
- ✅ **0.6892** [on_target=0.98 evidence=0.70] MSD takes a $400m bite of SciBrunch's KRAS drug — pharmaphorum.com (#6) `A`
- ✅ **0.686** [on_target=0.98 evidence=0.70] Merck licenses SPR2015, an oral KRAS G12D inhibitor, from ... — chemxplore.com (#8) `A`
- ❌ max_keep **0.6762** [on_target=0.98 evidence=0.69] Merck Licenses Preclinical KRAS G12D Inhibitor from SciBrunch — pharmexec.com (#5) `A`
- ❌ max_keep **0.6664** [on_target=0.98 evidence=0.68] Revolution Medicines - MedPath Trial — trial.medpath.com (#3) `A`
- ❌ max_keep **0.6531** [on_target=0.97 evidence=0.67] Merck, SciBrunch Launch Up-to-$2.13B Collaboration ... — genengnews.com (#2) `A`
- ❌ max_keep **0.6499** [on_target=0.97 evidence=0.67] Merck Inks $2.1B Deal With Chinese Biotech to Expand ... — finance.yahoo.com (#9) `A`
- ❌ max_keep **0.6272** [on_target=0.96 evidence=0.65] SPR2015 / SciBrunch Therapeutics, Merck (MSD) — delta.larvol.com (#10) `A`

**q031-1** `SPR2015 HPAC xenograft TGI percentage monotherapy` → ABSTAIN, jev 383 ms

- ❌ low_on_target **0.0147** [on_target=0.26 evidence=0.06] �,N������h����;�;s�=A����������;��^pg[~�'�9(�;U�;E1�z� ��aK� �'A�$�?J�譼F#X�G�h�Y��/��Kj�U+ϟ�g�:Ň�i�� — dailymed.nlm.nih.gov (#10)
- ❌ low_on_target **0.0135** [on_target=0.29 evidence=0.05] g�7Ke�wOD 2c����7�Ĕ��������aT@� �*� )A���s�$�TS�&g���R���Q��r6�*Ī���t��1wv8 �h�u%�;q�o�+j� @�m���Ʈ�� — dailymed.nlm.nih.gov (#7)
- ❌ low_on_target **0.0135** [on_target=0.29 evidence=0.05] �ͪ\�qӱ�`�/�#@�.�n��r���j_��r#~����t�>#��%t_�<�.<�if�eC�������sN������ufx�xQ?�{��8�� w���aW��;�V��×�8 — dailymed.nlm.nih.gov (#9)
- ❌ low_on_target **0.0132** [on_target=0.44 evidence=0.03] � — cdn.clinicaltrials.gov (#8)
- ❌ low_on_target **0.0121** [on_target=0.28 evidence=0.04] �3/c~X��D���;�T:K©z�r����s�1:etK$�$����[���{e�J���������+8�\Ul�`�[�:�HB0�p����~�ɔw�]�$��Q`�̡�xV�z��^ — dailymed.awsprod.nlm.nih.gov (#6)
- ❌ low_on_target **0.0002** [on_target=0.07 evidence=0.00] PDC000198 - Proteomic Data Commons - National Cancer Institute — proteomic.datacommons.cancer.gov (#2)
- ❌ low_on_target **0.0** [on_target=0.12 evidence=0.00] Internal Server Error — cdas.cancer.gov (#1)
- ❌ low_on_target **0.0** [on_target=0.03 evidence=0.00] Cloudflare — ejcancer.com (#3)
- ❌ low_on_target **0.0** [on_target=0.16 evidence=0.00] PMC — ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0** [on_target=0.07 evidence=0.00] Page Not Found — mayo.edu (#5)

**q031-4** `SPR2015 HPAC AsPC-1 xenograft AACR 2026 abstract 5978` → kept 5/10, jev 548 ms

- ✅ **0.8342** [on_target=0.97 evidence=0.86] Merck–SciBrunch SPR2015 Deal / Lucid Diligence Brief - LucidQuest — lqventures.com (#4) `A`
- ✅ **0.6958** [on_target=0.98 evidence=0.71] Merck Enters into Exclusive Global License Agreement ... — merck.com (#2) `A`
- ✅ **0.6794** [on_target=0.98 evidence=0.69] Merck Licenses SciBrunch's Preclinical Oral KRAS G12D ... — trial.medpath.com (#10) `A`
- ✅ **0.6564** [on_target=0.97 evidence=0.68] SPR2015: Merck Pays $400M, Up to $2.13B - novapharmanews.com — novapharmanews.com (#5) `A`
- ✅ **0.6531** [on_target=0.97 evidence=0.67] Merck, SciBrunch Launch Up-to-$2.13B Collaboration ... — genengnews.com (#7) `A`
- ❌ max_keep **0.6141** [on_target=0.94 evidence=0.65] SPR2015是一种高效且选择性的KRAS G12D（ON）抑制剂，在临床前模型中... — posterkeep.com (#1) `A`
- ❌ max_keep **0.54** [on_target=0.97 evidence=0.56] Why Merck Paid Up for the Same Founder's Next KRAS ... — oncodaily.com (#9) `A`
- ❌ max_keep **0.5152** [on_target=0.92 evidence=0.56] Anirban Maitra on X: "This #AACR26 abstract is worth $400 ... — x.com (#3) `A`
- ❌ low_on_target **0.0002** [on_target=0.06 evidence=0.00] Abstracts Annual Meeting 2026 / Meetings / AACR — aacr.org (#8)
- ❌ low_on_target **0.0001** [on_target=0.04 evidence=0.00] AACR 2026 Annual Meeting Abstracts — cancer.uillinois.edu (#6)

## q032

**Objective:** PHY-003 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Head and Neck Squamous Cell Carcinoma animal models  
**Target sent:** PHY-003 · anchors ['PHY-003']

**q032-2** `PHY-003 HNSCC in vivo tumour growth inhibition dose` → ABSTAIN, jev 356 ms

- ❌ low_on_target **0.1885** [on_target=0.29 evidence=0.65] Current and Emerging Molecular Therapies for Head and Neck ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.1639** [on_target=0.33 evidence=0.50] Melo, G., Silva, C. A. B., Hague, A., Parkinson, E. K., & Rivero, E. R. — research-information.bris.ac.uk (#9)
- ❌ low_on_target **0.09** [on_target=0.18 evidence=0.50] Targeting DNA Double-Strand Break Repair Enhances Radiosensitivity of HPV-Positive and HPV-Negative  — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0852** [on_target=0.18 evidence=0.47] The role of key gut microbial metabolites in ... — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0297** [on_target=0.10 evidence=0.30] [PDF] This electronic thesis or dissertation has been downloaded from the ... — kclpure.kcl.ac.uk (#3)
- ❌ low_on_target **0.0272** [on_target=0.34 evidence=0.08] ����~��?g���O����%��ö~�A��εo�+A�BF�f�2����A�5{�r�;y���/�߉5�~��u-)`���i�c��d �TY�&2�h��烐/���P_��/7� � — journals.plos.org (#2)
- ❌ low_on_target **0.0171** [on_target=0.09 evidence=0.19] Helmholtz-Zentrum Dresden-Rossendorf (HZDR) — hzdr.de (#5)
- ❌ low_on_target **0.0137** [on_target=0.41 evidence=0.03] OncJuly2 6..6 — citeseerx.ist.psu.edu (#1)
- ❌ low_on_target **0.0124** [on_target=0.07 evidence=0.18] Establishment of head and neck squamous cell carcinoma ... — oaepublish.com (#8)
- ❌ low_on_target **0.0007** [on_target=0.11 evidence=0.01] Other News To Note — bioworld.com (#6)

**q032-1** `PHY-003 HNSCC monotherapy xenograft tumour regression` → ABSTAIN, jev 464 ms

- ❌ low_on_target **0.0432** [on_target=0.48 evidence=0.09] ������+X�G������;��g6�vnUJ�Yg�D% 'qF�;�h Q��ҭT�%���2��蔴L�"�3C`�*�N�bh�^���`aj��*�yL�5����g��!��H)��� — frontiersin.org (#3)
- ❌ low_on_target **0.042** [on_target=0.42 evidence=0.10] ���̝��p�l��Б�KY��oA�W�Y���ڱ�P��…��lذ�j�&¿�/`+y8���W��M�_��5q���ԗ�[��ϧ�߄����Gu�F5�j�h��Ǿa�Z�a���d��թ} — frontiersin.org (#10)
- ❌ low_on_target **0.0415** [on_target=0.14 evidence=0.30] Targeted therapy for head and neck cancer: signaling pathways and ... — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0387** [on_target=0.40 evidence=0.10] �4��&�8�#�ol��)�g�,���Hڭ�G��r���3?�H�#d#7k��ܳy$l�uH���E],~ת��A������5��ݴ���K�m�=��%�<��cB����������  — frontiersin.org (#8)
- ❌ low_on_target **0.0364** [on_target=0.39 evidence=0.09] ��#���0�P7���ho����a� ��[�X�`�p"�3��(��]��5����m�r���� �gl���m�0�S���oH�(EA�?%�D����$RN�=������"}x�1 — frontiersin.org (#7)
- ❌ low_on_target **0.0296** [on_target=0.37 evidence=0.08] epub — frontiersin.org (#2)
- ❌ low_on_target **0.0123** [on_target=0.41 evidence=0.03] OncJuly2 6..6 — citeseerx.ist.psu.edu (#9)
- ❌ low_on_target **0.0114** [on_target=0.06 evidence=0.19] Targeted therapy for head and neck cancer: signaling ... — nature.com (#6)
- ❌ low_on_target **0.0064** [on_target=0.32 evidence=0.02] Original article Head and neck squamous cell carcinoma ... — sciencedirect.com (#1)
- ❌ low_on_target **0.0038** [on_target=0.19 evidence=0.02] A novel therapeutic approach for head and neck cancer — sciencedirect.com (#4)

**q032-3** `PHY-003 head and neck squamous cell carcinoma animal model efficacy` → ABSTAIN, jev 329 ms

- ❌ low_on_target **0.1247** [on_target=0.22 evidence=0.57] A Novel Modular Polymer Platform for the Treatment of Head ... — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.116** [on_target=0.30 evidence=0.39] Overview of current and future biologically based targeted therapies ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.1071** [on_target=0.21 evidence=0.51] Use of a Novel Polymer in an Animal Model of Head and Neck Squamous Cell Carcinoma - PubMed — pubmed.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.0127** [on_target=0.05 evidence=0.25] pmc.ncbi.nlm.nih.gov › articles › PMC7944998Head and neck squamous cell carcinoma - PMC — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0102** [on_target=0.05 evidence=0.20] 64878472 — biorxiv.org (#9)
- ❌ low_on_target **0.0093** [on_target=0.03 evidence=0.31] Preclinical models in head and neck squamous cell carcinoma — nature.com (#3)
- ❌ low_on_target **0.0059** [on_target=0.03 evidence=0.20] Key signalling pathways in head and neck squamous cell carcinoma — academic.oup.com (#5)
- ❌ low_on_target **0.0047** [on_target=0.04 evidence=0.12] Spandidos Publications: Medicine International — spandidos-publications.com (#6)
- ❌ low_on_target **0.0031** [on_target=0.03 evidence=0.10] Frontiers / Shaping next decade of systemic therapy for head and neck squamous cell carcinoma: where — frontiersin.org (#4)
- ❌ low_on_target **0.0006** [on_target=0.03 evidence=0.02] My Bibliography - NCBI — ncbi.nlm.nih.gov (#8)

## q033

**Objective:** DXP-007 sponsor development stage indication public source  
**Target sent:** DXP-007 · anchors ['DXP-007']

**q033-1** `DXP-007 sponsor` → ABSTAIN, jev 531 ms

- ❌ low_on_target **0.0127** [on_target=0.10 evidence=0.13] Sponsors & Exhibitors / ProcureCon MRO 2026 — procureconmro.wbresearch.com (#3)
- ❌ low_on_target **0.0086** [on_target=0.37 evidence=0.02] DXP Enterprises — x.com (#7)
- ❌ low_on_target **0.0056** [on_target=0.06 evidence=0.09] Legendary DXP: 007 - App Store - Apple — apps.apple.com (#1) `A`
- ❌ low_on_target **0.0045** [on_target=0.08 evidence=0.06] DXP / Logopedia — logos.fandom.com (#6)
- ❌ low_on_target **0.0042** [on_target=0.06 evidence=0.07] Legendary DXP: 007 – Apps no Google Play — play.google.com (#8) `A`
- ❌ low_on_target **0.0038** [on_target=0.23 evidence=0.02] DXP Enterprises, Inc. — sec.gov (#4)
- ❌ low_on_target **0.0007** [on_target=0.11 evidence=0.01] Master Investment Portfolio — sec.gov (#10)
- ❌ low_on_target **0.0005** [on_target=0.16 evidence=0.00] Events & Presentations — ir.dxpe.com (#9)
- ❌ low_on_target **0.0004** [on_target=0.11 evidence=0.00] DXP News — dxpwind.com (#2)
- ❌ low_on_target **0.0001** [on_target=0.03 evidence=0.00] Common searches — search.electoralcommission.org.uk (#5)

**q033-2** `DXP-007 development stage` → ABSTAIN, jev 547 ms

- ❌ low_on_target **0.5304** [on_target=0.68 evidence=0.78] www.otsuka.co.jp · pipelinePipeline / Otsuka Pharmaceutical Co., Ltd. — otsuka.co.jp (#8)
- ❌ low_on_target **0.0868** [on_target=0.31 evidence=0.28] Profiles — drughunter.com (#10)
- ❌ low_on_target **0.0702** [on_target=0.13 evidence=0.54] Digital eXperience Platform (DXP) Project — bcp.dof.ca.gov (#2)
- ❌ low_on_target **0.052** [on_target=0.12 evidence=0.43] Digital Experience Platform (DXP) Project — projecttracking.technology.ca.gov (#5)
- ❌ low_on_target **0.004** [on_target=0.11 evidence=0.04] DXP / Revolutionary AI-Powered Platform Elevating the Digital ... — dxp.io (#7)
- ❌ low_on_target **0.0037** [on_target=0.22 evidence=0.02] DXP Enterprises, Inc. — sec.gov (#3)
- ❌ low_on_target **0.0033** [on_target=0.14 evidence=0.02] Legendary DXP: 007 — apps.apple.com (#9) `A`
- ❌ low_on_target **0.0011** [on_target=0.16 evidence=0.01] DXP Enterprises, Inc. - Investor Relations — ir.dxpe.com (#6)
- ❌ low_on_target **0.0007** [on_target=0.21 evidence=0.00] DXPR Status — status.dxpr.com (#4)
- ❌ low_on_target **0.0** [on_target=0.18 evidence=0.00] News — ir.dxpe.com (#1)

**q033-3** `DXP-007 inflammatory bowel disease` → ABSTAIN, jev 374 ms

- ❌ low_on_target **0.2851** [on_target=0.47 evidence=0.61] Introduction — spandidos-publications.com (#1)
- ❌ low_on_target **0.0804** [on_target=0.18 evidence=0.45] Molecular fingerprints of neutrophil-dependent oxidative ... — pubmed.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0533** [on_target=0.17 evidence=0.31] Landscape of new drugs and targets in inflammatory bowel disease — onlinelibrary.wiley.com (#5)
- ❌ low_on_target **0.0306** [on_target=0.09 evidence=0.34] Inflammatory Bowel Diseases — clinpgx.org (#6)
- ❌ low_on_target **0.0294** [on_target=0.09 evidence=0.33] Selective Nanoparticulate Systems for Drug Delivery in Inflammatory ... — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0213** [on_target=0.09 evidence=0.24] Small Molecule Drugs in Inflammatory Bowel Diseases - PMC - NIH — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0178** [on_target=0.05 evidence=0.36] Inflammatory Bowel Disease — malacards.org (#4)
- ❌ low_on_target **0.015** [on_target=0.05 evidence=0.30] new drugs for inflammatory bowel disease treatment ... — pubmed.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0143** [on_target=0.05 evidence=0.29] Novel Therapies for Inflammatory Bowel Disease — link.springer.com (#8)
- ❌ low_on_target **0.0078** [on_target=0.05 evidence=0.16] Review article: novel oral‐targeted therapies in inflammatory bowel disease — onlinelibrary.wiley.com (#10)

## q034

**Objective:** Compound 18l first regulatory approval or market launch year for acute myeloid leukemia  
**Target sent:** Compound 18l · anchors ['Compound 18l']

**q034-1** `Compound 18l ALKBH5 AML regulatory approval launch year` → kept 2/10, jev 348 ms

- ✅ **0.5152** [on_target=0.84 evidence=0.61] Decoding the immunoregulatory functions of ALKBH5 in ... — frontiersin.org (#9) `A`
- ✅ **0.4984** [on_target=0.84 evidence=0.59] Chinese Academy of Sciences Shanghai Branch — english.shb.cas.cn (#4)
- ❌ low_on_target **0.3705** [on_target=0.65 evidence=0.57] Discovery of Covalent and Cell‐Active ALKBH5 Inhibitors with ... — onlinelibrary.wiley.com (#8)
- ❌ low_on_target **0.312** [on_target=0.49 evidence=0.64] Delving into the Latest Updates on ALKBH5 inhibitor(Shanghai Institute of Materia Medica Chinese Aca — synapse.patsnap.com (#6)
- ❌ low_on_target **0.1751** [on_target=0.26 evidence=0.67] Oncology (Cancer)/Hematologic Malignancies Approval ... — fda.gov (#7)
- ❌ low_on_target **0.0115** [on_target=0.08 evidence=0.14] ALKBH5 — affinage.wi.mit.edu (#10)
- ❌ low_on_target **0.0014** [on_target=0.06 evidence=0.02] NME — fda.gov (#2)
- ❌ low_on_target **0.0003** [on_target=0.05 evidence=0.01] Breakthrough Therapy Approvals - FDA — fda.gov (#5)
- ❌ low_on_target **0.0001** [on_target=0.03 evidence=0.00] Drug Approvals and Databases - FDA — fda.gov (#1)
- ❌ low_on_target **0.0** [on_target=0.06 evidence=0.00] Search Orphan Drug Designations and Approvals — accessdata.fda.gov (#3)

## q035

**Objective:** BS-HH-002 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** BS-HH-002 · anchors ['BS-HH-002']

**q035-2** `BS-HH-002 market launch AML` → kept 5/10, jev 342 ms

- ✅ **0.9408** [on_target=0.98 evidence=0.96] Ozmosi / BS HH 002.SA Drug Profile — pryzm.ozmosi.com (#8) `A`
- ✅ **0.8374** [on_target=0.97 evidence=0.86] Therapeutic effects of an innovative BS-HH-002 drug on ... — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.8166** [on_target=0.98 evidence=0.83] BS-HH-002 Drug Asset Due Diligence Report 2026 — synapse.patsnap.com (#5) `A`
- ✅ **0.8036** [on_target=0.98 evidence=0.82] 查看聚合内容 — bydrug.pharmcube.com (#6) `A`
- ✅ **0.8019** [on_target=0.97 evidence=0.83] Delving into the Latest Updates on BS-HH-002 with Synapse — synapse.patsnap.com (#3) `A`
- ❌ max_keep **0.552** [on_target=0.92 evidence=0.60] ACYLATED DERIVATIVE OF HOMOHARRINGTONINE, PREPARATION METHOD THEREFOR, AND APPLICATION THEREOF — patents.justia.com (#10) `A`
- ❌ low_on_target **0.3476** [on_target=0.44 evidence=0.79] First in Human Testing of Dose-escalation of SAR440234 in Patients With Acute Myeloid Leukemia, Acut — med.agiltrace.com (#9)
- ❌ low_on_target **0.0002** [on_target=0.03 evidence=0.01] Search / AML Hub — aml-hub.com (#1)
- ❌ low_on_target **0.0** [on_target=0.05 evidence=0.00] Content Search - hkexnews.hk — www3.hkexnews.hk (#4)
- ❌ low_on_target **0.0** [on_target=0.06 evidence=0.00] 0001213900-22-031666.txt — sec.gov (#7)

**q035-1** `BS-HH-002 regulatory approval AML` → kept 5/10, jev 333 ms

- ✅ **0.9506** [on_target=0.98 evidence=0.97] Ozmosi / BS HH 002.SA Drug Profile — pryzm.ozmosi.com (#4) `A`
- ✅ **0.8277** [on_target=0.97 evidence=0.85] Therapeutic effects of an innovative BS-HH-002 drug on ... — pmc.ncbi.nlm.nih.gov (#3) `A`
- ✅ **0.7296** [on_target=0.96 evidence=0.76] Delving into the Latest Updates on BS-HH-002 with Synapse — synapse.patsnap.com (#2) `A`
- ✅ **0.6102** [on_target=0.92 evidence=0.66] A Phase I, Open-Label, Dose Escalation and Cohort Expansion Study of BS HH 002.SA in Patients With A — med.agiltrace.com (#1) `A`
- ✅ **0.5731** [on_target=0.95 evidence=0.60] ACYLATED DERIVATIVE OF HOMOHARRINGTONINE, PREPARATION METHOD THEREFOR, AND APPLICATION THEREOF — patents.justia.com (#9) `A`
- ❌ max_keep **0.4194** [on_target=0.74 evidence=0.57] Assessment of Effectiveness and Safety of Luspatercept in Patients Suffering From Lower-risk Myelody — med.agiltrace.com (#5) `A`
- ❌ low_on_target **0.3619** [on_target=0.47 evidence=0.77] First in Human Testing of Dose-escalation of SAR440234 in Patients With Acute Myeloid Leukemia, Acut — med.agiltrace.com (#10)
- ❌ low_evidence **0.3186** [on_target=0.81 evidence=0.39] A Study of HSK29116 in Adults With Relapsed/Refractory B-cell Malignancies — med.agiltrace.com (#7) `A`
- ❌ low_on_target **0.2336** [on_target=0.49 evidence=0.48] A Safety and Efficacy Study of SHR-1702 Monotherapy in Patients With Acute Myeloid Leukemia (AML) or — med.agiltrace.com (#8)
- ❌ low_on_target **0.0051** [on_target=0.11 evidence=0.05] Hedgehog Pathway Inhibitors: A New Therapeutic Class for ... — aacrjournals.org (#6)

**q035-4** `BS-HH-002 expected approval year` → kept 3/10, jev 348 ms

- ✅ **0.8064** [on_target=0.96 evidence=0.84] BS-HH-002 Drug Asset Due Diligence Report 2026 — synapse.patsnap.com (#1) `A`
- ✅ **0.7906** [on_target=0.98 evidence=0.81] 查看聚合内容 — bydrug.pharmcube.com (#10) `A`
- ✅ **0.516** [on_target=0.90 evidence=0.57] BSB-1001 for Blood Cancers - Clinical Trials — withpower.com (#5) `A`
- ❌ low_evidence **0.4526** [on_target=0.93 evidence=0.49] Targeting the translational machinery to overcome apoptosis ... — pmc.ncbi.nlm.nih.gov (#7) `A`
- ❌ low_evidence **0.2311** [on_target=0.95 evidence=0.24] Delving into the Latest Updates on Shanghai Bensen Pharmaceutical Co., Ltd. with Synapse — synapse.patsnap.com (#4) `A`
- ❌ low_on_target **0.0008** [on_target=0.05 evidence=0.02] Fast Track Approvals — fda.gov (#6)
- ❌ low_on_target **0.0005** [on_target=0.07 evidence=0.01] www.fda.gov › drugs › nda-and-bla-approvalsNDA and BLA Calendar Year Approvals / FDA — fda.gov (#3)
- ❌ low_on_target **0.0003** [on_target=0.05 evidence=0.01] Breakthrough Therapy Approvals - FDA — fda.gov (#9)
- ❌ low_on_target **0.0** [on_target=0.17 evidence=0.00] Bristol Myers Squibb - Corporate news details — news.bms.com (#2)
- ❌ low_on_target **0.0** [on_target=0.05 evidence=0.00] FDA Calendar - FDA Tracker — fdatracker.com (#8)

**q035-5** `BS-HH-002 first patient AML` → kept 4/10, jev 371 ms

- ✅ **0.8102** [on_target=0.98 evidence=0.83] BS-HH-002 - Drug Targets, Indications, Patents — synapse-patsnap-com.libproxy1.nus.edu.sg (#1) `A`
- ✅ **0.6816** [on_target=0.96 evidence=0.71] A Phase I, Open-Label, Dose Escalation and Cohort Expansion ... — trial.medpath.com (#7) `A`
- ✅ **0.5336** [on_target=0.92 evidence=0.58] ACYLATED DERIVATIVE OF HOMOHARRINGTONINE, PREPARATION METHOD THEREFOR, AND APPLICATION THEREOF — patents.justia.com (#3) `A`
- ❌ low_evidence **0.4354** [on_target=0.92 evidence=0.47] Targeting the translational machinery to overcome ... — pmc.ncbi.nlm.nih.gov (#10) `A`
- ✅ **0.42** [on_target=0.75 evidence=0.56] BSB-1001 for Blood Cancers - Clinical Trials — withpower.com (#6) `A`
- ❌ low_evidence **0.3724** [on_target=0.76 evidence=0.49] Therapeutic effects of an innovative BS-HH-002 drug on pancreatic ... — pubmed.ncbi.nlm.nih.gov (#4) `A`
- ❌ low_evidence **0.3668** [on_target=0.84 evidence=0.44] Therapeutic effects of an innovative BS-HH-002 drug on pancreatic cancer cells via induction of comp — sciencedirect.com (#8) `A`
- ❌ low_on_target **0.255** [on_target=0.50 evidence=0.51] Acylated derivative of homoharringtonine, preparation method therefor, and application thereof — patents.google.com (#9)
- ❌ low_on_target **0.0004** [on_target=0.11 evidence=0.00] Clinical trial results - Bristol Myers Squibb — bms.com (#5)
- ❌ low_on_target **0.0** [on_target=0.04 evidence=0.00] Guidelines - British Society for Haematology — b-s-h.org.uk (#2)

**q035-3** `BS-HH-002 Bensheng Pharma AML clinical development` → kept 5/10, jev 427 ms

- ✅ **0.9572** [on_target=0.98 evidence=0.98] Ozmosi / BS HH 002.SA Drug Profile — pryzm.ozmosi.com (#9) `A`
- ✅ **0.8148** [on_target=0.97 evidence=0.84] Therapeutic effects of an innovative BS-HH-002 drug on ... — pmc.ncbi.nlm.nih.gov (#3) `A`
- ✅ **0.7676** [on_target=0.98 evidence=0.78] Delving into the Latest Updates on BS-HH-002 with Synapse — synapse.patsnap.com (#1) `A`
- ✅ **0.7566** [on_target=0.97 evidence=0.78] Delving into the Latest Updates on Shanghai Bensen Pharmaceutical Co., Ltd. with Synapse — synapse.patsnap.com (#10) `A`
- ✅ **0.5952** [on_target=0.96 evidence=0.62] Acylated derivative of homoharringtonine, preparation method ... — trea.com (#7) `A`
- ❌ max_keep **0.5826** [on_target=0.95 evidence=0.61] Acylated derivative of homoharringtonine, preparation method therefor, and application thereof — patents.google.com (#2) `A`
- ❌ max_keep **0.57** [on_target=0.95 evidence=0.60] A Phase I, Open-Label, Dose Escalation and Cohort Expansion Study of BS HH 002.SA in Patients With A — med.agiltrace.com (#6) `A`
- ❌ max_keep **0.5301** [on_target=0.93 evidence=0.57] 高三尖杉酯碱的酰化衍生物、及其制备方法和应用 — patents.google.com (#8) `A`
- ❌ low_on_target **0.417** [on_target=0.68 evidence=0.61] Homoharringtonine: mechanisms, clinical applications and ... — pmc.ncbi.nlm.nih.gov (#5) `A`
- ❌ low_on_target **0.034** [on_target=0.15 evidence=0.23] [PDF] MCL-1 inhibitors, fast-lane development of a new class of anti-canc ... — exaly.com (#4)

## q036

**Objective:** VAR-101 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic Ductal Carcinoma animal models  
**Target sent:** VAR-101 · anchors ['VAR-101']

**q036-2** `VAR-101 pancreatic cancer tumour regression animal model` → ABSTAIN, jev 332 ms

- ❌ low_on_target **0.0284** [on_target=0.50 evidence=0.06] Project Details — reporter.nih.gov (#10)
- ❌ low_on_target **0.0208** [on_target=0.25 evidence=0.08] Section Menu — reporter.nih.gov (#8)
- ❌ low_on_target **0.015** [on_target=0.45 evidence=0.03] Overview — vivo.weill.cornell.edu (#9)
- ❌ low_on_target **0.0136** [on_target=0.37 evidence=0.04] [PDF] VP-VSJ-110-2101 - ClinicalTrials.gov — cdn.clinicaltrials.gov (#7)
- ❌ low_on_target **0.0065** [on_target=0.39 evidence=0.02] Study Details / — clinicaltrials.gov (#6)
- ❌ low_on_target **0.0027** [on_target=0.20 evidence=0.01] Home — clinicaltrials.gov (#5)
- ❌ low_on_target **0.0024** [on_target=0.36 evidence=0.01] Study Details Page — abbvieclinicaltrials.com (#3)
- ❌ low_on_target **0.0** [on_target=0.08 evidence=0.00] Cloudflare — cell.com (#1)
- ❌ low_on_target **0.0** [on_target=0.09 evidence=0.00] Detail - OpenURL Connection — openurl.ebsco.com (#2)
- ❌ low_on_target **0.0** [on_target=0.10 evidence=0.00] Page not found — medschool.cuanschutz.edu (#4)

**q036-3** `VAR-101 aPKCi PDAC in vivo efficacy monotherapy` → kept 1/10, jev 319 ms

- ✅ **0.5609** [on_target=0.94 evidence=0.60] SPK Acquisition Corp. Form 425 Filed 2022-02-14 — pdf.secdatabase.com (#7) `A`
- ❌ low_on_target **0.0138** [on_target=0.46 evidence=0.03] NCT07195487 / A Clinical Study to Evaluate the Safety, ... — clinicaltrials.gov (#6)
- ❌ low_on_target **0.0117** [on_target=0.44 evidence=0.03] [PDF] VP-VSJ-110-2101 - ClinicalTrials.gov — cdn.clinicaltrials.gov (#5)
- ❌ low_on_target **0.0072** [on_target=0.36 evidence=0.02] 2.1. Step 1: Dose Escalation... — sciencedirect.com (#8)
- ❌ low_on_target **0.0072** [on_target=0.31 evidence=0.02] Exploratory, multicenter, open-label study to evaluate the ... — sciencedirect.com (#9)
- ❌ low_on_target **0.006** [on_target=0.36 evidence=0.02] Study Details / — clinicaltrials.gov (#4)
- ❌ low_on_target **0.0049** [on_target=0.21 evidence=0.02] Clinical Trial A phase 2b, randomized, double-blind ... — sciencedirect.com (#10)
- ❌ low_on_target **0.0032** [on_target=0.12 evidence=0.03] A potential therapeutic target for pancreatic ductal adenocarcinoma — sciencedirect.com (#3)
- ❌ low_on_target **0.001** [on_target=0.31 evidence=0.00] register — academic.oup.com (#1)
- ❌ low_on_target **0.0** [on_target=0.11 evidence=0.00] Page not found — medschool.cuanschutz.edu (#2)

**q036-1** `VAR-101 pancreatic ductal carcinoma monotherapy xenograft TGI` → ABSTAIN, jev 425 ms

- ❌ low_on_target **0.0173** [on_target=0.40 evidence=0.04] [PDF] VP-VSJ-110-2101 - ClinicalTrials.gov — cdn.clinicaltrials.gov (#6)
- ❌ low_on_target **0.0159** [on_target=0.53 evidence=0.03] Phase 1b/2a Study Assessing the Safety and Efficacy of ... — sciencedirect.com (#8)
- ❌ low_on_target **0.0089** [on_target=0.38 evidence=0.02] Exploratory, multicenter, open-label study to evaluate the ... — sciencedirect.com (#10)
- ❌ low_on_target **0.0061** [on_target=0.23 evidence=0.03] Clinical Trial A phase 2b, randomized, double-blind ... — sciencedirect.com (#9)
- ❌ low_on_target **0.0045** [on_target=0.34 evidence=0.01] Clinical Trial Detail — massgeneral.org (#5)
- ❌ low_on_target **0.0021** [on_target=0.16 evidence=0.01] Home — clinicaltrials.gov (#7)
- ❌ low_on_target **0.0011** [on_target=0.33 evidence=0.00] Study Details Page — abbvieclinicaltrials.com (#2)
- ❌ low_on_target **0.0** [on_target=0.11 evidence=0.00] Detail - OpenURL Connection — openurl.ebsco.com (#1)
- ❌ low_on_target **0.0** [on_target=0.06 evidence=0.00] Eligibility criteria - PAN Foundation Trial Finder — trialfinder.panfoundation.org (#3)
- ❌ low_on_target **0.0** [on_target=0.11 evidence=0.00] Page not found — medschool.cuanschutz.edu (#4)

## q037

**Objective:** IPS-06061 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in KRAS G12D Mutant Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** IPS-06061 · anchors ['IPS-06061']

**q037-2** `IPS-06061 30 mg/kg TGI AsPC-1` → kept 4/10, jev 384 ms

- ✅ **0.9024** [on_target=0.96 evidence=0.94] IPS-07004 - 炎症，哮喘，帕金森病_专利 - 新药情报库 - 智慧芽 — synapse.zhihuiya.com (#1) `A`
- ✅ **0.6531** [on_target=0.97 evidence=0.67] IPS-06061, a novel TPD molecular glue degrader targeting ... — semanticscholar.org (#7) `A`
- ✅ **0.6434** [on_target=0.97 evidence=0.66] IPS-06061 / InnoPharmaScreen - LARVOL DELTA — delta.larvol.com (#10) `A`
- ✅ **0.5367** [on_target=0.97 evidence=0.55] IPS-06061 / MedChemExpress — file.medchemexpress.com (#9) `A`
- ❌ low_evidence **0.0614** [on_target=0.80 evidence=0.08] IPS-06061 / KRAS G12D Degrader / MedChemExpress — medchemexpress.com (#4) `A`
- ❌ low_on_target **0.009** [on_target=0.18 evidence=0.05] `;���v�[@c�^��D�6�x��e-�K��G4Bg��ч�ʇ(Q'�3��.f���E��&����ָ'ᭌǪ븂'���M�g�fx�s��Ś.�b�b�����u\/�A�ֳֻ�v���� — refworld.org (#8)
- ❌ low_on_target **0.0044** [on_target=0.12 evidence=0.04] ���PYU�� Y%�������4T�Mc�X�0MMS�b���*մ4-UM�ڴV�L�F�����m:�N���f��[ͽ�^U��6�U=���W�� 3H�f�ړ���]&���4���o — microdata.worldbank.org (#6)
- ❌ low_on_target **0.0** [on_target=0.17 evidence=0.00] JavaScript is required... — pubchem.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0** [on_target=0.06 evidence=0.00] CONTENTdm — ojd.contentdm.oclc.org (#3)
- ❌ low_on_target **0.0** [on_target=0.04 evidence=0.00] Issue Information — onlinelibrary.wiley.com (#5)

**q037-3** `IPS-06061 day 28 tumour volume AsPC-1` → kept 1/10, jev 386 ms

- ✅ **0.9089** [on_target=0.95 evidence=0.96] IPS-07004 - 炎症，哮喘，帕金森病_专利 - 新药情报库 - 智慧芽 — synapse.zhihuiya.com (#1) `A`
- ❌ low_evidence **0.0598** [on_target=0.78 evidence=0.08] IPS-06061 / KRAS G12D Degrader / MedChemExpress — medchemexpress.com (#4) `A`
- ❌ low_on_target **0.0343** [on_target=0.49 evidence=0.07] Safety, pharmacokinetics, and antitumor activity of the anti ... — sciencedirect.com (#8)
- ❌ low_evidence **0.0124** [on_target=0.93 evidence=0.01] Delving into the Latest Updates on IPS-06061 with Synapse — synapse.patsnap.com (#5) `A`
- ❌ low_on_target **0.0093** [on_target=0.31 evidence=0.03] Primary day-28 analysis of a phase 2/3 open-label study — sciencedirect.com (#7)
- ❌ low_on_target **0.0066** [on_target=0.22 evidence=0.03] VIVOWeill Cornell Medical College — vivo.weill.cornell.edu (#6)
- ❌ low_on_target **0.0018** [on_target=0.03 evidence=0.06] cell lines aspc-1 — science.gov (#10)
- ❌ low_on_target **0.0012** [on_target=0.04 evidence=0.03] AsPC-1 — pubchem.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0** [on_target=0.04 evidence=0.00] Browse — inplasy.com (#2)
- ❌ low_evidence **0.0** [on_target=0.90 evidence=0.00] CAS 3064065-83-1 IPS-06061 - Alfa Chemistry — alfa-chemistry.com (#3) `A`

**q037-4** `IPS-06061 tumour shrinkage pancreatic cancer xenograft` → kept 3/10, jev 323 ms

- ✅ **0.6499** [on_target=0.97 evidence=0.67] IPS-06061, a novel orally active TPD molecular glue degrader targeting… / Gagan Kukreja / 10 comment — linkedin.com (#1) `A`
- ✅ **0.6338** [on_target=0.98 evidence=0.65] Degradation inducer — bioworld.com (#3) `A`
- ✅ **0.5949** [on_target=0.97 evidence=0.61] Molecular glue degraders - Articles - Page 5 / BioWorld — bioworld.com (#4) `A`
- ❌ low_evidence **0.1686** [on_target=0.92 evidence=0.18] Delving into the Latest Updates on IPS-06061 with Synapse — synapse.patsnap.com (#2) `A`
- ❌ low_on_target **0.0329** [on_target=0.29 evidence=0.11] Implanted Tumor Growth Is Suppressed and Survival Is ... — sciencedirect.com (#8)
- ❌ low_evidence **0.0142** [on_target=0.85 evidence=0.02] IPS-06061 / Molecular Glues / / Invivochem — invivochem.com (#5) `A`
- ❌ low_on_target **0.0118** [on_target=0.06 evidence=0.20] Radioimmunotherapy of pancreatic cancer xenografts in ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.01** [on_target=0.05 evidence=0.20] Combined treatment of pancreatic cancer xenograft with ... — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0058** [on_target=0.25 evidence=0.02] Preclinical characterization and clinical development of ... — sciencedirect.com (#9)
- ❌ low_on_target **0.0051** [on_target=0.03 evidence=0.17] Pancreatic Cancer Xenograft Models — xenograft.org (#7)

**q037-1** `IPS-06061 AsPC-1 xenograft tumour regression` → kept 2/10, jev 388 ms

- ✅ **0.8992** [on_target=0.96 evidence=0.94] IPS-07004 - 炎症，哮喘，帕金森病_专利 - 新药情报库 - 智慧芽 — synapse.zhihuiya.com (#1) `A`
- ✅ **0.6566** [on_target=0.98 evidence=0.67] IPS-06061, a novel orally active TPD molecular glue degrader targeting… / Gagan Kukreja / 10 comment — linkedin.com (#5) `A`
- ❌ low_on_target **0.0338** [on_target=0.39 evidence=0.09] ��Xt�v[�f8W�x�N��O q!���] �0�p*,^�H�ݞ���t�!��Eٳ� �/��߾� �������r����8��<[T��vc��O����w�;W����.�����] — jpccs.jp (#8)
- ❌ low_on_target **0.0187** [on_target=0.33 evidence=0.06] F��,�5��A�^7��G)/���>~:c4��C�^�����j��^G���+A=��!j��0�͌�ԏDqc����1�/] =y�X��R���ރ���e�k�I�+-��y�Z�_�� — dailymed.nlm.nih.gov (#6)
- ❌ low_on_target **0.0181** [on_target=0.34 evidence=0.05] y����e;� x�#1=P ����a!�ʎ"5@0� ����N�۷J�/�V m�$$8��;�%�+,*\�,6Ik�Sy ���T�$`�7���,��G��� w����A��1b��F — dailymed.nlm.nih.gov (#10)
- ❌ low_on_target **0.0155** [on_target=0.29 evidence=0.05] ���9YR�d��ʾ�7E#� ;�Q�(ٚl�V��煋�����D�hg��p����=��\���t���H�!R��Y��i����:���R4�_5?q�N�o�sv�>Y����Ԗg�A� — dailymed.nlm.nih.gov (#9)
- ❌ low_on_target **0.0063** [on_target=0.19 evidence=0.03] �z�/B+�fA��A�� ��Ζ?Q�\�~-�܍��ԟ� �eN%�B��U*��CY,��1ѥ�@mrt��7b�-����@ �t*��"���O��q'���ͲŊ睑�J��8�Zˢ! �k — dailymed.nlm.nih.gov (#7)
- ❌ low_on_target **0.0033** [on_target=0.20 evidence=0.02] Cancer Cell — sciencedirect.com (#3)
- ❌ low_on_target **0.0** [on_target=0.03 evidence=0.00] Cloudflare — aacrjournals.org (#2)
- ❌ low_on_target **0.0** [on_target=0.04 evidence=0.00] Browse — inplasy.com (#4)

## q038 (competitor objective)

**Objective:** KRAS G12D drugs approved against the target and their regulatory approval status  
**Target sent:** drugs competing with ZE980277: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['ZE980277']

**q038-1** `ZE980277 KRAS G12D approval status FDA EMA` → kept 5/10, jev 358 ms

- ✅ **0.837** [on_target=0.86 evidence=0.97] cancer.aestheticsadvisor.com · 2026 · 04KRAS Inhibitors (2026): The Complete Guide to Targeted Thera — cancer.aestheticsadvisor.com (#4)
- ✅ **0.68** [on_target=0.80 evidence=0.85] Investigational KRAS G12D Agents Demonstrate Promising ... - ILCN — ilcn.org (#7)
- ✅ **0.6658** [on_target=0.85 evidence=0.78] Therapeutic inhibition of RAS in non-small cell lung cancer - Frontiers — frontiersin.org (#10)
- ✅ **0.6207** [on_target=0.76 evidence=0.82] Zoldonrasib in Patients With KRAS G12D–Mutant NSCLC ... — ascopost.com (#8)
- ✅ **0.6162** [on_target=0.78 evidence=0.79] KRAS Inhibitor Clinical Trial Landscape, September 2026: 115 ... — datalookout.com (#5)
- ❌ low_on_target **0.5016** [on_target=0.57 evidence=0.88] Our Pipeline - KRAS G12D inhibitor - Genentech — gene.com (#9)
- ❌ low_on_target **0.4717** [on_target=0.58 evidence=0.81] Search Orphan Drug Designations and Approvals - FDA — accessdata.fda.gov (#1)
- ❌ low_on_target **0.2295** [on_target=0.45 evidence=0.51] Ongoing / Cancer Accelerated Approvals — fda.gov (#3)
- ❌ low_on_target **0.0889** [on_target=0.29 evidence=0.31] Oncology (Cancer)/Hematologic Malignancies Approval ... — fda.gov (#2)
- ❌ low_on_target **0.0002** [on_target=0.03 evidence=0.01] Medicines for human use under evaluation — ema.europa.eu (#6)

**q038-3** `ZE980277 KRAS G12D approved therapy status` → kept 5/10, jev 332 ms

- ✅ **0.7517** [on_target=0.82 evidence=0.92] Precision Targeting of KRAS-Mutant Cancers: Beyond G12C ... - PMC — pmc.ncbi.nlm.nih.gov (#4)
- ✅ **0.7452** [on_target=0.81 evidence=0.92] KRAS Inhibitor Clinical Trial Landscape, September 2026: 115 ... — datalookout.com (#3)
- ✅ **0.7014** [on_target=0.80 evidence=0.88] Oral Investigational Agent Zoldonrasib Elicits Objective Responses ... — aacr.org (#1)
- ✅ **0.6748** [on_target=0.84 evidence=0.80] Therapeutic inhibition of RAS in non-small cell lung cancer - Frontiers — frontiersin.org (#2)
- ✅ **0.67** [on_target=0.75 evidence=0.89] An Update on Drugs for KRAS Mutations — letswinpc.org (#6)
- ❌ max_keep **0.6531** [on_target=0.79 evidence=0.83] Potential New Treatment for KRAS-GI2D Lung Cancer Reported in ... — mskcc.org (#9)
- ❌ max_keep **0.6225** [on_target=0.75 evidence=0.83] Zoldonrasib in Patients With KRAS G12D–Mutant NSCLC ... — ascopost.com (#10)
- ❌ low_on_target **0.621** [on_target=0.68 evidence=0.91] Astellas moves KRAS G12D degrader setidegrasib into Phase III lung cancer trial — allsci.com (#8)
- ❌ low_on_target **0.4712** [on_target=0.62 evidence=0.76] KRAS Inhibition in Pancreatic Ductal Adenocarcinoma - PMC - NIH — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0** [on_target=0.26 evidence=0.00] KRAS G12D inhib News — sigma.larvol.com (#5)

**q038-2** `ZE980277 KRAS G12D regulatory approval` → kept 5/10, jev 350 ms

- ✅ **0.7756** [on_target=0.84 evidence=0.92] KRAS Inhibitors Competitive Landscape Analysis 2026 / Eureka — eureka.patsnap.com (#10)
- ✅ **0.7735** [on_target=0.85 evidence=0.91] KRAS Inhibitor Clinical Trial Landscape, September 2026: 115 ... — datalookout.com (#4)
- ✅ **0.71** [on_target=0.75 evidence=0.95] KRAS G12D Inhibitor HRS-4642 — cancerindex.io (#7)
- ✅ **0.6926** [on_target=0.79 evidence=0.88] Oral Investigational Agent Zoldonrasib Elicits Objective Responses ... — aacr.org (#2)
- ✅ **0.688** [on_target=0.80 evidence=0.86] KRAS G12D inhibitor (BeiGene) - Drug Targets, Indications, Patents — synapse.patsnap.com (#5)
- ❌ max_keep **0.6314** [on_target=0.77 evidence=0.82] Investigational KRAS G12D Agents Demonstrate Promising ... - ILCN — ilcn.org (#6)
- ❌ low_on_target **0.4363** [on_target=0.55 evidence=0.79] Our Pipeline - KRAS G12D inhibitor - Genentech — gene.com (#8)
- ❌ low_on_target **0.1512** [on_target=0.63 evidence=0.24] An overview of KRAS G12D inhibitors — pubmed.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.123** [on_target=0.41 evidence=0.30] KRAS G12D Inhibitor Molecule Overview — lillyoncologypipeline.com (#3)
- ❌ low_on_target **0.0** [on_target=0.25 evidence=0.00] KRAS G12D inhib News — sigma.larvol.com (#1)

## q039 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as KPG-818, including Small Molecule and Aiolos CRBN Ikaros therapies  
**Target sent:** drugs competing with KPG-818: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['KPG-818']

**q039-3** `KPG-818 CRBN degrader inflammatory bowel disease` → ABSTAIN, jev 361 ms

- ❌ low_evidence **0.3542** [on_target=0.83 evidence=0.43] Kangpu Biopharmaceuticals to Present Preclinical Efficacy Data of KPG-818 in Crohn's Disease at the  — pharmnews.com (#6) `A`
- ❌ low_evidence **0.3267** [on_target=0.81 evidence=0.40] 研发管线-康朴生物医药官网 — kangpugroup.com (#3) `A`
- ❌ low_on_target **0.306** [on_target=0.68 evidence=0.45] 康朴生物医药将在欧洲克罗恩病和结肠炎组织（ECCO）大会上发布 KPG-818治疗克罗恩病的临床前药效数据 （将申报美国II期临床试验） — kangpugroup.com (#8) `A`
- ❌ low_evidence **0.3003** [on_target=0.77 evidence=0.39] KPG-818 - Drug Targets, Indications, Patents — synapse-patsnap-com.libproxy1.nus.edu.sg (#2) `A`
- ❌ low_on_target **0.2908** [on_target=0.61 evidence=0.48] Multiple Investigational Approaches Show Promise for Lupus — medscape.com (#7) `A`
- ❌ low_evidence **0.2823** [on_target=0.73 evidence=0.39] Kangpu Biopharmaceuticals — biobase.whitefordresearch.com (#5) `A`
- ❌ low_evidence **0.2787** [on_target=0.76 evidence=0.37] KPG-818, a Novel Cereblon (CRBN) Modulator, in Patients with SLE — acrabstracts.org (#9) `A`
- ❌ low_evidence **0.2609** [on_target=0.76 evidence=0.34] Pipeline - Kangpu Biopharmaceuticals — kangpugroup.com (#4) `A`
- ❌ low_on_target **0.2233** [on_target=0.67 evidence=0.33] Epaldeudomide / New Drug Approvals — newdrugapprovals.org (#10) `A`
- ❌ low_on_target **0.187** [on_target=0.66 evidence=0.28] Epaldeudomide - Drug Targets, Indications, Patents - Synapse — synapse.patsnap.com (#1) `A`

**q039-2** `KPG-818 CELMoD IBD clinical pipeline` → kept 1/10, jev 353 ms

- ✅ **0.3674** [on_target=0.73 evidence=0.50] epaldeudomide (KPG-818) / Kangpu Biopharma - Larvol Delta — delta.larvol.com (#5) `A`
- ❌ low_evidence **0.3147** [on_target=0.71 evidence=0.44] Ubiquitin ligase x CRBN - Patsnap Synapse — synapse.patsnap.com (#9) `A`
- ❌ low_evidence **0.3066** [on_target=0.73 evidence=0.42] 康朴生物医药将在欧洲克罗恩病和结肠炎组织（ECCO）大会上发布 KPG-818治疗克罗恩病的临床前药效数据 （将申报美国II期临床试验） — kangpugroup.com (#7) `A`
- ❌ low_evidence **0.2541** [on_target=0.77 evidence=0.33] 研发管线-康朴生物医药官网 — kangpugroup.com (#1) `A`
- ❌ low_evidence **0.2048** [on_target=0.74 evidence=0.28] Pipeline - Kangpu Biopharmaceuticals — kangpugroup.com (#2) `A`
- ❌ low_on_target **0.1953** [on_target=0.58 evidence=0.34] BMS' CELMoD ZENBEXUS Enters the Multiple Myeloma ... — delveinsight.com (#6) `A`
- ❌ low_on_target **0.1456** [on_target=0.59 evidence=0.25] Kangpu Biopharmaceuticals Ltd. - Drug pipelines, Patents, ... — synapse.patsnap.com (#4) `A`
- ❌ low_on_target **0.1315** [on_target=0.58 evidence=0.23] Kangpu to Present Latest Study Results of epaldeudomide ... — biospace.com (#10) `A`
- ❌ low_on_target **0.0855** [on_target=0.57 evidence=0.15] Clinical Trials - KPG-818 - Kangpu Biopharmaceuticals — kangpugroup.com (#3) `A`
- ❌ low_on_target **0.0705** [on_target=0.46 evidence=0.15] Abstract 6367: KPG-818, a novel cereblon modulator, inhibits hematological malignancies in preclinic — aacrjournals.org (#8) `A`

**q039-1** `KPG-818 Aiolos CRBN Ikaros inflammatory bowel disease competitors` → kept 2/10, jev 346 ms

- ✅ **0.4488** [on_target=0.72 evidence=0.62] Targeted therapies in systemic lupus erythematosus — frontiersin.org (#1) `A`
- ✅ **0.4319** [on_target=0.79 evidence=0.55] [PDF] Protocol - ClinicalTrials.gov — cdn.clinicaltrials.gov (#8) `A`
- ❌ low_evidence **0.3206** [on_target=0.74 evidence=0.43] P131 Therapeutic effects of KPG-818 in a trinitrobenzene sulfonic acid - induced mouse Crohn's/Ulcer — academic.oup.com (#5) `A`
- ❌ low_evidence **0.2812** [on_target=0.74 evidence=0.38] Pipeline - Kangpu Biopharmaceuticals — kangpugroup.com (#3) `A`
- ❌ low_evidence **0.2556** [on_target=0.71 evidence=0.36] Abstract 6367: KPG-818, a novel cereblon modulator, inhibits hematological malignancies in preclinic — aacrjournals.org (#4) `A`
- ❌ low_evidence **0.2336** [on_target=0.73 evidence=0.32] "Kpg-818, a novel cereblon (CRBN) modulator, in patients with ... — scholarlycommons.henryford.com (#9) `A`
- ❌ low_on_target **0.1994** [on_target=0.65 evidence=0.31] POS0057 KPG-818, A NOVEL CEREBLON MODULATOR IN PATIENTS WITH SYSTEMIC LUPUS ERYTHEMATOSUS: RESULTS O — ard.bmj.com (#10) `A`
- ❌ low_on_target **0.138** [on_target=0.41 evidence=0.34] Multiple Investigational Approaches Show Promise for Lupus — medscape.com (#2) `A`
- ❌ low_on_target **0.0425** [on_target=0.14 evidence=0.30] Landscape of new drugs and targets in inflammatory bowel disease — onlinelibrary.wiley.com (#6)
- ❌ low_on_target **0.031** [on_target=0.10 evidence=0.31] Medications for Inflammatory Bowel Disease — merckmanuals.com (#7)

## q040 (competitor objective)

**Objective:** Active Ulcerative Colitis Moderate to Severe Ulcerative Colitis competing agents in the same mechanistic class as CHST15 Oligonucleotide Small Interfering RNA therapies  
**Target sent:** drugs competing with GUT-1: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['GUT-1']

**q040-2** `GUT-1 siRNA CHST15 ulcerative colitis` → ABSTAIN, jev 338 ms

- ❌ low_on_target **0.4209** [on_target=0.69 evidence=0.61] Gut Inc. — gut-oligo.com (#2) `A`
- ❌ low_on_target **0.3627** [on_target=0.64 evidence=0.57] Y-ECCO Literature Review: Lushen Pillay — ecco-ibd.eu (#7) `A`
- ❌ low_on_target **0.3531** [on_target=0.65 evidence=0.54] News — gut-oligo.com (#8) `A`
- ❌ low_on_target **0.3276** [on_target=0.63 evidence=0.52] Research and Development - Gut Inc. — gut-oligo.com (#4) `A`
- ❌ low_on_target **0.3258** [on_target=0.54 evidence=0.60] Y-ECCO Literature Review: Lushen Pillay - ECCO - European Crohn’s and Colitis Organisation — ecco-ibd.eu (#6) `A`
- ❌ low_on_target **0.3078** [on_target=0.54 evidence=0.57] Phase 1 Clinical Study of siRNA Targeting Carbohydrate ... — academic.oup.com (#10)
- ❌ low_on_target **0.2919** [on_target=0.63 evidence=0.46] Add-on multiple submucosal injections of the RNA oligonucleotide GUT-1 to anti-TNF antibody treatmen — d-nb.info (#3) `A`
- ❌ low_on_target **0.2754** [on_target=0.59 evidence=0.47] Submucosal Injection of the RNA Oligonucleotide GUT-1 in Active Ulcerative Colitis Patients: A Rando — academic.oup.com (#5) `A`
- ❌ low_on_target **0.2565** [on_target=0.57 evidence=0.45] Submucosal Injection of the RNA Oligonucleotide GUT-1 in Active ... — academic.oup.com (#1) `A`
- ❌ low_on_target **0.0317** [on_target=0.14 evidence=0.23] Identification of Ferro‐Aging‐Related Biomarkers for Ulcerative ... — pmc.ncbi.nlm.nih.gov (#9)

**q040-1** `GUT-1 CHST15 ulcerative colitis competitors` → kept 3/10, jev 372 ms

- ✅ **0.6395** [on_target=0.88 evidence=0.73] Research progress in molecular targeted therapy for inflammatory ... — link.springer.com (#1) `A`
- ✅ **0.582** [on_target=0.90 evidence=0.65] Oligonucleotides—A Novel Promising Therapeutic Option for IBD — pmc.ncbi.nlm.nih.gov (#7)
- ✅ **0.5412** [on_target=0.82 evidence=0.66] Therapeutic Oligonucleotides for Patients with Inflammatory Bowel ... — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.363** [on_target=0.66 evidence=0.55] Research and Development - Gut Inc. — gut-oligo.com (#2) `A`
- ❌ low_on_target **0.2941** [on_target=0.51 evidence=0.58] Articles tagged with: Y-ECCO Literature Review — ecco-ibd.eu (#10) `A`
- ❌ low_on_target **0.2636** [on_target=0.59 evidence=0.45] Submucosal Injection of the RNA Oligonucleotide GUT-1 in Active Ulcerative Colitis Patients: A Rando — academic.oup.com (#9) `A`
- ❌ low_on_target **0.1942** [on_target=0.56 evidence=0.35] Choosing Therapies in Ulcerative Colitis - PMC — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0578** [on_target=0.34 evidence=0.17] Abstract - PMC - NIH — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0288** [on_target=0.12 evidence=0.24] Unveiling the key genes, environmental toxins, and drug exposures in modulating the severity of ulce — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0252** [on_target=0.09 evidence=0.28] Identification of Ferro‐Aging‐Related Biomarkers for Ulcerative ... — pmc.ncbi.nlm.nih.gov (#3)

**q040-3** `GUT-1 CHST15 moderate to severe ulcerative colitis pipeline` → ABSTAIN, jev 393 ms

- ❌ low_on_target **0.4048** [on_target=0.66 evidence=0.61] Y-ECCO Literature Review: Lushen Pillay - ECCO - European Crohn’s and Colitis Organisation — ecco-ibd.eu (#6) `A`
- ❌ low_on_target **0.3861** [on_target=0.64 evidence=0.60] Research progress in molecular targeted therapy for inflammatory ... — pmc.ncbi.nlm.nih.gov (#9) `A`
- ❌ low_on_target **0.3791** [on_target=0.65 evidence=0.58] Gut Inc. — gut-oligo.com (#2) `A`
- ❌ low_on_target **0.3514** [on_target=0.62 evidence=0.57] Y-ECCO Literature Review: Lushen Pillay — ecco-ibd.eu (#7) `A`
- ❌ low_on_target **0.3432** [on_target=0.66 evidence=0.52] Submucosal Injection of the RNA Oligonucleotide GUT-1 in Active ... — academic.oup.com (#10) `A`
- ❌ low_on_target **0.3248** [on_target=0.58 evidence=0.56] News — gut-oligo.com (#8) `A`
- ❌ low_on_target **0.308** [on_target=0.66 evidence=0.47] Add-on multiple submucosal injections of the RNA oligonucleotide GUT-1 to anti-TNF antibody treatmen — inflammregen.biomedcentral.com (#1) `A`
- ❌ low_on_target **0.3036** [on_target=0.66 evidence=0.46] Add-on multiple submucosal injections of the RNA ... - PMC — pmc.ncbi.nlm.nih.gov (#3) `A`
- ❌ low_on_target **0.303** [on_target=0.61 evidence=0.50] Research and Development — gut-oligo.com (#4) `A`
- ❌ low_on_target **0.2881** [on_target=0.67 evidence=0.43] Most popular content — gutflix.eu (#5) `A`

## q041 (competitor objective)

**Objective:** competing agents in the same mechanistic class for this indication DB-3Q, Direct Biologics LLC, Medically Refractory Crohn's Disease  
**Target sent:** drugs competing with DB-3Q: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['DB-3Q']

**q041-1** `DB-3Q MSC-derived extracellular vesicle Crohn's competitors` → ABSTAIN, jev 355 ms

- ❌ low_on_target **0.3145** [on_target=0.51 evidence=0.62] Mesenchymal stem cell-derived extracellular vesicles ... - PMC — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.2757** [on_target=0.47 evidence=0.59] Stem cell- and extracellular vesicle-based therapies for ... — wjgnet.com (#8)
- ❌ low_on_target **0.1994** [on_target=0.65 evidence=0.31] Extracellular vesicle-based drug overview: research ... - PMC — pmc.ncbi.nlm.nih.gov (#4) `A`
- ❌ low_on_target **0.1512** [on_target=0.28 evidence=0.54] The tiny giants of regeneration: MSC-derived extracellular vesicles ... — frontiersin.org (#3)
- ❌ low_on_target **0.091** [on_target=0.21 evidence=0.43] Mesenchymal Stem Cells Derived Extracellular Vesicles in ... — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0612** [on_target=0.17 evidence=0.36] Therapeutic potential of mesenchymal stem cell‐derived ... — onlinelibrary.wiley.com (#9)
- ❌ low_on_target **0.0561** [on_target=0.17 evidence=0.33] Therapeutic potential of mesenchymal stem cell‐derived ... — onlinelibrary.wiley.com (#7)
- ❌ low_on_target **0.0513** [on_target=0.14 evidence=0.37] Frontiers / Extracellular vesicle-based therapies in IBD: immunomodulation, regeneration, and transl — frontiersin.org (#1)
- ❌ low_on_target **0.044** [on_target=0.12 evidence=0.37] Unleashing the potential of extracellular vesicles for ulcerative colitis ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0318** [on_target=0.09 evidence=0.35] Extracellular vesicles for the treatment of ulcerative colitis: A systematic review and meta-analysi — cell.com (#6)

**q041-2** `DB-3Q extracellular vesicle Crohn's disease clinical trials` → ABSTAIN, jev 332 ms

- ❌ low_on_target **0.3328** [on_target=0.62 evidence=0.54] DB-3Q bmMSC-EVs in Patients With Perianal Fistulizing ... — allclinicaltrials.com (#4) `A`
- ❌ low_on_target **0.3182** [on_target=0.62 evidence=0.51] DB-3Q bmMSC-EVs in Patients With Perianal Fistulizing Crohn's Disease — ichgcp.net (#2) `A`
- ❌ low_evidence **0.3115** [on_target=0.73 evidence=0.43] [PDF] Claudia Musat, MD - Columbia Surgery — columbiasurgery.org (#5) `A`
- ❌ low_on_target **0.246** [on_target=0.60 evidence=0.41] DB-3QDB-3Q for the Treatment of Medically Refractory Crohn's Disease — allclinicaltrials.com (#8) `A`
- ❌ low_evidence **0.238** [on_target=0.70 evidence=0.34] Columbia Enrolls Nation's First Patient in Direct Biologics' Phase 2 ... — columbiasurgery.org (#3) `A`
- ❌ low_evidence **0.2344** [on_target=0.74 evidence=0.32] Direct Biologics Clinical Research Programs — linkedin.com (#9) `A`
- ❌ low_on_target **0.173** [on_target=0.59 evidence=0.29] NCT06918808: An ongoing trial by Direct Biologics, LLC — fdaaa.trialstracker.net (#6) `A`
- ❌ low_on_target **0.162** [on_target=0.60 evidence=0.27] Direct Biologics LLC - Drug pipelines, Patents, Clinical trials — synapse.patsnap.com (#7) `A`
- ❌ low_on_target **0.154** [on_target=0.55 evidence=0.28] Study Details / NCT07625293 / ClinicalTrials.gov - ClinicalTrials.gov — clinicaltrials.gov (#1) `A`
- ❌ low_on_target **0.1155** [on_target=0.45 evidence=0.26] Allogeneic Bone Marrow Mesenchymal Stem Cell Derived ... — synapse.patsnap.com (#10) `A`

**q041-3** `DB-3Q MSC-derived EV medically refractory Crohn's` → ABSTAIN, jev 388 ms

- ❌ low_evidence **0.2769** [on_target=0.71 evidence=0.39] Columbia Enrolls Nation's First Patient in Direct Biologics' Phase 2 ... — columbiasurgery.org (#7) `A`
- ❌ low_on_target **0.2652** [on_target=0.52 evidence=0.51] DB-3Q bmMSC-EVs in Patients With Perianal Fistulizing Crohn's Disease — ichgcp.net (#10) `A`
- ❌ low_on_target **0.21** [on_target=0.60 evidence=0.35] Direct Biologics / MTEC — mtec-sc.org (#3) `A`
- ❌ low_on_target **0.1971** [on_target=0.65 evidence=0.30] Direct Biologics, LLC - MedPath Trial — trial.medpath.com (#6) `A`
- ❌ low_on_target **0.1815** [on_target=0.55 evidence=0.33] Allogeneic Bone Marrow Mesenchymal Stem Cell Derived ... — synapse.patsnap.com (#5) `A`
- ❌ low_on_target **0.1662** [on_target=0.56 evidence=0.30] Patients / Direct Biologics — directbiologics.com (#2) `A`
- ❌ low_on_target **0.1613** [on_target=0.55 evidence=0.29] Study Details / NCT07625293 / DB-3Q for the Treatment of ... — clinicaltrials.gov (#1) `A`
- ❌ low_on_target **0.1579** [on_target=0.32 evidence=0.49] Stem cell- and extracellular vesicle-based therapies for ... — wjgnet.com (#9)
- ❌ low_on_target **0.1343** [on_target=0.38 evidence=0.35] Stem Cells for the Treatment of Pouchitis — med.agiltrace.com (#4) `A`
- ❌ low_on_target **0.1029** [on_target=0.21 evidence=0.49] Extracellular vesicle-based therapies in IBD - Frontiers — frontiersin.org (#8)

## q042 (competitor objective)

**Objective:** Moderately to Severely Active Ulcerative Colitis, Duration 3 Months, Modified Mayo Score 5 to 9, With Inadequate Response, Loss of Response, or Intolerance to Prior Standard-of-Care Medications competing agents in the same mechanistic class as TYK2 Small Molecule  
**Target sent:** drugs competing with D-2570: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['D-2570']

**q042-1** `D-2570 TYK2 ulcerative colitis competitor Phase 2 status` → kept 4/10, jev 349 ms

- ✅ **0.7569** [on_target=0.95 evidence=0.80] Emerging Therapies for Ulcerative Colitis: Updates from Recent ... — pmc.ncbi.nlm.nih.gov (#9)
- ✅ **0.752** [on_target=0.94 evidence=0.80] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.6686** [on_target=0.92 evidence=0.73] Interleukin-23p19 Inhibitors in Inflammatory Bowel Disease — pmc.ncbi.nlm.nih.gov (#7)
- ✅ **0.637** [on_target=0.91 evidence=0.70] Top 7 Leading Drug Candidates in Ulcerative Colitis Treatment — delveinsight.com (#4)
- ❌ low_on_target **0.2969** [on_target=0.61 evidence=0.49] Advancing therapeutic frontiers: a pipeline of novel drugs ... — frontiersin.org (#1) `A`
- ❌ low_on_target **0.2223** [on_target=0.57 evidence=0.39] Yifang Bio-U (688382) 2026 H1 Report Commentary: Multiple Core Pipeline Programs Show Strong Progres — news.futunn.com (#5) `A`
- ❌ low_on_target **0.2105** [on_target=0.59 evidence=0.36] A Study on the Safety of TAK-279 and Whether it Can Reduce Inflammation in the Bowel of Participants — med.agiltrace.com (#8) `A`
- ❌ low_on_target **0.19** [on_target=0.57 evidence=0.33] The Efficacy of Hyperbaric Oxygen-assisted Treatment for ASUC and Refractory IBD — med.agiltrace.com (#10) `A`
- ❌ low_on_target **0.176** [on_target=0.55 evidence=0.32] SUMMARY — www1.hkexnews.hk (#3) `A`
- ❌ low_on_target **0.1474** [on_target=0.56 evidence=0.26] Study Evaluating ISM5411 Administered Orally to Subjects With Active Ulcerative Colitis (BETHESDA) — med.agiltrace.com (#6) `A`

## q043 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as VNN1, including Small Molecule therapies  
**Target sent:** drugs competing with MY009: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['MY009']

**q043-1** `MY009 VNN1 inflammatory bowel disease competing agents` → kept 1/10, jev 410 ms

- ✅ **0.4004** [on_target=0.77 evidence=0.52] MY-009212A - Drug Targets, Indications, Patents — synapse.patsnap.com (#9) `A`
- ❌ low_on_target **0.3615** [on_target=0.58 evidence=0.62] Revealing VNN1: An Emerging and Promising Target ... — mendeley.com (#8)
- ❌ low_on_target **0.3108** [on_target=0.63 evidence=0.49] The Present and Future of Inflammatory Bowel Disease ... - PMC — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.2527** [on_target=0.57 evidence=0.44] Current status of novel biologics and small molecule drugs ... — wjgnet.com (#2)
- ❌ low_on_target **0.2438** [on_target=0.59 evidence=0.41] Inflammatory Bowel Disease: Understanding Therapeutic Effects of ... — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.198** [on_target=0.44 evidence=0.45] Methods and pharmaceutical compositions for repairing intestinal ... — patents.google.com (#3)
- ❌ low_on_target **0.1599** [on_target=0.44 evidence=0.36] Landscape of new drugs and targets in inflammatory bowel disease — onlinelibrary.wiley.com (#4)
- ❌ low_on_target **0.0728** [on_target=0.23 evidence=0.32] Inflammatory Bowel Disease Biomarkers - PMC - NIH — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0614** [on_target=0.19 evidence=0.32] VNN1 Gene: Vanin 1 - Function, Mutations, and Disease ... — editxor.com (#10)
- ❌ low_on_target **0.0026** [on_target=0.13 evidence=0.02] Targeting the Unmet Needs in IBD: Emerging Therapies Beyond ... — sciencedirect.com (#5)

## q044 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as GPR52 Prostaglandin E2 Receptor EP4, including Small Molecule therapies  
**Target sent:** drugs competing with NXE0033744 / NXE744: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['NXE0033744', 'NXE744']

**q044-1** `NXE0033744 Phase 2 inflammatory bowel disease` → kept 2/10, jev 359 ms

- ✅ **0.6043** [on_target=0.88 evidence=0.69] Post procedural inflammation - Drugs, Targets, Patents - Synapse — synapse.patsnap.com (#2) `A`
- ✅ **0.4108** [on_target=0.79 evidence=0.52] NXE0033744 / Nxera Pharma - LARVOL DELTA — delta.larvol.com (#7) `A`
- ❌ low_evidence **0.3388** [on_target=0.77 evidence=0.44] Full Company Profile — stockanalysis.com (#4) `A`
- ❌ low_evidence **0.3058** [on_target=0.74 evidence=0.41] Nxera Pharma (TSE:4565) Stock Price - Simply Wall St — simplywall.st (#5) `A`
- ❌ low_evidence **0.2982** [on_target=0.71 evidence=0.42] 4565 / Nxera Pharma Co Ltd Share Price - Investing.com NG — ng.investing.com (#3) `A`
- ❌ low_evidence **0.2533** [on_target=0.76 evidence=0.33] Pipeline — nxera.life (#1) `A`
- ❌ low_on_target **0.1419** [on_target=0.38 evidence=0.37] Deucravacitinib in patients with inflammatory bowel disease - PubMed — pubmed.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.089** [on_target=0.30 evidence=0.30] new drugs for inflammatory bowel disease treatment ... — pubmed.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0155** [on_target=0.08 evidence=0.19] inflammatory bowel disease - MGeND — mgend.jihs.go.jp (#8)
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] Trial Review — anzctr.org.au (#6)

**q044-3** `NXE0033744 development stage IBD` → kept 5/10, jev 332 ms

- ✅ **0.5867** [on_target=0.88 evidence=0.67] Post procedural inflammation - Drugs, Targets, Patents - Synapse — synapse.patsnap.com (#8) `A`
- ✅ **0.5139** [on_target=0.82 evidence=0.63] Presentation title - investors.nxera.life — investors.nxera.life (#1) `A`
- ✅ **0.4536** [on_target=0.81 evidence=0.56] Annual Report - investors.nxera.life — investors.nxera.life (#3) `A`
- ❌ low_evidence **0.4018** [on_target=0.82 evidence=0.49] Nxera Pharma Operational Highlights and Consolidated ... — biospace.com (#5) `A`
- ✅ **0.395** [on_target=0.79 evidence=0.50] アニュアルレポート — investors.nxera.life (#2) `A`
- ✅ **0.395** [on_target=0.79 evidence=0.50] Corporate Presentation - October 2025 - Investors — investors.nxera.life (#4) `A`
- ❌ low_evidence **0.3547** [on_target=0.76 evidence=0.47] Nxera Pharma : Consolidated Financial Results for the FY2024 (IFRS) — marketscreener.com (#10) `A`
- ❌ low_evidence **0.3268** [on_target=0.76 evidence=0.43] Nxera Pharma : Consolidated Financial Results for the Nine months Ended September 30, 2024 (IFRS) — marketscreener.com (#9) `A`
- ❌ low_evidence **0.3265** [on_target=0.79 evidence=0.41] Nxera Pharma Operational Highlights and Consolidated Results for ... — samedanltd.com (#7) `A`
- ❌ low_on_target **0.2748** [on_target=0.62 evidence=0.44] GSK-4381406(GSK-4381406) - 药物靶点：GPR35_在研适应症 ... — synapse.zhihuiya.com (#6) `A`

**q044-2** `NXE0033744 EP4 agonist clinical trial` → kept 4/10, jev 331 ms

- ✅ **0.4694** [on_target=0.80 evidence=0.59] NXE0033744 / Nxera Pharma - LARVOL DELTA — delta.larvol.com (#9) `A`
- ✅ **0.4477** [on_target=0.85 evidence=0.53] [PDF] Presentation title - Nxera Pharma — investors.nxera.life (#7) `A`
- ✅ **0.4291** [on_target=0.82 evidence=0.52] Nxera Pharma : Annual Report Year ended 31 December 2024 — marketscreener.com (#5) `A`
- ✅ **0.3875** [on_target=0.77 evidence=0.50] Consolidated Financial Results for the Nine months Ended September 30, 2024 — finance.stockweather.co.jp (#4) `A`
- ❌ low_evidence **0.376** [on_target=0.80 evidence=0.47] [PDF] Corporate Presentation - Investors - Nxera Pharma — investors.nxera.life (#8) `A`
- ❌ low_evidence **0.3692** [on_target=0.78 evidence=0.47] [PDF] R&D Day - Investors - Nxera Pharma — investors.nxera.life (#1) `A`
- ❌ low_evidence **0.3564** [on_target=0.81 evidence=0.44] Nxera Pharma Operational Highlights and Consolidated Results for ... — biospace.com (#6) `A`
- ❌ low_evidence **0.344** [on_target=0.80 evidence=0.43] Nxera Pharma Operational Highlights and Consolidated ... — biospace.com (#3) `A`
- ❌ low_on_target **0.2426** [on_target=0.68 evidence=0.36] [PDF] Environment, Social & Governance Report - Investors — investors.nxera.life (#2) `A`
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] Clinical Trials Round-Up: March and April 2026 — pharmaphorum.com (#10)

**q044-4** `NXE744 EP4 agonist competitors IBD` → kept 5/10, jev 417 ms

- ✅ **0.642** [on_target=0.90 evidence=0.71] The update of prostaglandin E2 receptor subtype 4 (EP4) in ... — pmc.ncbi.nlm.nih.gov (#2)
- ✅ **0.606** [on_target=0.90 evidence=0.67] Earnings call transcript: Nxera Pharma Q4 2025 shows ... — investing.com (#7) `A`
- ✅ **0.5771** [on_target=0.87 evidence=0.66] The prevention of colitis by E Prostanoid receptor 4 agonist through enhancement of epithelium survi — pubmed.ncbi.nlm.nih.gov (#8)
- ✅ **0.5348** [on_target=0.84 evidence=0.64] Discovery of NXT-10796, an orally active, intestinally restricted EP4 ... — pubmed.ncbi.nlm.nih.gov (#10)
- ✅ **0.5265** [on_target=0.81 evidence=0.65] EP4 receptor: GPCR with multiple therapeutic Opportunities — investors.nxera.life (#3)
- ❌ max_keep **0.4752** [on_target=0.81 evidence=0.59] Discovery of Non-prostanoid EP4 Agonists for the ... - PubMed — pubmed.ncbi.nlm.nih.gov (#4)
- ❌ max_keep **0.4505** [on_target=0.85 evidence=0.53] Inflammatory Bowel Disease Therapy Area Landscape — mpadvisor.com (#1) `A`
- ❌ max_keep **0.432** [on_target=0.80 evidence=0.54] [PDF] Presentation title - Investors - Nxera Pharma — investors.nxera.life (#5) `A`
- ❌ max_keep **0.424** [on_target=0.79 evidence=0.54] Jefferies Global Healthcare Conference 2026 summary — quartr.com (#6) `A`
- ❌ low_on_target **0.0225** [on_target=0.13 evidence=0.17] Landscape of new drugs and targets in inflammatory bowel disease — onlinelibrary.wiley.com (#9)

## q045

**Objective:** BMF-500 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** BMF-500 · anchors ['BMF-500']

**q045-2** `BMF-500 expected regulatory approval AML` → kept 5/10, jev 485 ms

- ✅ **0.9146** [on_target=0.98 evidence=0.93] BMF-500(BMF-500) - 药物靶点：FLT3_在研适应症：急性髓性白血病 ... — synapse.zhihuiya.com (#2) `A`
- ✅ **0.9114** [on_target=0.98 evidence=0.93] Biomea Fusion (BMEA) FDA Approvals — marketbeat.com (#7) `A`
- ✅ **0.869** [on_target=0.98 evidence=0.89] BMF-500 - Drug Targets, Indications, Patents — synapse-patsnap-com.libproxy1.nus.edu.sg (#1) `A`
- ✅ **0.7857** [on_target=0.97 evidence=0.81] Biomea Fusion, Inc. — synapse.patsnap.com (#4) `A`
- ✅ **0.768** [on_target=0.96 evidence=0.80] BIOMEA FUSION, INC. Management's Discussion and Analysis of Financial Condition and Results of Opera — marketscreener.com (#10) `A`
- ❌ max_keep **0.721** [on_target=0.97 evidence=0.74] 10-K — sec.gov (#5) `A`
- ❌ max_keep **0.6646** [on_target=0.89 evidence=0.75] 10-K - SEC.gov — sec.gov (#3) `A`
- ❌ max_keep **0.6048** [on_target=0.96 evidence=0.63] BMF-500 / Biomea Fusion - LARVOL DELTA — delta.larvol.com (#8) `A`
- ❌ low_evidence **0.3466** [on_target=0.92 evidence=0.38] BMF-500, a Potential Best-in-Class Oral Covalent Inhibitor of ... — investors.biomeafusion.com (#6) `A`
- ❌ low_on_target **0.0986** [on_target=0.51 evidence=0.19] BMEA: Biomea Fusion Inc Latest Stock Price, Analysis ... — stocktwits.com (#9)

**q045-1** `BMF-500 first regulatory approval AML` → kept 5/10, jev 376 ms

- ✅ **0.895** [on_target=0.98 evidence=0.91] BMF-500(BMF-500) - 药物靶点：FLT3_在研适应症：急性髓性白血病 ... — synapse.zhihuiya.com (#1) `A`
- ✅ **0.8859** [on_target=0.97 evidence=0.91] Biomea Fusion (BMEA) FDA Approvals, PDUFA Dates & Drug Alerts 2025 — marketbeat.com (#9) `A`
- ✅ **0.8134** [on_target=0.98 evidence=0.83] BMEA_10K_2024_V3 high res.pdf — investors.biomeafusion.com (#8) `A`
- ✅ **0.8134** [on_target=0.98 evidence=0.83] 6b6182a8-cf1d-41de-8ea5-3be7003552a3 — investors.biomeafusion.com (#10) `A`
- ✅ **0.8051** [on_target=0.97 evidence=0.83] EX-99.1 — sec.gov (#3) `A`
- ❌ max_keep **0.7825** [on_target=0.97 evidence=0.81] BMF-500 - Drug Targets, Indications, Patents — synapse.patsnap.com (#2) `A`
- ❌ max_keep **0.7695** [on_target=0.97 evidence=0.79] Biomea Fusion, Inc. — synapse.patsnap.com (#5) `A`
- ❌ max_keep **0.7648** [on_target=0.96 evidence=0.80] BIOMEA FUSION, INC. Management's Discussion and Analysis of Financial Condition and Results of Opera — marketscreener.com (#7) `A`
- ❌ max_keep **0.7616** [on_target=0.96 evidence=0.79] Biomea Fusion, Inc. (NASDAQ:BMEA): Transforming the Diabetes and Obesity Landscape — beyondspx.com (#6) `A`
- ❌ max_keep **0.7469** [on_target=0.97 evidence=0.77] 10-K — sec.gov (#4) `A`

**q045-4** `BMF-500 expected launch date AML` → kept 5/10, jev 468 ms

- ✅ **0.8526** [on_target=0.98 evidence=0.87] BMF-500(BMF-500) - 药物靶点：FLT3_在研适应症：急性髓性白血病 ... — synapse.zhihuiya.com (#2) `A`
- ✅ **0.7728** [on_target=0.97 evidence=0.80] [PDF] Covalent FLT3 Inhibitor BMF-500 in Relapsed or Refractory (R/R ... — investors.biomeafusion.com (#10) `A`
- ✅ **0.7644** [on_target=0.98 evidence=0.78] BMF-500 - Drug Targets, Indications, Patents — synapse.patsnap.com (#1) `A`
- ✅ **0.7016** [on_target=0.97 evidence=0.72] A Phase 1, Study of BMF-500 in Adults With Acute Leukemia - Clinical Trial for Acute Myeloid Leukemi — trials.co (#5) `A`
- ✅ **0.6919** [on_target=0.97 evidence=0.71] BMF-500 / Biomea Fusion - LARVOL DELTA — delta.larvol.com (#3) `A`
- ❌ max_keep **0.6828** [on_target=0.98 evidence=0.70] Biomea Fusion Reports Second Quarter 2025 Financial ... — investors.biomeafusion.com (#4) `A`
- ❌ max_keep **0.5376** [on_target=0.96 evidence=0.56] Biomea Fusion to Present Preclinical Data for BMF-500, an ... — investors.biomeafusion.com (#6) `A`
- ❌ low_evidence **0.339** [on_target=0.90 evidence=0.38] A Phase 1, Study of BMF-500 in Adults With Acute Leukemia — georgiacancerinfo.org (#8) `A`
- ❌ low_on_target **0.2301** [on_target=0.58 evidence=0.40] BMEA: Biomea Fusion Inc Latest Stock Price, Analysis ... — stocktwits.com (#7)
- ❌ low_evidence **0.0121** [on_target=0.91 evidence=0.01] BMF-500 — vjhemonc.com (#9) `A`

**q045-3** `BMF-500 market launch AML` → kept 5/10, jev 477 ms

- ✅ **0.9278** [on_target=0.98 evidence=0.95] BMF-500(BMF-500) - 药物靶点：FLT3_在研适应症：急性髓性白血病 ... — synapse.zhihuiya.com (#2) `A`
- ✅ **0.8788** [on_target=0.98 evidence=0.90] BMF-500 - Drug Targets, Indications, Patents — synapse.patsnap.com (#1) `A`
- ✅ **0.8374** [on_target=0.97 evidence=0.86] NASDAQ_BMEA_2022.pdf — annualreports.com (#4) `A`
- ✅ **0.8134** [on_target=0.98 evidence=0.83] Biomea Fusion / Oncology / Drug Developments — pharmacompass.com (#5) `A`
- ✅ **0.8102** [on_target=0.98 evidence=0.83] Form 8-K for Biomea Fusion INC filed 05/02/2023 — investors.biomeafusion.com (#3) `A`
- ❌ max_keep **0.7825** [on_target=0.97 evidence=0.81] Biomea Fusion Announces First Patient Dosed with Covalent FLT3 ... — investors.biomeafusion.com (#10) `A`
- ❌ max_keep **0.7808** [on_target=0.98 evidence=0.80] PowerPoint Presentation — investors.biomeafusion.com (#9) `A`
- ❌ max_keep **0.7318** [on_target=0.98 evidence=0.75] Upcoming Catalyst - BioPharmaWatch — biopharmawatch.com (#6) `A`
- ❌ max_keep **0.6919** [on_target=0.97 evidence=0.71] [PDF] Form 8-K for Biomea Fusion INC filed 12/13/2022 — investors.biomeafusion.com (#7) `A`
- ❌ max_keep **0.5949** [on_target=0.97 evidence=0.61] Bmf-500: An Orally Bioavailable Covalent Inhibitor of FLT3 with High Selectivity and Potent Antileuk — ashpublications.org (#8) `A`

## q046

**Objective:** BW-101 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** BW-101 · anchors ['BW-101']

**q046-1** `BW-101 AML regulatory approval market launch year` → kept 1/10, jev 357 ms

- ✅ **0.8524** [on_target=0.91 evidence=0.94] Delving into the Latest Updates on BW-101 with Synapse — synapse.patsnap.com (#1) `A`
- ❌ low_on_target **0.155** [on_target=0.31 evidence=0.50] Acute Myeloid Leukemia Market Summary — delveinsight.com (#10)
- ❌ low_on_target **0.017** [on_target=0.34 evidence=0.05] NCI Drug Dictionary — cancer.gov (#8)
- ❌ low_on_target **0.0042** [on_target=0.42 evidence=0.01] Pipeline - BeOne Medical Affairs / Global — beonemedaffairs.com (#4)
- ❌ low_on_target **0.0028** [on_target=0.28 evidence=0.01] MeSH Linked Data — id.nlm.nih.gov (#5)
- ❌ low_on_target **0.0006** [on_target=0.03 evidence=0.02] Regulatory timeline - OnCo — onco.cc (#7)
- ❌ low_on_target **0.0002** [on_target=0.05 evidence=0.00] NDA and BLA Approvals — fda.gov (#2)
- ❌ low_on_target **0.0** [on_target=0.18 evidence=0.00] JavaScript is required... — pubchem.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0** [on_target=0.37 evidence=0.00] Disclaimer — bioinvent.se (#6)
- ❌ low_on_target **0.0** [on_target=0.02 evidence=0.00] ANNUAL REPORT - nbfira.org.bw — nbfira.org.bw (#9)

## q047

**Objective:** Dual CDK12/13 Inhibitor first regulatory approval or market launch year for acute myeloid leukemia  
**Target sent:** Dual CDK12/13 Inhibitor / CDK12 · anchors ['Dual CDK12/13 Inhibitor', 'CDK12']

**q047-1** `Dual CDK12/13 Inhibitor Insilico Medicine AML approval launch` → kept 5/10, jev 363 ms

- ✅ **0.5945** [on_target=0.91 evidence=0.65] CDK12/13 — insilico.com (#2) `A`
- ✅ **0.5848** [on_target=0.86 evidence=0.68] JMC｜With generative AI assistance, Insilico Medicine ... — eurekalert.org (#7) `A`
- ✅ **0.536** [on_target=0.86 evidence=0.62] Press Releases — insilico.com (#1) `A`
- ✅ **0.51** [on_target=0.85 evidence=0.60] Insilico Medicine's Post - LinkedIn — linkedin.com (#10) `A`
- ✅ **0.5057** [on_target=0.82 evidence=0.62] Insilico Medicine — siliconvalleyinvestclub.com (#3) `A`
- ❌ max_keep **0.4611** [on_target=0.76 evidence=0.61] Insilico Medicine News — sigma.larvol.com (#8) `A`
- ❌ max_keep **0.4337** [on_target=0.77 evidence=0.56] Design, Synthesis, and Biological Evaluation of Novel Orally ... — colab.ws (#6) `A`
- ❌ low_evidence **0.2318** [on_target=0.74 evidence=0.31] Pipeline / Insilico Medicine — insilico.com (#4) `A`
- ❌ low_on_target **0.1748** [on_target=0.69 evidence=0.25] Insilico Medicine: Main — insilico.com (#5) `A`
- ❌ low_on_target **0.0007** [on_target=0.05 evidence=0.01] Media Kit — insilico.com (#9)

**q047-3** `Dual CDK12/13 Inhibitor AML first market launch year` → kept 5/10, jev 543 ms

- ✅ **0.6219** [on_target=0.88 evidence=0.71] CDK12 Inhibitor Pipeline 2025: Key Companies, MOA, ROA, — openpr.com (#2) `A`
- ✅ **0.5578** [on_target=0.89 evidence=0.63] CDK12 Inhibitor- Pipeline Insight, 2025 — researchandmarkets.com (#3) `A`
- ✅ **0.5135** [on_target=0.79 evidence=0.65] Novel CDK12/13 dual inhibitors for tumour treatment - ecancer — ecancer.org (#4) `A`
- ✅ **0.4536** [on_target=0.72 evidence=0.63] link.springer.com · content · pdfCDK12 and CDK13 in oncology: from RNA regulation to ... -... — link.springer.com (#10) `A`
- ✅ **0.45** [on_target=0.90 evidence=0.50] Pipeline :: Carrick Therapeutics, Inc. — carricktherapeutics.com (#9) `A`
- ❌ max_keep **0.44** [on_target=0.75 evidence=0.59] Design, Synthesis, and Biological Evaluation of Novel ... — pubmed.ncbi.nlm.nih.gov (#6) `A`
- ❌ low_on_target **0.3355** [on_target=0.61 evidence=0.55] Degradation of Cyclin-Dependent Kinase - Who we serve — thieme-connect.com (#7) `A`
- ❌ low_evidence **0.321** [on_target=0.83 evidence=0.39] Posters & Publications — carricktherapeutics.com (#1) `A`
- ❌ low_on_target **0.2908** [on_target=0.61 evidence=0.48] Table 1. — pmc.ncbi.nlm.nih.gov (#8) `A`
- ❌ low_on_target **0.0044** [on_target=0.33 evidence=0.01] History of the discovery, development, and FDA-approval of ... — sciencedirect.com (#5)

**q047-2** `Dual CDK12/13 Inhibitor Insilico Medicine AML regulatory timeline` → kept 5/10, jev 833 ms

- ✅ **0.6886** [on_target=0.91 evidence=0.76] CDK12/CDK13 inhibitors(Insilico Medicine Shanghai) — synapse.patsnap.com (#6) `A`
- ✅ **0.6757** [on_target=0.87 evidence=0.78] CDK12/13 TARGET therapy (InSilico Medicine) - Patsnap Synapse — synapse.patsnap.com (#4) `A`
- ✅ **0.6483** [on_target=0.88 evidence=0.74] Insilico Medicine nominates novel CDK12/13 small ... — eurekalert.org (#10) `A`
- ✅ **0.636** [on_target=0.90 evidence=0.71] インシリコ・メディシン、生成AI技術を活用し腫瘍治療のための新規CDK12/13デュアル阻害剤を発表 — sciencesources.eurekalert.org (#7) `A`
- ✅ **0.591** [on_target=0.90 evidence=0.66] CDK12/13 — insilico.com (#1) `A`
- ❌ max_keep **0.588** [on_target=0.84 evidence=0.70] Novel CDK12/13 dual inhibitors for tumour treatment - ecancer — ecancer.org (#8) `A`
- ❌ max_keep **0.536** [on_target=0.86 evidence=0.62] Press Releases — insilico.com (#3) `A`
- ❌ max_keep **0.41** [on_target=0.75 evidence=0.55] Design, Synthesis, and Biological Evaluation of Novel Orally Available Covalent CDK12/13 Dual Inhibi — pubs.acs.org (#9) `A`
- ❌ low_evidence **0.2208** [on_target=0.77 evidence=0.29] Pipeline / Insilico Medicine — insilico.com (#2) `A`
- ❌ low_evidence **0.175** [on_target=0.70 evidence=0.25] Insilico Medicine: Main — insilico.com (#5) `A`

## q048

**Objective:** dCASP1-55 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** dCASP1-55 · anchors ['dCASP1-55']

**q048-1** `dCASP1-55 AML regulatory approval` → ABSTAIN, jev 428 ms

- ❌ low_on_target **0.0081** [on_target=0.22 evidence=0.04] CLINICAL TRIALS — amgentrials.com (#4)
- ❌ low_on_target **0.008** [on_target=0.16 evidence=0.05] ����-S�WJ6���X�^X�e�7/0s��b��]�ĺ-5-����1�h�V����h7/i��u\�}/��cK��=^��G]o���X��d���:��VG/O��M���<ߘ�߹� — dailymed.nlm.nih.gov (#9)
- ❌ low_on_target **0.0065** [on_target=0.15 evidence=0.04] ���+—���oA�e37 ����]��e��a%j��_" �e6�:�������Q��)��� ��xHV8�.x!���T�\� kO���㰘��̛;�D�Q�Ps��(=2 �!)[�� — dailymed.nlm.nih.gov (#6)
- ❌ low_on_target **0.0037** [on_target=0.11 evidence=0.03] ��x���mE��8�Y"�ɒ^�����QrW��0.�7�*�4�2� ���J��w�in�QM����!���c,��0��/���2^�P���x�ߖ73�� ��y.�]���4ي� i — dailymed.nlm.nih.gov (#3)
- ❌ low_on_target **0.0037** [on_target=0.14 evidence=0.03] HO�]7�,ew�,#����m�S�U9��D�蛞���D�/��N�"��gC[z{�����~���K���!��\h�(]܉u��/�i��η�}U����4�l�./�8�O�t���nŌ — dailymed.nlm.nih.gov (#5)
- ❌ low_on_target **0.0005** [on_target=0.15 evidence=0.00] Press Release-CStone Pharmaceuticals — cstonepharma.com (#1)
- ❌ low_on_target **0.0003** [on_target=0.09 evidence=0.00] Page Not Found — mayo.edu (#8)
- ❌ low_on_target **0.0001** [on_target=0.02 evidence=0.00] AML Intelligence — amlintelligence.com (#10)
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] Bank Secrecy Act / Anti-Money Laundering (BSA/AML) — fdic.gov (#2)
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] The Bank Secrecy Act — fincen.gov (#7)

**q048-3** `dCASP1-55 University of Cincinnati AML clinical development` → ABSTAIN, jev 331 ms

- ❌ low_on_target **0.418** [on_target=0.57 evidence=0.73] Multi-institutional team awarded NCI grant to open novel AML ... — cancer.osu.edu (#8)
- ❌ low_on_target **0.2079** [on_target=0.33 evidence=0.63] AML, sickle cell disease research among highlights of ASH abstracts — uc.edu (#2)
- ❌ low_on_target **0.1008** [on_target=0.63 evidence=0.16] A Ph 1B Study of the Anti-Cancer Stem Cell Agent ... — sciencedirect.com (#9)
- ❌ low_on_target **0.0131** [on_target=0.28 evidence=0.05] CLINICAL TRIALS — amgentrials.com (#5)
- ❌ low_on_target **0.008** [on_target=0.04 evidence=0.20] UC hematology experts present research at national conference — uc.edu (#4)
- ❌ low_on_target **0.0069** [on_target=0.23 evidence=0.03] CLINICAL TRIALS — amgentrials.com (#7)
- ❌ low_on_target **0.0055** [on_target=0.15 evidence=0.04] Acute Myeloid Leukemia AML-111: Updated Results and ... — sciencedirect.com (#10)
- ❌ low_on_target **0.002** [on_target=0.10 evidence=0.02] guce — finance.yahoo.com (#6)
- ❌ low_on_target **0.0006** [on_target=0.02 evidence=0.03] Clinical Trials - College of Medicine - University of Cincinnati — med.uc.edu (#3)
- ❌ low_on_target **0.0** [on_target=0.23 evidence=0.00] Internal Server Error — cdas.cancer.gov (#1)

**q048-2** `dCASP1-55 AML market launch` → ABSTAIN, jev 550 ms

- ❌ low_on_target **0.0587** [on_target=0.44 evidence=0.13] Nuance Pharma announces the completion of dosing ... — nuancepharma.com (#7)
- ❌ low_on_target **0.0073** [on_target=0.10 evidence=0.07] Trials / AML - AML Hub — aml-hub.com (#10)
- ❌ low_on_target **0.0067** [on_target=0.20 evidence=0.03] Cancer Discovery — x.com (#4)
- ❌ low_on_target **0.0053** [on_target=0.16 evidence=0.03] guce — finance.yahoo.com (#8)
- ❌ low_on_target **0.0018** [on_target=0.02 evidence=0.09] Acute Myeloid Leukemia Treatment Market Size, Drugs, Trends — delveinsight.com (#6)
- ❌ low_on_target **0.0017** [on_target=0.17 evidence=0.01] Press Release-CStone Pharmaceuticals — cstonepharma.com (#1)
- ❌ low_on_target **0.0001** [on_target=0.02 evidence=0.00] Search / AML Hub — aml-hub.com (#2)
- ❌ low_on_target **0.0001** [on_target=0.02 evidence=0.01] AML Intelligence — amlintelligence.com (#5)
- ❌ low_on_target **0.0** [on_target=0.08 evidence=0.00] Circulars & Announcements-CStone Pharmaceuticals — cstonepharma.com (#3)
- ❌ low_on_target **0.0** [on_target=0.02 evidence=0.00] Regtech / KYC / AML market intelligence — windsordrake.com (#9)

## q049

**Objective:** ABSK131 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in MTAP-Deleted KRAS G12D-Mutated Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** ABSK131 · anchors ['ABSK131']

**q049-1** `ABSK131 SU.86.86 monotherapy TGI` → kept 5/10, jev 504 ms

- ✅ **0.6598** [on_target=0.98 evidence=0.67] ABSK131 / Abbisko - LARVOL DELTA — delta.larvol.com (#2) `A`
- ✅ **0.6598** [on_target=0.98 evidence=0.67] 1 — www1.hkexnews.hk (#3) `A`
- ✅ **0.6596** [on_target=0.97 evidence=0.68] 2025 AACR / Abbisko Therapeutics Presents Late ... — prnewswire.com (#8) `A`
- ✅ **0.6596** [on_target=0.97 evidence=0.68] ABSK-131 - Drug Targets, Indications, Patents — synapse.patsnap.com (#10) `A`
- ✅ **0.6534** [on_target=0.98 evidence=0.67] AACR 2026 / Abbisko Therapeutics Showcases Six Research ... — prnewswire.com (#5) `A`
- ❌ max_keep **0.6467** [on_target=0.97 evidence=0.67] Abbisko Therapeutics präsentiert sechs Forschungsfortschritte zu ... — de.marketscreener.com (#9) `A`
- ❌ max_keep **0.5982** [on_target=0.97 evidence=0.62] [PDF] Abbisko Cayman Limited 和譽開曼有限責任公司 - HKEXnews — www1.hkexnews.hk (#1) `A`
- ❌ max_keep **0.5472** [on_target=0.96 evidence=0.57] [PDF] Abbisko Cayman Limited 和譽開曼有限責任公司 - Moomoo — newsfile.moomoo.com (#4) `A`
- ❌ max_keep **0.4988** [on_target=0.86 evidence=0.58] pan-KRAS Inhibitor(Hengrui Pharmaceutical) - Synapse — synapse-patsnap-com.libproxy1.nus.edu.sg (#6) `A`
- ❌ max_keep **0.472** [on_target=0.80 evidence=0.59] 免费的新药情报数据库- 药品查询 - 智慧芽 — synapse.zhihuiya.com (#7)

**q049-2** `ABSK131 PDAC xenograft monotherapy tumour regression` → kept 5/10, jev 383 ms

- ✅ **0.6958** [on_target=0.98 evidence=0.71] Abbisko Therapeutics - 上海和誉生物医药科技有限公司 — abbisko.com (#2) `A`
- ✅ **0.6598** [on_target=0.98 evidence=0.67] IDE397 / Ideaya Biosci - LARVOL DELTA — delta.larvol.com (#4) `A`
- ✅ **0.6596** [on_target=0.97 evidence=0.68] Delving into the Latest Updates on ABSK-131 with Synapse — synapse.patsnap.com (#9) `A`
- ✅ **0.6491** [on_target=0.95 evidence=0.68] MTA-PRMT5 - Drugs, Indications, Patents — synapse.patsnap.com (#1) `A`
- ✅ **0.64** [on_target=0.96 evidence=0.67] [PDF] Abbisko Cayman Limited 和譽開曼有限責任公司 - HKEXnews — www1.hkexnews.hk (#5) `A`
- ❌ max_keep **0.637** [on_target=0.98 evidence=0.65] Abbisko Therapeutics Unveils Six Major Cancer Research ... — minichart.com.sg (#6) `A`
- ❌ max_keep **0.6348** [on_target=0.89 evidence=0.71] Table 1. — pmc.ncbi.nlm.nih.gov (#10)
- ❌ max_keep **0.5917** [on_target=0.97 evidence=0.61] Abbisko Therapeutics Showcases Six Research Advances Highlighting pan-KRAS, 4th Generation EGFR, and — finance.yahoo.com (#7) `A`
- ❌ max_keep **0.582** [on_target=0.97 evidence=0.60] ABSK131 / Abbisko - LARVOL DELTA — delta.larvol.com (#8) `A`
- ❌ max_keep **0.5561** [on_target=0.97 evidence=0.57] AACR 2026 / Abbisko Therapeutics Showcases Six Research Advances Highlighting pan-KRAS, 4th Generati — biospace.com (#3) `A`

**q049-4** `ABSK131 MTAP-deleted pancreatic xenograft tumour volume` → kept 5/9, jev 426 ms

- ✅ **0.6799** [on_target=0.94 evidence=0.72] ENA-2024-Abstracts.pdf — event.eortc.org (#9) `A`
- ✅ **0.6794** [on_target=0.98 evidence=0.69] ABSK131 / Abbisko - LARVOL DELTA — delta.larvol.com (#4) `A`
- ✅ **0.6632** [on_target=0.98 evidence=0.68] [PDF] Abbisko Cayman Limited 和譽開曼有限責任公司 - HKEXnews — hkexnews.hk (#3) `A`
- ✅ **0.6624** [on_target=0.96 evidence=0.69] EGFR x PRMT5 - Drugs, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#8) `A`
- ✅ **0.656** [on_target=0.96 evidence=0.68] Delving into the Latest Updates on ABSK-131 with Synapse — synapse.patsnap.com (#6) `A`
- ❌ max_keep **0.65** [on_target=0.98 evidence=0.66] AACR 2026 / Abbisko Therapeutics Showcases Six Research ... — prnewswire.com (#5) `A`
- ❌ low_on_target **0.3499** [on_target=0.64 evidence=0.55] 和誉医药在第36届EORTC-NCI-AACR大会发布PRMT5*MTA及口服KRASG12D临床前研究成果 — pharnexcloud.com (#7)
- ❌ low_on_target **0.0153** [on_target=0.27 evidence=0.06] �Z6���K�X}е���{�_O=���"�f<����]o��:�)[wWAG�0J��^��a��MRF�i�9?`�q��N^�������K���Ȝ�k�1f��''�j�)�cS��{� — dailymed.nlm.nih.gov (#1)
- ❌ low_on_target **0.0024** [on_target=0.09 evidence=0.03] Pan-cancer clinical and molecular landscape of MTAP ... — sciencedirect.com (#2)

**q049-3** `ABSK131 KRAS G12D PDAC in vivo monotherapy` → kept 4/10, jev 340 ms

- ✅ **0.6762** [on_target=0.98 evidence=0.69] [PDF] Abbisko Cayman Limited 和譽開曼有限責任公司 - HKEXnews — hkexnews.hk (#6) `A`
- ✅ **0.6664** [on_target=0.98 evidence=0.68] ABSK131 / Abbisko - LARVOL DELTA — delta.larvol.com (#1) `A`
- ✅ **0.5632** [on_target=0.96 evidence=0.59] Abbisko Cayman Limited 和譽開曼有限責任公司 — hkexnews.hk (#4) `A`
- ✅ **0.5303** [on_target=0.97 evidence=0.55] AACR 2026 / Abbisko Therapeutics（アビスコ・セラ ... - Moomoo — moomoo.com (#7) `A`
- ❌ low_on_target **0.0455** [on_target=0.15 evidence=0.30] Frontiers / Evaluation of KRAS inhibitor-directed therapies for pancreatic cancer treatment — frontiersin.org (#9)
- ❌ low_on_target **0.0296** [on_target=0.12 evidence=0.25] KRAS G12D targeted therapies for pancreatic cancer - PMC - NIH — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0195** [on_target=0.09 evidence=0.22] KRAS: the Achilles' heel of pancreas cancer biology — jci.org (#3)
- ❌ low_on_target **0.0103** [on_target=0.05 evidence=0.21] Kras G12d — tandfonline.com (#2)
- ❌ low_on_target **0.0056** [on_target=0.04 evidence=0.14] KRASG12D-driven pentose phosphate pathway remodeling ... — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0028** [on_target=0.02 evidence=0.14] KRAS Mutation Status and Treatment Outcomes in Patients With ... — pmc.ncbi.nlm.nih.gov (#10)

## q050

**Objective:** ONC201/dordaviprone in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** ONC201/dordaviprone / ONC201 / dordaviprone · anchors ['ONC201/dordaviprone', 'ONC201', 'dordaviprone']

**q050-1** `ONC201/dordaviprone PDAC monotherapy xenograft tumour growth inhibition` → kept 5/10, jev 322 ms

- ✅ **0.6467** [on_target=0.97 evidence=0.67] Oncoceutics, Inc. - 新药情报- 智慧芽 — synapse.zhihuiya.com (#1) `A`
- ✅ **0.637** [on_target=0.98 evidence=0.65] Dordaviprone/ONC201 Activation of the ClpP Mitochondrial ... - PMC — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.608** [on_target=0.96 evidence=0.63] Preclinical efficacy and mechanism of action of dordaviprone in H3 K27M-mutant diffuse glioma — academic.oup.com (#2) `A`
- ✅ **0.5949** [on_target=0.97 evidence=0.61] Dordaviprone / C24H26N4O / CID 73777259 - PubChem — pubchem.ncbi.nlm.nih.gov (#10) `A`
- ✅ **0.5888** [on_target=0.96 evidence=0.61] Preclinical efficacy and mechanism of action of dordaviprone in H3 ... — academic.oup.com (#4) `A`
- ❌ max_keep **0.558** [on_target=0.93 evidence=0.60] 29 — touchoncology.com (#3) `A`
- ❌ max_keep **0.5488** [on_target=0.98 evidence=0.56] dordaviprone (ONC201) — drughunter.com (#6) `A`
- ❌ max_keep **0.5458** [on_target=0.92 evidence=0.59] A review of current therapeutics targeting the mitochondrial protease ClpP in diffuse midline glioma — academic.oup.com (#9) `A`
- ❌ low_evidence **0.4352** [on_target=0.96 evidence=0.45] ONC201 (Dordaviprone) in Recurrent H3 K27M-Mutant Diffuse ... — pubmed.ncbi.nlm.nih.gov (#8) `A`
- ❌ low_evidence **0.3943** [on_target=0.91 evidence=0.43] dordaviprone - NCI Drug Dictionary - National Cancer Institute — cancer.gov (#7) `A`

## q051

**Objective:** DWP216 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in KRAS G12C Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** DWP216 · anchors ['DWP216']

**q051-1** `DWP216 KRAS G12C pancreatic ductal adenocarcinoma monotherapy xenograft tumour growth inhibition regression` → ABSTAIN, jev 369 ms

- ❌ low_on_target **0.1128** [on_target=0.24 evidence=0.47] KRAS Inhibition in Pancreatic Ductal Adenocarcinoma - PMC - NIH — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0442** [on_target=0.13 evidence=0.34] Direct GDP-KRASG12C inhibitors and mechanisms of resistance: the tip of the iceberg - Joshua C. Rose — journals.sagepub.com (#9)
- ❌ low_on_target **0.0387** [on_target=0.14 evidence=0.28] Unraveling (K)RAS in pancreatic ductal adenocarcinoma - memo - Magazine of European Medical Oncology — link.springer.com (#3)
- ❌ low_on_target **0.0279** [on_target=0.09 evidence=0.31] Frontiers / Evaluation of KRAS inhibitor-directed therapies for pancreatic cancer treatment — frontiersin.org (#8)
- ❌ low_on_target **0.024** [on_target=0.09 evidence=0.27] Targeting KRAS for the potential treatment of pancreatic ductal adenocarcinoma: Recent advancements  — spandidos-publications.com (#4)
- ❌ low_on_target **0.0224** [on_target=0.11 evidence=0.20] Key Considerations for Targeting KRAS in Pancreatic Cancer - PMC — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.021** [on_target=0.09 evidence=0.23] Targeting KRAS in pancreatic cancer - PMC - NIH — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0187** [on_target=0.08 evidence=0.23] Modeling response to the KRAS-G12C inhibitor AZD4625 in KRAS G12C NSCLC patient-derived xenografts r — nature.com (#2)
- ❌ low_on_target **0.0163** [on_target=0.07 evidence=0.23] KRAS inhibitors: resistance drivers and combinatorial strategies — cell.com (#10)
- ❌ low_on_target **0.0098** [on_target=0.05 evidence=0.20] Kras G12d — tandfonline.com (#6)

## q052

**Objective:** HM100714 in vivo efficacy in combination with another agent in Head and Neck Squamous Cell Carcinoma, including the combination partner  
**Target sent:** HM100714 · anchors ['HM100714']

**q052-1** `HM100714 HNSCC combination in vivo efficacy` → kept 1/10, jev 336 ms

- ✅ **0.6176** [on_target=0.97 evidence=0.64] Hanmi Showcases Next Generation Drug Innovations at AACR — hanmipharm.com (#1) `A`
- ❌ low_on_target **0.3434** [on_target=0.51 evidence=0.67] Therapeutic approaches for the treatment of head and neck ... - PMC — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.1611** [on_target=0.32 evidence=0.50] Dual anti-HER2/EGFR inhibition synergistically increases therapeutic effects and alters tumor oxygen — nature.com (#7)
- ❌ low_on_target **0.057** [on_target=0.18 evidence=0.32] Frontiers / Head and neck cancer – emerging targeted therapies — frontiersin.org (#6)
- ❌ low_on_target **0.0257** [on_target=0.10 evidence=0.26] Driving Progress in Recurrent and Metastatic Head and Neck Cancer — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0163** [on_target=0.08 evidence=0.20] Combination Therapy as a Promising Way to Fight Oral ... — pdfs.semanticscholar.org (#5)
- ❌ low_on_target **0.0105** [on_target=0.07 evidence=0.15] Targeted therapy for head and neck cancer: signaling pathways and clinical studies — nature.com (#2)
- ❌ low_on_target **0.0103** [on_target=0.05 evidence=0.21] Current and Emerging Molecular Therapies for Head and Neck ... — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0096** [on_target=0.06 evidence=0.16] Key signalling pathways in head and neck squamous cell carcinoma — academic.oup.com (#8)
- ❌ low_on_target **0.0041** [on_target=0.31 evidence=0.01] Original article Head and neck squamous cell carcinoma ... — sciencedirect.com (#4)

**q052-2** `HM100714 head and neck squamous cell carcinoma xenograft combination` → ABSTAIN, jev 374 ms

- ❌ low_on_target **0.1344** [on_target=0.36 evidence=0.37] Combination of m<scp>TOR</scp> and <scp>EGFR</scp> targeting in an orthotopic xenograft model of hea — onlinelibrary.wiley.com (#7)
- ❌ low_on_target **0.0573** [on_target=0.20 evidence=0.29] Frontiers / Head and neck cancer – emerging targeted therapies — frontiersin.org (#1)
- ❌ low_on_target **0.0532** [on_target=0.19 evidence=0.28] Therapeutically targeting head and neck squamous cell carcinoma through synergistic inhibition of LS — ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0228** [on_target=0.12 evidence=0.19] Molecular Response to Combined Molecular- and External Radiotherapy in Head and Neck Squamous Cell C — mdpi.com (#3)
- ❌ low_on_target **0.022** [on_target=0.11 evidence=0.20] Personalized Treatment of Recurrent, Metastatic Head and Neck Cancer Guided by Patient-Derived Xenog — ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0174** [on_target=0.09 evidence=0.19] Targeted therapy for head and neck cancer: signaling pathways and clinical studies — nature.com (#2)
- ❌ low_on_target **0.0155** [on_target=0.08 evidence=0.19] Preclinical investigation of anti-tumor efficacy of allogeneic natural ... — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0096** [on_target=0.06 evidence=0.16] Preclinical Head and Neck Squamous Cell Carcinoma ... — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0082** [on_target=0.06 evidence=0.14] cancers — pdfs.semanticscholar.org (#10)
- ❌ low_on_target **0.0022** [on_target=0.02 evidence=0.11] Establishment and Characterization of Patient Tumor-Derived Head ... — pmc.ncbi.nlm.nih.gov (#9)

**q052-3** `HM100714 combination partner xenograft` → kept 5/10, jev 368 ms

- ✅ **0.624** [on_target=0.96 evidence=0.65] “비만 넘어 항암으로 혁신 확장”…한미, AACR서 차세대 신약 대거 공개 — hanmi.co.kr (#1) `A`
- ✅ **0.6176** [on_target=0.96 evidence=0.64] 제약/바이오 — securities.miraeasset.com (#7) `A`
- ✅ **0.6111** [on_target=0.97 evidence=0.63] Hanmi Showcases Next Generation Drug Innovations at AACR — hanmipharm.com (#2) `A`
- ✅ **0.6111** [on_target=0.97 evidence=0.63] Hanmi Pharmaceutical Seeks New Frontiers in Cancer ... — hanmipharm.com (#5) `A`
- ✅ **0.5826** [on_target=0.95 evidence=0.61] 한미약품 美 AACR서 '업계 최다' 11개 비임상 연구결과 공개 — fnnews.com (#6) `A`
- ❌ max_keep **0.5574** [on_target=0.95 evidence=0.59] “비만 넘어 항암으로 혁신 넓힌다”…한미, AACR서 국내 최다 연구성과 발표 / 한미약품 — hanmi.co.kr (#3) `A`
- ❌ max_keep **0.4731** [on_target=0.94 evidence=0.50] 1744602650044.docx — hanmi.co.kr (#4) `A`
- ❌ low_evidence **0.3572** [on_target=0.94 evidence=0.38] Hanmi Records Highest Number of AACR Presentations ... — hanmipharm.com (#9) `A`
- ❌ low_evidence **0.3546** [on_target=0.95 evidence=0.37] 한미약품, 美암연구학회서 국내 최다 연구 발표 - 머니투데이 — mt.co.kr (#10) `A`
- ❌ low_evidence **0.2262** [on_target=0.87 evidence=0.26] 한미·HLB부터 루닛까지 AACR 2026 출격…특허 절벽 앞둔 빅파마 ... — medigatenews.com (#8) `A`

**q052-4** `HM100714 AACR HNSCC combination` → kept 5/10, jev 393 ms

- ✅ **0.6305** [on_target=0.97 evidence=0.65] Hanmi Showcases Next Generation Drug Innovations at AACR — hanmipharm.com (#5) `A`
- ✅ **0.6272** [on_target=0.96 evidence=0.65] 한미약품, 美 AACR서 차세대 항암 신약 9건 공개 - 전자신문 — etnews.com (#9) `A`
- ✅ **0.6272** [on_target=0.96 evidence=0.65] “비만 넘어 항암으로 혁신 확장”…한미, AACR서 차세대 신약 대거 공개 — hanmi.co.kr (#10) `A`
- ✅ **0.57** [on_target=0.95 evidence=0.60] “비만 넘어 항암으로 혁신 넓힌다”…한미, AACR서 국내 최다 연구성과 발표 / 한미약품 — hanmi.co.kr (#2) `A`
- ✅ **0.5636** [on_target=0.95 evidence=0.59] 한미약품 美 AACR서 '업계 최다' 11개 비임상 연구결과 공개 — fnnews.com (#8) `A`
- ❌ max_keep **0.5389** [on_target=0.94 evidence=0.57] '비만 다음은 항암' 한미약품, AACR서 연구 성과 11건 발표 — health.chosun.com (#7) `A`
- ❌ max_keep **0.5256** [on_target=0.95 evidence=0.55] 1744602650044.docx — hanmi.co.kr (#4) `A`
- ❌ max_keep **0.5187** [on_target=0.91 evidence=0.57] 한미약품, AACR 2026서 차세대 항암 파이프라인 공개 - Daum — v.daum.net (#6) `A`
- ❌ low_evidence **0.3782** [on_target=0.93 evidence=0.41] Hanmi Records Highest Number of AACR Presentations ... — hanmipharm.com (#1) `A`
- ❌ low_evidence **0.3782** [on_target=0.93 evidence=0.41] “탄탄한 근거 중심 R&D 집중”…한미약품, AACR서 국내 최다 ... — hanmi.co.kr (#3) `A`

**q052-5** `HM100714 cisplatin or pembrolizumab HNSCC` → ABSTAIN, jev 584 ms

- ❌ low_on_target **0.0133** [on_target=0.08 evidence=0.17] FDA approves neoadjuvant and adjuvant pembrolizumab ... — fda.gov (#1)
- ❌ low_on_target **0.0124** [on_target=0.06 evidence=0.21] ASCO Publishes New Guideline on Immunotherapy, Biomarker Testing in Advanced Head and Neck Cancer — dailynews.ascopubs.org (#4)
- ❌ low_on_target **0.0122** [on_target=0.06 evidence=0.20] New developments in the management of head and neck cancer — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0117** [on_target=0.08 evidence=0.15] Real-world use of first-line pembrolizumab + platinum + ... — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0109** [on_target=0.08 evidence=0.14] FDA Approves Pembrolizumab for First-Line Treatment ... — ons.org (#5)
- ❌ low_on_target **0.0102** [on_target=0.06 evidence=0.17] Immunotherapy for Head and Neck Squamous Cell Carcinoma: A Review of Current and Emerging Therapeuti — academic.oup.com (#7)
- ❌ low_on_target **0.01** [on_target=0.07 evidence=0.14] Pembrolizumab With or Without Chemotherapy in Recurrent or Metastatic Head and Neck Squamous Cell Ca — ascopubs.org (#10)
- ❌ low_on_target **0.0077** [on_target=0.05 evidence=0.15] Immunotherapy and Biomarker Testing in Recurrent and Metastatic Head and Neck Cancers: ASCO Guidelin — ascopubs.org (#2)
- ❌ low_on_target **0.0039** [on_target=0.04 evidence=0.10] The Society for Immunotherapy of Cancer consensus statement on immunotherapy for the treatment of sq — jitc.biomedcentral.com (#9)
- ❌ low_on_target **0.0037** [on_target=0.04 evidence=0.09] Efficacy and safety of the neoadjuvant chemoimmunotherapy with ... — frontiersin.org (#6)

## q053

**Objective:** ADT-1004 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** ADT-1004 · anchors ['ADT-1004']

**q053-2** `ADT-1004 tumour regression percentage MIA PaCa-2 xenograft` → kept 5/8, jev 379 ms

- ✅ **0.8827** [on_target=0.97 evidence=0.91] ADT-1004 / Auburn University, ADT Pharma - LARVOL DELTA — delta.larvol.com (#8) `A`
- ✅ **0.8608** [on_target=0.96 evidence=0.90] Broad-Spectrum RAS Inhibition in Pancreatic Ductal ... - PMC — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.806** [on_target=0.93 evidence=0.87] ADT-007 / ADT Pharma, ChemomAb — delta.larvol.com (#1) `A`
- ✅ **0.7404** [on_target=0.97 evidence=0.76] ADT-1004: A First-in-Class, Orally Bioavailable Selective pan-RAS Inhibitor for — biorxiv.org (#2) `A`
- ✅ **0.7293** [on_target=0.99 evidence=0.74] A potent and selective pan-RAS inhibitor, ADT-1004, targeting complex KRAS mutations for pancreatic  — ascopubs.org (#4) `A`
- ❌ max_keep **0.6705** [on_target=0.94 evidence=0.71] A Novel Pan-RAS Inhibitor with a Unique Mechanism of Action Blocks Tumor Growth in Mouse Models of G — biorxiv.org (#3) `A`
- ❌ max_keep **0.6076** [on_target=0.98 evidence=0.62] ADT-1004: a first-in-class, oral pan-RAS inhibitor with robust antitumor activity in preclinical mod — pubmed.ncbi.nlm.nih.gov (#7) `A`
- ❌ low_evidence **0.2881** [on_target=0.95 evidence=0.30] Adt-1004: A First-in-Class, Orally Bioavailable Selective ... — augusta.elsevierpure.com (#6) `A`

**q053-3** `ADT-1004 KRAS G12D PDX tumour shrinkage monotherapy` → kept 5/10, jev 390 ms

- ✅ **0.8943** [on_target=0.99 evidence=0.90] ADT-1004: a first-in-class, oral pan-RAS inhibitor with robust ... — link.springer.com (#1) `A`
- ✅ **0.8712** [on_target=0.99 evidence=0.88] ADT-1004: a first-in-class, oral pan-RAS inhibitor with ... - PubMed — pubmed.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.8494** [on_target=0.98 evidence=0.87] Pan-RAS Inhibitors: Expanding Therapeutic Potential and Evading Resistance — mdpi.com (#5) `A`
- ✅ **0.8349** [on_target=0.99 evidence=0.84] ADT-1004: A First-in-Class, Orally Bioavailable Selective pan-RAS Inhibitor for Pancreatic Ductal Ad — pubmed.ncbi.nlm.nih.gov (#7) `A`
- ✅ **0.7774** [on_target=0.98 evidence=0.79] Abstract LB_B26: Efficacy and tolerability of a novel pan-RAS inhibitor with a unique mechanism of s — aacrjournals.org (#9) `A`
- ❌ max_keep **0.7598** [on_target=0.97 evidence=0.78] Broad-Spectrum RAS Inhibition in Pancreatic Ductal ... - PMC — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ max_keep **0.72** [on_target=0.96 evidence=0.75] Key Considerations for Targeting KRAS in Pancreatic Cancer - PMC — pmc.ncbi.nlm.nih.gov (#4) `A`
- ❌ max_keep **0.6534** [on_target=0.98 evidence=0.67] Emerging KRAS G12D inhibitor in the treatment of digestive ... — pmc.ncbi.nlm.nih.gov (#8) `A`
- ❌ max_keep **0.4424** [on_target=0.79 evidence=0.56] Abstract 7236: Selective deletion of the KRAS mutant gene with ADGN-123 and ADGN-121 peptide-RNA nan — bohrium.dp.tech (#6) `A`
- ❌ low_on_target **0.0118** [on_target=0.05 evidence=0.24] Kras G12d — tandfonline.com (#3) `A`

**q053-5** `ADT-1004 MIA-AMG-R xenograft final tumour volume monotherapy` → kept 5/10, jev 342 ms

- ✅ **0.8558** [on_target=0.98 evidence=0.87] ADT-1004: a first-in-class, oral pan-RAS inhibitor with robust ... - PMC — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.8547** [on_target=0.99 evidence=0.86] Abstract LB322: Antitumor activity of 1st-in-class pan-RAS inhibitor ADT-1004 in mouse models of pan — aacrjournals.org (#5) `A`
- ✅ **0.8382** [on_target=0.99 evidence=0.85] ADT-1004: a first-in-class, oral pan-RAS inhibitor with robust antitumor activity in preclinical mod — pubmed.ncbi.nlm.nih.gov (#6) `A`
- ✅ **0.832** [on_target=0.96 evidence=0.87] Broad-Spectrum RAS Inhibition in Pancreatic Ductal Adenocarcinoma: Mechanistic Advances and Therapeu — mdpi.com (#8) `A`
- ✅ **0.6688** [on_target=0.96 evidence=0.70] ADT-007 / ADT Pharma, ChemomAb — delta.larvol.com (#2) `A`
- ❌ max_keep **0.6301** [on_target=0.95 evidence=0.66] Title: A Novel Pan-RAS Inhibitor with a Unique Mechanism of Action Blocks Tumor Growth in — biorxiv.org (#7) `A`
- ❌ max_keep **0.5814** [on_target=0.98 evidence=0.59] ADT-1004 / Auburn University, ADT Pharma - LARVOL DELTA — delta.larvol.com (#3) `A`
- ❌ low_evidence **0.3912** [on_target=0.97 evidence=0.40] A potent and selective pan-RAS inhibitor, ADT-1004, targeting complex KRAS mutations for pancreatic  — ascopubs.org (#10) `A`
- ❌ low_on_target **0.1685** [on_target=0.32 evidence=0.53] Androgen Receptor Pathway Inhibitor Monotherapy in ... — research.unipd.it (#9)
- ❌ low_on_target **0.0356** [on_target=0.11 evidence=0.32] A Pan-RAS Inhibitor with a Unique Mechanism of Action ... — pmc.ncbi.nlm.nih.gov (#4)

**q053-4** `ADT-1004 KPC orthotopic tumour volume change day 27` → kept 5/10, jev 387 ms

- ✅ **0.9504** [on_target=0.99 evidence=0.96] ADT-1004: a first-in-class, oral pan-RAS inhibitor with robust ... - PMC — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.8316** [on_target=0.99 evidence=0.84] ADT-1004: a first-in-class, oral pan-RAS inhibitor with robust antitumor activity in preclinical mod — pubmed.ncbi.nlm.nih.gov (#3) `A`
- ✅ **0.8217** [on_target=0.99 evidence=0.83] Abstract LB322: Antitumor activity of 1st-in-class pan-RAS inhibitor ADT-1004 in mouse models of pan — aacrjournals.org (#7) `A`
- ✅ **0.8004** [on_target=0.98 evidence=0.82] ADT-1004 / Auburn University, ADT Pharma - LARVOL DELTA — delta.larvol.com (#6) `A`
- ✅ **0.7363** [on_target=0.94 evidence=0.78] ADT-007 / ADT Pharma, ChemomAb — delta.larvol.com (#4) `A`
- ❌ max_keep **0.7154** [on_target=0.98 evidence=0.73] A potent and selective pan-RAS inhibitor, ADT-1004, targeting complex KRAS mutations for pancreatic  — ascopubs.org (#9) `A`
- ❌ max_keep **0.6762** [on_target=0.98 evidence=0.69] Table 1. — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ low_on_target **0.0147** [on_target=0.11 evidence=0.13] Assessing the effects of androgen-deprivation therapy ... — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0065** [on_target=0.28 evidence=0.02] Proprietary Information of MD Anderson — cdn.clinicaltrials.gov (#5)
- ❌ low_on_target **0.0024** [on_target=0.03 evidence=0.08] [PDF] Physics and Imaging in Radiation Oncology - DiVA portal — diva-portal.org (#8)

**q053-1** `ADT-1004 quantitative tumour growth inhibition percentage PDAC monotherapy` → kept 5/8, jev 327 ms

- ✅ **0.9042** [on_target=0.99 evidence=0.91] ADT-1004: a first-in-class, oral pan-RAS inhibitor with robust ... — link.springer.com (#1) `A`
- ✅ **0.8052** [on_target=0.99 evidence=0.81] Abstract LB322: Antitumor activity of 1st-in-class pan-RAS inhibitor ADT-1004 in mouse models of pan — aacrjournals.org (#4) `A`
- ✅ **0.7885** [on_target=0.95 evidence=0.83] Broad-Spectrum RAS Inhibition in Pancreatic Ductal Adenocarcinoma: Mechanistic Advances and Therapeu — mdpi.com (#5) `A`
- ✅ **0.776** [on_target=0.97 evidence=0.80] Adt-1004: A First-in-Class, Orally Bioavailable Selective ... — augusta.elsevierpure.com (#2) `A`
- ✅ **0.7722** [on_target=0.99 evidence=0.78] A potent and selective pan-RAS inhibitor, ADT-1004, targeting complex KRAS mutations for pancreatic  — ascopubs.org (#3) `A`
- ❌ max_keep **0.6944** [on_target=0.96 evidence=0.72] Treatment of KRAS-Mutated Pancreatic Cancer: New Hope for the Patients? — mdpi.com (#8) `A`
- ❌ max_keep **0.6598** [on_target=0.98 evidence=0.67] KRAS Inhibition in Pancreatic Ductal Adenocarcinoma - PMC - NIH — pmc.ncbi.nlm.nih.gov (#6) `A`
- ❌ low_on_target **0.0158** [on_target=0.06 evidence=0.26] link.springer.com · content · pdfCurrent advances in immunotherapy for KRAS-Mutant pancreatic... — link.springer.com (#7)

## q054

**Objective:** DWP216 in vivo animal models and results: cell-line xenograft (CDX), patient-derived xenograft (PDX), syngeneic, orthotopic, or genetically engineered models  
**Target sent:** DWP216 · anchors ['DWP216']

**q054-1** `DWP216 HNSCC in vivo xenograft monotherapy` → kept 3/10, jev 338 ms

- ✅ **0.7284** [on_target=0.98 evidence=0.74] [PDF] Development of DWP216, a TEAD1 selective inhibitor for NF2 ... — kddf.org (#4) `A`
- ✅ **0.7224** [on_target=0.84 evidence=0.86] pan-TEAD inhib News — sigma.larvol.com (#1) `A`
- ✅ **0.686** [on_target=0.98 evidence=0.70] [단독] 대웅제약의 '차세대 항암 신약' 비밀병기 3종은? - 헬스케어N — m.healthcaren.com (#5) `A`
- ❌ low_on_target **0.0459** [on_target=0.09 evidence=0.51] Preclinical Head and Neck Squamous Cell Carcinoma ... — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0359** [on_target=0.11 evidence=0.33] [PDF] Download PDF - eScholarship.org — escholarship.org (#10)
- ❌ low_on_target **0.0105** [on_target=0.07 evidence=0.15] Targeted therapy for head and neck cancer: signaling pathways and clinical studies — nature.com (#8)
- ❌ low_on_target **0.006** [on_target=0.05 evidence=0.12] Therapeutic approaches for the treatment of head and neck ... - PMC — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0032** [on_target=0.16 evidence=0.02] Original article Head and neck squamous cell carcinoma ... — sciencedirect.com (#7)
- ❌ low_on_target **0.0002** [on_target=0.06 evidence=0.00] PDC000198 - Proteomic Data Commons - National Cancer Institute — proteomic.datacommons.cancer.gov (#3)
- ❌ low_on_target **0.0** [on_target=0.03 evidence=0.00] Cloudflare — advancesradonc.org (#2)

**q054-3** `DWP216 pancreatic cancer PDX syngeneic orthotopic` → ABSTAIN, jev 466 ms

- ❌ low_on_target **0.0264** [on_target=0.08 evidence=0.33] Establishment and Thorough Characterization of Xenograft (PDX) Models Derived from Patients with Pan — mdpi.com (#10)
- ❌ low_on_target **0.0234** [on_target=0.06 evidence=0.39] Orthotopic Patient-Derived Pancreatic Cancer Xenografts Engraft ... — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0192** [on_target=0.06 evidence=0.32] Patient Derived Xenograft — tumor.informatics.jax.org (#1)
- ❌ low_on_target **0.0152** [on_target=0.05 evidence=0.30] [PDF] The use of patient-derived xenografts and patient-derived organoids ... — publications.cuni.cz (#5)
- ❌ low_on_target **0.0129** [on_target=0.04 evidence=0.32] Patient-Derived Xenograft Models of Pancreatic Cancer - PMC — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0128** [on_target=0.04 evidence=0.32] Preclinical mouse models for immunotherapeutic and non-immunotherapeutic drug development for pancre — ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0113** [on_target=0.05 evidence=0.23] Pancreatic cancer — jax.org (#4)
- ❌ low_on_target **0.0113** [on_target=0.04 evidence=0.28] Patient-Derived Xenograft (PDX) Models — criver.com (#7)
- ❌ low_on_target **0.0096** [on_target=0.06 evidence=0.16] Pancreatic cancer PDX models - Crown Bioscience — crownbio.com (#3)
- ❌ low_on_target **0.0002** [on_target=0.05 evidence=0.00] {{ngMeta['og:title']}} — bio.tools (#2)

**q054-5** `DWP216 genetically engineered mouse model` → kept 1/10, jev 368 ms

- ✅ **0.7056** [on_target=0.98 evidence=0.72] [PDF] Development of DWP216, a TEAD1 selective inhibitor for NF2 ... — kddf.org (#1) `A`
- ❌ low_on_target **0.0103** [on_target=0.10 evidence=0.10] Resource Page — wagnerlab.net (#3)
- ❌ low_on_target **0.0102** [on_target=0.06 evidence=0.17] A Comprehensive Review of Genetically Engineered Mouse Models ... — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0017** [on_target=0.05 evidence=0.03] Genetically Engineered Mouse Models — gempharmatech.com (#7)
- ❌ low_on_target **0.0009** [on_target=0.04 evidence=0.02] Genetically engineered mouse models for studying radiation biology — tcr.amegroups.org (#10)
- ❌ low_on_target **0.0002** [on_target=0.06 evidence=0.00] Gene search results — mousephenotype.org (#2)
- ❌ low_on_target **0.0002** [on_target=0.03 evidence=0.01] 017536 — jax.org (#9)
- ❌ low_on_target **0.0001** [on_target=0.03 evidence=0.00] 029619 — jax.org (#4)
- ❌ low_on_target **0.0001** [on_target=0.03 evidence=0.00] 026622 — jax.org (#5)
- ❌ low_on_target **0.0** [on_target=0.06 evidence=0.00] PMC — ncbi.nlm.nih.gov (#6)

**q054-2** `DWP216 NCI-H1373 monotherapy tumour volume` → kept 1/10, jev 519 ms

- ✅ **0.6855** [on_target=0.97 evidence=0.71] [단독] 대웅제약의 '차세대 항암 신약' 비밀병기 3종은? - 헬스케어N — m.healthcaren.com (#6) `A`
- ❌ low_on_target **0.0821** [on_target=0.16 evidence=0.51] NCI-H1373 AdagR — ribometrix.com (#3)
- ❌ low_on_target **0.0234** [on_target=0.27 evidence=0.09] "� �����/f�˪���~��EwI��LIq7����5�����]�dO`��㪗F�to��^(@����H<��v{�ZF�m� `G�:I_0w�������~8 ���ԛ������R — public-pages-files-2025.frontiersin.org (#7)
- ❌ low_on_target **0.0154** [on_target=0.33 evidence=0.05] ,A����-�۠���˽f=�@�H����#�;3��oQ�{P��X�O� �lFc�M����Y�$���/��^������ �10�pa��=� u�[�m"hI!�uQp���p���  — dailymed.nlm.nih.gov (#8)
- ❌ low_on_target **0.014** [on_target=0.07 evidence=0.20] NCI-H1373 — wikidata.org (#9)
- ❌ low_on_target **0.0058** [on_target=0.29 evidence=0.02] CLINICAL TRIALS — amgentrials.com (#4)
- ❌ low_on_target **0.0048** [on_target=0.06 evidence=0.08] NCI-H1373 Pharmacogenomics Data / CellMinerCDB — discover.nci.nih.gov (#10)
- ❌ low_on_target **0.0023** [on_target=0.05 evidence=0.05] NCI-H1373 - Cell Model Passports — cellmodelpassports.sanger.ac.uk (#5)
- ❌ low_on_target **0.0005** [on_target=0.05 evidence=0.01] NCI-H1373 [H1373] - CRL-5866 — atcc.org (#2)
- ❌ low_on_target **0.0** [on_target=0.05 evidence=0.00] PDC000198 - Proteomic Data Commons - National Cancer Institute — proteomic.datacommons.cancer.gov (#1)

**q054-4** `DWP216 CAPAN-1 xenograft monotherapy 1200 mm3` → ABSTAIN, jev 435 ms

- ❌ low_on_target **0.027** [on_target=0.30 evidence=0.09] 樗��Tb!ܓ��c���Nw����>����z�Q��z8n���K{�S��a��i�'���\�n�2���4}ec�d�!��ɖ%��T/�̛��@%-A����*YX~���U�Dip�� — public-pages-files-2025.frontiersin.org (#4)
- ❌ low_on_target **0.0251** [on_target=0.29 evidence=0.09] z�V���lآ794��ܛ"�u���q�O� &皙�壧"€4,�b�g2������iPѤD#j���l��[����9P_%n�Ăx-�23���4�r%b�f��>.ٹ�$��k��7�F�> — frontiersin.org (#5)
- ❌ low_on_target **0.0248** [on_target=0.31 evidence=0.08] � bb��L�d����47��yB��A���;kqgè�k��;��՝�h�jC���&�� �ٷ�o�k��mhl�ƒ~5���ވ��!*��}}����{����6�ȭϵ��.�/w���� — public-pages-files-2025.frontiersin.org (#9)
- ❌ low_on_target **0.024** [on_target=0.30 evidence=0.08] �+4s��x�1��k �윦0�wUY/_"������f��grVsU�_�"<��^��8�;���g}*��Q��2��D����D�G�PɊIS�^']#������\���rx�P�Swo — frontiersin.org (#7)
- ❌ low_on_target **0.0238** [on_target=0.31 evidence=0.08] "� �����/f�˪���~��EwI��LIq7����5�����]�dO`��㪗F�to��^(@����H<��v{�ZF�m� `G�:I_0w�������~8 ���ԛ������R — public-pages-files-2025.frontiersin.org (#8)
- ❌ low_on_target **0.0215** [on_target=0.28 evidence=0.08] �`�}�r.�V�OIx��t\��Uf_/ JI'_.����5���bm��b]1��_��P+�į�8��M�/�O���CЃ^o��C23�Q/D �?:K�G��M�b�U�M]��No� — frontiersin.org (#10)
- ❌ low_on_target **0.0207** [on_target=0.27 evidence=0.08] ߄w����I*�/b�r˕٘�}>�g��_��":^)Љ��P�}�꼖���(e��㡱Y;�~�]���E�����/�IbU�̓����-Ʊ�{�{t{LA=�Tm)P,�*u����Q:ʾ�, — techscience.com (#6)
- ❌ low_on_target **0.0065** [on_target=0.28 evidence=0.02] CLINICAL TRIALS — amgentrials.com (#3)
- ❌ low_on_target **0.0002** [on_target=0.06 evidence=0.00] PDC000198 - Proteomic Data Commons - National Cancer Institute — proteomic.datacommons.cancer.gov (#1)
- ❌ low_on_target **0.0** [on_target=0.05 evidence=0.00] Cloudflare — aacrjournals.org (#2)

## q055

**Objective:** DB-1305/Anti-PD-L1/VEGF Bispecific Antibody patients studied in Recurrent or Disseminated HNSCC (Oral Cavity/Oropharynx/Hypopharynx/Larynx), Incurable by Local Therapies trials: biomarker selection, disease severity, line of therapy, and required prior treatment  
**Target sent:** DB-1305 · anchors ['DB-1305']

**q055-1** `DB-1305 recurrent metastatic HNSCC prior treatment line of therapy` → kept 2/10, jev 509 ms

- ✅ **0.7047** [on_target=0.87 evidence=0.81] DB-1311 in Combination With BNT327 or DB-1305 ... — centerwatch.com (#4) `A`
- ✅ **0.6641** [on_target=0.87 evidence=0.76] DB-1311 in Combination With BNT327 or DB-1305 ... — trial.medpath.com (#7) `A`
- ❌ low_on_target **0.0374** [on_target=0.11 evidence=0.34] Emerging and Investigational Systemic Therapies in ... - PMC — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0323** [on_target=0.10 evidence=0.32] Driving Progress in Recurrent and Metastatic Head and Neck Cancer — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.0261** [on_target=0.08 evidence=0.33] Immunotherapy in Recurrent/Metastatic Squamous Cell ... — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0261** [on_target=0.08 evidence=0.33] The Society for Immunotherapy of Cancer consensus statement on immunotherapy for the treatment of sq — jitc.bmj.com (#9)
- ❌ low_on_target **0.0215** [on_target=0.07 evidence=0.31] Essential news of current guidelines: head and neck squamous cell carcinoma — link.springer.com (#3)
- ❌ low_on_target **0.0196** [on_target=0.06 evidence=0.33] Immunotherapy in recurrent/metastatic head and neck ... - PMC — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0192** [on_target=0.06 evidence=0.32] Paradigm Change in First-Line Treatment of Recurrent and ... — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0123** [on_target=0.04 evidence=0.31] Evidence-Based Treatment Options in Recurrent and/or ... - PMC — pmc.ncbi.nlm.nih.gov (#2)

**q055-3** `DB-1305 HNSCC ECOG measurable disease inclusion criteria` → kept 5/10, jev 418 ms

- ✅ **0.7253** [on_target=0.85 evidence=0.85] ANZCTR - Registration — anzctr.org.au (#10)
- ✅ **0.7136** [on_target=0.96 evidence=0.74] Drug: DB-1305/BNT325 - TrialFetch — trialfetch.com (#3) `A`
- ✅ **0.7104** [on_target=0.96 evidence=0.74] First-in-human Study of DB-1305/BNT325 for Advanced/Metastatic Solid Tumors — clinicaltrials.gov (#5) `A`
- ✅ **0.6952** [on_target=0.97 evidence=0.72] First-in-human Study of DB-1305/BNT325 for... / Clinical Trial — trial.medpath.com (#2) `A`
- ✅ **0.686** [on_target=0.84 evidence=0.82] DB-1311 in Combination With BNT327 or DB-1305 ... — uclahealth.org (#1) `A`
- ❌ max_keep **0.494** [on_target=0.95 evidence=0.52] DB-1305 for Solid Tumors · Info for Participants — withpower.com (#4) `A`
- ❌ low_on_target **0.3345** [on_target=0.45 evidence=0.74] dbGaP Study — ncbi.nlm.nih.gov (#8)
- ❌ low_evidence **0.2352** [on_target=0.72 evidence=0.33] A Phase II, Multicenter, Open-Label Trial of DB-1311 in ... — cancer.columbia.edu (#6) `A`
- ❌ low_on_target **0.1421** [on_target=0.26 evidence=0.55] TrialFinder (PDF) — uke.de (#7)
- ❌ low_on_target **0.1408** [on_target=0.22 evidence=0.64] EA3191 Head and Neck Cancer Clinical Trial Home Page — ecog-acrin.org (#9)

**q055-2** `DB-1305 HNSCC PD-L1 biomarker eligibility` → kept 1/10, jev 399 ms

- ✅ **0.6335** [on_target=0.83 evidence=0.76] DB-1311 in Combination With BNT327 or DB-1305 ... — uclahealth.org (#9) `A`
- ❌ low_on_target **0.0446** [on_target=0.13 evidence=0.34] Immunotherapy in recurrent/metastatic head and neck ... — iris.uniroma1.it (#6)
- ❌ low_on_target **0.0367** [on_target=0.11 evidence=0.33] Assessing PD-L1 Expression in Head and Neck Squamous ... — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.0337** [on_target=0.10 evidence=0.34] Immune biomarkers for head and neck cancer - PMC — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0261** [on_target=0.08 evidence=0.33] PD-L1 Testing in Cancer - MyPathologyReport — mypathologyreport.ca (#4)
- ❌ low_on_target **0.0261** [on_target=0.08 evidence=0.33] Immunotherapy and Biomarker Testing in Recurrent and Metastatic Head and Neck Cancers: ASCO Guidelin — ascopubs.org (#5)
- ❌ low_on_target **0.0256** [on_target=0.08 evidence=0.32] The Society for Immunotherapy of Cancer consensus statement on immunotherapy for the treatment of sq — jitc.bmj.com (#8)
- ❌ low_on_target **0.0252** [on_target=0.09 evidence=0.28] PD-L1: Test Selection Guide — testdirectory.questdiagnostics.com (#3)
- ❌ low_on_target **0.0212** [on_target=0.07 evidence=0.30] Multicenter real-world data on immunotherapy for R/M HNSCC from ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.004** [on_target=0.04 evidence=0.10] UCLA Head and Neck Squamous Cell Carcinoma Clinical Trials — ucla.clinicaltrials.researcherprofiles.org (#2)

## q056

**Objective:** MNPS Asset planned or expected data readouts, regulatory submissions, regulatory decisions, and expected timing in Head and Neck Cancer  
**Target sent:** MNPS · anchors ['MNPS']

**q056-2** `MNPS Asset head and neck cancer regulatory submission` → ABSTAIN, jev 358 ms

- ❌ low_on_target **0.5478** [on_target=0.66 evidence=0.83] PDF / Head And Neck Cancer / Radiation Therapy - Scribd — scribd.com (#6)
- ❌ low_on_target **0.49** [on_target=0.61 evidence=0.80] Head & Neck Cancer / Clinical - CancerNetwork — cancernetwork.com (#7)
- ❌ low_on_target **0.0208** [on_target=0.08 evidence=0.26] Mononuclear phagocytes in head and neck squamous cell carcinoma — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ low_on_target **0.0154** [on_target=0.06 evidence=0.26] Advances in nanomaterials for the diagnosis and treatment of head ... — sciencedirect.com (#8) `A`
- ❌ low_on_target **0.0066** [on_target=0.03 evidence=0.22] NCCN Guidelines® Insights: Head and Neck Cancers ... — pubmed.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0023** [on_target=0.17 evidence=0.01] 9196json-file-1.pdf — gov.br (#9)
- ❌ low_on_target **0.0013** [on_target=0.20 evidence=0.01] MPSA — yumpu.com (#2)
- ❌ low_on_target **0.0011** [on_target=0.04 evidence=0.03] NCCN - head and neck cancers v4.2024 - ARUP Consult — arupconsult.com (#4)
- ❌ low_on_target **0.0004** [on_target=0.06 evidence=0.01] [PDF] 2022 Update edited by the Japan Society for Head and Neck Cancer — sciencedirect.com (#3)
- ❌ low_on_target **0.0** [on_target=0.22 evidence=0.00] Internal Server Error — cdas.cancer.gov (#1)

**q056-1** `MNPS Asset first-line recurrent metastatic head and neck cancer data readout` → ABSTAIN, jev 369 ms

- ❌ low_on_target **0.1624** [on_target=0.29 evidence=0.56] First-line therapy for recurrent metastatic head and neck ... — tcr.amegroups.org (#6)
- ❌ low_on_target **0.1067** [on_target=0.32 evidence=0.33] Driving Progress in Recurrent and Metastatic Head and Neck Cancer — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0672** [on_target=0.21 evidence=0.32] First-Line Therapy in Recurrent or Metastatic Head and Neck Squamous Cell Carcinoma: A Retrospective — onlinelibrary.wiley.com (#2)
- ❌ low_on_target **0.063** [on_target=0.15 evidence=0.42] Nasopharyngeal Carcinoma... — datalookout.com (#1)
- ❌ low_on_target **0.0598** [on_target=0.23 evidence=0.26] First-Line Therapy in Recurrent or Metastatic Head and Neck ... — pubmed.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0485** [on_target=0.16 evidence=0.30] Real-World Treatment Patterns and Outcomes — ispor.org (#7)
- ❌ low_on_target **0.0435** [on_target=0.15 evidence=0.29] Real-world treatment patterns and outcomes among ... - PMC — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0352** [on_target=0.16 evidence=0.22] Real world treatment patterns for recurrent and metastatic ... — frontiersin.org (#9)
- ❌ low_on_target **0.0229** [on_target=0.08 evidence=0.29] Current Therapy for Metastatic Head and Neck Cancer: Evidence, Opportunities, and Challenges — ascopubs.org (#8)
- ❌ low_on_target **0.0064** [on_target=0.03 evidence=0.21] Recurrent/metastatic relapse after definitive treatment for HNSCC — frontiersin.org (#4)

**q056-3** `MNPS Asset head and neck cancer regulatory decision` → ABSTAIN, jev 352 ms

- ❌ low_on_target **0.4592** [on_target=0.56 evidence=0.82] Head & Neck Cancer / Clinical - CancerNetwork — cancernetwork.com (#7)
- ❌ low_on_target **0.1193** [on_target=0.20 evidence=0.60] Head & Neck Cancers / Clinical - OncLive — onclive.com (#9)
- ❌ low_on_target **0.0067** [on_target=0.03 evidence=0.22] NCCN Guidelines® Insights: Head and Neck Cancers ... — pubmed.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.004** [on_target=0.11 evidence=0.04] Live Head And Neck Cancer updates — miragenews.com (#4)
- ❌ low_on_target **0.0018** [on_target=0.11 evidence=0.02] Regulatory Decision Summaries - Drug and Health Product Register — hpr-rps.hres.ca (#3)
- ❌ low_on_target **0.001** [on_target=0.06 evidence=0.02] [PDF] 2022 Update edited by the Japan Society for Head and Neck Cancer — sciencedirect.com (#5)
- ❌ low_on_target **0.0005** [on_target=0.08 evidence=0.01] Search Page - Drug and Health Product Register — hpr-rps.hres.ca (#1)
- ❌ low_on_target **0.0005** [on_target=0.03 evidence=0.02] NCCN - head and neck cancers v4.2024 - ARUP Consult — arupconsult.com (#8)
- ❌ low_on_target **0.0** [on_target=0.13 evidence=0.00] Internal Server Error — cdas.cancer.gov (#2)
- ❌ low_on_target **0.0** [on_target=0.37 evidence=0.00] Legal News & Analysis on Litigation, Policy, Deals : Law360 — law360.com (#6)

## q057

**Objective:** CNP200137 first regulatory approval or market launch year for acute myeloid leukemia  
**Target sent:** CNP200137 · anchors ['CNP200137']

**q057-1** `CNP200137 regulatory approval AML` → kept 1/10, jev 374 ms

- ✅ **0.8019** [on_target=0.97 evidence=0.83] Menin Inhibitor Drug Development Pipeline: AML, Diabetes ... — inflectionlabs.bio (#1) `A`
- ❌ low_on_target **0.547** [on_target=0.56 evidence=0.98] Regulatory timeline - OnCo — onco.cc (#6)
- ❌ low_on_target **0.5123** [on_target=0.58 evidence=0.88] Important announcement - Home / AML Hub — aml-hub.com (#10)
- ❌ low_on_target **0.2222** [on_target=0.31 evidence=0.72] Acute Myeloid Leukemia: 2025 Update on Diagnosis, Risk-Stratification, and Management — onlinelibrary.wiley.com (#3)
- ❌ low_on_target **0.208** [on_target=0.30 evidence=0.69] Oncology (Cancer)/Hematologic Malignancies Approval ... — fda.gov (#2)
- ❌ low_on_target **0.2052** [on_target=0.27 evidence=0.76] Acute Myeloid Leukemia Market Summary — delveinsight.com (#9)
- ❌ low_on_target **0.0565** [on_target=0.15 evidence=0.38] CA A Cancer J Clinicians - 2024 - Kantarjian - Acute Myeloid ... — scribd.com (#7)
- ❌ low_on_target **0.0271** [on_target=0.29 evidence=0.09] .����Ge#� �������� ��KW����ro���m�T����bu5���.t�m�����:��o�{�f=��,���_����D�;F'��-�.�u�y�ȶ�E����8y�� — filehosting.pharmacm.com (#8)
- ❌ low_on_target **0.0016** [on_target=0.16 evidence=0.01] NCATS Inxight Drugs — drugs.ncats.io (#5)
- ❌ low_on_target **0.0** [on_target=0.08 evidence=0.00] Circulars & Announcements-CStone Pharmaceuticals — cstonepharma.com (#4)

**q057-2** `CNP200137 market launch AML` → kept 1/10, jev 463 ms

- ✅ **0.8083** [on_target=0.97 evidence=0.83] Menin Inhibitor Drug Development Pipeline: AML, Diabetes ... — inflectionlabs.bio (#1) `A`
- ❌ low_on_target **0.1146** [on_target=0.18 evidence=0.64] Acute Myeloid Leukemia Market Summary — delveinsight.com (#9)
- ❌ low_on_target **0.0001** [on_target=0.02 evidence=0.00] Nano One Materials Corp: NEWS RELEASE EN — news.futunn.com (#8)
- ❌ low_on_target **0.0001** [on_target=0.03 evidence=0.00] Blog / AML Oceanographic Acquired by Union Park Capital ... — amloceanographic.com (#10)
- ❌ low_on_target **0.0** [on_target=0.02 evidence=0.00] 555 Security Incident Detected — 2npharma.com (#2)
- ❌ low_on_target **0.0** [on_target=0.04 evidence=0.00] 520: Web server is returning an unknown error — q-depot.com (#3)
- ❌ low_on_target **0.0** [on_target=0.07 evidence=0.00] Circulars & Announcements-CStone Pharmaceuticals — cstonepharma.com (#4)
- ❌ low_on_target **0.0** [on_target=0.11 evidence=0.00] Please verify you are a human — zoominfo.com (#5)
- ❌ low_on_target **0.0** [on_target=0.02 evidence=0.00] cnp — roblox.com (#6)
- ❌ low_on_target **0.0** [on_target=0.05 evidence=0.00] New Listing Information - AP & PHIP — www1.hkexnews.hk (#7)

## q058

**Objective:** HEC234055 in vivo efficacy in combination with another agent in Pancreatic Ductal Adenocarcinoma, including the combination partner  
**Target sent:** HEC234055 · anchors ['HEC234055']

**q058-1** `HEC234055 combination pancreatic ductal adenocarcinoma in vivo` → kept 1/10, jev 398 ms

- ✅ **0.595** [on_target=0.75 evidence=0.79] Three innovative drugs showcased at the 2026 AACR Annual ... — moomoo.com (#2)
- ❌ low_on_target **0.1838** [on_target=0.37 evidence=0.50] Unbiased in vivo preclinical evaluation of anticancer drugs identifies effective therapy for the tre — pubmed.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0585** [on_target=0.15 evidence=0.39] Concerted cell and in vivo screen for pancreatic ductal adenocarcinoma (PDA) chemotherapeutics — ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0312** [on_target=0.26 evidence=0.12] Combing Treatment for PDAC — public-pages-files-2025.frontiersin.org (#1)
- ❌ low_on_target **0.0166** [on_target=0.07 evidence=0.24] A rapid in vivo screen for pancreatic ductal adenocarcinoma therapeutics — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0132** [on_target=0.06 evidence=0.22] Pancreatic Ductal Adenocarcinoma: Current and Evolving ... — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0095** [on_target=0.03 evidence=0.32] Pancreatic ductal adenocarcinoma: Treatment hurdles, tumor ... — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0077** [on_target=0.03 evidence=0.26] In vivo Mouse Models of Pancreatic Ductal Adenocarcinoma — pancreapedia.org (#10)
- ❌ low_on_target **0.0067** [on_target=0.03 evidence=0.22] Preclinical Models of Pancreatic Ductal Adenocarcinoma and Their Utility in Immunotherapy Studies — mdpi.com (#7)
- ❌ low_on_target **0.0019** [on_target=0.03 evidence=0.06] Contact us — malacards.org (#5)

**q058-2** `HEC234055 combination partner PDAC xenograft` → kept 2/10, jev 349 ms

- ✅ **0.759** [on_target=0.99 evidence=0.77] Three innovative drugs showcased at the 2026 AACR Annual ... — moomoo.com (#2) `A`
- ✅ **0.7186** [on_target=0.98 evidence=0.73] C262019A_Sunshine Pharma 1..4 — hecpharm.com (#1) `A`
- ❌ low_on_target **0.084** [on_target=0.21 evidence=0.40] Molecular alterations and targeted therapy in pancreatic ... — d-nb.info (#9)
- ❌ low_on_target **0.0558** [on_target=0.18 evidence=0.31] Combinatorial Screening of Pancreatic Adenocarcinoma Reveals Sensitivity to Drug Combinations Includ — ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0159** [on_target=0.28 evidence=0.06] Treatment of pancreatic cancer with a combination ... — sciencedirect.com (#6)
- ❌ low_on_target **0.0098** [on_target=0.06 evidence=0.16] [PDF] Combinatorial screening of pancreatic adenocarcinoma reveals ... — scispace.com (#5)
- ❌ low_on_target **0.0085** [on_target=0.05 evidence=0.17] Patient-Derived Xenograft Models of Pancreatic Cancer - PMC — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0063** [on_target=0.19 evidence=0.03] A potential therapeutic target for pancreatic ductal adenocarcinoma — sciencedirect.com (#4)
- ❌ low_on_target **0.0039** [on_target=0.13 evidence=0.03] Experimental drugs and drug combinations in pancreatic cancer — sciencedirect.com (#3)
- ❌ low_on_target **0.0008** [on_target=0.04 evidence=0.02] Table 2. — pmc.ncbi.nlm.nih.gov (#8)

**q058-3** `HEC234055 AACR 2026 combination efficacy` → kept 3/10, jev 439 ms

- ✅ **0.7774** [on_target=0.98 evidence=0.79] Three innovative drugs showcased at the 2026 AACR Annual ... — moomoo.com (#3) `A`
- ✅ **0.7644** [on_target=0.98 evidence=0.78] C262019A_Sunshine Pharma 1..4 — hkexnews.hk (#1) `A`
- ✅ **0.699** [on_target=0.98 evidence=0.71] Sunshine Lake Pharma Co., Ltd. Showcases Three Innovative ... — marketscreener.com (#2) `A`
- ❌ low_evidence **0.4247** [on_target=0.91 evidence=0.47] 東陽光薬（06887.HK）の3種類の創薬が2026年AACR年次総会で発表 — moomoo.com (#7) `A`
- ❌ low_on_target **0.0561** [on_target=0.17 evidence=0.33] AACR Annual Meeting 2026 – Post-event summary — insights.bio (#4)
- ❌ low_on_target **0.0308** [on_target=0.13 evidence=0.24] AACR DRUG DISCOVERY AND DEVELOPMENT ( ... — aacr.org (#6)
- ❌ low_on_target **0.0137** [on_target=0.05 evidence=0.27] Advances in antibody-drug conjugates in cancer - PMC - NIH — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0024** [on_target=0.04 evidence=0.06] AACR 2026: Emerging Antibody-Drug Conjugates for the ... — adcreview.com (#10)
- ❌ low_on_target **0.0016** [on_target=0.16 evidence=0.01] AACR 2026 — medical.emdserono.com (#9)
- ❌ low_on_target **0.0005** [on_target=0.03 evidence=0.02] Annual Meeting 2026 Session Recaps Archives — aacrmeetingnews.org (#8)

## q059

**Objective:** HEC234055 in vivo animal models and results: cell-line xenograft (CDX), patient-derived xenograft (PDX), syngeneic, orthotopic, genetically engineered models  
**Target sent:** HEC234055 · anchors ['HEC234055']

**q059-2** `HEC234055 PDX model` → kept 2/10, jev 378 ms

- ✅ **0.7469** [on_target=0.97 evidence=0.77] [PDF] C262019A_Sunshine Pharma 1..4 — stockn.xueqiu.com (#7) `A`
- ✅ **0.7056** [on_target=0.98 evidence=0.72] Sunshine Lake Pharma Co., Ltd. Showcases Three Innovative ... — marketscreener.com (#6) `A`
- ❌ low_on_target **0.0143** [on_target=0.13 evidence=0.11] Establishment of Patient-derived Xenografts (PDX) Models ... — mdanderson.org (#9)
- ❌ low_on_target **0.0125** [on_target=0.05 evidence=0.25] PDX models / CancerTools.org — cancertools.org (#10)
- ❌ low_on_target **0.0098** [on_target=0.05 evidence=0.20] Explore PDX Models by Indication — xenograft.org (#2)
- ❌ low_on_target **0.0045** [on_target=0.08 evidence=0.06] PDX Model Database Registration — crownbio.com (#1)
- ❌ low_on_target **0.0043** [on_target=0.08 evidence=0.05] PDX Models - PDXNet — pdxnetwork.org (#4)
- ❌ low_on_target **0.0016** [on_target=0.08 evidence=0.02] Cancer Research: PDX Model Studies & Articles / Certis — certisoncology.com (#5)
- ❌ low_on_target **0.0002** [on_target=0.07 evidence=0.00] {{ngMeta['og:title']}} — bio.tools (#3)
- ❌ low_on_target **0.0** [on_target=0.05 evidence=0.00] Development of an automated 3D high content cell screening ... — sciencedirect.com (#8)

**q059-3** `HEC234055 syngeneic model` → kept 2/10, jev 380 ms

- ✅ **0.7404** [on_target=0.97 evidence=0.76] C262019A_Sunshine Pharma 1..4 — hkexnews.hk (#1) `A`
- ✅ **0.6794** [on_target=0.98 evidence=0.69] Three innovative drugs showcased at the 2026 AACR Annual ... — moomoo.com (#4) `A`
- ❌ low_on_target **0.0122** [on_target=0.05 evidence=0.24] Syngeneic Mouse Models for Immuno-Oncology Research — medicilon.com (#9)
- ❌ low_on_target **0.0118** [on_target=0.05 evidence=0.24] Syngeneic Models — biocytogen.com (#7)
- ❌ low_on_target **0.0083** [on_target=0.05 evidence=0.17] Syngeneic Model Data - Charles River Laboratories — criver.com (#8)
- ❌ low_on_target **0.0047** [on_target=0.04 evidence=0.12] Syngeneic Cancer Models: Accelerating Discoveries and Innovations in Oncology — crownbio.com (#5)
- ❌ low_on_target **0.0009** [on_target=0.04 evidence=0.02] Cyagen Mouse Model Library / Humanized & Disease Models — cyagen.com (#10)
- ❌ low_on_target **0.0006** [on_target=0.19 evidence=0.00] BioProject — ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0004** [on_target=0.03 evidence=0.01] 022505 — jax.org (#6)
- ❌ low_on_target **0.0003** [on_target=0.05 evidence=0.01] Syngeneic Models - Xenograft Model Database — xenograft.org (#2)

**q059-5** `HEC234055 genetically engineered mouse model` → ABSTAIN, jev 382 ms

- ❌ low_on_target **0.022** [on_target=0.11 evidence=0.20] Resource Page — wagnerlab.net (#4)
- ❌ low_on_target **0.0091** [on_target=0.07 evidence=0.13] Find Your Research Mouse Model 丨 ... — en.gempharmatech.com (#3)
- ❌ low_on_target **0.0059** [on_target=0.04 evidence=0.15] Genetically Engineered Rodent Models and Humanized Mice — taconic.com (#10)
- ❌ low_on_target **0.004** [on_target=0.05 evidence=0.08] Mouse Model Generation & Catalog / 14,774+ Lines — genetargeting.com (#7)
- ❌ low_on_target **0.0023** [on_target=0.05 evidence=0.05] Genetically Engineered Mouse Models — gempharmatech.com (#9)
- ❌ low_on_target **0.0017** [on_target=0.04 evidence=0.04] Find Your Research Mouse Model 丨 GemPharmatech — en.gempharmatech.com (#1)
- ❌ low_on_target **0.0009** [on_target=0.02 evidence=0.05] MMRRC Repository — mmrrc.org (#5)
- ❌ low_on_target **0.0007** [on_target=0.03 evidence=0.02] International Mouse Strain Resource — findmice.org (#2)
- ❌ low_on_target **0.0007** [on_target=0.04 evidence=0.02] Cyagen Mouse Model Library / Humanized & Disease Models — cyagen.com (#8)
- ❌ low_on_target **0.0002** [on_target=0.03 evidence=0.01] All Catalog Mouse Models - Ingenious targeting laboratory — genetargeting.com (#6)

**q059-4** `HEC234055 orthotopic pancreatic model` → kept 1/10, jev 428 ms

- ✅ **0.699** [on_target=0.98 evidence=0.71] [PDF] E262019A_Sunshine Pharma 1..4 - HKEXnews — www1.hkexnews.hk (#4) `A`
- ❌ low_on_target **0.0437** [on_target=0.10 evidence=0.44] Orthotopic and heterotopic murine models of pancreatic ... — pubmed.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0399** [on_target=0.09 evidence=0.44] Orthotopic and Heterotopic Murine Models of Pancreatic ... — frontiersin.org (#8)
- ❌ low_on_target **0.0317** [on_target=0.07 evidence=0.45] An Orthotopic Resectional Mouse Model of Pancreatic Cancer - PubMed — pubmed.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0271** [on_target=0.07 evidence=0.39] Clinically relevant orthotopic pancreatic cancer models for ... — pubmed.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0254** [on_target=0.06 evidence=0.42] Orthotopic models of human pancreatic cancer - PubMed — pubmed.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0222** [on_target=0.06 evidence=0.37] Inoculation of Pan02 cells produces tumor nodules in mouse ... — journals.plos.org (#10)
- ❌ low_on_target **0.0204** [on_target=0.06 evidence=0.34] Clinically relevant orthotopic pancreatic cancer models ... - PMC — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0142** [on_target=0.06 evidence=0.24] LP – Orthotopic Tumor Models — td2inc.com (#1)
- ❌ low_on_target **0.0103** [on_target=0.04 evidence=0.26] Orthotopic Models — dda.creative-bioarray.com (#3)

**q059-1** `HEC234055 HNSCC xenograft` → kept 1/10, jev 424 ms

- ✅ **0.7049** [on_target=0.97 evidence=0.73] [PDF] E262019A_Sunshine Pharma 1..4 - HKEXnews — www1.hkexnews.hk (#1) `A`
- ❌ low_on_target **0.2772** [on_target=0.36 evidence=0.77] A controlled trial of HNSCC patient-derived xenografts reveals broad efficacy of PI3Kα inhibition in — pubmed.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.1349** [on_target=0.19 evidence=0.71] New patient derived head and neck cancer xenograft (PDX ... — epo-berlin.com (#8)
- ❌ low_on_target **0.028** [on_target=0.10 evidence=0.28] The value of subcutaneous xenografts for individualised radiotherapy in HNSCC: robust gene signature — freidok.uni-freiburg.de (#9)
- ❌ low_on_target **0.0264** [on_target=0.07 evidence=0.38] Head and neck squamous cell carcinoma cell lines: Established models and rationale for selection — scispace.com (#5)
- ❌ low_on_target **0.0164** [on_target=0.06 evidence=0.27] Lung (Non-Small Cell) Cancer CDX Models — xenograft.org (#10)
- ❌ low_on_target **0.0083** [on_target=0.08 evidence=0.10] Xenograft Model Database — xenograft.org (#3)
- ❌ low_on_target **0.0056** [on_target=0.07 evidence=0.08] Head and neck squamous cell carcinoma cell lines: Established models and rationale for selection — deepblue.lib.umich.edu (#6)
- ❌ low_on_target **0.0052** [on_target=0.04 evidence=0.13] Xenograft Cell Line Reference Database — taconic.com (#2)
- ❌ low_on_target **0.0015** [on_target=0.09 evidence=0.02] Human Xenograft Models_GemPharmatech — gempharmatech.com (#4)

## q060

**Objective:** EOM613 sponsor development stage indication public source  
**Target sent:** EOM613 Crohn's disease / EOM613 · anchors ["EOM613 Crohn's disease", 'EOM613']

**q060-2** `EOM613 Crohn's disease Phase 2 initiation 2026` → kept 5/10, jev 344 ms

- ✅ **0.9604** [on_target=0.98 evidence=0.98] EOM Pharmaceutical Holdings Reports Promising Preclinical — globenewswire.com (#1) `A`
- ✅ **0.9183** [on_target=0.97 evidence=0.95] EOM Pharmaceutical Holdings Reports FDA Clearance of ... — globenewswire.com (#2) `A`
- ✅ **0.9183** [on_target=0.97 evidence=0.95] EOM Pharmaceuticals — biobase.whitefordresearch.com (#3) `A`
- ✅ **0.8624** [on_target=0.98 evidence=0.88] EOM Pharmaceutical Holdings Provides an Update on its Lead Drug Candidate EOM613 — prnewswire.com (#6) `A`
- ✅ **0.8032** [on_target=0.96 evidence=0.84] reticulose (EOM613) / EOM Pharma — delta.larvol.com (#8) `A`
- ❌ max_keep **0.6467** [on_target=0.97 evidence=0.67] Methods of treating inflammatory bowel diseases — patents.google.com (#4) `A`
- ❌ low_evidence **0.3321** [on_target=0.81 evidence=0.41] [PDF] EOM PHARMACEUTICAL HOLDINGS, INC. - OTC Markets — otcmarkets.com (#10) `A`
- ❌ low_on_target **0.2769** [on_target=0.39 evidence=0.71] Crohn's disease / pharmaphorum — pharmaphorum.com (#9)
- ❌ low_on_target **0.062** [on_target=0.20 evidence=0.31] Highlights of the 2026 European Crohn's and Colitis Conference — academic.oup.com (#7)
- ❌ low_on_target **0.0005** [on_target=0.03 evidence=0.02] Clinical Trials / EOM Pharmaceuticals, Inc. — eompharma.com (#5)

**q060-1** `EOM613 Crohn's disease trial current status` → kept 5/10, jev 360 ms

- ✅ **0.9636** [on_target=0.98 evidence=0.98] EOM Pharmaceutical Holdings Reports Promising Preclinical — globenewswire.com (#1) `A`
- ✅ **0.9636** [on_target=0.98 evidence=0.98] EOM Pharmaceutical plans 15-20-patient Phase II Crohn's disease ... — sahmcapital.com (#4) `A`
- ✅ **0.9118** [on_target=0.97 evidence=0.94] EOM Pharmaceuticals — biobase.whitefordresearch.com (#6) `A`
- ✅ **0.9053** [on_target=0.97 evidence=0.93] EOM Pharmaceutical Holdings Reports FDA Clearance of ... — globenewswire.com (#3) `A`
- ✅ **0.8754** [on_target=0.98 evidence=0.89] EOM Pharmaceutical Holdings Provides an Update on its Lead Drug Candidate EOM613 — prnewswire.com (#7) `A`
- ❌ max_keep **0.8245** [on_target=0.97 evidence=0.85] ImmunoCellular Therapeutics Ltd. - Drug pipelines, Patents, Clinical ... — synapse.patsnap.com (#8) `A`
- ❌ max_keep **0.714** [on_target=0.85 evidence=0.84] EOM Pharmaceuticals Appoints Business Veteran Wayne I. Danson ... — businesswire.com (#10) `A`
- ❌ low_on_target **0.0817** [on_target=0.14 evidence=0.58] DataLookout — Clinical Trial Intelligence — dashboard.datalookout.com (#2)
- ❌ low_on_target **0.0047** [on_target=0.07 evidence=0.07] Clinical Trials for Crohn's Disease - NIDDK — niddk.nih.gov (#9)
- ❌ low_on_target **0.0004** [on_target=0.02 evidence=0.02] Clinical Trials / EOM Pharmaceuticals, Inc. — eompharma.com (#5)

**q060-3** `EOM613 Crohn's disease clinical trial registry` → kept 5/10, jev 340 ms

- ✅ **0.9636** [on_target=0.98 evidence=0.98] EOM Pharmaceutical Holdings Reports Promising Preclinical — globenewswire.com (#1) `A`
- ✅ **0.9312** [on_target=0.97 evidence=0.96] EOM Pharmaceutical Holdings Reports FDA Clearance of ... — globenewswire.com (#9) `A`
- ✅ **0.869** [on_target=0.98 evidence=0.89] EOM Pharmaceutical Holdings Provides an Update on its Lead Drug Candidate EOM613 — prnewswire.com (#2) `A`
- ✅ **0.8128** [on_target=0.96 evidence=0.85] ImmunoCellular Therapeutics Ltd. - Drug pipelines, Patents, Clinical ... — synapse.patsnap.com (#4) `A`
- ✅ **0.7854** [on_target=0.95 evidence=0.83] FDA Clears IND for EOM613 Trial in Cancer Cachexia Patients — clinicaltrialvanguard.com (#10) `A`
- ❌ max_keep **0.7728** [on_target=0.97 evidence=0.80] reticulose (EOM613) / EOM Pharma — delta.larvol.com (#3) `A`
- ❌ max_keep **0.6111** [on_target=0.97 evidence=0.63] Methods of treating inflammatory bowel diseases — patents.google.com (#8) `A`
- ❌ low_on_target **0.0007** [on_target=0.07 evidence=0.01] Clinical Trials in the European Union - EMA — euclinicaltrials.eu (#5)
- ❌ low_on_target **0.0003** [on_target=0.04 evidence=0.01] Find Studies / ClinicalTrials.gov — clinicaltrials.gov (#7)
- ❌ low_on_target **0.0001** [on_target=0.04 evidence=0.00] ICTRP Search Portal - World Health Organization (WHO) — who.int (#6)

## q061

**Objective:** FG-3149 sponsor development stage indication public source  
**Target sent:** FG-3149 · anchors ['FG-3149']

**q061-1** `FG-3149 sponsor development stage` → ABSTAIN, jev 350 ms

- ❌ low_on_target **0.3776** [on_target=0.59 evidence=0.64] SCGE Platform - Gene Therapy Clinical Trials — scge.mcw.edu (#6)
- ❌ low_on_target **0.315** [on_target=0.54 evidence=0.58] Drug Development Pipeline / CFF Clinical Trials Tool - CF Foundation — apps.cff.org (#9)
- ❌ low_on_target **0.064** [on_target=0.64 evidence=0.10] ���������������������� — cdn.clinicaltrials.gov (#10)
- ❌ low_on_target **0.0384** [on_target=0.48 evidence=0.08] ac93704f-8e33-43ba-8b56-3d61092ff1d9.xml — accessdata.fda.gov (#1)
- ❌ low_on_target **0.0375** [on_target=0.15 evidence=0.25] Fundamental Global — fundamentalglobal.com (#8)
- ❌ low_on_target **0.0308** [on_target=0.14 evidence=0.22] State of Illinois Uniform Notice of Funding Opportunity ( ... — omb.illinois.gov (#5)
- ❌ low_on_target **0.0189** [on_target=0.27 evidence=0.07] User's Guide — accessdata.fda.gov (#4)
- ❌ low_on_target **0.0153** [on_target=0.20 evidence=0.08] Drug Development Pipeline Archive — curefa.org (#3)
- ❌ low_on_target **0.0014** [on_target=0.14 evidence=0.01] Other News To Note — bioworld.com (#7)
- ❌ low_on_target **0.0** [on_target=0.08 evidence=0.00] 404 — gempharmatech.com (#2)

**q061-2** `FG-3149 Crohn's disease` → kept 4/10, jev 322 ms

- ✅ **0.7508** [on_target=0.85 evidence=0.88] Efficacy and safety of filgotinib as induction and maintenance therapy for Crohn's disease (DIVERSIT — thelancet.com (#5)
- ✅ **0.7395** [on_target=0.87 evidence=0.85] Combined Phase 3, Double-blind, Randomized, Placebo-Controlled Studies Evaluating the Efficacy and S — medifind.com (#10)
- ✅ **0.6434** [on_target=0.97 evidence=0.66] Mechanical stress-induced connective tissue growth factor ... — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.6208** [on_target=0.97 evidence=0.64] Mechanical stress-induced connective tissue growth factor ... — researchexperts.utmb.edu (#1) `A`
- ❌ low_on_target **0.0414** [on_target=0.62 evidence=0.07] ������������ — cdn.clinicaltrials.gov (#6)
- ❌ low_on_target **0.033** [on_target=0.55 evidence=0.06] ����������� — cdn.clinicaltrials.gov (#7)
- ❌ low_on_target **0.021** [on_target=0.09 evidence=0.23] Intestinal Fibrosis in Crohn's Disease - PMC - NIH — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0154** [on_target=0.22 evidence=0.07] New weapons for the management of perianal Crohn's disease — oamonitor.ireland.openaire.eu (#3)
- ❌ low_on_target **0.0071** [on_target=0.03 evidence=0.24] Crohn Disease - Gastroenterology — merckmanuals.com (#9)
- ❌ low_on_target **0.0069** [on_target=0.08 evidence=0.09] Serum biomarkers of fibrostenotic Crohn's disease — onlinelibrary.wiley.com (#4)

**q061-3** `FG-3149 FibroGen clinical development` → ABSTAIN, jev 411 ms

- ❌ low_on_target **0.0161** [on_target=0.22 evidence=0.07] FibroGen wields axe as pancreatic cancer drug is canned — pharmaphorum.com (#10)
- ❌ low_on_target **0.0085** [on_target=0.51 evidence=0.02] FibroGen Inc. (NASDAQ:FGEN) : Ptab Cases :: Law360 — law360.co.uk (#2)
- ❌ low_on_target **0.0067** [on_target=0.10 evidence=0.07] Our Partners - FibroGen — fibrogen.com (#4)
- ❌ low_on_target **0.004** [on_target=0.07 evidence=0.06] Kyntra Bio - Wikipedia — en.wikipedia.org (#3)
- ❌ low_on_target **0.0035** [on_target=0.13 evidence=0.03] FibroGen : Corporate Presentation - September 2025 — marketscreener.com (#6)
- ❌ low_on_target **0.0029** [on_target=0.08 evidence=0.04] FibroGen / Drug Developments / Pipeline Prospector — pharmacompass.com (#7)
- ❌ low_on_target **0.0028** [on_target=0.07 evidence=0.04] FibroGen Reports First Quarter 2024 Financial Results — investor.kyntrabio.com (#1)
- ❌ low_on_target **0.0028** [on_target=0.07 evidence=0.04] FibroGen (FGEN) Drug Pipeline – Trials, Approvals & Status Updates — tipranks.com (#9)
- ❌ low_on_target **0.0021** [on_target=0.04 evidence=0.05] FibroGen, Inc. (NASDAQ:FGEN) Q1 2024 Earnings Conference Call ... — reportify-1252068037.cos.ap-beijing.myqcloud.com (#5)
- ❌ low_on_target **0.002** [on_target=0.05 evidence=0.04] FibroGen Reports Third Quarter 2024 Financial Results - Kyntra Bio — investor.kyntrabio.com (#8)

## q062

**Objective:** HDM-3018 sponsor Huadong Medicine Co. Ltd., development stage Preclinical, and indication Inflammatory Bowel Disease  
**Target sent:** HDM-3018 · anchors ['HDM-3018']

**q062-1** `HDM-3018 Huadong Medicine sponsor` → kept 2/10, jev 484 ms

- ✅ **0.9056** [on_target=0.95 evidence=0.95] Huadong Medicine Co., Ltd. — static.cninfo.com.cn (#2) `A`
- ✅ **0.8134** [on_target=0.98 evidence=0.83] HDM3018 - Drug Targets, Indications, Patents — synapse.patsnap.com (#1) `A`
- ❌ low_on_target **0.1116** [on_target=0.54 evidence=0.21] Huadong Medicine Co., Ltd. - Drug pipelines, Patents, ... — synapse.patsnap.com (#5)
- ❌ low_on_target **0.0256** [on_target=0.64 evidence=0.04] NMPA Database — nmpa.gov.cn (#8)
- ❌ low_on_target **0.0075** [on_target=0.16 evidence=0.05] Huadong Medicine Group - CGE — cgeinc.com (#4)
- ❌ low_on_target **0.0042** [on_target=0.21 evidence=0.02] Huadong Medicine — en.huadongmedicine.com (#6)
- ❌ low_on_target **0.004** [on_target=0.11 evidence=0.04] Huadong Medicine / Drug Developments / Pipeline Prospector — pharmacompass.com (#9)
- ❌ low_on_target **0.0017** [on_target=0.10 evidence=0.02] Company News — en.huadongmedicine.com (#3)
- ❌ low_on_target **0.0015** [on_target=0.11 evidence=0.01] Products / Huadong Medicine — en.huadongmedicine.com (#7)
- ❌ low_on_target **0.0003** [on_target=0.08 evidence=0.00] Your Request Originates from an Undeclared Automated Tool — sec.gov (#10)

**q062-3** `HDM-3018 inflammatory bowel disease indication` → kept 1/10, jev 356 ms

- ✅ **0.944** [on_target=0.98 evidence=0.96] HDM3018 - Drug Targets, Indications, Patents - Synapse — synapse.patsnap.com (#1) `A`
- ❌ low_on_target **0.344** [on_target=0.60 evidence=0.57] US20250243280A1 - Methods of treating gastrointestinal ... — patents.google.com (#6)
- ❌ low_on_target **0.2773** [on_target=0.53 evidence=0.52] Pharmaceutical compositions for preventing or treating ... — patents.google.com (#10)
- ❌ low_on_target **0.0261** [on_target=0.09 evidence=0.29] Digestive enzyme – Knowledge and References — taylorandfrancis.com (#4)
- ❌ low_on_target **0.0165** [on_target=0.31 evidence=0.05] �fx��zI�zG`��AN��2g���W눷ov�P��w{����$�KĝA������wTc�w���Z��č{�Fy�e�+�]m�\�0tnjBԯ�d���)����ŀ&�˴UV31��$ — korea.kr (#8)
- ❌ low_on_target **0.0155** [on_target=0.05 evidence=0.31] Efficacy and Safety of Advanced Oral Small Molecules for ... — pubmed.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0099** [on_target=0.33 evidence=0.03] Graphical Abstract — academic.oup.com (#3)
- ❌ low_on_target **0.0005** [on_target=0.15 evidence=0.00] register — academic.oup.com (#2)
- ❌ low_on_target **0.0005** [on_target=0.07 evidence=0.01] Study Details Page — abbvieclinicaltrials.com (#5)
- ❌ low_on_target **0.0003** [on_target=0.05 evidence=0.01] the SPIRIT Consensus From the IOIBD — sciencedirect.com (#7)

**q062-2** `HDM-3018 development stage` → kept 1/10, jev 473 ms

- ✅ **0.9702** [on_target=0.98 evidence=0.99] HDM3018 - Drug Targets, Indications, Patents - Synapse — synapse.patsnap.com (#1) `A`
- ❌ low_on_target **0.0058** [on_target=0.29 evidence=0.02] Pipeline / 3D Medicines Inc. - Investor Relations — ir.3d-medicines.com (#8)
- ❌ low_on_target **0.0015** [on_target=0.23 evidence=0.01] Improvements Incorporated in the new HDM- 4 Version 2 — sciencedirect.com (#3)
- ❌ low_on_target **0.0007** [on_target=0.20 evidence=0.00] Bloomberg — bloomberg.com (#2)
- ❌ low_on_target **0.0002** [on_target=0.07 evidence=0.00] Study Details Page — abbvieclinicaltrials.com (#4)
- ❌ low_on_target **0.0002** [on_target=0.03 evidence=0.01] [PDF] The SRI hierarchical development methodology (HDM ... - GovInfo — govinfo.gov (#10)
- ❌ low_on_target **0.0001** [on_target=0.04 evidence=0.00] Profiles of Major Products under Development — sumitomo-pharma.com (#9)
- ❌ low_on_target **0.0** [on_target=0.02 evidence=0.00] HDM - Support — h3c.com (#5)
- ❌ low_on_target **0.0** [on_target=0.03 evidence=0.00] Coming Soon — HDM System Corporation — hdm-sys.com (#6)
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] Electronics News & Analysis - EE Times — eetimes.com (#7)

## q063

**Objective:** Granisetron in Head and Neck Cancer: clinical trial population, biomarker or severity selection, line of therapy, and required prior treatment  
**Target sent:** Granisetron · anchors ['Granisetron']

**q063-2** `Granisetron head and neck cancer Phase 2 prior treatment` → kept 5/10, jev 402 ms

- ✅ **0.7395** [on_target=0.87 evidence=0.85] NRG-HN005 1 Version Date: August 21, 2023 ... — cdn.clinicaltrials.gov (#9) `A`
- ✅ **0.7178** [on_target=0.97 evidence=0.74] Pharmacokinetics, safety, and efficacy of APF530 (extended-release ... — pmc.ncbi.nlm.nih.gov (#8) `A`
- ✅ **0.7081** [on_target=0.97 evidence=0.73] Difference in the emetic control among highly emetogenic ... — pmc.ncbi.nlm.nih.gov (#7) `A`
- ✅ **0.6904** [on_target=0.95 evidence=0.73] Comparison of an extended-release formulation of granisetron ... — link.springer.com (#3) `A`
- ✅ **0.589** [on_target=0.93 evidence=0.63] PMH CLINICAL PRACTICE GUIDELINES TEMPLATE — uhn.ca (#5) `A`
- ❌ max_keep **0.5511** [on_target=0.99 evidence=0.56] Granisetron Monograph for Professionals — drugs.com (#1) `A`
- ❌ max_keep **0.5445** [on_target=0.99 evidence=0.55] Granisetron: An Update on its Clinical Use in the Management ... — academic.oup.com (#10) `A`
- ❌ max_keep **0.5312** [on_target=0.83 evidence=0.64] A Hematology Oncology Wiki — hemonc.org (#4) `A`
- ❌ low_on_target **0.0539** [on_target=0.16 evidence=0.34] Antiemetic prophylaxis for chemoradiotherapy-induced nausea and vomiting in locally advanced head an — ncbi.nlm.nih.gov (#6) `A`
- ❌ low_on_target **0.0016** [on_target=0.02 evidence=0.08] Clinical Trial 23691 / Moffitt — moffitt.org (#2)

**q063-3** `Granisetron head and neck cancer biomarker ECOG` → kept 5/10, jev 414 ms

- ✅ **0.7774** [on_target=0.98 evidence=0.79] a randomized controlled trial - IRIS UniCa - Università di Cagliari — iris.unica.it (#9) `A`
- ✅ **0.6946** [on_target=0.91 evidence=0.76] A Hematology Oncology Wiki — hemonc.org (#8) `A`
- ✅ **0.6467** [on_target=0.97 evidence=0.67] Efficacy of the granisetron transdermal system for ... — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.6434** [on_target=0.97 evidence=0.66] Gestione di nausea e vomito nel paziente oncologico. Utilizzo ... — iris.uniupo.it (#1) `A`
- ✅ **0.6273** [on_target=0.97 evidence=0.65] Pharmacokinetics, safety, and efficacy of APF530 (extended-release ... — pmc.ncbi.nlm.nih.gov (#10) `A`
- ❌ max_keep **0.6176** [on_target=0.97 evidence=0.64] Gestione di nausea e vomito nel paziente oncologico. ... — iris.uniupo.it (#2) `A`
- ❌ max_keep **0.5728** [on_target=0.96 evidence=0.60] results of a prospective, randomized, double-blind, ... — pmc.ncbi.nlm.nih.gov (#3) `A`
- ❌ low_evidence **0.3718** [on_target=0.97 evidence=0.38] Research Review — researchreview.co.nz (#4) `A`
- ❌ low_evidence **0.3658** [on_target=0.98 evidence=0.37] Granisetron: An Update on its Clinical Use in the Management ... — academic.oup.com (#6) `A`
- ❌ low_on_target **0.0016** [on_target=0.03 evidence=0.05] Head and neck cancer Archives — ecog-acrin.org (#7)

**q063-4** `Granisetron Kyowa Kirin head and neck cancer trial` → kept 5/10, jev 413 ms

- ✅ **0.9504** [on_target=0.99 evidence=0.96] Comparison of Granisetron, Ondansetron, and Tropisetron ... — pubmed.ncbi.nlm.nih.gov (#7) `A`
- ✅ **0.918** [on_target=0.98 evidence=0.94] a randomized controlled trial - IRIS UniCa - Università di Cagliari — iris.unica.it (#4) `A`
- ✅ **0.9114** [on_target=0.98 evidence=0.93] activity and safety of transdermal granisetron in preventing ... — simul-europe.com (#6) `A`
- ✅ **0.8362** [on_target=0.98 evidence=0.85] Manifest Anxiety Scale for evaluation of effects of granisetron in chemotherapy with CDDP and 5FU fo — pubmed.ncbi.nlm.nih.gov (#9) `A`
- ✅ **0.6892** [on_target=0.98 evidence=0.70] [PDF] SANCUSO (granisetron transdermal system) - Kyowa Kirin — kkna.kyowakirin.com (#2) `A`
- ❌ max_keep **0.5504** [on_target=0.96 evidence=0.57] © Kyowa Hakko Kirin Co., Ltd. — ir.kyowakirin.com (#5) `A`
- ❌ max_keep **0.459** [on_target=0.85 evidence=0.54] Granisetron - Drug Targets, Indications, Patents — synapse.patsnap.com (#3) `A`
- ❌ low_evidence **0.4344** [on_target=0.98 evidence=0.44] Safety Study of Electrocardiogram (ECG) Effects of Sancuso ... — clinicaltrials.gov (#10) `A`
- ❌ low_evidence **0.4192** [on_target=0.96 evidence=0.44] Kyowa Kirin, Inc. — trial.medpath.com (#1) `A`
- ❌ low_evidence **0.379** [on_target=0.98 evidence=0.39] Granisetron Hydrochloride - NCI — cancer.gov (#8) `A`

**q063-1** `Granisetron recurrent metastatic head and neck cancer clinical trial eligibility` → kept 1/10, jev 327 ms

- ✅ **0.833** [on_target=0.98 evidence=0.85] Granisetron Extended Release Injection (GERSC) for the Prevention of Chemotherapy-induced Nausea and — clinicaltrials.gov (#8) `A`
- ❌ low_evidence **0.2492** [on_target=0.89 evidence=0.28] Granisetron, Aprepitant, and Dexamethasone in Preventing Nausea ... — clinicaltrials.gov (#10) `A`
- ❌ low_on_target **0.1147** [on_target=0.16 evidence=0.72] NCT00588770 — loyolamedicine.org (#1)
- ❌ low_on_target **0.0858** [on_target=0.13 evidence=0.66] A Study for Participants With Recurrent or Metastatic ... — clinicaltrials.gov (#2)
- ❌ low_on_target **0.0288** [on_target=0.06 evidence=0.48] A Study for Patients With Recurrent or Metastatic Squamous Cell Head and Neck Cancer — clinicaltrials.gov (#6)
- ❌ low_on_target **0.0131** [on_target=0.04 evidence=0.33] Clinical Trial 23276 — moffitt.org (#4)
- ❌ low_on_target **0.0128** [on_target=0.04 evidence=0.32] Clinical Trials — med.stanford.edu (#5)
- ❌ low_on_target **0.0031** [on_target=0.03 evidence=0.10] Head and Neck Cancer Clinical Trials — ccr.cancer.gov (#9)
- ❌ low_on_target **0.0013** [on_target=0.02 evidence=0.06] Surgery Clinical Trials — med.stanford.edu (#7)
- ❌ low_on_target **0.0002** [on_target=0.01 evidence=0.02] Axitinib in Treating Patients with Recurrent or Metastatic Head and ... — cancer.gov (#3)

## q064

**Objective:** HPV Vaccine (HAd5 Vector) in Head and Neck Cancer: clinical trial population, biomarker or severity selection, line of therapy, and required prior treatment  
**Target sent:** HPV Vaccine (HAd5 Vector) ImmunityBio / HAd5 · anchors ['HPV Vaccine (HAd5 Vector) ImmunityBio', 'HAd5']

**q064-1** `HPV Vaccine (HAd5 Vector) ImmunityBio head and neck cancer clinical trial eligibility` → kept 5/10, jev 359 ms

- ✅ **0.967** [on_target=0.98 evidence=0.99] NCT07628062 / Phase 2 Study of NAI, HPV Vaccine, and Nab ... — clinicaltrials.gov (#3) `A`
- ✅ **0.8323** [on_target=0.87 evidence=0.96] Clinical Trials — mayo.edu (#5)
- ✅ **0.7936** [on_target=0.93 evidence=0.85] Human Papillomavirus — immunitybio.com (#4) `A`
- ✅ **0.7763** [on_target=0.85 evidence=0.91] HPV+ / HPV- 2nd Line Head & Neck Cancer — immunitybio.com (#2)
- ✅ **0.7424** [on_target=0.87 evidence=0.85] Patients & Caregivers — immunitybio.com (#1)
- ❌ low_on_target **0.6578** [on_target=0.69 evidence=0.95] Safety Study of HPV DNA Vaccine to Treat Head and Neck Cancer Patients — clinicaltrials.gov (#8)
- ❌ low_on_target **0.5339** [on_target=0.57 evidence=0.94] Therapeutic vaccines targeting HPV epitopes in human ... - PMC — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0392** [on_target=0.25 evidence=0.16] Current landscape of clinical trials for HPV-positive head and neck ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0291** [on_target=0.09 evidence=0.32] Head and Neck Cancer Clinical Trials — ccr.cancer.gov (#7)
- ❌ low_on_target **0.0148** [on_target=0.06 evidence=0.25] Head and Neck Cancer - Cancer Research Institute — cancerresearch.org (#6)

**q064-2** `HPV Vaccine (HAd5 Vector) ImmunityBio HPV biomarker head and neck cancer` → kept 2/10, jev 329 ms

- ✅ **0.9344** [on_target=0.97 evidence=0.96] NCT07628062 / Phase 2 Study of NAI, HPV Vaccine, and Nab ... — clinicaltrials.gov (#7) `A`
- ✅ **0.7936** [on_target=0.93 evidence=0.85] Human Papillomavirus — immunitybio.com (#1) `A`
- ❌ low_on_target **0.07** [on_target=0.20 evidence=0.35] Immunotherapeutic strategies in head and neck cancer: challenges ... — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0612** [on_target=0.17 evidence=0.36] Head and neck cancer therapeutic vaccines: a review - Frontiers — frontiersin.org (#6)
- ❌ low_on_target **0.06** [on_target=0.15 evidence=0.40] Immunotherapy Advances in Locally ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.032** [on_target=0.10 evidence=0.32] Head and neck cancers - World Cancer Report — ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0224** [on_target=0.07 evidence=0.32] HPV-Associated Head and Neck Cancer: Molecular and Nano ... - NIH — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0184** [on_target=0.06 evidence=0.31] Molecular Insights into HPV-Driven Head and Neck Cancers - PMC — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.015** [on_target=0.05 evidence=0.30] HPV and head and neck cancers: Towards early diagnosis and ... — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.015** [on_target=0.05 evidence=0.30] Human Papillomavirus: Update in Bridging Basic Science to Clinical ... — onlinelibrary.wiley.com (#9)

**q064-3** `HPV Vaccine (HAd5 Vector) ImmunityBio recurrent metastatic head and neck cancer prior treatment` → kept 1/10, jev 446 ms

- ✅ **0.8153** [on_target=0.93 evidence=0.88] Human Papillomavirus — immunitybio.com (#1) `A`
- ❌ low_on_target **0.1995** [on_target=0.44 evidence=0.45] Therapeutic Vaccination for HPV-Mediated Cancers - PMC - NIH — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.123** [on_target=0.31 evidence=0.40] Immunotherapy for HPV Malignancies - PMC - NIH — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.1118** [on_target=0.26 evidence=0.43] Therapeutic Vaccines for Head and Neck Squamous Cell ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.1** [on_target=0.25 evidence=0.40] Head and Neck Carcinoma Immunotherapy — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0867** [on_target=0.25 evidence=0.35] A Review of Immunotherapy for Head and Neck Cancer - PMC — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0823** [on_target=0.26 evidence=0.32] The current landscape of therapeutic vaccination approaches ... — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0749** [on_target=0.21 evidence=0.36] Head and neck cancer therapeutic vaccines: a review - Frontiers — frontiersin.org (#2)
- ❌ low_on_target **0.0539** [on_target=0.16 evidence=0.34] Driving Progress in Recurrent and Metastatic Head and Neck Cancer — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0392** [on_target=0.12 evidence=0.33] Novel Immunotherapeutic Approaches to Treating HPV-Related ... — pmc.ncbi.nlm.nih.gov (#9)

**q064-4** `HPV Vaccine (HAd5 Vector) ImmunityBio phase 2 trial inclusion criteria` → kept 4/10, jev 344 ms

- ✅ **0.9571** [on_target=0.97 evidence=0.99] NCT07628062 / Phase 2 Study of NAI, HPV Vaccine, and Nab ... — clinicaltrials.gov (#4) `A`
- ✅ **0.816** [on_target=0.90 evidence=0.91] NCT07628062 Nogapendekin alfa inbakicept-pmln HPV16 ... — synapse.patsnap.com (#7) `A`
- ✅ **0.714** [on_target=0.84 evidence=0.85] Patients & Caregivers — immunitybio.com (#1)
- ✅ **0.498** [on_target=0.83 evidence=0.60] Annual Report — ir.immunitybio.com (#5) `A`
- ❌ low_on_target **0.3375** [on_target=0.45 evidence=0.75] Vaccine Therapy in Preventing Human Papillomavirus Infection in ... — cancer.gov (#9)
- ❌ low_on_target **0.1248** [on_target=0.48 evidence=0.26] NCT00478621 / Human Papillomavirus Vaccine Safety & ... — clinicaltrials.gov (#3)
- ❌ low_on_target **0.0994** [on_target=0.42 evidence=0.24] NCT04537156 / Efficacy, Immunogenicity and Safety Study ... — clinicaltrials.gov (#6)
- ❌ low_on_target **0.0347** [on_target=0.13 evidence=0.27] Therapeutic Vaccines for HPV-Associated Cervical Malignancies: A Systematic Review — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.003** [on_target=0.07 evidence=0.04] hAd5-COVID-19-PS — cdn.clinicaltrials.gov (#8) `A`
- ❌ low_on_target **0.0007** [on_target=0.02 evidence=0.03] a phase 2/3, placebo-controlled — cdn.clinicaltrials.gov (#2)


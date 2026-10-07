# Jev inspect: 20261006-174818__jev-jev_v2_k10__on__20261006-174729__parallel-parallel_fast__batch

Config `jev_v2_k10` (per_link), select={"keep_threshold": 0.5, "max_keep": 10, "gates": {"on_target": 0.6, "evidence": 0.5}}. Reasons: {"low_on_target": 327, "kept": 239, "low_evidence": 74}. Answer means: {"on_target": 0.527, "evidence": 0.476}.

Legend: ✅ kept · ❌ dropped (reason) · `A` = mentions the anchor · scores are Jev's answers in [0, 1].

## q001

**Objective:** Tamuzimod safety findings and adverse events in Moderately to severely active ulcerative colitis Ulcerative Colitis  
**Target sent:** Tamuzimod · anchors ['Tamuzimod']

**q001-batch** `Tamuzimod long-term extension safety ulcerative colitis || Tamuzimod maintenance adverse events ulcerative colitis || Tamuzimod UEGW 2024 safety || Tamuzimod open-label extension adverse events` → kept 8/10, jev 365 ms

- ✅ **0.895** [on_target=0.98 evidence=0.91] Tamuzimod in patients with moderately-to-severely active ulcerative colitis: a multicentre, double-b — pubmed.ncbi.nlm.nih.gov (#8) `A`
- ✅ **0.7857** [on_target=0.97 evidence=0.81] [PDF] UEG Week 2024 - CONFERENCE REPORTPEER-REVIEWED — conferences.medicom-publishers.com (#2) `A`
- ✅ **0.7612** [on_target=0.98 evidence=0.78] Tamuzimod delivers promising long-term data in ulcerative colitis — esanum.com (#3) `A`
- ✅ **0.748** [on_target=0.98 evidence=0.76] Tamuzimod in patients with moderately-to-severely active ulcerative ... — sciencedirect.com (#6) `A`
- ✅ **0.6666** [on_target=0.99 evidence=0.67] Ventyx Biosciences Presents New 52-Week Results from the — globenewswire.com (#1) `A`
- ✅ **0.582** [on_target=0.97 evidence=0.60] A Randomized Controlled Pilot Study Evaluating the Safety ... — europepmc.org (#9) `A`
- ✅ **0.5792** [on_target=0.96 evidence=0.60] Tamuzimod in patients with moderately-to-severely active ... — sciencedirect.com (#5) `A`
- ✅ **0.5422** [on_target=0.98 evidence=0.55] Ventyx Biosciences Presents New 52-Week Results from ... — biospace.com (#10) `A`
- ❌ low_on_target **0.1083** [on_target=0.26 evidence=0.42] Medline ® Abstracts for References 78-84 of 'Management of moderate to severe ulcerative colitis in  — uptodate.com (#7)
- ❌ low_on_target **0.056** [on_target=0.23 evidence=0.24] Cardiovascular events observed among patients in the etrasimod clinical programme: an integrated saf — bmjopengastro.bmj.com (#4)

## q002 (competitor objective)

**Objective:** C. difficile Infection Episode: Receipt of SOC Antibacterial Therapy (Fidaxomicin, Vancomycin, Metronidazole) With Planned Duration 10–25 Days at Time of IMP Administration competing agents in the same mechanistic class as AZD5148, including Monoclonal Antibody targeting Clostridioides Difficile Toxin B TcdB  
**Target sent:** drugs competing with AZD5148: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['AZD5148']

**q002-batch** `AZD5148 competing anti-TcdB monoclonal antibodies Phase 2 2026 || AZD5148 TcdB antibody competitors licensing || AZD5148 RePreve comparator anti-toxin antibody || AZD5148 TcdB epitope binding mechanism || AZD5148 clinical pipeline TcdB antibody 2026` → kept 8/10, jev 429 ms

- ✅ **0.6206** [on_target=0.95 evidence=0.65] Comparative Efficacy of Vancomycin and Fidaxomicin ... — medrxiv.org (#4)
- ✅ **0.6049** [on_target=0.95 evidence=0.64] Zinplava (bezlotoxumab) News - LARVOL Sigma — sigma.larvol.com (#8) `A`
- ✅ **0.5922** [on_target=0.94 evidence=0.63] Comparative Efficacy of Vancomycin and Fidaxomicin Regimens for the Prevention of Recurrent Clostrid — medrxiv.org (#9)
- ✅ **0.5766** [on_target=0.92 evidence=0.63] The monoclonal antibody AZD5148 confers broad protection against TcdB-diverse Clostridioides diffici — pubmed.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.382** [on_target=0.73 evidence=0.52] The monoclonal antibody AZD5148 confers broad ... — semanticscholar.org (#10) `A`
- ✅ **0.3715** [on_target=0.71 evidence=0.52] Ombetoxabart (AZD-5148) / Anti-TcdB Monoclonal Antibody / MedChemExpress — medchemexpress.com (#2) `A`
- ✅ **0.3417** [on_target=0.67 evidence=0.51] P-1055. Anti-Toxin B Neutralizing Monoclonal Antibody ... — academic.oup.com (#3) `A`
- ✅ **0.3192** [on_target=0.61 evidence=0.52] Ombetoxabart - Drug Targets, Indications, Patents  - Synapse — synapse.patsnap.com (#7) `A`
- ❌ low_evidence **0.262** [on_target=0.60 evidence=0.44] The monoclonal antibody AZD5148 confers broad protection ... — journals.plos.org (#6) `A`
- ❌ low_on_target **0.1248** [on_target=0.36 evidence=0.35] Facile Therapeutics — platform.tracxn.com (#1)

## q003 (competitor objective)

**Objective:** Distal Ulcerative Colitis competing agents in the same mechanistic class as RpoB Small Molecule  
**Target sent:** drugs competing with RpoB: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['RpoB']

**q003-batch** `Distal Ulcerative Colitis RpoB inhibitors pipeline || Distal Ulcerative Colitis RpoB competitors Phase 2 || Distal Ulcerative Colitis RpoB mechanism clinical trial` → kept 1/10, jev 337 ms

- ✅ **0.494** [on_target=0.78 evidence=0.63] Cosmo Announces Completion of Phase II Enrolment in Distal Ulcerative Colitis Program — finance.yahoo.com (#7)
- ❌ low_on_target **0.1956** [on_target=0.36 evidence=0.54] Oral Ritlecitinib and Brepocitinib for Moderate-to-Severe Ulcerative ... — sciencedirect.com (#5)
- ❌ low_on_target **0.1935** [on_target=0.45 evidence=0.43] 
            New progress of small-molecule drugs in the treatment of inflammatory bowel disease - P — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.1505** [on_target=0.35 evidence=0.43] a phase 2, multi-center, randomized, double-blind — cdn.clinicaltrials.gov (#3)
- ❌ low_on_target **0.0792** [on_target=0.24 evidence=0.33] Comparative onset of effect of biologics and small molecules in moderate-to-severe ulcerative coliti — thelancet.com (#2)
- ❌ low_on_target **0.0782** [on_target=0.23 evidence=0.34] 
            Exploring the Pipeline of Novel Therapies for Inflammatory Bowel Disease; State of the  — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0667** [on_target=0.20 evidence=0.33] Advancing therapeutic frontiers: a pipeline of novel drugs for UC management - PubMed — pubmed.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0439** [on_target=0.14 evidence=0.31] Advancing therapeutic frontiers: a pipeline of novel drugs for ... — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0412** [on_target=0.13 evidence=0.32] Advances in the Treatment of Ulcerative Colitis-From Conventional Therapies to Targeted Biologics an — pubmed.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.0279** [on_target=0.11 evidence=0.25] Pathological mechanism and targeted drugs of ulcerative colitis — pmc.ncbi.nlm.nih.gov (#10)

## q004 (competitor objective)

**Objective:** competing agents in the same mechanistic class for this indication MT501, Mirador Therapeutics, Crohn's Disease, Moderately to Severely Active by CDAI and SES-CD  
**Target sent:** drugs competing with MT501: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['MT501']

**q004-batch** `MT501 mechanism of action mechanistic class || MT501 Crohn's disease target pathway || MT501 inflammatory bowel disease competitors same mechanism` → kept 5/10, jev 582 ms

- ✅ **0.825** [on_target=0.90 evidence=0.92] Mirikizumab for treating moderately to severely active Crohn's disease — nice.org.uk (#10)
- ✅ **0.6994** [on_target=0.86 evidence=0.81] Mirikizumab Pharmacokinetics and Exposure‐Response in Patients With Moderately‐To‐Severely Active Cr — ascpt.onlinelibrary.wiley.com (#6)
- ✅ **0.5703** [on_target=0.91 evidence=0.63] 
            New Interleukin-23 Antagonists’ Use in Crohn’s Disease - PMC
         — pmc.ncbi.nlm.nih.gov (#8)
- ✅ **0.5544** [on_target=0.84 evidence=0.66] Efficacy and Safety of Mirikizumab in a Randomized Phase 2 Study of Patients With Crohn's Disease -  — pubmed.ncbi.nlm.nih.gov (#3)
- ✅ **0.4536** [on_target=0.72 evidence=0.63] Tremfya — platform.tracxn.com (#1)
- ❌ low_on_target **0.1416** [on_target=0.50 evidence=0.28] MT-501 - Drug Targets, Indications, Patents  - Synapse — synapse.patsnap.com (#5) `A`
- ❌ low_on_target **0.1203** [on_target=0.44 evidence=0.27] MT 501 - AdisInsight — adisinsight.springer.com (#7) `A`
- ❌ low_on_target **0.112** [on_target=0.56 evidence=0.20] 

    
        Trial / NCT07113522
    

 — cdek.pharmacy.purdue.edu (#2) `A`
- ❌ low_on_target **0.0132** [on_target=0.06 evidence=0.22] Validation of the Modified Multiplier of SES-CD (MM-SES-CD) to Predict Endoscopic Healing in Crohn's — pubmed.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0051** [on_target=0.22 evidence=0.02] Mirador Therapeutics, Inc. - Drug pipelines, Patents, Clinical trials - Synapse — synapse.patsnap.com (#9)

## q005

**Objective:** SOR102 safety findings and adverse events in Crohn's Disease Ulcerative Colitis  
**Target sent:** SOR102 / SOR102-101 · anchors ['SOR102', 'SOR102-101']

**q005-batch** `SOR102 Crohn's disease safety adverse events || SOR102-101 registry identifier safety || SOR102 ulcerative colitis individual adverse events infections deaths || SOR102 Grade 3 adverse events 810 mg || SOR102 900 mg 42-day safety results` → kept 7/10, jev 370 ms

- ✅ **0.9474** [on_target=0.97 evidence=0.98] First In Human Study Of SOR102, A Novel, Orally Delivered ... — sorrisopharma.com (#2) `A`
- ✅ **0.8633** [on_target=0.97 evidence=0.89] Safety and pharmacokinetics of SOR102, an oral ... - ScienceDirect — sciencedirect.com (#3) `A`
- ✅ **0.7616** [on_target=0.96 evidence=0.79] Safely targeting combination TNF and IL-23 using a gut ... - PMC — pmc.ncbi.nlm.nih.gov (#4) `A`
- ✅ **0.7474** [on_target=0.95 evidence=0.79] SOR102 for Ulcerative Colitis / Gastro Today — docwirenews.com (#6) `A`
- ✅ **0.7379** [on_target=0.95 evidence=0.78] SOR102 / Sorriso Pharma - Gastroenterology — delta.larvol.com (#5) `A`
- ✅ **0.6173** [on_target=0.94 evidence=0.66] [PDF] SOR102, an anti-TNFα/anti-IL-23 antibody in — sorrisopharma.com (#1) `A`
- ✅ **0.506** [on_target=0.92 evidence=0.55] Safety and pharmacokinetics of SOR102, an oral bispecific ... — pubmed.ncbi.nlm.nih.gov (#8) `A`
- ❌ low_on_target **0.4366** [on_target=0.59 evidence=0.74] Adverse events associated with ustekinumab in Crohn's ... — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.079** [on_target=0.15 evidence=0.53] Drug-Related Adverse Events in Inflammatory Bowel Disease — researchgate.net (#9)
- ❌ low_on_target **0.0212** [on_target=0.06 evidence=0.35] Mortality in ulcerative colitis—what should we tell our patients ... — pmc.ncbi.nlm.nih.gov (#10)

## q006 (competitor objective)

**Objective:** Moderately to Severely Active Crohn's Disease Moderately to Severely Active Crohn’s Disease Refractory to Systemic Therapies Moderately to Severely Active Ulcerative Colitis Refractory to Systemic Therapies Moderately to Severely Active Ulcerative Colitis with inadequate response, loss of response, or intolerance to ≥1 biologic or novel oral with biologic-like activity competing agents in the same mechanistic class as JNJ-4804 Co Antibody Therapy, including Antibody Cocktail Monoclonal Antibody and IL-23 IL23A TNF-α Tumor Necrosis Factor Alpha therapies  
**Target sent:** drugs competing with JNJ-4804: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['JNJ-4804']

**q006-batch** `JNJ-4804 guselkumab golimumab IL-23 TNF-α competitors IBD || JNJ-4804 IL-23 TNF-α dual antibody competing agents IBD || JNJ-4804 same mechanistic class IBD pipeline || JNJ-4804 competing IL-23 TNF-α antibody Crohn's disease ulcerative colitis` → kept 7/10, jev 788 ms

- ✅ **0.7998** [on_target=0.93 evidence=0.86] Johnson & Johnson investigational co-antibody therapy JNJ-4804 shows potential to raise the bar for  — jnj.com (#5) `A`
- ✅ **0.6758** [on_target=0.93 evidence=0.73] [PDF] Efficacy of Guselkumab in Moderately to Severely Active Ulcerative ... — jnjmedicalconnect.com (#3)
- ✅ **0.6365** [on_target=0.88 evidence=0.72] DDW: Combination Therapy Shows Efficacy for Crohn Disease, Ulcerative Colitis — thecardiologyadvisor.com (#10) `A`
- ✅ **0.6102** [on_target=0.92 evidence=0.66] 
	Johnson & Johnson investigational co-antibody therapy JNJ-4804 shows potential to raise the bar fo — investor.jnj.com (#4) `A`
- ✅ **0.5824** [on_target=0.84 evidence=0.69] 
	Johnson & Johnson investigational co-antibody therapy JNJ-4804 shows potential to raise the bar fo — investor.jnj.com (#2) `A`
- ✅ **0.5684** [on_target=0.84 evidence=0.68] Johnson & Johnson investigational co-antibody therapy JNJ ... — s203.q4cdn.com (#8) `A`
- ✅ **0.4845** [on_target=0.79 evidence=0.61] Entyviohcp — platform.tracxn.com (#1)
- ❌ low_evidence **0.308** [on_target=0.62 evidence=0.50] efficacy and safety of the first co-antibody therapy, jnj- ... — jnjmedicalconnect.com (#7) `A`
- ❌ low_evidence **0.2904** [on_target=0.65 evidence=0.45] Presentation - jnjmedicalconnect.com — jnjmedicalconnect.com (#9) `A`
- ❌ low_on_target **0.2845** [on_target=0.53 evidence=0.54] GI and Hepatology News - Dualpathway coantibody therapy shows promise in refractory IBD — news.gastro.org (#6) `A`

## q007 (competitor objective)

**Objective:** Ulcerative Colitis competing agents in the same mechanistic class as FN1 IL-10RB IL10RA Interleukin-10 Antibody-Cytokine Conjugate Fusion Protein Biologic  
**Target sent:** drugs competing with Dekavil: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['Dekavil']

**q007-batch** `Dekavil ulcerative colitis IL-10 fusion competitors || Dekavil ulcerative colitis antibody-cytokine fusion pipeline || Dekavil PF-06687234 sponsor ownership || Dekavil ulcerative colitis current development status` → kept 7/10, jev 350 ms

- ✅ **0.618** [on_target=0.90 evidence=0.69] Pfizer Pipeline — cdn.pfizer.com (#10) `A`
- ✅ **0.5934** [on_target=0.89 evidence=0.67] Pfizer Pipeline — cdn.pfizer.com (#3) `A`
- ✅ **0.5655** [on_target=0.87 evidence=0.65] Efficacy and safety of the interleukin-10–fragment F8 fusion protein PF-06687234 as add-on therapy t — journals.sagepub.com (#4) `A`
- ✅ **0.53** [on_target=0.75 evidence=0.71] Efficacy and safety of the interleukin-10-fragment F8 fusion protein PF-06687234 as add-on therapy t — pubmed.ncbi.nlm.nih.gov (#9)
- ✅ **0.4428** [on_target=0.82 evidence=0.54] Dekavil - Drug Targets, Indications, Patents — synapse.patsnap.com (#8) `A`
- ✅ **0.424** [on_target=0.79 evidence=0.54] Dekavil (F8-IL10) / Pfizer, Philogen — delta.larvol.com (#5) `A`
- ❌ low_evidence **0.3866** [on_target=0.80 evidence=0.48] View PDF — pfizer.com (#2) `A`
- ✅ **0.3717** [on_target=0.63 evidence=0.59] Efficacy and safety of the interleukin-10–fragment F8 fusion ... — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_evidence **0.2728** [on_target=0.66 evidence=0.41] A Phase IB Clinical Trial with Dekavil (F8-Il10), an ... — researchgate.net (#7) `A`
- ❌ low_evidence **0.156** [on_target=0.78 evidence=0.20] Study Details / NCT02711462 / Study in Healthy Subjects to Evaluate the Safety, Tolerability, Pharma — clinicaltrials.gov (#1) `A`

## q008 (competitor objective)

**Objective:** Clostridioides Difficile Colitis competing agents in the same mechanistic class as LMN-201, including Antibody Fragment Enzyme Biological Biologic Cocktail and Clostridioides Difficile Toxin B TcdB therapies  
**Target sent:** drugs competing with LMN-201: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['LMN-201']

**q008-batch** `LMN-201 TcdB antitoxin competitors Phase 2 clinical || LMN-201 PA-41 development phase || LMN-201 BL5-6.2 clinical development || LMN-201 AZD5148 clinical trial regulatory status || LMN-201 bezlotoxumab withdrawal current status` → kept 4/10, jev 527 ms

- ✅ **0.7688** [on_target=0.93 evidence=0.83] The monoclonal antibody AZD5148 confers broad protection against TcdB-diverse Clostridioides diffici — journals.plos.org (#4)
- ✅ **0.6746** [on_target=0.92 evidence=0.73] LMN-201 in Clostridioides Difficile Infection - Clinical Trials Registry - ICH GCP — ichgcp.net (#8) `A`
- ✅ **0.5638** [on_target=0.85 evidence=0.66] Study Details / NCT03829475 / ICON-2: FMT and Bezlotoxumab Compared to FMT and Placebo for Patients  — clinicaltrials.gov (#3)
- ✅ **0.435** [on_target=0.75 evidence=0.58] LMN-201 / Lumen Bio — delta.larvol.com (#6) `A`
- ❌ low_evidence **0.2788** [on_target=0.74 evidence=0.38] Using antibody synergy to engineer a high potency biologic cocktail against C. difficile — lumen.bio (#5) `A`
- ❌ low_evidence **0.2777** [on_target=0.70 evidence=0.40] New Antibody Cocktail Shows Promise in Preventing C Diff Infection — contagionlive.com (#7) `A`
- ❌ low_evidence **0.2524** [on_target=0.67 evidence=0.38] Lumen Bioscience Receives Fast Track Designation from U.S. FDA for LMN-201 — prnewswire.com (#10) `A`
- ❌ low_evidence **0.2233** [on_target=0.67 evidence=0.33] An oral protein cocktail therapeutic for C. difficile infection / bioRxiv — biorxiv.org (#9) `A`
- ❌ low_evidence **0.2121** [on_target=0.63 evidence=0.34] Lumen Bioscience Releases Data on Potent, Orally Delivered Biologic Drug Cocktail for Preventing C.  — lumen.bio (#1) `A`
- ❌ low_evidence **0.2004** [on_target=0.62 evidence=0.32] [PDF] An oral protein cocktail therapeutic for C. difficile infection - bioRxiv — biorxiv.org (#2) `A`

## q009 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as CHRM1 CHRM3 CHRM4 CHRM5 Small Molecule  
**Target sent:** drugs competing with Dicyclomine: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['Dicyclomine']

**q009-batch** `Dicyclomine inflammatory bowel disease muscarinic competitors || Dicyclomine IBD CHRM pipeline || Dicyclomine inflammatory bowel disease clinical development` → kept 1/10, jev 345 ms

- ✅ **0.4657** [on_target=0.89 evidence=0.52] NCATS Inxight Drugs — DICYCLOMINE HYDROCHLORIDE — drugs.ncats.io (#10) `A`
- ❌ low_evidence **0.3364** [on_target=0.87 evidence=0.39] Dicyclomine: MedlinePlus Drug Information — medlineplus.gov (#7) `A`
- ❌ low_evidence **0.3145** [on_target=0.85 evidence=0.37] DailyMed - DICYCLOMINE HYDROCHLORIDE- dicyclomine hydrochloride capsule
 — dailymed.nlm.nih.gov (#1) `A`
- ❌ low_on_target **0.3042** [on_target=0.54 evidence=0.56] CHRM1 gene Cholinergic Receptor Muscarinic 1 — genecards.org (#5) `A`
- ❌ low_evidence **0.3024** [on_target=0.81 evidence=0.37] These highlights do not include all the information needed to use dicyclomine hydrochloride safely a — dailymed.nlm.nih.gov (#3) `A`
- ❌ low_evidence **0.2791** [on_target=0.79 evidence=0.35] Dicyclomine = 99 TLC, powder 67-92-5 — sigmaaldrich.com (#9) `A`
- ❌ low_evidence **0.2425** [on_target=0.75 evidence=0.32] DICYCLOMINE HYDROCHLORIDE capsule - DailyMed - NIH — dailymed.nlm.nih.gov (#2) `A`
- ❌ low_on_target **0.0279** [on_target=0.09 evidence=0.31] Target-Based Small Molecule Drug Discovery Towards Novel Therapeutics for Inflammatory Bowel Disease — academic.oup.com (#8)
- ❌ low_on_target **0.0191** [on_target=0.07 evidence=0.27] Next generation of small molecules in inflammatory bowel disease — gut.bmj.com (#6)
- ❌ low_on_target **0.0082** [on_target=0.06 evidence=0.14] Innovative pipeline therapeutics in inflammatory bowel disease — ovid.com (#4)

## q010 (competitor objective)

**Objective:** competing agents in the same mechanistic class for this indication LY4395089, Eli Lilly & Company, Crohn''s Disease  
**Target sent:** drugs competing with LY4395089: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['LY4395089']

**q010-batch** `LY4395089 mechanism target Crohn’s disease || LY4395089 competing agents Crohn’s disease same mechanism` → kept 5/10, jev 373 ms

- ✅ **0.5576** [on_target=0.82 evidence=0.68] LY4395089 - Crohn Disease / Phase 2 / Eli Lilly and ... — biopharmawatch.com (#3) `A`
- ✅ **0.5156** [on_target=0.74 evidence=0.70] [PDF] 761072Orig1s000 - accessdata.fda.gov — accessdata.fda.gov (#2)
- ✅ **0.4833** [on_target=0.81 evidence=0.60] A clinical research study for people with moderately to severely active Crohn’s disease to test if 2 — trials.lilly.com (#7) `A`
- ✅ **0.3952** [on_target=0.77 evidence=0.51] FXR Agonist LY4395089 and Mirikizumab Co-administration for Moderately to Severely Active Crohn's Di — patlynk.com (#8) `A`
- ❌ low_evidence **0.3513** [on_target=0.83 evidence=0.42] Eli Lilly Targets Crohn’s Disease With New Combo Trial That Could Extend Its IBD Franchise - The Glo — theglobeandmail.com (#5) `A`
- ✅ **0.3422** [on_target=0.68 evidence=0.50] Lilly's Mirikizumab Met Primary Endpoint and Key Secondary Endpoints in Phase 2 Study, Including Red — prnewswire.com (#9)
- ❌ low_evidence **0.3168** [on_target=0.66 evidence=0.48] Lilly's mirikizumab is first and only IL23p19 antagonist to report long-term, multi-year, sustained  — investor.lilly.com (#10)
- ❌ low_on_target **0.2223** [on_target=0.58 evidence=0.38] LY4395089 + Mirikizumab for Crohn's Disease — withpower.com (#6) `A`
- ❌ low_on_target **0.126** [on_target=0.36 evidence=0.35] Network Meta-Analysis: Comparative Efficacy of Biologics and Small Molecules in the Induction and Ma — pubmed.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0045** [on_target=0.08 evidence=0.06] Eli Lilly — platform.tracxn.com (#1)

## q011 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as Small Molecule targeting ITGA4 ITGB7 Integrin Alpha-4 Beta-7  
**Target sent:** drugs competing with α4β7 Inhibitor / α4β7: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['α4β7 Inhibitor', 'α4β7']

**q011-batch** `α4β7 Inhibitor etrolizumab mechanism IBD || α4β7 Inhibitor vedolizumab current development status 2026 || α4β7 Inhibitor abrilumab current status IBD || α4β7 Inhibitor Phase 2 Phase 3 Crohn's disease competitors || α4β7 Inhibitor AJM300 natalizumab class comparison` → kept 9/10, jev 357 ms

- ✅ **0.8139** [on_target=0.95 evidence=0.86] 
            Targeting Beta-7 Integrins for the Treatment of Inflammatory Bowel Disease - PMC
       — pmc.ncbi.nlm.nih.gov (#9)
- ✅ **0.7011** [on_target=0.88 evidence=0.80] Polpharma Biologics Announces FDA and EMA Acceptance for Review of PB016 Vedolizumab Biosimilar Cand — biospace.com (#3) `A`
- ✅ **0.6643** [on_target=0.94 evidence=0.71] EA-1080 - Drug Targets, Indications, Patents  - Synapse — synapse.patsnap.com (#7) `A`
- ✅ **0.6365** [on_target=0.88 evidence=0.72] Targeting Beta-7 Integrins for the Treatment of Inflammatory Bowel Disease - Gastroenterology & Hepa — gastroenterologyandhepatology.net (#8)
- ✅ **0.6134** [on_target=0.92 evidence=0.67] Frontiers / Cellular Mechanisms of Etrolizumab Treatment in Inflammatory Bowel Disease — frontiersin.org (#5) `A`
- ✅ **0.5985** [on_target=0.94 evidence=0.64] Vedolizumab - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#10) `A`
- ✅ **0.5515** [on_target=0.88 evidence=0.63] ABRILUMAB profile page — platform.opentargets.org (#1)
- ✅ **0.5312** [on_target=0.83 evidence=0.64] ontamalimab (TAK-647) / Takeda, Pfizer — delta.larvol.com (#2) `A`
- ✅ **0.4664** [on_target=0.88 evidence=0.53] Frontiers / Effects of Anti-Integrin Treatment With Vedolizumab on Immune Pathways and Cytokines in  — frontiersin.org (#6) `A`
- ❌ low_evidence **0.3735** [on_target=0.83 evidence=0.45] Vedolizumab: an α4β7 integrin inhibitor for inflammatory bowel diseases - PubMed — pubmed.ncbi.nlm.nih.gov (#4) `A`

## q012

**Objective:** Lenvatinib + Nofazinlimab pivotal, registrational, or Phase 3 trial in Unresectable or Metastatic Hepatocellular Carcinoma: planned or initiated status and expected start date  
**Target sent:** Lenvatinib + Nofazinlimab NCT04194775 / Lenvatinib / Nofazinlimab / NCT04194775 · anchors ['Lenvatinib + Nofazinlimab NCT04194775', 'Lenvatinib', 'Nofazinlimab', 'NCT04194775']

**q012-batch** `Lenvatinib + Nofazinlimab NCT04194775 first patient enrollment date || Lenvatinib + Nofazinlimab NCT04194775 current trial status` → kept 10/10, jev 347 ms

- ✅ **0.9636** [on_target=0.98 evidence=0.98] NCT04194775: A reported trial by CStone Pharmaceuticals — fdaaa.trialstracker.net (#4) `A`
- ✅ **0.8754** [on_target=0.98 evidence=0.89] clinicaltrials.gov — clinicaltrials.gov (#1) `A`
- ✅ **0.8624** [on_target=0.98 evidence=0.88] A Study of Nofazinlimab (CS1003) in Subjects With Advanced Hepatocellular Carcinoma — ctv.veeva.com (#7) `A`
- ✅ **0.8096** [on_target=0.96 evidence=0.84] CStone announced the global multi-regional registration trial of anti-PD-1 antibody nofazinlimab in  — cstonepharma.com (#9) `A`
- ✅ **0.7663** [on_target=0.97 evidence=0.79] Study Details / NCT04194775 / A Study of Nofazinlimab (CS1003) in Subjects With Advanced Hepatocellu — clinicaltrials.gov (#2) `A`
- ✅ **0.7505** [on_target=0.95 evidence=0.79] LBA52 Nofazinlimab combined with lenvatinib versus placebo plus lenvatinib as first-line therapy for — annalsofoncology.org (#8) `A`
- ✅ **0.7366** [on_target=0.87 evidence=0.85] A Study of Nofazinlimab (CS1003) in Subjects With Advanced ... — guidelinecentral.com (#10) `A`
- ✅ **0.7088** [on_target=0.98 evidence=0.72] Nofazinlimab (CS1003)+Lenvatinib in Hepatocellular Carcinoma - Clinical Trials Registry - ICH GCP — ichgcp.net (#5) `A`
- ✅ **0.678** [on_target=0.90 evidence=0.75] News - nofazinlimab (CS1003) - LARVOL VERI — veri.larvol.com (#6) `A`
- ✅ **0.5918** [on_target=0.92 evidence=0.64] Clinical Protocol CS1003-305 ClinicalTrials.gov Document Cover Page Clinical Protocol -305 Study CS1 — cdn.clinicaltrials.gov (#3) `A`

## q013

**Objective:** SD-133 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** SD-133 · anchors ['SD-133']

**q013-batch** `SD-133 pancreatic ductal adenocarcinoma monotherapy xenograft TGI || SD-133 tumour regression pancreatic cancer animal model` → kept 2/10, jev 340 ms

- ✅ **0.5529** [on_target=0.97 evidence=0.57] SD 133 - AdisInsight - Springer — adisinsight.springer.com (#4) `A`
- ✅ **0.544** [on_target=0.96 evidence=0.57] SD-133 - Drug Targets, Indications, Patents  - Synapse — synapse.patsnap.com (#5) `A`
- ❌ low_on_target **0.1782** [on_target=0.27 evidence=0.66] Neutralization of p40 Homodimer and p40 Monomer Leads to Tumor Regression in Patient-Derived Xenogra — mdpi.com (#7)
- ❌ low_on_target **0.0787** [on_target=0.20 evidence=0.39] In vivo assessment of treatment response in a xenograft ... — researchgate.net (#8)
- ❌ low_on_target **0.01** [on_target=0.04 evidence=0.25] Patient-Derived Xenograft Models of Pancreatic Cancer: Overview and Comparison with Other Types of M — mdpi.com (#3)
- ❌ low_on_target **0.0099** [on_target=0.04 evidence=0.25] 
            Patient-Derived Xenograft Models of Pancreatic Cancer: Overview and Comparison with Oth — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0066** [on_target=0.03 evidence=0.22] 
        Patient-derived xenograft model of pancreatic cancer
      -  UT MD Anderson Cancer Center — mdanderson.elsevierpure.com (#1)
- ❌ low_on_target **0.006** [on_target=0.03 evidence=0.20] Preclinical mouse models for immunotherapeutic and non-immunotherapeutic drug development for pancre — apc.amegroups.org (#2)
- ❌ low_on_target **0.0045** [on_target=0.02 evidence=0.22] Models of pancreatic ductal adenocarcinoma / Cancer and Metastasis Reviews / Springer Nature Link — link.springer.com (#6)
- ❌ low_on_target **0.0037** [on_target=0.03 evidence=0.12] Pancreatic ductal adenocarcinoma Datasets — biogps.org (#10)

## q014

**Objective:** Sirpiglenastat in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** Sirpiglenastat / DRP-104 · anchors ['Sirpiglenastat', 'DRP-104']

**q014-batch** `Sirpiglenastat PDAC monotherapy TGI xenograft || DRP-104 pancreatic cancer single-agent tumour regression || Sirpiglenastat pancreatic PDX monotherapy tumour volume || DRP-104 PDAC xenograft dose response || Sirpiglenastat pancreatic cancer in vivo monotherapy` → kept 7/10, jev 358 ms

- ✅ **0.8102** [on_target=0.98 evidence=0.83] Targeting pancreatic cancer metabolic dependencies ... — nature.com (#7) `A`
- ✅ **0.6822** [on_target=0.97 evidence=0.70] DON of Hope: Starving Pancreatic Cancer by Glutamine ... — aacrjournals.org (#8) `A`
- ✅ **0.6598** [on_target=0.98 evidence=0.67] Sirpiglenastat (DRP-104) Induces Antitumor Efficacy through Direct, Broad Antagonism of Glutamine Me — pubmed.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.6143** [on_target=0.97 evidence=0.63] An In-Depth Technical Guide to the In Vivo Efficacy of Novel Anti-Cancer Agents DRP-104 and PR-104 — pdf.benchchem.com (#6) `A`
- ✅ **0.608** [on_target=0.96 evidence=0.63] Dracen Pharmaceuticals, Inc. - Drug pipelines, Patents, Clinical trials - Synapse — synapse.patsnap.com (#4) `A`
- ✅ **0.6044** [on_target=0.98 evidence=0.62] Sirpiglenastat (DRP-104) Induces Antitumor Efficacy through ... — aacrjournals.org (#10) `A`
- ✅ **0.5425** [on_target=0.93 evidence=0.58] AACR Poster 2022 — dracenpharma.com (#1) `A`
- ❌ low_on_target **0.0836** [on_target=0.23 evidence=0.36] Head-to-head comparison of the dual-MEK inhibitor IMM-1-104 versus sotorasib or adagrasib in KRAS mu — asco.org (#3)
- ❌ low_on_target **0.0076** [on_target=0.03 evidence=0.25] Preclinical mouse models for immunotherapeutic and non-immunotherapeutic drug development for pancre — pubmed.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0043** [on_target=0.02 evidence=0.22] Progress in Animal Models of Pancreatic Ductal Adenocarcinoma — jcancer.org (#2)

## q015

**Objective:** GFH375/VS-7375 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in KRAS G12D-Mutated/MTAP-Deleted Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** GFH375 VS-7375 / GFH375 / VS-7375 · anchors ['GFH375 VS-7375', 'GFH375', 'VS-7375']

**q015-batch** `GFH375 VS-7375 quantitative TGI KP4 PDAC monotherapy || GFH375 VS-7375 MTAP-deleted KP4 monotherapy tumour regression || GFH375 VS-7375 MTAP-deleted pancreatic xenograft single-agent TGI || GFH375 VS-7375 AsPC-1 Panc 04.03 monotherapy tumour volume data` → kept 9/10, jev 333 ms

- ✅ **0.7318** [on_target=0.98 evidence=0.75] Abstract 7100: VS-7375: An oral, selective KRAS G12D dual ON/OFF inhibitor with potent anti-tumor ac — aacrjournals.org (#7) `A`
- ✅ **0.7056** [on_target=0.98 evidence=0.72] [PDF] VS-7375 (GFH375): An oral, selective KRAS G12D (ON/OFF) inhibitor with ... — verastem.com (#4) `A`
- ✅ **0.6762** [on_target=0.98 evidence=0.69] Anti-Tumor Efficacy of the Selective Oral KRAS G12D Dual ON ... — verastem.com (#5) `A`
- ✅ **0.6693** [on_target=0.97 evidence=0.69] Abstract A076: VS-7375: An oral, selective KRAS G12D dual ON/OFF inhibitor with superior anti-tumor  — aacrjournals.org (#8) `A`
- ✅ **0.6429** [on_target=0.95 evidence=0.68] Slide 1 — verastem.com (#6) `A`
- ✅ **0.6329** [on_target=0.94 evidence=0.67] Abstract LB183: Strong durable tumor regressions with the KRASG12D ON/OFF inhibitor VS-7375 in combi — aacrjournals.org (#2) `A`
- ✅ **0.6144** [on_target=0.95 evidence=0.65] VS-7375 / Verastem, GenFleet Therap - LARVOL DELTA — delta.larvol.com (#9) `A`
- ✅ **0.5303** [on_target=0.97 evidence=0.55] Verastem Oncology Announces Updated Data from Partner GenFleet Therapeutics’ Phase 1/2 Monotherapy S — investor.verastem.com (#3) `A`
- ✅ **0.4968** [on_target=0.92 evidence=0.54] [PDF] LBA84 Efficacy and safety of GFH375 monotherapy in previously ... — s3.eu-central-1.amazonaws.com (#1) `A`
- ❌ low_evidence **0.4834** [on_target=0.98 evidence=0.49] GFH375 (VS-7375): An oral, selective KRAS G12D (ON/OFF ... — aacrjournals.org (#10) `A`

## q016

**Objective:** PLM-103 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic ductal adenocarcinoma (PDAC) animal models  
**Target sent:** PLM-103 · anchors ['PLM-103']

**q016-batch** `PLM-103 PDAC xenograft monotherapy tumour regression TGI` → kept 1/10, jev 354 ms

- ✅ **0.6337** [on_target=0.97 evidence=0.65] PLM-103: A dual-mechanism YES1/YAP pathway inhibitor ... — aacrjournals.org (#2) `A`
- ❌ low_on_target **0.2015** [on_target=0.31 evidence=0.65] Neutralization of p40 Homodimer and p40 Monomer Leads to Tumor Regression in Patient-Derived Xenogra — mdpi.com (#3)
- ❌ low_on_target **0.1716** [on_target=0.39 evidence=0.44] MK-8353 induces tumor growth inhibition or regression ... — insight.jci.org (#7)
- ❌ low_on_target **0.0316** [on_target=0.13 evidence=0.24] TV monotherapy induces tumor regression in xenograft ... — researchgate.net (#5)
- ❌ low_on_target **0.031** [on_target=0.10 evidence=0.31] Patient-Derived Xenograft Models of Pancreatic Cancer - PMC — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0224** [on_target=0.08 evidence=0.28] Explaining in-vitro to in-vivo efficacy correlations in oncology pre ... — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0153** [on_target=0.10 evidence=0.15] Tumor growth inhibition (TGI)-monotherapy (a) and ... — researchgate.net (#4)
- ❌ low_on_target **0.014** [on_target=0.05 evidence=0.28] Optimal design for informative protocols in xenograft tumor ... — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0043** [on_target=0.02 evidence=0.21] Progress in Animal Models of Pancreatic Ductal Adenocarcinoma — jcancer.org (#1)
- ❌ low_on_target **0.0022** [on_target=0.03 evidence=0.07] 
            Radius additivity score: a novel combination index for tumour growth inhibition in fixe — pmc.ncbi.nlm.nih.gov (#8)

## q017

**Objective:** SW-682 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Head and Neck Squamous Cell Carcinoma animal models  
**Target sent:** SW-682 · anchors ['SW-682']

**q017-batch** `SW-682 CAL-33 SCC-25 xenograft tumour growth inhibition monotherapy || SW-682 HNSCC xenograft tumour regression monotherapy || SW-682 CAL-33 SCC-25 tumour volume TGI` → kept 5/10, jev 353 ms

- ✅ **0.7808** [on_target=0.96 evidence=0.81] Targeting YAP/TAZ-TEAD signaling as a therapeutic ... — sciencedirect.com (#7) `A`
- ✅ **0.7774** [on_target=0.98 evidence=0.79] Targeting YAP/TAZ-TEAD signaling as a therapeutic approach ... — pmc.ncbi.nlm.nih.gov (#6) `A`
- ✅ **0.7644** [on_target=0.98 evidence=0.78] Frontiers / Targeting TEAD in cancer — frontiersin.org (#10) `A`
- ✅ **0.4891** [on_target=0.73 evidence=0.67] Inhibition of the chemokine receptors CXCR1 and CXCR2 synergizes... - CiteAb — citeab.com (#1)
- ❌ low_on_target **0.391** [on_target=0.51 evidence=0.77] TV monotherapy induces tumor regression in xenograft ... — researchgate.net (#4)
- ✅ **0.3253** [on_target=0.61 evidence=0.53] A phase I clinical and pharmacokinetic study of CS-682 administered orally in advanced malignant sol — pubmed.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.1654** [on_target=0.41 evidence=0.40] SX-682 Treatment in Subjects With... / Clinical Trial — trial.medpath.com (#3)
- ❌ low_on_target **0.0645** [on_target=0.22 evidence=0.29] Tumor growth inhibition (TGI)-monotherapy (a) and ... — researchgate.net (#5)
- ❌ low_on_target **0.0303** [on_target=0.14 evidence=0.22] Inhibition of human tumor xenograft growth by treatment ... - PubMed — pubmed.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0078** [on_target=0.06 evidence=0.13] A patient‐derived xenograft and a cell line... : Cancer Medicine — ovid.com (#9)

## q018

**Objective:** SPR2015 in vivo animal models and results: cell-line xenograft CDX, patient-derived xenograft PDX, syngeneic, orthotopic, or genetically engineered models  
**Target sent:** SPR2015 · anchors ['SPR2015']

**q018-batch** `SPR2015 HNSCC in vivo xenograft || SPR2015 PDAC patient-derived xenograft || SPR2015 PDAC syngeneic model || SPR2015 PDAC genetically engineered mouse model || SPR2015 HPAC AsPC-1 tumour volume percentage inhibition` → kept 3/10, jev 368 ms

- ✅ **0.9604** [on_target=0.98 evidence=0.98] Abstract 5978: SPR2015, a highly potent and selective KRAS G12D (on) inhibitor, exhibits favorable p — aacrjournals.org (#6) `A`
- ✅ **0.7452** [on_target=0.85 evidence=0.88] 
            Tumor-selective effects of active RAS inhibition in pancreatic ductal adenocarcinoma -  — pmc.ncbi.nlm.nih.gov (#3)
- ✅ **0.6144** [on_target=0.72 evidence=0.85] Humanized Anti-Trop-2 IgG-SN-38 Conjugate for Effective Treatment of Diverse Epithelial Cancers: Pre — aacrjournals.org (#2)
- ❌ low_on_target **0.3927** [on_target=0.51 evidence=0.77] In vivo efficacy evaluation in AsPC-1 cell-derived xenograft ... — researchgate.net (#4)
- ❌ low_on_target **0.218** [on_target=0.30 evidence=0.73] Tumor Growth Suppression of Pancreatic Cancer ... — mdpi.com (#7)
- ❌ low_on_target **0.2069** [on_target=0.32 evidence=0.65] Development of gemcitabine-resistant patient-derived xenograft models of pancreatic ductal adenocarc — oaepublish.com (#1)
- ❌ low_on_target **0.0648** [on_target=0.12 evidence=0.54] Clinical, Molecular and Genetic Validation of a Murine Orthotopic Xenograft Model of Pancreatic Aden — journals.plos.org (#5)
- ❌ low_on_target **0.0623** [on_target=0.10 evidence=0.62] 
            Construction of orthotopic xenograft mouse models for human pancreatic cancer - PMC
    — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0532** [on_target=0.11 evidence=0.48] 
            Update on in-vivo preclinical research models in adrenocortical carcinoma - PMC
        — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0198** [on_target=0.06 evidence=0.33] Patient-derived xenograft models: Current status, challenges ... — pmc.ncbi.nlm.nih.gov (#10)

## q019

**Objective:** Innovent Biologics Inc. descriptions of IBI-3001's advantage over existing treatments for Head and Neck Squamous Cell Carcinoma in investor materials, earnings calls, investor day presentations, and press releases  
**Target sent:** IBI-3001 · anchors ['IBI-3001']

**q019-batch** `IBI-3001 HNSCC investor presentation treatment advantage || IBI3001 recurrent metastatic HNSCC Innovent press release || IBI3001 HNSCC first-line standard of care comparison` → kept 3/10, jev 343 ms

- ✅ **0.6762** [on_target=0.98 evidence=0.69] Press Release — en.innoventbio.com (#4) `A`
- ✅ **0.624** [on_target=0.96 evidence=0.65] IBI3001 / Innovent Biologics, Takeda, Fortvita Biologics — delta.larvol.com (#5) `A`
- ✅ **0.5859** [on_target=0.95 evidence=0.62] Press Release - Innovent Biologics — en.innoventbio.com (#7) `A`
- ❌ low_evidence **0.3432** [on_target=0.72 evidence=0.48] LiGeR-HN phase III trials of petosemtamab + pembrolizumab ... — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0208** [on_target=0.16 evidence=0.13] Innovent Announces 2025 Interim Results and Business Updates — prnewswire.com (#1) `A`
- ❌ low_on_target **0.0028** [on_target=0.06 evidence=0.05] Innovent Reports Oncology Pipeline Updates at Investor Meeting - June 19, 2024 - BioSpace — biospace.com (#6)
- ❌ low_on_target **0.0026** [on_target=0.02 evidence=0.13] HNSCC - The Cancer Imaging Archive (TCIA) — cancerimagingarchive.net (#10)
- ❌ low_on_target **0.0018** [on_target=0.06 evidence=0.03] Innovent Announces 2025 Annual Results and Business Updates — prnewswire.com (#3)
- ❌ low_on_target **0.0013** [on_target=0.39 evidence=0.00] (no title) — synapse.patsnap.com (#9)
- ❌ low_on_target **0.0007** [on_target=0.03 evidence=0.02] /C O R R E C T I O N — Innovent Biologics/ / Morningstar — morningstar.com (#2)

## q020 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as JTO2, including Monoclonal Antibody and CXCL10 therapies  
**Target sent:** drugs competing with JTO2: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['JTO2']

**q020-batch** `JTO2 CXCL10 inflammatory bowel disease competitors || JTO2 anti-CXCL10 monoclonal antibody IBD pipeline || JTO2 CXCL10 clinical trial inflammatory bowel disease` → kept 4/10, jev 368 ms

- ✅ **0.5824** [on_target=0.84 evidence=0.69] Eldelumab - Drug Targets, Indications, Patents  - Synapse — synapse.patsnap.com (#3)
- ✅ **0.5667** [on_target=0.85 evidence=0.67] New Non-anti-TNF-α Biological Therapies for the Treatment of Inflammatory Bowel Disease / Abdominal  — abdominalkey.com (#6)
- ✅ **0.4042** [on_target=0.67 evidence=0.60] 
            New treatment options for inflammatory bowel diseases - PMC
         — pmc.ncbi.nlm.nih.gov (#1)
- ✅ **0.4004** [on_target=0.66 evidence=0.61] IBD therapeutics: what is in the pipeline? — fg.bmj.com (#2)
- ❌ low_evidence **0.3496** [on_target=0.76 evidence=0.46] JT-02(Jyant Technologies) - Drug Targets, Indications, Patents  - Synapse — synapse.patsnap.com (#5)
- ❌ low_evidence **0.3335** [on_target=0.69 evidence=0.48] 
            Current, new and future biological agents on the horizon for the treatment of inflammat — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.2744** [on_target=0.49 evidence=0.56] Innovative pipeline therapeutics in inflammatory bowel disease — ovid.com (#4)
- ❌ low_on_target **0.2011** [on_target=0.52 evidence=0.39] Chemokines and Chemokine Receptors as Therapeutic Targets in Inflammatory Bowel Disease; Pitfalls an — academic.oup.com (#10)
- ❌ low_on_target **0.1092** [on_target=0.28 evidence=0.39] CXCL10 CXC motif chemokine ligand 10 [ (human)] — ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0616** [on_target=0.22 evidence=0.28] CXCL10/IP-10 in infectious diseases pathogenesis and ... - PMC — pmc.ncbi.nlm.nih.gov (#8)

## q021 (competitor objective)

**Objective:** Crohn's Disease Ulcerative Colitis competing agents with the same mechanistic class as S1PR S1PR1 Sphingosine-1-phosphate receptor, including Small Molecule  
**Target sent:** drugs competing with Mocravimod: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['Mocravimod']

**q021-batch** `Mocravimod IBD S1PR competitors licensing status || Mocravimod Crohn's disease ulcerative colitis S1PR1 agents || Mocravimod etrasimod ozanimod head-to-head IBD || Mocravimod IBD partnering in-licensing || Mocravimod ClinicalTrials.gov Crohn's ulcerative colitis` → kept 8/10, jev 379 ms

- ✅ **0.8836** [on_target=0.94 evidence=0.94] Etrasimod: First Approval - PubMed — pubmed.ncbi.nlm.nih.gov (#5)
- ✅ **0.8795** [on_target=0.97 evidence=0.91] Frontiers / Advancing therapeutic frontiers: a pipeline of novel drugs for UC management — frontiersin.org (#6) `A`
- ✅ **0.7657** [on_target=0.93 evidence=0.82] Everest Medicines Announces that Licensing Partner Pfizer Reports Positive Topline Results from Year — prnewswire.com (#1)
- ✅ **0.7104** [on_target=0.96 evidence=0.74] 
            Targeting the Sphingosine-1-Phosphate Pathway: New Opportunities in Inflammatory Bowel  — pmc.ncbi.nlm.nih.gov (#2) `A`
- ✅ **0.6746** [on_target=0.92 evidence=0.73] Efficacy and Safety of Etrasimod in a Phase 2 Randomized Trial of Patients With Ulcerative Colitis - — gastrojournal.org (#7)
- ✅ **0.6641** [on_target=0.87 evidence=0.76] The Current Sphingosine 1 Phosphate Receptor Modulators in the Management of Ulcerative Colitis — mdpi.com (#4)
- ✅ **0.6431** [on_target=0.91 evidence=0.71] 
            New progress of small-molecule drugs in the treatment of inflammatory bowel disease - P — pmc.ncbi.nlm.nih.gov (#8)
- ✅ **0.601** [on_target=0.92 evidence=0.65] An overview of ozanimod as a therapeutic option for adults with ... — pubmed.ncbi.nlm.nih.gov (#10)
- ❌ low_evidence **0.377** [on_target=0.78 evidence=0.48] [PDF] Mocravimod, a Selective Sphingosine-1-Phosphate Receptor ... — astctjournal.org (#3) `A`
- ❌ low_evidence **0.3569** [on_target=0.83 evidence=0.43] MOCRAVIMOD profile page — platform.opentargets.org (#9) `A`

## q022 (competitor objective)

**Objective:** competing agents in the same mechanistic class for this indication Novel UC Treatment, Cosmo Health, Distal Ulcerative Colitis  
**Target sent:** drugs competing with Novel UC Treatment: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['Novel UC Treatment']

**q022-batch** `Novel UC Treatment mechanism of action ulcerative colitis || Novel UC Treatment target mechanistic class UC || Novel UC Treatment Phase 2 competitor landscape ulcerative colitis` → kept 5/10, jev 366 ms

- ✅ **0.5925** [on_target=0.88 evidence=0.67] Therapeutic Class Overview Ulcerative Colitis Agents — medicaid.nv.gov (#3)
- ✅ **0.592** [on_target=0.83 evidence=0.71] 
            Current and Emerging Biologics for Ulcerative Colitis - PMC
         — pmc.ncbi.nlm.nih.gov (#2)
- ✅ **0.5252** [on_target=0.78 evidence=0.67] Landscape of new drugs and targets in inflammatory bowel ... — onlinelibrary.wiley.com (#4)
- ✅ **0.524** [on_target=0.79 evidence=0.66] 
            Management of inflammatory bowel disease beyond tumor necrosis factor inhibitors: novel — pmc.ncbi.nlm.nih.gov (#8)
- ✅ **0.4132** [on_target=0.67 evidence=0.62] Emerging treatments for ulcerative colitis: a systematic review - PubMed — pubmed.ncbi.nlm.nih.gov (#9)
- ❌ low_evidence **0.2816** [on_target=0.65 evidence=0.43] 
            Novel treatment options for ulcerative colitis - PMC
         — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.261** [on_target=0.58 evidence=0.45] Frontiers / Advancing therapeutic frontiers: a pipeline of novel drugs for UC management — frontiersin.org (#7)
- ❌ low_on_target **0.1907** [on_target=0.44 evidence=0.43] Study Details / NCT03341962 / Phase 2 Dose-finding IMU-838 for Ulcerative Colitis / ClinicalTrials.g — clinicaltrials.gov (#1)
- ❌ low_on_target **0.1452** [on_target=0.36 evidence=0.40] Novel Agent Promising for Refractory Ulcerative Colitis - Medscape — medscape.com (#10)
- ❌ low_on_target **0.0** [on_target=0.01 evidence=0.00] UC Davis Scientists Describe Novel Drug Mechanism That ... — newswise.com (#6)

## q023 (competitor objective)

**Objective:** Inflammatory Bowel Diseases Mild-to-moderate ulcerative colitis Ulcerative Colitis competing agents with the same mechanistic class as Gut Microbiome Dysbiosis, including Live Biotherapeutic Product  
**Target sent:** drugs competing with VE202 / MB310 / SER-287 / EXL01: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['VE202', 'MB310', 'SER-287', 'EXL01']

**q023-batch** `VE202 Phase 2 current status licensing || MB310 Phase 2 Microbiotica licensing || SER-287 ulcerative colitis development status licensing || EXL01 ReMind Phase 2 licensing Crohn's disease` → kept 5/10, jev 349 ms

- ✅ **0.6622** [on_target=0.86 evidence=0.77] MRM Health’s Lead Candidate MH002 Granted Fast Track Designation by U.S. FDA for the Treatment of Mi — businesswire.com (#5)
- ✅ **0.4988** [on_target=0.86 evidence=0.58] Flerie’s portfolio company Microbiotica reports positive Phase 1b data for MB310 in patients with ul — flerie.com (#8) `A`
- ✅ **0.4957** [on_target=0.88 evidence=0.56] Seres Therapeutics Announces Initiation of a Phase 1b Clinical Trial of SER-287 in Mild-to-Moderate  — ir.serestherapeutics.com (#7) `A`
- ✅ **0.4844** [on_target=0.86 evidence=0.56]  Microbiotica Announces Impressive Results in its Phase 1b Trial of MB310 in Ulcerative Colitis

 /  — manilatimes.net (#4) `A`
- ✅ **0.4536** [on_target=0.84 evidence=0.54] PureTech Founded Entity Vedanta Biosciences Announces New Data from Phase 1 Study of VE202 for the T — news.puretechhealth.com (#6) `A`
- ❌ low_evidence **0.4242** [on_target=0.86 evidence=0.49] Microbiotica – Precision Microbiome Medicines — microbiotica.com (#3) `A`
- ❌ low_evidence **0.369** [on_target=0.82 evidence=0.45] Study Details / NCT02618187 / A Study to Evaluate the Safety, Tolerability and Microbiome Dynamics o — clinicaltrials.gov (#10) `A`
- ❌ low_evidence **0.3313** [on_target=0.70 evidence=0.47] Exeliom Biosciences Announces First Patient Enrolled in Phase 1 ... — exeliombio.com (#2) `A`
- ❌ low_on_target **0.1316** [on_target=0.42 evidence=0.31] Study Details / NCT05684484 / Role of Roflumilast in Ulcerative Colitis / ClinicalTrials.gov — clinicaltrials.gov (#1)
- ❌ low_evidence **0.1159** [on_target=0.71 evidence=0.16] VE202 in Patients With Mild-to-Moderate Ulcerative Colitis — clinicaltrials.gov (#9) `A`

## q024 (competitor objective)

**Objective:** Ulcerative Colitis competing agents in the same mechanistic class as ITGA4 ITGB7 Integrin Alpha-4 Beta-7 Integrin α4β7 Small Molecule therapies  
**Target sent:** drugs competing with emvistegrast: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['emvistegrast']

**q024-batch** `emvistegrast α4β7 ulcerative colitis Phase 2 competitors || emvistegrast α4β7 ulcerative colitis pipeline Phase 3 || emvistegrast α4β7 ulcerative colitis licensing || emvistegrast integrin alpha-4 beta-7 ulcerative colitis clinical trial` → kept 8/10, jev 452 ms

- ✅ **0.8859** [on_target=0.97 evidence=0.91] 
            Advancing therapeutic frontiers: a pipeline of novel drugs for UC management - PMC
     — pmc.ncbi.nlm.nih.gov:443 (#5) `A`
- ✅ **0.6219** [on_target=0.88 evidence=0.71] Etrolizumab as induction therapy for ulcerative colitis: a randomised, controlled, phase 2 trial - P — pubmed.ncbi.nlm.nih.gov (#3)
- ✅ **0.621** [on_target=0.90 evidence=0.69] Integrin Inhibitors in Inflammatory Bowel Disease: From Therapeutic Antibodies to Small-Molecule Dru — gastrojournal.org (#6)
- ✅ **0.498** [on_target=0.83 evidence=0.60] Emvistegrast - Drug Targets, Indications, Patents  - Synapse — synapse.patsnap.com (#4) `A`
- ✅ **0.4928** [on_target=0.84 evidence=0.59] CN122206461A – Therapy for the treatment of inflammatory bowel disease / Patsnap Eureka — eureka.patsnap.com (#7)
- ✅ **0.4819** [on_target=0.79 evidence=0.61] 
            Etrolizumab for the Treatment of Ulcerative Colitis and Crohn’s Disease: An Overview of — pmc.ncbi.nlm.nih.gov (#1)
- ✅ **0.4534** [on_target=0.80 evidence=0.57] emvistegrast / Ligand page / IUPHAR/BPS Guide to PHARMACOLOGY — guidetopharmacology.org (#9) `A`
- ✅ **0.4155** [on_target=0.76 evidence=0.55] emvistegrast (GS-1427) — drughunter.com (#8) `A`
- ❌ low_evidence **0.3242** [on_target=0.68 evidence=0.48] The Potential of the Alpha4 Beta7 Integrin Inhibitors as Treatment for Inflammatory Bowel Diseases a — pubs.acs.org (#10)
- ❌ low_on_target **0.172** [on_target=0.43 evidence=0.40] 
        Etrasimod as induction and maintenance therapy for ulcerative colitis (ELEVATE): two random — scholars.mssm.edu (#2)

## q025 (competitor objective)

**Objective:** Ulcerative Colitis competing agents with the same mechanism of action as HEMAY007, targeting TNF-α Tumor Necrosis Factor Alpha  
**Target sent:** drugs competing with HEMAY007: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['HEMAY007']

**q025-batch** `HEMAY007 ulcerative colitis anti-TNF Phase 2 competitors || HEMAY007 ulcerative colitis anti-TNF licensing availability || HEMAY007 TNF-alpha ulcerative colitis clinical development status || HEMAY007 ulcerative colitis anti-TNF biosimilar landscape` → kept 3/10, jev 385 ms

- ✅ **0.8115** [on_target=0.94 evidence=0.86] 
            Emerging drugs for the treatment of ulcerative colitis - PMC
         — pmc.ncbi.nlm.nih.gov (#3)
- ✅ **0.7068** [on_target=0.93 evidence=0.76] Current and emerging biologics for ulcerative colitis — pubmed.ncbi.nlm.nih.gov (#7)
- ✅ **0.5309** [on_target=0.88 evidence=0.60] Landscape of new drugs and targets in inflammatory bowel disease - Vieujean - 2022 - United European — onlinelibrary.wiley.com (#6) `A`
- ❌ low_evidence **0.296** [on_target=0.74 evidence=0.40] Hemay 007 - AdisInsight — adisinsight.springer.com (#9) `A`
- ❌ low_evidence **0.2725** [on_target=0.67 evidence=0.41] Hemay007 - Drug Targets, Indications, Patents  - Synapse — synapse.patsnap.com (#1) `A`
- ❌ low_evidence **0.2714** [on_target=0.69 evidence=0.39] Hemay Pharmaceutical Pty Ltd - Drug pipelines, Patents, Clinical trials - Synapse — synapse.patsnap.com (#5) `A`
- ❌ low_evidence **0.2434** [on_target=0.67 evidence=0.36] Hemay Pharmaceutical Pty Ltd (Hemay Pharmaceutical Pty Ltd) - 药物管线_专利_临床试验_投融营收_最新药物:Hemay007 — synapse.zhihuiya.com (#4) `A`
- ❌ low_on_target **0.1392** [on_target=0.58 evidence=0.24] Phase II Study of Hemay007 in Patients... / Clinical Trial — trial.medpath.com (#2) `A`
- ❌ low_on_target **0.1279** [on_target=0.59 evidence=0.22] Ganzhou Hemay Pharmaceutical News - LARVOL Sigma — sigma.larvol.com (#8) `A`
- ❌ low_on_target **0.1008** [on_target=0.54 evidence=0.19] Hemay007 / Ganzhou Hemay Pharmaceutical — delta.larvol.com (#10) `A`

## q026

**Objective:** BM-013 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** BM-013 · anchors ['BM-013']

**q026-batch** `BM-013 acute myeloid leukemia regulatory approval launch || BM-013 BIMINI Biotech approval AML || BM-013 WASP AML clinical development forecast` → kept 1/10, jev 351 ms

- ✅ **0.6672** [on_target=0.72 evidence=0.93] FDA Approves a New Treatment for Acute Myeloid Leukemia / The AACR — aacr.org (#8)
- ❌ low_on_target **0.4956** [on_target=0.59 evidence=0.84] FDA Approves Revumenib for Acute Myeloid Leukemia ... — oncologynewscentral.com (#7)
- ❌ low_evidence **0.4123** [on_target=0.89 evidence=0.46] Bimini Biotech company information, funding & investors — app.dealroom.co (#9) `A`
- ❌ low_on_target **0.3916** [on_target=0.50 evidence=0.78] 
	Bristol Myers Squibb - U.S. Food and Drug Administration (FDA) Accepts for Priority Review Bristol — news.bms.com (#3)
- ❌ low_on_target **0.2713** [on_target=0.37 evidence=0.73] FDA approves novel treatment for acute myeloid leukemia — damonrunyon.org (#4)
- ❌ low_on_target **0.1102** [on_target=0.29 evidence=0.38] Study Details / NCT04214249 / BLAST MRD AML-1: BLockade of PD-1 Added to Standard Therapy to Target  — clinicaltrials.gov (#2)
- ❌ low_on_target **0.0925** [on_target=0.19 evidence=0.49] Acute Myeloid Leukemia with Myelodysplasia-Related Changes - Drugs, Targets, Patents - Synapse — synapse.patsnap.com (#5)
- ❌ low_on_target **0.0355** [on_target=0.13 evidence=0.27] 
            New Targeted Agents in Acute Myeloid Leukemia: New Hope on the Rise - PMC
         — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.0323** [on_target=0.10 evidence=0.32] 
            Recent drug approvals for acute myeloid leukemia - PMC
         — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.012** [on_target=0.10 evidence=0.12] BIMINI Biotech — startup.usi.ch (#6)

## q027

**Objective:** HQL-79 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** HQL-79 · anchors ['HQL-79']

**q027-batch** `HQL-79 pancreatic ductal adenocarcinoma in vivo || HQL-79 monotherapy PDAC xenograft || HQL-79 tumour regression animal model || HQL-79 tumour growth inhibition pancreatic cancer` → kept 1/10, jev 404 ms

- ✅ **0.4154** [on_target=0.62 evidence=0.67] Tumour-selective activity of RAS-GTP inhibition in pancreatic ... — pubmed.ncbi.nlm.nih.gov (#4)
- ❌ low_evidence **0.3321** [on_target=0.94 evidence=0.35] Structural and functional characterization of HQL-79, an ... — pubmed.ncbi.nlm.nih.gov (#6) `A`
- ❌ low_evidence **0.2944** [on_target=0.92 evidence=0.32] Structural and Functional Characterization of HQL-79, an ... — jbc.org (#3) `A`
- ❌ low_on_target **0.024** [on_target=0.09 evidence=0.27] Targeted therapy for pancreatic ductal adenocarcinoma: Mechanisms and clinical study - Kung - 2023 - — onlinelibrary.wiley.com (#10)
- ❌ low_on_target **0.0168** [on_target=0.06 evidence=0.28] 
            Translational Learnings in the Development of Chemo-Immunotherapy Combination to Bypass — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0128** [on_target=0.06 evidence=0.21] A mathematical model of tumor regression and recurrence ... — nature.com (#9)
- ❌ low_on_target **0.0071** [on_target=0.03 evidence=0.24] Pancreatic Ductal Adenocarcinoma: MicroRNAs Affecting ... — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0057** [on_target=0.03 evidence=0.19] Spontaneous and Induced Animal Models for Cancer ... — mdpi.com (#8)
- ❌ low_on_target **0.0031** [on_target=0.02 evidence=0.15] Objective assessment of tumor regression in post-neoadjuvant therapy resections for pancreatic ducta — nature.com (#1)
- ❌ low_on_target **0.0005** [on_target=0.02 evidence=0.02] Animal models in preclinical metastatic breast cancer ... - PMC — pmc.ncbi.nlm.nih.gov (#7)

## q028

**Objective:** HEC234055 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** HEC234055 · anchors ['HEC234055']

**q028-batch** `HEC234055 monotherapy HPAC PDAC xenograft regression || HEC234055 PK-59 PDAC monotherapy tumour regression` → ABSTAIN, jev 395 ms

- ❌ low_on_target **0.2103** [on_target=0.38 evidence=0.55] Regression of human pancreatic tumor xenografts in mice ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0618** [on_target=0.18 evidence=0.34] TV monotherapy induces tumor regression in xenograft ... — researchgate.net (#5)
- ❌ low_on_target **0.015** [on_target=0.09 evidence=0.17] Subcutaneous xenograft tumors in mice showed ... — researchgate.net (#6)
- ❌ low_on_target **0.014** [on_target=0.06 evidence=0.23] Molecular alterations and targeted therapy in pancreatic ductal adenocarcinoma / Journal of Hematolo — link.springer.com (#4)
- ❌ low_on_target **0.0087** [on_target=0.03 evidence=0.29] 
        Translational advances in pancreatic ductal adenocarcinoma therapy
      -  UT MD Anderson  — mdanderson.elsevierpure.com (#8)
- ❌ low_on_target **0.0069** [on_target=0.03 evidence=0.23] Preclinical mouse models for immunotherapeutic and non-immunotherapeutic drug development for pancre — apc.amegroups.org (#7)
- ❌ low_on_target **0.0067** [on_target=0.04 evidence=0.17] 
            Clinical and Preclinical Targeting of Oncogenic Pathways in PDAC: Targeted Therapeutic  — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0065** [on_target=0.04 evidence=0.16] 
            Recent advances in targeted therapy for pancreatic adenocarcinoma - PMC
         — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.006** [on_target=0.03 evidence=0.20] 
            Therapeutic Status and Available Strategies in Pancreatic Ductal Adenocarcinoma - PMC
  — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0018** [on_target=0.02 evidence=0.09] 
            Human pancreatic adenocarcinoma contains a side population resistant to gemcitabine - P — pmc.ncbi.nlm.nih.gov (#1)

## q029

**Objective:** TP-317 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** TP-317 KPC / TP-317 · anchors ['TP-317 KPC', 'TP-317']

**q029-batch** `TP-317 KPC pancreatic cancer tumour regression monotherapy || TP-317 KPC PDAC dose schedule monotherapy` → kept 1/10, jev 894 ms

- ✅ **0.452** [on_target=0.60 evidence=0.75] Looking Beyond Checkpoint Inhibitor Monotherapy ... — aacrjournals.org (#8)
- ❌ low_on_target **0.1602** [on_target=0.27 evidence=0.59] 
            Efficacy and Imaging-Enabled Pharmacodynamic Profiling of KRAS G12C Inhibitors in Xenog — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.127** [on_target=0.30 evidence=0.42] Tumour-selective activity of RAS-GTP inhibition in pancreatic ... — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0861** [on_target=0.21 evidence=0.41] 
            Proteolytic pan-RAS cleavage leads to tumor regression in patient-derived pancreatic ca — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0768** [on_target=0.18 evidence=0.43] Three-drug strategy forces pancreatic tumors into lasting ... — news-medical.net (#6)
- ❌ low_on_target **0.0707** [on_target=0.21 evidence=0.34] T-cell Dependency of Tumor Regressions and Complete ... — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0243** [on_target=0.09 evidence=0.27] Preclinical Models of Pancreatic Ductal Adenocarcinoma ... — mdpi.com (#5)
- ❌ low_on_target **0.0198** [on_target=0.11 evidence=0.18] Tumor growth inhibition modeling to support the starting dose for ... — ascpt.onlinelibrary.wiley.com (#10)
- ❌ low_on_target **0.0187** [on_target=0.08 evidence=0.23] 
            Genetically Engineered Mouse Models of Pancreatic Cancer: The KPC Model (LSL-KrasG12D/+ — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0083** [on_target=0.05 evidence=0.17] Mechanisms of Tumor Progression and Drug Resistance in Pancreatic Cancer Models (PANC-1, MiaPaCa-2,  — biomedpharmajournal.org (#1)

## q030

**Objective:** SGR-4174 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** SGR-4174 · anchors ['SGR-4174']

**q030-batch** `SGR-4174 Mia PaCa2 monotherapy tumour regression xenograft || SGR-4174 PDAC xenograft tumour shrinkage single agent` → kept 5/10, jev 551 ms

- ✅ **0.6926** [on_target=0.98 evidence=0.71] Schrödinger Presents New Preclinical Data at AACR Annual Meeting — s203.q4cdn.com (#3) `A`
- ✅ **0.6632** [on_target=0.98 evidence=0.68] SGR-4174 / Schrodinger — delta.larvol.com (#4) `A`
- ✅ **0.6534** [on_target=0.98 evidence=0.67] Abstract 4376: Preclinical characterization of SGR-4174, a ... — researchgate.net (#5) `A`
- ✅ **0.6338** [on_target=0.98 evidence=0.65] Abstract 4376: Preclinical characterization of SGR-4174, a potent and selective SOS1 inhibitor for t — aacrjournals.org (#6) `A`
- ✅ **0.5592** [on_target=0.72 evidence=0.78] A Pan-RAS Inhibitor with a Unique Mechanism of Action ... — aacrjournals.org (#7)
- ❌ low_evidence **0.3584** [on_target=0.96 evidence=0.37] SGR 4174 - AdisInsight — adisinsight.springer.com (#10) `A`
- ❌ low_on_target **0.06** [on_target=0.24 evidence=0.25] Phase I clinical trial repurposing all-trans retinoic acid as a stromal targeting agent for pancreat — nature.com (#1)
- ❌ low_on_target **0.0328** [on_target=0.12 evidence=0.27] Z-360 Suppresses Tumor Growth in MIA PaCa-2-bearing Mice via Inhibition of Gastrin-induced Anti-Apop — ar.iiarjournals.org (#2)
- ❌ low_on_target **0.0299** [on_target=0.14 evidence=0.21] Responses of 31 individual xenograft models in mice ... — researchgate.net (#8)
- ❌ low_on_target **0.0057** [on_target=0.04 evidence=0.14] MiA-PaCa2: Orthotopic pancreas tumor model — reactionbiology.com (#9)

## q031

**Objective:** SPR2015 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma (PDAC) animal models  
**Target sent:** SPR2015 · anchors ['SPR2015']

**q031-batch** `SPR2015 HPAC xenograft TGI percentage monotherapy || SPR2015 AsPC-1 xenograft tumour regression shrinkage || SPR2015 PDAC monotherapy xenograft tumour growth inhibition || SPR2015 HPAC AsPC-1 xenograft AACR 2026 abstract 5978` → kept 3/10, jev 384 ms

- ✅ **0.7178** [on_target=0.97 evidence=0.74] Abstract 5978: SPR2015, a highly potent and selective KRAS G12D (on) inhibitor, exhibits favorable p — aacrjournals.org (#4) `A`
- ✅ **0.6402** [on_target=0.98 evidence=0.65] SPR2015, a highly potent and selective KRAS G12D (on) ... — semanticscholar.org (#6) `A`
- ✅ **0.6272** [on_target=0.96 evidence=0.65] SPR2015, a highly potent and selective KRAS G12D (on) ... — researchgate.net (#8) `A`
- ❌ low_on_target **0.2369** [on_target=0.34 evidence=0.70] Inhibition of Cell Proliferation and Growth of Pancreatic Cancer by Silencing of Carbohydrate Sulfot — journals.plos.org (#7)
- ❌ low_on_target **0.1859** [on_target=0.39 evidence=0.48] Tumor growth inhibition (TGI)-monotherapy (a) and ... — researchgate.net (#5)
- ❌ low_on_target **0.0799** [on_target=0.17 evidence=0.47] Extensive preclinical validation of combined RMC-4550 and LY3214996 supports clinical investigation  — cell.com (#1)
- ❌ low_on_target **0.0261** [on_target=0.14 evidence=0.19] Inhibition of human tumor xenograft growth by treatment ... - PubMed — pubmed.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0142** [on_target=0.05 evidence=0.28] Preclinical pancreatic cancer mouse models for treatment with small molecule inhibitors: a systemati — nature.com (#3)
- ❌ low_on_target **0.0088** [on_target=0.04 evidence=0.22] Patient-derived xenograft models for gastrointestinal tumors — frontiersin.org (#10)
- ❌ low_on_target **0.0019** [on_target=0.02 evidence=0.09] 
            Human pancreatic adenocarcinoma contains a side population resistant to gemcitabine - P — pmc.ncbi.nlm.nih.gov (#2)

## q032

**Objective:** PHY-003 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Head and Neck Squamous Cell Carcinoma animal models  
**Target sent:** PHY-003 · anchors ['PHY-003']

**q032-batch** `PHY-003 HNSCC monotherapy xenograft tumour regression || PHY-003 HNSCC in vivo tumour growth inhibition dose || PHY-003 head and neck squamous cell carcinoma animal model efficacy` → ABSTAIN, jev 379 ms

- ❌ low_on_target **0.3734** [on_target=0.56 evidence=0.67] PF-3644022 (CAS Number: 1276121-88-0) — caymanchem.com (#2)
- ❌ low_on_target **0.36** [on_target=0.48 evidence=0.75] TV monotherapy induces tumor regression in xenograft ... — researchgate.net (#4)
- ❌ low_on_target **0.246** [on_target=0.41 evidence=0.60] In Vivo Tumor Growth Inhibition and Antiangiogenic Effect of ... — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.1976** [on_target=0.39 evidence=0.51] In Vivo Tumor Growth Inhibition and Antiangiogenic Effect of ... — link.springer.com (#10)
- ❌ low_on_target **0.0868** [on_target=0.19 evidence=0.46] Enhanced Inhibition of HNSCC Growth by α-Tomatine and ... — mdpi.com (#5)
- ❌ low_on_target **0.0861** [on_target=0.21 evidence=0.41] Overcoming resistance to EGFR monotherapy in HNSCC by identification and inhibition of individualize — thno.org (#6)
- ❌ low_on_target **0.042** [on_target=0.10 evidence=0.42] Derived Xenograft Models — rheumatology.cureus.com (#9)
- ❌ low_on_target **0.0087** [on_target=0.03 evidence=0.29] Models of head and neck squamous cell carcinoma using bioengineering approaches - ScienceDirect — sciencedirect.com (#3)
- ❌ low_on_target **0.0058** [on_target=0.02 evidence=0.29] Head and neck squamous cell carcinoma - PubMed - NIH — pubmed.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0038** [on_target=0.03 evidence=0.13] [PDF] Humanized patient-derived xenografts preserve tumour ... - bioRxiv — biorxiv.org (#1)

## q033

**Objective:** DXP-007 sponsor development stage indication public source  
**Target sent:** DXP-007 · anchors ['DXP-007']

**q033-batch** `DXP-007 sponsor || DXP-007 development stage || DXP-007 inflammatory bowel disease` → kept 1/10, jev 386 ms

- ✅ **0.6076** [on_target=0.98 evidence=0.62] 产品管线 — singlomics.com (#5) `A`
- ❌ low_evidence **0.3266** [on_target=0.69 evidence=0.47] Study Details / NCT06721962 / Treatment of Moderate to Severe Refractory Crohn's Disease / ClinicalT — clinicaltrials.gov (#3)
- ❌ low_on_target **0.2827** [on_target=0.33 evidence=0.86] DXC-007 - Drug Targets, Indications, Patents  - Synapse — synapse.patsnap.com (#1)
- ❌ low_evidence **0.206** [on_target=0.60 evidence=0.34] Study Details / NCT07113522 / A Phase 2 Study to Evaluate Therapies for Inflammatory Bowel Disease / — clinicaltrials.gov (#2)
- ❌ low_on_target **0.063** [on_target=0.21 evidence=0.30] Current scenario in inflammatory bowel disease: Drug development ... — link.springer.com (#4)
- ❌ low_on_target **0.0347** [on_target=0.13 evidence=0.27] Pfizer's next-generation therapies for inflammatory bowel disease / Drug Discovery News — drugdiscoverynews.com (#7)
- ❌ low_on_target **0.0144** [on_target=0.06 evidence=0.24] Crohn’s & Colitis Foundation IBD Ventures Initiative — crohnscolitisfoundation.org (#8)
- ❌ low_on_target **0.0087** [on_target=0.03 evidence=0.29] Inflammatory Bowel Disease (IBD) Basics - CDC — cdc.gov (#6)
- ❌ low_on_target **0.0084** [on_target=0.03 evidence=0.28] Inflammatory Bowel Disease - Medscape Reference — emedicine.medscape.com (#10)
- ❌ low_on_target **0.0082** [on_target=0.03 evidence=0.27] IBD Facts and Stats — cdc.gov (#9)

## q034

**Objective:** Compound 18l first regulatory approval or market launch year for acute myeloid leukemia  
**Target sent:** Compound 18l · anchors ['Compound 18l']

**q034-batch** `Compound 18l ALKBH5 AML regulatory approval launch year` → kept 1/10, jev 381 ms

- ❌ low_on_target **0.5339** [on_target=0.57 evidence=0.94] Rydapt ratified: Novartis' targeted AML therapy wins FDA approval + / Bioworld / BioWorld — bioworld.com (#10)
- ❌ low_on_target **0.5278** [on_target=0.58 evidence=0.91] Genentech: Press Releases / Wednesday, Nov 21, 2018 — gene.com (#3)
- ✅ **0.4902** [on_target=0.85 evidence=0.58] Discovery of Covalent and Cell-Active ALKBH5 Inhibitors with ... — onlinelibrary.wiley.com (#8) `A`
- ❌ low_on_target **0.4896** [on_target=0.54 evidence=0.91] FDA approves new treatment for patients with acute myeloid leukemia — prnewswire.com (#7)
- ❌ low_on_target **0.272** [on_target=0.41 evidence=0.66] FDA approves new drug to treat advanced AML in adults — bloodcancerunited.org (#4)
- ❌ low_on_target **0.2695** [on_target=0.35 evidence=0.77] FDA approves novel treatment for acute myeloid leukemia — damonrunyon.org (#5)
- ❌ low_on_target **0.1715** [on_target=0.31 evidence=0.55] FDA Approves First All-Oral Regimen for AML / AJMC — ajmc.com (#6)
- ❌ low_on_target **0.039** [on_target=0.13 evidence=0.30] Acute Myeloid Leukemia (AML) Medication: Antineoplastics, Antimetabolites, Antineoplastics, Anthracy — emedicine.medscape.com (#1)
- ❌ low_on_target **0.008** [on_target=0.06 evidence=0.13] ALKBH5 facilitates acute myeloid leukemia development and ... — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0008** [on_target=0.08 evidence=0.01] RNA demethylase ALKBH5 - Homo sapiens (Human) — uniprot.org (#2)

## q035

**Objective:** BS-HH-002 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** BS-HH-002 · anchors ['BS-HH-002']

**q035-batch** `BS-HH-002 regulatory approval AML || BS-HH-002 market launch AML || BS-HH-002 Bensheng Pharma AML clinical development || BS-HH-002 expected approval year || BS-HH-002 first patient AML` → kept 6/10, jev 453 ms

- ✅ **0.9114** [on_target=0.98 evidence=0.93] BS-HH-002 - Drug Targets, Indications, Patents  - Synapse — synapse-patsnap-com.libproxy1.nus.edu.sg (#10) `A`
- ✅ **0.8504** [on_target=0.97 evidence=0.88] Therapeutic effects of an innovative BS-HH-002 drug on ... — sciencedirect.com (#7) `A`
- ✅ **0.6076** [on_target=0.93 evidence=0.65] A Phase I, Open-Label, Dose Escalation and Cohort Expansion Study of BS HH 002.SA in Patients With A — smartpatients.com (#3) `A`
- ✅ **0.5734** [on_target=0.94 evidence=0.61] Therapeutic effects of an innovative BS-HH-002 drug on pancreatic cancer cells via induction of comp — pubmed.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.5504** [on_target=0.96 evidence=0.57] Bensheng Pharma Trials — sigma.larvol.com (#4) `A`
- ✅ **0.5301** [on_target=0.93 evidence=0.57] Study Details / NCT04743115 / A Phase I, Open-Label, Dose Escalation and Cohort Expansion Study of B — clinicaltrials.gov (#1) `A`
- ❌ low_evidence **0.4085** [on_target=0.95 evidence=0.43] Shanghai Bensen Pharmaceutical Co., Ltd. (上海本生药业 ... — synapse.zhihuiya.com (#6) `A`
- ❌ low_evidence **0.2328** [on_target=0.97 evidence=0.24] BS-HH-002 - Drug Targets, Indications, Patents — synapse.patsnap.com (#8) `A`
- ❌ low_on_target **0.2149** [on_target=0.31 evidence=0.69] FDA Approves First All-Oral Regimen for AML / AJMC — ajmc.com (#9)
- ❌ low_on_target **0.0192** [on_target=0.08 evidence=0.24] 
            Novel agents and regimens in acute myeloid leukemia: latest updates from 2022 ASH Annua — pmc.ncbi.nlm.nih.gov (#2)

## q036

**Objective:** VAR-101 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic Ductal Carcinoma animal models  
**Target sent:** VAR-101 · anchors ['VAR-101']

**q036-batch** `VAR-101 pancreatic ductal carcinoma monotherapy xenograft TGI || VAR-101 pancreatic cancer tumour regression animal model || VAR-101 aPKCi PDAC in vivo efficacy monotherapy` → ABSTAIN, jev 399 ms

- ❌ low_on_target **0.16** [on_target=0.30 evidence=0.53] In vivo assessment of treatment response in a xenograft ... — researchgate.net (#5)
- ❌ low_on_target **0.0267** [on_target=0.09 evidence=0.30] Looking Beyond Checkpoint Inhibitor Monotherapy ... — aacrjournals.org (#9)
- ❌ low_on_target **0.0121** [on_target=0.04 evidence=0.30] Preclinical pancreatic cancer mouse models for treatment with small molecule inhibitors: a systemati — nature.com (#7)
- ❌ low_on_target **0.0099** [on_target=0.04 evidence=0.25] 
            Recent advances in targeted therapy for pancreatic adenocarcinoma - PMC
         — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.0094** [on_target=0.06 evidence=0.16] Establishment and Thorough Characterization of Xenograft ... — mdpi.com (#8)
- ❌ low_on_target **0.0093** [on_target=0.04 evidence=0.23] Patient-Derived Xenograft Models of Pancreatic Cancer - PMC — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0075** [on_target=0.04 evidence=0.19] Insights into gemcitabine resistance in pancreatic cancer: association with metabolic reprogramming  — link.springer.com (#2)
- ❌ low_on_target **0.0065** [on_target=0.03 evidence=0.22] Spontaneous and Induced Animal Models for Cancer ... — mdpi.com (#4)
- ❌ low_on_target **0.0059** [on_target=0.03 evidence=0.20] Pancreatic Cancer Xenograft — altogenlabs.com (#10)
- ❌ low_on_target **0.0051** [on_target=0.02 evidence=0.25] 
            Progress in Animal Models of Pancreatic Ductal Adenocarcinoma - PMC
         — pmc.ncbi.nlm.nih.gov (#3)

## q037

**Objective:** IPS-06061 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in KRAS G12D Mutant Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** IPS-06061 · anchors ['IPS-06061']

**q037-batch** `IPS-06061 AsPC-1 xenograft tumour regression || IPS-06061 30 mg/kg TGI AsPC-1 || IPS-06061 day 28 tumour volume AsPC-1 || IPS-06061 tumour shrinkage pancreatic cancer xenograft` → kept 3/10, jev 404 ms

- ✅ **0.6598** [on_target=0.98 evidence=0.67] Abstract 384: IPS-06061, a novel TPD molecular glue degrader ... — semanticscholar.org (#5) `A`
- ✅ **0.6566** [on_target=0.98 evidence=0.67] Abstract 384: IPS-06061, a novel TPD molecular glue degrader targeting KRAS G12D — researchgate.net (#6) `A`
- ✅ **0.4628** [on_target=0.89 evidence=0.52] An overview of KRAS G12D inhibitors: Expanding the therapeutic frontier of KRAS in targeting KRAS G1 — researchgate.net (#8) `A`
- ❌ low_evidence **0.4261** [on_target=0.94 evidence=0.45] An overview of KRAS G12D inhibitors: Expanding the ... - ScienceDirect — sciencedirect.com (#10) `A`
- ❌ low_evidence **0.4139** [on_target=0.97 evidence=0.43] IPS-06061 - Drug Targets, Indications, Patents — synapse.patsnap.com (#9) `A`
- ❌ low_on_target **0.17** [on_target=0.25 evidence=0.68] Quarterly Report for Quarter Ending September 30, 2025 (Form ... — publicnow.com (#4)
- ❌ low_on_target **0.1334** [on_target=0.23 evidence=0.58] Discovery of KRAS(G12D) selective degrader ASP3082 - PubMed — pubmed.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0675** [on_target=0.15 evidence=0.45] 
            Reshaping the Tumor Microenvironment of KRASG12D Pancreatic Ductal Adenocarcinoma with  — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0395** [on_target=0.15 evidence=0.26] Efficacy and safety signals from early-phase studies of KRAS inhibition in pancreatic cancer / Scien — nature.com (#2)
- ❌ low_on_target **0.0192** [on_target=0.06 evidence=0.32] Targeted Therapy in Pancreatic Ductal Adenocarcinoma: Current Advances and Challenges — mdpi.com (#1)

## q038 (competitor objective)

**Objective:** KRAS G12D drugs approved against the target and their regulatory approval status  
**Target sent:** drugs competing with ZE980277: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['ZE980277']

**q038-batch** `ZE980277 KRAS G12D approval status FDA EMA || ZE980277 KRAS G12D regulatory approval || ZE980277 KRAS G12D approved therapy status` → kept 7/10, jev 628 ms

- ✅ **0.7018** [on_target=0.87 evidence=0.81] KRAS G12D - Drugs, Indications, Patents - Synapse — synapse-patsnap-com.sutd.idm.oclc.org (#5)
- ✅ **0.6257** [on_target=0.76 evidence=0.82] Revolution Medicines Announces FDA Breakthrough Therapy ... — ir.revmed.com (#6)
- ✅ **0.5676** [on_target=0.66 evidence=0.86] FDA Grants Fast Track Designation to VS-7375 for KRAS ... — targetedonc.com (#7)
- ✅ **0.5598** [on_target=0.68 evidence=0.82] KRAS G12C and G12D Inhibitors: Three Regulatory Milestones in ... — patsnap.com (#4)
- ✅ **0.536** [on_target=0.67 evidence=0.80] Investigational KRAS(ON) Inhibitor Zoldonrasib Showed Effective and Durable Responses in Patients Wi — aacr.org (#10)
- ✅ **0.5313** [on_target=0.77 evidence=0.69] 
            KRAS G12D targeted therapies for pancreatic cancer: Has the fortress been conquered? -  — pmc.ncbi.nlm.nih.gov (#8)
- ✅ **0.4258** [on_target=0.73 evidence=0.58] 
            Dual Inhibition of KRAS G12D and PI3K/BRD4 signaling overcomes therapeutic resistance i — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.2352** [on_target=0.48 evidence=0.49] Abbreviated Title: mTCR Targeting KRAS G12D NIH Protocol Number: 19C0017 IBC Number: RD-17-VI-12 NCT — cdn.clinicaltrials.gov (#2)
- ❌ low_on_target **0.1972** [on_target=0.58 evidence=0.34] KRAS G12D Inhibitors Market Research Report 2034 — dataintelo.com (#9)
- ❌ low_on_target **0.1133** [on_target=0.34 evidence=0.33] CENTER FOR DRUG EVALUATION AND RESEARCH - Food and Drug ... — accessdata.fda.gov (#3)

## q039 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as KPG-818, including Small Molecule and Aiolos CRBN Ikaros therapies  
**Target sent:** drugs competing with KPG-818: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['KPG-818']

**q039-batch** `KPG-818 Aiolos CRBN Ikaros inflammatory bowel disease competitors || KPG-818 CELMoD IBD clinical pipeline || KPG-818 CRBN degrader inflammatory bowel disease` → kept 1/10, jev 368 ms

- ✅ **0.4212** [on_target=0.78 evidence=0.54] Epaldeudomide - Drug Targets, Indications, Patents — synapse.patsnap.com (#5) `A`
- ❌ low_evidence **0.3268** [on_target=0.76 evidence=0.43] Kangpu Biopharmaceuticals to Present Preclinical Efficacy Data of KPG-818 in Crohn's Disease at the  — kangpugroup.com (#9) `A`
- ❌ low_evidence **0.2939** [on_target=0.76 evidence=0.39] Pipeline-Kangpu Biopharmaceuticals — kangpugroup.com (#3) `A`
- ❌ low_evidence **0.2604** [on_target=0.73 evidence=0.36] Kangpu Biopharmaceuticals Successfully Completed Phase I Study of Novel CRL4-CRBN Modulator KPG-818  — prnewswire.com (#1) `A`
- ❌ low_on_target **0.2552** [on_target=0.58 evidence=0.44] Multiple Investigational Approaches Show Promise for Lupus — medscape.com (#10) `A`
- ❌ low_evidence **0.2466** [on_target=0.74 evidence=0.33] Kangpu Biopharmaceuticals Received IND Approval from ... — biospace.com (#6) `A`
- ❌ low_evidence **0.2331** [on_target=0.63 evidence=0.37] Kangpu Biopharmaceuticals Received CDE Approval for Phase IIb Clinical Trial of KPG-818 in Moderate  — prnewswire.com (#2) `A`
- ❌ low_evidence **0.2254** [on_target=0.65 evidence=0.35] KPG-818, a Novel Cereblon (CRBN) Modulator, in Patients with SLE: Results of a Phase Ib Multiple Asc — acrabstracts.org (#4) `A`
- ❌ low_evidence **0.2022** [on_target=0.74 evidence=0.27] POS0057 KPG-818, A NOVEL CEREBLON MODULATOR ... — researchgate.net (#8) `A`
- ❌ low_evidence **0.142** [on_target=0.60 evidence=0.24] Kpg-818, a novel cereblon (CRBN) modulator, in patients ... — researchgate.net (#7) `A`

## q040 (competitor objective)

**Objective:** Active Ulcerative Colitis Moderate to Severe Ulcerative Colitis competing agents in the same mechanistic class as CHST15 Oligonucleotide Small Interfering RNA therapies  
**Target sent:** drugs competing with GUT-1: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['GUT-1']

**q040-batch** `GUT-1 CHST15 ulcerative colitis competitors || GUT-1 siRNA CHST15 ulcerative colitis || GUT-1 CHST15 moderate to severe ulcerative colitis pipeline` → ABSTAIN, jev 357 ms

- ❌ low_evidence **0.272** [on_target=0.68 evidence=0.40] Submucosal Injection of the RNA Oligonucleotide GUT-1 in ... — pubmed.ncbi.nlm.nih.gov (#2) `A`
- ❌ low_evidence **0.272** [on_target=0.68 evidence=0.40] Add-on multiple submucosal injections of the RNA ... — pubmed.ncbi.nlm.nih.gov (#3) `A`
- ❌ low_evidence **0.2359** [on_target=0.61 evidence=0.39] Submucosal Injection of the RNA Oligonucleotide GUT-1 in ... — academic.oup.com (#8) `A`
- ❌ low_evidence **0.2319** [on_target=0.65 evidence=0.36] Add-on multiple submucosal injections of the RNA ... — link.springer.com (#6) `A`
- ❌ low_on_target **0.2193** [on_target=0.51 evidence=0.43] Repression of intestinal fibrosis by systemic CHST15 ... — researchgate.net (#5) `A`
- ❌ low_on_target **0.1794** [on_target=0.46 evidence=0.39] Comparative Efficacy of Different Targeted Therapies in ... — bpspubs.onlinelibrary.wiley.com (#10)
- ❌ low_on_target **0.171** [on_target=0.45 evidence=0.38] 
            Advancing therapeutic frontiers: a pipeline of novel drugs for UC management - PMC
     — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.1629** [on_target=0.52 evidence=0.31] The Sulfate Moieties of Glycosaminoglycans Are Critical for ... — researchgate.net (#9) `A`
- ❌ low_on_target **0.1357** [on_target=0.37 evidence=0.37] Frontiers / Advancing therapeutic frontiers: a pipeline of novel drugs for UC management — frontiersin.org (#4)
- ❌ low_on_target **0.1176** [on_target=0.36 evidence=0.33] 
            Efficacy and Safety of Advanced Therapies in Moderately-to-Severely Active Ulcerative C — pmc.ncbi.nlm.nih.gov (#1)

## q041 (competitor objective)

**Objective:** competing agents in the same mechanistic class for this indication DB-3Q, Direct Biologics LLC, Medically Refractory Crohn's Disease  
**Target sent:** drugs competing with DB-3Q: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['DB-3Q']

**q041-batch** `DB-3Q MSC-derived extracellular vesicle Crohn's competitors || DB-3Q extracellular vesicle Crohn's disease clinical trials || DB-3Q MSC-derived EV medically refractory Crohn's` → ABSTAIN, jev 348 ms

- ❌ low_evidence **0.2517** [on_target=0.64 evidence=0.39] Direct Biologics Announces Initiation of Phase 1 Clinical Trial for Medically Refractory Crohn’s Dis — biospace.com (#9)
- ❌ low_on_target **0.2255** [on_target=0.55 evidence=0.41] Bone Marrow Mesenchymal Stem Cell Derived Extracellular Vesicles (Direct Biologics) - Drug Targets,  — synapse.patsnap.com (#1)
- ❌ low_on_target **0.2065** [on_target=0.59 evidence=0.35] Direct Biologics Announces Initiation of Phase 1 Clinical Trial for Medically Refractory Crohn’s Dis — businesswire.com (#8)
- ❌ low_on_target **0.2025** [on_target=0.59 evidence=0.34] DB-3Q in Crohn Disease (CD) - Clinical Trials Registry - ICH GCP — ichgcp.net (#7) `A`
- ❌ low_on_target **0.1837** [on_target=0.58 evidence=0.32] Study Details / NCT07625293 / DB-3Q for the Treatment of Medically Refractory Crohn's Disease / Clin — clinicaltrials.gov (#6) `A`
- ❌ low_on_target **0.159** [on_target=0.53 evidence=0.30] Direct Biologics’ Phase 1 Clinical Trial Seeks to Treat Crohn Disease With Extracellular Vesicles — cgtlive.com (#10)
- ❌ low_on_target **0.1365** [on_target=0.45 evidence=0.30] Allogeneic Bone Marrow Mesenchymal Stem Cell Derived Extracellular Vesicle Isolate Product(Direct Bi — synapse.patsnap.com (#4) `A`
- ❌ low_on_target **0.106** [on_target=0.53 evidence=0.20] Search ClinicalTrials.gov for: Other terms: "direct biologics" / List Results / ClinicalTrials.gov — clinicaltrials.gov (#2) `A`
- ❌ low_on_target **0.095** [on_target=0.37 evidence=0.26] Direct Biologics Investigational Site Trials - LARVOL Sigma — sigma.larvol.com (#3)
- ❌ low_on_target **0.0831** [on_target=0.53 evidence=0.16] DB-3Q bmMSC-EVs in Patients With Perianal Fistulizing ... — clinicaltrials.gov (#5) `A`

## q042 (competitor objective)

**Objective:** Moderately to Severely Active Ulcerative Colitis, Duration 3 Months, Modified Mayo Score 5 to 9, With Inadequate Response, Loss of Response, or Intolerance to Prior Standard-of-Care Medications competing agents in the same mechanistic class as TYK2 Small Molecule  
**Target sent:** drugs competing with D-2570: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['D-2570']

**q042-batch** `D-2570 TYK2 ulcerative colitis competitor Phase 2 status` → kept 2/10, jev 408 ms

- ✅ **0.4781** [on_target=0.88 evidence=0.54] Selective tyrosine kinase 2 inhibitors in inflammatory bowel ... — sciencedirect.com (#10)
- ✅ **0.4155** [on_target=0.76 evidence=0.55] Deucravacitinib Competitive Landscape Analysis 2026 / Eureka — eureka.patsnap.com (#9)
- ❌ low_on_target **0.3283** [on_target=0.49 evidence=0.67] 
	AMG 181 Phase 2 Study in Subjects with Moderate to Severe Ulcerative Colitis - Mayo Clinic
 — mayo.edu (#3)
- ❌ low_on_target **0.3116** [on_target=0.57 evidence=0.55] Efficacy and Safety of Etrasimod in Patients With Moderately to Severely Active Ulcerative Colitis S — pubmed.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.3004** [on_target=0.53 evidence=0.57] Study Details / NCT07463183 / A Study to Evaluate Efficacy and Safety of MK-8690 in Participants Wit — clinicaltrials.gov (#2)
- ❌ low_on_target **0.2695** [on_target=0.49 evidence=0.55] Phase 2 Trial of Anti-TL1A Monoclonal Antibody... : New England Journal of Medicine — ovid.com (#1)
- ❌ low_on_target **0.1213** [on_target=0.40 evidence=0.30] Ulcerative Colitis Competitive Landscape Analysis 2026 / Eureka — eureka.patsnap.com (#6)
- ❌ low_on_target **0.1162** [on_target=0.42 evidence=0.28] Novel TYK2 inhibitor D-2570 in moderate-to-severe... : Journal of the American Academy of Dermatolog — ovid.com (#8) `A`
- ❌ low_on_target **0.0658** [on_target=0.47 evidence=0.14] IBD Research Resource Center — biosino.org (#5) `A`
- ❌ low_on_target **0.0588** [on_target=0.43 evidence=0.14] NCT07035041 / A Phase 2 Study of D-2570 in Subjects ... — clinicaltrials.gov (#7) `A`

## q043 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as VNN1, including Small Molecule therapies  
**Target sent:** drugs competing with MY009: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['MY009']

**q043-batch** `MY009 VNN1 inflammatory bowel disease competing agents` → kept 1/10, jev 381 ms

- ✅ **0.3796** [on_target=0.73 evidence=0.52] MY-009212A - Drug Targets, Indications, Patents - Patsnap Synapse — synapse.patsnap.com (#5) `A`
- ❌ low_on_target **0.2219** [on_target=0.52 evidence=0.43] What drugs are in development for Inflammatory Bowel ... — synapse.patsnap.com (#9)
- ❌ low_on_target **0.1889** [on_target=0.52 evidence=0.36] TNFα-Inhibitors in Inflammatory Bowel Disease - NCBI - NIH — ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.1408** [on_target=0.41 evidence=0.34] 
            Management of inflammatory bowel disease beyond tumor necrosis factor inhibitors: novel — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.1408** [on_target=0.33 evidence=0.43] Harnessing the Vnn1 pantetheinase pathway boosts short chain fatty acids production and mucosal prot — gut.bmj.com (#8)
- ❌ low_on_target **0.1352** [on_target=0.39 evidence=0.35] 
            Current status of novel biologics and small molecule drugs in the individualized treatm — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.1141** [on_target=0.32 evidence=0.36] Vanin1 (VNN1) in chronic diseases: Future directions for targeted ... — sciencedirect.com (#4)
- ❌ low_on_target **0.0817** [on_target=0.25 evidence=0.33] Revealing VNN1: An Emerging and Promising Target for ... — pubmed.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0555** [on_target=0.17 evidence=0.33] Combination therapy with biologics and/or small molecules in inflammatory bowel disease: a comprehen — pubmed.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.0385** [on_target=0.15 evidence=0.26] Functional polymorphisms in the regulatory regions of the ... — pubmed.ncbi.nlm.nih.gov (#10)

## q044 (competitor objective)

**Objective:** Inflammatory Bowel Disease competing agents in the same mechanistic class as GPR52 Prostaglandin E2 Receptor EP4, including Small Molecule therapies  
**Target sent:** drugs competing with NXE0033744 / NXE744: other agents in the same mechanistic class or for the same indication, as described in `objective` · anchors ['NXE0033744', 'NXE744']

**q044-batch** `NXE0033744 Phase 2 inflammatory bowel disease || NXE0033744 EP4 agonist clinical trial || NXE0033744 development stage IBD || NXE744 EP4 agonist competitors IBD` → kept 6/10, jev 384 ms

- ✅ **0.7081** [on_target=0.94 evidence=0.75] Presentation title - Nxera Pharma — investors.nxera.life (#1) `A`
- ✅ **0.5766** [on_target=0.92 evidence=0.63] Corporate Presentation - Investors - Nxera Pharma — investors.nxera.life (#9) `A`
- ✅ **0.4817** [on_target=0.85 evidence=0.57] [PDF] Nxera R&D Day Be Bold, Move Fast. — net-presentations.com (#3) `A`
- ✅ **0.4811** [on_target=0.82 evidence=0.59] Discovery of Non-prostanoid EP4 Agonists for the Treatment of Inflammatory Bowel Disease - PubMed — pubmed.ncbi.nlm.nih.gov (#8)
- ✅ **0.4564** [on_target=0.84 evidence=0.54] Nxera Pharma Operational Highlights and Consolidated — globenewswire.com (#2) `A`
- ✅ **0.368** [on_target=0.69 evidence=0.53] HCRTR x Orexin receptor - Drugs, Indications, Patents - Synapse — synapse.patsnap.com (#10) `A`
- ❌ low_evidence **0.364** [on_target=0.78 evidence=0.47] Nxera Pharma Korea Co. Ltd. - Drug pipelines, Patents, Clinical trials - Synapse — synapse.patsnap.com (#5) `A`
- ❌ low_evidence **0.3598** [on_target=0.85 evidence=0.42] NXE0033744 / Nxera Pharma - LARVOL DELTA — delta.larvol.com (#4) `A`
- ❌ low_evidence **0.3264** [on_target=0.72 evidence=0.45] NXE-0033744 by Nxera Pharma for Crohn's Disease ... — pharmaceutical-technology.com (#7) `A`
- ❌ low_evidence **0.2652** [on_target=0.78 evidence=0.34] Nxera Pharma Q1 2024 Operational Highlights and Results — synapse.patsnap.com (#6) `A`

## q045

**Objective:** BMF-500 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** BMF-500 · anchors ['BMF-500']

**q045-batch** `BMF-500 first regulatory approval AML || BMF-500 expected regulatory approval AML || BMF-500 market launch AML || BMF-500 expected launch date AML` → kept 8/10, jev 342 ms

- ✅ **0.8036** [on_target=0.98 evidence=0.82] Investigational Covalent FLT3 Inhibitor BMF-500 in ... - Biomea Fusion — investors.biomeafusion.com (#1) `A`
- ✅ **0.7676** [on_target=0.98 evidence=0.78] Biomea Fusion Announces FDA Clearance of Investigational New Drug (IND) Application for Covalent FLT — investors.biomeafusion.com (#9) `A`
- ✅ **0.721** [on_target=0.97 evidence=0.74] 10-K — sec.gov (#8) `A`
- ✅ **0.703** [on_target=0.95 evidence=0.74] Biomea Fusion Reports Third Quarter 2023 Financial Results ... — sec.gov (#2) `A`
- ✅ **0.6693** [on_target=0.97 evidence=0.69] Biomea Fusion Announces FDA Clearance of INDA for ... — drug-dev.com (#10) `A`
- ✅ **0.6143** [on_target=0.97 evidence=0.63] Covalent-103: A Phase 1, Open-Label, Dose-Escalation, and Dose-Expansion Study of Bmf-500, an Oral C — ashpublications.org (#4) `A`
- ✅ **0.6076** [on_target=0.98 evidence=0.62] BMF-500 - Drug Targets, Indications, Patents — synapse.patsnap.com (#6) `A`
- ✅ **0.6048** [on_target=0.96 evidence=0.63] Covalent-103: A phase 1, open-label, dose-escalation and expansion study of BMF-500, an oral covalen — ascopubs.org (#7) `A`
- ❌ low_evidence **0.2068** [on_target=0.94 evidence=0.22] Study Details / NCT05918692 / A Phase 1 Study of BMF-500 in Adults With Acute Leukemia / ClinicalTri — clinicaltrials.gov (#3) `A`
- ❌ low_on_target **0.0159** [on_target=0.07 evidence=0.23] 
            Recent drug approvals for acute myeloid leukemia - PMC
         — pmc.ncbi.nlm.nih.gov (#5)

## q046

**Objective:** BW-101 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** BW-101 · anchors ['BW-101']

**q046-batch** `BW-101 AML regulatory approval market launch year` → kept 2/10, jev 396 ms

- ✅ **0.5695** [on_target=0.85 evidence=0.67] Revumenib for Patients With Relapsed or Refractory (R/R) Nucleophosmin 1–Mutated (NPM1m) Acute Myelo — cms.syndax.com (#2)
- ✅ **0.4595** [on_target=0.61 evidence=0.75] FDA Approves a New Treatment for Acute Myeloid Leukemia / The AACR — aacr.org (#8)
- ❌ low_on_target **0.3854** [on_target=0.47 evidence=0.82] FDA Grants Positive Review for AML Drug Trial, First ... — curetoday.com (#9)
- ❌ low_on_target **0.2027** [on_target=0.38 evidence=0.53] FDA approves novel treatment for acute myeloid leukemia — damonrunyon.org (#10)
- ❌ low_on_target **0.1891** [on_target=0.31 evidence=0.61] Rydapt ratified: Novartis' targeted AML therapy wins FDA approval + / Bioworld / BioWorld — bioworld.com (#7)
- ❌ low_on_target **0.1722** [on_target=0.41 evidence=0.42] FDA approves new drug to treat advanced AML in adults — bloodcancerunited.org (#5)
- ❌ low_on_target **0.112** [on_target=0.24 evidence=0.47] FDA Approves First All-Oral Regimen for AML / AJMC — ajmc.com (#4)
- ❌ low_on_target **0.021** [on_target=0.07 evidence=0.30] A Landmark Year for FDA-Approved Therapies for Acute Myeloid Leukemia / The Hematologist / American  — ashpublications.org (#6)
- ❌ low_on_target **0.0105** [on_target=0.05 evidence=0.21] 
            Acute myeloid leukemia: current progress and future directions - PMC
         — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.0053** [on_target=0.02 evidence=0.27] Acute Myeloid Leukemia Treatment (PDQ®) - PDQ Cancer Information Summaries - NCBI Bookshelf — ncbi.nlm.nih.gov (#3)

## q047

**Objective:** Dual CDK12/13 Inhibitor first regulatory approval or market launch year for acute myeloid leukemia  
**Target sent:** Dual CDK12/13 Inhibitor / CDK12 · anchors ['Dual CDK12/13 Inhibitor', 'CDK12']

**q047-batch** `Dual CDK12/13 Inhibitor Insilico Medicine AML approval launch || Dual CDK12/13 Inhibitor Insilico Medicine AML regulatory timeline || Dual CDK12/13 Inhibitor AML first market launch year` → kept 9/10, jev 377 ms

- ✅ **0.8556** [on_target=0.92 evidence=0.93] CDK12/CDK13 inhibitors(Insilico Medicine Shanghai) - Drug Targets, Indications, Patents  - Synapse — synapse.patsnap.com (#3) `A`
- ✅ **0.798** [on_target=0.95 evidence=0.84] Carrick Therapeutics Announces First Patient Dosed in Phase 1 Clinical Trial of CT7439 (CDK12/13 Inh — carricktherapeutics.com (#1) `A`
- ✅ **0.5691** [on_target=0.88 evidence=0.65] Insilico Medicine Develops Novel AI-Designed CDK12/13 ... — trial.medpath.com (#9) `A`
- ✅ **0.5476** [on_target=0.86 evidence=0.64] CDK12/13 / Insilico Medicine — insilico.com (#4) `A`
- ✅ **0.546** [on_target=0.91 evidence=0.60] CDK12/13 inhibitor, CTX-439, suppresses tumor growth ... — biorxiv.org (#8) `A`
- ✅ **0.4752** [on_target=0.81 evidence=0.59] JMC｜Con la ayuda de la IA generativa, Insilico Medicine anuncia nuevos inhibidores duales de CDK12/1 — eurekalert.org (#2) `A`
- ✅ **0.4194** [on_target=0.74 evidence=0.57] Novel CDK12/13 dual inhibitors for tumour treatment - ecancer — ecancer.org (#5) `A`
- ✅ **0.4015** [on_target=0.73 evidence=0.55] Design, Synthesis, and Biological Evaluation of Novel Orally Available Covalent CDK12/13 Dual Inhibi — pubmed.ncbi.nlm.nih.gov (#6) `A`
- ✅ **0.3514** [on_target=0.62 evidence=0.57] CDK12/13 dual inhibitors are potential therapeutics for Acute ... — pmc.ncbi.nlm.nih.gov (#7) `A`
- ❌ low_on_target **0.0096** [on_target=0.04 evidence=0.24] 
            Recent drug approvals for acute myeloid leukemia - PMC
         — pmc.ncbi.nlm.nih.gov (#10)

## q048

**Objective:** dCASP1-55 first regulatory approval or market launch year in acute myeloid leukemia  
**Target sent:** dCASP1-55 · anchors ['dCASP1-55']

**q048-batch** `dCASP1-55 AML regulatory approval || dCASP1-55 AML market launch || dCASP1-55 University of Cincinnati AML clinical development` → kept 2/10, jev 361 ms

- ✅ **0.4752** [on_target=0.81 evidence=0.59] Scaffolding-dependent CASP1 constrains excessive ... — cell.com (#5) `A`
- ✅ **0.46** [on_target=0.92 evidence=0.50] PROTACs — medchemexpress.com (#9) `A`
- ❌ low_on_target **0.2662** [on_target=0.49 evidence=0.54] FDA Approves First All-Oral Regimen for AML / AJMC — ajmc.com (#6)
- ❌ low_evidence **0.2604** [on_target=0.93 evidence=0.28] dCASP1-55 / CASP1 PROTAC Degrader — medchemexpress.com (#4) `A`
- ❌ low_on_target **0.0624** [on_target=0.52 evidence=0.12] Study Details / NCT00049582 / Decitabine in Treating Patients With Myelodysplastic Syndromes or Acut — clinicaltrials.gov (#3)
- ❌ low_on_target **0.0476** [on_target=0.17 evidence=0.28] All-Oral Treatment Combo for AML Earns FDA Nod — medscape.com (#10)
- ❌ low_on_target **0.0168** [on_target=0.08 evidence=0.21] Exhibit 99.1 — sec.gov (#1)
- ❌ low_on_target **0.0113** [on_target=0.04 evidence=0.28] New AML Drugs Approved and Under Investigation in 2017 / OncLive — onclive.com (#2)
- ❌ low_on_target **0.0075** [on_target=0.03 evidence=0.25] 
            Recent drug approvals for acute myeloid leukemia - PMC
         — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0071** [on_target=0.03 evidence=0.24] A Landmark Year for FDA-Approved Therapies for Acute Myeloid Leukemia / The Hematologist / American  — ashpublications.org (#7)

## q049

**Objective:** ABSK131 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in MTAP-Deleted KRAS G12D-Mutated Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** ABSK131 · anchors ['ABSK131']

**q049-batch** `ABSK131 SU.86.86 monotherapy TGI || ABSK131 PDAC xenograft monotherapy tumour regression || ABSK131 KRAS G12D PDAC in vivo monotherapy || ABSK131 MTAP-deleted pancreatic xenograft tumour volume` → kept 6/10, jev 376 ms

- ✅ **0.6566** [on_target=0.98 evidence=0.67] ABSK131 / Abbisko — delta.larvol.com (#5) `A`
- ✅ **0.6566** [on_target=0.98 evidence=0.67] ABSK131 / Abbisko — delta.larvol.com (#6) `A`
- ✅ **0.6534** [on_target=0.98 evidence=0.67] Abstract 4504: Synergistic antitumor activity of the MTA-cooperative ... — aacrjournals.org (#8) `A`
- ✅ **0.6042** [on_target=0.92 evidence=0.66] KRAS G12D inhib News - LARVOL Sigma — sigma.larvol.com (#4) `A`
- ✅ **0.601** [on_target=0.98 evidence=0.61] Abstract LB427: The MTA-cooperative PRMT5 inhibitor ABSK131 exhibits potent activity and broad syner — aacrjournals.org (#3) `A`
- ✅ **0.5076** [on_target=0.94 evidence=0.54] ABSK-131 - Drug Targets, Indications, Patents  - Synapse — synapse.patsnap.com (#7) `A`
- ❌ low_on_target **0.155** [on_target=0.30 evidence=0.52] MAT2A inhibition blocks the growth of MTAP-deleted ... — researchgate.net (#10)
- ❌ low_on_target **0.0219** [on_target=0.09 evidence=0.24] Complete Regression of Xenograft Tumors upon Targeted ... — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.011** [on_target=0.07 evidence=0.16] Pharmacologically targeting KRAS G12D in PDAC models — biorxiv.org (#2)
- ❌ low_on_target **0.0085** [on_target=0.05 evidence=0.17] Activity Observed with Novel KRAS Inhibitor in Pancreatic Cancer - The ASCO Post — ascopost.com (#1)

## q050

**Objective:** ONC201/dordaviprone in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** ONC201/dordaviprone / ONC201 / dordaviprone · anchors ['ONC201/dordaviprone', 'ONC201', 'dordaviprone']

**q050-batch** `ONC201/dordaviprone PDAC monotherapy xenograft tumour growth inhibition` → kept 5/10, jev 403 ms

- ✅ **0.6468** [on_target=0.99 evidence=0.65] 
            Dordaviprone/ONC201 Activation of the ClpP Mitochondrial Protease Inhibits the Growth o — pmc.ncbi.nlm.nih.gov (#1) `A`
- ✅ **0.6435** [on_target=0.99 evidence=0.65] Dordaviprone/ONC201 Activation of the ClpP Mitochondrial Protease Inhibits the Growth of KRAS-Mutant — biorxiv.org (#10) `A`
- ✅ **0.5954** [on_target=0.95 evidence=0.63] IRB#17-1020 1 A Phase 2 Study of Single Agent ONC201 ... — cdn.clinicaltrials.gov (#2) `A`
- ✅ **0.5088** [on_target=0.96 evidence=0.53] A Phase 1 Randomized Study to Evaluate the Safety ... — accp1.onlinelibrary.wiley.com (#4) `A`
- ✅ **0.4864** [on_target=0.96 evidence=0.51] ONC201 (Dordaviprone) in Recurrent H3 K27M–Mutant ... - PMC - NIH — pmc.ncbi.nlm.nih.gov (#9) `A`
- ❌ low_on_target **0.0407** [on_target=0.20 evidence=0.20] Tumor growth inhibition (TGI)-monotherapy (a) and ... — researchgate.net (#5)
- ❌ low_evidence **0.024** [on_target=0.90 evidence=0.03] ONC201/dordaviprone for H3 K27M-mutant tumors: Discovery, mechanisms, therapeutic potential, and fut — pubmed.ncbi.nlm.nih.gov (#3) `A`
- ❌ low_on_target **0.006** [on_target=0.04 evidence=0.15] 
            T-cell Dependency of Tumor Regressions and Complete Responses with RAS(ON) Multi-select — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0032** [on_target=0.04 evidence=0.08] Treatment of Pancreatic Cancer Patient-Derived Xenograft ... — pubmed.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.001** [on_target=0.03 evidence=0.03] Inhibition of Cell Proliferation and Growth of Pancreatic ... — journals.plos.org (#6)

## q051

**Objective:** DWP216 in vivo monotherapy tumour growth inhibition TGI tumour regression tumour shrinkage in KRAS G12C Pancreatic Ductal Adenocarcinoma animal models  
**Target sent:** DWP216 · anchors ['DWP216']

**q051-batch** `DWP216 KRAS G12C pancreatic ductal adenocarcinoma monotherapy xenograft tumour growth inhibition regression` → kept 1/10, jev 387 ms

- ✅ **0.6273** [on_target=0.97 evidence=0.65] Abstract 7091: DWP216, a TEAD1/2 inhibitor, enhances efficacy of diverse KRAS inhibitors by reversin — aacrjournals.org (#1) `A`
- ❌ low_on_target **0.1323** [on_target=0.32 evidence=0.41] KRAS Inhibition in Pancreatic Ductal Adenocarcinoma - PMC — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0713** [on_target=0.20 evidence=0.36] 
            D‐1553: A novel KRASG12C inhibitor with potent and selective cellular and in vivo antit — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0576** [on_target=0.19 evidence=0.30] Sotorasib in KRAS p.G12C–Mutated Advanced Pancreatic Cancer / New England Journal of Medicine — nejm.org (#3)
- ❌ low_on_target **0.0445** [on_target=0.15 evidence=0.30] Mechanisms of Resistance to KRASG12C Inhibitors — christie.openrepository.com (#8)
- ❌ low_on_target **0.0244** [on_target=0.12 evidence=0.20] Activity Observed with Novel KRAS Inhibitor in Pancreatic ... — ascopost.com (#6)
- ❌ low_on_target **0.0243** [on_target=0.08 evidence=0.30] The State of KRAS Drug Development in Pancreatic Cancer — lustgarten.org (#7)
- ❌ low_on_target **0.0182** [on_target=0.07 evidence=0.26] Novel Pan-RAS Inhibitor ADT-007 Induces Tumor ... — biorxiv.org (#9)
- ❌ low_on_target **0.0152** [on_target=0.06 evidence=0.25] 
            Second-Line Treatment of Pancreatic Adenocarcinoma: Shedding Light on New Opportunities — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.003** [on_target=0.03 evidence=0.10] KRAS Inhibition in Pancreatic Ductal Adenocarcinoma — mdpi.com (#5)

## q052

**Objective:** HM100714 in vivo efficacy in combination with another agent in Head and Neck Squamous Cell Carcinoma, including the combination partner  
**Target sent:** HM100714 · anchors ['HM100714']

**q052-batch** `HM100714 HNSCC combination in vivo efficacy || HM100714 head and neck squamous cell carcinoma xenograft combination || HM100714 combination partner xenograft || HM100714 AACR HNSCC combination || HM100714 cisplatin or pembrolizumab HNSCC` → kept 2/10, jev 565 ms

- ✅ **0.5904** [on_target=0.77 evidence=0.77] 
            Exploration of Immune-Modulatory Effects of Amivantamab in Combination with Pembrolizum — pmc.ncbi.nlm.nih.gov (#1)
- ✅ **0.5826** [on_target=0.95 evidence=0.61] Abstract 5882: Structure- and bioinformatics-driven development of ... — aacrjournals.org (#10) `A`
- ❌ low_on_target **0.0364** [on_target=0.12 evidence=0.30] Efficacy and safety of immunotherapy for head and neck ... — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0194** [on_target=0.07 evidence=0.28] 
            Immunotherapies and Future Combination Strategies for Head and Neck Squamous Cell Carci — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0186** [on_target=0.13 evidence=0.14] 799 Real-world use of pembrolizumab combination regimens in first-line recurrent/metastatic head and — jitc.bmj.com (#7)
- ❌ low_on_target **0.0096** [on_target=0.08 evidence=0.12] Pembrolizumab combined with nab-paclitaxel and platinum in … — sciencedirect.com (#3)
- ❌ low_on_target **0.0089** [on_target=0.03 evidence=0.30] Head and neck squamous cell carcinoma - PMC - NIH — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0088** [on_target=0.06 evidence=0.15] 
            Safety and Efficacy of Pembrolizumab With Chemoradiotherapy in Locally Advanced Head an — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0078** [on_target=0.06 evidence=0.13] Safety and Efficacy of Pembrolizumab in Combination with Acalabrutinib in Advanced Head and Neck Squ — pubmed.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0051** [on_target=0.02 evidence=0.26] Squamous Cell Carcinoma of Head and Neck MeSH ... — meshb.nlm.nih.gov (#9)

## q053

**Objective:** ADT-1004 in vivo single-agent monotherapy tumour growth inhibition TGI tumour regression or shrinkage in Pancreatic ductal adenocarcinoma animal models  
**Target sent:** ADT-1004 · anchors ['ADT-1004']

**q053-batch** `ADT-1004 quantitative tumour growth inhibition percentage PDAC monotherapy || ADT-1004 tumour regression percentage MIA PaCa-2 xenograft || ADT-1004 KRAS G12D PDX tumour shrinkage monotherapy || ADT-1004 KPC orthotopic tumour volume change day 27 || ADT-1004 MIA-AMG-R xenograft final tumour volume monotherapy` → kept 8/10, jev 601 ms

- ✅ **0.8646** [on_target=0.99 evidence=0.87] ADT-1004: a first-in-class, oral pan-RAS inhibitor with robust antitumor activity in preclinical mod — link.springer.com (#4) `A`
- ✅ **0.846** [on_target=0.98 evidence=0.86] ADT-1004: A First-in-Class, Orally Bioavailable Selective ... — biorxiv.org (#6) `A`
- ✅ **0.8264** [on_target=0.98 evidence=0.84] ADT-1004 / Auburn University, ADT Pharma - Larvol Delta — delta.larvol.com (#2) `A`
- ✅ **0.7854** [on_target=0.99 evidence=0.79] ADT-1004: A First-in-Class, Orally Bioavailable Selective pan-RAS Inhibitor for Pancreatic Ductal Ad — biorxiv.org (#8) `A`
- ✅ **0.735** [on_target=0.98 evidence=0.75] ADT-1004: A First-in-Class, Orally Bioavailable Selective ... — biorxiv.org (#7) `A`
- ✅ **0.7056** [on_target=0.98 evidence=0.72] A potent and selective pan-RAS inhibitor, ADT-1004, ... — asco.org (#9) `A`
- ✅ **0.699** [on_target=0.98 evidence=0.71] ADT-1004: a first-in-class, oral pan-RAS inhibitor with robust ... — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.6014** [on_target=0.97 evidence=0.62] ADT-1004 / ADT-007 Prodrug / MedChemExpress — medchemexpress.com (#1) `A`
- ❌ low_evidence **0.3298** [on_target=0.97 evidence=0.34] A potent and selective pan-RAS inhibitor, ADT-1004, targeting complex KRAS mutations for pancreatic  — ascopubs.org (#3) `A`
- ❌ low_on_target **0.0033** [on_target=0.03 evidence=0.11] 
            A Comparative Analysis of Orthotopic and Subcutaneous Pancreatic Tumour Models: Tumour  — pmc.ncbi.nlm.nih.gov (#10)

## q054

**Objective:** DWP216 in vivo animal models and results: cell-line xenograft (CDX), patient-derived xenograft (PDX), syngeneic, orthotopic, or genetically engineered models  
**Target sent:** DWP216 · anchors ['DWP216']

**q054-batch** `DWP216 HNSCC in vivo xenograft monotherapy || DWP216 NCI-H1373 monotherapy tumour volume || DWP216 pancreatic cancer PDX syngeneic orthotopic || DWP216 CAPAN-1 xenograft monotherapy 1200 mm3 || DWP216 genetically engineered mouse model` → kept 1/10, jev 473 ms

- ✅ **0.7081** [on_target=0.97 evidence=0.73] pan-TEAD inhib News - LARVOL Sigma — sigma.larvol.com (#3) `A`
- ❌ low_on_target **0.248** [on_target=0.40 evidence=0.62] In vivo evaluation of HER-2-specific ADCs in a mouse ... — researchgate.net (#5)
- ❌ low_on_target **0.1675** [on_target=0.25 evidence=0.67] 
            Polymeric nanoparticle-docetaxel for the treatment of advanced solid tumors: phase I cl — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.1671** [on_target=0.28 evidence=0.60] In vivo Wnt pathway inhibition of human squamous cell carcinoma ... — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0779** [on_target=0.19 evidence=0.41] A KrasG12D-driven genetic mouse model of pancreatic cancer requires glypican-1 for efficient prolife — pubmed.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0527** [on_target=0.17 evidence=0.31] In vivo Efficacy Studies in Cell Line and Patient-derived ... - PMC — pmc.ncbi.nlm.nih.gov (#9)
- ❌ low_on_target **0.0222** [on_target=0.07 evidence=0.32] Novel orthotopic patient-derived xenograft model using ... - PMC — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.0186** [on_target=0.06 evidence=0.31] Generation and application of patient-derived xenograft ... — mednexus.org (#7)
- ❌ low_on_target **0.0145** [on_target=0.05 evidence=0.29] 
            Genetically Engineered Mouse Models of Pancreatic Cancer: The KPC Model (LSL-KrasG12D/+ — pmc.ncbi.nlm.nih.gov (#4)
- ❌ low_on_target **0.0124** [on_target=0.04 evidence=0.31] Preclinical mouse models for immunotherapeutic and non-immunotherapeutic drug development for pancre — apc.amegroups.org (#8)

## q055

**Objective:** DB-1305/Anti-PD-L1/VEGF Bispecific Antibody patients studied in Recurrent or Disseminated HNSCC (Oral Cavity/Oropharynx/Hypopharynx/Larynx), Incurable by Local Therapies trials: biomarker selection, disease severity, line of therapy, and required prior treatment  
**Target sent:** DB-1305 · anchors ['DB-1305']

**q055-batch** `DB-1305 recurrent metastatic HNSCC prior treatment line of therapy || DB-1305 HNSCC PD-L1 biomarker eligibility || DB-1305 HNSCC ECOG measurable disease inclusion criteria` → kept 2/10, jev 532 ms

- ✅ **0.7353** [on_target=0.82 evidence=0.90] 
	NCT06496178  - Victorian Cancer Trials Link
 — trials.cancervic.org.au (#9)
- ✅ **0.5339** [on_target=0.88 evidence=0.61] Abstract 648: Activity of BNT327/PM8002 (PD-L1 x VEGF-A bispecific antibody) in combination with BNT — aacrjournals.org (#2) `A`
- ❌ low_evidence **0.4449** [on_target=0.94 evidence=0.47] UCLA Head and Neck Squamous Cell Carcinoma Clinical Trials — ucla.clinicaltrials.researcherprofiles.org (#8) `A`
- ❌ low_on_target **0.0523** [on_target=0.16 evidence=0.33] Phase III randomized trial of chemotherapy with or without bevacizumab (B) in patients (pts) with re — ascopubs.org (#1)
- ❌ low_on_target **0.0523** [on_target=0.16 evidence=0.33] PD-L1: a novel prognostic biomarker in head and neck squamous cell carcinoma / Oncotarget — oncotarget.com (#3)
- ❌ low_on_target **0.0319** [on_target=0.11 evidence=0.29] PD-1, PD-L1 / Oncology Nursing Society — ons.org (#6)
- ❌ low_on_target **0.0264** [on_target=0.08 evidence=0.33] 
            Biomarkers in head and neck squamous cell carcinoma: unraveling the path to precision i — pmc.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0226** [on_target=0.07 evidence=0.32] 
            Paradigm Change in First-Line Treatment of Recurrent and/or Metastatic Head and Neck Sq — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0194** [on_target=0.06 evidence=0.32] The role of systemic therapy in patients with recurrent or metastatic ... — sciencedirect.com (#7)
- ❌ low_on_target **0.0113** [on_target=0.04 evidence=0.28] Recurrent/metastatic relapse after definitive treatment ... - PMC — pmc.ncbi.nlm.nih.gov (#4)

## q056

**Objective:** MNPS Asset planned or expected data readouts, regulatory submissions, regulatory decisions, and expected timing in Head and Neck Cancer  
**Target sent:** MNPS · anchors ['MNPS']

**q056-batch** `MNPS Asset first-line recurrent metastatic head and neck cancer data readout || MNPS Asset head and neck cancer regulatory submission || MNPS Asset head and neck cancer regulatory decision` → kept 4/10, jev 346 ms

- ✅ **0.6663** [on_target=0.76 evidence=0.88] Petosemtamab Gets Breakthrough Therapy Status for ... — cancertherapyadvisor.com (#10)
- ✅ **0.6557** [on_target=0.70 evidence=0.94] Subcutaneous Amivantamab Receives FDA Priority Review in R/M HNSCC — cancernetwork.com (#6)
- ✅ **0.5597** [on_target=0.73 evidence=0.77] Dostarlimab Monotherapy Elicits Responses in First-Line ... — onclive.com (#9)
- ✅ **0.5368** [on_target=0.61 evidence=0.88] Head & Neck Cancer / Clinical / CancerNetwork — cancernetwork.com (#4)
- ❌ low_on_target **0.3511** [on_target=0.46 evidence=0.76] FDA Grants Designation to Investigational Drug for Head ... — curetoday.com (#8)
- ❌ low_on_target **0.228** [on_target=0.40 evidence=0.57] FDA Approves Keytruda for Head and Neck Cancer — curetoday.com (#7)
- ❌ low_on_target **0.1808** [on_target=0.31 evidence=0.58] New Findings Show Durable Anti-Tumor Activity with KEYTRUDA® (pembrolizumab), Merck’s Anti-PD-1 Ther — merck.com (#2)
- ❌ low_on_target **0.0317** [on_target=0.10 evidence=0.32] Head & Neck Cancers / Clinical / OncLive — onclive.com (#1)
- ❌ low_on_target **0.028** [on_target=0.10 evidence=0.28] HEAD & NECK CANCERS / Clinical / Targeted Oncology - Immunotherapy, Biomarkers, and Cancer Pathways — targetedonc.com (#3)
- ❌ low_on_target **0.0082** [on_target=0.06 evidence=0.14] Submissions to the Office of Oncologic Diseases (OOD) — fda.gov (#5)

## q057

**Objective:** CNP200137 first regulatory approval or market launch year for acute myeloid leukemia  
**Target sent:** CNP200137 · anchors ['CNP200137']

**q057-batch** `CNP200137 regulatory approval AML || CNP200137 market launch AML` → kept 3/10, jev 356 ms

- ✅ **0.9244** [on_target=0.98 evidence=0.94] CNP200137 - Drug Targets, Indications, Patents  - Synapse — synapse.patsnap.com (#4) `A`
- ✅ **0.672** [on_target=0.72 evidence=0.93] FDA Approves a New Treatment for Acute Myeloid Leukemia / The AACR — aacr.org (#9)
- ✅ **0.6642** [on_target=0.68 evidence=0.98] VENCLEXTA® (venetoclax) Receives FDA Full Approval for Acute Myeloid Leukemia (AML) — prnewswire.com (#10)
- ❌ low_on_target **0.3109** [on_target=0.44 evidence=0.71] FDA Approves First Maintenance Therapy for AML — medscape.com (#5)
- ❌ low_on_target **0.0946** [on_target=0.22 evidence=0.43] Recent drug approvals for acute myeloid leukemia / Journal of Hematology & Oncology / Springer Natur — link.springer.com (#7)
- ❌ low_on_target **0.0756** [on_target=0.18 evidence=0.42] A Landmark Year for FDA-Approved Therapies for Acute Myeloid Leukemia / The Hematologist / American  — ashpublications.org (#8)
- ❌ low_on_target **0.059** [on_target=0.15 evidence=0.39] 
            Recent drug approvals for acute myeloid leukemia - PMC
         — pmc.ncbi.nlm.nih.gov (#6)
- ❌ low_on_target **0.027** [on_target=0.09 evidence=0.30] 
            Cutting Edge Molecular Therapy for Acute Myeloid Leukemia - PMC
         — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.0255** [on_target=0.09 evidence=0.28] Advances in the drug therapies of acute myeloid leukemia ... — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.008** [on_target=0.03 evidence=0.27] Acute Myeloid Leukemia Treatment (PDQ®) - NCI - National Cancer Institute — cancer.gov (#1)

## q058

**Objective:** HEC234055 in vivo efficacy in combination with another agent in Pancreatic Ductal Adenocarcinoma, including the combination partner  
**Target sent:** HEC234055 · anchors ['HEC234055']

**q058-batch** `HEC234055 combination pancreatic ductal adenocarcinoma in vivo || HEC234055 combination partner PDAC xenograft || HEC234055 AACR 2026 combination efficacy` → ABSTAIN, jev 348 ms

- ❌ low_evidence **0.4** [on_target=0.96 evidence=0.42] HEC234055 - Drug Targets, Indications, Patents — synapse.patsnap.com (#8) `A`
- ❌ low_evidence **0.3621** [on_target=0.97 evidence=0.37] HEC 234055 - AdisInsight — adisinsight.springer.com (#10) `A`
- ❌ low_on_target **0.2067** [on_target=0.39 evidence=0.53] Cantargia Highlights Preclinical Data at AACR Supporting Nadunolimab in Combination with RAS Inhibit — biospace.com (#9)
- ❌ low_on_target **0.1629** [on_target=0.27 evidence=0.60] 
            Emerging therapeutic advancements in pancreatic cancer: a contemporary review - PMC
    — pmc.ncbi.nlm.nih.gov (#7)
- ❌ low_on_target **0.1484** [on_target=0.28 evidence=0.53] [PDF] Phase I+Phase II Clinical Study of PRaG Therapy in Combination ... — cdn.clinicaltrials.gov (#2)
- ❌ low_on_target **0.0194** [on_target=0.07 evidence=0.28] Targeted Therapy in Pancreatic Ductal Adenocarcinoma: Current Advances and Challenges — mdpi.com (#6)
- ❌ low_on_target **0.0148** [on_target=0.06 evidence=0.25] Pancreatic Ductal Adenocarcinoma: MicroRNAs Affecting ... — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.014** [on_target=0.05 evidence=0.28] Current and emerging strategies to enhance chemotherapeutic efficacy in pancreatic ductal adenocarci — link.springer.com (#3)
- ❌ low_on_target **0.0092** [on_target=0.03 evidence=0.31] 
            Therapeutic Status and Available Strategies in Pancreatic Ductal Adenocarcinoma - PMC
  — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.0056** [on_target=0.03 evidence=0.19] In vivo models of pancreatic ductal adenocarcinoma - PubMed — pubmed.ncbi.nlm.nih.gov (#4)

## q059

**Objective:** HEC234055 in vivo animal models and results: cell-line xenograft (CDX), patient-derived xenograft (PDX), syngeneic, orthotopic, genetically engineered models  
**Target sent:** HEC234055 · anchors ['HEC234055']

**q059-batch** `HEC234055 HNSCC xenograft || HEC234055 PDX model || HEC234055 syngeneic model || HEC234055 orthotopic pancreatic model || HEC234055 genetically engineered mouse model` → ABSTAIN, jev 362 ms

- ❌ low_evidence **0.3232** [on_target=0.96 evidence=0.34] HEC 234055 - AdisInsight — adisinsight.springer.com (#7) `A`
- ❌ low_on_target **0.0965** [on_target=0.15 evidence=0.64] Establishment of Highly Transplantable Cholangiocarcinoma Cell Lines from a Patient-Derived Xenograf — pubmed.ncbi.nlm.nih.gov (#10)
- ❌ low_on_target **0.0609** [on_target=0.11 evidence=0.55] Patient-derived xenograft models of Fanconi... : Journal of Clinical Investigation — qa-ai.ovid.com (#2)
- ❌ low_on_target **0.0462** [on_target=0.09 evidence=0.51] Patient-derived xenograft models of Fanconi... : Journal of Clinical Investigation — dev-ai.ovid.com (#9)
- ❌ low_on_target **0.039** [on_target=0.10 evidence=0.39] 
            Establishment and Thorough Characterization of Xenograft (PDX) Models Derived from Pati — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.0243** [on_target=0.07 evidence=0.35] 
            Genetically Engineered Mouse Models of Pancreatic Cancer: The KPC Model (LSL-KrasG12D/+ — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.0243** [on_target=0.07 evidence=0.35] 
            A fast, simple, and cost-effective method of expanding patient-derived xenograft mouse  — pmc.ncbi.nlm.nih.gov (#5)
- ❌ low_on_target **0.0226** [on_target=0.07 evidence=0.32] Clinically relevant orthotopic pancreatic cancer models ... - PMC — pmc.ncbi.nlm.nih.gov (#8)
- ❌ low_on_target **0.0194** [on_target=0.06 evidence=0.32] Preclinical mouse models for immunotherapeutic and non-immunotherapeutic drug development for pancre — apc.amegroups.org (#4)
- ❌ low_on_target **0.0158** [on_target=0.05 evidence=0.32] 
            Patient-derived xenograft models in hepatopancreatobiliary cancer - PMC
         — pmc.ncbi.nlm.nih.gov (#6)

## q060

**Objective:** EOM613 sponsor development stage indication public source  
**Target sent:** EOM613 Crohn's disease / EOM613 · anchors ["EOM613 Crohn's disease", 'EOM613']

**q060-batch** `EOM613 Crohn's disease trial current status || EOM613 Crohn's disease Phase 2 initiation 2026 || EOM613 Crohn's disease clinical trial registry` → kept 5/10, jev 366 ms

- ✅ **0.797** [on_target=0.98 evidence=0.81] EOM Pharmaceutical Holdings Reports Promising ... — biospace.com (#5) `A`
- ✅ **0.797** [on_target=0.98 evidence=0.81] EOM Pharmaceutical Holdings Provides an Update on its ... — prnewswire.com (#6) `A`
- ✅ **0.7395** [on_target=0.85 evidence=0.87] Study Details / nct06456593 / Efficacy and Safety of Obefazimod in Subjects With Moderately to Sever — clinicaltrials.gov (#4)
- ✅ **0.6207** [on_target=0.70 evidence=0.89] Study Details / NCT07077746 / HB-adMSCs for the Treatment of Crohn's Disease / ClinicalTrials.gov — clinicaltrials.gov (#3)
- ✅ **0.5144** [on_target=0.61 evidence=0.84] Study Details / NCT06548542 / Study of Targeted Therapies for the Treatment of Adult Participants Wi — clinicaltrials.gov (#9)
- ❌ low_on_target **0.364** [on_target=0.39 evidence=0.93] Study Details / NCT03261206 / Stopping Aminosalicylate Therapy in Inactive Crohn's Disease / Clinica — clinicaltrials.gov (#2)
- ❌ low_on_target **0.3525** [on_target=0.45 evidence=0.78] Crohnsmapvaccine — platform.tracxn.com (#1)
- ❌ low_evidence **0.3197** [on_target=0.69 evidence=0.46] EOM Pharmaceutical Holdings Provides an Update on its Lead Drug Candidate EOM613 — eompharma.com (#10) `A`
- ❌ low_on_target **0.0946** [on_target=0.17 evidence=0.56] Crohns' Disease Clinical Trial Drug Development Pipeline — openpr.com (#8)
- ❌ low_on_target **0.0072** [on_target=0.06 evidence=0.12] Registry and Biorepository for IBD in Central Texas — clinicaltrials.gov (#7)

## q061

**Objective:** FG-3149 sponsor development stage indication public source  
**Target sent:** FG-3149 · anchors ['FG-3149']

**q061-batch** `FG-3149 sponsor development stage || FG-3149 Crohn's disease || FG-3149 FibroGen clinical development` → kept 3/10, jev 345 ms

- ✅ **0.8112** [on_target=0.86 evidence=0.94] FibroGen Announces First Patient Enrolled in ... — parentprojectmd.org (#4)
- ✅ **0.637** [on_target=0.98 evidence=0.65] 
            Mechanical stress-induced connective tissue growth factor plays a critical role in inte — pmc.ncbi.nlm.nih.gov (#5) `A`
- ✅ **0.615** [on_target=0.75 evidence=0.82] Study Details / NCT05197049 / A Study of Guselkumab Subcutaneous Therapy in Participants With Modera — clinicaltrials.gov (#3)
- ❌ low_on_target **0.0642** [on_target=0.47 evidence=0.14] FibroGen (Alumni) — foresitecapital.com (#7)
- ❌ low_on_target **0.027** [on_target=0.10 evidence=0.27] Crohn’s & Colitis Foundation IBD Ventures Fibrostenosis Therapeutics — crohnscolitisfoundation.org (#9)
- ❌ low_on_target **0.0081** [on_target=0.09 evidence=0.09] [PDF] FibroGen China Sale Presentation - Kyntra Bio — investor.kyntrabio.com (#1)
- ❌ low_on_target **0.0052** [on_target=0.04 evidence=0.13] Treatment for Crohn's Disease - NIDDK — niddk.nih.gov (#10)
- ❌ low_on_target **0.0027** [on_target=0.04 evidence=0.07] FibroGen Announces Clinical Trial Supply Agreement with — globenewswire.com (#2)
- ❌ low_on_target **0.0026** [on_target=0.07 evidence=0.04] FibroGen: FG-3246 for mCRPC (Metastatic Castration- ... — dukecancerinstitute.org (#8)
- ❌ low_on_target **0.0023** [on_target=0.07 evidence=0.03] FibroGen Announces FDA Clearance for FG-3165 IND ... — synapse.patsnap.com (#6)

## q062

**Objective:** HDM-3018 sponsor Huadong Medicine Co. Ltd., development stage Preclinical, and indication Inflammatory Bowel Disease  
**Target sent:** HDM-3018 · anchors ['HDM-3018']

**q062-batch** `HDM-3018 Huadong Medicine sponsor || HDM-3018 development stage || HDM-3018 inflammatory bowel disease indication` → kept 1/10, jev 397 ms

- ✅ **0.967** [on_target=0.98 evidence=0.99] HDM3018 - Drug Targets, Indications, Patents  - Synapse — synapse.patsnap.com (#5) `A`
- ❌ low_on_target **0.1439** [on_target=0.26 evidence=0.55] ISM5411, A NOVEL GUT-RESTRICTED PHD1/2 INHIBITOR FOR INFLAMMATORY BOWEL DISEASE: A RANDOMIZED, DOUBL — academic.oup.com (#3)
- ❌ low_on_target **0.073** [on_target=0.15 evidence=0.49] CLINICAL TRIAL PROTOCOL A Phase II, Randomized, Double-blind, Placebo-controlled Study to Evaluate t — cdn.clinicaltrials.gov (#4)
- ❌ low_on_target **0.0406** [on_target=0.23 evidence=0.18] Huadong Medicine — platform.tracxn.com (#1)
- ❌ low_on_target **0.027** [on_target=0.09 evidence=0.30] Current scenario in inflammatory bowel disease: Drug development ... — link.springer.com (#10)
- ❌ low_on_target **0.0199** [on_target=0.13 evidence=0.15] huadonglicenseandcollabo - SEC.gov — sec.gov (#7)
- ❌ low_on_target **0.0156** [on_target=0.18 evidence=0.09] Huadong Medicine Co., Ltd. Third Quarterly Report 2025 — disc.static.szse.cn (#2)
- ❌ low_on_target **0.0126** [on_target=0.14 evidence=0.09] Huadong Medicine Co., Ltd. - Drug pipelines, Patents, Clinical trials - Synapse — synapse.patsnap.com (#6)
- ❌ low_on_target **0.0112** [on_target=0.16 evidence=0.07] Huadong Medicine — pharmaboardroom.com (#8)
- ❌ low_on_target **0.0104** [on_target=0.12 evidence=0.09] [PDF] Huadong Medicine Co., Ltd. Third Quarterly Report 2024 — static.cninfo.com.cn (#9)

## q063

**Objective:** Granisetron in Head and Neck Cancer: clinical trial population, biomarker or severity selection, line of therapy, and required prior treatment  
**Target sent:** Granisetron · anchors ['Granisetron']

**q063-batch** `Granisetron recurrent metastatic head and neck cancer clinical trial eligibility || Granisetron head and neck cancer Phase 2 prior treatment || Granisetron head and neck cancer biomarker ECOG || Granisetron Kyowa Kirin head and neck cancer trial` → ABSTAIN, jev 332 ms

- ❌ low_evidence **0.3594** [on_target=0.98 evidence=0.37] Granisetron: MedlinePlus Drug Information — medlineplus.gov (#9) `A`
- ❌ low_evidence **0.0696** [on_target=0.95 evidence=0.07] Study of Granisetron Hydrochloride Nasal Spray (GNS) in ... — clinicaltrials.gov (#6) `A`
- ❌ low_on_target **0.0052** [on_target=0.03 evidence=0.17] Frontiers / Evidence-Based Treatment Options in Recurrent and/or Metastatic Squamous Cell Carcinoma  — frontiersin.org (#10)
- ❌ low_on_target **0.0032** [on_target=0.02 evidence=0.16] 
            Head and neck cancer – emerging targeted therapies - PMC
         — pmc.ncbi.nlm.nih.gov (#1)
- ❌ low_on_target **0.0027** [on_target=0.04 evidence=0.07] Study Details / NCT03546582 / SBRT +/- Pembrolizumab in Patients With Local-Regionally Recurrent or  — clinicaltrials.gov (#3)
- ❌ low_on_target **0.0016** [on_target=0.03 evidence=0.05] Head and Neck Cancer Clinical Trials / Center for Cancer Research — ccr.cancer.gov (#4)
- ❌ low_on_target **0.0013** [on_target=0.03 evidence=0.04] [PDF] NCTN Head and Neck Cancer Trials Portfolio (Open as of 5/15/2026) — dctd.cancer.gov (#2)
- ❌ low_on_target **0.0009** [on_target=0.02 evidence=0.05] Head And Neck Cancers Clinical Trials - Mayo Clinic Research — mayo.edu (#8)
- ❌ low_on_target **0.0006** [on_target=0.02 evidence=0.03] Study Details / NCT00003257 / Gene Therapy in Treating Patients With Recurrent Head and Neck Cancer  — clinicaltrials.gov (#7)
- ❌ low_on_target **0.0003** [on_target=0.03 evidence=0.01] Head and neck cancer Archives — ecog-acrin.org (#5)

## q064

**Objective:** HPV Vaccine (HAd5 Vector) in Head and Neck Cancer: clinical trial population, biomarker or severity selection, line of therapy, and required prior treatment  
**Target sent:** HPV Vaccine (HAd5 Vector) ImmunityBio / HAd5 · anchors ['HPV Vaccine (HAd5 Vector) ImmunityBio', 'HAd5']

**q064-batch** `HPV Vaccine (HAd5 Vector) ImmunityBio head and neck cancer clinical trial eligibility || HPV Vaccine (HAd5 Vector) ImmunityBio HPV biomarker head and neck cancer || HPV Vaccine (HAd5 Vector) ImmunityBio recurrent metastatic head and neck cancer prior treatment || HPV Vaccine (HAd5 Vector) ImmunityBio phase 2 trial inclusion criteria` → kept 3/10, jev 353 ms

- ✅ **0.7892** [on_target=0.89 evidence=0.89] HPV+ / HPV- 2nd Line Head & Neck Cancer - ImmunityBio — immunitybio.com (#5)
- ✅ **0.6641** [on_target=0.87 evidence=0.76] Immunotherapy Clinical Trials Pipeline - ImmunityBio — immunitybio.com (#10)
- ✅ **0.6141** [on_target=0.94 evidence=0.65] HPV Vaccine Clinical Trials / Human Papillomavirus Research — immunitybio.com (#4) `A`
- ❌ low_on_target **0.1518** [on_target=0.29 evidence=0.52] 
            The current landscape of therapeutic vaccination approaches for treatment of HPV-depend — pmc.ncbi.nlm.nih.gov (#2)
- ❌ low_on_target **0.1353** [on_target=0.58 evidence=0.23] Clinical Trial Research Studies for Cancer & Disease — immunitybio.com (#6) `A`
- ❌ low_on_target **0.1144** [on_target=0.39 evidence=0.29] ImmunityBio Announces Completion of $470 Million Post ... — immunitybio.com (#7) `A`
- ❌ low_on_target **0.114** [on_target=0.18 evidence=0.63] Study Details / NCT07065630 / Response-Adaptive Treatment in Untreated Locoregional HPV-Negative Hea — clinicaltrials.gov (#9)
- ❌ low_on_target **0.0573** [on_target=0.20 evidence=0.29] 
            Immunotherapy Approaches in HPV-Associated Head and Neck Cancer - PMC
         — pmc.ncbi.nlm.nih.gov (#3)
- ❌ low_on_target **0.054** [on_target=0.27 evidence=0.20] ImmunityBio, Inc. - Drug pipelines, Patents, Clinical trials - Synapse — synapse.patsnap.com (#8)
- ❌ low_on_target **0.0504** [on_target=0.17 evidence=0.30] Frontiers / Head and neck cancer therapeutic vaccines: a review — frontiersin.org (#1)


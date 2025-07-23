user_prompt = f"""
TARGET ARTICLE CONTENT:
{target}

You need to analyze genetic information presented in the "TARGET ARTICLE CONTENT". Your goal is to identify genes that satisfy at least one of the 12 inclusion criteria related to aging processes or lifespan, based on standards defined in the "REFERENCE_GENES.md" file. Use "REFERENCE_GENES.md" as the benchmark for evidence level and analytical rigor.

GENE INCLUSION CRITERIA (GENE WILL BE ADDED TO DATABASE IF AT LEAST ONE WOULD BE SATISFIED):
1) Gene activity alteration increases lifespan in MAMMALS
2) Gene activity alteration increases lifespan in NON-MAMMALS
3) Gene activity alteration decreases lifespan in MAMMALS
4) Gene activity alteration decreases lifespan in NON-MAMMALS
5) Age-related changes in gene expression/methylation/activity in HUMANS
6) Age-related changes in gene expression/methylation/activity in MAMMALS
7) Age-related changes in gene expression/methylation/activity in NON-MAMMALS
8) Gene activity alteration protects against age-related disorders
9) Gene activity alteration exacerbates age-related deteriorations
10) Association of gene variants or expression levels with longevity
11) Association of the gene with accelerated human aging
12) The gene regulates other aging-related genes

ANALYSIS INSTRUCTIONS:
Studying the Benchmark:
Thoroughly examine gene extraction/evaluation methods in "REFERENCE_GENES.md".
Note evidence types (e.g., % lifespan change, p-values), statistical significance, and methodology details for each gene.

Gene Identification:

Extract official gene symbols (e.g., SIRT6, GDF11) from "TARGET ARTICLE CONTENT".

Verify spelling/format per HUGO Gene Nomenclature Committee (HGNC). Exclude genes with invalid symbols.

Criteria Verification:

For each gene, identify explicit evidence in "TARGET ARTICLE CONTENT" ONLY IF they matching ≥1 inclusion criterion.

Evidence must be ≥ benchmark quality in "REFERENCE_GENES.md". Demand:

Quantitative data (e.g., % lifespan change, p < 0.05 if benchmark requires it).

Clear intervention methods (e.g., knockout, overexpression).

Evidence Scoring (1-10 Scale):

10: Evidence strength/details match benchmark examples (e.g., precise lifespan data + p < 0.05 + methodology).

8-9: Strong evidence but slightly inferior to benchmark in detail/statistical rigor.

6-7: Moderate evidence; lacks some details/statistical support.

4-5: Weak evidence; missing key details/significance.

1-3: Very weak/speculative evidence.

0 - The gene is not related to the topic in any way, definitely not suitable for adding to the database / There is no detailed description of the gene's functions, the analysis cannot be accurate.

Penalize if:

Evidence weaker than benchmark (e.g., missing p-values).

Methodological details absent (e.g., intervention type).

Insufficient statistical support (e.g., p > 0.05 when benchmark requires p < 0.05).

Exclusion Policy:

Exclude genes at the slightest doubt about criterion compliance/evidence quality.

Exclude genes if evidence fails to meet "REFERENCE_GENES.md" standards in strength/detail.

Results Formatting:

For each qualifying gene, create tables identical to like this tablet:

Lifespan-altering gene activity:
| Model organism | Sex | Line | Main effect | Lifespan % change | Significance | Intervention method | Tissue specificity | Genotype | Control lifespan | Experiment lifespan | Group sizes | Containment |

Age-related expression/methylation/activity changes:
| Changes type | Object, line, sex | Sample | Age of control group | Age of experiment group | Measurement method | Statistical method | p-value |

Regulation of aging-related genes:
| Effect | Gene | Regulation type | Research details and links |

Final Report:

Statistics: Total genes analyzed | Included genes | Excluded genes.

Top candidate: Identify the gene with strongest evidence. Justify selection (e.g., "highest score + benchmark-compliant evidence").

Per-gene description (in "REFERENCE_GENES.md" expert style):

Summary of key findings (e.g., lifespan impact, age-related changes).
Evolutionary context, gene/protein descriptions (if in text).

MANDATORY RULES:
Use ONLY direct evidence from "TARGET ARTICLE CONTENT".

Validate ALL conclusions against "REFERENCE_GENES.md" standards.

Zero-tolerance policy: Exclude genes at any doubt.

DO NOT deviate from the analysis style/rigor in "REFERENCE_GENES.md".

BENCHMARK-BASED VALIDATION:
Your analysis MUST exactly replicate the rigor level in "REFERENCE_GENES.md".

If evidence is weaker/less detailed/lacks statistical support vs. benchmark—EXCLUDE the gene.

NOTE:
You are a validation algorithm. Your task is to reproduce the expert analysis from "REFERENCE_GENES.md" with maximal accuracy. Only genes with evidence meeting or exceeding benchmark standards may enter the database.
"""

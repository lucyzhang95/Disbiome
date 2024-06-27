# Disbiome_data
Parse the data from Disbiome database in order to include in the potential Biological Knowledge Graph

## Data Summary: (11/08/2023)
- 10,837 total records in Disbiome
- 10,837 total records in the output
- 95 records do not have taxid (10837 - 10742 = 95)
- meddra_id: 323 total - 1 None value  = 322 unique meddra_id
- meddra_id: 46 mapped to MONDO, 2 mapped to Human Phenotype (HP), 1 to Disease Ontology (DOID), 81 to The Experimental Factor Ontology (EFO), 8 to Orphanet rare disease, and 184 meddra_ids
- Disease: 10,697 records with ontology IDs + 140 no ontology IDs = 10,837 records
- Field count: `{'MedDRA': 5009, 'EFO': 4529, 'MONDO': 928, 'Orphanet': 217, 'HP': 14}`
- ncbi_taxid: 1535 unique taxid value
- ncbi_taxid rank types: 10,617 records with rank + 220 no rank keys = 10,837 records
- Number of records: `{'species': 5099, 'genus': 4509, 'family': 721, 'phylum': 161, 'order': 58, 'class': 43, 'strain': 14, 'no rank': 6, 'subspecies': 4, 'clade': 2}`
- 'no rank' above in the dictionary means 'rank': 'no rank', since these records have viruses: `['respiratory syncytial virus', 'hsv-1', 'ebv', 'ureaplasma parvum serovar 3', 'epstein-barr virus', 'respiratory syncytial virus']`
- Number of unique organism in different ranks: `{'species': 768, 'genus': 604, 'family': 119, 'phylum': 17, 'order': 15, 'class': 7, 'strain': 3, 'no rank': 5, 'subspecies': 3, 'clade': 2}`
- Publications: 10,837 records (19 records do not have doi/pmid/pmcid/url publication info )
- Field count: `{'publication_id': 10837, 'title': 10837, 'doi': 10590, 'pmid': 10031, 'pmcid': 573, 'pubmed_url': 192}`
  

## Output Example:
```ruby
{
   "association":{
      "predicate":"OrganismalEntityAsAModelOfDiseaseAssociation",
      "qualifier":"decreased",
      "method_name":"Metagenomic sequencing",
      "host_type":"human",
      "control_name":"healthy control",
      "sources":"feces"
   },
   "object":{
      "id":"EFO:1000653",
      "name":"sarcopenia",
      "type":"biolink:Disease",
      "meddra":10063024,
      "meddra_level":"preferred_term",
      "efo":"1000653"
   },
   "subject":{
      "id":"taxid:216816",
      "taxid":216816,
      "name":"bifidobacterium longum",
      "type":"biolink:Bacterium",
      "scientific_name":"bifidobacterium longum",
      "parent_taxid":1678,
      "lineage":[
         216816,
         1678,
         31953,
         85004,
         1760,
         201174,
         1783272,
         2,
         131567,
         1
      ],
      "rank":"species"
   },
   "publications":{
      "publication_id":1224,
      "title":"Bifidobacterium as a Potential Biomarker of Sarcopenia in Elderly Women",
      "type":"biolink:Publication",
      "pmcid":"10005572",
      "doi":"10.3390/nu15051266"
   }
}
```

## Records missing publication info:
- 9 records do not have pubmed_url

<details>
<summary>Click to expand!</summary>
  
1. No pubmed_url: publication_id: 58, Alterations of the subgingival microbiota in pediatric Crohn's Disease studied longitudinally in discovery and validation cohorts..
2. No pubmed_url: publication_id: 188, Increased archaea species and changes with therapy in gut microbiome of multiple sclerosis subjects..
3. No pubmed_url: publication_id: 217, The oral microflora in obesity and type-2 diabetes.
4. No pubmed_url: publication_id: 554, The nasopharyngeal microbiota in patients with viral respiratory tract infections is enriched in bacterial pathogens.
5. No pubmed_url: publication_id: 650, Dandruff is associated with disequilibrium in the proportion of the major bacterial and fungal populations colonizing the scalp.
6. No pubmed_url: publication_id: 942, The sinonasal mycobiota in chronic rhinosinusitis and control patients.
7. No pubmed_url: publication_id: 1021, Change of the duodenal mucosa-associated microbiota is related to intestinal metaplasia.
8. No pubmed_url: publication_id: 1044, Cytokine levels and salivary microbiome play a potential role in oral lichen planus diagnosis.
9. No pubmed_url: publication_id: 1213, Intestinal microbiota composition in patients with amyotrophic lateral sclerosis: establishment of bacterial and archaeal communities analyses.

</details>

- 19 records do not have any publication info (only have paper title)

<details>
<summary>Click to expand!</summary>

```
[{'publication_id': 58, 'title': "Alterations of the subgingival microbiota in pediatric Crohn's Disease studied longitudinally in discovery and validation cohorts."}, {'publication_id': 188, 'title': 'Increased archaea species and changes with therapy in gut microbiome of multiple sclerosis subjects.'}, {'publication_id': 217, 'title': 'The oral microflora in obesity and type-2 diabetes'}, {'publication_id': 554, 'title': 'The nasopharyngeal microbiota in patients with viral respiratory tract infections is enriched in bacterial pathogens'}, {'publication_id': 650, 'title': 'Dandruff is associated with disequilibrium in the proportion of the major bacterial and fungal populations colonizing the scalp'}, {'publication_id': 942, 'title': 'The sinonasal mycobiota in chronic rhinosinusitis and control patients'}]
```

</details>

## Records with same association between microbe and disease but based on different samples and publications:

For example:
- Same _id but different samples

<details>
  <summary>Click to expand!</summary>
  
{```'_id': '189330_OrganismalEntityAsAModelOfDiseaseAssociation_10061536'```, 'edge': "dorea_associated_with_parkinson's_disease", 'association': {'predicate': 'OrganismalEntityAsAModelOfDiseaseAssociation', 'qualifier': 'reduced', 'method': 'RNA gene amplicon sequencing', ```'sample': 'faeces'```, 'host_type': 'human', 'control_name': 'healthy control'}, 'object': {'meddra_id': '10061536', 'name': "parkinson's disease", 'meddra_level': 'preferred_term', 'id': '10061536'}, 'subject': {'id': '189330', 'organism_name': 'dorea'}, 'publications': {'publication_id': 44, 'title': "Colonic bacterial composition in Parkinson's Disease", 'pubmed_url': 'https://www.ncbi.nlm.nih.gov/pubmed/26179554', 'pmid': '26179554'}}

{```'_id': '189330_OrganismalEntityAsAModelOfDiseaseAssociation_10061536'```, 'edge': "dorea_associated_with_parkinson's_disease", 'association': {'predicate': 'OrganismalEntityAsAModelOfDiseaseAssociation', 'qualifier': 'reduced', 'method': 'RNA gene amplicon sequencing', ```'sample': 'tissue biopsie'```, 'host_type': 'human', 'control_name': 'healthy control'}, 'object': {'meddra_id': '10061536', 'name': "parkinson's disease", 'meddra_level': 'preferred_term', 'id': '10061536'}, 'subject': {'id': '189330', 'organism_name': 'dorea'}, 'publications': {'publication_id': 44, 'title': "Colonic bacterial composition in Parkinson's Disease", 'pubmed_url': 'https://www.ncbi.nlm.nih.gov/pubmed/26179554', 'pmid': '26179554'}}

</details>


- Same _id but different publications

<details>
  <summary>Click to expand!</summary>
  
{```'_id': '543_OrganismalEntityAsAModelOfDiseaseAssociation_10019641'```, 'edge': 'enterobacteriaceae_associated_with_cirrhosis', 'association': {'predicate': 'OrganismalEntityAsAModelOfDiseaseAssociation', 'qualifier': 'elevated', 'method': '16S rRNA sequencing', 'sample': 'faeces', 'host_type': 'human', 'control_name': 'healthy control'}, 'object': {'meddra_id': '10019641', 'name': 'cirrhosis', 'meddra_level': 'preferred_term', 'id': '10019641'}, 'subject': {'id': '543', 'organism_name': 'enterobacteriaceae'}, 'publications': {```'publication_id': 50```, 'title': 'Altered profile of human gut microbiome is associated with cirrhosis and its complications', 'pubmed_url': 'https://www.ncbi.nlm.nih.gov/pubmed/24374295', 'pmid': '24374295'}}

{```'_id': '543_OrganismalEntityAsAModelOfDiseaseAssociation_10019641'```, 'edge': 'enterobacteriaceae_associated_with_cirrhosis', 'association': {'predicate': 'OrganismalEntityAsAModelOfDiseaseAssociation', 'qualifier': 'elevated', 'method': '16S rRNA sequencing', 'sample': 'faeces', 'host_type': 'human', 'control_name': 'healthy control'}, 'object': {'meddra_id': '10019641', 'name': 'cirrhosis', 'meddra_level': 'preferred_term', 'id': '10019641'}, 'subject': {'id': '543', 'organism_name': 'enterobacteriaceae'}, 'publications': {```'publication_id': 51```, 'title': 'Characterization of fecal microbial communities in patients with liver cirrhosis', 'pubmed_url': 'https://www.ncbi.nlm.nih.gov/pubmed/21574172', 'pmid': '21574172'}}

</details>

## Records do not have ncbi_taxids:
Some of due to the organism cluster (a group of organisms), some due to taxonomy name changes (The mapping between old and new taxids can be found [here](https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/) merged.dmp file)

<details>
  <summary>Click to expand!</summary>

merged.dmp file: <br>

```Merged nodes file fields:```

	old_tax_id                              -- id of nodes which has been merged
	new_tax_id                              -- id of nodes which is result of merging

</details>

### Details of records do not have ncbi_taxids
#### If I can find out the specific species in the group, and then add in the information, it will be really helpful.

<details>
  <summary>Click to expand!</summary>


Disbiome Experiment Data: <br>

```[{"experiment_id": "organism_name", "disease": "disease_name"}]```
 
```
[{'Experiment_id': 3, 'organism': 'Clostridia cluster I', 'disease': 'Autism'}, {'Experiment_id': 416, 'organism': 'Clostridiales XIV', 'disease': 'Cirrhosis'}, {'Experiment_id': 486, 'organism': 'TM7', 'disease': "Crohn's Disease"}, {'Experiment_id': 756, 'organism': 'Clostridium cluster IV', 'disease': 'Atopy'}, {'Experiment_id': 764, 'organism': 'Mitis group streptococci', 'disease': 'Caries'}, {'Experiment_id': 781, 'organism': 'Bacteroides-Prevotella group', 'disease': 'Celiac Disease, Coaliac disease'}, {'Experiment_id': 937, 'organism': 'Clostridium cluster XIVa', 'disease': 'Cystic Fibrosis'}, {'Experiment_id': 1232, 'organism': 'TM7', 'disease': 'Chronic Obstructive Pulmonary Disease'}, {'Experiment_id': 1335, 'organism': 'Clostridia cluster I', 'disease': 'Juvenile Idiopathic Arthritis'}, {'Experiment_id': 1336, 'organism': 'Clostridium cluster IV', 'disease': 'Preterm birth'}, {'Experiment_id': 1337, 'organism': 'Clostridium cluster XIVa', 'disease': 'Preterm birth'}, {'Experiment_id': 1339, 'organism': 'Clostridium cluster XVIII', 'disease': 'Preterm birth'}, {'Experiment_id': 1364, 'organism': 'TM7', 'disease': 'Aggressive periodontitis'}, {'Experiment_id': 1482, 'organism': 'Gemellales', 'disease': 'Pneumonia'}, {'Experiment_id': 1638, 'organism': 'Clostridium cluster IV', 'disease': 'Polycystic Ovary Syndrome'}, {'Experiment_id': 2012, 'organism': 'anaerobacter', 'disease': 'Chronic Obstructive Pulmonary Disease'}, {'Experiment_id': 2080, 'organism': 'Clostridium cluster IV', 'disease': "Inactive Crohn's Disease"}, {'Experiment_id': 2084, 'organism': 'Bacteriodes-Prevotella', 'disease': "Inactive Crohn's Disease"}, {'Experiment_id': 2278, 'organism': 'Mitis group streptococci', 'disease': 'Chronic lung disease'}, {'Experiment_id': 2397, 'organism': 'Bacteroides-Prevotella group', 'disease': "Crohn's Disease"}, {'Experiment_id': 2410, 'organism': 'Clostridium coccoides group', 'disease': 'Anorexia Nervosa'}, {'Experiment_id': 2411, 'organism': 'Clostridium leptum subgroup', 'disease': 'Anorexia Nervosa'}, {'Experiment_id': 2412, 'organism': 'Bacteroides fragilis group', 'disease': 'Anorexia Nervosa'}, {'Experiment_id': 2457, 'organism': 'Clostridium coccoides group', 'disease': 'Short Bowel Syndrome'}, {'Experiment_id': 2632, 'organism': 'anaerobacter', 'disease': 'Non-alcoholic fatty liver disease'}, {'Experiment_id': 2708, 'organism': 'Clostridiales XIV', 'disease': 'Cirrhosis'}, {'Experiment_id': 2719, 'organism': 'Clostridium coccoides group', 'disease': 'Non alcoholic steatohepatitis'}, {'Experiment_id': 2825, 'organism': 'Clostridium coccoides group', 'disease': "Crohn's Disease"}, {'Experiment_id': 2960, 'organism': 'Clostridium coccoides group', 'disease': "Crohn's Disease"}, {'Experiment_id': 2964, 'organism': 'Clostridium coccoides group', 'disease': 'Ulcerative Colitis'}, {'Experiment_id': 3047, 'organism': 'anaerobacter', 'disease': 'Chronic kidney disease'}, {'Experiment_id': 3053, 'organism': 'Clostridium coccoides group', 'disease': 'Chronic kidney disease'}, {'Experiment_id': 3060, 'organism': 'Clostridium cluster IV', 'disease': 'Ulcerative Colitis'}, {'Experiment_id': 3063, 'organism': 'Clostridium cluster IV', 'disease': "Crohn's Disease"}, {'Experiment_id': 3065, 'organism': 'Clostridium cluster XIVa', 'disease': "Crohn's Disease"}, {'Experiment_id': 3068, 'organism': 'Clostridium cluster XIVa', 'disease': 'Ulcerative Colitis'}, {'Experiment_id': 3287, 'organism': 'Clostridium cluster IV', 'disease': "Parkinson's Disease"}, {'Experiment_id': 3290, 'organism': 'Clostridium cluster XVIII', 'disease': "Parkinson's Disease"}, {'Experiment_id': 3822, 'organism': 'Clostridium cluster IV', 'disease': 'Idiopathic nephrotic syndrome'}, {'Experiment_id': 3823, 'organism': 'Clostridium cluster XIVa', 'disease': 'Idiopathic nephrotic syndrome'}, {'Experiment_id': 3935, 'organism': 'Clostridium cluster XIVa', 'disease': 'Pancreatitis'}, {'Experiment_id': 3952, 'organism': 'Clostridium cluster IV', 'disease': 'Hepatitis B'}, {'Experiment_id': 4017, 'organism': 'Clostridium cluster IV', 'disease': 'Hepatitis C'}, {'Experiment_id': 4018, 'organism': 'Clostridium cluster XIVa', 'disease': 'Hepatitis C'}, {'Experiment_id': 4142, 'organism': 'Clostridium cluster IV', 'disease': 'Budd-Chiari syndrome'}, {'Experiment_id': 4184, 'organism': 'Clostridium cluster IV', 'disease': 'Pancreatic cancer'}, {'Experiment_id': 4200, 'organism': 'TM7', 'disease': 'Asthma'}, {'Experiment_id': 4215, 'organism': 'Clostridium cluster IV', 'disease': 'Idiopathic nephrotic syndrome'}, {'Experiment_id': 4216, 'organism': 'Clostridium cluster XIVa', 'disease': 'Idiopathic nephrotic syndrome'}, {'Experiment_id': 4347, 'organism': 'Clostridium cluster XIVa', 'disease': 'Infantile eczema'}, {'Experiment_id': 4702, 'organism': 'TM7', 'disease': "Behcet's Disease"}, {'Experiment_id': 4889, 'organism': 'TM7', 'disease': 'Oral cancer'}, {'Experiment_id': 4890, 'organism': 'SR1', 'disease': 'Oral cancer'}, {'Experiment_id': 5018, 'organism': 'Clostridium cluster XIVa', 'disease': 'Primary biliary cholangitis'}, {'Experiment_id': 5020, 'organism': 'Clostridium cluster XIVa', 'disease': 'Autoimmune hepatitis'}, {'Experiment_id': 5461, 'organism': 'TM7', 'disease': 'Clonorchis sinensis infection'}, {'Experiment_id': 5496, 'organism': 'Clostridium cluster XIVa', 'disease': 'Type 1 Diabetes'}, {'Experiment_id': 5499, 'organism': 'Clostridium cluster IV', 'disease': 'Type 1 Diabetes'}, {'Experiment_id': 5593, 'organism': 'Clostridium cluster XIVb', 'disease': 'Hepatocellular cancer'}, {'Experiment_id': 5597, 'organism': 'Clostridium cluster IV', 'disease': 'Hepatocellular cancer'}, {'Experiment_id': 6109, 'organism': 'Clostridium cluster XVIII', 'disease': 'Drug-resistant Epilepsy'}, {'Experiment_id': 6220, 'organism': 'TM7', 'disease': 'Halitosis'}, {'Experiment_id': 6339, 'organism': 'Clostridium cluster IV', 'disease': "Crohn's Disease"}, {'Experiment_id': 6679, 'organism': 'Candidatus', 'disease': 'Chronic kidney disease'}, {'Experiment_id': 7427, 'organism': 'SR1', 'disease': 'Halitosis'}, {'Experiment_id': 7429, 'organism': 'TM7', 'disease': 'Halitosis'}, {'Experiment_id': 7451, 'organism': 'Clostridium III', 'disease': 'Obstructive sleep apnea-hypopnea syndrome'}, {'Experiment_id': 7461, 'organism': 'Gp21', 'disease': 'Obstructive sleep apnea-hypopnea syndrome'}, {'Experiment_id': 7462, 'organism': 'Gp7', 'disease': 'Obstructive sleep apnea-hypopnea syndrome'}, {'Experiment_id': 7677, 'organism': 'Clostridium cluster IV', 'disease': 'Diarrhea'}, {'Experiment_id': 7683, 'organism': 'Clostridium cluster XIVb', 'disease': 'Ankylosing spondylitis'}, {'Experiment_id': 8014, 'organism': 'Clostridium cluster XIVa', 'disease': 'Obesity'}, {'Experiment_id': 8020, 'organism': 'Clostridium cluster IV', 'disease': 'Obesity'}, {'Experiment_id': 8289, 'organism': 'Clostridium cluster XVIII', 'disease': 'Gastric carcinoma'}, {'Experiment_id': 8363, 'organism': 'Clostridium cluster IV', 'disease': 'Collagenous colitis'}, {'Experiment_id': 8557, 'organism': 'Clostridium cluster IV', 'disease': 'Chronic kidney disease'}, {'Experiment_id': 8647, 'organism': 'TM7', 'disease': 'Colorectal cancer'}, {'Experiment_id': 8675, 'organism': 'TM7', 'disease': 'Edentulism'}, {'Experiment_id': 8861, 'organism': 'Clostridium cluster XIVa', 'disease': 'Osteoporosis'}, {'Experiment_id': 8990, 'organism': 'Clostridium III', 'disease': 'Uveitits'}, {'Experiment_id': 8994, 'organism': 'Clostridium cluster XVIII', 'disease': 'Uveitits'}, {'Experiment_id': 9051, 'organism': 'TM7', 'disease': 'periodontitis'}, {'Experiment_id': 9071, 'organism': 'TM7', 'disease': 'Autism spectrum disorders'}, {'Experiment_id': 9269, 'organism': 'TM7', 'disease': 'periodontitis'}, {'Experiment_id': 9355, 'organism': 'Clostridium cluster XIVa', 'disease': 'Biliary atresia'}, {'Experiment_id': 9516, 'organism': 'Clostridium cluster XIVa', 'disease': 'Posttraumatic stress syndrome'}, {'Experiment_id': 9628, 'organism': 'anaerobacter', 'disease': 'Neuromyelitis optica'}, {'Experiment_id': 9689, 'organism': 'TM7', 'disease': 'Extrinsic black stain'}, {'Experiment_id': 9959, 'organism': 'Clostridium coccoides group', 'disease': 'Ischemic stroke'}, {'Experiment_id': 9960, 'organism': 'Bacteroides fragilis group', 'disease': 'Ischemic stroke'}, {'Experiment_id': 10442, 'organism': 'Clostridium cluster IV', 'disease': 'Kidney stone with hypertension'}, {'Experiment_id': 10577, 'organism': 'Clostridium cluster IV', 'disease': 'Multiple Sclerosis'}, {'Experiment_id': 10593, 'organism': 'Clostridium cluster XVIII', 'disease': 'Major depressive disorder'}, {'Experiment_id': 10602, 'organism': 'Clostridium cluster XVIII', 'disease': 'Major depressive disorder'}, {'Experiment_id': 11448, 'organism': 'Absiella innocuum', 'disease': 'Sarcopenia'}]
```

</details>

## TODO: 
1. Find species in different Clostridia clusters.
- [EZBioCloud](https://help.ezbiocloud.net/taxonomy-of-clostridium-cluster-xiva-iv/) mentions the species in Clostridum clusters XIVa and IV.
- I have found another [source](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6656338/#sup1) with bacterial species in different Clostridum clusters. The .docx file can be downloaded [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6656338/bin/supplementary_matrial_evz096.docx). I might need to map the organism name to the Disbiome organims_name or write a new function using biothings_client to map it, so that I can use for other data sources. <br>

	The .docx file looks like:
	
	<details>
	  <summary>Click to expand!</summary>

   	```
	
	Organism name	Completeness1	Clostridial cluster2	Contigs	Length	N503	L504
	Clostridium_acetobutylicum_ATCC_824_2	98.03	I	2	4132880	3940880	1
	Clostridium_acetobutylicum_DSM_1731_61	98.03	I	3	4145581	3942462	1
	Clostridium_acetobutylicum_DSM_1732_527	98.43	I	55	4091215	270881	6
	Clostridium_acetobutylicum_EA_2018_57	98.03	I	2	4132226	3940230	1
	Clostridium_acetobutylicum_GXAS18_1_231	98.43	I	49	3796049	325351	4
	Clostridium_acetobutylicum_NCCB_24020_525	98.82	I	20	4098731	759218	2
	Clostridium_stercorarium_sub. thermolacticum_DSM2910_441	98.03	III	1	3035622	2970010	1
	Clostridium_termitidis_CT1112_89	98.43	III	78	6415858	146289	15
	Clostridium_leptum_DSM_753_25	97.64	iv /XIVa	21	3270209	452649	4
	Clostridium_sporosphaeroides_DSM_1294_VPI_4527_111	97.24	IV/XIVa	21	3174421	324437	4
	Clostridioides_difficile_VL_0092_988	98.82	XIa	321	4157070	90393	16
   	```
	
	</details>

2. Obtain pmid/pmcid/doi for the weird pubmed_url format of 192 records in Disbiome
   - can use [ncbi eutils package](https://www.ncbi.nlm.nih.gov/books/NBK25500/) to get the pubmed_id from these urls
   - make sure to return one specific paper from the query result

   Example: `"pubmed_url": "https://www.ncbi.nlm.nih.gov/pubmed?term=(Community%20dynamics%20and%20the%20lower%20airway%20microbiota%20in%20stable%20chronic%20obstructive%20pulmonary%20disease%2C%20smokers%20and%20healthy%20non-smokers.)"`

4. Figure out what is the best hierarchy of the microorganism to use for the subsequent analyses.

![The Hierarchy of Bacteria](https://atlasbiomed.com/blog/content/images/2021/06/2020-06-05-Taxonomy.png)
   - For example, I have `Eubacterium rectale` and its NCBI blast name is `firmicutes`, where it shows a classification of several clades of bacteria that are gram-positive with a low DNA mol% G+C and have rigid cells walls containing muramic acid. In theory, these bacteria should have some conserved proteins or pathways that are associated with certain disease. It could be easier to calculate similarity scores. 



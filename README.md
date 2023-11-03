# Disbiome_data
Parse the data from Disbiome database in order to include in the potential Biological Knowledge Graph

## Data Summary:
- 10837 records originally in Disbiome
- 10742 records in the output total with 2322 records with duplicated _id
- 95 records do not have taxid (10837 - 10742 = 95)
- 8420 records without duplicated output_dict _id
- meddra_id: 322 unique meddra_id (46 meddra_id are mapped to MONDO, 276 has no mapping)
- ncbi_taxid: 1535 unique taxid value


## Output Example:
```ruby
{
    "_id":"e44e6b852420495cb815004e725f53a3",
    "association":{
        "predicate":"OrganismalEntityAsAModelOfDiseaseAssociation",
        "qualifier":"reduced",
        "sample_name":"faeces"
    },
    "object":{
        "name":"pulmonary arterial hypertension",
        "type":"biolink:Disease",
        "id":"MONDO:0005149",
        "meddra_id":"10037400",
        "meddra_level":"preferred_term",
        "mondo":"0005149"
    },
    "subject":{
        "id":"taxid:310298",
        "organism_name":"bacteroides coprocola",
        "type":"biolink:OrganismalEntity",
        "scientific_name":"phocaeicola coprocola",
        "parent_taxid":909656,
        "lineage":[
            310298,
            909656,
            815,
            171549,
            200643,
            976,
            68336,
            1783270,
            2,
            131567,
            1
        ],
        "rank":"species"
    },
    "publications":{
        "publication_id":1097,
        "title":"Altered gut microbiome profile in patients with pulmonary arterial hypertension",
        "pmid":"32088998",
        "doi":"10.1161/HYPERTENSIONAHA.119.14294"
    }
}
```

## Records do not have pubmed_url:
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

## Records with duplicated _id:

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
#### The bacterial cluster information is very important for the subsequent analysis, so it's better to keep them in some format with the associations between the group and disease.
#### If I can find out the specific species in the group, and then add in the information, it will be really helpful.
#### TODO: find species in different Clostridia clusters. [EZBioCloud](https://help.ezbiocloud.net/taxonomy-of-clostridium-cluster-xiva-iv/) mentions the species in Clostridum clusters XIVa and IV.

<details>
  <summary>Click to expand!</summary>


Disbiome Experiment Data: <br>

```[{"experiment_id": "organism_name", "disease": "disease_name"}]```
 
```
[{'Experiment_id': 3, 'organism': 'Clostridia cluster I', 'disease': 'Autism'}, {'Experiment_id': 416, 'organism': 'Clostridiales XIV', 'disease': 'Cirrhosis'}, {'Experiment_id': 486, 'organism': 'TM7', 'disease': "Crohn's Disease"}, {'Experiment_id': 756, 'organism': 'Clostridium cluster IV', 'disease': 'Atopy'}, {'Experiment_id': 764, 'organism': 'Mitis group streptococci', 'disease': 'Caries'}, {'Experiment_id': 781, 'organism': 'Bacteroides-Prevotella group', 'disease': 'Celiac Disease, Coaliac disease'}, {'Experiment_id': 937, 'organism': 'Clostridium cluster XIVa', 'disease': 'Cystic Fibrosis'}, {'Experiment_id': 1232, 'organism': 'TM7', 'disease': 'Chronic Obstructive Pulmonary Disease'}, {'Experiment_id': 1335, 'organism': 'Clostridia cluster I', 'disease': 'Juvenile Idiopathic Arthritis'}, {'Experiment_id': 1336, 'organism': 'Clostridium cluster IV', 'disease': 'Preterm birth'}, {'Experiment_id': 1337, 'organism': 'Clostridium cluster XIVa', 'disease': 'Preterm birth'}, {'Experiment_id': 1339, 'organism': 'Clostridium cluster XVIII', 'disease': 'Preterm birth'}, {'Experiment_id': 1364, 'organism': 'TM7', 'disease': 'Aggressive periodontitis'}, {'Experiment_id': 1482, 'organism': 'Gemellales', 'disease': 'Pneumonia'}, {'Experiment_id': 1638, 'organism': 'Clostridium cluster IV', 'disease': 'Polycystic Ovary Syndrome'}, {'Experiment_id': 2012, 'organism': 'anaerobacter', 'disease': 'Chronic Obstructive Pulmonary Disease'}, {'Experiment_id': 2080, 'organism': 'Clostridium cluster IV', 'disease': "Inactive Crohn's Disease"}, {'Experiment_id': 2084, 'organism': 'Bacteriodes-Prevotella', 'disease': "Inactive Crohn's Disease"}, {'Experiment_id': 2278, 'organism': 'Mitis group streptococci', 'disease': 'Chronic lung disease'}, {'Experiment_id': 2397, 'organism': 'Bacteroides-Prevotella group', 'disease': "Crohn's Disease"}, {'Experiment_id': 2410, 'organism': 'Clostridium coccoides group', 'disease': 'Anorexia Nervosa'}, {'Experiment_id': 2411, 'organism': 'Clostridium leptum subgroup', 'disease': 'Anorexia Nervosa'}, {'Experiment_id': 2412, 'organism': 'Bacteroides fragilis group', 'disease': 'Anorexia Nervosa'}, {'Experiment_id': 2457, 'organism': 'Clostridium coccoides group', 'disease': 'Short Bowel Syndrome'}, {'Experiment_id': 2632, 'organism': 'anaerobacter', 'disease': 'Non-alcoholic fatty liver disease'}, {'Experiment_id': 2708, 'organism': 'Clostridiales XIV', 'disease': 'Cirrhosis'}, {'Experiment_id': 2719, 'organism': 'Clostridium coccoides group', 'disease': 'Non alcoholic steatohepatitis'}, {'Experiment_id': 2825, 'organism': 'Clostridium coccoides group', 'disease': "Crohn's Disease"}, {'Experiment_id': 2960, 'organism': 'Clostridium coccoides group', 'disease': "Crohn's Disease"}, {'Experiment_id': 2964, 'organism': 'Clostridium coccoides group', 'disease': 'Ulcerative Colitis'}, {'Experiment_id': 3047, 'organism': 'anaerobacter', 'disease': 'Chronic kidney disease'}, {'Experiment_id': 3053, 'organism': 'Clostridium coccoides group', 'disease': 'Chronic kidney disease'}, {'Experiment_id': 3060, 'organism': 'Clostridium cluster IV', 'disease': 'Ulcerative Colitis'}, {'Experiment_id': 3063, 'organism': 'Clostridium cluster IV', 'disease': "Crohn's Disease"}, {'Experiment_id': 3065, 'organism': 'Clostridium cluster XIVa', 'disease': "Crohn's Disease"}, {'Experiment_id': 3068, 'organism': 'Clostridium cluster XIVa', 'disease': 'Ulcerative Colitis'}, {'Experiment_id': 3287, 'organism': 'Clostridium cluster IV', 'disease': "Parkinson's Disease"}, {'Experiment_id': 3290, 'organism': 'Clostridium cluster XVIII', 'disease': "Parkinson's Disease"}, {'Experiment_id': 3822, 'organism': 'Clostridium cluster IV', 'disease': 'Idiopathic nephrotic syndrome'}, {'Experiment_id': 3823, 'organism': 'Clostridium cluster XIVa', 'disease': 'Idiopathic nephrotic syndrome'}, {'Experiment_id': 3935, 'organism': 'Clostridium cluster XIVa', 'disease': 'Pancreatitis'}, {'Experiment_id': 3952, 'organism': 'Clostridium cluster IV', 'disease': 'Hepatitis B'}, {'Experiment_id': 4017, 'organism': 'Clostridium cluster IV', 'disease': 'Hepatitis C'}, {'Experiment_id': 4018, 'organism': 'Clostridium cluster XIVa', 'disease': 'Hepatitis C'}, {'Experiment_id': 4142, 'organism': 'Clostridium cluster IV', 'disease': 'Budd-Chiari syndrome'}, {'Experiment_id': 4184, 'organism': 'Clostridium cluster IV', 'disease': 'Pancreatic cancer'}, {'Experiment_id': 4200, 'organism': 'TM7', 'disease': 'Asthma'}, {'Experiment_id': 4215, 'organism': 'Clostridium cluster IV', 'disease': 'Idiopathic nephrotic syndrome'}, {'Experiment_id': 4216, 'organism': 'Clostridium cluster XIVa', 'disease': 'Idiopathic nephrotic syndrome'}, {'Experiment_id': 4347, 'organism': 'Clostridium cluster XIVa', 'disease': 'Infantile eczema'}, {'Experiment_id': 4702, 'organism': 'TM7', 'disease': "Behcet's Disease"}, {'Experiment_id': 4889, 'organism': 'TM7', 'disease': 'Oral cancer'}, {'Experiment_id': 4890, 'organism': 'SR1', 'disease': 'Oral cancer'}, {'Experiment_id': 5018, 'organism': 'Clostridium cluster XIVa', 'disease': 'Primary biliary cholangitis'}, {'Experiment_id': 5020, 'organism': 'Clostridium cluster XIVa', 'disease': 'Autoimmune hepatitis'}, {'Experiment_id': 5461, 'organism': 'TM7', 'disease': 'Clonorchis sinensis infection'}, {'Experiment_id': 5496, 'organism': 'Clostridium cluster XIVa', 'disease': 'Type 1 Diabetes'}, {'Experiment_id': 5499, 'organism': 'Clostridium cluster IV', 'disease': 'Type 1 Diabetes'}, {'Experiment_id': 5593, 'organism': 'Clostridium cluster XIVb', 'disease': 'Hepatocellular cancer'}, {'Experiment_id': 5597, 'organism': 'Clostridium cluster IV', 'disease': 'Hepatocellular cancer'}, {'Experiment_id': 6109, 'organism': 'Clostridium cluster XVIII', 'disease': 'Drug-resistant Epilepsy'}, {'Experiment_id': 6220, 'organism': 'TM7', 'disease': 'Halitosis'}, {'Experiment_id': 6339, 'organism': 'Clostridium cluster IV', 'disease': "Crohn's Disease"}, {'Experiment_id': 6679, 'organism': 'Candidatus', 'disease': 'Chronic kidney disease'}, {'Experiment_id': 7427, 'organism': 'SR1', 'disease': 'Halitosis'}, {'Experiment_id': 7429, 'organism': 'TM7', 'disease': 'Halitosis'}, {'Experiment_id': 7451, 'organism': 'Clostridium III', 'disease': 'Obstructive sleep apnea-hypopnea syndrome'}, {'Experiment_id': 7461, 'organism': 'Gp21', 'disease': 'Obstructive sleep apnea-hypopnea syndrome'}, {'Experiment_id': 7462, 'organism': 'Gp7', 'disease': 'Obstructive sleep apnea-hypopnea syndrome'}, {'Experiment_id': 7677, 'organism': 'Clostridium cluster IV', 'disease': 'Diarrhea'}, {'Experiment_id': 7683, 'organism': 'Clostridium cluster XIVb', 'disease': 'Ankylosing spondylitis'}, {'Experiment_id': 8014, 'organism': 'Clostridium cluster XIVa', 'disease': 'Obesity'}, {'Experiment_id': 8020, 'organism': 'Clostridium cluster IV', 'disease': 'Obesity'}, {'Experiment_id': 8289, 'organism': 'Clostridium cluster XVIII', 'disease': 'Gastric carcinoma'}, {'Experiment_id': 8363, 'organism': 'Clostridium cluster IV', 'disease': 'Collagenous colitis'}, {'Experiment_id': 8557, 'organism': 'Clostridium cluster IV', 'disease': 'Chronic kidney disease'}, {'Experiment_id': 8647, 'organism': 'TM7', 'disease': 'Colorectal cancer'}, {'Experiment_id': 8675, 'organism': 'TM7', 'disease': 'Edentulism'}, {'Experiment_id': 8861, 'organism': 'Clostridium cluster XIVa', 'disease': 'Osteoporosis'}, {'Experiment_id': 8990, 'organism': 'Clostridium III', 'disease': 'Uveitits'}, {'Experiment_id': 8994, 'organism': 'Clostridium cluster XVIII', 'disease': 'Uveitits'}, {'Experiment_id': 9051, 'organism': 'TM7', 'disease': 'periodontitis'}, {'Experiment_id': 9071, 'organism': 'TM7', 'disease': 'Autism spectrum disorders'}, {'Experiment_id': 9269, 'organism': 'TM7', 'disease': 'periodontitis'}, {'Experiment_id': 9355, 'organism': 'Clostridium cluster XIVa', 'disease': 'Biliary atresia'}, {'Experiment_id': 9516, 'organism': 'Clostridium cluster XIVa', 'disease': 'Posttraumatic stress syndrome'}, {'Experiment_id': 9628, 'organism': 'anaerobacter', 'disease': 'Neuromyelitis optica'}, {'Experiment_id': 9689, 'organism': 'TM7', 'disease': 'Extrinsic black stain'}, {'Experiment_id': 9959, 'organism': 'Clostridium coccoides group', 'disease': 'Ischemic stroke'}, {'Experiment_id': 9960, 'organism': 'Bacteroides fragilis group', 'disease': 'Ischemic stroke'}, {'Experiment_id': 10442, 'organism': 'Clostridium cluster IV', 'disease': 'Kidney stone with hypertension'}, {'Experiment_id': 10577, 'organism': 'Clostridium cluster IV', 'disease': 'Multiple Sclerosis'}, {'Experiment_id': 10593, 'organism': 'Clostridium cluster XVIII', 'disease': 'Major depressive disorder'}, {'Experiment_id': 10602, 'organism': 'Clostridium cluster XVIII', 'disease': 'Major depressive disorder'}, {'Experiment_id': 11448, 'organism': 'Absiella innocuum', 'disease': 'Sarcopenia'}]
```

</details>

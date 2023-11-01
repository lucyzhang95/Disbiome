# Disbiome_data
Parse the data from Disbiome database in order to include in the potential Biological Knowledge Graph

## Data Summary:
- 10837 records originally in Disbiome
- 10742 records in the output total with 2322 records with duplicated _id
- 95 records do not have taxid (10837 - 10742 = 95)
- 8420 records without duplicated output_dict _id
- meddra_id: 322 without duplicates (46 meddra_id are mapped to MONDO, 276 has no mapping)
- ncbi_taxid: 1535 without duplicates


## Output Example:
```ruby
{
    "_id":"207244_OrganismalEntityAsAModelOfDiseaseAssociation_10028245",
    "edge":"anaerostipes_associated_with_multiple_sclerosis",
    "association":{
        "predicate":"OrganismalEntityAsAModelOfDiseaseAssociation",
        "qualifier":"reduced",
        "method":"16S rRNA sequencing",
        "sample_name":"faeces",
        "host_type":"human",
        "control_name":"healthy control"
    },
    "object":{
        "meddra_id":"10028245",
        "name":"multiple sclerosis",
        "meddra_level":"preferred_term",
        "id":"10028245"
    },
    "subject":{
        "id":"207244",
        "organism_name":"anaerostipes",
        "scientific_name":"anaerostipes",
        "parent_taxid":186803,
        "lineage":[
            207244,
            186803,
            186802,
            186801,
            1239,
            1783272,
            2,
            131567,
            1
        ],
        "rank":"genus"
    },
    "publications":{
        "publication_id":1220,
        "title":"Alterations of host-gut microbiome interactions in multiple sclerosis",
        "pubmed_url":"https://pubmed.ncbi.nlm.nih.gov/35094961/",
        "pmid":"35094961"
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
<details>
  <summary>Click to expand!</summary>


Disbiome Experiment Data: <br>

```[{"experiment_id": "organism_name"}]```
 
```
[{'3': 'Clostridia cluster I'}, {'416': 'Clostridiales XIV'}, {'486': 'TM7'}, {'756': 'Clostridium cluster IV'}, {'764': 'Mitis group streptococci'}, {'781': 'Bacteroides-Prevotella group'}, {'937': 'Clostridium cluster XIVa'}, {'1232': 'TM7'}, {'1335': 'Clostridia cluster I'}, {'1336': 'Clostridium cluster IV'}, {'1337': 'Clostridium cluster XIVa'}, {'1339': 'Clostridium cluster XVIII'}, {'1364': 'TM7'}, {'1482': 'Gemellales'}, {'1638': 'Clostridium cluster IV'}, {'2012': 'anaerobacter'}, {'2080': 'Clostridium cluster IV'}, {'2084': 'Bacteriodes-Prevotella'}, {'2278': 'Mitis group streptococci'}, {'2397': 'Bacteroides-Prevotella group'}, {'2410': 'Clostridium coccoides group'}, {'2411': 'Clostridium leptum subgroup'}, {'2412': 'Bacteroides fragilis group'}, {'2457': 'Clostridium coccoides group'}, {'2632': 'anaerobacter'}, {'2708': 'Clostridiales XIV'}, {'2719': 'Clostridium coccoides group'}, {'2825': 'Clostridium coccoides group'}, {'2960': 'Clostridium coccoides group'}, {'2964': 'Clostridium coccoides group'}, {'3047': 'anaerobacter'}, {'3053': 'Clostridium coccoides group'}, {'3060': 'Clostridium cluster IV'}, {'3063': 'Clostridium cluster IV'}, {'3065': 'Clostridium cluster XIVa'}, {'3068': 'Clostridium cluster XIVa'}, {'3287': 'Clostridium cluster IV'}, {'3290': 'Clostridium cluster XVIII'}, {'3822': 'Clostridium cluster IV'}, {'3823': 'Clostridium cluster XIVa'}, {'3935': 'Clostridium cluster XIVa'}, {'3952': 'Clostridium cluster IV'}, {'4017': 'Clostridium cluster IV'}, {'4018': 'Clostridium cluster XIVa'}, {'4142': 'Clostridium cluster IV'}, {'4184': 'Clostridium cluster IV'}, {'4200': 'TM7'}, {'4215': 'Clostridium cluster IV'}, {'4216': 'Clostridium cluster XIVa'}, {'4347': 'Clostridium cluster XIVa'}, {'4702': 'TM7'}, {'4889': 'TM7'}, {'4890': 'SR1'}, {'5018': 'Clostridium cluster XIVa'}, {'5020': 'Clostridium cluster XIVa'}, {'5461': 'TM7'}, {'5496': 'Clostridium cluster XIVa'}, {'5499': 'Clostridium cluster IV'}, {'5593': 'Clostridium cluster XIVb'}, {'5597': 'Clostridium cluster IV'}, {'6109': 'Clostridium cluster XVIII'}, {'6220': 'TM7'}, {'6339': 'Clostridium cluster IV'}, {'6679': 'Candidatus'}, {'7427': 'SR1'}, {'7429': 'TM7'}, {'7451': 'Clostridium III'}, {'7461': 'Gp21'}, {'7462': 'Gp7'}, {'7677': 'Clostridium cluster IV'}, {'7683': 'Clostridium cluster XIVb'}, {'8014': 'Clostridium cluster XIVa'}, {'8020': 'Clostridium cluster IV'}, {'8289': 'Clostridium cluster XVIII'}, {'8363': 'Clostridium cluster IV'}, {'8557': 'Clostridium cluster IV'}, {'8647': 'TM7'}, {'8675': 'TM7'}, {'8861': 'Clostridium cluster XIVa'}, {'8990': 'Clostridium III'}, {'8994': 'Clostridium cluster XVIII'}, {'9051': 'TM7'}, {'9071': 'TM7'}, {'9269': 'TM7'}, {'9355': 'Clostridium cluster XIVa'}, {'9516': 'Clostridium cluster XIVa'}, {'9628': 'anaerobacter'}, {'9689': 'TM7'}, {'9959': 'Clostridium coccoides group'}, {'9960': 'Bacteroides fragilis group'}, {'10442': 'Clostridium cluster IV'}, {'10577': 'Clostridium cluster IV'}, {'10593': 'Clostridium cluster XVIII'}, {'10602': 'Clostridium cluster XVIII'}, {'11448': 'Absiella innocuum'}]
```

</details>

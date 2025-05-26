# Biomedical Translation Evaluation

This repository contains the resources, code, and data used to evaluate the quality of Turkish and Azerbaijani translations for biomedical texts, particularly focusing on domain-specific annotation consistency and linguistic accuracy.

## 📚 Project Description

This project explores the comparative translation quality of Turkish and Azerbaijani medical text data derived from the **BC5CDR** biomedical NER dataset. We manually annotated and graded translations to evaluate semantic accuracy and syntactic correctness.

## 📂 Contents

- **`bc5cdr.json`**: Original biomedical dataset with token-level annotations.
- **`translated_ds_tr.json`**: Turkish-translated version of the dataset.
- **`translated_ds_az.json`** *(not uploaded yet)*: Azerbaijani-translated version (referenced in the evaluation code).
- **`translation_eval.py`**: A Python script to manually grade the translations with a 0–4 scale:
  - `0`: Semantically wrong
  - `1`: Major syntactic errors
  - `2`: Minor syntactic errors
  - `3`: Correct translation
  - `4`: Not applicable
- **`translation_grades.csv`**: Resulting dataset containing translation grades for analysis.
- **`THESIS-1-1.pdf`**: Thesis draft or report describing the translation evaluation framework.

## 🚀 How to Run the Evaluation

1. Ensure the translated Azerbaijani and Turkish JSON files are placed in the same directory.
2. Run the script:
   ```bash
   python translation_eval.py
   ```

3. Grade 50 randomly selected samples interactively.
4. The graded samples will be saved to `translation_grades.csv`.




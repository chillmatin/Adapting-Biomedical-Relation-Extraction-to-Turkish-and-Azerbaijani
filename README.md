# Biomedical Translation Evaluation

This repository contains the resources, code, and data used to evaluate the quality of Turkish and Azerbaijani translations for biomedical texts, particularly focusing on domain-specific annotation consistency and linguistic accuracy.

## 📚 Project Description

This project explores the comparative translation quality of Turkish and Azerbaijani medical text data derived from the **BC5CDR** biomedical NER dataset. We manually annotated and graded translations to evaluate semantic accuracy and syntactic correctness.

## 📂 Contents

- **`bc5cdr.json`**: Original biomedical dataset with token-level annotations.
- **`translated_ds_tr.json`**: Turkish-translated version of the dataset.
- **`translated_ds_az.json`** Azerbaijani-translated version (referenced in the evaluation code).
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



## References

\[1] Holger Schwenk, Guillaume Wenzek, Sergey Edunov, Edouard Grave, and Armand Joulin. *CCMatrix: Mining Billions of High-Quality Parallel Sentences on the Web*. arXiv preprint arXiv:1911.04944, 2019.

\[2] NLLB Team, Marta R. Costa-jussà, James Cross, Onur Çelebi, Maha Elbayad, Kenneth Heafield, Kevin Heffernan, Elahe Kalbassi, Janice Lam, Daniel Licht, Jean Maillard, Anna Sun, Skyler Wang, Guillaume Wenzek, Al Youngblood, Bapi Akula, Loïc Barrault, Gabriel Mejia Gonzalez, Prangthip Hansanti, John Hoffman, Semarley Jarrett, Kaushik Ram Sadagopan, Dirk Rowe, Shannon Spruit, Chau Tran, Pierre Andrews, Necip Fazil Ayan, Shruti Bhosale, Angela Fan, and Francisco Guzmán. *No Language Left Behind: Scaling Human-Centered Machine Translation*. arXiv preprint arXiv:2207.04672, 2022.

\[3] Myle Ott, Sergey Edunov, Alexei Baevski, Angela Fan, Sam Gross, Nathan Ng, David Grangier, and Michael Auli. *fairseq: A Fast, Extensible Toolkit for Sequence Modeling*. arXiv preprint arXiv:1904.01038, 2019.

\[4] Rishabh Agarwal, Avi Singh, Lei M. Zhang, Bernd Bohnet, Stephanie C.Y. Chan, Ankesh Anand, Zaheer Abbas, Azade Nova, John D. Co-Reyes, Eric Chu, Feryal Behbahani, Aleksandra Faust, and Hugo Larochelle. *Many-Shot In-Context Learning*. arXiv preprint arXiv:2404.11018, 2024.

\[5] Jiao Li, Yueping Sun, Robert J. Johnson, Daniela Sciaky, Chih-Hsuan Wei, Robert Leaman, Allan Peter Davis, Carolyn J. Mattingly, Thomas C. Wiegers, and Zhiyong Lu. *BioCreative V CDR Task Corpus: A Resource for Chemical Disease Relation Extraction*. Database, 2016.

\[6] Duygu Altinok. *A Diverse Set of Freely Available Linguistic Resources for Turkish*. Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 13739–13750, 2023.

\[7] Turkish NLP Suite. *Vitamins and Supplements NER Dataset*. GitHub repository, 2023. Available at: [https://github.com/turkish-nlp-suite/Vitamins-Supplements-NER-dataset](https://github.com/turkish-nlp-suite/Vitamins-Supplements-NER-dataset)

\[8] Hugging Face. *Token Classification with Hugging Face Transformers*. 2023. Available at: [https://huggingface.co/docs/transformers/tasks/token\_classification](https://huggingface.co/docs/transformers/tasks/token_classification)

\[9] Dina Demner-Fushman, Sophia Ananiadou, Paul Thompson, and Brian Ondov (Eds.). *Proceedings of the First Workshop on Patient-Oriented Language Processing (CL4Health) @ LREC-COLING 2024*. ELRA and ICCL, Torino, Italy, 2024.


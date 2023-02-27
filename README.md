# Models-InProduction
 Integrating robust and reliable ML Pipelines in Production

**`CI/CD and automated ML Pipeline`**
![mlops_cicd](https://user-images.githubusercontent.com/26667491/221462555-4ff921ec-6f31-4bf8-a7d9-5ab62f7d3630.png)

<pre>
.
├── 01-research_env
│   ├── 0-Data_Analysis_v4.ipynb
│   ├── 1-Feature_Engineering_v2.ipynb
│   ├── 2-Feature_Selection_v2.ipynb
│   ├── 3-Model_Training.ipynb
│   ├── 4-Scoring(unseen_data).ipynb
│   ├── 5-Final_Pipeline.ipynb
│   └── pre_process.py
├── 02-production_env
│   ├── regression_model
│   │   ├── config
│   │   │   ├── __init__.py
│   │   │   └── core.py
│   │   ├── config.yml
│   │   ├── datasets
│   │   │   └── __init__.py
│   │   ├── pipeline.py
│   │   ├── predict.py
│   │   ├── preprocessing
│   │   │   ├── __init__.py
│   │   │   ├── data_manager.py
│   │   │   ├── features.py
│   │   │   └── validation.py
│   │   ├── train_pipeline.py
│   │   └── trained_models
│   │       └── __init__.py
│   ├── requirements
│   │   ├── requirements.txt
│   │   ├── test_requirements.txt
│   │   └── typing_requirements.txt
│   └── tests
│       └── __init__.py
└── README.md
</pre>

<p align="center">
  <kbd><img src="https://user-images.githubusercontent.com/26667491/221332315-4716d85d-6e4b-4493-a363-94302d376163.png" alt="ml_lifecycle.png"></kbd>
</p>


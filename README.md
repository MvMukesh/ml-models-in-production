# Models-InProduction
 Integrating robust and reliable ML Pipelines in Production

<hr> </hr>

# ML System Design

## `Offline Training Phase`
![offline](https://github.com/MvMukesh/Models-InProduction/assets/26667491/13ca6951-6ff2-45a2-af95-c9c16fcac9c4)

## `Application Structure` (Online-Prediction-Phase)
![prod](https://github.com/MvMukesh/Models-InProduction/assets/26667491/d57dbf3f-e75e-475e-a028-fd4015c82668)

## `Full System` (Online + Offline)
![full_system](https://github.com/MvMukesh/Models-InProduction/assets/26667491/632b544b-cacb-4fba-9274-dee847ffb54a)

![cicd](https://github.com/MvMukesh/Models-InProduction/assets/26667491/fe7fcea9-307a-47a5-afed-307d32f61010)

<hr> </hr>

## `Tree`
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

**`CI/CD and automated ML Pipeline`**
![mlops_cicd](https://user-images.githubusercontent.com/26667491/221462555-4ff921ec-6f31-4bf8-a7d9-5ab62f7d3630.png)


<p align="center">
  <kbd><img src="https://user-images.githubusercontent.com/26667491/221332315-4716d85d-6e4b-4493-a363-94302d376163.png" alt="ml_lifecycle.png"></kbd>
</p>

## Resources
* [Google Cloud Architecture Center](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
* [Google ML](https://developers.google.com/machine-learning)

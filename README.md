# Models-InProduction
 Integrating robust and reliable ML Pipelines in Production

<hr> </hr>

## `Directory Tree`
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

# ML System Design
## `Offline Training Phase`
<div style="border: 2px solid black; padding: 10px;"> 
 <p align="center">
   <kbd><img src="https://github.com/MvMukesh/Models-InProduction/assets/26667491/13ca6951-6ff2-45a2-af95-c9c16fcac9c4" alt="ml_lifecycle.png" width="550" height="300"></kbd>
 </p>
</div>

## `Application Structure` (Online-Prediction-Phase)
<div style="border: 2px solid black; padding: 10px;"> 
 <p align="center">
   <kbd><img src="https://github.com/MvMukesh/Models-InProduction/assets/26667491/d57dbf3f-e75e-475e-a028-fd4015c82668" alt="prod.png" width="550" height="300"></kbd>
 </p>
</div>

## `Full System` (Online + Offline)
<div style="border: 2px solid black; padding: 10px;"> 
 <p align="center">
   <kbd><img src="https://github.com/MvMukesh/Models-InProduction/assets/26667491/632b544b-cacb-4fba-9274-dee847ffb54a" alt="full_system.png" width="550" height="300"></kbd>
   <p> Automated required steps using CI/CD </p>
 </p>
</div>

<div style="border: 2px solid black; padding: 10px;"> 
 <p align="center">
    <kbd><img src="https://github.com/MvMukesh/Models-InProduction/assets/26667491/fe7fcea9-307a-47a5-afed-307d32f61010" alt="cicd.png" width="600" height="200"></kbd>
    <p> Step: 1 -  Automating || Training, Testing & Deployment </p>
    <kbd><img src="https://github.com/MvMukesh/Models-InProduction/assets/26667491/96fce2d5-e517-408e-95d6-07da83704283" alt="CICD-automation(train,test,deploy).png" width="650" height="350"></kbd>
    <p> Step: 2 -  Automating || Model building & Publishing </p>
    <kbd><img src="https://github.com/MvMukesh/Models-InProduction/assets/26667491/a0f00218-50c3-408a-8d13-cedb4313fcc0" alt="CICD-automation(model_building,publishing.png" width="650" height="350">
 </p>
</div>


<hr> </hr>

## `API Architecture`
<div style="border: 2px solid black; padding: 10px;"> 
 <p align="center">
   <kbd><img src="https://github.com/MvMukesh/Models-InProduction/assets/26667491/d10fe99c-5f7e-4735-ac4c-230a70758293" alt="api_architecture.png" width="650" height="400"></kbd>
 </p>
</div>


<hr> </hr>

## `Learning` | Python WebFrameworks
| Aspect                    | FastAPI                                           | Flask                                                | Django                                               |
|---------------------------|--------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| Performance               | High-performance with asynchronous capabilities | Lightweight with moderate performance                | Robust and scalable for large-scale applications    |
| Development Speed         | Rapid development with automatic documentation  | Quick prototyping and simple application structure  | Longer development time due to boilerplate and complexity |
| Scalability               | Highly scalable and efficient for high loads   | Suitable for small to medium-sized projects         | Robust and scalable for large-scale applications    |
| Learning Curve            | Moderate learning curve due to advanced features | Easy to learn and get started with                  | Steeper learning curve due to complex architecture   |
| Community Support         | Growing community with a range of resources and tutorials | Active community with numerous third-party packages | Large and mature community with extensive resources  |
| Extensions and Plugins    | Limited number of available extensions and plugins | Abundant ecosystem of third-party extensions        | Vast ecosystem of extensions and packages           |
| Documentation              | Well-documented with automatic API documentation | Comprehensive documentation and abundant learning resources | Extensive documentation and official tutorials      |
| Database Support          | Wide range of database support with integrated ORM | Supports multiple databases with the help of extensions | Powerful ORM with support for various databases      |
| Testing and Debugging     | Excellent testing support with built-in test client | Basic testing capabilities with various extensions  | Comprehensive testing framework and debugging tools |
| Community Adoption        | Gaining popularity with a growing user base     | Widely adopted and widely used in the Python community | Established and widely used in the Python community |
| Project Size Suitability | Suitable for small to large-scale projects      | Suitable for small to medium-sized projects          | Suitable for medium to large-scale projects         |
| Flexibility and Customization | Offers flexibility and customization options   | Highly flexible and customizable                    | Offers flexibility within its established conventions |
| Pros                      | - Exceptional performance with high throughput  | - Lightweight and easy to get started with         | - Robust and comprehensive framework with "batteries included"|
|                             | - Automatic API documentation generation         | - Flexible and customizable architecture             | - Built-in admin interface for easy management|
|                             | - Strong type safety and automatic data validation | - Extensive ecosystem of third-party extensions      | - Excellent security features and protection against common vulnerabilities
|                             | - Excellent support for asynchronous programming | - Well-suited for small to medium-sized projects     | - Ideal for large-scale and enterprise-level applications
|                             | - Easy integration with other Python libraries and frameworks | - Abundant learning resources and tutorials         | - Well-established and extensive community support
| Cons                      | - Relatively new framework with a smaller community compared to Flask and Django | - Limited out-of-the-box features compared to Django | - Longer development time due to the included features and conventions
|                             | - Limited number of available extensions and plugins | - Less suitable for large-scale applications with high traffic | - Requires manual configuration for complex functionality
|                             | - Steeper learning curve due to advanced features and concepts | - Requires manual configuration for complex functionality | - Complex architecture and extensive boilerplate code
|                             |                                                      | - Complex architecture and extensive boilerplate code | - Less flexibility compared to FastAPI and Flask

<hr> </hr>

**`CI/CD and automated ML Pipeline`**
<div style="border: 2px solid black; padding: 10px;"> 
 <p align="center">
   <kbd><img src="https://user-images.githubusercontent.com/26667491/221462555-4ff921ec-6f31-4bf8-a7d9-5ab62f7d3630.png" alt="mlops_cicd.png" width="800" height="450"></kbd>
   <kbd><img src="https://user-images.githubusercontent.com/26667491/221332315-4716d85d-6e4b-4493-a363-94302d376163.png" alt="ml_lifecycle.png" width="800" height="500"></kbd>
 </p>
</div>



## Resources
* [Google Cloud Architecture Center](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
* [Google ML](https://developers.google.com/machine-learning)

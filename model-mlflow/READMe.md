# Model Construction with ML-Flow

This section presenting on simple model training with Machine Learning Operation tools which is ML-Flow. The context is simple by using mlflow python package. The metric on trained model logged into mlflow dashboard so it's presenting easy to understand information if the machine learning development set on continous improvements.

## Testing the service
1. Train model : 
    ```
    python model.py 
    ```
    This will generate  ` mlruns ` folder that contain the model, experiments, and the environment config for testing.  
2. Serving the model for REST Client
    ```
    mlflow models serve --model-uri runs:/[model_uuid]/model 
    ```
3. Testing the model with curl to designated endpoint
    ```
    curl -d '{"data":[[0.09178,0.0,4.05,0.0,0.51,6.416,84.1,2.6463,5.0,296.0 16.6,395.5,9.04]]}' 
    -H 'Content-Type: application/json'  localhost:5000/invocations
    ```
    The result would be the looks like
    ```
    [28.994834741]
    ```
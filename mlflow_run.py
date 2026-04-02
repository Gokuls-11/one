import mlflow

mlflow.set_experiment("Gokul_MLflow_Test")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.92)

print("Experiment logged successfully!")
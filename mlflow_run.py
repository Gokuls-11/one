import mlflow
import random
import time

# Create / select experiment
mlflow.set_experiment("Gokul_MLflow_Test")

# Simulate multiple experiment runs
for run_number in range(3):

    with mlflow.start_run():

        # Example parameters
        learning_rate = round(random.uniform(0.001, 0.1), 3)
        epochs = random.randint(5, 20)

        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_param("epochs", epochs)

        # Simulated metrics
        accuracy = round(random.uniform(0.80, 0.95), 3)
        loss = round(random.uniform(0.05, 0.30), 3)

        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("loss", loss)

        # Simulate training time
        time.sleep(1)

        print(f"Run {run_number+1} logged successfully!")
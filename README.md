git credential-manager erase

protocol=https
host=github.com

git remote remove origin
git remote add origin https://github.com/Gokuls-11/one.git

git push -u origin main

Username → Gokuls-11
Password → your GitHub Personal Access Token (PAT)

python mlflow_run.py

mlflow ui --backend-store-uri file:./mlruns

import os
import subprocess
from google.colab import userdata

def commit(branch, message):
  try:
    token = userdata.get('token') #IMPORTANT! Remember to store the token in the "Secrets" in Colab with name "token" and for "Value" use ... [ask MauriVass]
    
    user = "LimitParadigm" #You can change with your credentials
    email = "LimitParadigm@gmail.com" #You can change with your credentials
    repo = "LimitParadigm/DOEs" #Do not change

    # Configure git user (if not already done)
    subprocess.run(["git", "config", "user.name", user], check=True)
    subprocess.run(["git", "config", "user.email", email], check=True)
    
    # Set remote URL
    subprocess.run(["git", "remote", "set-url", "origin", f"https://{user}:{token}@github.com/{repo}.git"], check=True)
    
    # Fetch and checkout
    subprocess.run(["git", "fetch"], check=True)
    subprocess.run(["git", "checkout", "-B", branch], check=True)
    
    # Check if there are changes to commit. Check result(?)
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    
    # Add, commit, and push
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", message], check=True)
    subprocess.run(["git", "push", "origin", branch], check=True)
    
    print(f"Successfully committed and pushed to {branch}")
      
  except subprocess.CalledProcessError as e:
      print(f"Git command failed: {e}")
  except Exception as e:
      print(f"Error: {e}")
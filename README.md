# Work in progress

This repository provides the implementation.

For more detailed information, refer to the paper [here](https://).

## Table of Contents
- [Introduction](#introduction)
- [Required Data](#requireddata)
- [Usage](#usage)

## Introduction
T

## Required Data
The required data for running the code is available in the `Data` folder. The data includes:

## Usage
### For Desktop
To run the methodology, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/LimitParadigm/DOEs.git
   cd DOEs

2. Install the required packages:
   ```bash
   pip install -r requirements.txt

3. Run main notebook script:
   ```bash
   python main.ipynb

### For Colab
To run the methodology, follow these steps:

1. Go to Google Colab
2. Open the `main.ipynb` notebook from GitHub (https://github.com/LimitParadigm/DOEs, main branch)
3. Now you should be able to run the notebook and modify other files
4. Add the token to Colab secrets (check CommitScript.py for more details)
5. If you want to commit, use the script `CommitScript.py` as follows:
   ```bash
   python CommitScript.py <branch> <message>
   (By default it will commit everything ("git commit .") so be careful, especially if there is something you don't want to commit)

***

For any questions or issues, please contact mvassallo@uliege.be.

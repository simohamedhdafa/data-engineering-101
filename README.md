# data-engineering-101
### 1. Description
This repo is a guide in learning by doing modern data engineering 

### 2. Getting started
#### 2.1 Prerequisites
1. Install python (v3.11.6)
2. Create virtual env
    -> Install : pip install virtualenv
    -> Create dedicated folder for your virtual env (separeted from this project)
    -> Create new folder : mkdir virtual-env
    -> Creae Virtual Env insid virtual-env : python -m venv space-env
    -> Activate Virtual Env from root folder : source virtual-env/space_env/bin/ activate
3. Install requirements.txt packages
    -> pip install -r requirements.txt

#### 2.2 Run IT
After setting up the ENV, we only need to execute this command from root folder (we can change part-1 with the part we're at)
-> python part-1/src/main.py

### 3. Walkthrough
#### 3.1 Overview
We have input and output folders represents our source and target systems
we have src folder where we have main.py represents our pipline entrypoint along with config and util folders

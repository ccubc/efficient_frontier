# Efficient Frontier
work in progress

### 0. after cloning the repo, make directories
	mkdir data
	mkdir results
	mkdir notebook

Note: data and results are not version controled

### 1. create virtual environment and install packages
	conda create -n <env_name> python=3.8
	conda active <env_name>	
	pip install -r requirements.txt
	conda install nb_conda_kernels

### 2. Configure fields in config/config.yaml

### 3. Download stock data, run code below
	python src/download_data.py

daoluan

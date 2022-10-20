.DEFAULT_GOAL := scrape

scrape: ## Scraper all users setted on settings
	python main.py

scrape_user: ## Scraper a single user passed as arg
	python main.py --username ${username}

setup: requirements.txt
	pip install -r requirements.txt


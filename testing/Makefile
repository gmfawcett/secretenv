export ENVKEY=4HRXH5HNfYNNKb7qZeicu9TCMFnxMQyNytENAzX2vHZcXE7jVpQ7ofVcNKJ9jUpCbvzskXaxtfJvrVigFQg3oxX2zUkgVrgHq4MknTHSe7XtoRweCvcx2RvytaLLDJ4t
export PYTHONPATH=..

test:
	python test.py

enc:
	python -m secretenv enc main.env local.env

dec:
	python -m secretenv dec main.env local.env

tidy: main.env.secret local.env.secret
	rm -f main.env local.env

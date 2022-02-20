ENVKEY=4HRXH5HNfYNNKb7qZeicu9TCMFnxMQyNytENAzX2vHZcXE7jVpQ7ofVcNKJ9jUpCbvzskXaxtfJvrVigFQg3oxX2zUkgVrgHq4MknTHSe7XtoRweCvcx2RvytaLLDJ4t
test:
	PYTHONPATH=.. python test.py

enc:
	PYTHONPATH=.. python -m secretenv enc main.env local.env

dec:
	PYTHONPATH=.. python -m secretenv dec main.env local.env

tidy: main.env.secret local.env.secret
	rm -f main.env local.env

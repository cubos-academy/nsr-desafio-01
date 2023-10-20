
run_telegram_bot_listener:
	python3 -m nsrdesafio01.src.main --run

clean:
	find . -name "*.pyc" -exec rm -f {} \;
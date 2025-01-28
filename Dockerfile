FROM python:slim
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "main.py", "&&", "python", "bot/bot.py" ]
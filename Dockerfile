FROM python

RUN apt install openssl libstdc++
RUN pip install --upgrade pip
RUN pip install requests
RUN pip install python-telegram-bot==12.0.0b1 --upgrade

ADD ./plexbot.py /

CMD python /plexbot.py

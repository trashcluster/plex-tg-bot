FROM python

RUN apt install openssl libstdc++
RUN pip install --upgrade pip
RUN pip install requests
RUN pip install python-telegram-bot==12.0.0b1 --upgrade

ADD ./plexbot.py /

ENV TELEGRAM_TOKEN
ENV PLEX_USERNAME
ENV PLEX_PASSWORD
ENV PLEX_SERVERNAME

CMD python /plexbot.py

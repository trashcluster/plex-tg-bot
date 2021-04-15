FROM python

RUN apt install openssl libstdc++
RUN pip install --upgrade pip
RUN pip install requests
RUN pip install python-telegram-bot==12.0.0b1 --upgrade

ADD ./plexbot.py /

ENV PLEX_SERVER changeme
ENV PLEX_UASER changeme
ENV PLEX_PASSWORD changeme
ENV TELEGRAM_TOKEN changeme

CMD python /plexbot.py

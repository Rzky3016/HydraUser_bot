# Feri Ganteng
FROM biansepang/weebproject:buster
#
# Feri
#
RUN git clone -b Linux-Userbot https://github.com/PashaDIE/HydraUser_bot/root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/PashaDIE/HydraUser_bot/HydraUser_bot/requirements.txt

CMD ["python3","-m","userbot"]

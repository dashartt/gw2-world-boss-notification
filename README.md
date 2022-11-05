# Guild Wars 2 - World Boss Notification

## Propósito
Jogo [Guild Wars 2](https://www.guildwars2.com/en/), um MMORPG incrível! E o jogo possui um [Wiki](https://wiki.guildwars2.com/wiki/Main_Page) muito rico em informações no qual há uma sessão para visualizar a agenda de [World Boss](https://wiki.guildwars2.com/wiki/World_boss) onde a cada 15 minutos haverá um Boss para ser feito. <br>
Porém, é meio chato ficar olhando que horas são e qual Boss ira nascer no Wiki, dessa forma, sugiu a ideia de criar um Bot no Discord para alertar sobre os World Boss. <br>
Avisa com antecedência de 10 minutos algum World Boss próximo após usar o :star: Gw2 World Boss Notification :star:

## Por que Discord?
É bem comum jogadores usarem o [Discord](https://discord.com/) para criarem comunidades e se comunicar durante a gameplay, nesse sentido, gostei da ideia de direcionar ao Discord a forma de alertar o jogador. Pensei também em alertar via SMS, WhatsApp, mas, Discord enquadra mais pra quem joga :sunglasses:

## O que foi usado?
- [Python](https://www.python.org/) - Melhor linguagem ever para programar :rocket:
- [Discordpy](https://discordpy.readthedocs.io/en/stable/) - Criar Bot para Discord
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Raspar dados do Wiki do jogo
- [Schedule](https://schedule.readthedocs.io/en/stable/) - Criar task que se repete por hora e/ou data
- [Datetime](https://docs.python.org/3/library/datetime.html) - Manipular data e hora

## Como executar o código
1. Primeiro é necessário criar um Bot no Discord e colocá-lo em seu Servidor - [Referência](https://discord.com/developers/docs/getting-started)
2. Clone o projeto e instale as dependencias:
```
git clone git@github.com:jonatasqueirozlima/gw2-world-boss-notification.git
cd gw2-world-boss-notification
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Pegar o [Bot Token](https://discord.com/developers/applications) e na raiz do projeto criar um .env da seguinte forma:
```
BOT_TOKEN=<SEU_TOKEN>
```
3. Em seguida, executar:
```
python3 main.py
```

## Como usar:
No Bot do Discord:
- $start: será notificado sobre os World Boss
- $stop: não te notificará mais sobre os World Boss

## Futuros ajustes
Supomos que seja 13h51 e inicia os alertas com: $start, o próximo World Boss é 14h00, não avisará ao jogador pois o Bot avisa faltando 10 minutos e no exemplo faltam 9 minutos.<br>
Isso ocorre apenas no início uma vez ao exececutar: $start.

## Futuros updates:
- Melhorar README.md
- Implementar testes unitários
- Refatorar código
- Usar docker para dockerizar o app

## Contribuições
Quer contribuir? Sinta-se a vontade compartilhando suas ideias e ajudando no projeto :wink:

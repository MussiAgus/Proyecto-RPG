from app.entidades.berserker import Berserker
from app.entidades.mago import Mago
from app.engine.batalla import Batalla

yo = Mago("Sbender")
enemigo = Berserker("TheBoss")

round = Batalla(yo, enemigo)
round.comienzo()
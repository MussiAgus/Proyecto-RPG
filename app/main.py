from .entidades.berserker import Berserker
from .entidades.mago import Mago
from .engine.batalla import Batalla

yo = Mago("Sbender")
enemigo = Berserker("TheBoss")

yo.subir_nivel(5)

round = Batalla(yo, enemigo)
round.comienzo()
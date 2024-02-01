from datetime import date

from models.political_party import PoliticalParty
from models.candidate import Candidate
from models.candidate_position import CandidatePosition

representative1 = Candidate(
    birthdate=date(1990, 1, 1),
    ci="1234567",
    gender="M",
    name="Naranjito Manzana",
    photo="",
    position=CandidatePosition(name="Presidente"),
)

representative2 = Candidate(
    birthdate=date(1990, 1, 1),
    gender="F",
    ci="1234567",
    name="Laura Gómez",
    photo="",
    position=CandidatePosition(name="Presidente"),
)

representative3 = Candidate(
    birthdate=date(1990, 1, 1),
    ci="1234567",
    gender="M",
    name="Miguel Rodríguez",
    photo="",
    position=CandidatePosition(name="Presidente"),
)

representative4 = Candidate(
    birthdate=date(1990, 1, 1),
    ci="1234567",
    gender="F",
    name="María Fernández",
    photo="",
    position=CandidatePosition(name="Presidente"),
)

political_parties = [
    PoliticalParty(
        name="Movimiento Naranja",
        acronym="24mn",
        logo="https://picsum.photos/100/200",
        description="Un frente apoyado en el apoyo ciudadano comprometidos con el Naranja",
        representative=representative1,
    ),
    PoliticalParty(
        name="Unión Ciudadana",
        acronym="45ab",
        logo="https://picsum.photos/300/400",
        description="Un frente comprometido con el progreso y la igualdad para todos los ciudadanos.",
        representative=representative2,
    ),
    PoliticalParty(
        name="Renovación Democrática",
        acronym="32gh",
        logo="https://picsum.photos/500/600",
        description="Trabajamos por una democracia renovada, justa y transparente en beneficio de la sociedad.",
        representative=representative3,
    ),
    PoliticalParty(
        name="Fuerza Popular",
        acronym="78uv",
        logo="https://picsum.photos/700/800",
        description="Somos la fuerza que impulsa el desarrollo y la seguridad para el bienestar de todos.",
        representative=representative4,
    ),
]

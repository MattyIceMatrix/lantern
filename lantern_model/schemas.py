"""Mission data model.

          Scout ----> Sighting ----+
                                   |
          Field Brain -> Sitrep ---+--> Sector --> Mission
                                   |
          Agents ----> Assignment -+

STARTER FILE (Op 0 / Op 3). The shapes are sketched; the validation rules are TODOs.
Make the tests in tests/test_schemas.py pass, then remove their xfail markers.
"""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class SearchState(str, Enum):
    NOT_SEARCHED = "not_searched"
    IN_PROGRESS = "in_progress"
    CLEARED = "cleared"
    DENIED = "denied"  # Guardian refused entry (e.g. water too deep)


class FloodScenario(str, Enum):
    HQ10 = "HQ10"
    HQ100 = "HQ100"
    HQEXTREM = "HQextrem"


class Priority(str, Enum):
    IMMEDIATE = "immediate"
    URGENT = "urgent"
    ROUTINE = "routine"


class HazardZone(BaseModel):
    scenario: FloodScenario
    polygon: dict  # GeoJSON Polygon in EPSG:4326
    # TODO (Op 1): validate that polygon is a GeoJSON Polygon with a closed ring


class Sector(BaseModel):
    sector_id: str  # e.g. "D-4"
    boundary: dict  # GeoJSON Polygon in EPSG:4326
    assigned_team: str | None = None
    state: SearchState = SearchState.NOT_SEARCHED
    # TODO (Op 1): sector_id must match the pattern LETTER-NUMBER, e.g. "D-4"


class Sighting(BaseModel):
    sighting_id: str
    sector_id: str
    lat: float
    lon: float
    confidence: float = Field(ge=0.0, le=1.0)
    seen_at: datetime
    confirmed_by_human: bool = False
    # TODO (Op 2): lat must be in [-90, 90] and lon in [-180, 180]


class Sitrep(BaseModel):
    sitrep_id: str
    sector_id: str
    people_count: int
    injured_count: int = 0
    needs: list[str] = []
    priority: Priority
    source_note_id: str  # every SITREP points back to the note it came from (REQ-006)
    created_at: datetime
    # TODO (Op 3): injured_count can never be greater than people_count
    # TODO (Op 3): people_count and injured_count can never be negative


def can_mark_cleared(sector: Sector, human_confirmed: bool) -> bool:
    """A sector may only become CLEARED when a person confirms it (safety case H-01).

    TODO (Op 1): implement. Return True only if the sector is IN_PROGRESS
    and a human has confirmed the search.
    """
    raise NotImplementedError

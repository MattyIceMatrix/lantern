"""Mission model tests.

  These start as expected failures (xfail). Your job: make each one pass,
  then delete its xfail marker so it guards the code forever.

      [ xfail ] --(you write the rule)--> [ PASS ] --(remove marker)--> [ guarded ]
"""

from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from lantern_model.schemas import (
    Priority,
    SearchState,
    Sector,
    Sighting,
    Sitrep,
    can_mark_cleared,
)

SQUARE = {
    "type": "Polygon",
    "coordinates": [[[7.0, 50.5], [7.01, 50.5], [7.01, 50.51], [7.0, 50.51], [7.0, 50.5]]],
}
NOW = datetime(2026, 1, 1, tzinfo=timezone.utc)


def test_sector_defaults_to_not_searched():
    sector = Sector(sector_id="D-4", boundary=SQUARE)
    assert sector.state is SearchState.NOT_SEARCHED


def test_confidence_must_be_between_0_and_1():
    with pytest.raises(ValidationError):
        Sighting(sighting_id="s1", sector_id="D-4", lat=50.5, lon=7.0, confidence=1.5, seen_at=NOW)


@pytest.mark.xfail(reason="Op 1: sector_id pattern not implemented yet", strict=True)
def test_sector_id_pattern():
    with pytest.raises(ValidationError):
        Sector(sector_id="sector four", boundary=SQUARE)


@pytest.mark.xfail(reason="Op 2: lat/lon range not implemented yet", strict=True)
def test_latitude_range():
    with pytest.raises(ValidationError):
        Sighting(sighting_id="s1", sector_id="D-4", lat=95.0, lon=7.0, confidence=0.9, seen_at=NOW)


@pytest.mark.xfail(reason="Op 3: injured <= people rule not implemented yet", strict=True)
def test_injured_cannot_exceed_people():
    with pytest.raises(ValidationError):
        Sitrep(
            sitrep_id="r1",
            sector_id="D-4",
            people_count=1,
            injured_count=2,
            priority=Priority.IMMEDIATE,
            source_note_id="n1",
            created_at=NOW,
        )


@pytest.mark.xfail(reason="Op 1: can_mark_cleared not implemented yet", strict=True)
def test_sector_needs_human_to_clear():
    sector = Sector(sector_id="D-4", boundary=SQUARE, state=SearchState.IN_PROGRESS)
    assert can_mark_cleared(sector, human_confirmed=False) is False
    assert can_mark_cleared(sector, human_confirmed=True) is True

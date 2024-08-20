from unittest.mock import AsyncMock, MagicMock

from pytest import fixture

import yellowbox_kind.kind_cluster as kind_cluster_mod


@fixture(autouse=True)
def squib_subprocess(monkeypatch):
    monkeypatch.setattr(
        kind_cluster_mod, "subprocess", MagicMock(side_effect=AssertionError("subprocess should not be called"))
    )
    monkeypatch.setattr(
        kind_cluster_mod.asyncio_subprocess,
        "create_subprocess_exec",
        AsyncMock(side_effect=AssertionError("subprocess should not be called")),
    )

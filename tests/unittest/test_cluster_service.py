from yellowbox_kind.kind_cluster import KindClusterService


def test_close_without_start(tmp_path_factory):
    cluster_service = KindClusterService(tmp_path_factory)
    cluster_service.stop()
    assert cluster_service.cluster_name is None


async def test_aclose_without_start(tmp_path_factory):
    cluster_service = KindClusterService(tmp_path_factory)
    await cluster_service.astop()
    assert cluster_service.cluster_name is None

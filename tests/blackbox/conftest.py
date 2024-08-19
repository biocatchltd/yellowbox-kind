from pytest import fixture

from yellowbox_kind.kind_cluster import KindClusterService


@fixture(scope="session")
def kind(tmp_path_factory):
    with KindClusterService.run(tmp_path_factory) as cluster:
        yield cluster

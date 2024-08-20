from yellowbox_kind.kind_cluster import KindClusterService


def test_non_inferance(tmp_path_factory):
    cluster_service = KindClusterService(tmp_path_factory, cluster_name="set_cluster_name")
    cluster_service._infer_cluster_config()
    assert cluster_service.cluster_name == "set_cluster_name"
    assert cluster_service.config_path.match(
        str(tmp_path_factory.getbasetemp()) + "/yellowbox-*/kubeconfig-set_cluster_name.yaml"
    )

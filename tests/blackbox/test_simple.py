from time import sleep

from kubernetes.client import AppsV1Api, CoreV1Api

from tests.blackbox.util import fake_deployment
from yellowbox_kind.kind_cluster import KindClusterService


def test_run(tmp_path_factory):
    with KindClusterService.run(tmp_path_factory) as cluster, cluster.kube_client() as client:
        apps_api = AppsV1Api(client)
        core_api = CoreV1Api(client)
        with cluster.namespace("test") as ns:
            apps_api.create_namespaced_deployment(
                ns,
                fake_deployment(),
            )

            # assert deployment is running
            assert apps_api.read_namespaced_deployment("my-http-echo", ns) is not None
        sleep(20)  # wait for namespace to terminate
        assert core_api.list_namespace(field_selector=f"metadata.name={ns}").items == []


async def test_arun(tmp_path_factory):
    async with KindClusterService.arun(tmp_path_factory) as cluster:
        with cluster.kube_client() as client:
            apps_api = AppsV1Api(client)
            core_api = CoreV1Api(client)
            with cluster.namespace("test") as ns:
                apps_api.create_namespaced_deployment(
                    ns,
                    fake_deployment(),
                )

                # assert deployment is running
                assert apps_api.read_namespaced_deployment("my-http-echo", ns) is not None
            sleep(20)  # wait for namespace to terminate
            assert core_api.list_namespace(field_selector=f"metadata.name={ns}").items == []

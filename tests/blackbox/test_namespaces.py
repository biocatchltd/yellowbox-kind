from kubernetes.client import AppsV1Api
from pytest import raises

from tests.blackbox.util import fake_deployment


def test_anonymous_namespaces(kind):
    with kind.anonymous_namespace() as ns, kind.kube_client() as client:
        apps_api = AppsV1Api(client)
        apps_api.create_namespaced_deployment(
            ns,
            fake_deployment(),
        )


def test_namespace_conflict(kind):
    with kind.anonymous_namespace() as ns, kind.kube_client() as client:
        apps_api = AppsV1Api(client)
        apps_api.create_namespaced_deployment(
            ns,
            fake_deployment(),
        )

        with raises(ValueError), kind.namespace(ns):
            pass


def test_namespace_conflict_ok(kind):
    with kind.anonymous_namespace() as ns, kind.kube_client() as client:
        apps_api = AppsV1Api(client)
        apps_api.create_namespaced_deployment(
            ns,
            fake_deployment(),
        )

        with kind.namespace(ns, exists_ok=True):
            pass

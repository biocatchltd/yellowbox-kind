from kubernetes.client import (
    V1Container,
    V1ContainerPort,
    V1Deployment,
    V1DeploymentSpec,
    V1HTTPGetAction,
    V1LabelSelector,
    V1ObjectMeta,
    V1PodSpec,
    V1PodTemplateSpec,
    V1Probe,
)


def fake_deployment():
    return V1Deployment(
        metadata=V1ObjectMeta(
            name="my-http-echo",
        ),
        spec=V1DeploymentSpec(
            replicas=1,
            selector=V1LabelSelector(match_labels={"app": "my-http-echo"}),
            template=V1PodTemplateSpec(
                metadata=V1ObjectMeta(labels={"app": "my-http-echo"}),
                spec=V1PodSpec(
                    containers=[
                        V1Container(
                            name="http-echo",
                            image="hashicorp/http-echo:1.0",
                            args=["-listen", ":8080"],
                            image_pull_policy="IfNotPresent",
                            ports=[V1ContainerPort(container_port=8080, name="http", protocol="TCP")],
                            startup_probe=V1Probe(
                                failure_threshold=10,
                                http_get=V1HTTPGetAction(path="/health", port="http", scheme="HTTP"),
                                initial_delay_seconds=1,
                                period_seconds=1,
                                success_threshold=1,
                                timeout_seconds=1,
                            ),
                        ),
                    ]
                ),
            ),
        ),
    )

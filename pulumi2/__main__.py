import pulumi
import pulumi_kubernetes as kubernetes

#kubernetes.config.namespace = "devops-challenge-2"

# First Deployment
deployment1 = kubernetes.apps.v1.Deployment("jobs",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels={
            "app": "jobs",
        },
    ),
    spec=kubernetes.apps.v1.DeploymentSpecArgs(
        replicas=1,
        selector=kubernetes.meta.v1.LabelSelectorArgs(
            match_labels={
                "app": "jobs",
            },
        ),
        template=kubernetes.core.v1.PodTemplateSpecArgs(
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "app": "jobs",
                },
            ),
            spec=kubernetes.core.v1.PodSpecArgs(
                containers=[kubernetes.core.v1.ContainerArgs(
                    image="amith0504/devops-challenge:25",
                    name="jobs",
                    ports=[kubernetes.core.v1.ContainerPortArgs(
                        container_port=5001,
                    )],
                )],
            ),
        ),
    ))

# Second Deployment
deployment2 = kubernetes.apps.v1.Deployment("api",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels={
            "app": "api",
        },
    ),
    spec=kubernetes.apps.v1.DeploymentSpecArgs(
        replicas=1,
        selector=kubernetes.meta.v1.LabelSelectorArgs(
            match_labels={
                "app": "api",
            },
        ),
        template=kubernetes.core.v1.PodTemplateSpecArgs(
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "app": "api",
                },
            ),
            spec=kubernetes.core.v1.PodSpecArgs(
                containers=[kubernetes.core.v1.ContainerArgs(
                    image="amith0504/api:8",
                    name="api",
                    ports=[kubernetes.core.v1.ContainerPortArgs(
                        container_port=5000,
                    )],
                )],
            ),
        ),
    ))

devops_challenge_service = kubernetes.core.v1.Service("devops-challenge-service",
    spec=kubernetes.core.v1.ServiceSpecArgs(
        selector={
            "app": "jobs",
        },
        type="ClusterIP",
        ports=[
            kubernetes.core.v1.ServicePortArgs(
                port=5001,
                target_port=5001,
            ),
        ]
    )
)

# Create a service for the amith0504/api:4 pod
api_service = kubernetes.core.v1.Service("api-service",
    spec=kubernetes.core.v1.ServiceSpecArgs(
        selector={
            "app": "api",
        },
        type="ClusterIP",
         ports=[
            kubernetes.core.v1.ServicePortArgs(
                port=5000,
                target_port=5002,
            ),
        ]
    )
)


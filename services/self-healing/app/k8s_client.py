from kubernetes import client, config
from kubernetes.client.rest import ApiException

from datetime import datetime, timezone


# ======================================================
# LOAD KUBERNETES CONFIG
# ======================================================

def load_k8s():

    try:

        config.load_incluster_config()

        print(
            "✅ Using in-cluster config",
            flush=True
        )

    except Exception:

        config.load_kube_config()

        print(
            "✅ Using local kubeconfig",
            flush=True
        )


# ======================================================
# GET ROLLOUT API
# ======================================================

def get_rollout_api():

    load_k8s()

    return client.CustomObjectsApi()


# ======================================================
# GET CURRENT REPLICAS
# ======================================================

def get_current_replicas(
    namespace,
    rollout_name
):

    try:

        api = get_rollout_api()

        rollout = api.get_namespaced_custom_object(

            group="argoproj.io",

            version="v1alpha1",

            namespace=namespace,

            plural="rollouts",

            name=rollout_name
        )

        replicas = rollout["spec"].get(
            "replicas",
            1
        )

        print(
            f"📦 Current replicas: {replicas}",
            flush=True
        )

        return replicas

    except ApiException as e:

        print(
            f"❌ Failed to fetch replicas: {e}",
            flush=True
        )

        return 1


# ======================================================
# SCALE ROLLOUT
# ======================================================

def scale_rollout(
    namespace,
    rollout_name,
    replicas
):

    replicas = max(1, replicas)

    replicas = min(10, replicas)

    body = {
        "spec": {
            "replicas": replicas
        }
    }

    try:

        api = get_rollout_api()

        api.patch_namespaced_custom_object(

            group="argoproj.io",

            version="v1alpha1",

            namespace=namespace,

            plural="rollouts",

            name=rollout_name,

            body=body
        )

        print(
            f"📈 Rollout scaled to {replicas}",
            flush=True
        )

    except ApiException as e:

        print(
            f"❌ Rollout scaling failed: {e}",
            flush=True
        )


# ======================================================
# RESTART ROLLOUT
# ======================================================

def restart_rollout(
    namespace,
    rollout_name
):

    restart_time = datetime.now(
        timezone.utc
    ).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )

    body = {
        "spec": {
            "restartAt": restart_time
        }
    }

    try:

        api = get_rollout_api()

        api.patch_namespaced_custom_object(

            group="argoproj.io",

            version="v1alpha1",

            namespace=namespace,

            plural="rollouts",

            name=rollout_name,

            body=body
        )

        print(
            f"🔄 Rollout restart triggered: "
            f"{rollout_name}",
            flush=True
        )

    except ApiException as e:

        print(
            f"❌ Rollout restart failed: {e}",
            flush=True
        )

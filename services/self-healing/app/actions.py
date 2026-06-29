from k8s_client import (
    get_current_replicas,
    restart_rollout,
    scale_rollout
)

from metrics import (
    scaling_actions_total,
    restart_actions_total
)


# ======================================================
# SCALE ROLLOUT
# ======================================================

def scale(
    name,
    namespace,
    replicas
):

    try:

        # ==================================================
        # SAFETY LIMITS
        # ==================================================

        replicas = max(1, replicas)

        replicas = min(10, replicas)

        # ==================================================
        # CURRENT STATE
        # ==================================================

        current = get_current_replicas(
            namespace,
            name
        )

        print(
            f"📊 Current replicas: {current}",
            flush=True
        )

        print(
            f"🎯 Target replicas: {replicas}",
            flush=True
        )

        # ==================================================
        # AVOID NO-OP SCALE
        # ==================================================

        if current == replicas:

            print(
                "⚠️ Scaling skipped "
                "(already desired state)",
                flush=True
            )

            return

        # ==================================================
        # SCALE ROLLOUT
        # ==================================================

        print(
            f"⚡ Scaling rollout "
            f"{name}: {current} → {replicas}",
            flush=True
        )

        scale_rollout(
            namespace,
            name,
            replicas
        )

        scaling_actions_total.inc()

        print(
            f"✅ Rollout scaled successfully",
            flush=True
        )

    except Exception as e:

        print(
            f"❌ Scaling failed: {e}",
            flush=True
        )


# ======================================================
# RESTART ROLLOUT
# ======================================================

def restart(
    name,
    namespace
):

    try:

        print(
            f"🔄 Restarting rollout: {name}",
            flush=True
        )

        restart_rollout(
            namespace,
            name
        )

        restart_actions_total.inc()

        print(
            f"✅ Rollout restart triggered: {name}",
            flush=True
        )

    except Exception as e:

        print(
            f"❌ Restart failed: {e}",
            flush=True
        )

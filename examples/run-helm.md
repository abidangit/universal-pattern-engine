# Run with Helm (example)

1. Ensure image is published to GHCR or registry and update values.yaml image.repository and tag.
2. Install/upgrade with Helm:

   helm upgrade --install upe k8s/helm/universal-pattern-engine -n upe --create-namespace \
     --set image.repository=ghcr.io/OWNER/universal-pattern-engine --set image.tag=latest

3. Verify pods:

   kubectl get pods -n upe

4. To rollback:

   helm rollback upe <REVISION>

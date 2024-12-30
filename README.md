# TODO
1. Automatic K8S Deployment
2. Authenticate to private registry automatically
3. Load Deploy secrets during build step and apply to cluster

# IMPORTANT TODO
*Move Turso client initialization/binding to shared worker context.*
It's currently created in the  app.before_server_start hook and added to `app.ctx`
This ***may*** be the culprit of slow startup time (`WorkerManager.THRESHOLD = 600`) if each worker process (10 per pod on current testing env) has to initialize a connection to Turso


Testing out https://sanic.dev/.


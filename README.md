# TODO
1. Automatic K8S Deployment
2. Authenticate to private registry automatically
3. Load Deploy secrets during build step and apply to cluster

# IMPORTANT TODO
*Move Turso client initialization/binding to shared worker context.*
It's currently created in the  app.before_server_start hook and added to `app.ctx`
This ***may*** be the culprit of slow startup time (`WorkerManager.THRESHOLD = 600`) if each worker process (10 per pod on current testing env) has to initialize a connection to Turso

# Images
Docker images are automatically built for [amd64](https://git.victorbrink.dev/Victor/-/packages/container/sanic-server/latest) and [aarch64](https://git.victorbrink.dev/Victor/-/packages/container/sanic-arm/latest)

Get started with x86
`docker pull git.victorbrink.dev/victor/sanic-server:latest`

Get started with arm
`docker pull git.victorbrink.dev/victor/sanic-arm:latest`

# Run
Install uv (`pip install uv`)

```
uv venv # Create virtual environment
uv run pip install .  # Install project dependencies
```
Running the app can be done with most of your favourite ASGI or WSGI web servers. I am using Sanic's built in server to utilise their [Worker Manager](https://sanic.dev/en/guide/running/manager.html)

Development server
```
uv run sanic server --dev --reload
```
To run in production remove `--dev`, configure workers and run with `--no-access-log` to prevent Sanic from writing an access log.
The Python API is slower than other logging options, you can reverse proxy through nginx for access logs and [tune nginx for sanic](https://sanic.dev/en/guide/deployment/nginx.html)

This will start a Sanic HTTP server with one worker. Sanic provides an integrated REPL shell in dev mode, just press enter in the terminal.

Sanic is built for speed and creates multiple seperate proceses as workers. [Configuration Guide]()
The easiest way to automatically use the highest worker count, is by using the `--fast` flag after `sanic server` you can combine it with `--dev`


Testing out https://sanic.dev/.


#!/usr/bin/env bash

uvicorn --host "0.0.0.0" --port 80 iso.asgi:app

#!/bin/bash

gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 main:APP

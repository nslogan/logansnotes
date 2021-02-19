# Makefile preamble
MAKEFLAGS += --warn-undefined-variables
SHELL := bash
# .SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:

# ------------------------------------------------------------------------------

project_name     := logansnotes-zola

docker_image     := "balthek/zola:0.13.0"
server_cont_name := "${project_name}-server"

http_port   := 8080
reload_port := 1024

serve_flags := --drafts

USER := $(shell id -u)
GROUP := $(shell id -g)

.PHONY: all
all: xxx


.PHONY: init
init:
	docker run -it --rm -u "${USER}:${GROUP}" -v ${PWD}:/app --workdir /app ${docker_image} init

.PHONY: build
build:
	docker run -u "${USER}:${GROUP}" -v ${PWD}:/app --workdir /app ${docker_image} build

.PHONY: serve
serve:
	docker run -d --rm -u "${USER}:${GROUP}" -v ${PWD}:/app --workdir /app -p ${http_port}:${http_port} -p ${reload_port}:${reload_port} --name ${server_cont_name} ${docker_image} serve --interface 0.0.0.0 --port ${http_port} --base-url localhost ${serve_flags}

.PHONY: stop-serve
stop-serve:
	docker stop ${server_cont_name}

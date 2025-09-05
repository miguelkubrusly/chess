PYTHON ?= python

.PHONY: gen-client clean-client

gen-client:
	$(PYTHON) tools/openapi/generate.py

clean-client:
	rm -rf .openapi_client_build third_party/lichess_org_api_reference_client
	@echo "Cleaned generated client."


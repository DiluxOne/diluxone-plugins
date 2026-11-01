# `make pre-pr` is the one check before a pull request (DiluxOne/.github#479,
# scripts/pre-pr.py): every check this repository's pull request and its
# merge queue run, one after the other, stopping at the first failure. The
# repository has no kind (repos.yml), so it gets no dx.mk: the target is
# written here, in the form dx.mk takes. DX_CENTRAL is the organisation's
# checkout (`dx check` sets it; the autopilot's is .dx-central, the default).
.PHONY: pre-pr
define PRE_PR
central=$${DX_CENTRAL:-.dx-central}
test -f "$$central/scripts/agent-manifests.py" || { echo "pre-pr: DX_CENTRAL ($$central) is not a checkout of DiluxOne/.github" >&2; exit 1; }
python3 "$$central/scripts/agent-manifests.py" catalog .
python3 -I -m unittest discover -s tests
endef
export PRE_PR
pre-pr:
	@bash -euo pipefail -c "$$PRE_PR"

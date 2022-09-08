# https://www.gnu.org/software/make/manual/make.html
.PHONY: all
all:

########################################################################
# boiler plate
########################################################################
SHELL=bash
.SHELLFLAGS=-ec -o pipefail

current_makefile:=$(lastword $(MAKEFILE_LIST))
current_makefile_dirname:=$(dir $(current_makefile))
current_makefile_dirname_abspath:=$(dir $(abspath $(current_makefile)))
current_makefile_dirname_realpath:=$(dir $(realpath $(current_makefile)))

ifneq ($(filter all vars,$(VERBOSE)),)
dump_var=$(info var $(1)=$($(1)))
dump_vars=$(foreach var,$(1),$(call dump_var,$(var)))
else
dump_var=
dump_vars=
endif

ifneq ($(filter all targets,$(VERBOSE)),)
__ORIGINAL_SHELL:=$(SHELL)
SHELL=$(warning Building $@$(if $<, (from $<))$(if $?, ($? newer)))$(TIME) $(__ORIGINAL_SHELL)
endif

########################################################################
# variables
########################################################################

localstatedir?=var
generated_dir?=$(localstatedir)/generated

########################################################################
# targets
########################################################################

validate:
	buf lint
	buf format --diff

validate-fix:
	buf format --write

$(generated_dir)/main.dsc: | $(generated_dir)/
	buf build --as-file-descriptor-set -o $(@) -vv --debug

publish: $(generated_dir)/main.dsc
	find proto/ -name '*.proto' -type f -print0 \
		| DATAHUB_ENV=EI xargs -0 -t -I{} \
		jbang run --catalog=jbang-catalog.json datahub-protobuf var/generated/main.dsc {}


.PHONY: clean
clean:


########################################################################
# utility targets
########################################################################

.PHONY: help
help: ## Show this message.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(current_makefile) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: .FORCE
.FORCE:
$(force_targets): .FORCE

## Create directories
.PRECIOUS: %/
%/:
	mkdir -vp $(@)

## Clean directories
.PHONY: clean-%/
clean-%/:
	@{ test -d $(*) && { set -x; rm -vr $(*); set +x; } } || echo "directory $(*) does not exist ... nothing to clean"

TopLevelDir="$(dirname "$(readlink -f "$BASH_SOURCE[0]")")"
export PYTHONPATH="${TopLevelDir}${PYTHONPATH+:$PYTHONPATH}"

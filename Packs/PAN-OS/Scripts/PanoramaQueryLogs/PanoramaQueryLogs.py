import demistomock as demisto
from CommonServerPython import *
from CommonServerUserPython import *

def main():
    try:
        return_results(execute_polling_command("pan-os-query-logs", demisto.args()))
    except Exception as ex:
        return_error(f"Failed to execute PanoramaQueryLogs. Error: {str(ex)}")

if __name__ in ("__main__", "__builtin__", "builtins"):  # pragma: no cover
    main()

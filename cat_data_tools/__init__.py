"""A Python module to process cats data"""

from importlib.metadata import version as metadata_version

__version__ = metadata_version("cat-data-tools")

from .cli import (  # noqa
    filter_monthly_summary,
    join_traps_ids_and_daily_status,
    join_traps_positions_and_active_traps_by_id_and_line,
    update_status_traps,
    version,
    write_daily_effort_and_captures_summary_by_zone,
    write_effort_captures_as_json,
    write_effort_captures_from_traps_and_cameras_to_json_stan,
    write_filtered_data_between_dates,
    write_filtered_monthly_summary_between_years,
    write_monthly_summary_without_trappers,
    write_monthly_summary,
    write_posterior_samples_summary,
    write_trap_check_log,
    write_trap_daily_status,
)
from .summary_posterior_results import compute_posterior_summary_for_cameras_and_traps
from .transform_effort_captures import (  # noqa
    transform_effort_and_captures_from_cameras_and_traps_to_dict,
)

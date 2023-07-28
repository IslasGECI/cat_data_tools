from .filter_data_by_month import summarize_effort_captures_and_trappers
import pandas as pd
import typer


app = typer.Typer(help="Cat tools for eradication projects")


@app.command(help="Write monthly summary from weekly summary")
def write_monthly_summary(weekly_data_path: str, monthly_trappers_path: str, output_path: str):
    effort_data = pd.read_csv(weekly_data_path)
    monthly_trappers = pd.read_csv(monthly_trappers_path)
    monthly_data = summarize_effort_captures_and_trappers(monthly_trappers, effort_data)
    monthly_data.to_csv(output_path, index=False, na_rep="NA")

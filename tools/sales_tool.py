from pydantic import BaseModel, Field
from tools.base import Tool


class GetSalesByDayArgs(BaseModel):
    day: str = Field(description="Day in format YYYY-MM-DD")


class GetSalesToday(Tool):
    name = "get_sales_today"
    description = "Get the total sales amount for today. Use this when the user asks about today's sales, revenue, or how much they made today."
    args_model = GetSalesByDayArgs

    def execute(self, arguments: GetSalesByDayArgs):
        if arguments.day == "2026-02-17":
            return 99

        return 10

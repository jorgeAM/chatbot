from tools.base import Tool


class GetSalesToday(Tool):
    name = "get_sales_today"
    description = "Get the total sales amount for today. Use this when the user asks about today's sales, revenue, or how much they made today."

    def execute(self, arguments):
        return "99 USD"

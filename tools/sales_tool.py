from tools.base import Tool

class GetSalesToday(Tool):
    name = "get_sales_today"
    description = "Use this tool to get the total sales for today"

    def execute(self, arguments):
        return "99 USD"

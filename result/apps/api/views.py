from quart import current_app

from ...helpers.result import ResultParser


async def result(roll: int):
    result = ResultParser.get_single_result(current_app.results, roll)
    return result

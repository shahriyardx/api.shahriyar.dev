from quart import current_app

from ...helpers.result import ResultParser


async def result(roll: int):
    if roll in current_app.result_cache:
        result = current_app.result_cache[roll]
    else:
        result = ResultParser.get_single_result(current_app, roll)

    return result

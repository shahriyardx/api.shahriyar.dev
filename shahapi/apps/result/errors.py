from . import result_api


@result_api.app_errorhandler(404)
async def not_found(e):
    return "This route doesn't exist", 404

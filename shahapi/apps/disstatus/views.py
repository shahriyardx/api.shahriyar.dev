from quart import current_app

async def status(user_id: int):
    return {'something': user_id}
    

from app import app

@app.sio.on('connect')
async def _connect(sid, *args, **kwargs):
    print('CONNECTED')

from aiohttp import web
import json

async def handle(request):
    response_obj={'Hello':'da'}
    return web.Response(text=json.dumps(response_obj),status=200)

async def new_user(request):
    try:
        data=await request.post().match_info('name')
        print(data)
        response_obj={'status':'good'}
        return web.Response(text=json.dumps(response_obj),status=200)
    except Exception as e:
        response_obj={'status':'500','mess':str(e)}
        return web.Response(text=json.dumps(response_obj),status=500)


app=web.Application(debug=True)
app.router.add_get('/',handle)
app.router.add_post('/user',new_user)

web.run_app(app)
from quart import jsonify
from sanic import Blueprint
from sanic.request import Request, RequestParameters
from utils import render
from sclib.asyncio import SoundcloudAPI, Track, Playlist
from io import BytesIO


sc_downloader = Blueprint('soundcloud')

@sc_downloader.route('/soundcloud/')
async def index(request):
    context = {'title':'Soundcloud Downloader | ISOGEN.net'}
    return await render('app/soundcloud.html', context)


@sc_downloader.route('/api/soundcloud/resolve')
async def resolve_url(request:Request):
    url = request.args.get('url')
    api = SoundcloudAPI()

    try:
        object = await api.resolve(url)  # type: Track
        if type(object) is Playlist:

            await object.clean_attributes()

    except Exception as e:
        import sys
        print(e, file=sys.stderr)
        return jsonify({},status=400)
    return jsonify(object.to_dict())


@sc_downloader.route('/api/soundcloud/tracks/<id>')
async def download_track(request:Request, id):
    api = SoundcloudAPI()
    tracks = await api.get_tracks(id)
    track = Track(obj=tracks[0], client=api)  # type: Track

    filename = f'/tmp/{track.id}.mp3'
    with open(filename, 'wb+') as fp:
        await track.write_mp3_to(fp)

    return await file_stream(filename, mime_type='audio/mp3', filename=f'{track.artist} - {track.title}.mp3')


@sc_downloader.route("/soundcloud/<username>/sets/<playlist_name>")
async def view_playlist(request:Request, username, playlist_name):
    url = f"https://soundcloud.com/{username}/sets/{playlist_name}"
    context = {
        'title': f'Download {playlist_name} by {username} | ISOGEN.net',
        'url':url
    }
    return await render('app/soundcloud/playlist.html', context)
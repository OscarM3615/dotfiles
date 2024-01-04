import dbus

MAX_LENGTH = 35
OUTPUT_FORMAT = ' {title} - {artist}'

try:
    bus = dbus.SessionBus()
    spotify = bus.get_object('org.mpris.MediaPlayer2.spotify',
                             '/org/mpris/MediaPlayer2')
    props = dbus.Interface(spotify, 'org.freedesktop.DBus.Properties')

    metadata = props.Get('org.mpris.MediaPlayer2.Player', 'Metadata')

    artist = metadata.get('xesam:artist')[0] if metadata.get(
        'xesam:artist') else ''
    title = metadata.get('xesam:title') if metadata.get(
        'xesam:title') else ''

    result = OUTPUT_FORMAT.format(title=title, artist=artist)

    if len(result) > MAX_LENGTH:
        result = result[:MAX_LENGTH - 3] + '...'

    if artist and title:
        print(result)
except dbus.exceptions.DBusException:
    print('')
except Exception as ex:
    print(ex)

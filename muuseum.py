import serial
import vlc

port = "COM3"
baud_rate = 115200
videos = {
    "play1": r"C:\Users\oskarpar\Desktop\KAAMERA\PRIVATE\AVCHD\BDMV\STREAM\00001.MTS",
    "play2": r"C:\Users\oskarpar\Desktop\KAAMERA\PRIVATE\AVCHD\BDMV\STREAM\00003.MTS"
}

vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()

try:
    ser = serial.Serial(port, baud_rate)
    print(f"Ootan vajutust pordil {port}...")
    
    while True:
        line = ser.readline().decode("utf-8").strip()
        
        if line in videos:
            if player.is_playing():
                player.stop()

            media = vlc_instance.media_new(videos[line])
            player.set_media(media)
            player.play()
            player.set_fullscreen(True)

except serial.SerialException as e:
    print(f"Error opening serial port {port}: {e}")
except KeyboardInterrupt:
    print("Programm kasutaja poolt katkestatud")

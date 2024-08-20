from machine import I2S, Pin
import time

def record_audio(file_path, sck_pin_number=18, ws_pin_number=19, sd_pin_number=5, record_duration_ms=3000, buffer_size=2048, mode=I2S.RX, bits=16, format=I2S.MONO, rate=16000, ibuf=8096):
    """Record audio from the I2S microphone and save it to a file."""
    # Setup I2S for audio input
    sck_pin = Pin(sck_pin_number)
    ws_pin = Pin(ws_pin_number)
    sd_pin = Pin(sd_pin_number)
    
    audio_in = I2S(
        0,
        sck=sck_pin,
        ws=ws_pin,
        sd=sd_pin,
        mode=mode,
        bits=bits,
        format=format,
        rate=rate,
        ibuf=ibuf,
    )
    
    print(f"Recording for {record_duration_ms / 1000} seconds")

    # Buffer for audio data
    samples = bytearray(buffer_size)
    start_time = time.ticks_ms()

    # Open file to write the recorded data
    with open(file_path, "wb") as file:
        while time.ticks_diff(time.ticks_ms(), start_time) < record_duration_ms:
            read_bytes = audio_in.readinto(samples)
            file.write(samples[:read_bytes])
    
    print("Finished Recording")

if __name__ == "__main__":
    record_audio("test.raw")

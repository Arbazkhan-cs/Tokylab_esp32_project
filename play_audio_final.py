from machine import I2S, Pin

def play_audio(wav_file, sample_rate_in_hz=8000):
    bck_pin = Pin(26) 
    ws_pin = Pin(25)  
    sdout_pin = Pin(22)

    audio_out = I2S(
        1, 
        sck=bck_pin,
        ws=ws_pin,
        sd=sdout_pin, 
        mode=I2S.TX,
        bits=16, 
        format=I2S.STEREO,
        rate=sample_rate_in_hz,
        ibuf=5000
    )

    wav = open(wav_file, 'rb')

    # Advance to first byte of Data section in WAV file
    wav.seek(44)

    # Allocate sample arrays
    wav_samples = bytearray(2048)
    wav_samples_mv = memoryview(wav_samples)

    print('Starting')
    try:
        while True:
            num_read = wav.readinto(wav_samples_mv)
            if num_read == 0:
                break  # Exit the loop after playing the audio once
            num_written = 0
            while num_written < num_read:
                num_written += audio_out.write(wav_samples_mv[num_written:num_read])
    except (KeyboardInterrupt, Exception) as e:
        print(f'Caught exception {type(e).__name__}: {e}')
    
    wav.close()
    audio_out.deinit()
    print('Done')

if __name__ == "__main__":
    #play_audio("response_audio.raw")
    #play_audio("recorded_audio.raw")
    play_audio("synthesized_audio.wav")
import os
from f5_tts.api import F5TTS

def main():
    print("=" * 40)
    print("VOICE CLONING USING F5-TTS")
    print("=" * 40)

    reference_audio = input("Enter reference audio path: ").strip().strip('"')
    reference_text = input("Enter exact transcript of reference audio: ").strip()
    target_text = input("Enter text to generate: ").strip()

    if not os.path.isfile(reference_audio):
        print("Error: Reference audio file does not exist.")
        return
    if not reference_text:
        print("Error: Reference transcript cannot be empty.")
        return
    if not target_text:
        print("Error: Target text cannot be empty.")
        return

    output_file = "cloned_voice.wav"

    model = F5TTS()
    model.infer(
        ref_file=reference_audio,
        ref_text=reference_text,
        gen_text=target_text,
        file_wave=output_file
    )

    print("\nVOICE CLONING COMPLETE")
    print("Reference Audio :", os.path.basename(reference_audio))
    print("Output File     :", output_file)

if __name__ == "__main__":
    main()

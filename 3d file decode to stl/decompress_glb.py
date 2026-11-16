
from pathlib import Path
import brotli

# Original BuildCores model
INPUT = Path(
    r"C:\Users\tt\Downloads\642599278f1bfd41942ae558_medium.glb.br"
)

# Output GLB
OUTPUT = Path(
    r"C:\projects\3d file\GR701.glb"
)

def main():
    data = INPUT.read_bytes()

    print("Original file size:", len(data))
    print("Original header:", data[:16].hex(" "))

    try:
        result = brotli.decompress(data)

        print("Decompression successful!")
        print("Decompressed size:", len(result))
        print("Decompressed header:", result[:16].hex(" "))

        if result[:4] == b"glTF":
            OUTPUT.write_bytes(result)
            print("Valid GLB file!")
            print("Saved to:", OUTPUT)
        else:
            print("Warning: Output is not a standard GLB.")

    except brotli.error as e:
        print("Brotli decompression failed:", e)

if __name__ == "__main__":
    main()

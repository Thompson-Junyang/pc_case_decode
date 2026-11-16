

from pathlib import Path
import gzip
import zlib
import bz2
import lzma
import brotli

src = Path(r"C:\Users\tt\Downloads\642599278f1bfd41942ae558_medium.glb.br")
data = src.read_bytes()

print("File size:", len(data))
print("Header:", data[:32].hex(" "))

decoders = {
    "Brotli": brotli.decompress,
    "Gzip": gzip.decompress,
    "Zlib": zlib.decompress,
    "Raw Deflate": lambda b: zlib.decompress(b, -15),
    "Bzip2": bz2.decompress,
    "LZMA": lzma.decompress,
}

for name, decoder in decoders.items():
    try:
        result = decoder(data)
        print(f"\n{name}: SUCCESS")
        print("Output size:", len(result))
        print("Output header:", result[:16].hex(" "))

        if result[:4] == b"glTF":
            output = Path("GR701.glb")
            output.write_bytes(result)
            print("Valid GLB header! Saved:", output.resolve())
            break

    except Exception as e:
        print(f"{name}: failed ({type(e).__name__})")

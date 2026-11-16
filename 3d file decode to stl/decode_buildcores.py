
from pathlib import Path
import brotli

# 修改成你下载的文件名
input_file = Path("642599278f1bfd41942ae558_medium.glb.br")
output_file = input_file.with_suffix("")

salt = "BSQw8a54yg0HPntWIf6Bw5JGab4CAuTQ"

data = input_file.read_bytes()

# 对应 JavaScript 的 XOR 变换
decoded = bytes(
    b ^ ord(salt[i % len(salt)]) ^ (i & 255)
    for i, b in enumerate(data)
)

try:
    result = brotli.decompress(decoded)

    print("Brotli 解压成功！")
    print("解压后大小:", len(result))
    print("文件头:", result[:16])

    if result[:4] == b"glTF":
        output_file.write_bytes(result)
        print("GLB 文件已保存:", output_file)
    else:
        print("解压成功，但文件头不是标准 GLB，需要进一步检查。")

except brotli.error as e:
    print("解压失败:", e)

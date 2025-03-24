from pathlib import Path

import shutil
import sys
import json

from configure import configure_ocr_model


working_dir = Path(__file__).parent
install_path = working_dir / Path("install")
version = len(sys.argv) > 1 and sys.argv[1] or "v0.0.1"


def install_deps():
    # 检查工作目录下的 "deps" 文件夹是否存在
    if not (working_dir / "deps" / "bin").exists():
        # 如果不存在，提示用户先下载 MaaFramework 到 "deps" 文件夹
        print("Please download the MaaFramework to \"deps\" first.")
        print("请先下载 MaaFramework 到 \"deps\"。")
        # 退出程序
        sys.exit(1)

    # 将 "deps" 文件夹下的 "bin" 文件夹复制到安装路径
    shutil.copytree(
        working_dir / "deps" / "bin",
        install_path,
        # 忽略以下文件
        ignore=shutil.ignore_patterns(
            "*MaaDbgControlUnit*",
            "*MaaThriftControlUnit*",
            "*MaaRpc*",
            "*MaaHttp*",
        ),
        # 如果目标文件夹已存在，则覆盖
        dirs_exist_ok=True,
    )
    # 将 "deps" 文件夹下的 "share" 文件夹下的 "MaaAgentBinary" 文件夹复制到安装路径
    shutil.copytree(
        working_dir / "deps" / "share" / "MaaAgentBinary",
        install_path / "MaaAgentBinary",
        # 如果目标文件夹已存在，则覆盖
        dirs_exist_ok=True,
    )


def install_resource():

    # 配置OCR模型
    configure_ocr_model()

    # 将资源文件复制到安装路径
    shutil.copytree(
        working_dir / "assets" / "resource",
        install_path / "resource",
        dirs_exist_ok=True,
    )
    # 将interface.json文件复制到安装路径
    shutil.copy2(
        working_dir / "assets" / "interface.json",
        install_path,
    )

    # 读取interface.json文件
    with open(install_path / "interface.json", "r", encoding="utf-8") as f:
        interface = json.load(f)

    # 更新interface.json文件中的版本号
    interface["version"] = version

    # 将更新后的interface.json文件写回安装路径
    with open(install_path / "interface.json", "w", encoding="utf-8") as f:
        json.dump(interface, f, ensure_ascii=False, indent=4)

def install_chores():
    # 将working_dir目录下的README.md文件复制到install_path目录下
    shutil.copy2(
        working_dir / "README.md",
        install_path,
    )
    # 将working_dir目录下的LICENSE文件复制到install_path目录下
    shutil.copy2(
        working_dir / "LICENSE",
        install_path,
    )
    # 将working_dir目录下的logo.ico文件复制到install_path目录下
    shutil.copy2(
        working_dir / "logo.ico",
        install_path,
    )



if __name__ == "__main__":
    install_deps()
    install_resource()
    install_chores()

    print(f"Install to {install_path} successfully.")
# quickshot

Windows 一键截屏工具：按一下，截图直接进剪贴板，自动存档，开机自启。

配合支持图片粘贴的应用（如 Kimi Code CLI 的 `Alt+V`），发截图从"截屏→保存→找文件→拖拽"缩短到"F9 → Alt+V → 回车"。

## 功能

| 快捷键 | 动作 |
|---|---|
| `F9` | 全屏截图 → 剪贴板 + 存档（成功有提示音） |
| `F10` | 当前活动窗口截图 → 剪贴板 + 存档 |

- 存档目录：`C:\Users\Administrator\screenshots\`（时间戳命名，`latest.png` 恒为最新一张）
- 后台常驻，无窗口无托盘图标，资源占用可忽略

## 安装与运行

依赖：Python 3.9+，然后：

```bash
pip install pillow pywin32 keyboard
pythonw quickshot.py     # 后台启动
```

### 开机自启（可选）

在 `shell:startup`（Win+R 输入回车）目录放一个指向 `pythonw.exe quickshot.py` 的快捷方式即可。

### 停止

运行 `quickshot_stop.bat`，或任务管理器结束对应 `pythonw.exe` 进程。

## 说明

- "直接发送"刻意不做：截屏瞬间焦点在被截窗口上，脚本替你按键会把图贴错地方。F9 → 切到目标窗口 → 粘贴，是最短且可靠的链路。
- 剪贴板写入格式为 CF_DIB，兼容主流应用的粘贴。

## 反馈

遇到问题或想要新功能，到 [Issues](https://github.com/lotuswu2580-dev/fuplus-tools/issues) 提一句就行。

# BossKey

![build-passing](https://img.shields.io/badge/build-passing-brightgreen)

本项目基于[keyboard](https://github.com/boppreh/keyboard)和[pywin32]，**目前只支持在windows平台使用**

支持使用自定义热键，一键隐藏特定的窗口，并展示需要展示的窗口。

## 使用方法

### 使用exe文件运行

可直接在release页面下载本项目的二进制可执行文件（`.exe`），点击即可使用。

### 使用python运行

运行源码前，需要安装以下库：

- pywin32
- tkinter
- keyboard
- json
- ctypes
- sys

使用以下命令运行程序：

```shell
cd src/
python3 main.py
```

成功运行后，会出现如下页面:

![BossKey主页面](https://raw.githubusercontent.com/SSRMori/photo/master/img/BossKey界面.png)

- `confirm`按钮：选中需要**保留**的窗口后按下confirm按钮进行确认
- `update`按钮：按下该按钮，更新当前窗口信息

确认保留的页面后，使用快捷键即可对窗口进行隐藏/显示

默认快捷键设置如下：

|按键|功能|
|:-:|:-|
|`Alt+D`|隐藏未选中窗口，并置顶+最大化选中窗口|
|`ESC+Alt+D`|显示所有（未选中/选中）窗口，可从`Alt+D`状态恢复窗口|
|`Ctrl+Alt+Shift+H`|隐藏`BossKey`窗口|
|`Ctrl+Alt+Shift+S`|显示`BossKey`窗口|

自定义快捷键可在程序（`main.py`/`.exe`）目录下新建`hotkey.json`，并以如下格式，遵循[keyboard](https://github.com/boppreh/keyboard)hotkey的定义格式，定义**全部**的快捷键：

```json
{
    "bossKey": "alt+d",
    "exitBossKey": "esc+alt+d",
    "hide": "ctrl+alt+shift+h",
    "show": "ctrl+alt+shift+s"
}
```

**建议使用前检查热键冲突！建议设置完成后隐藏BOSSKEY窗口！**


## TODOs

- [ ] 优化UI界面
- [ ] 增加确认等步骤提示
- [ ] 改进对窗口的识别
- [ ] 跨平台支持

## 打赏

请开发者喝杯奶茶吧！

![支付宝](https://raw.githubusercontent.com/SSRMori/photo/master/img/AlipayQR.jpg)

![微信](https://raw.githubusercontent.com/SSRMori/photo/master/img/WechatQR.jpg)
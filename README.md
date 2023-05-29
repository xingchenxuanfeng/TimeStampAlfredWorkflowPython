# TimeStampAlfredWorkflowPython

参考 https://github.com/WiconWang/Alfred-Workflows-TimeStamp 写的 alfred 插件.

功能和上面链接里的原版基本一致.

重写的原因是换了新电脑,安装原版插件时,发现原版插件时 php 写的,而新版 macos 没有了 php 环境,运行直接报错! 手动装了 php 环境后,还是报错,原版插件和新版 alfred 不兼容!

遂使用 python 重写了一遍.

## 使用说明

1. time now
显示当前时间、时间戳、毫秒时间戳

2. time 1488888888 时间戳转为时间.

3. time 2017-03-07 20:14:48 时间转为时间戳

按回车将当前选中内容保存到剪切板

![demo](https://raw.githubusercontent.com/xingchenxuanfeng/TimeStampAlfredWorkflowPython/main/wf.png)

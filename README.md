# 个人Rime配置

## 基础配置：[雾凇拼音](https://github.com/iDvel/rime-ice)

## 字体：[霞鹜新晰黑](https://github.com/lxgw/LxgwNeoXiHei)

## 安装或更新

任务栏右键输入法->输入法设定->获取更多输入方案

``` bash
# 安装雾凇拼音
Enter package name, URL, user/repo or downloaded ZIP to install: iDvel/rime-ice:others/recipes/full
# 安装个人配置
Enter package name, URL, user/repo or downloaded ZIP to install: fimmy/rime-config
```

``` bash
iDvel/rime-ice:others/recipes/full fimmy/rime-config
```

## 配置好`雾凇拼音`后，复制文件到用户资料文件夹覆盖，修改`rime_ice.dict.yaml`，取消大字表的注释后重新部署即可

| 文件                      | 说明               |
| ------------------------- | ------------------ |
| default.custom.yaml       | 全局自定义配置     |
| double_pinyin.custom.yaml | 双拼方案自定义配置 |
| rime_ice.custom.yaml      | 雾凇拼音自定义配置 |
| weasel_fimmy.yaml         | 个人方案、配色配置 |
| weasel.custom.yaml        | 小狼毫自定义配置   |
| fimmy.dict.yaml           | 个人词库配置       |
| recipe.yaml               | plum安装配置       |
# 快速开始

![](asset/xbot.jpg)

## 使用方法 

1. 安装依赖包

推荐使用 python3.8

```bash
python -m pip install -U pip
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple rasa==2.8
pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
```

如果出现 santic 相关错误，请重新安装 sanic-jwt 包

```bash
pip install sanic-jwt==1.6.0
```

安装完包，执行以下命令，判断是否安装成功。

```bash
rasa --version 
```


rasa、rasa sdk 和 rasa-x 要符合[兼容矩阵](https://rasa.com/docs/rasa-x/changelog/compatibility-matrix)

1. 训练 Rasa 对话模型

--num-thread 表示要使用的训练线程的数量，模型会存储在 /models/default 中。

```bash
rasa train --num-threads 4
```

3. 运行 Rasa action server

```bash
rasa run actions
```


4. 使用 rasa x 进行对话机器人的测试

```
rasa x
```

5. 持续更新对话机器人

## 对话效果不好？


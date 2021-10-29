# 快速开始

使用 Rasa 构建中文对话机器人，项目包括
- 闲聊
- 知识库查询
- 任务设置
- 知识图谱使用
- 自定义 Component

欢迎加入，一起共建中文智能对话机器人 :robot:。

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

## 领域对话测试
### 闲聊领域
```bash
rasa data validate --domain domain/chitchat/domain.yml --data data/chitchat/ 
rasa train --domain domain/chitchat/domain.yml --data data/chitchat/ --config config/chitchat.yml
rasa shell --debug
```

### 健康领域
```bash
rasa data validate --domain domain/health/domain.yml --data data/health/
rasa train --domain domain/health/domain.yml --data data/health/
rasa train core -d domain/health/domain.yml -s data/health/story.yml
RASA_X_PASSWORD=rasa rasa x --domain domain/health/domain.yml 
```

## NLU

```bash
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download zh_core_web_sm
```

## TODO
[这里](TODO.md) 有项目的 TODO 列表，欢迎提交你的想法，提交 PR，一起建设一个强大的对话机器人。
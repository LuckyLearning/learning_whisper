# learning_whisper
学习whisper时的一些想法

## 安装依赖
```shell
pip install -U openai-whisper
pip install sanic
pip install pyngrok
```
配置文件在：config.yml
## 执行
```shell
./start.sh
```
ngrok地址，形如：
NgrokTunnel: "https://f721-113-57-20-204.ngrok.io" -> "http://localhost:9090"
本地地址：
http://0.0.0.0:9090
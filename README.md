
conda
下载与安装
使用 清华下载源 下载：Miniconda3-py38_4.10.3-Windows-x86_64.exe 并安装。

基本操作
常用操作
# 查看版本号
conda --version

# 查看当前存在的虚拟环境
conda env list

# 查看-安装-更新-删除 package
conda list
conda search  package-name
conda install package-name
conda install package-name=vesion
conda update  package-name
conda remove  package-name
虚拟环境管理
# 创建 env-name 的虚拟环境
conda create --name env-name  

# 创建 env-name 的虚拟环境，并指定 python 版本
conda create --name env-name python=3.8

# 创建 env-name 的虚拟环境，指定 python 版本和某些包
conda create --name env-name numpy scipy

# Linux 激活虚拟环境
source activate env-name

# Windows 激活虚拟环境
activate env-name

# Linux 退出虚拟环境
source deactivate env-name

# Windows 退出虚拟环境
deactivate env-name

# 删除虚拟环境
conda remove --name env-name --all

# 复制某个环境
conda create --name new-env-name --clone old-env-name
指定环境中管理包
conda list --name env-name
conda install --name env-name package-name
conda remove  --name env-name package-name
使用国内源
# 添加源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/

# 删除源
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/

# 显示源
conda config --show-sources  

# 安装包时显示channel的url
conda config --set show_channel_urls yes
jupyter notebook
安装与运行
pip install jupyter notebook

【jupyter notebook】 # 网页中输入：http://localhost:8888/tree
【Control+C】停止服务

两种模式


命令模式->编辑模式：【Enter】
编辑模式->命令模式：【Esc】
命令模式快捷键
H：显示快捷键帮助
F：查找和替换
P：打开命令面板
Y：把当前 cell 内容转换为代码形式
M：把当前 cell 内容转换为 markdown 形式
A：在上方新建cell
B：在下方新建cell
X/C/Shift-V/V：剪切/复制/上方粘贴/下方粘贴
双击D：删除当前 cell
Z：撤销删除
S：保存 notebook
L：为当前 cell 的代码添加行编号
Shift+上下键：按住 Shift 进行上下键操作可复选多个 cell
Shift+L：为所有 cell 的代码添加行编号
Shift+M：合并所选 cell 或合并当前 cell 和下方的 cell
Ctrl+Enter：运行当前 cell
Shift+Enter：运行当前 cell 并跳转到下一 cell
Alt+Enter：运行当前cell并在下方新建 cell
双击 I：停止 kernel
双击 0：重启 kernel
编辑模式快捷键
Tab：代码补全
Ctrl+A：全选
Ctrl+Z：撤销
Ctrl+Home：将光标移至cell最前端
Ctrl+End：将光标移至cell末端
其它
jupyter notebook 导出 markdown 文件格式：
pip install nbconvert
pip install pandoc
jupyter nbconvert --to FORMAT notebook.ipynb
若要使用 Matplotlib 绘图，为确保图形能顺利输出，需在 cell 开头键入 %matplotlib inline
Autopep8 插件：规范化代码格式：需要通过 pip install autopep8 安装 autopep8，安装完之后需要重启 jupyter notebook 服务才能生效
pytorch
pip install torch==1.10.2
pip install torchvision==0.11.3
测试：

import torch

print(torch.arange(10))
tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

__EOF__

本文作者：刘皇叔
本文链接：https://www.cnblogs.com/xiaojianliu/p/16149089.html
关于博主：评论和私信会在第一时间回复。或者直接私信我。
版权声明：本博客所有文章除特别声明外，均采用 BY-NC-SA 许可协议。转载请注明出处！
声援博主：如果您觉得文章对您有帮助，可以点击文章右下角【推荐】一下。您的鼓励是博主的最大动力！
分类: pytorch 深度学习
好文要顶 关注我 收藏该文 微信分享刘-皇叔
粉丝 - 106 关注 - 0
+加关注
00
« 上一篇： 线程安全的对象生命周期管理
» 下一篇： pytorch 深度学习之数据操作
posted @ 2022-04-15 14:48  刘-皇叔  阅读(118)  评论(0)  编辑  收藏  举报
登录后才能查看或发表评论，立即 登录 或者 逛逛 博客园首页
【推荐】阿里巴巴全球数学竞赛，首次向AI开放，期待您的参加
【推荐】园子周边第二季：更大的鼠标垫，没有logo的鼠标垫

编辑推荐：
· 从 0-1 聊聊网络的演进
· 记一次 .NET某防伪验证系统 崩溃分析
· MappedByteBuffer VS FileChannel：从内核层面对比两者的性能差异
· 深度探索 .NET Feature Management 功能开关的魔法
· 线上 gc 问题 - SpringActuator 的坑

阅读排行：
· 一款比Typora更简洁优雅的Markdown编辑器神器（完全开源免费）
· 我们正在被 DDoS 攻击，但是我们啥也不干，随便攻击...
· 强烈推荐：2024 年12款 Visual Studio 亲测、好用、优秀的工具，AI插件等
· .NET开源、免费、跨平台的Git可视化管理工具
· 京东一面挂在了CAS算法的三大问题上，痛定思痛不做同一个知识点的小丑
MENU	
pytorch 深度学习之环境安装与配置
发表于 2022-04-15 14:48阅读：118评论：0推荐：0

PYTORCH 深度学习

[ Stay hungryStay foolish ]
This blog has running : 1917 d 1 h 10 m 49 sღゝ◡╹)ノ♡
友情链接：暗时间/酷壳/廖雪峰/阮一峰/陈硕/当然我在扯淡/Andrzej's C++ blog/Microsoft C++ blog
Copyright © 2024 刘-皇叔 Powered by .NET 8.0 on Kubernetes
Theme version: v1.3.3 / Loading theme version: v1.3.3




--------------
，也是一个可执行命令，其核心功能是包管理与环境管理。所以对虚拟环境进行创建、删除等操作需要使用conda命令。

conda 本地环境常用操作
#获取版本号
conda --version 或 conda -V

#检查更新当前conda
conda update conda

#查看当前存在哪些虚拟环境
conda env list 或 conda info -e

#查看--安装--更新--删除包

conda list：
conda search package_name# 查询包
conda install package_name
conda install package_name=1.5.0
conda update package_name
conda remove package_name
conda创建虚拟环境
#创建名为your_env_name的环境
conda create --name your_env_name
#创建制定python版本的环境
conda create --name your_env_name python=2.7
conda create --name your_env_name python=3.6
#创建包含某些包（如numpy，scipy）的环境
conda create --name your_env_name numpy scipy
#创建指定python版本下包含某些包的环境
conda create --name your_env_name python=3.6 numpy scipy
激活虚拟环境
#Linux
source activate your_env_name

#Windows
activate your_env_name
退出虚拟环境
#Linux
source deactivate your_env_name

#Windows
deactivate env_name
删除虚拟环境
conda remove -n your_env_name --all
conda remove --name your_env_name --all
复制某个环境
conda create --name new_env_name --clone old_env_name
在指定环境中管理包
conda list -n your_env_name
conda install --name myenv package_name 
conda remove --name myenv package_name
使用国内 conda 软件源加速
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes
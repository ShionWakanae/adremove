## 功能：
- 查看模型参数文件中的所有参数名，参数值，值类型。
- 修改模型中的参数值（输入已有参数名，再输入新参数值）
- 删除模型中的某个参数（输入已有参数名，再输入一个空格）
- 新增某个参数到模型中（输入新参数名，再输入参数值）—— 应该没有用吧？


## 作用：
- 等2秒按回车修改参数困难的时候用。
- 删掉模型参数中的广告语句。
- 模型训练太久保留loss历史太多文件太大。


## 用法：
1. 解压到DFL的主目录。
1. 运行“--ADRemove模型参数删改查 by 若苗瞬.bat”批处理。
1. 选一个模型参数配置文件（模型是正常放在"workspace\model"里的，参数配置文件是".dat"文件）。
1. 增删改查参数名/参数值（参考上方【功能】）（重复）。
1. 在参数名那输出“quit”保存退出。
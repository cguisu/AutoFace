# AutoFace
 
## 使用流程
1. 下载 DeepFaceLab2.0，在目录DeepFaceLab2.0\成本版本\DeepFaceLab_NVIDIA_build_05_06_2020中找到DeepFaceLab_NVIDIA文件夹。
2. 下载或克隆本AutoFace项目，并将DeepFaceLab_NVIDIA文件夹放其中，文件目录如下图所示。![目录](https://github.com/cguisu/AutoFace/blob/master/cap.png)
3. 将模特视频放入model_vedio文件夹，学生视频（视频文件名用学生姓名拼音）放入student_vedio文件夹。
4. 双击运行run_this.bat，输入训练迭代次数（可设定为10000代），按回车即可开始运行整个程序。
5. 程序运行结束后，在DeepFaceLab文件夹中会有多个前缀为workpace的文件夹（数量取决于学生视频文件夹中的数量），后缀为学生姓名拼音，人工重命名对应文件夹为workpace，然后运行merge SHAEHD.bat处理图像，后续具体操作参照上次DeepFaceLab简介所讲内容，直到导出视频，为workpace文件夹中的result.mp4，查看结果并将结果保存，将文件夹换回之前的名字，操作下一个文件夹。

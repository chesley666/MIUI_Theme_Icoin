一、设计图标上层遮罩，保存并替换mask.png<br/>
===

二、（可选）第三方图标变形工具<br/>
===
1、下载第三方图标放到temp_baseicoin，动过adb shell "logcat | grep START"查看包名，并更改下载的图标文件名；<br/>
执行resize_tmp_baseicoin.py，会把图标变成182*182大小并截取144*144的圆，复制到baseIcoin里<br/>

三、生成xml工具<br/>
===
1、修改main.py 15行 card_captor_sakura<br/>
2、（可选）修改main.py 45行 face_sf=0.7, base_sf=0.7, mask_sf=1 缩放倍率，默认face144*144，base182*182，mask182*182<br/>
3、执行main.py，生成结果在result文件夹下，将result目录下全部文件拷贝到编辑器目录下的icoin/fancy_icoin下，用编辑器应用主题<br/>
备注：<br/>
第三方图标大小需要手动修改编辑器中的图标滤镜<br/>

效果预览：<br/>
===
![Image text](https://github.com/ChesleyCN/MIUI_Theme_Icoin/blob/master/preview/syaooran_preview.gif)

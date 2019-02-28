生成xml工具
1、修改main.py 15行 card_captor_sakura
2、（可选）修改main.py 45行 face_sf=0.7, base_sf=0.7, mask_sf=1 缩放倍率，默认face144*144，base182*182，mask182*182
3、执行main.py，生成结果在result文件夹下，将result目录下全部文件拷贝到编辑器目录下的icoin/fancy_icoin下，用编辑器应用主题
备注：
第三方图标大小需要手动修改图标滤镜

第三方图标变形工具
1、下载第三方图标放到temp_baseicoin，动过adb shell "logcat | grep START"查看包名，并更改下载的图标文件名；
执行resize_tmp_baseicoin.py，会把图标变成182*182大小并截取144*144的圆，复制到baseIcoin里
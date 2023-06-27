# Guideline
## 将所有待分析文件加入files目录下
### decoder_analysis
用于分析files目录下的所有decoder文件
### encoder_analysis
用于分析files目录下的所有encoder文件
### encoder_decoder_single_analysis
用于分析特定的encoder和decoder文件x

encode文件：
* all.encoder_single_analysis("文件的相对路径或绝对路径")

decoder文件:
* all.decoder_single_analysis("文件的相对路径或绝对路径")
### filter_by_time
用于选择输入的起始和截至时间内范围内的所有数据，并生成新的csv文件，并分析

新的文件将会被保存在files_filter_by_time目录下

all.filter_by_time("文件的相对路径或绝对路径", '起始时间，如：2023-06-07T11:45:40+0200','结束时间')
### merge
用于合并两个文件中的数据，如有相同数据，后输入的文件覆盖前面的文件，同时对合并后的文件进行分析

新生成的文件保存在files_merged目录下

all.merge('文件的相对路径或绝对路径','文件的相对路径或绝对路径')



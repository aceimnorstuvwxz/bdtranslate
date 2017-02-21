# bdtranslate

Google is no longer provider free services. If using the web API, blocking(503) happens soon or later.
Now baidu translate service provider 2000 thousand free word per month, Wow! Here is the simple python wrapper.
Enjoy!

Don't use the testing appid/secret provided in testing code, it will reserved in any time.
Get your own appid/secret in ONE minute by [this](http://api.fanyi.baidu.com/api/trans/product/index).


##Installation

	pip install bdtranslate

##Usage

```
import bdtranslate

yourAppId = '20170221000039563'
yourSecret = 'nIyk6j2N4pOIc3PpE9tY'

print dbtranslate.translate(yourAppId, yourSecret, "en", "zh", "Prisident reject to lough out loudly, interesting!")

```
总统拒绝笑大声，有趣！


##language arguments
<div>
<table class="info-table">
<tbody><tr>
<th>simbol</th>
<th>ref</th>
</tr>
<tr>
<td>auto</td>
<td>自动检测</td>
</tr>
<tr>
<td>zh</td>
<td>中文</td>
</tr>
<tr>
<td>en</td>
<td>英语</td>
</tr>
<tr>
<td>yue</td>
<td>粤语</td>
</tr>
<tr>
<td>wyw</td>
<td>文言文</td>
</tr>
<tr>
<td>jp</td>
<td>日语</td>
</tr>
<tr>
<td>kor</td>
<td>韩语</td>
</tr>
<tr>
<td>fra</td>
<td>法语</td>
</tr>
<tr>
<td>spa</td>
<td>西班牙语</td>
</tr>
<tr>
<td>th</td>
<td>泰语</td>
</tr>
<tr>
<td>ara</td>
<td>阿拉伯语</td>
</tr>
<tr>
<td>ru</td>
<td>俄语</td>
</tr>
<tr>
<td>pt</td>
<td>葡萄牙语</td>
</tr>
<tr>
<td>de</td>
<td>德语</td>
</tr>
<tr>
<td>it</td>
<td>意大利语</td>
</tr>
<tr>
<td>el</td>
<td>希腊语</td>
</tr>
<tr>
<td>nl</td>
<td>荷兰语</td>
</tr>
<tr>
<td>pl</td>
<td>波兰语</td>
</tr>
<tr>
<td>bul</td>
<td>保加利亚语</td>
</tr>
<tr>
<td>est</td>
<td>爱沙尼亚语</td>
</tr>
<tr>
<td>dan</td>
<td>丹麦语</td>
</tr>
<tr>
<td>fin</td>
<td>芬兰语</td>
</tr>
<tr>
<td>cs</td>
<td>捷克语</td>
</tr>
<tr>
<td>rom</td>
<td>罗马尼亚语</td>
</tr>
<tr>
<td>slo</td>
<td>斯洛文尼亚语</td>
</tr>
<tr>
<td>swe</td>
<td>瑞典语</td>
</tr>
<tr>
<td>hu</td>
<td>匈牙利语</td>
</tr>
<tr>
<td>cht</td>
<td>繁体中文</td>
</tr>
</tbody></table>

</div>


##Lisense
MIT


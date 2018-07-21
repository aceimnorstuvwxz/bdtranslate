# bdtranslate

Google is no longer a provider of free services. If you are using any of the unofficial APIs, getting blocked(503) will happen sooner or later.

Fortunately, Baidu Translator now offers 2 million free characters per month, with no limit on the number or frequency of requests.  Here is a simple Python2 wrapper.
Enjoy!

Don't use the testing appid & secret provided in testing code.
Create a free Baidu account and obtain your own appid & secret [here](http://api.fanyi.baidu.com/api/trans/product/index) (in Chinese).


##Installation

	pip install bdtranslate

##Usage

```
import bdtranslate

yourAppId = '20170221000039563'
yourSecret = 'nIyk6j2N4pOIc3PpE9tY'

print dbtranslate.translate(yourAppId, yourSecret, "en", "zh", "The president refuses to laugh out loud. Interesting!")

```
Output: 
总统拒绝大声笑。很有趣！


##language arguments
<div>
<table class="info-table">
<tbody><tr>
<th>code</th>
<th>Language</th>
</tr>
<tr>
<td>auto</td>
<td>自动检测 - Auto-detection</td>
</tr>
<tr>
<td>zh</td>
<td>中文 - Mandarin Chinese</td>
</tr>
<tr>
<td>cht</td>
<td>繁体中文 - Mandarin Chinese (Traditional)</td>
</tr>
<tr>
<td>en</td>
<td>英语 - English</td>
</tr>
<tr>
<td>yue</td>
<td>粤语 - Cantonese</td>
</tr>
<tr>
<td>wyw</td>
<td>文言文 - Classical Chinese</td>
</tr>
<tr>
<td>jp</td>
<td>日语 - Japanese</td>
</tr>
<tr>
<td>kor</td>
<td>韩语 - Korean</td>
</tr>
<tr>
<td>fra</td>
<td>法语 - French</td>
</tr>
<tr>
<td>spa</td>
<td>西班牙语 -  Spanish</td>
</tr>
<tr>
<td>th</td>
<td>泰语 - Thai</td>
</tr>
<tr>
<td>ara</td>
<td>阿拉伯语 - Arabic</td>
</tr>
<tr>
<td>ru</td>
<td>俄语 - Russian</td>
</tr>
<tr>
<td>pt</td>
<td>葡萄牙语 - Portuguese</td>
</tr>
<tr>
<td>de</td>
<td>德语 - German</td>
</tr>
<tr>
<td>it</td>
<td>意大利语 - Italian</td>
</tr>
<tr>
<td>el</td>
<td>希腊语 - Greek</td>
</tr>
<tr>
<td>nl</td>
<td>荷兰语 - Dutch</td>
</tr>
<tr>
<td>pl</td>
<td>波兰语 - Polish</td>
</tr>
<tr>
<td>bul</td>
<td>保加利亚语 - Bulgarian</td>
</tr>
<tr>
<td>est</td>
<td>爱沙尼亚语 - Estonian</td>
</tr>
<tr>
<td>dan</td>
<td>丹麦语 - Danish</td>
</tr>
<tr>
<td>fin</td>
<td>芬兰语 - Finish</td>
</tr>
<tr>
<td>cs</td>
<td>捷克语 - Czech</td>
</tr>
<tr>
<td>rom</td>
<td>罗马尼亚语 - Romanian</td>
</tr>
<tr>
<td>slo</td>
<td>斯洛文尼亚语 - Slovenian</td>
</tr>
<tr>
<td>swe</td>
<td>瑞典语 - Swedish</td>
</tr>
<tr>
<td>hu</td>
<td>匈牙利语 -  Hungarian</td>
</tr>
</tbody></table>
</div>


##Lisense
MIT


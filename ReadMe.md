使用了python+selenium+unittest
 =====
V1:登录、搜索功能已完成

V2:登录、搜索全局化、自动化测试框架的搭建

V3:发送报告功能已完成

V4:添加日志记录功能

V5:修改登录、搜索将初始登录提取出来

V6:对登录的异常情况、搜索进行添加

V7:增加截图，针对网页和弹窗分别截图。增加发送邮件模块

globalparam.py 修改

到目前为止，感觉还有很多要做的，比如对selenium进行二次封装，这个框也是在从其他人的代码中学到的，稍微改动了一部分改成自身风格的

环境搭建配置
Python 3.6.5
selenium 3.11.0
requests 2.18.4

##注意：
此处拉下来后，要在report建立一个log文件夹，不然找不到路径

selenium提供了三种模式的断言：assert,verify,waitfor
    Assert：失败时，该测试将终止
    Verify：失败时，该测试继续执行，并将错误日志记录在日显示屏
    Waitfor：等待某些条件变为真，一般使用在AJAX应用程序的测试


断言常用的有，具体见如下：
assertLocation：判断当前是在正确的页面
assertTitle：检查当前页面的title是否正确
assertValue：检查input的值，check or radio，有为on，无为off
assertSelected：检查select的下拉菜单中选中是否正确
assertSelectedOptions：检查下拉菜单中的A选项是否正确
asserttext：检查指定元素的文本
assertTextParset：检查在当前给用户显示的页面上是否具有出现指定的文本
asserttextNotPresent：检查在当前给用户显示的页面上是否没有出现指定的文本
assertAttribute：检查当前指定元素的属性的值
assertTable：检查table里的某个cell中的值
assertEditable：检查指定的input是否可以编辑
assertNotEditable：检查指定的input是否不可以编辑
assertAlert：检查是否有产生带指定message的alert对话框
verifyTitle：验证预期的页面标题
verifyTextPresent：验证预期的文本是否在页面上的某个位置
verifyElementPresent：验证预期的UI元素，它的html标签的定义，是否在当前网页上
verifyText：核实预期的文本和相应的HTML标签是否都存在于页面上
verifyTable：验证表的预期内容
waitForPageToLoad：暂停执行，直到预期的新的页面加载
waitForElementPresent：等待检验某元素的存在，为真时，则执行

# 封装显示等待
"""
WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
driver：浏览器驱动    timeout：最长超时时间，默认以秒为单位
poll_frequency：检测的时隔步长(在2中表示调用until或until_not中方法的间隔时间），默认是0.5s
ignored_exceptions:超时后的抛出的异常信息，默认抛出NoSuchException信息。

与until()或者until_not()方法结合使用
WebDriverWait(driver,10).until(method,message="") 调用该方法提供的驱动程序作为参数，直到返回为True
WebDriverWait(driver,10).until_not(method,message="") 调用该方法提供的驱动程序作为参数，直到返回为False
在设置时间10s内，等待后面的条件发生。如果超时设置时间未发生，则抛出异常。
method：在等待时间，每隔一段时间（__init__中的poll_frequency）调用until或until_not里的方法，知道它返回True或False。
调用message: 如果超时，抛出TimeoutException，将message传入异常

WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)
"""


class WebDriverWait:
    def WebDriverWait(self):
        pass

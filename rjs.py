import uiautomator2 as u2
d = u2.connect_usb('b43052abe230')

print(d.info)
print(d.session)
#!/usr/bin/python
# -*- coding: utf-8 -*-
# example fo file url
files = [
    'https://dystonia.wustl.edu/DYS1001_20170222/DYS1001_20170222.mp4',
    'https://dystonia.wustl.edu/DYS1002_20121219/DYS1002_20121219.mp4',
    'https://dystonia.wustl.edu/DYS1003_20170322/DYS1003_20170322.mp4',
    'https://dystonia.wustl.edu/DYS1004_20130109/DYS1004_20130109.mp4',
    'https://dystonia.wustl.edu/DYS1007_20121213/DYS1007_20121213.mp4',
    'https://dystonia.wustl.edu/DYS1009_20121212/DYS1009_20121212.mp4',
    'https://dystonia.wustl.edu/DYS1018_20121219/DYS1018_20121219.mp4',
    'https://dystonia.wustl.edu/DYS1020_20130110/DYS1020_20130110.mp4',
    'https://dystonia.wustl.edu/DYS1025_20130102/DYS1025_20130102.mp4',
    'https://dystonia.wustl.edu/DYS1026_20121203/DYS1026_20121203.mp4',
    'https://dystonia.wustl.edu/DYS1040_20150311/DYS1040_20150311.mp4',
    'https://dystonia.wustl.edu/DYS1050_20130114/DYS1050_20130114.mp4',
    'https://dystonia.wustl.edu/DYS1053_20180207/DYS1053_20180207.mp4',
    'https://dystonia.wustl.edu/DYS1057_20130117/DYS1057_20130117.mp4',
    'https://dystonia.wustl.edu/DYS1060_20130117/DYS1060_20130117.mp4',
    'https://dystonia.wustl.edu/DYS1074_20130206/DYS1074_20130206.mp4',
    'https://dystonia.wustl.edu/DYS1078_20130205/DYS1078_20130205.mp4',
    'https://dystonia.wustl.edu/DYS1088_20130212/DYS1088_20130212.mp4',
    'https://dystonia.wustl.edu/DYS1090_20130211/DYS1090_20130211.mp4',
    'https://dystonia.wustl.edu/DYS1098_20130128/DYS1098_20130128.mp4',
    'https://dystonia.wustl.edu/DYS1100_20130107/DYS1100_20130107.mp4',
    'https://dystonia.wustl.edu/DYS 1101_20150706/DYS 1101_20150706.mp4'
        ,
    'https://dystonia.wustl.edu/DYS1102_20121210/DYS1102_20121210.mp4',
    'https://dystonia.wustl.edu/DYS1107_20170320/DYS1107_20170320.mp4',
    'https://dystonia.wustl.edu/DYS1111_20160428/DYS1111_20160428.mp4',
    'https://dystonia.wustl.edu/DYS1128_20130220/DYS1128_20130220.mp4',
    'https://dystonia.wustl.edu/DYS1141_20130314/DYS1141_20130314.mp4',
    'https://dystonia.wustl.edu/DYS1143_20130314/DYS1143_20130314.mp4',
    'https://dystonia.wustl.edu/DYS1147_20150309/DYS1147_20150309.mp4',
    'https://dystonia.wustl.edu/DYS1152_20130326/DYS1152_20130326.mp4',
    'https://dystonia.wustl.edu/DYS1161_20200127/DYS1161_20200127.mp4',
    'https://dystonia.wustl.edu/DYS1187_20130422/DYS1187_20130422.mp4',
    'https://dystonia.wustl.edu/DYS1196_20130429/DYS1196_20130429.mp4',
    'https://dystonia.wustl.edu/DYS1199_20130612/DYS1199_20130612.mp4',
    'https://dystonia.wustl.edu/DYS1214_20130605/DYS1214_20130605.mp4',
    'https://dystonia.wustl.edu/DYS1232_20130515/DYS1232_20130515.mp4',
    'https://dystonia.wustl.edu/DYS1233_20130516/DYS1233_20130516.mp4',
    'https://dystonia.wustl.edu/DYS1242_20160519/DYS1242_20160519.mp4',
    'https://dystonia.wustl.edu/DYS1245_20130605/DYS1245_20130605.mp4',
    'https://dystonia.wustl.edu/DYS1250_20140423/DYS1250_20140423.mp4',
    'https://dystonia.wustl.edu/DYS1254_20150903/DYS1254_20150903.mp4',
    'https://dystonia.wustl.edu/DYS1257_20140206/DYS1257_20140206.mp4',
    'https://dystonia.wustl.edu/DYS1261_20130610/DYS1261_20130610.mp4',
    'https://dystonia.wustl.edu/DYS1263_20130610/DYS1263_20130610.mp4',
    'https://dystonia.wustl.edu/DYS1265_20180329/DYS1265_20180329.mp4',
    'https://dystonia.wustl.edu/DYS1266_20130610/DYS1266_20130610.mp4',
    'https://dystonia.wustl.edu/DYS1267_20130611/DYS1267_20130611.mp4',
    'https://dystonia.wustl.edu/DYS1269_20130612/DYS1269_20130612.mp4',
    'https://dystonia.wustl.edu/DYS1270_20130523/DYS1270_20130523.mp4',
    'https://dystonia.wustl.edu/DYS1275_20130617/DYS1275_20130617.mp4',
    'https://dystonia.wustl.edu/DYS1277_20130617/DYS1277_20130617.mp4',
    'https://dystonia.wustl.edu/DYS128_20141008/DYS128_20141008.mp4',
    'https://dystonia.wustl.edu/DYS1280_20130225/DYS1280_20130225.mp4',
    'https://dystonia.wustl.edu/DYS1281_20130729/DYS1281_20130729.mp4',
    'https://dystonia.wustl.edu/DYS1282_20150518/DYS1282_20150518.mp4',
    'https://dystonia.wustl.edu/DYS1285_20130325/DYS1285_20130325.mp4',
    'https://dystonia.wustl.edu/DYS1286_20150713/DYS1286_20150713.mp4',
    'https://dystonia.wustl.edu/DYS1287_20150116/DYS1287_20150116.mp4',
    'https://dystonia.wustl.edu/DYS1291_20130525/DYS1291_20130525.mp4',
    'https://dystonia.wustl.edu/DYS1293_20130724/DYS1293_20130724.mp4',
    'https://dystonia.wustl.edu/DYS1298_20130701/DYS1298_20130701.mp4',
    'https://dystonia.wustl.edu/DYS1300_20140715/DYS1300_20140715.mp4',
    'https://dystonia.wustl.edu/DYS1337_20130723/DYS1337_20130723.mp4',
    'https://dystonia.wustl.edu/DYS1341_20130726/DYS1341_20130726.mp4',
    'https://dystonia.wustl.edu/DYS1344_20130731/DYS1344_20130731.mp4',
    'https://dystonia.wustl.edu/DYS1359_20130815/DYS1359_20130815.mp4',
    'https://dystonia.wustl.edu/DYS1367_20130820/DYS1367_20130820.mp4',
    'https://dystonia.wustl.edu/DYS1370_20171128/DYS1370_20171128.mp4',
    'https://dystonia.wustl.edu/DYS1377_20130821/DYS1377_20130821.mp4',
    'https://dystonia.wustl.edu/DYS1379_20130823/DYS1379_20130823.mp4',
    'https://dystonia.wustl.edu/DYS1380_20191030/DYS1380_20191030.mp4',
    'https://dystonia.wustl.edu/DYS1381_20130823/DYS1381_20130823.mp4',
    'https://dystonia.wustl.edu/DYS1382_20130824/DYS1382_20130824.mp4',
    'https://dystonia.wustl.edu/DYS1383_20130826/DYS1383_20130826.mp4',
    'https://dystonia.wustl.edu/DYS1400_20141030/DYS1400_20141030.mp4',
    'https://dystonia.wustl.edu/DYS1404_20130905/DYS1404_20130905.mp4',
    'https://dystonia.wustl.edu/DYS1405_20131022/DYS1405_20131022.mp4',
    'https://dystonia.wustl.edu/DYS1412_20130911/DYS1412_20130911.mp4',
    'https://dystonia.wustl.edu/DYS1413_20130911/DYS1413_20130911.mp4',
    'https://dystonia.wustl.edu/DYS1414_20130912/DYS1414_20130912.mp4',
    'https://dystonia.wustl.edu/DYS1417_20130916/DYS1417_20130916.mp4',
    'https://dystonia.wustl.edu/DYS1419_20130918/DYS1419_20130918.mp4',
    'https://dystonia.wustl.edu/DYS1421_20130916/DYS1421_20130916.mp4',
    'https://dystonia.wustl.edu/DYS1424_20130926/DYS1424_20130926.mp4',
    'https://dystonia.wustl.edu/DYS1428_20130924/DYS1428_20130924.mp4',
    'https://dystonia.wustl.edu/DYS1441_20131002/DYS1441_20131002.mp4',
    'https://dystonia.wustl.edu/DYS1447_20131007/DYS1447_20131007.mp4',
    'https://dystonia.wustl.edu/DYS1452_20131009/DYS1452_20131009.mp4',
    'https://dystonia.wustl.edu/DYS1455_20131010/DYS1455_20131010.mp4',
    'https://dystonia.wustl.edu/DYS1464_20140116/DYS1464_20140116.mp4',
    'https://dystonia.wustl.edu/DYS1465_20131017/DYS1465_20131017.mp4',
    'https://dystonia.wustl.edu/DYS1468_20131019/DYS1468_20131019.mp4',
    'https://dystonia.wustl.edu/DYS1479_20150709/DYS1479_20150709.mp4',
    'https://dystonia.wustl.edu/DYS1481_20141016/DYS1481_20141016.mp4',
    'https://dystonia.wustl.edu/DYS1484_20190617/DYS1484_20190617.mp4',
    'https://dystonia.wustl.edu/DYS1486_20131022/DYS1486_20131022.mp4',
    'https://dystonia.wustl.edu/DYS1518_20131104/DYS1518_20131104.mp4',
    'https://dystonia.wustl.edu/DYS1519_20131104/DYS1519_20131104.mp4',
    'https://dystonia.wustl.edu/DYS1522_20131105/DYS1522_20131105.mp4',
    'https://dystonia.wustl.edu/DYS1526_20131107/DYS1526_20131107.mp4',
    'https://dystonia.wustl.edu/DYS1533_20131114/DYS1533_20131114.mp4',
    'https://dystonia.wustl.edu/DYS1535_20131114/DYS1535_20131114.mp4',
    'https://dystonia.wustl.edu/DYS1542_20131118/DYS1542_20131118.mp4',
    'https://dystonia.wustl.edu/DYS1544_20131119/DYS1544_20131119.mp4',
    'https://dystonia.wustl.edu/DYS1546_20131204/DYS1546_20131204.mp4',
    'https://dystonia.wustl.edu/DYS1548_20160427/DYS1548_20160427.mp4',
    'https://dystonia.wustl.edu/DYS1553_20131120/DYS1553_20131120.mp4',
    'https://dystonia.wustl.edu/DYS1555_20131122/DYS1555_20131122.mp4',
    'https://dystonia.wustl.edu/DYS1559_20131122/DYS1559_20131122.mp4',
    'https://dystonia.wustl.edu/DYS1560_20131122/DYS1560_20131122.mp4',
    'https://dystonia.wustl.edu/DYS1561_20131127/DYS1561_20131127.mp4',
    'https://dystonia.wustl.edu/DYS1563_20131204/DYS1563_20131204.mp4',
    'https://dystonia.wustl.edu/DYS1565_20131122/DYS1565_20131122.mp4',
    'https://dystonia.wustl.edu/DYS1566_20131120/DYS1566_20131120.mp4',
    'https://dystonia.wustl.edu/DYS1572_20161214/DYS1572_20161214.mp4',
    'https://dystonia.wustl.edu/DYS1573_20131205/DYS1573_20131205.mp4',
    'https://dystonia.wustl.edu/DYS1576_20131211/DYS1576_20131211.mp4',
    'https://dystonia.wustl.edu/DYS1593_20131219/DYS1593_20131219.mp4',
    'https://dystonia.wustl.edu/DYS1602_20131230/DYS1602_20131230.mp4',
    'https://dystonia.wustl.edu/DYS1605_20140108/DYS1605_20140108.mp4',
    'https://dystonia.wustl.edu/DYS1610_20140410/DYS1610_20140410.mp4',
    'https://dystonia.wustl.edu/DYS1616_20140212/DYS1616_20140212.mp4',
    'https://dystonia.wustl.edu/DYS1620_20140116/DYS1620_20140116.mp4',
    'https://dystonia.wustl.edu/DYS1633_20140123/DYS1633_20140123.mp4',
    'https://dystonia.wustl.edu/DYS1638_20140128/DYS1638_20140128.mp4',
    'https://dystonia.wustl.edu/DYS1640_20140130/DYS1640_20140130.mp4',
    'https://dystonia.wustl.edu/DYS1642_20140130/DYS1642_20140130.mp4',
    'https://dystonia.wustl.edu/DYS166_20171122/DYS166_20171122.mp4',
    'https://dystonia.wustl.edu/DYS1665_20140218/DYS1665_20140218.mp4',
    'https://dystonia.wustl.edu/DYS1678_20140225/DYS1678_20140225.mp4',
    'https://dystonia.wustl.edu/DYS1687_20190529/DYS1687_20190529.mp4',
    'https://dystonia.wustl.edu/DYS1693_20140305/DYS1693_20140305.mp4',
    'https://dystonia.wustl.edu/DYS1698_20140306/DYS1698_20140306.mp4',
    'https://dystonia.wustl.edu/DYS1700_20140314/DYS1700_20140314.mp4',
    'https://dystonia.wustl.edu/DYS1709_20150625/DYS1709_20150625.mp4',
    'https://dystonia.wustl.edu/DYS1710_20140313/DYS1710_20140313.mp4',
    'https://dystonia.wustl.edu/DYS1721_20191011/DYS1721_20191011.mp4',
    'https://dystonia.wustl.edu/DYS1727_20140325/DYS1727_20140325.mp4',
    'https://dystonia.wustl.edu/DYS1730_20180718/DYS1730_20180718.mp4',
    'https://dystonia.wustl.edu/DYS1747_20140403/DYS1747_20140403.mp4',
    'https://dystonia.wustl.edu/DYS1750_20140407/DYS1750_20140407.mp4',
    'https://dystonia.wustl.edu/DYS1751_20140407/DYS1751_20140407.mp4',
    'https://dystonia.wustl.edu/DYS1770_20140414/DYS1770_20140414.mp4',
    'https://dystonia.wustl.edu/DYS179_20171018/DYS179_20171018.mp4',
    'https://dystonia.wustl.edu/DYS1792_20140523/DYS1792_20140523.mp4',
    'https://dystonia.wustl.edu/DYS1807_20140502/DYS1807_20140502.mp4',
    'https://dystonia.wustl.edu/DYS1820_20140513/DYS1820_20140513.mp4',
    'https://dystonia.wustl.edu/DYS1821_20140513/DYS1821_20140513.mp4',
    'https://dystonia.wustl.edu/DYS1828_20140514/DYS1828_20140514.mp4',
    'https://dystonia.wustl.edu/DYS1833_20140515/DYS1833_20140515.mp4',
    'https://dystonia.wustl.edu/DYS1834_20140516/DYS1834_20140516.mp4',
    'https://dystonia.wustl.edu/DYS1835_20140516/DYS1835_20140516.mp4',
    'https://dystonia.wustl.edu/DYS1836_20140519/DYS1836_20140519.mp4',
    'https://dystonia.wustl.edu/DYS1848_20140521/DYS1848_20140521.mp4',
    'https://dystonia.wustl.edu/DYS1854_20150721/DYS1854_20150721.mp4',
    'https://dystonia.wustl.edu/DYS1855_20140716/DYS1855_20140716.mp4',
    'https://dystonia.wustl.edu/DYS1857_20170406/DYS1857_20170406.mp4',
    'https://dystonia.wustl.edu/DYS1865_20140529/DYS1865_20140529.mp4',
    'https://dystonia.wustl.edu/DYS1868_20140529/DYS1868_20140529.mp4',
    'https://dystonia.wustl.edu/DYS1873_20180718/DYS1873_20180718.mp4',
    'https://dystonia.wustl.edu/DYS1880_20140616/DYS1880_20140616.mp4',
    'https://dystonia.wustl.edu/DYS1942_20180404/DYS1942_20180404.mp4',
    'https://dystonia.wustl.edu/DYS1959_20140903/DYS1959_20140903.mp4',
    'https://dystonia.wustl.edu/DYS1969_20140909/DYS1969_20140909.mp4',
    'https://dystonia.wustl.edu/DYS1984_20140916/DYS1984_20140916.mp4',
    'https://dystonia.wustl.edu/DYS1990_20141001/DYS1990_20141001.mp4',
    'https://dystonia.wustl.edu/DYS2006_20140921/DYS2006_20140921.mp4',
    'https://dystonia.wustl.edu/DYS2009_20180115/DYS2009_20180115.mp4',
    'https://dystonia.wustl.edu/DYS201_20190717/DYS201_20190717.mp4',
    'https://dystonia.wustl.edu/DYS2015_20140930/DYS2015_20140930.mp4',
    'https://dystonia.wustl.edu/DYS2020_20141007/DYS2020_20141007.mp4',
    'https://dystonia.wustl.edu/DYS2045_20141028/DYS2045_20141028.mp4',
    'https://dystonia.wustl.edu/DYS2067_20141118/DYS2067_20141118.mp4',
    'https://dystonia.wustl.edu/DYS2072_20141217/DYS2072_20141217.mp4',
    'https://dystonia.wustl.edu/DYS2074_20141121/DYS2074_20141121.mp4',
    'https://dystonia.wustl.edu/DYS2076_20141121/DYS2076_20141121.mp4',
    'https://dystonia.wustl.edu/DYS2077_20141124/DYS2077_20141124.mp4',
    'https://dystonia.wustl.edu/DYS2078_20141125/DYS2078_20141125.mp4',
    'https://dystonia.wustl.edu/DYS208_20160330/DYS208_20160330.mp4',
    'https://dystonia.wustl.edu/DYS2081_20141126/DYS2081_20141126.mp4',
    'https://dystonia.wustl.edu/DYS2082_20141201/DYS2082_20141201.mp4',
    'https://dystonia.wustl.edu/DYS2087_20141202/DYS2087_20141202.mp4',
    'https://dystonia.wustl.edu/DYS2092_20141205/DYS2092_20141205.mp4',
    'https://dystonia.wustl.edu/DYS2095_20141209/DYS2095_20141209.mp4',
    'https://dystonia.wustl.edu/DYS2096_20141209/DYS2096_20141209.mp4',
    'https://dystonia.wustl.edu/DYS2098_20181017/DYS2098_20181017.mp4',
    'https://dystonia.wustl.edu/DYS2102_20141216/DYS2102_20141216.mp4',
    'https://dystonia.wustl.edu/DYS2105_20160513/DYS2105_20160513.mp4',
    'https://dystonia.wustl.edu/DYS2106_20141218/DYS2106_20141218.mp4',
    'https://dystonia.wustl.edu/DYS2112_20150102/DYS2112_20150102.mp4',
    'https://dystonia.wustl.edu/DYS2115_20150106/DYS2115_20150106.mp4',
    'https://dystonia.wustl.edu/DYS2120_20150115/DYS2120_20150115.mp4',
    'https://dystonia.wustl.edu/DYS2124_20150113/DYS2124_20150113.mp4',
    'https://dystonia.wustl.edu/DYS2129_20150114/DYS2129_20150114.mp4',
    'https://dystonia.wustl.edu/DYS2136_20170413/DYS2136_20170413.mp4',
    'https://dystonia.wustl.edu/DYS2139_20150119/DYS2139_20150119.mp4',
    'https://dystonia.wustl.edu/DYS2143_20150120/DYS2143_20150120.mp4',
    'https://dystonia.wustl.edu/DYS2150_20150218/DYS2150_20150218.mp4',
    'https://dystonia.wustl.edu/DYS2163_20180125/DYS2163_20180125.mp4',
    'https://dystonia.wustl.edu/DYS2174_20150205/DYS2174_20150205.mp4',
    'https://dystonia.wustl.edu/DYS2182_20170413/DYS2182_20170413.mp4',
    'https://dystonia.wustl.edu/DYS2190_20150316/DYS2190_20150316.mp4',
    'https://dystonia.wustl.edu/DYS2191_20150225/DYS2191_20150225.mp4',
    'https://dystonia.wustl.edu/DYS2197_20150220/DYS2197_20150220.mp4',
    'https://dystonia.wustl.edu/DYS2200_20150224/DYS2200_20150224.mp4',
    'https://dystonia.wustl.edu/DYS2205_20150225/DYS2205_20150225.mp4',
    'https://dystonia.wustl.edu/DYS2206_20150226/DYS2206_20150226.mp4',
    'https://dystonia.wustl.edu/DYS2216_20150504/DYS2216_20150504.mp4',
    'https://dystonia.wustl.edu/DYS2229_20170627/DYS2229_20170627.mp4',
    'https://dystonia.wustl.edu/DYS2233_20150316/DYS2233_20150316.mp4',
    'https://dystonia.wustl.edu/DYS2234_20150316/DYS2234_20150316.mp4',
    'https://dystonia.wustl.edu/DYS2236_20170601/DYS2236_20170601.mp4',
    'https://dystonia.wustl.edu/DYS2237_20150323/DYS2237_20150323.mp4',
    'https://dystonia.wustl.edu/DYS2238_20150323/DYS2238_20150323.mp4',
    'https://dystonia.wustl.edu/DYS2239_20150323/DYS2239_20150323.mp4',
    'https://dystonia.wustl.edu/DYS2247_20150324/DYS2247_20150324.mp4',
    'https://dystonia.wustl.edu/DYS2258_20150331/DYS2258_20150331.mp4',
    'https://dystonia.wustl.edu/DYS2267_20180518/DYS2267_20180518.mp4',
    'https://dystonia.wustl.edu/DYS2268_20150415/DYS2268_20150415.mp4',
    'https://dystonia.wustl.edu/DYS2278_20150428/DYS2278_20150428.mp4',
    'https://dystonia.wustl.edu/DYS2279_20150618/DYS2279_20150618.mp4',
    'https://dystonia.wustl.edu/DYS2287_20170511/DYS2287_20170511.mp4',
    'https://dystonia.wustl.edu/DYS2303_20190128/DYS2303_20190128.mp4',
    'https://dystonia.wustl.edu/DYS2306_20150522/DYS2306_20150522.mp4',
    'https://dystonia.wustl.edu/DYS2307_20150526/DYS2307_20150526.mp4',
    'https://dystonia.wustl.edu/DYS2310_20150526/DYS2310_20150526.mp4',
    'https://dystonia.wustl.edu/DYS2313_20150527/DYS2313_20150527.mp4',
    'https://dystonia.wustl.edu/DYS2320_20150608/DYS2320_20150608.mp4',
    'https://dystonia.wustl.edu/DYS233_20160120/DYS233_20160120.mp4',
    'https://dystonia.wustl.edu/DYS2335_20150615/DYS2335_20150615.mp4',
    'https://dystonia.wustl.edu/DYS2337_20150616/DYS2337_20150616.mp4',
    'https://dystonia.wustl.edu/DYS2340_20150617/DYS2340_20150617.mp4',
    'https://dystonia.wustl.edu/DYS2342_20150619/DYS2342_20150619.mp4',
    'https://dystonia.wustl.edu/DYS2344 20150624/DYS2344 20150624.mp4',
    'https://dystonia.wustl.edu/DYS2348_20150625/DYS2348_20150625.mp4',
    'https://dystonia.wustl.edu/DYS2353_20150630/DYS2353_20150630.mp4',
    'https://dystonia.wustl.edu/DYS2354_20171220/DYS2354_20171220.mp4',
    'https://dystonia.wustl.edu/DYS2356_20150706/DYS2356_20150706.mp4',
    'https://dystonia.wustl.edu/DYS2359_20170313/DYS2359_20170313.mp4',
    'https://dystonia.wustl.edu/DYS2369_20150728/DYS2369_20150728.mp4',
    'https://dystonia.wustl.edu/DYS2370_20150728/DYS2370_20150728.mp4',
    'https://dystonia.wustl.edu/DYS2378_20151021/DYS2378_20151021.mp4',
    'https://dystonia.wustl.edu/DYS2387_20150825/DYS2387_20150825.mp4',
    'https://dystonia.wustl.edu/DYS2393_20150831/DYS2393_20150831.mp4',
    'https://dystonia.wustl.edu/DYS2407_20150929/DYS2407_20150929.mp4',
    'https://dystonia.wustl.edu/DYS2414_20151012/DYS2414_20151012.mp4',
    'https://dystonia.wustl.edu/DYS2415_20151012/DYS2415_20151012.mp4',
    'https://dystonia.wustl.edu/DYS2416_20151013/DYS2416_20151013.mp4',
    'https://dystonia.wustl.edu/DYS2418_20170208/DYS2418_20170208.mp4',
    'https://dystonia.wustl.edu/DYS2422_20151015/DYS2422_20151015.mp4',
    'https://dystonia.wustl.edu/DYS2423_20171222/DYS2423_20171222.mp4',
    'https://dystonia.wustl.edu/DYS2425_20151020/DYS2425_20151020.mp4',
    'https://dystonia.wustl.edu/DYS2431_20190828/DYS2431_20190828.mp4',
    'https://dystonia.wustl.edu/DYS2432_20151125/DYS2432_20151125.mp4',
    'https://dystonia.wustl.edu/DYS2450_20161013/DYS2450_20161013.mp4',
    'https://dystonia.wustl.edu/DYS2455_20151120/DYS2455_20151120.mp4',
    'https://dystonia.wustl.edu/DYS2473_20151210/DYS2473_20151210.mp4',
    'https://dystonia.wustl.edu/DYS2480_20151216/DYS2480_20151216.mp4',
    'https://dystonia.wustl.edu/DYS2482_20151217/DYS2482_20151217.mp4',
    'https://dystonia.wustl.edu/DYS2486_20160210/DYS2486_20160210.mp4',
    'https://dystonia.wustl.edu/DYS2497_20160112/DYS2497_20160112.mp4',
    'https://dystonia.wustl.edu/DYS2498_20160111/DYS2498_20160111.mp4',
    'https://dystonia.wustl.edu/DYS2499_20160111/DYS2499_20160111.mp4',
    'https://dystonia.wustl.edu/DYS2506_20180516/DYS2506_20180516.mp4',
    'https://dystonia.wustl.edu/DYS2510_20160211/DYS2510_20160211.mp4',
    'https://dystonia.wustl.edu/DYS2515_20160128/DYS2515_20160128.mp4',
    'https://dystonia.wustl.edu/DYS2538_20160316/DYS2538_20160316.mp4',
    'https://dystonia.wustl.edu/DYS2539_20160406/DYS2539_20160406.mp4',
    'https://dystonia.wustl.edu/DYS2557_20160307/DYS2557_20160307.mp4',
    'https://dystonia.wustl.edu/DYS2567_20160322/DYS2567_20160322.mp4',
    'https://dystonia.wustl.edu/DYS2570_20160328/DYS2570_20160328.mp4',
    'https://dystonia.wustl.edu/DYS2572_20160329/DYS2572_20160329.mp4',
    'https://dystonia.wustl.edu/DYS2575_20180413/DYS2575_20180413.mp4',
    'https://dystonia.wustl.edu/DYS2576_20160406/DYS2576_20160406.mp4',
    'https://dystonia.wustl.edu/DYS2577_20160407/DYS2577_20160407.mp4',
    'https://dystonia.wustl.edu/DYS2585_20160520/DYS2585_20160520.mp4',
    'https://dystonia.wustl.edu/DYS2588_20160511/DYS2588_20160511.mp4',
    'https://dystonia.wustl.edu/DYS2591_20160516/DYS2591_20160516.mp4',
    'https://dystonia.wustl.edu/DYS2598_20160519/DYS2598_20160519.mp4',
    'https://dystonia.wustl.edu/DYS2605_20160615/DYS2605_20160615.mp4',
    'https://dystonia.wustl.edu/DYS2615_20160616/DYS2615_20160616.mp4',
    'https://dystonia.wustl.edu/DYS2629_20160715/DYS2629_20160715.mp4',
    'https://dystonia.wustl.edu/DYS263_20111215/DYS263_20111215.mp4',
    'https://dystonia.wustl.edu/DYS2635_20160728/DYS2635_20160728.mp4',
    'https://dystonia.wustl.edu/DYS2643_20160811/DYS2643_20160811.mp4',
    'https://dystonia.wustl.edu/DYS2658_20160901/DYS2658_20160901.mp4',
    'https://dystonia.wustl.edu/DYS2662_20161024/DYS2662_20161024.mp4',
    'https://dystonia.wustl.edu/DYS2672_20160928/DYS2672_20160928.mp4',
    'https://dystonia.wustl.edu/DYS2676_20161004/DYS2676_20161004.mp4',
    'https://dystonia.wustl.edu/DYS2687_20161014/DYS2687_20161014.mp4',
    'https://dystonia.wustl.edu/DYS2715_20161205/DYS2715_20161205.mp4',
    'https://dystonia.wustl.edu/DYS2723_20170104/DYS2723_20170104.mp4',
    'https://dystonia.wustl.edu/DYS2727_20161207/DYS2727_20161207.mp4',
    'https://dystonia.wustl.edu/DYS2738_20161109/DYS2738_20161109.mp4',
    'https://dystonia.wustl.edu/DYS2740_20161109/DYS2740_20161109.mp4',
    'https://dystonia.wustl.edu/DYS2741_20161102/DYS2741_20161102.mp4',
    'https://dystonia.wustl.edu/DYS2743_20161207/DYS2743_20161207.mp4',
    'https://dystonia.wustl.edu/DYS2744_20161214/DYS2744_20161214.mp4',
    'https://dystonia.wustl.edu/DYS2756_20161220/DYS2756_20161220.mp4',
    'https://dystonia.wustl.edu/DYS2760_20161221/DYS2760_20161221.mp4',
    'https://dystonia.wustl.edu/DYS2761_20161222/DYS2761_20161222.mp4',
    'https://dystonia.wustl.edu/DYS2763_20170104/DYS2763_20170104.mp4',
    'https://dystonia.wustl.edu/DYS277_20140623/DYS277_20140623.mp4',
    'https://dystonia.wustl.edu/DYS2781_20170124/DYS2781_20170124.mp4',
    'https://dystonia.wustl.edu/DYS2786_20170130/DYS2786_20170130.mp4',
    'https://dystonia.wustl.edu/DYS2795_20170208/DYS2795_20170208.mp4',
    'https://dystonia.wustl.edu/DYS2796_20170208/DYS2796_20170208.mp4',
    'https://dystonia.wustl.edu/DYS2802_20170213/DYS2802_20170213.mp4',
    'https://dystonia.wustl.edu/DYS2806_20170215/DYS2806_20170215.mp4',
    'https://dystonia.wustl.edu/DYS2811_20180130/DYS2811_20180130.mp4',
    'https://dystonia.wustl.edu/DYS2812_20180320/DYS2812_20180320.mp4',
    'https://dystonia.wustl.edu/DYS2815_20170222/DYS2815_20170222.mp4',
    'https://dystonia.wustl.edu/DYS2818_20170224/DYS2818_20170224.mp4',
    'https://dystonia.wustl.edu/DYS2825_20170228/DYS2825_20170228.mp4',
    'https://dystonia.wustl.edu/DYS2827_20170301/DYS2827_20170301.mp4',
    'https://dystonia.wustl.edu/DYS2836_20170303/DYS2836_20170303.mp4',
    'https://dystonia.wustl.edu/DYS2849_20170315/DYS2849_20170315.mp4',
    'https://dystonia.wustl.edu/DYS2850_20170315/DYS2850_20170315.mp4',
    'https://dystonia.wustl.edu/DYS2852_20170315/DYS2852_20170315.mp4',
    'https://dystonia.wustl.edu/DYS2858_20170322/DYS2858_20170322.mp4',
    'https://dystonia.wustl.edu/DYS2860_20180306/DYS2860_20180306.mp4',
    'https://dystonia.wustl.edu/DYS2868_20170330/DYS2868_20170330.mp4',
    'https://dystonia.wustl.edu/DYS2869_20170330/DYS2869_20170330.mp4',
    'https://dystonia.wustl.edu/DYS2874_20170404/DYS2874_20170404.mp4',
    'https://dystonia.wustl.edu/DYS2876_20170407/DYS2876_20170407.mp4',
    'https://dystonia.wustl.edu/DYS2890_20170420/DYS2890_20170420.mp4',
    'https://dystonia.wustl.edu/DYS2899_20170419/DYS2899_20170419.mp4',
    'https://dystonia.wustl.edu/DYS2903_20170514/DYS2903_20170514.mp4',
    'https://dystonia.wustl.edu/DYS2913_20170512/DYS2913_20170512.mp4',
    'https://dystonia.wustl.edu/DYS2923_20170518/DYS2923_20170518.mp4',
    'https://dystonia.wustl.edu/DYS2930_20170629/DYS2930_20170629.mp4',
    'https://dystonia.wustl.edu/DYS2934_20170531/DYS2934_20170531.mp4',
    'https://dystonia.wustl.edu/DYS2935_20170531/DYS2935_20170531.mp4',
    'https://dystonia.wustl.edu/DYS2943_20170605/DYS2943_20170605.mp4',
    'https://dystonia.wustl.edu/DYS2960_20170620/DYS2960_20170620.mp4',
    'https://dystonia.wustl.edu/DYS2961_20180620/DYS2961_20180620.mp4',
    'https://dystonia.wustl.edu/DYS2966_20170620/DYS2966_20170620.mp4',
    'https://dystonia.wustl.edu/DYS2981_20170628/DYS2981_20170628.mp4',
    'https://dystonia.wustl.edu/DYS2984_20170627/DYS2984_20170627.mp4',
    'https://dystonia.wustl.edu/DYS299_20170203/DYS299_20170203.mp4',
    'https://dystonia.wustl.edu/DYS2992_20170628/DYS2992_20170628.mp4',
    'https://dystonia.wustl.edu/DYS2995_20170629/DYS2995_20170629.mp4',
    'https://dystonia.wustl.edu/DYS3015_20170713/DYS3015_20170713.mp4',
    'https://dystonia.wustl.edu/DYS3025_20170823/DYS3025_20170823.mp4',
    'https://dystonia.wustl.edu/DYS3026_20171114/DYS3026_20171114.mp4',
    'https://dystonia.wustl.edu/DYS3041_20170803/DYS3041_20170803.mp4',
    'https://dystonia.wustl.edu/DYS3054_20170817/DYS3054_20170817.mp4',
    'https://dystonia.wustl.edu/DYS3056_20170817/DYS3056_20170817.mp4',
    'https://dystonia.wustl.edu/DYS3073_20170829/DYS3073_20170829.mp4',
    'https://dystonia.wustl.edu/DYS3080_20170905/DYS3080_20170905.mp4',
    'https://dystonia.wustl.edu/DYS3084_20170912/DYS3084_20170912.mp4',
    'https://dystonia.wustl.edu/DYS3088_20161215/DYS3088_20161215.mp4',
    'https://dystonia.wustl.edu/DYS309_20180207/DYS309_20180207.mp4',
    'https://dystonia.wustl.edu/DYS3091_20170911/DYS3091_20170911.mp4',
    'https://dystonia.wustl.edu/DYS3092_20170913/DYS3092_20170913.mp4',
    'https://dystonia.wustl.edu/DYS3099_20170919/DYS3099_20170919.mp4',
    'https://dystonia.wustl.edu/DYS31_20110415/DYS31_20110415.mp4',
    'https://dystonia.wustl.edu/DYS3103_20170922/DYS3103_20170922.mp4',
    'https://dystonia.wustl.edu/DYS3104_20170922/DYS3104_20170922.mp4',
    'https://dystonia.wustl.edu/DYS311_20120126/DYS311_20120126.mp4',
    'https://dystonia.wustl.edu/DYS3111_20170926/DYS3111_20170926.mp4',
    'https://dystonia.wustl.edu/DYS313_20161005/DYS313_20161005.mp4',
    'https://dystonia.wustl.edu/DYS3135_20171005/DYS3135_20171005.mp4',
    'https://dystonia.wustl.edu/DYS3142_20171013/DYS3142_20171013.mp4',
    'https://dystonia.wustl.edu/DYS3173_20171106/DYS3173_20171106.mp4',
    'https://dystonia.wustl.edu/DYS3188_20171113/DYS3188_20171113.mp4',
    'https://dystonia.wustl.edu/DYS3189_20171115/DYS3189_20171115.mp4',
    'https://dystonia.wustl.edu/DYS3194_20171120/DYS3194_20171120.mp4',
    'https://dystonia.wustl.edu/DYS3203_20171206/DYS3203_20171206.mp4',
    'https://dystonia.wustl.edu/DYS3205_20171201/DYS3205_20171201.mp4',
    'https://dystonia.wustl.edu/DYS321_20120112/DYS321_20120112.mp4',
    'https://dystonia.wustl.edu/DYS3218_20171208/DYS3218_20171208.mp4',
    'https://dystonia.wustl.edu/DYS322_20120119/DYS322_20120119.mp4',
    'https://dystonia.wustl.edu/DYS3223_20171218/DYS3223_20171218.mp4',
    'https://dystonia.wustl.edu/DYS327_20120208/DYS327_20120208.mp4',
    'https://dystonia.wustl.edu/DYS3273_20180416/DYS3273_20180416.mp4',
    'https://dystonia.wustl.edu/DYS3281_20180329/DYS3281_20180329.mp4',
    'https://dystonia.wustl.edu/DYS3316_20180514/DYS3316_20180514.mp4',
    'https://dystonia.wustl.edu/DYS336_20180606/DYS336_20180606.mp4',
    'https://dystonia.wustl.edu/DYS340_20171220/DYS340_20171220.mp4',
    'https://dystonia.wustl.edu/DYS342_20160629/DYS342_20160629.mp4',
    'https://dystonia.wustl.edu/DYS345_20120217/DYS345_20120217.mp4',
    'https://dystonia.wustl.edu/DYS347_20180411/DYS347_20180411.mp4',
    'https://dystonia.wustl.edu/DYS348_20121011/DYS348_20121011.mp4',
    'https://dystonia.wustl.edu/DYS3494_20190121/DYS3494_20190121.mp4',
    'https://dystonia.wustl.edu/DYS3495_20190121/DYS3495_20190121.mp4',
    'https://dystonia.wustl.edu/DYS3497_20190122/DYS3497_20190122.mp4',
    'https://dystonia.wustl.edu/DYS355_20120229/DYS355_20120229.mp4',
    'https://dystonia.wustl.edu/DYS36_20170510/DYS36_20170510.mp4',
    'https://dystonia.wustl.edu/DYS363_20120307/DYS363_20120307.mp4',
    'https://dystonia.wustl.edu/DYS394_03202012/DYS394_03202012.mp4',
    'https://dystonia.wustl.edu/DYS41_20170412/DYS41_20170412.mp4',
    'https://dystonia.wustl.edu/DYS414_20120328/DYS414_20120328.mp4',
    'https://dystonia.wustl.edu/DYS456_20120413/DYS456_20120413.mp4',
    'https://dystonia.wustl.edu/DYS46_20160629/DYS46_20160629.mp4',
    'https://dystonia.wustl.edu/DYS474_20120418/DYS474_20120418.mp4',
    'https://dystonia.wustl.edu/DYS479_20120419/DYS479_20120419.mp4',
    'https://dystonia.wustl.edu/DYS48_20120808/DYS48_20120808.mp4',
    'https://dystonia.wustl.edu/DYS49_20151022/DYS49_20151022.mp4',
    'https://dystonia.wustl.edu/DYS504_20120508/DYS504_20120508.mp4',
    'https://dystonia.wustl.edu/DYS533_20120517/DYS533_20120517.mp4',
    'https://dystonia.wustl.edu/DYS560_20120524/DYS560_20120524.mp4',
    'https://dystonia.wustl.edu/DYS568_20150827/DYS568_20150827.mp4',
    'https://dystonia.wustl.edu/DYS57_20170208/DYS57_20170208.mp4',
    'https://dystonia.wustl.edu/DYS585_20180615/DYS585_20180615.mp4',
    'https://dystonia.wustl.edu/DYS59_20110511/DYS59_20110511.mp4',
    'https://dystonia.wustl.edu/DYS614_20160727/DYS614_20160727.mp4',
    'https://dystonia.wustl.edu/DYS62_20171213/DYS62_20171213.mp4',
    'https://dystonia.wustl.edu/DYS63_20170920/DYS63_20170920.mp4',
    'https://dystonia.wustl.edu/DYS653_20130910/DYS653_20130910.mp4',
    'https://dystonia.wustl.edu/DYS661_20120710/DYS661_20120710.mp4',
    'https://dystonia.wustl.edu/DYS662_20120710/DYS662_20120710.mp4',
    'https://dystonia.wustl.edu/DYS669_20120712/DYS669_20120712.mp4',
    'https://dystonia.wustl.edu/DYS672_20180614/DYS672_20180614.mp4',
    'https://dystonia.wustl.edu/DYS674_20120712/DYS674_20120712.mp4',
    'https://dystonia.wustl.edu/DYS675_20130718/DYS675_20130718.mp4',
    'https://dystonia.wustl.edu/DYS676_2012717/DYS676_2012717.mp4',
    'https://dystonia.wustl.edu/DYS682_20120801/DYS682_20120801.mp4',
    'https://dystonia.wustl.edu/DYS691_ 20131220/DYS691_ 20131220.mp4',
    'https://dystonia.wustl.edu/DYS698_20120720/DYS698_20120720.mp4',
    'https://dystonia.wustl.edu/DYS708_20120725/DYS708_20120725.mp4',
    'https://dystonia.wustl.edu/DYS709_20180207/DYS709_20180207.mp4',
    'https://dystonia.wustl.edu/DYS710_20171025/DYS710_20171025.mp4',
    'https://dystonia.wustl.edu/DYS717_20120801/DYS717_20120801.mp4',
    'https://dystonia.wustl.edu/DYS727_20120803/DYS727_20120803.mp4',
    'https://dystonia.wustl.edu/DYS738_20130109/DYS738_20130109.mp4',
    'https://dystonia.wustl.edu/DYS782_20120829/DYS782_20120829.mp4',
    'https://dystonia.wustl.edu/DYS817_20140314/DYS817_20140314.mp4',
    'https://dystonia.wustl.edu/DYS9_20110127/DYS9_20110127.mp4',
    'https://dystonia.wustl.edu/DYS929_20170925/DYS929_20170925.mp4',
    'https://dystonia.wustl.edu/DYS940_20161029/DYS940_20161029.mp4',
    'https://dystonia.wustl.edu/DYS950_20120822/DYS950_20120822.mp4',
    'https://dystonia.wustl.edu/DYS988_20121203/DYS988_20121203.mp4',
    'https://dystonia.wustl.edu/DYS989_20121203/DYS989_20121203.mp4',
    'https://dystonia.wustl.edu/DYS993_20130102/DYS993_20130102.mp4',
    'https://dystonia.wustl.edu/DYS994_20121213/DYS994_20121213.mp4',
    ]


import requests
import shutil
import os


def download_file(url):
    local_filename = url.split('/')[-1]
    if os.path.exists(local_filename):
        print('\nAlready')
        return 

    print ('\nDownloading ', local_filename)
    # put your credentials here
    with requests.get(url, stream=True, auth=('username', 'password')) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
            return local_filename

for e in files:
    download_file(e)
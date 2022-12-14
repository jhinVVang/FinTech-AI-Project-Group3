-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022-12-10 10:04:59
-- 伺服器版本： 10.4.27-MariaDB
-- PHP 版本： 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `shop`
--

-- --------------------------------------------------------

--
-- 資料表結構 `goods`
--

CREATE TABLE `goods` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `original_price` decimal(10,2) DEFAULT NULL,
  `current_price` decimal(10,2) DEFAULT NULL,
  `picture` varchar(255) DEFAULT NULL,
  `introduction` text DEFAULT NULL,
  `is_sale` tinyint(1) DEFAULT NULL,
  `is_new` tinyint(1) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `views_count` int(11) DEFAULT NULL,
  `subcat_id` int(11) DEFAULT NULL,
  `supercat_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 傾印資料表的資料 `goods`
--

INSERT INTO `goods` (`id`, `name`, `original_price`, `current_price`, `picture`, `introduction`, `is_sale`, `is_new`, `addtime`, `views_count`, `subcat_id`, `supercat_id`) VALUES
(2, 'RW0520公主方形鑽石戒指', '6520.00', '5868.00', '1.jpg', '優雅、復古又具現代風，公主方形切割鑽石戒指是有一顆方形主鑽，鑽石的四角均為 90 度。通常被稱為方形鑽石訂婚戒指，此形狀是異形鑽中最受歡迎的鑽石形狀。\r\n這款完美無暇的鑽石戒指鑲有多顆法式密釘鑲鑽石，與您所選擇的主鑽作完美配襯，讓人移不開視線。', 1, 0, '2016-07-20 09:58:53', 20, 27, 14),
(3, 'RW0636 圓鑽婚戒', '18000.00', '16200.00', '2.jpg', 'Princess 20分浪漫公主款式，外圈小鑽細緻包覆，復古設計卻不失低調優雅，屬於小公主般的華麗冒險。', 1, 0, '2016-07-20 10:10:38', 12, 28, 14),
(4, 'RW0704 鑽石線戒', '20000.00', '18000.00', '3.jpg', '18K金戒指鑲嵌天然鑽石，在簡單中營造獨特，閃耀指間，皆能表現出最耀眼品味。', 1, 0, '2016-07-20 10:12:00', 0, 31, 14),
(5, 'RW0637 鑽石線戒', '16500.00', '14850.00', '4.jpg', 'Princess 30分浪漫公主款式，外圈小鑽細緻包覆，復古設計卻不失低調優雅，屬於小公主般的華麗冒險。', 1, 0, '2016-07-20 10:13:06', 3, 28, 14),
(6, 'RW0310交織圈戒指', '6800.00', '6120.00', '5.jpg', '鑽石採用時尚的混合切割方式，將階梯式切割的冠部與明亮式切割的底部相結合。', 1, 0, '2016-07-20 10:14:24', 9, 30, 14),
(7, 'RW0312風格戒指', '5800.00', '5220.00', '6.jpg', '鑽石採用時尚的混合切割方式，將階梯式切割的冠部與明亮式切割的底部相結合。', 1, 0, '2016-07-20 10:18:19', 1, 30, 14),
(8, 'RW0233梨形水鑽', '38000.00', '34200.00', '7.jpg', '梨形切割融合圓形明亮式切割與欖尖形切割風格，創造出逐漸收細的流線水滴形狀，展示出非凡光線。就如橢圓形和欖尖形鑽石那般，令人更顯美態的梨形鑽石亦會讓手指顯得更修長，尤其在採用將尖端指向指甲的佩戴方式時。梨形鑽石展現出精準的對稱，與光環鑲嵌方式配合時尤為美麗。', 1, 1, '2016-07-20 10:20:10', 2, 29, 14),
(9, 'RW0110花型鑽戒', '66800.00', '60120.00', '8.jpg', '採用時尚的混合切割方式，將階梯式切割的冠部與明亮式切割的底部相結合。十分適合追求富現代感訂情戒指款式之人，它呈現出明亮強烈的白色反光，並巧妙地與彩虹及光線移動取得平衡。', 1, 0, '2016-07-20 10:24:51', 0, 32, 14),
(10, 'RW0522法式密釘公主方鑽戒指', '36.80', '42650.00', '9.jpg', '這款觸動人心的訂婚鑽戒配有兩圈相互交融的戒指，象徵著兩人的邂逅相遇。 一圈是光滑的鉑金，另一圈是精緻的密釘鑲鑽。 在戒指中央，一顆公主方形切割美鑽鑲嵌於這兩圈並立的戒指上，盡顯璀然亮光。 這款經典之作上選用的所有鑽石都以遵循道德章程的方式採購，並悉心手工鑲嵌。 與結婚戒指搭配亦華美絕倫。', 1, 0, '2016-07-20 10:26:06', 0, 28, 14),
(11, 'RW0655圓鑽鑽戒', '35000.00', '31500.00', '10.jpg', 'Princess 20分浪漫公主款式，外圈小鑽細緻包覆，復古設計卻不失低調優雅，屬於小公主般的華麗冒險。', 1, 0, '2016-07-20 10:27:22', 0, 28, 14),
(12, 'RW0115璀璨紫鑽', '46800.00', '42120.00', '11.jpg', '璀璨的珠式鑲嵌鑽石閃爍的光環加上令人心動、切工精巧的橢圓形主寶石，整個設計各處都集聚著光芒，映照出無與倫比的閃耀光輝。橢圓形主鑽本身就引人矚目，加上一行鑽石使之更顯高貴美麗。', 1, 0, '2016-07-20 10:29:44', 0, 30, 14),
(13, 'RW0366簡約線鑽', '25000.00', '22500.00', '12.jpg', '鑽石採用時尚的混合切割方式，將階梯式切割的冠部與明亮式切割的底部相結合。', 1, 0, '2016-07-20 10:31:56', 0, 31, 14),
(14, 'RW0345簡約對戒', '85800.00', '77220.00', '13.jpg', '鑽石採用時尚的混合切割方式，將階梯式切割的冠部與明亮式切割的底部相結合。', 1, 0, '2016-07-20 10:34:32', 1, 31, 14),
(15, 'RW0128花形線戒', '8800.00', '7920.00', '14.jpg', '18K金戒指鑲嵌天然鑽石，在簡單中營造獨特，閃耀指間，皆能表現出最耀眼品味。', 1, 0, '2016-07-20 10:39:48', 1, 32, 14),
(16, 'RW0318白金對戒', '38500.00', '34650.00', '15.jpg', '鑽石採用時尚的混合切割方式，將階梯式切割的冠部與明亮式切割的底部相結合。18K金戒指鑲嵌天然鑽石，在簡單中營造獨特，閃耀指間，皆能表現出最耀眼品味。', 1, 0, '2016-07-20 10:40:43', 0, 31, 14),
(17, 'KA6211個性鏈墜', '8800.00', '7920.00', '16.jpg', '優雅革命，展現紐約市女力特質。這款項鏈兼具優雅與桀驁不馴風格。', 1, 0, '2016-07-20 10:43:27', 0, 33, 15),
(18, 'KA6022復古方鑽', '23600.00', '21240.00', '17.jpg', '10K金鑽石項鍊，使用精緻優質的鑽石，優美細膩的設計，最適合送給甜美可愛的她，鑽石浪漫禮物推薦！', 1, 0, '2016-07-20 10:45:55', 0, 34, 15),
(19, 'KA6055璀璨花鏈', '7650.00', '6885.00', '18.jpg', '18K金鑽石項鍊，織入完美鑽石的燦耀火光，弧線與美鑽交錯的結合，纖膩的設計風格，點綴在胸前的燦爛星光，增添美好的每一天，象徵年輕且充滿活力的姿態。', 1, 0, '2016-07-20 10:46:55', 0, 34, 15),
(20, 'KA6012藍色眼淚', '5300.00', '4770.00', '19.jpg', '10K藍色寶石項鍊，使用精緻優質的寶石，優美細膩的設計，最適合送給甜美可愛的她，鑽石浪漫禮物推薦！', 1, 0, '2016-07-20 10:47:48', 0, 34, 15),
(21, '海尔四开门冰箱 BCD-620WDGF', '6999.00', '6699.00', '20.jpg', '冰箱冰柜品牌: Haier/海尔海尔冰箱型号: 全新正品 海尔四开门冰箱BCD-620WDGF 620立升冰箱总容量范围: >600升智能类型: 其他智能采购地: 中国大陆制冷方式: 风冷箱门结构: 多门式面板类型: 钢化玻璃面板能效等级: 一级颜色分类: BCD-620WDGF', 1, 0, '2016-07-20 10:49:30', 0, 30, 15),
(22, 'Samsung/三星 UA40JU5920CXXZ', '3399.00', '3199.00', '21.jpg', '证书编号：2015010808758923证书状态：有效申请人名称：三星电子株式会社制造商名称：天津三星电子有限公司产品名称：液晶彩色电视机 品牌: Samsung/三星 型号: UA40JU5920CXXZ分辨率: 3840x21603D类型: 无能效等级: 三级网络连接方式: 全部支持操作系统: 安卓', 1, 0, '2016-07-20 10:50:35', 0, 31, 15),
(23, 'Philips/飞利浦 55PUF6031/T3', '2999.00', '2699.00', '22.jpg', '证书编号：2014010808723913证书状态：有效产品名称：LED背光源液晶电视，LED背光源网络电视，LED背光源智能电视产品名称：Philips/飞利浦 55PUF603...品牌: Philips/飞利浦飞利浦LED型号: 55PUF6031/T3分辨率: 3840x21603D类型: 无能效等级: 二级网络连接方式: 无线连接操作系统: 安卓', 1, 0, '2016-07-20 10:51:57', 0, 31, 15),
(24, 'Hisense/海信 LED55EC520UA', '3049.00', '3000.00', '23.jpg', '证书编号：2015010808787658证书状态：有效申请人名称：青岛海信电器股份有限公司制造商名称：青岛海信电器股份有限公司产品名称：液晶电视3C产品型号：LED55EC520UA：220VAC 50Hz 170W产品名称：Hisense/海信 LED55EC520...品牌: Hisense/海信型号: LED55EC520UA分辨率: 3840x21603D类型: 无能效等级: 无网络连接方式: 全部支持操作系统: 安卓', 1, 0, '2016-07-20 10:52:58', 0, 31, 15),
(25, 'MIUI/小米 55英寸套装', '3699.00', '3199.00', '24.jpg', '证书编号：2015010808807283证书状态：有效申请人名称：北京小米电子产品有限公司制造商名称：北京小米电子产品有限公司产品名称：小米电视3C产品型号：L55M4-AA AC100-240W 50/60Hz 180W产品名称：MIUI/小米 小米电视2 55英...品牌: Xiaomi/小米型号: 小米电视2 55英寸分辨率: 3840x21603D类型: 无能效等级: 三级网络连接方式: 全部支持操作系统: MIUI TV', 1, 0, '2016-07-20 10:54:58', 0, 31, 15),
(26, 'Sony/索尼 KD-55X9000C', '9999.00', '9000.00', '25.jpg', '证书编号：2015010808769326证书状态：有效申请人名称：上海索广映像有限公司制造商名称：上海索广映像有限公司产品名称：电视机3C产品型号：KD-55X9000C ：220VAC 50Hz 241W产品名称：Sony/索尼 KD-55X9000C品牌: Sony/索尼索尼LED型号: KD-55X9000C分辨率: 3840x21603D类型: 偏光式3D能效等级: 三级网络连接方式: 全部支持操作系统: 安卓', 1, 0, '2016-07-20 10:56:21', 0, 31, 15),
(27, 'Samsung/三星 WD80J6413AW', '4299.00', '4099.00', '26.jpg', '证书编号：2014010705746604证书状态：有效申请人名称：苏州三星电子有限公司制造商名称：苏州三星电子有限公司产品名称：全自动滚筒洗衣机3C产品型号：WW80J6413CW(XQG80-80J6413CW), WW80J6410CX(XQG80-80...产品名称：Samsung/三星 WD80J6413A...洗衣机品牌: Samsung/三星三星洗衣机型号: WD80J6413AW(XQG80-80J6413AW))产品类型: 洗烘一体机使用方式: 全自动洗衣程序: 精细织物 衬衫,内衣,窗帘,护肤,羽绒服 羊毛洗 大件洗 化纤洗 棉麻洗 快洗 预洗 单漂 单甩 强力洗 牛仔洗 标准洗 筒自洁能效等级: 一级电机类型: 变频电机', 1, 0, '2016-07-20 10:57:39', 0, 32, 15),
(28, 'SIEMENS/西门子 XQG80-WM12N1C80W', '3999.00', '3599.00', '27.jpg', '证书编号：2015010705784184证书状态：有效申请人名称：博西威家用电器有限公司制造商名称：博西威家用电器有限公司产品名称：全自动滚筒式洗衣机3C产品型号：XQG70-WM10N0600W, XQG70-WM10N0R80W, XQG70-WM10N0C8...产品名称：SIEMENS/西门子 XQG80-W...洗衣机品牌: SIEMENS/西门子型号: XQG80-WM12N1C80W产品类型: 滚筒洗衣机使用方式: 全自动洗衣程序: 衬衫,内衣,窗帘,护肤,羽绒服 防过敏洗 羽绒服洗、羊毛洗、混合洗 羊毛洗 大件洗 化纤洗 棉麻洗 快洗 预洗 单漂 单排 真丝洗 牛仔洗 抗菌洗 筒自洁能效等级: 一级电机类型: 变频电机', 1, 0, '2016-07-20 10:58:36', 0, 32, 15),
(29, 'LG WD-HH2430D', '2299.00', '2099.00', '28.jpg', '证书编号：2015010705764495证书状态：有效申请人名称：南京乐金熊猫电器有限公司制造商名称：南京乐金熊猫电器有限公司产品名称：全自动滚筒洗衣机3C产品型号：WD-T14415D, WD-T12415D, WD-T14410DM, WD-T14410DL, ...产品名称：LG WD-HH2430D洗衣机品牌: LG型号: WD-HH2430D产品类型: 滚筒洗衣机使用方式: 全自动洗衣程序: 羊毛洗 大件洗 化纤洗 棉麻洗 快洗 强力洗 筒自洁能效等级: 一级电机类型: DD变频直驱电机', 1, 0, '2016-07-20 11:00:27', 0, 32, 15),
(30, 'TCL XQG80-F12102TB', '1699.00', '1399.00', '29.jpg', '证书编号：2015010705776204证书状态：有效产品名称：滚筒式全自动洗衣机产品名称：TCL XQG80-F12102TB洗衣机品牌: TCL型号: XQG80-F12102TB产品类型: 滚筒洗衣机使用方式: 全自动洗衣程序: 羊毛洗 化纤洗 棉麻洗 快洗 单甩 强力洗 筒自洁能效等级: 一级电机类型: 变频电机', 1, 0, '2016-07-20 11:01:39', 0, 32, 15),
(31, 'Bosch/博世 XQG80-WDG244601W', '5590.00', '5490.00', '30.jpg', '证书编号：2014010705729421证书状态：有效申请人名称：博西华电器(江苏)有限公司制造商名称：博西华电器(江苏)有限公司产品名称：全自动滚筒式洗衣干衣机3C产品型号：XQG80-WDG244601W, XQG80-WDG244681W, 220V～ 50Hz 洗涤/...产品名称：Bosch/博世 XQG80-WDG24...洗衣机品牌: Bosch/博世型号: XQG80-WDG244601W产品类型: 洗烘一体机使用方式: 全自动洗衣程序: 羊毛洗 棉麻洗 快洗 单漂 烘干 抗菌洗能效等级: 一级电机类型: 变频电机', 1, 0, '2016-07-20 11:02:43', 0, 32, 15),
(32, '七匹狼夹克 秋装新款中年男士翻领茄克衫外套jacket', '439.00', '409.00', '31.jpg', '材质成分：聚酯纤维100%货号：111510101432销售渠道类型：商场同款(线上线下都销售)面料分类：涤纶品牌：Septwolves/七匹狼厚薄：常规基础风格：商务绅士', 1, 0, '2016-07-20 11:04:26', 0, 33, 16),
(33, '太平鸟男装 新款青年薄外套韩版潮流飞行员夹克男BWBC63202', '439.00', '409.00', '32.jpg', '材质成分：聚酯纤维100%货号：BWBC63202销售渠道类型：纯电商(只在线上销售)面料分类：涤纶品牌：PEACEBIRD/太平鸟厚薄：常规基础风格：时尚都市', 1, 1, '2016-07-20 11:06:02', 0, 33, 16),
(34, '劲霸男装 夹克外套BKDU1120', '599.00', '499.00', '33.jpg', '货号：BKDU1120品牌：K-boxing/劲霸厚薄：常规基础风格：时尚都市  领型：立领  版型：修身  下摆设计：本布下摆', 1, 1, '2016-07-20 11:07:22', 0, 33, 16),
(35, '柒牌 商务休闲男茄克703K2662', '169.00', '149.00', '34.jpg', '材质成分：聚酯纤维100%货号：703K2662面料分类：涤纶品牌：seven7/柒牌厚薄：常规基础风格：时尚都市', 1, 0, '2016-07-20 11:08:38', 0, 33, 16),
(36, 'JackJones杰克琼 夹克外套S|216121074', '799.00', '769.00', '35.jpg', '材质成分：粘胶纤维(粘纤)69% 聚酯纤维13% 棉12% 金属纤维6%货号：216121074销售渠道类型：商场同款(线上线下都销售)面料分类：PU皮品牌：Jack Jones/杰克琼斯厚薄：常规基础风格：时尚都市', 1, 0, '2016-07-20 11:09:51', 0, 33, 16),
(37, 'ZARA 女装 宽松长裤 02479149401', '139.00', '109.00', '36.jpg', '材质成分: 聚酯纤维100%裤长: 长裤销售 货号: 02479149401-20女裤裤型: 阔腿裤女裤腰高: 自然腰颜色分类: 蓝色品牌: ZARA尺寸: XS (160/62A) S (165/66A) M (170/70A) L (175/78A)服装款式细节: 印染厚薄: 常规', 1, 0, '2016-07-20 11:12:04', 0, 34, 16),
(38, '乐町 新款女装潮破洞短裤', '139.00', '109.00', '37.jpg', '材质成分: 棉98.5% 聚氨酯弹性纤维(氨纶)1.5%裤长: 短裤 货号: CWGC61651女裤裤型: 直筒裤女裤腰高: 高腰面料: 棉布风格: 甜美甜美: 日系颜色分类: 白色品牌: 乐町尺寸: 155/S 160/M 165/L成分含量: 96%及以上服装款式细节: 手工磨破厚薄: 常规', 1, 0, '2016-07-20 11:13:03', 0, 34, 16),
(39, '无印良品 MUJI', '149.00', '119.00', '38.jpg', '材质成分: 亚麻100%裤长: 七分裤 货号: W6SE432女裤裤型: 直筒裤女裤 腰高: 自然腰 颜色分类: 浅灰色 生成色 卡其绿 深蓝色 品牌: MUJI/无印良品 尺寸: S M L', 1, 0, '2016-07-20 11:14:48', 0, 34, 16),
(40, 'Vero Moda 雪纺吊带九分阔腿连体裤|316144024', '349.50', '300.00', '39.jpg', '材质成分: 聚酯纤维100%裤长: 九分裤货号: 316144024女裤裤型: 阔腿裤女裤腰高: 自然腰面料: 其他风格: 通勤通勤: OL风格颜色分类: 010黑 023本白 070红品牌: Vero Moda尺寸: 155/60A/XSR 160/64A/SR 165/68A/MR 170/72A/LR 175/76A/XLR 180/80A/XXLR成分含量: 96%及以上厚薄: 常规', 1, 0, '2016-07-20 11:15:57', 0, 34, 16),
(41, 'Amii[极简主义]休闲短裤女11670440', '149.00', '129.00', '40.jpg', '材质成分: 聚酯纤维100%裤长: 短裤货号: 11670440女裤裤型: 直筒裤女裤腰高: 高腰风格: 通勤通勤: 简约颜色分类: 米白 深蓝 黑色品牌: Amii尺寸: XS S M L XL XXL XXXL成分含量: 96%及以上厚薄: 常规', 1, 0, '2016-07-20 11:17:06', 2, 34, 16),
(42, '齐齐熊 宝宝背心套装', '32.00', '29.00', '41.jpg', '品牌: CICIIBEAR/齐齐熊安全等级: 其他材质成分: 棉100%货号: QQ1668适用性别: 中性颜色分类: 每日前200名包邮！ 1668鸽子粉 1668鸽子蓝 1051小马白色 1751汽车白 1751汽车黄参考身高: 66cm(6M参考身高56-62cm) 73cm(12M参考身高64-70cm) 80cm(18M参考身高72-78cm) 90cm(24M参考身高80-86cm) 100cm(36M参考身高88-94cm) 110cm(48M参考身高96-104cm) 120cm(60M参考身高106-114cm)模特实拍: 实拍有模特适用场景: 爱意表达按关系送礼: 孩子是否带帽子: 无组合形式: 无袖+裤子面料: 纯棉(95%及以上)厚薄: 常规适用季节: 夏季风格: 其他衣门襟: 套头图案: 卡通动漫件数: 2件', 1, 1, '2016-07-20 11:18:48', 0, 35, 16),
(43, '优贝宜 短袖T恤套装', '36.80', '30.00', '42.jpg', '品牌: Yobeyi/优贝宜安全等级: A类材质成分: 棉96% 聚氨酯弹性纤维(氨纶)4%货号: Y15282101适用性别: 中性颜色分类: 条纹猫头 围巾狗 面具 卡通大眼镜 卡通队长 高帽先生 小小熊 雪糕 小象灰 爆米花 熊 胡子 英文参考身高: 73cm 80cm 90cm 100cm 110cm 120cm 130cm 140cm 150cm 160cm 165cm模特实拍: 实拍无模特适用场景: 爱意表达按关系送礼: 孩子是否带帽子: 无组合形式: 其他面料: 纯棉(95%及以上)厚薄: 薄款适用季节: 夏季风格: 休闲衣门襟: 套头图案: 卡通动漫件数: 2件', 1, 1, '2016-07-20 11:20:07', 0, 35, 16),
(44, 'TAGA儿童运动套装潮圆领2件套', '69.90', '69.90', '43.jpg', '品牌: TAGA安全等级: B类材质成分: 棉95% 聚氨酯弹性纤维(氨纶)5%货号: TG2K0745适用性别: 男颜色分类: 花灰0745 浅蓝0745 米白0732 花灰0732 浅花灰0761 浅蓝0734 花灰0734 阳光黄0745 阳光黄0734 米白色0734 米白0761参考身高: 100cm【2016夏款主打套装上市】 110cm【夏季新品时尚印花潮流百搭】 120cm【多重款式尽情挑选】 130cm【圆领纯棉套装 一套搞定所有】 140cm【 特色印染技术 印花不脱落不掉色】 150cm【 购买搭配套餐更划算更实惠】 160cm【主打套装库存限量务必抓紧购买】模特实拍: 实拍无模特适用场景: 爱意表达按关系送礼: 孩子是否带帽子: 有帽可拆组合形式: 短袖+裤子面料: 纯棉(95%及以上)厚薄: 薄款适用季节: 夏季风格: 休闲衣门襟: 套头图案: 卡通动漫件数: 2件', 0, 1, '2016-07-20 11:21:19', 0, 35, 16),
(45, '安塞尔斯童装T恤套装', '69.00', '49.00', '44.jpg', '品牌: Ansel’s/安塞尔斯安全等级: A类材质成分: 棉100%货号: 1162070适用性别: 男颜色分类: 大红色 米白色（运动熊） 深橙红（数字） 米白色（时尚熊） 米白色 大红色（斑点） 大红色（萌猫） 深橙红 玻璃蓝 米白色（宝贝熊） 嫩绿色 法国蓝（萌猫） 考拉灰色 花灰色 深橙红（字母） 苹果绿萌飞熊 苹果绿创意熊 法国蓝 玻璃蓝（卡通） 大红色（卡通） 花灰色（字母熊） 米白色（字母熊） 米白色（潮萌熊） 大红色（可爱熊）参考身高: 73cm 80cm 90cm 100cm 110cm 120cm模特实拍: 实拍无模特适用场景: 上学送礼按关系送礼: 孩子是否带帽子: 无组合形式: 短袖+裤子面料: 纯棉(95%及以上)厚薄: 常规适用季节: 夏季风格: 休闲衣门襟: 套头图案: 卡通动漫件数: 2件', 1, 0, '2016-07-20 11:25:22', 0, 35, 16),
(46, '莫伊儿短袖儿童套装', '19.90', '9.90', '45.jpg', '品牌: 莫伊儿货号: N-104适用性别: 男颜色分类: 学校套装兰 学校套装绿 1拉绿色 1拉兰色 1拉桔色 海军AI 藏青 小鸭子兰色 米姥鼠 YZ绿色 夏猫 卡通熊藏青 卡通熊红 羽毛藏青 羽毛红 大XX白色 迷彩灰 六角星绿 小黑帽绿色 PN兰 六角星兰 1拉白色 花袋白 W衬衫红 动物参考身高: 80码建议身高75CM以内 90码建议身高85CM以内 100码建议身高85-95CM 110码建议身高95-105CM 120码建议身高105-115CM是否带帽子: 无组合形式: 短袖+裤子面料: 棉混纺布厚薄: 常规适用季节: 春秋风格: 运动衣门襟: 套头图案: 格子件数: 2件', 1, 0, '2016-07-20 11:27:00', 0, 35, 16),
(47, 'Razer/雷蛇 灵刃潜行版 RZ09-01682E22', '13499.00', '13000.00', '46.jpg', '证书编号：2015010902812387证书状态：有效申请人名称：Razer Inc.制造商名称：Razer Inc.产品名称：雷蛇灵刃潜行版 游戏笔记本电脑3C产品型号：RZ09-0168,RZ09-0184产品名称：Razer/雷蛇 灵刃潜行版 R...能效等级: 二级品牌: Razer/雷蛇型号: RZ09-01682E22屏幕尺寸: 12.5英寸CPU: Intel Core i7-6500U显卡类型: Intel HD Graphics 520显存容量: 共享内存容量机械硬盘容量: 无机械硬盘内存容量: 8GB操作系统: windows 10', 1, 1, '2016-07-20 11:28:23', 0, 36, 17),
(48, 'Dell/戴尔 灵越15(7559) Ins15P-2748', '7199.00', '7000.00', '47.jpg', '证书编号：2015010902785887证书状态：有效产品名称：便携式计算机产品名称：Dell/戴尔 灵越15(7559)...能效等级: 一级品牌: Dell/戴尔型号: Ins15P-2748屏幕尺寸: 15.6英寸CPU: Core/酷睿 i7显卡类型: GTX 960M 4GB GDDR5显存容量: 4GB机械硬盘容量: 1TB内存容量: 8GB操作系统: windows 10', 1, 0, '2016-07-20 11:29:16', 0, 36, 17),
(49, 'Asus/华硕 顽石4代', '5499.00', '5000.00', '48.jpg', '证书编号：2013010902601399证书状态：有效申请人名称：华硕电脑股份有限公司制造商名称：华硕电脑股份有限公司产品名称：笔记本电脑3C产品型号：见附件产品名称：Asus/华硕 顽石 顽石4代能效等级: 一级品牌: Asus/华硕型号: 顽石4代屏幕尺寸: 15.6英寸CPU: 第六代酷睿I7-6500U显卡类型: NVIDIA GeForce 940M显存容量: 2GB机械硬盘容量: 无机械硬盘内存容量: 4GB', 1, 0, '2016-07-20 11:30:20', 0, 36, 17),
(50, 'Apple/苹果 MacBook Pro MJLT2CH/A', '17588.00', '17588.00', '49.jpg', '证书编号：2012010902552763证书状态：有效申请人名称：美国苹果公司制造商名称：美国苹果公司产品名称：笔记型电脑3C产品型号：A1398：20VDC，4.25A（电源适配器（可选）:A1424）产品名称：Apple/苹果 MacBook Pro ...能效等级: 无品牌: Apple/苹果MacBook Pro系列型号: MJLT2CH/A屏幕尺寸: 15英寸CPU: Intel 酷睿i7 4870HQ显卡类型: AMD Radeon R9 M370X 配备 2GB GDD显存容量: 2GB机械硬盘容量: 无机械硬盘内存容量: 16G操作系统: Mac OS', 0, 1, '2016-07-20 11:31:28', 0, 36, 17),
(51, 'Lenovo/联想 YOGA710 -14ISK', '5499.00', '5499.00', '50.jpg', '证书编号：2014010902742663证书状态：有效申请人名称：联宝(合肥)电子科技有限公司制造商名称：联想(北京)有限公司产品名称：便携式计算机3C产品型号：Lenovo Yoga 3 14xxxx (x 代表0-9, a-z, A-Z, - 或空格,代表销...产品名称：Lenovo/联想 YOGA710 -1...能效等级: 一级品牌: Lenovo/联想型号: -14ISK屏幕尺寸: 14英寸CPU: Core/酷睿 i5 i5-6200U显卡类型: NVIDIA GeForce GT940MX显存容量: 2GB机械硬盘容量: 无机械硬盘内存容量: 4GB操作系统: windows 10', 0, 1, '2016-07-20 11:32:20', 8, 36, 17),
(52, '联想台式机电脑G50500I', '3299.00', '3299.00', '51.jpg', '证书编号：2012010902583758证书状态：有效申请人名称：联宝(合肥)电子科技有限公司制造商名称：联想(北京)有限公司产品名称：便携式计算机3C产品型号：见附件CPU类型: Core/酷睿 i5型号: I5-4460新圆梦系列型号: H5050 I5-4460...适用品牌: Intel/英特尔内存容量: 4GB内存类型: DDR3硬盘容量: 1TB显卡类型: 独立显卡屏幕尺寸: 无显示器显示器类型: 无显示器', 0, 1, '2016-07-20 11:34:09', 2, 36, 17),
(53, 'Dell/戴尔 I3650-1838', '5499.00', '5499.00', '52.jpg', 'CPU类型: Core/酷睿 i5型号: i5-6400内存容量: 8GB硬盘容量: 1TB显卡类型: 独立显卡显卡型号: NVIDIA GeForce 730 2GB GDDR3屏幕尺寸: 23英寸显示器类型: 其他/other', 0, 1, '2016-07-20 11:36:28', 0, 37, 17),
(54, 'Alienware 外星人 ALPHA R2 ALWAD-4728', '8999.00', '8999.00', '53.jpg', '产品名称：alienware ALWAD-4728CPU类型: Core/酷睿 i7型号: i7 6700T内存容量: 8GB内存类型: 其他/other硬盘容量: 其他/other显卡类型: 独立显卡显卡型号: NVIDIA GeForce GTX 960 GPU屏幕尺寸: 无显示器显示器类型: 无显示器操作系统: 其他/other', 0, 1, '2016-07-20 11:37:29', 1, 37, 17),
(55, '海尔电脑主机轰天雷X9', '3999.00', '3999.00', '54.jpg', '证书编号：2014010901684338证书状态：有效申请人名称：海尔信息科技(深圳)有限公司制造商名称：海尔信息科技(深圳)有限公司产品名称：微型计算机 产品名称：Haier/海尔 轰天雷X8-8G...CPU类型: Core/酷睿 i5型号: 4460适用品牌: Intel/英特尔台机Intel型号: 其他/other内存容量: 8GB内存类型: DDR3硬盘容量: 1T显卡类型: 独立显卡显卡型号: GTX950屏幕尺寸: 无显示器显示器类型: 无显示器操作系统: MS-DOS', 0, 1, '2016-07-20 11:38:45', 0, 37, 17),
(56, 'asus/华硕 G11', '5899.00', '5899.00', '55.jpg', '产品名称：Asus/华硕 G11CDCPU类型: Core/酷睿 i7型号: I7-6700适用品牌: 其他/other内存容量: 8GB内存类型: DDR3硬盘容量: 1T显卡类型: 独立显卡显卡型号: 其他/other屏幕尺寸: 无显示器显示器类型: 无显示器', 0, 1, '2016-07-20 11:39:52', 2, 37, 17),
(57, 'SNSIR/申士 Y207', '1298.00', '1298.00', '56.jpg', '产品名称：SNSIR/申士 Y207主机播放碟片格式: 无主机类型: 仅有功放无碟机毛重: 大约23KG视频连接方式: 无附加功能: AUX接口 USB接口 蓝牙连接 麦克风接口音效模式: Dolby Digital（AC-3）音箱箱体材质: 塑料音箱连接方式: 光纤传输 同轴传输颜色分类: 香槟色壁挂式5.1家庭影院 香槟色落地式5.1家庭影院品牌: SNSIR/申士型号: Y207声道数: 5.1是否DVD播放机: 不带DVD机', 0, 1, '2016-07-20 11:41:14', 2, 38, 17),
(58, 'Philips/飞利浦 HTB3581/93', '2699.00', '2699.00', '57.jpg', '产品名称：Philips/飞利浦 HTB3581/...主机播放碟片格式: CD DVD VCD 蓝光主机类型: 功放与碟机一体式毛重: 26.3kg视频连接方式: HDMI 混合Video附加功能: AUX接口 LAN网络接口 USB接口 收音机 麦克风接口音效模式: DTS Dolby Digital（AC-3） Dolby Pro Logic Dolby Pro Logic II PCM sdds音箱箱体材质: 塑料音箱连接方式: HDMI传输 光纤传输 同轴传输 模拟传输颜色分类: 黑色品牌: Philips/飞利浦飞利浦家庭影院型号: HTB3581/93声道数: 5.1款式: 音柱式是否DVD播放机: 带DVD机输出功率: 801W(含)-1000W(含) 最大输出功率: 1000W', 0, 1, '2016-07-20 11:42:31', 5, 38, 17),
(59, 'Yamaha/雅马哈 YHT-299', '2990.00', '2990.00', '58.jpg', '产品名称：Yamaha/雅马哈 YHT-299主机播放碟片格式: 无主机类型: 仅有功放无碟机毛重: 21kg视频连接方式: 无音效模式: DTS Dolby Pro Logic Dolby Pro Logic II音箱箱体材质: 塑料音箱连接方式: HDMI传输 光纤传输 同轴传输颜色分类: 黑色品牌: Yamaha/雅马哈型号: YHT-299声道数: 5.1款式: 卫星/迷你式是否DVD播放机: 不带DVD机输出功率: 601W(含)-800W(含) 最大输出功率: 675W', 0, 1, '2016-07-20 11:43:18', 73, 38, 17),
(60, 'JBL ARENA180/VSX-531', '10580.00', '10580.00', '59.jpg', '主机播放碟片格式: 无主机类型: 仅有功放无碟机堆码层数极限: 3层毛重: 约60KG视频连接方式: HDMI附加功能: USB接口 收音机 蓝牙连接音效模式: DTS Dolby Digital（AC-3）音箱箱体材质: 木颜色分类: 180影院+先锋531品牌: JBL型号: ARENA180/VSX-531声道数: 5.1款式: 古典是否DVD播放机: 不带DVD机输出功率: 801W(含)-1000W(含)', 0, 1, '2016-07-20 11:44:21', 48, 38, 17),
(61, 'Sony/索尼 BDV-N9200WL', '7038.00', '7038.00', '60.jpg', '产品名称：Sony/索尼 BDV-N9200WL主机播放碟片格式: CD DVD VCD 蓝光主机类型: 功放与碟机一体式堆码层数极限: 9层毛重: 28kg视频连接方式: HDMI附加功能: 2D转3D LAN网络接口 NFC USB接口 WIFI 收音机 蓝牙连接音效模式: DTS Dolby Digital（AC-3） Dolby Pro Logic Dolby Pro Logic II音箱箱体材质: 塑料音箱连接方式: 无线 模拟传输品牌: Sony/索尼索尼家庭影院型号: BDV-N9200WL声道数: 5.1款式: 音柱式是否DVD播放机: 带DVD机输出功率: 401W(含)-600W(含)售后服务: 全国联保', 0, 0, '2016-07-20 11:45:23', 16, 38, 17);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `goods`
--
ALTER TABLE `goods`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_goods_addtime` (`addtime`),
  ADD KEY `supercat_id` (`supercat_id`),
  ADD KEY `subcat_id` (`subcat_id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `goods`
--
ALTER TABLE `goods`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `goods`
--
ALTER TABLE `goods`
  ADD CONSTRAINT `goods_ibfk_1` FOREIGN KEY (`supercat_id`) REFERENCES `supercat` (`id`),
  ADD CONSTRAINT `goods_ibfk_2` FOREIGN KEY (`subcat_id`) REFERENCES `subcat` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

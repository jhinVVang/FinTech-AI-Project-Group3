
/* jBox 全局設置 */
var jBoxConfig = {};

jBoxConfig.defaults = {
    id: null, /* 在頁面中的唯一id，如果為null則自動生成隨機id,一個id只會顯示一個jBox */
    top: '15%', /* 窗口離頂部的距離,可以是百分比或像素(如 '100px') */
    border: 5, /* 窗口的外邊框像素大小,必須是0以上的整數 */
    opacity: 0.1, /* 窗口隔離層的透明度,如果設置為0,則不顯示隔離層 */
    timeout: 0, /* 窗口顯示多少毫秒後自動關閉,如果設置為0,則不自動關閉 */
    showType: 'fade', /* 窗口顯示的類型,可選值有:show、fade、slide */
    showSpeed: 'fast', /* 窗口顯示的速度,可選值有:'slow'、'fast'、表示毫秒的整數 */
    showIcon: true, /* 是否顯示窗口標題的圖標，true顯示，false不顯示，或自定義的CSS樣式類名（以為圖標為背景） */
    showClose: true, /* 是否顯示窗口右上角的關閉按鈕 */
    draggable: true, /* 是否可以拖動窗口 */
    dragLimit: true, /* 在可以拖動窗口的情況下，是否限制在可視範圍 */
    dragClone: false, /* 在可以拖動窗口的情況下，鼠標按下時窗口是否克隆窗口 */
    persistent: true, /* 在顯示隔離層的情況下，點擊隔離層時，是否堅持窗口不關閉 */
    showScrolling: true, /* 是否顯示瀏覽的滾動條 */
    ajaxData: {},  /* 在窗口內容使用get:或post:前綴標識的情況下，ajax post的數據，例如：{ id: 1 } 或 "id=1" */
    iframeScrolling: 'auto', /* 在窗口內容使用iframe:前綴標識的情況下，iframe的scrolling屬性值，可選值有：'auto'、'yes'、'no' */

    title: 'jBox', /* 窗口的標題 */
    width: 350, /* 窗口的寬度，值為'auto'或表示像素的整數 */
    height: 'auto', /* 窗口的高度，值為'auto'或表示像素的整數 */
    bottomText: '', /* 窗口的按鈕左邊的內容，當沒有按鈕時此設置無效 */
    buttons: { '確定': 'ok' }, /* 窗口的按鈕 */
    buttonsFocus: 0, /* 表示第幾個按鈕為默認按鈕，索引從0開始 */
    loaded: function (h) { }, /* 窗口加載完成後執行的函數，需要注意的是，如果是ajax或iframe也是要等加載完http請求才算窗口加載完成，參數h表示窗口內容的jQuery對象 */
    submit: function (v, h, f) { return true; }, /* 點擊窗口按鈕後的回調函數，返回true時表示關閉窗口，參數有三個，v表示所點的按鈕的返回值，h表示窗口內容的jQuery對象，f表示窗口內容里的form表單鍵值 */
    closed: function () { } /* 窗口關閉後執行的函數 */
};

jBoxConfig.stateDefaults = {
    content: '', /* 狀態的內容，不支持前綴標識 */
    buttons: { '確定': 'ok' }, /* 狀態的按鈕 */
    buttonsFocus: 0, /* 表示第幾個按鈕為默認按鈕，索引從0開始 */
    submit: function (v, h, f) { return true; } /* 點擊狀態按鈕後的回調函數，返回true時表示關閉窗口，參數有三個，v表示所點的按鈕的返回值，h表示窗口內容的jQuery對象，f表示窗口內容里的form表單鍵值 */
};

jBoxConfig.tipDefaults = {
    content: '', /* 提示的內容，不支持前綴標識 */
    icon: 'info', /* 提示的圖標，可選值有'info'、'success'、'warning'、'error'、'loading'，默認值為'info'，當為'loading'時，timeout值會被設置為0，表示不會自動關閉。 */
    top: '40%', /* 提示離頂部的距離,可以是百分比或像素(如 '100px') */
    width: 'auto', /* 提示的高度，值為'auto'或表示像素的整數 */
    height: 'auto', /* 提示的高度，值為'auto'或表示像素的整數 */
    opacity: 0, /* 窗口隔離層的透明度,如果設置為0,則不顯示隔離層 */
    timeout: 3000, /* 提示顯示多少毫秒後自動關閉,必須是大於0的整數 */
    loaded: function (h) { } /* 窗口加載完成後執行的函數，參數h表示窗口內容的jQuery對象 */
};

jBoxConfig.messagerDefaults = {
    content: '', /* 信息的內容，不支持前綴標識 */
    title: 'jBox', /* 信息的標題 */
    icon: 'none', /* 信息圖標，值為'none'時為不顯示圖標，可選值有'none'、'info'、'question'、'success'、'warning'、'error' */
    width: 350, /* 信息的高度，值為'auto'或表示像素的整數 */
    height: 'auto', /* 信息的高度，值為'auto'或表示像素的整數 */
    timeout: 3000, /* 信息顯示多少毫秒後自動關閉,如果設置為0,則不自動關閉 */
    showType: 'slide', /* 信息顯示的類型,可選值有:show、fade、slide */
    showSpeed: 600, /* 信息顯示的速度,可選值有:'slow'、'fast'、表示毫秒的整數 */
    border: 0, /* 信息的外邊框像素大小,必須是0以上的整數 */
    buttons: {}, /* 信息的按鈕 */
    buttonsFocus: 0, /* 表示第幾個按鈕為默認按鈕，索引從0開始 */
    loaded: function () { }, /* 窗口加載完成後執行的函數 */
    submit: function (v, h, f) { return true; }, /* 點擊信息按鈕後的回調函數，返回true時表示關閉窗口，參數有三個，v表示所點的按鈕的返回值，h表示窗口內容的jQuery對象，f表示窗口內容里的form表單鍵值 */
    loaded: function (h) { } /* 窗口加載完成後執行的函數，參數h表示窗口內容的jQuery對象 */
};

jBoxConfig.languageDefaults = {
    close: '關閉', /* 窗口右上角關閉按鈕提示 */
    ok: '確定', /* $.jBox.prompt() 系列方法的“確定”按鈕文字 */
    yes: '是', /* $.jBox.warning() 方法的“是”按鈕文字 */
    no: '否', /* $.jBox.warning() 方法的“否”按鈕文字 */
    cancel: '取消' /* $.jBox.confirm() 和 $.jBox.warning() 方法的“取消”按鈕文字 */
};

$.jBox.setDefaults(jBoxConfig);

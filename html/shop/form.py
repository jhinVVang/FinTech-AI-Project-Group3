from wtforms.validators import DataRequired, Email, Regexp, \
    EqualTo, ValidationError, Length
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
    TextAreaField, RadioField, DecimalField, SelectField

from model import *


class RegisterForm(FlaskForm):
    """
    用戶註冊表單
    """
    username = StringField(
        label="帳戶 ：",
        validators=[
            DataRequired("用戶名不能為空！"),
            Length(min=3, max=50, message="用戶名長度必須在3到10位之間")
        ],
        description="用戶名",
        render_kw={
            "type": "text",
            "placeholder": "請輸入用戶名！",
            "class": "validate-username",
            "size": 38,
        }
    )
    email = StringField(
        label="郵箱 ：",
        validators=[
            DataRequired("郵箱不能為空！"),
            Email("郵箱格式不正確！")
        ],
        description="郵箱",
        render_kw={
            "type": "email",
            "placeholder": "請輸入郵箱！",
            "size": 38,
        }
    )
    password = PasswordField(
        label="密碼 ：",
        validators=[
            DataRequired("密碼不能為空！")
        ],
        description="密碼",
        render_kw={
            "placeholder": "請輸入密碼！",
            "size": 38,
        }
    )
    repassword = PasswordField(
        label="確認密碼 ：",
        validators=[
            DataRequired("請輸入確認密碼！"),
            EqualTo('password', message="兩次密碼不一致！")
        ],
        description="確認密碼",
        render_kw={
            "placeholder": "請輸入確認密碼！",
            "size": 38,
        }
    )
    submit = SubmitField(
        '同意協議並註冊',
        render_kw={
            "class": "btn btn-primary login",
        }
    )

    def validate_email(self, field):
        """
        檢測註冊郵箱是否已經存在
        :param field: 字段名
        """
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError("郵箱已經存在！")

class LoginForm(FlaskForm):
    """
    登錄功能
    """
    username = StringField(
        validators=[
            DataRequired("用戶名不能為空！"),
            Length(min=3, max=50, message="用戶名長度必須在3到10位之間")
        ],
        description="用戶名",
        render_kw={
            "type": "text",
            "placeholder": "請輸入用戶名！",
            "class": "validate-username",
            "size": 38,
            "maxlength": 99
        }
    )
    password = PasswordField(
        validators=[
            DataRequired("密碼不能為空！"),
            Length(min=3, message="密碼長度不少於6位")
        ],
        description="密碼",
        render_kw={
            "type": "password",
            "placeholder": "請輸入密碼！",
            "class": "validate-password",
            "size": 38,
            "maxlength": 99
        }
    )
    verify_code = StringField(
        'VerifyCode',
        validators=[DataRequired()],
        render_kw={
            "class": "validate-code",
            "size": 18,
            "maxlength": 4,
        }
    )

    submit = SubmitField(
        '登錄',
        render_kw={
            "class": "btn btn-primary login",
        }
    )


class PasswordForm(FlaskForm):
    """
     修改密碼表單
     """
    old_password = PasswordField(
        label="原始密碼 ：",
        validators=[
            DataRequired("原始密碼不能為空！")
        ],
        description="原始密碼",
        render_kw={
            "placeholder": "請輸入原始密碼！",
            "size": 38,
        }
    )
    password = PasswordField(
        label="新密碼 ：",
        validators=[
            DataRequired("新密碼不能為空！")
        ],
        description="新密碼",
        render_kw={
            "placeholder": "請輸入新密碼！",
            "size": 38,
        }
    )
    repassword = PasswordField(
        label="確認密碼 ：",
        validators=[
            DataRequired("請輸入確認密碼！"),
            EqualTo('password', message="兩次密碼不一致！")
        ],
        description="確認密碼",
        render_kw={
            "placeholder": "請輸入確認密碼！",
            "size": 38,
        }
    )
    submit = SubmitField(
        '確認修改',
        render_kw={
            "class": "btn btn-primary login",
        }
    )

    def validate_old_password(self, field):
        from flask import session
        old_password = field.data
        user_id = session["user_id"]
        user = User.query.get(int(user_id))
        if not user.check_password(old_password):
            raise ValidationError("原始密碼錯誤！")


class SuggetionForm(FlaskForm):
    """
    意見建議
    """
    name = StringField(
        label="姓名",
        validators=[
            DataRequired("姓名不能為空！")
        ],
        description="姓名",
        render_kw={
            "placeholder": "請輸入姓名！",
            "class": "form-control"
        }
    )
    email = StringField(
        label="郵箱",
        validators=[
            DataRequired("郵箱不能為空！")
        ],
        description="郵箱",
        render_kw={
            "type": "email",
            "placeholder": "請輸入郵箱！",
            "class": "form-control"
        }
    )
    content = TextAreaField(
        label="意見建議",
        validators=[
            DataRequired("內容不能為空！")
        ],
        description="意見建議",
        render_kw={
            "class": "form-control",
            "placeholder": "請輸入內容！",
            "rows": 7
        }
    )
    submit = SubmitField(
        '發送消息',
        render_kw={
            "class": "btn-default btn-cf-submit",
        }
    )


class MLoginForm(FlaskForm):
    """
    管理員登錄表單
    """
    manager = StringField(
        label="管理員名",
        validators=[
            DataRequired("管理員名不能為空")
        ],
        description="管理員名",
        render_kw={
            "class": "manager",
            "placeholder": "請輸入管理員名！",
        }
    )
    password = PasswordField(
        label="密碼",
        validators=[
            DataRequired("密碼不能為空")
        ],
        description="密碼",
        render_kw={
            "class": "password",
            "placeholder": "請輸入密碼！",
        }
    )
    submit = SubmitField(
        '登錄',
        render_kw={
            "class": "login_ok",
        }
    )

    # 驗證帳號，命名規則：validate_ + 字段名。如果要驗證密碼，則可以創建函數validate_pwd
    def validate_manager(self, field):
        account = field.data
        admin = Admin.query.filter_by(manager=account).count()
        if admin == 0:
            raise ValidationError("帳號不存在! ")


class GoodsForm(FlaskForm):
    name = StringField(
        label="商品名稱",
        validators=[
            DataRequired("商品名稱不能為空！"),
        ],
        description="商品名稱",
        render_kw={
            "class": "Sytle_text",
            "placeholder": "請輸入商品名稱！",
            "size": "50"
        }
    )
    supercat_id = SelectField(
        label="大分類",
        validators=[
            DataRequired("請選擇大分類！")
        ],
        coerce=int,
        description="大分類",
        render_kw={
            "class": "form-control",
        }
    )

    subcat_id = SelectField(
        label="小分類",
        validators=[
            DataRequired("請選擇小分類！")
        ],
        coerce=int,
        description="小分類",
        render_kw={
            "class": "form-control",
        }
    )
    picture = StringField(
        label="圖片名稱",
        validators=[
            DataRequired("圖片名稱不能為空！")
        ],
        description="圖片名稱",
        render_kw={
            "class": "Style_upload",
            "placeholder": "請輸入圖片名稱！"
        }
    )
    original_price = DecimalField(
        label="商品價格",
        validators=[
            DataRequired("請輸入正確的價格類型")
        ],
        description="商品價格",
        render_kw={
            "class": "Sytle_text",
            "placeholder": "請輸入商品價格！"
        }
    )
    current_price = DecimalField(
        label="商品特價",
        validators=[
            DataRequired("商品特價不能為空！")
        ],
        description="商品特價",
        render_kw={
            "class": "Sytle_text",
            "placeholder": "請輸入商品特價！"
        }
    )
    is_new = RadioField(
        label='是否新品',
        description="是否新品",
        coerce=int,
        choices=[(0, '否'), (1, '是')], default=0,
        render_kw={
            "class": "is_radio"
        }
    )
    is_sale = RadioField(
        label='是否特價',
        description="是否特價",
        coerce=int,
        choices=[(0, '否'), (1, '是')], default=0,
        render_kw={
            "class": "is_radio"
        }
    )
    introduction = TextAreaField(
        label=" 商品簡介",
        validators=[
            DataRequired(" 商品簡介不能為空！")
        ],
        description=" 商品簡介",
        render_kw={
            "class": "textarea",
            "rows": 5
        }
    )
    submit = SubmitField(
        '保存',
        render_kw={
            "class": "btn_bg_short",
        }
    )
